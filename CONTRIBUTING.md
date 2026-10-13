# Contributing

## Ground rules

- Python 3.12+ standard library only. No new dependencies, no frontend build.
- Never put real tax data in code, tests, issues or screenshots: use made-up names, NIE `X1234567L`, IBAN `ES91 2100 0418 4502 0005 1332`, example.com.
- gestor calculates and explains; it never files, signs or pays. Keep it that way, in the web app and in the MCP server.
- Every rule or amount cites a legal source card (`gestor/sources/*.json`) with its status: verified, interpretation or disputed. Do not present an interpretation as settled law.

## Run the tests

```bash
python3 -W ignore -m unittest tests.test_web tests.test_mcp tests.test_sede tests.test_sources tests.test_tax tests.test_i18n
```

CI runs the same command on every push and pull request.

## Languages

- Interface strings: write the source string in Russian inside `_()` (or `N_()` for module constants) and add the English and Spanish translation to `gestor/locale/en/*.json` and `gestor/locale/es/*.json`. Spanish uses the AEAT's own terms (`docs/glosario-aeat.md`). `tests/test_i18n.py` fails on any missing translation.
- Knowledge base and docs: the Spanish files in `kb/` and `docs/` are the originals. Change them first, then `kb/en`, `kb/ru`, `docs/en`, `docs/ru`.
- Legal source cards: `quote_es` is the verbatim original; keep `title_*`, `summary_*` and `status_note_*` in all three languages.

## Database changes

The schema is created with `CREATE TABLE IF NOT EXISTS` (`gestor/db.py`). Existing data folders must keep working. The first change to an existing table must add a migration step in `db.connect()` keyed on `PRAGMA user_version` (current databases are version 0), plus a test that opens a version-0 database.

## Every January

- New IRPF state and regional scales, mínimos, RETA bases and rates (`gestor/tax.py`), each with a source card.
- AEAT calendar for the new year (deadlines and domiciliación dates) and holidays that move a deadline.
- New diseños de registro for the Sede files (`gestor/dr/`, `scripts/dr_extract.py`); bump `DR303_YEAR` in `gestor/sede.py` only after checking the new layout.
- Re-check the `checked` date of every source card you rely on.
