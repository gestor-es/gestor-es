English | [Русский](README.ru.md) | [Español](README.es.md)

# gestor

A local gestor for autónomos and SLs in Spain: invoices, expenses, IVA/IRPF/Beckham/SL, RETA and a filing calendar. One user, runs locally, no dependencies (Python 3.12+, stdlib). It computes your returns and explains every amount with the law; you file them yourself.

Everything is in English, Russian and Spanish: the interface, the legal source cards, the knowledge base and the docs. Switch the interface language in the profile menu or in "Questionnaire". The language is stored per profile. The MCP server answers in the same language.

```bash
python3 -m gestor                      # http://127.0.0.1:8765, data in ~/.gestor
python3 -m gestor --data ~/gestor-data --port 8800
python3 -m unittest tests.test_tax -v  # engine against the examples in kb/
```

- `gestor/tax.py` — engine: 303, 349, 347, 390, 130, 100, 151, 202, 111, 115, 200, RETA, calendar, warnings.
- `gestor/web.py` — interface (server-rendered HTML, no frameworks, no build step), `gestor/db.py` — SQLite, one file per profile.
- [`kb/en/`](kb/en/) — knowledge base with sources (BOE, AEAT, TGSS), checked as of 08.10.2026: [IVA and invoicing](kb/en/iva-facturacion.md), [IRPF for autónomos](kb/en/irpf-autonomo.md), [Beckham regime](kb/en/beckham.md), [RETA](kb/en/reta.md), [Sociedad Limitada](kb/en/sociedad-limitada.md), [visas and residence](kb/en/visados.md), [filing calendar](kb/en/calendario-presentacion.md). The originals are in Spanish in [`kb/`](kb/), with the law quoted verbatim; they are the source of truth. Russian: [`kb/ru/`](kb/ru/).
- `gestor/sources/*.json` — legal sources: the Spanish quote from BOE/AEAT/DGT, a translation, what it means, status (explicit in the text / interpretation / disputed), practice. In the interface: a § mark on every amount, an explanation with the law under every input field, "Profile" with gestor's conclusions about your situation, and the "Sources" page. `python3 -m unittest tests.test_sources` checks that every § leads to a complete entry.
- [`docs/en/use-cases.md`](docs/en/use-cases.md) — what the service does and what it does not do.
- [`docs/en/onboarding.md`](docs/en/onboarding.md) — the canonical onboarding order: which documents to upload, what to ask, what to clarify.
- [`docs/en/explainer.html`](docs/en/explainer.html) — how gestor works, on a fictional profile: parts, the path of one invoice, a quarter worked through. Open it in a browser after cloning.
- [`docs/glosario-aeat.md`](docs/glosario-aeat.md) — the AEAT terms gestor uses, each with its AEAT page (Spanish).

Backup: copy the data folder (`*.db` and `receipts/`). Invoice as PDF: "Print / PDF" in the browser.
The figures are a calculation from the data you enter. You file them yourself in the AEAT Sede.

## Help in the Sede from Claude Code or Codex

`gestor/mcp.py` is a read-only MCP server over stdio. Tools: `declarations` (the year's declarations with due date and status) and `declaration` (the casillas of one declaration in Sede format, notes with §, a link to the Sede and a file for "Importar" in `<data>/sede/<profile>/`). The subscription is yours, in your own program. gestor stores no keys.

```bash
claude mcp add -s user gestor -e PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
codex mcp add gestor --env PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
claude --chrome   # Claude in Chrome: the agent works in your Chrome, where you are signed in to the Sede
```

The agent opens the form, uploads the file or types in the casillas, presses "Validar" and checks the screen against gestor. It does not press "Presentar" or "Firmar y enviar": this rule is in `INSTRUCTIONS`. You sign.
