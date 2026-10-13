"""python3 -m gestor.mcp [--data DIR] [--entity main] — stdio MCP server: the person's own Claude Code / Codex works with gestor.
It reads the returns, fills the questionnaire, clients, expenses and invoice drafts, marks returns filed, and helps fill the AEAT
Sede form in the browser. It never issues an invoice, files or pays: issuing, signing and paying stay with the person."""
import argparse
import contextvars
import json
import re
import sys
from contextlib import contextmanager
from datetime import date
from pathlib import Path
from types import SimpleNamespace

from . import core, db, i18n, rules, sede, tax, web
from .i18n import _
from .web import BOX_RU, SEDE

VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26")  # 2026-07-28 clients probe server/discover, get -32601, fall back here
DOCS = Path(__file__).resolve().parent.parent / "docs"

INSTRUCTIONS = f"""gestor computes this person's Spanish tax returns (autónomo / SL). Numbers come only from these tools: never recompute
or round them, never invent a casilla. Cite rules with the [[source-id]] the tools return. Talk to the person in their language
(English, Russian or Spanish), whatever language the tools return.

Profiles: one database per profile, for example a personal autónomo and an SL. `profiles` lists them; every other tool works on
the default profile unless you pass `profile`. A new person with no profile: `profile_create`, then fill it.

First session (no profile, or `profile_incomplete` in `declarations`):
1. Follow the onboarding order in {DOCS / "en" / "onboarding.md"} (Spanish original: {DOCS / "onboarding.md"}, Russian:
   {DOCS / "ru" / "onboarding.md"}). Nearest deadline first: with less than 15 days left, work only on that quarter.
   Then official documents, invoices, bank statement, expenses, open questions.
2. Ask one thing at a time. An official document outweighs an answer; an answer outweighs a guess from the bank statement.
3. Fill the questionnaire with `profile_update`. The person can also type in gestor's web interface, http://127.0.0.1:8765
   by default (`python3 -m gestor` in the gestor folder starts it).
4. Until the profile is complete, `declarations` lists only the upcoming deadlines of a default autónomo calendar: never call
   a return late, never quote amounts, never claim which returns this person must file.

Writing (profile_update, client_save, expense_save, invoice_draft_save, filing_mark, the deletes):
1. Write only what the person confirmed in this conversation. Show the exact values first, get an explicit yes, then call the
   tool. Never write a guess silently.
2. Invoices: drafts only. Issuing gives the invoice its number and cannot be undone: the person does it in the web interface
   (Invoices → the draft → Issue). Issued invoices are changed only with a factura rectificativa, also there.
3. After a write, read back (`profile`, `books`, `declarations`) when the next step depends on it.

Bank statement (CSV or Excel export the person gives you; read it yourself, gestor never stores it). It is not a tax document:
it only finds what is missing in gestor. Rules in detail: step 3 of the onboarding file above. Call `books` for every year it
covers, then:
1. Each incoming payment ↔ an issued invoice (amount in EUR or the invoice currency, payer ≈ client, paid after the issue date).
   No invoice: ask what it is (payment for work, refund, transfer from a relative, own money). Payment for work: propose the
   client (`client_save`) and an invoice draft (`invoice_draft_save`) with operation_date = when the work was done and
   issue_date = today; say that an invoice to a business was due by the 15th of the next month [[rd1619-11]].
2. Debits: first skip the ones already in `books` expenses (same supplier and amount). Group the rest: certainly business
   (RETA cuota, gestoría, bank fees; tax payments are no expense: compare them with `declarations`), possibly business
   (software, phone and internet, coworking, trips, equipment), home share with a home office, personal (food,
   entertainment, transfers to people, cash). Ask only about the doubtful ones, a few at a time.
3. An expense needs a factura completa to the person's NIE/NIF; a statement line is not enough: ask for the factura, read it,
   propose `expense_save` from it. Two exceptions you propose straight from the statement line: the RETA cuota (category reta;
   its document is the TGSS recibo, downloadable in Import@ss) and bank fees (category bank, vat_kind none; the bank's own
   settlement is the document).
4. The category sets the deductible shares. Two start at 0 % and need the person's numbers in deductible_pct: home (supplies
   of the flat with a home office: 30 % × the work room's share of the floor area) and meals (only within the daily limits
   of a business trip). Rent of the flat is not that formula: category rent, deductible_pct = the floor-area share of a room
   used only for work (details: {DOCS.parent / "kb" / "irpf-autonomo.md"}, home office). Ask for the m² or the trip; never guess.
5. Show a short summary first: matched, payments without an invoice, expense candidates. Then go one item at a time.

Helping in the AEAT Sede (browser):
1. The person logs in with Cl@ve or a certificate. Never type PINs, passwords or certificate passphrases.
2. Open `sede_url`, choose «Nueva declaración», the year and the period.
3. If `sede_file` is given, use «Importar» with that file; otherwise type each casilla one-to-one (gestor casilla number = form casilla).
4. Press «Validar declaración». Then compare every casilla on screen with `casillas` and list every difference.
5. STOP. Never press «Presentar declaración», «Firmar y enviar», or confirm a payment, NRC or domiciliación. The person checks,
   signs and sends. Filing is theirs, always.
6. After sending, ask for the date, the amount and the CSV / justificante number, then `filing_mark` with them."""

START = """Start my session with gestor. Call `profiles`, then `declarations` for the current year. If there is no profile or it is
incomplete, follow the First session steps from the gestor instructions. Otherwise tell me the nearest deadline, what it needs and
what is still missing in gestor for it. Talk to me in the language I use here; if I have not written anything yet, ask me first
whether I prefer English, Russian or Spanish."""
STATEMENT = """Check my bank statement against gestor: {file}. Follow the Bank statement steps from the gestor instructions. Talk
to me in the language I use here; if I have not written anything yet, ask me first whether I prefer English, Russian or Spanish."""
PROMPTS = [{"name": "start", "title": "Start with gestor",
            "description": "First session: set up the profile step by step. Later: the nearest deadline and what it needs."},
           {"name": "statement", "title": "Check a bank statement",
            "description": "Match a bank statement with gestor: payments without an invoice, expenses without a factura; propose drafts.",
            "arguments": [{"name": "file", "description": "path to the CSV or Excel export from the bank", "required": False}]}]
TEXTS = {"start": START, "statement": STATEMENT}

S, I, N, B = {"type": "string"}, {"type": "integer"}, {"type": ["number", "string"]}, {"type": "boolean"}
YEAR, ID = {"type": "integer", "description": "tax year, e.g. 2026"}, {"type": "integer", "description": "id from `books`; omit to create"}
DECL = {"modelo": {"type": "string", "description": "303, 130, 349, 151, 390, 347, 100, 111, 115, 202, 200"}, "year": YEAR,
        "period": {"type": "string", "description": "1T-4T for quarterly returns, 0A for annual ones"}}
AMOUNT = {"type": ["number", "string"], "description": "euros, e.g. 1234.56 or «1234,56»"}
FIELDS_DOC = (
    "Questionnaire fields → value in the web form's format; only the given fields change. name, tax_id (NIE/NIF), address, "
    "email, iban, phone; lang: en|ru|es; sex: H|M; iae: epígrafe, e.g. 763; kind: autonomo|sl; visa: " + "|".join(rules.VISAS) + "; "
    "activity_start (alta en Hacienda), reta_start, permit_until, censo_date, birth_date: YYYY-MM-DD; beckham_first_year, "
    "inicio_first_year, sl_first_profit_year: YYYY; residence: lines «YYYY-MM-DD region», region one of " + "|".join(rules.REGIONS) + "; "
    "censo: space-separated obligations with ALTA in the certificado censal, of 303 130 111 115 roi; series: invoice number format, "
    "e.g. FACT-{YYYY}-{NNNNN}; activity_kind: profesional|empresarial; new_activity_irpf_7, tarifa_plana, sl_small_incn, "
    "sl_emergente: true|false; reta_base: euros; iva_carry, sl_200_cuotas: lines «YYYY amount»; irnr_paid: lines «YYYY 1T amount».")


def tool(name, description, props=None, required=(), read=False, profile=True):
    props = dict(props or {}) | ({"profile": {"type": "string", "description": "profile name from `profiles`; default: the server's"}}
                                 if profile else {})
    t = {"name": name, "description": description,
         "inputSchema": {"type": "object", "properties": props, "required": list(required), "additionalProperties": False}}
    return t | ({"annotations": {"readOnlyHint": True}} if read else {})


TOOLS = [
    tool("profiles", "Every profile: name, kind, regime, interface language, which questionnaire fields are still empty.",
         read=True, profile=False),
    tool("profile_create", "Create a new empty profile (a new database). Name: a-z 0-9 - _, e.g. «main» or «sl».",
         {"name": S}, ["name"], profile=False),
    tool("profile", "The questionnaire of a profile: every field with its current value, and the empty required fields.", read=True),
    tool("profile_update", "Change questionnaire fields. " + FIELDS_DOC,
         {"fields": {"type": "object", "description": "field → value"}}, ["fields"]),
    tool("books", "Clients (all), and the invoices and expenses of a year, with ids for the save and delete tools. Invoice amounts "
         "in EUR in Sede format; draft invoices have number null.", {"year": YEAR}, ["year"], read=True),
    tool("client_save", "Create a client, or change the given fields of client `id`.",
         {"id": ID, "name": S, "tax_id": {"type": "string", "description": "NIF / VAT ID / foreign tax id"},
          "country": {"type": "string", "description": "ISO 2 letters, e.g. ES, DE, US"},
          "is_business": {"type": "boolean", "description": "company or self-employed (true), private person (false)"},
          "address": S, "email": S}),
    tool("expense_save", "Create an expense, or replace expense `id` with these values (omitted optional ones fall back to their "
         "defaults). The receipt file is attached in the web interface.",
         {"id": ID, "date": {"type": "string", "description": "YYYY-MM-DD of the factura"}, "supplier": S, "supplier_tax_id": S,
          "invoice_ref": {"type": "string", "description": "the supplier's factura number"}, "description": S,
          "category": {"type": "string", "description": "|".join(rules.EXPENSE_CATEGORIES)},
          "vat_kind": {"type": "string", "description": "|".join(rules.VAT_KINDS) + "; default domestic"},
          "base": AMOUNT, "vat_rate": {"type": ["number", "string"], "description": "IVA %, e.g. 21"},
          "vat": AMOUNT | {"description": "IVA in euros; default base × rate"},
          "deductible_pct": {"type": ["number", "string"], "description": "% for income tax; default by category"},
          "vat_deductible_pct": {"type": ["number", "string"], "description": "% of IVA deductible; default by category"},
          "withheld": AMOUNT | {"description": "retención the person withheld from the supplier (→ 111 / 115)"}},
         ["date", "supplier", "category", "base"]),
    tool("expense_delete", "Delete expense `id` and its receipt file.", {"id": I}, ["id"]),
    tool("invoice_draft_save", "Create an invoice draft, or replace draft `id` with these values. Never issues: the number is given "
         "when the person issues the draft in the web interface. Empty treatment, vat_rate, irpf_rate: gestor chooses by the client.",
         {"id": ID, "client_id": I, "issue_date": {"type": "string", "description": "YYYY-MM-DD"},
          "operation_date": {"type": "string", "description": "YYYY-MM-DD if different from the issue date"},
          "currency": {"type": "string", "description": "|".join(rules.CURRENCIES) + "; default EUR"},
          "fx_rate": {"type": ["number", "string"], "description": "currency units per 1 EUR; empty: ECB rate"},
          "treatment": {"type": "string", "description": "|".join(rules.TREATMENTS)},
          "vat_rate": N, "irpf_rate": N, "notes": S,
          "lines": {"type": "array", "maxItems": 5, "items": {"type": "object", "additionalProperties": False, "required": ["description", "price"],
                    "properties": {"description": S, "quantity": N, "price": AMOUNT | {"description": "unit price in the invoice currency"}}}}},
         ["client_id", "issue_date", "lines"]),
    tool("invoice_draft_delete", "Delete invoice draft `id`. Issued invoices cannot be deleted.", {"id": I}, ["id"]),
    tool("declarations", "All returns of a year with deadline, result and status: filed / open / late / not open yet / no books "
         "(deadline passed, but gestor has no invoices or expenses for that year, so it cannot tell whether one was missed). "
         "While the questionnaire is incomplete: `profile_incomplete` with the empty fields and only upcoming deadlines, no amounts.",
         {"year": YEAR}, ["year"], read=True),
    tool("declaration", "One return for the Sede: every casilla (Spanish label as in the Sede form, a plain label in the person's "
         "interface language below, none in Spanish, value in Sede format), notes with sources, status, Sede link and, for "
         "130/303/349/151, an import file written to disk.", DECL, ["modelo", "year", "period"]),
    tool("filing_mark", "Mark a return filed, with what the Sede justificante says.",
         DECL | {"filed_on": {"type": "string", "description": "YYYY-MM-DD; default today"},
                 "amount": AMOUNT | {"description": "result as filed, negative for a refund"},
                 "reference": {"type": "string", "description": "CSV / justificante number"}},
         ["modelo", "year", "period", "amount"]),
    tool("filing_unmark", "Remove the filed mark of a return.", DECL, ["modelo", "year", "period"]),
]
SCHEMAS = {t["name"]: t["inputSchema"] for t in TOOLS}


def es(cents: int) -> str:
    """Sede number format: no thousands separator, comma decimals."""
    return f"{'-' if cents < 0 else ''}{abs(cents) // 100},{abs(cents) % 100:02d}"


def text(v) -> str:
    """A JSON argument as the web form would post it."""
    return "" if v is None else ("1" if v else "0") if isinstance(v, bool) else " ".join(map(str, v)) if isinstance(v, list) else str(v)


def incomplete(s: dict) -> list[str]:
    """Questionnaire fields still empty: the bar of «How gestor understood you» (web.understood) plus the NIE/NIF the Sede needs.
    An SL needs its start date too: the first tax period (sl_days) and the first-year 202 exemption depend on it."""
    need = (("name", s["name"]), ("tax_id", s["tax_id"]), ("activity_start", s["activity_start"] or s["reta_start"]))
    return [k for k, v in need if not v]


class Gestor:
    def __init__(self, data: Path, entity: str):
        self.data, self.entity = data, entity

    @contextmanager
    def _profile(self, profile=None):
        """Connection and settings of one existing profile, with the request language set from it. No new file."""
        name = profile or self.entity
        if not re.fullmatch(r"[a-z0-9_-]+", name) or not (self.data / f"{name}.db").exists():
            raise ValueError(f"no gestor profile «{name}» in {self.data}: see `profiles`; a new person starts with `profile_create`")
        con = db.connect(self.data / f"{name}.db")
        try:
            s = db.get_settings(con)
            i18n.current.set(i18n.pick(s.get("lang", "")))
            con.execute("BEGIN")  # one transaction per tool call, as the web app does per request
            yield con, s
            con.execute("COMMIT")
        finally:
            if con.in_transaction:
                con.execute("ROLLBACK")
            con.close()

    def _forms(self, con, s, year):
        filed = {(r["modelo"], r["period"]): r for r in con.execute("SELECT * FROM filings WHERE year = ?", (year,))}
        today, books = date.today().isoformat(), bool(tax.sales(con, year) or tax.purchases(con, year))  # web.stamp's rule
        for _, fs in tax.forms(con, s, year):
            for f in fs:
                done = filed.get((f["modelo"], f["period"]))
                status = ("filed" if done else "not open yet" if today < f["opens"] else "open" if today <= f["deadline"]
                          else "late" if books else "no books")
                yield f, done, status

    def profiles(self):
        out = []
        for p in sorted(self.data.glob("*.db")):
            with self._profile(p.stem) as (_con, s):
                out.append({"profile": p.stem, "default": p.stem == self.entity, "name": s["name"], "kind": s["kind"],
                            "regime": tax.regime_label(s, date.today().year), "lang": s["lang"], "incomplete": incomplete(s)})
        return {"profiles": out}

    def profile_create(self, name):
        name = web.create_entity(self.data, name)
        return {"profile": name}

    def profile(self, profile=None):
        with self._profile(profile) as (_con, s):
            return {"profile": profile or self.entity, "fields": s, "incomplete": incomplete(s)}

    def profile_update(self, fields, profile=None):
        if unknown := sorted(set(fields) - set(web.SETTINGS_FIELDS)):
            raise ValueError(f"unknown fields {unknown}; known: {sorted(web.SETTINGS_FIELDS)}")
        with self._profile(profile) as (con, _s):
            values = web.settings_values({k: text(v) for k, v in fields.items()})
            db.save_settings(con, values)
            return {"saved": values, "incomplete": incomplete(db.get_settings(con))}

    def _invoice(self, con, inv):
        a = core.invoice_amounts(con, inv)
        return {k: inv[k] for k in ("id", "client_id", "issue_date", "operation_date", "currency", "fx_rate", "treatment", "vat_rate",
                                    "irpf_rate", "notes", "paid_date", "rectifies_id")} | {
            "number": core.invoice_number(inv) if inv["number"] else None,
            "lines": [{"description": l["description"], "quantity": l["quantity"], "price": es(l["unit_price_cents"])}
                      for l in db.invoice_lines(con, inv["id"])],
            "base_eur": es(a["base_eur"]), "vat_eur": es(a["vat_eur"]), "irpf_eur": es(a["irpf_eur"]), "total_eur": es(a["total_eur"])}

    def books(self, year, profile=None):
        with self._profile(profile) as (con, _s):
            y = str(year)
            return {"clients": [dict(c) for c in con.execute("SELECT * FROM clients ORDER BY name")],
                    "invoices": [self._invoice(con, i) for i in
                                 con.execute("SELECT * FROM invoices WHERE substr(issue_date, 1, 4) = ? ORDER BY issue_date, id", (y,))],
                    "expenses": [dict(e) for e in
                                 con.execute("SELECT * FROM expenses WHERE substr(date, 1, 4) = ? ORDER BY date, id", (y,))]}

    def client_save(self, id=None, profile=None, **fields):
        with self._profile(profile) as (con, _s):
            if id:
                old = con.execute("SELECT * FROM clients WHERE id = ?", (id,)).fetchone()
                if not old:
                    raise ValueError(f"no client {id}")
                fields = dict(old) | fields
            return {"id": web.save_client(con, {k: text(v) for k, v in fields.items()}, id)}

    def expense_save(self, id=None, profile=None, **fields):
        with self._profile(profile) as (con, s):
            if id and not con.execute("SELECT 1 FROM expenses WHERE id = ?", (id,)).fetchone():
                raise ValueError(f"no expense {id}")
            req = SimpleNamespace(con=con, s=s, files={}, data_dir=self.data, form={k: text(v) for k, v in fields.items()})
            return {"id": web.save_expense(req, id)}

    def expense_delete(self, id, profile=None):
        with self._profile(profile) as (con, s):
            if not con.execute("SELECT 1 FROM expenses WHERE id = ?", (id,)).fetchone():
                raise ValueError(f"no expense {id}")
            web.delete_expense(con, self.data, id)
            return {"deleted": id}

    def invoice_draft_save(self, lines, id=None, profile=None, **fields):
        if not 1 <= len(lines) <= 5:
            raise ValueError("an invoice draft has 1 to 5 lines")
        form = {k: text(v) for k, v in fields.items()}
        for i, l in enumerate(lines):
            form |= {f"desc{i}": text(l.get("description")), f"qty{i}": text(l.get("quantity", 1)), f"price{i}": text(l.get("price"))}
        with self._profile(profile) as (con, s):
            inv_id = web.save_invoice(SimpleNamespace(con=con, s=s, form=form), id)
            return self._invoice(con, con.execute("SELECT * FROM invoices WHERE id = ?", (inv_id,)).fetchone())

    def invoice_draft_delete(self, id, profile=None):
        with self._profile(profile) as (con, _s):
            if not con.execute("DELETE FROM invoices WHERE id = ? AND number IS NULL", (id,)).rowcount:
                raise ValueError(f"no invoice draft {id}: issued invoices are corrected with a factura rectificativa in the web interface")
            return {"deleted": id}

    def declarations(self, year, profile=None):
        with self._profile(profile) as (con, s):
            missing, today = incomplete(s), date.today().isoformat()
            rows = [({"modelo": f["modelo"], "period": f["period"], "title": f["title"], "opens": f["opens"], "deadline": f["deadline"]},
                     f, st) for f, _done, st in self._forms(con, s, year)]
            if missing:  # default settings: the calendar is generic, amounts and «late» would be invented
                return {"profile_incomplete": missing, "declarations": [r for r, f, _st in rows if f["deadline"] >= today]}
            return {"regime": tax.regime_label(s, year),
                    "declarations": [r | {"result": es(f["result"]), "status": st} for r, f, st in rows]}

    def _one(self, con, s, modelo, year, period):
        if missing := incomplete(s):
            raise ValueError(f"profile incomplete ({', '.join(missing)}): fill the questionnaire first (First session in the instructions)")
        hit = next(((f, d, st) for f, d, st in self._forms(con, s, year) if f["modelo"] == modelo and f["period"] == period), None)
        if not hit:
            raise ValueError(f"gestor has no {modelo} {period} {year} for this profile; call declarations first")
        return hit

    def declaration(self, modelo, year, period, profile=None):
        with self._profile(profile) as (con, s):
            f, done, status = self._one(con, s, modelo, year, period)
            plain = {} if i18n.current.get() == "es" else {_(k): _(v) for k, v in BOX_RU.items()}
            out = {"modelo": modelo, "year": year, "period": period, "title": f["title"], "opens": f["opens"], "deadline": f["deadline"],
                   "status": status, "result": es(f["result"]), "result_cents": f["result"],
                   "casillas": [{"casilla": c, "label_es": label, "label": plain.get(label, ""), "value": es(v), "cents": v}
                                for c, label, v in f["boxes"]],
                   "notes": [n for n in f.get("notes", []) if n], "sources": f.get("sources", []), "sede_url": SEDE.get(modelo, "")}
            if done:
                out["filed"] = {"on": done["filed_on"], "amount": es(done["amount_cents"] or 0), "csv": done["reference"]}
            if sede.available(f):
                if s.get("tax_id"):
                    path = self.data / "sede" / (profile or self.entity) / sede.filename(s, f)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(sede.BUILDERS[modelo](s, f))
                    out["sede_file"] = str(path)
                else:
                    out["sede_file_missing"] = "Add NIE/NIF in gestor settings: Sede will not accept the file without it."
            return out

    def filing_mark(self, modelo, year, period, amount, filed_on="", reference="", profile=None):
        with self._profile(profile) as (con, s):
            self._one(con, s, modelo, year, period)
            web.save_filing(con, {"modelo": modelo, "year": year, "period": period, "filed_on": filed_on, "amount": text(amount),
                                  "reference": reference})
            return {"filed": {"modelo": modelo, "year": year, "period": period}}

    def filing_unmark(self, modelo, year, period, profile=None):
        with self._profile(profile) as (con, _s):
            web.delete_filing(con, {"modelo": modelo, "year": year, "period": period})
            return {"unfiled": {"modelo": modelo, "year": year, "period": period}}


def handle(g: Gestor, msg: dict):
    """One JSON-RPC request → result dict; raises LookupError for unknown methods."""
    method, p = msg.get("method"), msg.get("params") or {}
    if method == "initialize":
        asked = p.get("protocolVersion")
        return {"protocolVersion": asked if asked in VERSIONS else VERSIONS[0], "capabilities": {"tools": {}, "prompts": {}},
                "serverInfo": {"name": "gestor", "version": "2"}, "instructions": INSTRUCTIONS}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": TOOLS}
    if method == "prompts/list":
        return {"prompts": PROMPTS}
    if method == "prompts/get":
        if (name := p.get("name")) not in TEXTS:
            raise ValueError(f"unknown prompt {name}")
        file = (p.get("arguments") or {}).get("file") or "ask me for the file first (CSV or Excel export from the bank)"
        prompt = next(x for x in PROMPTS if x["name"] == name)
        return {"description": prompt["description"],
                "messages": [{"role": "user", "content": {"type": "text", "text": TEXTS[name].format(file=file)}}]}
    if method == "tools/call":
        name, args = p.get("name"), p.get("arguments") or {}
        try:
            schema = SCHEMAS.get(name) or {}
            if not schema:
                raise ValueError(f"unknown tool {name}")
            if bad := sorted(set(args) - set(schema["properties"])):
                raise ValueError(f"unknown arguments {bad}")
            if lack := [k for k in schema["required"] if k not in args]:
                raise ValueError(f"missing arguments {lack}")
            # each call sets the profile's language; it must not leak into the next
            data = contextvars.copy_context().run(getattr(g, name), **args)
        except web.NotFound:
            return {"content": [{"type": "text", "text": "error: not found (check the ids with `books`)"}], "isError": True}
        except Exception as e:  # a bad argument must not kill the server for the rest of the session
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
            except ValueError as e:
                reply = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32602, "message": str(e)}}
        tx.write(json.dumps(reply, ensure_ascii=False) + "\n")
        tx.flush()


if __name__ == "__main__":
    a = argparse.ArgumentParser(prog="gestor.mcp")
    a.add_argument("--data", type=Path, default=Path.home() / ".gestor")
    a.add_argument("--entity", default="main")
    args = a.parse_args()
    serve(Gestor(args.data, args.entity))
