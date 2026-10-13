"""python3 -m gestor.mcp [--data DIR] [--entity main] — stdio MCP server: the person's own Claude Code / Codex reads gestor's
returns and helps fill the AEAT Sede form in the browser. Read-only: no tool writes the books, files or pays."""
import argparse
import contextvars
import json
import sys
from datetime import date
from pathlib import Path

from . import db, i18n, sede, tax
from .i18n import _
from .web import BOX_RU, SEDE

VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26")  # 2026-07-28 clients probe server/discover, get -32601, fall back here

INSTRUCTIONS = """gestor computes this person's Spanish tax returns (autónomo / SL). Numbers come only from these tools: never recompute
or round them, never invent a casilla. Cite rules with the [[source-id]] the tools return.

Helping in the AEAT Sede (browser):
1. The person logs in with Cl@ve or a certificate. Never type PINs, passwords or certificate passphrases.
2. Open `sede_url`, choose «Nueva declaración», the year and the period.
3. If `sede_file` is given, use «Importar» with that file; otherwise type each casilla one-to-one (gestor casilla number = form casilla).
4. Press «Validar declaración». Then compare every casilla on screen with `casillas` and list every difference.
5. STOP. Never press «Presentar declaración», «Firmar y enviar», or confirm a payment, NRC or domiciliación. The person checks,
   signs and sends. Filing is theirs, always.
6. After sending, remind them to keep the PDF justificante and mark the return filed in gestor (Taxes page)."""

TOOLS = [
    {"name": "declarations", "description": "All returns of a year with deadline, result and status (filed / open / late / not open yet).",
     "inputSchema": {"type": "object", "properties": {"year": {"type": "integer"}}, "required": ["year"], "additionalProperties": False}},
    {"name": "declaration", "description": "One return for the Sede: every casilla (Spanish label as in the Sede form, a plain label "
     "in the person's interface language below, none in Spanish, value in Sede format), notes with sources, status, Sede link and, "
     "for 130/303/349/151, an import file written to disk.",
     "inputSchema": {"type": "object", "properties": {
         "modelo": {"type": "string", "description": "303, 130, 349, 151, 390, 347, 100, 111, 115, 202, 200"},
         "year": {"type": "integer"},
         "period": {"type": "string", "description": "1T-4T for quarterly returns, 0A for annual ones"}},
         "required": ["modelo", "year", "period"], "additionalProperties": False}},
]


def es(cents: int) -> str:
    """Sede number format: no thousands separator, comma decimals."""
    return f"{'-' if cents < 0 else ''}{abs(cents) // 100},{abs(cents) % 100:02d}"


class Gestor:
    def __init__(self, data: Path, entity: str):
        self.data, self.entity, self.path = data, entity, data / f"{entity}.db"

    def _forms(self, con, s, year):
        filed = {(r["modelo"], r["period"]): r for r in con.execute("SELECT * FROM filings WHERE year = ?", (year,))}
        today = date.today().isoformat()
        for _, fs in tax.forms(con, s, year):
            for f in fs:
                done = filed.get((f["modelo"], f["period"]))
                status = ("filed" if done else "not open yet" if today < f["opens"] else "late" if f["deadline"] < today else "open")
                yield f, done, status

    def declarations(self, year):
        con = db.connect(self.path)
        try:
            s = db.get_settings(con)
            i18n.current.set(i18n.pick(s.get("lang", "")))
            return {"profile": tax.regime_label(s, year), "declarations": [
                {"modelo": f["modelo"], "period": f["period"], "title": f["title"], "opens": f["opens"], "deadline": f["deadline"],
                 "result": es(f["result"]), "status": st} for f, _, st in self._forms(con, s, year)]}
        finally:
            con.close()

    def declaration(self, modelo, year, period):
        con = db.connect(self.path)
        try:
            s = db.get_settings(con)
            i18n.current.set(i18n.pick(s.get("lang", "")))
            plain = {} if i18n.current.get() == "es" else {_(k): _(v) for k, v in BOX_RU.items()}
            hit = next(((f, d, st) for f, d, st in self._forms(con, s, year) if f["modelo"] == modelo and f["period"] == period), None)
            if not hit:
                raise ValueError(f"gestor has no {modelo} {period} {year} for this profile; call declarations first")
            f, done, status = hit
            out = {"modelo": modelo, "year": year, "period": period, "title": f["title"], "opens": f["opens"], "deadline": f["deadline"],
                   "status": status, "result": es(f["result"]), "result_cents": f["result"],
                   "casillas": [{"casilla": c, "label_es": label, "label": plain.get(label, ""), "value": es(v), "cents": v}
                                for c, label, v in f["boxes"]],
                   "notes": [n for n in f.get("notes", []) if n], "sources": f.get("sources", []), "sede_url": SEDE.get(modelo, "")}
            if done:
                out["filed"] = {"on": done["filed_on"], "amount": es(done["amount_cents"] or 0), "csv": done["reference"]}
            if sede.available(f):
                if s.get("tax_id"):
                    path = self.data / "sede" / self.entity / sede.filename(s, f)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(sede.BUILDERS[modelo](s, f))
                    out["sede_file"] = str(path)
                else:
                    out["sede_file_missing"] = "Add NIE/NIF in gestor settings: Sede will not accept the file without it."
            return out
        finally:
            con.close()


def handle(g: Gestor, msg: dict):
    """One JSON-RPC request → result dict; raises LookupError for unknown methods."""
    method, p = msg.get("method"), msg.get("params") or {}
    if method == "initialize":
        asked = p.get("protocolVersion")
        return {"protocolVersion": asked if asked in VERSIONS else VERSIONS[0], "capabilities": {"tools": {}},
                "serverInfo": {"name": "gestor", "version": "1"}, "instructions": INSTRUCTIONS}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": TOOLS}
    if method == "tools/call":
        name, args = p.get("name"), p.get("arguments") or {}
        try:
            run = contextvars.copy_context().run  # each call sets the profile's language; it must not leak into the next
            if name == "declarations":
                data = run(g.declarations, int(args["year"]))
            elif name == "declaration":
                data = run(g.declaration, str(args["modelo"]), int(args["year"]), str(args["period"]))
            else:
                raise ValueError(f"unknown tool {name}")
        except (KeyError, ValueError, TypeError) as e:
            return {"content": [{"type": "text", "text": f"error: {e}"}], "isError": True}
        return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False)}], "structuredContent": data}
    raise LookupError(method)


def serve(g: Gestor, rx=sys.stdin, tx=sys.stdout):
    for line in rx:
        if not line.strip():
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}
        else:
            if "id" not in msg:
                continue  # notification: notifications/initialized, cancelled
            try:
                reply = {"jsonrpc": "2.0", "id": msg["id"], "result": handle(g, msg)}
            except LookupError:
                reply = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32601, "message": f"method not found: {msg.get('method')}"}}
        tx.write(json.dumps(reply, ensure_ascii=False) + "\n")
        tx.flush()


if __name__ == "__main__":
    a = argparse.ArgumentParser(prog="gestor.mcp")
    a.add_argument("--data", type=Path, default=Path.home() / ".gestor")
    a.add_argument("--entity", default="main")
    args = a.parse_args()
    serve(Gestor(args.data, args.entity))
