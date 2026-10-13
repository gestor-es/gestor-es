"""Files for «Importar» in the AEAT Sede forms, built from the official «diseños de registro» (gestor/dr/*.json).

The JSON specs are extracted by scripts/dr_extract.py from the AEAT workbooks; positions, lengths, types and constants
come from there, never typed by hand (the 349 has only a PDF, see file_349). A file is fixed-width ISO-8859-1 text.
Importing a file is not filing: the user still validates, signs and keeps the justificante.
"""
import json
import re
import unicodedata
from pathlib import Path

from .i18n import _
from .rules import EU
from .tax import region_for_year

DR = Path(__file__).parent / "dr"
PROGRAM = "0100"  # «Versión del programa» in <AUX>


def spec(name: str) -> dict:
    return json.loads((DR / f"{name}.json").read_text())


def latin(text: str) -> str:
    """DR text fields: upper case, letters/digits/blanks, no accents except Ñ and Ç; punctuation becomes a blank.
    Empty when a letter has no Latin form (Cyrillic, also Ł/Ø): the Sede then asks for the name instead of a garbled one."""
    out = []
    for ch in (text or "").upper():
        if ch in "ÑÇ":
            out.append(ch)
            continue
        base = unicodedata.normalize("NFD", ch)[0]
        if base.isascii() and base.isalnum():
            out.append(base)
        elif base.isalpha():
            return ""
        else:
            out.append(" ")
    return re.sub(r" +", " ", "".join(out)).strip()


def nif(s: dict) -> str:
    return re.sub(r"[^A-Z0-9]", "", (s.get("tax_id") or "").upper())


def field(f: dict, value) -> str:
    """One field to its exact width. value: int = cents (Num/N) or number; str = text/code; None = default fill."""
    width, kind = f["len"], f["type"]
    if f["const"] is not None:
        return f["const"].ljust(width)[:width] if len(f["const"]) <= width else _overflow(f, f["const"])
    if value is None:
        return ("0" if kind in ("Num", "N") else " ") * width
    if isinstance(value, str):
        if kind in ("Num", "N") and value.strip() == "":
            return " " * width  # DR allows a blank in some numeric flags (e.g. 303 prorrata outside the last period)
        if kind in ("Num", "N"):
            if not value.isdigit():
                raise ValueError(_("{field}: «{value}» не число").format(field=f["desc"], value=value))
            return value.rjust(width, "0") if len(value) <= width else _overflow(f, value)
        return value.ljust(width) if len(value) <= width else _overflow(f, value)
    if kind not in ("Num", "N"):
        raise ValueError(_("{field}: число в текстовом поле").format(field=f["desc"]))
    if value < 0:
        if kind != "N":
            raise ValueError(_("{field}: отрицательное значение в поле без знака").format(field=f["desc"]))
        digits = str(-value)
        return "N" + digits.rjust(width - 1, "0") if len(digits) < width else _overflow(f, value)
    digits = str(value)
    return digits.rjust(width, "0") if len(digits) <= width else _overflow(f, value)


def _overflow(f, value):
    raise ValueError(_("{field}: «{value}» не помещается в {width} знаков").format(field=f["desc"], value=value, width=f["len"]))


def record(page: dict, values: dict) -> str:
    """values keyed by casilla ('27') or by position (int) for fields without a casilla or with a repeated one."""
    out = []
    for f in sorted(page["fields"], key=lambda x: x["pos"]):
        v = values.get(f["pos"], values.get(f["box"]) if f["box"] else None)
        out.append(field(f, v))
    rec = "".join(out)
    if len(rec) != page["length"]:
        raise ValueError(_("запись {length} знаков вместо {expected}").format(length=len(rec), expected=page["length"]))
    return rec


def wrap(modelo: str, year: int, period: str, nif: str, pages: list[str]) -> bytes:
    head = f"<T{modelo}0{year}{period}0000><AUX>{' ' * 70}{PROGRAM}{' ' * 4}{nif.ljust(9)[:9]}{' ' * 213}</AUX>"
    return (head + "".join(pages) + f"</T{modelo}0{year}{period}0000>").encode("iso-8859-1")


SEPA_NON_EU = {"GB", "CH", "NO", "IS", "LI", "MC", "SM", "AD", "VA"}


def refund_account(s: dict) -> tuple[str, str]:
    """IBAN and the DID «Marca SEPA»: 1 Spain, 2 other SEPA, 3 rest of the world (DR303 Nota 2)."""
    iban = re.sub(r"[^A-Z0-9]", "", (s.get("iban") or "").upper())
    return iban, "0" if not iban else "1" if iban[:2] == "ES" else "2" if iban[:2] in EU | SEPA_NON_EU else "3"


# ---------- 130 ----------

def file_130(s: dict, f: dict) -> bytes:
    page = spec("130")["pages"]["DR 13001"]
    box = {b[0]: b[2] for b in f["boxes"]}
    q, r = f["period"], f["result"]
    kind = "I" if r > 0 else ("B" if r < 0 and q != "4T" else "N")
    values = {k: box.get(k, 0) for k in (f"{i:02d}" for i in range(1, 20))}
    values["17"] = values["14"] - values["15"] - values["16"]  # Total; the engine shows only [19] = [17] − [18], [18] = 0
    # Sede checks identity against the signer's census entry; «Apellidos, Nombre» splits, otherwise all goes to apellidos
    last, __, first = s.get("name", "").partition(",")
    values.update({13: kind, 14: nif(s), 23: latin(last), 83: latin(first), 103: str(f["year"]), 107: q})
    return wrap("130", f["year"], q, nif(s), [record(page, values)])


# ---------- 303 ----------

def file_303(s: dict, f: dict) -> bytes:
    if f["year"] != DR303_YEAR:
        raise ValueError(_("формат 303 есть только для {year} года; для {other} нужен свой diseño de registro")
                         .format(year=DR303_YEAR, other=f["year"]))
    pages = spec(f"303-{DR303_YEAR}")["pages"]
    c, q = dict(f["c"]), f["period"]
    last = q == "4T"
    r = c.get("71", 0)
    kind = "I" if r > 0 else "N" if r == 0 else ("D" if last and not f["carry_out"] else "C")
    p1 = dict(c)  # page 1 and page 3 take casillas by number; positions (flags) are per page and may collide
    p1.update({13: kind, 14: nif(s), 23: latin(s.get("name", "")), 103: str(f["year"]), 107: q,
               109: "2", 110: "2", 111: "3", 112: "2", 113: "2", 114: "2",           # flags: common territory, RG only
               115: "2" if last else " ", 116: "2" if last else " ",                 # prorrata especial (Nota 6)
               117: "2", 127: "2", 128: "2" if last else "0", 129: "0", 130: "0"})   # concurso, SII, 390, volumen, gasóleo
    p3 = {**c, "65": "10000",                                                        # 100 % atribuible al Estado
          425: "X" if not any(c.values()) else " "}                                  # sin actividad
    iban, sepa = refund_account(s) if kind == "D" else ("", "0")                     # DID only for a refund
    recs = [record(pages["DP30301"], p1), record(pages["DP30303"], p3), record(pages["DP303DID"], {23: iban, 194: sepa})]
    return wrap("303", f["year"], q, nif(s), recs)


# ---------- 349 ----------
# No workbook for the 349: positions from the AEAT «Anexo» PDF (DR_Anexo_349.pdf, registro tipo 1 + tipo 2 operador,
# 500 bytes each). Rectification records (tipo 2 rectificaciones) are not built: the engine has no per-period link yet.

def file_349(s: dict, f: dict) -> bytes:
    name, decl, y, q = latin(s.get("name", ""))[:40], nif(s).rjust(9, "0"), f["year"], f["period"]
    if len(decl) != 9:
        raise ValueError(_("NIF/NIE в настройках длиннее 9 знаков"))
    if not name:
        raise ValueError(_("Для 349 нужно имя латиницей, как в NIE: «Apellidos, Nombre» в настройках"))
    ops = []
    for clave, vat_id, country, who, base in f["ops"]:
        vat_id = re.sub(r"[^A-Z0-9]", "", vat_id.upper())
        if vat_id[:2] in EU and vat_id[:2].isalpha():
            country, vat_id = vat_id[:2], vat_id[2:]
        country = {"GR": "EL"}.get(country, country)
        if country not in EU or country == "ES" or not 1 <= len(vat_id) <= 15 or not latin(who):
            raise ValueError(_("349: у «{who}» нужны название латиницей и NIF-IVA страны ЕС с префиксом, например IE6388047V").format(who=who))
        if base < 0:
            raise ValueError(_("349: сумма по «{who}» отрицательная — это rectificación, её gestor пока не выгружает").format(who=who))
        ops.append(f"2349{y}{decl}{' ' * 58}{country}{vat_id:<15}{latin(who)[:40]:<40}{clave}{base:013d}{' ' * 354}")
    phone = s.get("phone", "") if re.fullmatch(r"\d{9}", s.get("phone", "")) else "0" * 9
    head = (f"1349{y}{decl}{name:<40} {phone}{name:<40}349{y}{q[0]}00001  {'0' * 13}{q}"  # numid: 349 + year + quarter + 00001
            f"{len(ops):09d}{sum(op[-1] for op in f['ops']):015d}{'0' * 24}{' ' * 315}")
    recs = [head] + ops
    if any(len(r) != 500 for r in recs):
        raise ValueError(_("349: запись не 500 знаков"))
    # ponytail: CRLF between records as AEAT informative-file generators do; drop it if Sede «Importar» rejects the file
    return "\r\n".join(recs).encode("iso-8859-1")


# ---------- 151 ----------
# DR151E2023 is the latest the AEAT has published (checked 08.10.2026) and applies until a new one appears.
# Codes from the AEAT «Instrucciones de cumplimentación ejercicio 2023 y siguientes»: CCAA (página 1), tipo de renta
# 10/12 and tipo de actividad 1 = emprendedora (hoja informativa), [22]/[23] and [31]/[32] = 50 % of the total each.
# ponytail: [10] is always 1 (emprendedora, the visa this app targets); codes 2–4 need a settings field when a user has them.
CCAA = {"andalucia": "01", "asturias": "03", "cataluna": "09", "madrid": "12", "valencia": "17"}


def file_151(s: dict, f: dict) -> bytes:
    pages = spec("151-2023")["pages"]
    box = {b[0]: b[2] for b in f["boxes"]}
    income, rn, cuota, withheld, r, y = box["B.02"], box["B.05 = F.17"], box["G.19"], box["G.33"], f["result"], f["year"]
    kind = "I" if r > 0 else "D" if r < 0 else "N"
    state, region = cuota - cuota // 2, cuota // 2
    p1 = {13: kind, 14: nif(s), 23: latin(s.get("name", "")), 103: str(y), 107: "0A", 118: "X",  # [06] principal
          109: s.get("sex", ""), 110: "".join(reversed(s["birth_date"].split("-"))) if s.get("birth_date") else None,  # [04], [05]
          385: s.get("phone", ""), 983: CCAA.get(region_for_year(s, y))}  # [42] móvil; address: the Sede form asks
    p5 = {13: "12" if s.get("activity_kind") == "profesional" else "10", 15: income, 66: max(rn, 0), 83: min(rn, 0),
          100: withheld, 117: "1", 121: s.get("iae", "")}  # [11] epígrafe IAE
    p6 = {648: max(rn, 0), 665: withheld}  # B totals [08], [09]
    p10 = {791: max(rn, 0), 825: cuota, 859: cuota, 876: state, 893: region,
           1012: cuota, 1029: state, 1046: region, 1063: withheld, 1233: r}
    if box.get("G.34"):  # voluntary 210: [34] total, [37] Epígrafe B — placement after the residence year is disputed
        p10 |= {1080: box["G.34"], 1131: box["G.34"]}
    iban, sepa = refund_account(s) if kind == "D" else ("", "0")
    did = {14: "X" if iban else " ", 15: iban, 197: sepa}
    recs = [record(pages[p], v) for p, v in
            (("M15101000", p1), ("M15105000", p5), ("M15106000", p6), ("M15100000", p10), ("M151DID00", did))]
    return wrap("151", y, "0A", nif(s), recs)


BUILDERS = {"130": file_130, "303": file_303, "349": file_349, "151": file_151}
DR303_YEAR = 2026  # the 303 changes casillas every year: add gestor/dr/303-<year>.json when the AEAT publishes it


def available(f: dict) -> bool:
    return f["modelo"] in BUILDERS and (f["modelo"] != "303" or f["year"] == DR303_YEAR)


def filename(s: dict, f: dict) -> str:
    return f"{nif(s) or 'NIF'}_{f['year']}_{f['period']}.{f['modelo']}"
