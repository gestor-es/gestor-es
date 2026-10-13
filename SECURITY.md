# Security

gestor runs on your machine and answers only on 127.0.0.1 / localhost. Your books stay in the data folder (`~/.gestor` by default).

## Report a vulnerability

Use GitHub's private reporting: **Security → Report a vulnerability** on https://github.com/gestor-es/gestor-es. Do not open a public issue.

Never attach real tax data, databases, receipts, NIE/NIF, IBAN or bank statements to a report or an issue. Reproduce with the demo profile or made-up data.

## Scope

In scope: the web app (`gestor/web.py`), the MCP server (`gestor/mcp.py`), the Sede files (`gestor/sede.py`), anything that can read, change or leak the data folder.
Out of scope: wrong tax figures (open a normal issue with made-up numbers), the AEAT Sede itself, the AI agent you connect over MCP.
