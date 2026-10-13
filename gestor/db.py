"""SQLite storage. One file per entity (autónomo or SL). Money is integer cents (EUR)."""
import json
import sqlite3
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS clients (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  tax_id TEXT NOT NULL DEFAULT '',
  country TEXT NOT NULL DEFAULT 'ES',
  is_business INTEGER NOT NULL DEFAULT 1,
  address TEXT NOT NULL DEFAULT '',
  email TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS invoices (
  id INTEGER PRIMARY KEY,
  series TEXT NOT NULL,
  number INTEGER,                      -- NULL while draft; assigned on issue
  issue_date TEXT NOT NULL,
  operation_date TEXT,                 -- if different from issue date
  client_id INTEGER NOT NULL REFERENCES clients(id),
  currency TEXT NOT NULL DEFAULT 'EUR',
  fx_rate REAL NOT NULL DEFAULT 1,     -- currency units per 1 EUR (ECB convention)
  treatment TEXT NOT NULL,             -- see rules.TREATMENTS
  vat_rate REAL NOT NULL DEFAULT 0,
  irpf_rate REAL NOT NULL DEFAULT 0,   -- retención withheld by a Spanish business client
  notes TEXT NOT NULL DEFAULT '',
  paid_date TEXT,
  rectifies_id INTEGER REFERENCES invoices(id),
  rectify_reason TEXT NOT NULL DEFAULT '',
  parties TEXT NOT NULL DEFAULT '',    -- JSON snapshot of issuer and client, frozen on issue
  UNIQUE(series, number)
);
CREATE TABLE IF NOT EXISTS invoice_lines (
  id INTEGER PRIMARY KEY,
  invoice_id INTEGER NOT NULL REFERENCES invoices(id) ON DELETE CASCADE,
  description TEXT NOT NULL,
  quantity REAL NOT NULL DEFAULT 1,
  unit_price_cents INTEGER NOT NULL    -- in invoice currency
);
CREATE TABLE IF NOT EXISTS expenses (
  id INTEGER PRIMARY KEY,
  date TEXT NOT NULL,
  supplier TEXT NOT NULL,
  supplier_tax_id TEXT NOT NULL DEFAULT '',
  invoice_ref TEXT NOT NULL DEFAULT '',
  description TEXT NOT NULL DEFAULT '',
  category TEXT NOT NULL,              -- see rules.EXPENSE_CATEGORIES
  vat_kind TEXT NOT NULL DEFAULT 'domestic',  -- domestic | reverse_eu | reverse_non_eu | none
  base_cents INTEGER NOT NULL,
  vat_rate REAL NOT NULL DEFAULT 0,
  vat_cents INTEGER NOT NULL DEFAULT 0,
  deductible_pct REAL NOT NULL DEFAULT 100,      -- share deductible for income tax
  vat_deductible_pct REAL NOT NULL DEFAULT 100,  -- share of input VAT deductible
  withheld_cents INTEGER NOT NULL DEFAULT 0,     -- retención WE withheld from the supplier (→ 111, rent → 115)
  receipt TEXT NOT NULL DEFAULT ''     -- file name under <data>/receipts
);
CREATE TABLE IF NOT EXISTS filings (
  modelo TEXT NOT NULL,
  year INTEGER NOT NULL,
  period TEXT NOT NULL,                -- 1T..4T, 0A (annual), 01..12
  filed_on TEXT NOT NULL,
  amount_cents INTEGER NOT NULL DEFAULT 0,  -- result actually filed (+ to pay, - to refund/compensate)
  reference TEXT NOT NULL DEFAULT '',  -- CSV / justificante
  PRIMARY KEY (modelo, year, period)
);
"""

DEFAULT_SETTINGS = {
    "name": "",
    "tax_id": "",
    "address": "",
    "email": "",
    "phone": "",                 # 9 digits; goes into the 349 and 151 files
    "lang": "",                  # interface language en | ru | es; empty = browser's (gestor/i18n.py)
    "sex": "",                   # H | M, as in the certificado censal; 151 [04]
    "birth_date": "",            # ISO; 151 [05]
    "iae": "",                   # epígrafe IAE, e.g. 763 (programadores y analistas); 151 [11]
    "iban": "",
    "kind": "autonomo",          # autonomo | sl
    "visa": "emprendedor",       # emprendedor | nomada_digital | cuenta_propia | none
    "beckham_first_year": "",    # autónomo: first tax year under Beckham (regime lasts that year + 5)
    "residence": [],             # [{"from": "2024-01-01", "region": "valencia"}, ...]
    "activity_start": "",        # alta en Hacienda (036/037)
    "reta_start": "",            # alta en RETA
    "reta_base": 0,              # chosen monthly base, cents; 0 = minimum of the tramo
    "tarifa_plana": False,
    "activity_kind": "profesional",  # profesional (IAE sección 2) | empresarial (sección 1)
    "permit_until": "",          # residence permit expiry
    "series": "A",               # invoice number template: 'FACT-{YYYY}-{NNNNN}', or a bare prefix 'A' → A2026-0001
    "censo": [],                 # obligations with alta in the certificado censal: 303, 130, 111, 115, roi
    "censo_date": "",            # date of that certificado; empty = not compared
    "new_activity_irpf_7": False,  # 7% retención: year of start + 2 following years (profesionales)
    "inicio_first_year": "",     # first year with positive net, if art. 32.3 conditions are met (20 % reduction)
    "iva_carry": {},             # {"2027": cents} IVA a compensar brought into the year (4T not refunded)
    "irnr_paid": {},             # {"2026-1T": cents} Modelo 210 paid voluntarily under Beckham, credited in 151
    "sl_200_cuotas": {},         # {"2025": cents} base for 202 (40.2) from each filed Modelo 200
    "sl_small_incn": True,       # SL: INCN < 1M (reduced IS scale)
    "sl_emergente": False,       # SL: certified empresa emergente (Ley 28/2022)
    "sl_first_profit_year": "",  # SL: first period with positive base (15 % emergente window, 202 exemption)
}


def connect(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(path, isolation_level=None)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(SCHEMA)
    return con


def get_settings(con) -> dict:
    s = dict(DEFAULT_SETTINGS)
    for row in con.execute("SELECT key, value FROM settings"):
        s[row["key"]] = json.loads(row["value"])
    return s


def save_settings(con, values: dict) -> None:
    con.executemany(
        "INSERT INTO settings(key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        [(k, json.dumps(v, ensure_ascii=False)) for k, v in values.items()],
    )


def invoice_lines(con, invoice_id: int) -> list:
    return con.execute("SELECT * FROM invoice_lines WHERE invoice_id = ? ORDER BY id", (invoice_id,)).fetchall()
