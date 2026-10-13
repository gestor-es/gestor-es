*Translated from the Spanish original [docs/use-cases.md](../use-cases.md) on 13.10.2026. The Spanish file is the source of truth.*

# Use cases

Profiles: **A** — autónomo + Beckham, **B** — autónomo under the general IRPF, **C** — Sociedad Limitada.
The residence status is chosen in the profile: entrepreneur visa, digital nomad visa, self-employment residence permit, EU / no restrictions.
Sources of the rules: `kb/*.md`.

## Every month

| # | Scenario | Profiles | What the service does |
|---|---|---|---|
| 1 | Issue an invoice to a foreign client (outside the EU) | A B C | IVA regime «no sujeta» based on the client's country, mention of art. 69.Uno.1º, ECB exchange rate on the date of the transaction (or manual), base and cuota in EUR. The number is assigned on issue. It is sequential and follows the dates. It uses the format from the questionnaire (for example FACT-{YYYY}-{NNNNN} → FACT-2026-00001). The details of the parties are fixed in the invoice. |
| 2 | Invoice to an EU client (B2B) | A B C | Mention «inversión del sujeto pasivo», casilla 59 of the 303, line with key S in the 349. Without the client's VAT ID and address, the invoice is not issued. |
| 3 | Invoice to a Spanish company | A B C | IVA 21 %. Retención: 15 % (7 % in the start year and the 2 following years) — B; 24 % — A; 0 % — C and business activity. |
| 4 | Correct an issued invoice | A B C | Only with a factura rectificativa (series R), with a mandatory reason and a reference to the original invoice. A draft can be changed and deleted. |
| 5 | Mark the payment as received | A B C | Payment date on the invoice. |
| 6 | Record an expense with a receipt | A B C | The category sets the % that goes into the taxable base and the % of deductible IVA. The receipt is stored in `<data>/receipts`. EU / non-EU supplier without IVA → autorrepercusión (10/11 + 36/37 or 12/13 + 28/29). Equipment over 300 € is depreciated (26 % autónomo, 25 % SL). Health insurance: no more than 500 € per year. Meals: only the % that you enter (limits per day). |
| 7 | Record the cuota RETA | A B C | Category «Cuota RETA»: B — expense (casilla 0186); A — does not reduce the base of the 151; C — payment in kind to the director (111). |
| 8 | Pay a Spanish professional or the rent of an office with retención | A B C | The expense field «Retención que usted practicó» → Modelo 111 (professionals) or 115 (rent). The annual 190/180 appear in the calendar. |

## Every quarter

| # | Scenario | Profiles | What the service does |
|---|---|---|---|
| 9 | Modelo 303 | A B C | All casillas from the transactions of the quarter, cuotas «a compensar» between quarters, refund request in 4T. |
| 10 | Modelo 130 | B | Cumulative amount, 20 %, 5 % gastos de difícil justificación (≤ 2 000 €), minoración art. 110.3.c (without data for the previous year: 0), carry-over of negative results. It is not filed if in the previous year ≥ 70 % of the income had retención (professionals only). |
| 11 | No 130 and no 210 with Beckham | A | The 130 is not shown (it is disputed whether the general 130 applies to the activity inside the regime; see «Where can gestor be wrong»). The quarterly 210 is not needed: it is a modelo for non-residents, and a client with no presence in Spain does not withhold (sources: `gestor/sources/beckham.json`). The overview shows the amount «to set aside» according to the 24 % / 47 % scale. |
| 12 | Modelo 349 | A B C | Only if there were transactions with the EU: clients (S) and suppliers (I). If they exceed 50 000 € in a quarter: warning about monthly filing. |
| 13 | Modelo 202 | C | Modalidad 40.2: 18 % of the base of the last Modelo 200 (it is entered in the profile; without it, an estimate from the invoices or a reminder to enter it). It is not filed in the first year. |
| 14 | Modelo 111 / 115 | A B C | SL: retención 19 % / 35 % on the director's pay and on the RETA paid by the SL (without a turnover for the previous year: 35 %). All: retenciones withheld from professionals and landlords. |
| 15 | Mark the filing | A B C | Amount of the filed return, date, Código Seguro de Verificación (CSV) of the justificante de presentación. The mark can be undone. The annual 100/200 take into account only the filed pagos fraccionados. |

## Every year

| # | Scenario | Profiles | What the service does |
|---|---|---|---|
| 16 | Modelo 390 | A B C | Annual summary return of the 303 of the year, rectificativas, turnover. |
| 17 | Modelo 347 | A B C | Transactions with third parties > 3 005,06 € including IVA, without the transactions of the 349, without the transactions with retención and without the director's pay. |
| 18 | Modelo 100 (estimate) | B | State + regional scale of the year (Valencia 2025/2026/2027, Asturias 2025/2026 with a published fixed cuota), personal allowance, start reduction 20 % (if the profile states the first year with a positive return), minus the filed 130 and the retenciones. Region: the one where you spent the most days of the year (art. 72). |
| 19 | Modelo 151 (estimate) | A | 24 % / 47 % on all income (expenses and the RETA do not reduce the base), minus the retenciones and the 210 paid voluntarily according to the questionnaire (in [34]/[37]; where to declare them after the year of the move is disputed). |
| 20 | Modelo 200 (estimate) | C | Micro rates: 2024 — 23 %, 2025 — 21/22 %, 2026 — 19/21 %, 2027 — 17/20 % (the 50 000 € threshold is proportional for a short first period); 15 % empresa emergente; minus the filed 202. |
| 21 | RETA: band and regularisation | A B C | Return for the SS → band → min./max. base → expected regularisation (to pay or to refund) against the current base, only for the months after the tarifa plana. For C: minimum base for company owners (societario). For A: note that the TGSS has not set a criterion for the 151. |
| 22 | IVA cuotas a compensar between tax years | A B C | By default, in 4T: refund request. If you left it «a compensar», the amount is entered in the profile and goes to casilla 110 («Cuotas a compensar pendientes de períodos anteriores») of the first quarter. |
| 23 | Libros registro | A B C | CSV book of issued and received invoices (separator `;`, BOM for Excel). |

## Trust in the figures

| # | Scenario | What the service does |
|---|---|---|
| 31 | Why does this casilla have this value? | § symbol on each casilla, note and warning. On the card: what it means, status (stated in the text / interpretation / disputed), quote in Spanish, translation, links to the original and to the machine translation of the page, DGT and court practice. |
| 32 | What does this field mean? | Under each field of the questionnaire, the invoice, the expense and the client: what it affects. Then each rule: its content in one sentence, a link to the entry in «Sources» and to the original. For the expense category and the IVA rate, the block changes with the selection. |
| 34 | How did gestor understand me? | In «Profile», above the questionnaire: conclusions from your answers in plain sentences; which returns you file and why they apply to you (with the rule); which you do not file and why; where the law is not clear in your case. |
| 35 | Does my filing match the calculation? | The amount from the Sede that you enter when you mark «filed» is compared with the current calculation. If there is a difference: warning and a link to the autoliquidación rectificativa. |
| 36 | How do I file and what do I do next? | Each return has a «Next» block: what to do now (file «a ingresar», file «sin ingreso», wait for the filing period to open, late filing, keep the justificante de presentación, wait for the TGSS regularisation) and the links «How to file» (/guide: steps based on the AEAT technical help) and «Open in the Sede». The casillas carry their Spanish name, as on the form; in English and in Russian, a line in the interface language is shown below it. |
| 37 | Can I avoid typing the casillas again? | «Download the file for the Sede» in the «Next» block of the 130, 303 (2026), 349 and 151: a text file based on the official AEAT record layout (`gestor/dr/*.json`, extracted with `scripts/dr_extract.py`). On the Sede form: «Importar», then «Validar declaración» and «Firmar y enviar». Sex, date of birth, epígrafe IAE and telephone for the 151 are taken from the questionnaire. The form will ask for the address. The files have not yet been tested on the real Sede. |
| 38 | Help to fill in the form on the Sede | MCP server `gestor/mcp.py` for Claude Code and Codex with the user's subscription: casillas in the Sede format, file for «Importar», status and deadline. The agent fills in the form in the browser and checks it after «Validar declaración», but it does not press «Firmar y enviar». It has not yet been tested on the real Sede. |
| 39 | Does my censo match what gestor calculates? | In the questionnaire: date of the certificado de situación censal and obligations in ALTA status (303, 130, 111, 115, ROI). In «How gestor understood you»: the differences (gestor expects a return without an alta, there is an alta without a return, 349 without an alta in the Registro de Operadores Intracomunitarios). Census changes are reported with Modelo 036 within one month. The telephone from the questionnaire is included in the files of the 349 and the 151. |
| 40 | How much have I paid and how much is left? | In the overview, «Taxes and RETA for the year»: columns per quarter and for the year, table modelo × quarter. Paid: filing marks (130, 303, 111, 115, 202), 210 per quarter according to the questionnaire, RETA according to the expenses. Outstanding: gestor's calculation, RETA until the end of the year based on the last cuota, annual 100/151/200. For Beckham the total is a range: only what has been invoiced, or what has been invoiced plus an average quarter of the last year. |
| 41 | Interface in English, Russian and Spanish | The language is stored in the profile: you choose it in the «Questionnaire» or in the profile menu (EN RU ES). By default the browser language is used. Legal source cards: title, content and translation of the quote in the chosen language; in Spanish, only the original. The MCP server answers in the language of the profile. |
| 33 | Where can gestor be wrong? | «Sources» starts with the disputed points and states which prudent option was chosen. Each source has its check date. |

## Residence status and regimes

| # | Scenario | What the service does |
|---|---|---|
| 24 | Digital nomad visa | Warning when Spanish clients exceed 18 % of the income in 12 months (limit 20 %). |
| 25 | Beckham + nomad / self-employment | Warning: normal self-employed work = permanent establishment → exclusion from the regime. |
| 26 | End of Beckham | In the last year: warning. From the next year, the service switches to the 100/130 by itself. |
| 27 | Deadline of Modelo 149 | Reminder before the date «alta RETA + 6 months». |
| 28 | Move between autonomous regions | Lines «date region» in the profile. The region of the year is calculated by days. For self-employment: warning about the territorial link of the first permit. |
| 29 | Renewal of the residence permit | 120 days before the expiry date: list of documents. |
| 30 | Several profiles | One database per profile (personal autónomo, SL), selector in the header. |

## What it does not do (on purpose)

- It does not file returns with the AEAT: filing happens on the Sede electrónica (Cl@ve / electronic certificate). gestor gives the casillas and the file for «Importar». The user presses «Firmar y enviar».
- It does not generate Verifactu records (mandatory for autónomos from 01.07.2027; a postponement to 10.2028 has been announced).
- It does not calculate dividends, savings, children, mortgage, regional deductions, reserva de capitalización, OSS (369), 720/721: only reminders.
- 349: the monthly breakdown and the correction records for earlier periods are done by hand (the service warns).
