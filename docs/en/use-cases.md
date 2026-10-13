*Translated from the Russian original [docs/use-cases.md](../use-cases.md) on 13.10.2026. The Russian file is the source of truth; facts were checked as of the date stated below.*

# Use cases

Profiles: **A**: autónomo + Beckham. **B**: autónomo under the general IRPF. **C**: Sociedad Limitada.
The residence status is chosen in the profile: entrepreneur visa, digital nomad visa, cuenta propia residence permit, EU / no restrictions.
The rules come from `kb/*.md`.

## Every month

| # | Scenario | Profiles | What the service does |
|---|---|---|---|
| 1 | Issue an invoice to a foreign client (outside the EU) | A B C | IVA regime "no sujeta" by the client's country, the art. 69.Uno.1º clause, the ECB rate on the transaction date (or entered manually), base and cuota in EUR. The number is assigned on issue, in order and by date, in the format from the questionnaire (for example FACT-{YYYY}-{NNNNN} → FACT-2026-00001). The data of both parties is frozen in the invoice. |
| 2 | Invoice to an EU client (B2B) | A B C | The "inversión del sujeto pasivo" clause, casilla 59 in the 303, a line with clave S in the 349. Without the client's VAT ID and address the invoice cannot be issued. |
| 3 | Invoice to a Spanish company | A B C | IVA 21 %. Retención: 15 % (7 % in the start year and the 2 following years) for B; 24 % for A; 0 % for C and for empresarial activity. |
| 4 | Correct an issued invoice | A B C | Only with a factura rectificativa (series R), with a required reason and a reference to the original invoice. A draft can be edited and deleted. |
| 5 | Mark a payment | A B C | Payment date on the invoice. |
| 6 | Enter an expense with a receipt | A B C | The category sets the % that goes into the tax base and the % of IVA you can deduct. The receipt is stored in `<data>/receipts`. Supplier from the EU / outside the EU without IVA → autorrepercusión (10/11 + 36/37 or 12/13 + 28/29). Equipment > 300 € is amortised (26 % autónomo, 25 % SL). Health insurance: no more than 500 € per year. Meals: only the % you enter (limits per day). |
| 7 | Enter the cuota RETA | A B C | Category "Cuota RETA": for B it is an expense (casilla 0186); for A it does not reduce the base of the 151; for C it is retribución en especie of the administrador (111). |
| 8 | Pay a Spanish professional or office rent with retención | A B C | The field "Retención that YOU withheld" in the expense → Modelo 111 (professionals) or 115 (rent), the annual 190/180 in the calendar. |

## Every quarter

| # | Scenario | Profiles | What the service does |
|---|---|---|---|
| 9 | Modelo 303 | A B C | All casillas from the quarter's transactions, carry-over of "a compensar" between quarters, refund in 4T. |
| 10 | Modelo 130 | B | Running total, 20 %, 5 % gastos de difícil justificación (≤ 2 000 €), minoración art. 110.3.c (without last year's data: 0), carry-over of negative results. Not filed if ≥ 70 % of last year's income had retención (profesional only). |
| 11 | No 130 and no 210 under Beckham | A | The 130 is not shown (whether the general 130 applies to activity under the regime is disputed; see "Where gestor may be wrong"). The quarterly 210 is not needed: it is a form for non-residents, and a client without a permanent presence in Spain does not withhold (sources: `gestor/sources/beckham.json`). The overview shows an amount to "set aside" on the 24 % / 47 % scale. |
| 12 | Modelo 349 | A B C | Only if there were EU transactions: clients (S) and suppliers (I). Above 50 000 € per quarter: a warning about monthly filing. |
| 13 | Modelo 202 | C | Modalidad 40.2: 18 % of the base of the last Modelo 200 (entered in the profile; without it: an estimate from the invoices or a reminder to enter it). First year: not filed. |
| 14 | Modelo 111 / 115 | A B C | SL: retención 19 % / 35 % on the administrador's remuneration and on RETA paid by the SL (without last year's turnover: 35 %). All profiles: retenciones withheld from professionals and landlords. |
| 15 | Mark a return as filed | A B C | Amount from the filed return, date, CSV/justificante number. The mark can be cancelled. The annual 100/200 count only the advance payments that were filed. |

## Every year

| # | Scenario | Profiles | What the service does |
|---|---|---|---|
| 16 | Modelo 390 | A B C | Summary of the year's 303, rectificativas, volumen de operaciones. |
| 17 | Modelo 347 | A B C | Counterparties > 3 005,06 € including IVA, without transactions from the 349, with retención and the administrador's remuneration. |
| 18 | Modelo 100 (estimate) | B | State + regional scale for the year (Valencia 2025/2026/2027, Asturias 2025/2026 with published cuota fija), mínimo personal, reducción inicio 20 % (if the profile states the first profitable year), minus the filed 130 and retenciones. The region is where you spent more days in the year (art. 72). |
| 19 | Modelo 151 (estimate) | A | 24 % / 47 % on all revenue (expenses and RETA do not reduce the base), minus retenciones and the 210 paid voluntarily from the questionnaire (in [34]/[37]; where to enter them after the year of the move is disputed). |
| 20 | Modelo 200 (estimate) | C | Micro rates: 2024: 23 %, 2025: 21/22 %, 2026: 19/21 %, 2027: 17/20 % (the 50 000 € threshold is prorated for a short first period); 15 % empresa emergente; minus the filed 202. |
| 21 | RETA: tramo and regularisation | A B C | Income for SS → tramo → min./max. base → expected extra payment/refund compared with the current base, only for the months after the tarifa plana. For C: the minimum base for societario. For A: a note that the TGSS has not set a criterion for the 151. |
| 22 | IVA a compensar between years | A B C | By default 4T means a refund. If you kept it a compensar, the amount is entered in the profile and goes into casilla 110 of the first quarter. |
| 23 | Accounting books | A B C | CSV libro de facturas emitidas and recibidas (separator `;`, BOM for Excel). |

## Trust in the figures

| # | Scenario | What the service does |
|---|---|---|
| 31 | Why is this casilla what it is? | A § sign next to every casilla, note and warning. The card shows: what it means, the status (stated in the text / interpretation / disputed), the Spanish quote, a translation, links to the original and to an automatic translation of the page, DGT and court practice. |
| 32 | What does this field mean? | Under every field of the questionnaire, invoice, expense and client: what it affects, then each law: its gist in one sentence, a link to the entry in "Sources" and to the original. For the expense category and the IVA type the block changes together with the choice. |
| 34 | How did gestor understand me? | In "Profile", above the questionnaire: conclusions from the answers in plain sentences; which returns you file and why you in particular (with the law); which ones you do not file and why; where the law is unclear in your case. |
| 35 | Does my filing match the calculation? | The amount from the Sede entered when marking "filed" is compared with the current calculation. If they differ: a warning and a link to the autoliquidación rectificativa. |
| 36 | How do I file and what comes next? | Each return has a "Next" block: what to do now (file and pay, file without payment, wait for the window, the deadline has passed, keep the justificante, wait for the TGSS recalculation) and the links "How to file" (/guide: steps based on the AEAT help) and "Open in the Sede". Casillas are labelled in Spanish, as in the form, and in the interface language on the line below (the Spanish interface has no second line). |
| 37 | Can I avoid retyping the casillas? | "Download the file for the Sede" in the "Next" block of the 130, 303 (2026), 349 and 151: a text file based on the official AEAT diseño de registro (`gestor/dr/*.json`, extracted by `scripts/dr_extract.py`). In the Sede form: "Importar", then "Validar" and "Firmar y enviar". For the 151, gender, date of birth, the IAE epígrafe and phone number are taken from the questionnaire; the form will ask for the address. The files have not yet been tested on the real Sede. |
| 38 | Help me fill in the form in the Sede | The MCP server `gestor/mcp.py` for Claude Code and Codex with the user's subscription: casillas in the Sede format, the file for "Importar", status and deadline. An agent in the browser fills in the form and checks it after "Validar", but does not sign or submit it. Not yet tested on the real Sede. |
| 39 | Does my censo match what gestor calculates? | The questionnaire has the certificado censal date and the obligations with ALTA status (303, 130, 111, 115, ROI). "How gestor understood you" shows the differences: gestor expects a return without an alta, an alta without a return, a 349 without ROI. Changes: Modelo 036 within one month. The phone number from the questionnaire goes into the 349 and 151 files. |
| 40 | How much have I paid and how much is still to come? | The overview "Taxes and RETA for the year": columns by quarter and for the year, a table of modelo × quarter. Paid: the filing marks (130, 303, 111, 115, 202), the 210 by quarter from the questionnaire, RETA from the expenses. Still due: gestor's calculation, RETA until the end of the year based on the last contribution, the annual 100/151/200. For Beckham the total is a range: only what has been invoiced, or that plus an average quarter of the last year. |
| 41 | Interface in English, Russian and Spanish | The language is stored in the profile: chosen in the "Questionnaire" or in the profile menu (EN RU ES). The default is the browser language. Cards of legal sources show the title, the gist and the translation of the quote in the chosen language; in Spanish only the original is shown. The MCP server answers in the profile language. |
| 33 | Where may gestor be wrong? | "Sources" starts with the disputed points and says which cautious option was chosen. Each source shows the date it was checked. |

## Residence status and regimes

| # | Scenario | What the service does |
|---|---|---|
| 24 | Nomad visa | A warning when Spanish clients are > 18 % of revenue over 12 months (the limit is 20 %). |
| 25 | Beckham + nomad / cuenta propia | A warning: ordinary self-employment = establecimiento permanente → exclusion from the regime. |
| 26 | End of Beckham | A warning in the last year. From the following year the service switches to 100/130 by itself. |
| 27 | Modelo 149 deadline | A reminder before the date "alta RETA + 6 months". |
| 28 | Moving between autonomous communities | Lines "date region" in the profile. The region for the year is calculated by days. For cuenta propia: a warning about the regional link of the first permit. |
| 29 | Residence permit renewal | 120 days before the expiry date: a list of documents. |
| 30 | Several profiles | A separate database for each profile (personal autónomo, SL), a switch in the header. |

## What it does not do (on purpose)

- It does not file returns with the AEAT: filing happens in the Sede (Cl@ve / certificate). gestor provides the casillas and the file for "Importar". The user signs and submits.
- It does not create Verifactu records (mandatory for autónomos from 01.07.2027; a postponement to 10.2028 has been announced).
- It does not calculate dividends, savings, children, mortgage, regional deductions, reserva de capitalización, OSS (369), 720/721: only reminders.
- 349: the monthly breakdown and correction records for past periods are done manually (the service warns about this).
