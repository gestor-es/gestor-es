"""Turn an official AEAT «diseño de registro» workbook into gestor/dr/<name>.json (positions, lengths, types, constants, casillas).

Dev-only, run when AEAT publishes a new DR:
    soffice --headless --convert-to xlsx DR130e15v12.xls        # old .xls only
    python3 scripts/dr_extract.py DR303e26v101.xlsx gestor/dr/303-2026.json --url <official url>
The app never reads the workbook; it reads the JSON. Stdlib only.
"""
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
CONST = re.compile(r'^(?:Constante\s*)?"([^"]*)"(?:\.?\s*Nota \d+\.?)?\.?$')
BOX = re.compile(r"\[\s*(\d{2,3})\s*\]")
OWN = re.compile(r"[^\]\s] - \[\s*(\d{2,3})\s*\]")  # 130: «Directa - [03] … ([01] - [02])»; else (303) the last one


def sheets(path):
    z = zipfile.ZipFile(path)
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            ss.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    for sh in wb.find("m:sheets", NS):
        t = rels[sh.get("{%s}id" % NS["r"])].lstrip("/")
        rows = []
        for row in ET.fromstring(z.read(t if t.startswith("xl/") else "xl/" + t)).iter("{%s}row" % NS["m"]):
            cells = {}
            for c in row.findall("m:c", NS):
                v = c.find("m:v", NS)
                if v is None:
                    is_ = c.find("m:is", NS)
                    val = "".join(x.text or "" for x in is_.iter("{%s}t" % NS["m"])) if is_ is not None else ""
                else:
                    val = ss[int(v.text)] if c.get("t") == "s" else v.text
                cells[re.match(r"[A-Z]+", c.get("r")).group()] = re.sub(r"\s+", " ", val).strip()
            rows.append(cells)
        yield sh.get("name"), rows


def page(rows):
    head = next((r for r in rows if any(v.startswith("Posic") for v in r.values())), None)
    if not head:
        return None
    col = {k: c for c, v in head.items() for k in ("Posic", "Lon", "Tipo", "Contenido") if v.startswith(k)}
    order = sorted(head)
    cand = [c for c in order if c not in col.values() and head[c] not in ("Nº", "Validación", "Com.")]
    desc_col = cand[-1] if cand else None
    fields, total = [], None
    for r in rows:
        pos, ln = r.get(col["Posic"], ""), r.get(col["Lon"], "")
        if r.get(order[0], "").upper().startswith("TOTAL") or r.get(col["Posic"], "").upper().startswith("TOTAL"):
            total = int(float(ln)) if ln.replace(".", "").isdigit() else total
            continue
        if not (pos.replace(".0", "").isdigit() and ln.replace(".0", "").isdigit()):
            continue
        content = r.get(col.get("Contenido", ""), "")
        desc = r.get(desc_col, "") if desc_col else ""
        m, boxes, own = CONST.match(content), BOX.findall(desc), OWN.search(desc)
        fields.append({"pos": int(float(pos)), "len": int(float(ln)), "type": r.get(col["Tipo"], ""), "desc": desc,
                       "const": m.group(1) if m else None, "content": content,
                       "box": own.group(1) if own else (boxes[-1] if boxes else None)})
    if not fields:
        return None
    end = max(f["pos"] + f["len"] - 1 for f in fields)
    return {"length": end, "declared_length": total, "fields": fields}


def main(src, out, url):
    spec = {"source": url, "file": src.rsplit("/", 1)[-1], "pages": {}}
    for name, rows in sheets(src):
        p = page(rows)
        if p:
            spec["pages"][name] = p
    with open(out, "w") as f:
        json.dump(spec, f, ensure_ascii=False, indent=1)
    for n, p in spec["pages"].items():
        print(n, p["length"], p["declared_length"], len(p["fields"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[sys.argv.index("--url") + 1] if "--url" in sys.argv else "")
