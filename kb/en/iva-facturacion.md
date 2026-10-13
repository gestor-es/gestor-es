*Translated from the Russian original [kb/iva-facturacion.md](../iva-facturacion.md) on 13.10.2026. The Russian file is the source of truth; facts were checked as of the date stated below.*

# IVA and invoicing (facturación) for autónomos / SLs that provide services

Status as of 2026-10-08. Sources are primary (BOE, AEAT Sede, DGT). Everything that could not be confirmed by a primary source is marked **UNVERIFIED** or `[INFERENCE]`.

## Summary

- IVA does not depend on the Beckham regime, on the region (Valencia/Asturias) or on the legal form (autónomo/SL): the rules are the same. The region matters only for Canarias/Ceuta/Melilla (there is no IVA there; IGIC/IPSI applies instead).
- B2B services to a business customer in another EU country: **no sujeta** in Spain (art. 69.Uno.1º LIVA). The customer pays the IVA by reverse charge. Registration in the ROI is required (Modelo 036, casilla 582). The customer's NIF-IVA is checked in VIES. Modelo 303 → casilla **59**; Modelo 349 → clave **S**.
- B2B services to a customer outside the EU (USA etc.): **no sujeta** (art. 69.Uno.1º), without a reverse charge statement. Since 2023 the "uso efectivo" rule (art. 70.Dos) does not apply to B2B services of our type. Modelo 303 → casilla **120**; the operation does not go into the 349.
- Spanish customer (B2B or B2C): IVA 21 %. If the customer is an empresario/profesional and the provider is an individual with a *professional* activity, the invoice shows a retención IRPF: 15 % (7 % in the first 3 years) in the ordinary regime; **24 %** in the Beckham regime. With an *empresarial* activity and for an SL there is no retención.
- B2C to a customer in the EU: Spanish IVA 21 % (art. 69.Uno.2º). The exception is electronic/telecom services: up to 10 000 €/year, Spanish IVA applies; above that (or by option), the IVA of the customer's country applies through OSS (Modelo 369, casilla 123 in the 303).
- B2C to a customer outside the EU: consulting/development/data processing (the list in art. 69.Dos) and electronic services are **no sujeta** (casilla 120); everything else is 21 %.
- The right to deduct input IVA is **kept** when services are provided to foreign customers (art. 94.Uno.2º LIVA). Prorrata is not needed if there are no exentas sin derecho (art. 20). Typical profile (all customers abroad) ⇒ the 303 is almost always "a compensar". A refund is possible only in 4T (casilla 73) or through REDEME/SII.
- Services received from EU suppliers (SaaS etc.): autorrepercusión, casillas 10/11 and 36/37, 349 clave **I**. From suppliers outside the EU: casillas 12/13 and 28/29; this does not go into the 349.
- Invoice (RD 1619/2012 art. 6): number/series, date, parties with NIF and addresses, description, base, tipo, cuota, date of the operation if different, mandatory statements for exentas/no sujetas/ISP. Any currency is allowed, but the **cuota IVA must be in euros** at the exchange rate on the devengo date. Simplificada ≤ 400 € including IVA, but it is forbidden for invoices to foreign customers (art. 4.4.d).
- Modelo 390 is **mandatory** for our profile (only módulos/rental of real estate/SII are exempt). Modelo 347 covers only counterparties > 3 005,06 €/year, excluding operations reported in the 349 and operations with retención.
- Verifactu (RD 1007/2023, Orden HAC/1177/2024): under RDL 15/2025 the deadlines are: IS from 01.01.2027, all others (IRPF autónomo) from 01.07.2027. **On 05.10.2026 Hacienda announced a postponement to October 2028**; the legal act has not been published yet. Self-written software must comply (SHA-256 hash chain, QR 30–40 mm, XML records) and must have its own declaración responsable.
- B2B electronic invoice (Ley Crea y Crece, RD 238/2026, Orden HAC/1028/2026): mandatory for business recipients in Spain from **06.10.2027** (turnover > 8 million) and **06.10.2028** (everyone else). It does not apply to foreign customers.
- Books (libros registro): facturas expedidas, recibidas, bienes de inversión. The official AEAT format is XLSX (LSI.xlsx) with the sheets EXPEDIDAS_INGRESOS / RECIBIDAS_GASTOS / BIENES-INVERSIÓN. The same file is imported into Pre303, Renta Web and Modelo 130.
- Invoice retention: the LGT prescripción period (4 years from the end of the filing period of the corresponding return). For bienes de inversión it is longer (regularisation period + 4 years). For an SL there are additionally 6 years under the Código de Comercio.

## Rules

1. **General place-of-supply rule for B2B services**: the service is located where the business customer is (sede/EP/domicilio). If the customer is not in the TAI (Península+Baleares), the operation is *no sujeta* in Spain. In force since 01.01.2010 (Ley 2/2010). Source: art. 69.Uno.1º LIVA, https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a69
2. **General B2C rule**: the service is located where the provider is (TAI) ⇒ Spanish IVA 21 %. Exception in art. 69.Dos: the listed services (IP rights, advertising, asesoramiento/consultores/ingeniería/abogacía, tratamiento de datos y suministro de informaciones, traducción, cesión de personal, rental of movable property and others) to a non-business customer **outside the EU** (not Canarias/Ceuta/Melilla) are no sujetas. Source: art. 69.Dos LIVA (same link).
3. **Electronic B2C services** (hosting, SaaS/subscriptions, downloadable software, online courses without human involvement; art. 69.Tres.4º): for a customer in another EU country, Spanish IVA applies as long as the total of such services + ventas a distancia does not exceed **10 000 €** (without IVA) in the current and the previous year, and there is no option for taxation at destino (art. 70.Uno.8º, art. 73). Above that, the IVA of the customer's country applies (OSS/Modelo 369). Customer outside the EU: no sujeta (AEAT). Sources: art. 70.Uno.4º/8º, art. 73 LIVA; AEAT "IVA telecomunicaciones y servicios electrónicos" https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html
4. **Uso efectivo (art. 70.Dos)**: after Ley 31/2022 and Ley 13/2023 it applies only to (1) art. 69.Dos services to non-business customers and (2) rental of means of transport, if they are actually used in the TAI. It does not apply to B2B consulting/development for a customer outside the EU. Source: art. 70.Dos LIVA (consolidated text).
5. **Sujeto pasivo when receiving services from a non-resident** (art. 84.Uno.2º.a): the business recipient in the TAI charges the IVA itself (inversión del sujeto pasivo). The document for the deduction is the supplier's invoice or a justificante contable (art. 97.Uno.4º). A separate "autofactura" is not needed. Source: art. 84, 97 LIVA.
6. **Right to deduct** (art. 94.Uno): the right arises, among others, under point 2º: operations outside the TAI that would give the right to deduct if made inside. ⇒ services to foreign customers (B2B EU/outside the EU, no sujetas) **give the right to deduct**. Prorrata (art. 102–106) applies only if there are at the same time operations with and without the right to deduct (exentas art. 20). Source: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a94
7. **Limits on deduction**: art. 95: only expenses directly and exclusively related to the activity. Bienes de inversión in partial use: proportionally. Cars (turismos): a presumption of **50 %** (the same 50 % applies to fuel, parking, repairs and spare parts; art. 95.Cuatro). art. 96: never deductible: jewellery, food/drinks/tobacco, shows, atenciones a clientes, travel/hotels/restaurants, except when the expense is deductible in IRPF/IS. Source: art. 95–96 LIVA.
8. **Formal requirements for deduction** (art. 97): an original invoice in the taxpayer's name with all the details of art. 6 RD 1619/2012. A "ticket" (factura simplificada without the recipient's NIF) does not give a deduction, unless the seller added the recipient's NIF and address and showed the cuota on a separate line (art. 7.2 RD 1619/2012). The deduction must be used within 4 years from devengo (art. 99.Tres, 100 LIVA).
9. **Devengo of services** (art. 75): when the service is provided (75.Uno.2º). With prepayment: when the payment is received (75.Dos). Continuous services (tracto sucesivo, 75.Uno.7º): when each part of the price becomes exigible. If exigibilidad does not occur within a year: on 31 December of each year. Source: art. 75 LIVA.
10. **Obligation to issue an invoice** (RD 1619/2012 art. 2): for all operations, including no sujetas and exentas, if the customer is an empresario/profesional or a persona jurídica, and when the operation is located outside the TAI but the provider is in the TAI (art. 2.3.b.b’). Deadline: B2B, by the 16th day of the month after devengo (art. 11); B2C, at the time of the operation. The invoice must be sent to the customer within the same deadline (art. 18). Source: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
11. **Content of the invoice** (art. 6 RD 1619/2012): a) number and series (consecutive numbering within a series; separate series are mandatory for rectificativas and for invoices issued by the recipient/a third party); b) date of issue; c) full names/company names of the parties; d) the provider's NIF; the customer's NIF is mandatory for ISP, for operations in the TAI and for EIB; e) addresses of the parties; f) description, unit price without IVA, discounts; g) tipo; h) cuota shown separately; i) date of the operation, if different; j) for an exención, a reference to the article of Directiva 2006/112/CE or LIVA, or the word "exenta"; m) "inversión del sujeto pasivo", if the recipient is the taxpayer; p) "régimen especial del criterio de caja". For operations under art. 2.3.b.b’.a’’ (EU B2B) items f/g/h may be omitted if the volume and nature of the service and the taxable amount are stated (art. 6.3). Since 07.12.2023, art. 6.5: when a SIF is used, a QR code and (only in VERI*FACTU mode) the phrase "VERI*FACTU"/"Factura verificable en la sede electrónica de la AEAT".
12. **Factura simplificada** (art. 4, 7): up to 400 € including IVA (up to 3 000 € for the listed retail activities) and for rectificativas. It is **not allowed** for EIB and for operations located outside the TAI (art. 4.4.d → art. 2.3.b.b’). This means that foreign customers always get a full invoice.
13. **Factura rectificativa** (art. 15): mandatory when there is an error in the invoice details, a wrong cuota or a change in the base (art. 80 LIVA). It is issued as soon as the reason is found, within 4 years from devengo, in a separate series. It contains the details of the corrected invoice and the nature of the correction. Amounts are shown either as the difference (with sign) or "as they should be" with the difference stated. Reporting in the 303: casillas 14/15 (change of base/cuota) for operations with IVA. For no sujetas, the amount in casilla 59/120 of the period is corrected.
14. **Currency and language** (art. 12 RD 1619/2012; art. 79.Once LIVA): amounts may be in any currency, but the cuota IVA must be in euros at the "tipo de cambio vendedor fijado por el Banco de España" on the devengo date. According to DGT V2630-17, the BdE does not fix a rate. The ECB reference rate (published by the BdE) is used. Another publicly available source is allowed if it is used consistently and does not deviate materially. Any language is allowed; the AEAT may require a translation into castellano.
15. **Retention** (art. 19–23 RD 1619/2012; art. 66–70 LGT): invoices received, copies of invoices issued, justificantes contables and DUA must be kept for the prescripción period (4 years). Authenticity, integrity, legibility and online access for the AEAT must be guaranteed. Storage outside Spain is allowed only electronically, with remote access and prior notice to the AEAT. For bienes de inversión: until the end of the regularisation period (5 years; real estate 10) + prescripción. For an SL: 6 years under art. 30 Código de Comercio.
16. **ROI / NIF-IVA**: before the first intra-community operation, file Modelo 036 with casilla **582** (alta ROI) and the date of the first operation in casilla **584**. Modelo 037 was abolished from 03.02.2025 (Orden HAC/1526/2024). No reply from the AEAT within 3 months = refusal. Source: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html ; BOE-A-2025-410.
17. **Modelo 303**: quarterly (1–20 April/July/October; 4T: 1–30 January). A refund (casilla 73) is possible only in the last return of the year, if there is no REDEME (art. 30 RIVA). In 1T–3T a negative result can only be "a compensar" (casilla 72). A result "a compensar" is not allowed if cuotas from previous periods were applied in the same period (casilla 78 is filled in). Source: Instrucciones 303 2026, https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
18. **Modelo 390**: mandatory for everyone who files periodic 303 returns, except (a) quarterly filers only in régimen simplificado and/or urban real estate rental and (b) SII. Deadline 1–30 January. Source: Instrucciones 390-2025, https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
19. **Modelo 349**: filed for each period in which there were operations with the claves E/A/S/I/T/M/H/R/D/C. The filing is quarterly if the total of EIB + EU services (claves E, S and others) did not exceed **50 000 €** without IVA in the current quarter or in any of the 4 previous quarters. Otherwise it is monthly (if the threshold is exceeded in the 2nd month: "trimestre truncado"). Deadlines: 1–20 of the following month; for the last period of the year: 1–30 January; July: by 20 September (monthly filers). Source: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
20. **Modelo 347**: annually in February (1–28/29). It covers counterparties with whom the total for the year is > **3 005,06 €** (including IVA), split by quarter. Excluded: operations without an invoicing obligation, import/export of goods, operations already reported in other periodic returns with the same content (349, retenciones 190/180). Not filed by: SII filers, persons with only excluded operations. Source: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
21. **Retención IRPF on a professional's invoice** to a Spanish business payer: 15 % (art. 101.5.a LIRPF). 7 % in the start year and the two following years, if no professional activity was carried out in the previous year and the customer received a written notice (art. 95.1 RIRPF). Beckham regime: withholding under the IRNR rules: professional activity **24 %**, empresarial activity: no withholding (art. 114 RIRPF as amended by RD 1008/2023). Sources: https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
22. **Verifactu: scope and deadlines**: the RRSIF (RD 1007/2023) applies to IS taxpayers, IRPF taxpayers with actividades económicas, IRNR taxpayers with an EP, and ERAR. It does not apply to SII. Deadlines under RDL 15/2025: IS, by 01.01.2027; all others, by 01.07.2027. On 05.10.2026 the Ministry announced its intention to postpone to **October 2028** (aligned with e-factura). Until the rule is published, the 2027 dates apply. Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf ; https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
23. **Verifactu: requirements for a SIF** (RRSIF art. 8–16; Orden HAC/1177/2024 art. 10–21): for each invoice, a registro de facturación de alta (XML UTF-8); for a cancellation, a registro de anulación. A SHA-256 huella with chaining (the Huella field of the previous record). Either all records are sent to the AEAT (VERI*FACTU mode, web service, flow control 60 s), or they are signed with XAdES using a qualified certificate + a registro de eventos. QR 30×30–40×40 mm, ISO/IEC 18004, level M, with the AEAT URL (NIF, serie+número, fecha, importe total). The phrase "VERI*FACTU" only when records are sent. Source: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
24. **Declaración responsable** (RRSIF art. 13; OM art. 15): mandatory for each version of any SIF, including **self-written software for own use**. The developer-user certifies it themselves. There is no external certification or registration. Source: AEAT FAQ, https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
25. **Factura electrónica B2B** (Ley 18/2022 art. 12; RD 238/2026; Orden HAC/1028/2026, in force from 06.10.2026): mandatory when the recipient is an empresario/profesional with sede/EP/domicilio in Spain. Not for simplificadas (except art. 7.2). Deadlines: 06.10.2027 for issuers with turnover > 8 million €; 06.10.2028 for all others. Reporting of statuses (accepted/paid): 06.10.2027 / 06.10.2028 (legal entities) / 06.10.2029 (individuals). Source: https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html ; https://www.boe.es/eli/es/rd/2026/03/25/238/con
26. **Libros registro** (art. 62–70 RIVA; Orden HAC/773/2019 for IRPF): facturas expedidas, recibidas, bienes de inversión (+ determinadas operaciones intracomunitarias, not relevant for us). Entries in euros, in chronological order, with quarterly totals; rectificativas are recorded separately. AEAT electronic format: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; field design: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx
27. **Volumen de operaciones** (art. 121 LIVA) = the total contraprestaciones of all operations of the year (including operations no sujetas by location rules and exentas), without IVA. Sales of bienes de inversión and occasional financial/real estate operations are excluded. It is used in the 303 (4T, casilla 88 for filers exempt from the 390), in the 390 (casilla 108) and for the 8 million e-factura threshold.

## Figures

### Rates and thresholds (2025 and 2026: no changes for our profile)

| Parameter | 2025 | 2026 | Source |
|---|---|---|---|
| Tipo general IVA | 21 % | 21 % | art. 90 LIVA |
| Tipo reducido / superreducido | 10 % / 4 % (0 % and 5 %/7,5 % applied only to food products until 2024) | 10 % / 4 % | art. 91 LIVA |
| OSS threshold (B2C electronic + EU ventas a distancia) | 10 000 € without IVA | 10 000 € | art. 73 LIVA |
| Monthly 349 threshold | 50 000 € without IVA (quarter and 4 previous) | 50 000 € | art. 81 RIVA |
| 347 threshold per counterparty | > 3 005,06 € including IVA | > 3 005,06 € | art. 33 RGAT |
| Bien de inversión (IVA) | ≥ 3 005,06 € and use > 1 year | same | art. 108 LIVA |
| Factura simplificada | ≤ 400 € including IVA (≤ 3 000 € for retail) | same | art. 4 RD 1619/2012 |
| Presumed affectación of a car | 50 % | 50 % | art. 95.Tres.2ª LIVA |
| Prorrata: rounding | up to a whole % | same | art. 104.Dos LIVA |
| Prorrata especial is mandatory | if the general one gives ≥ 10 % more deduction | same | art. 103.Dos.2º |
| Gran empresa (monthly 303, SII) | > 6 010 121,04 € turnover in the previous year | same | art. 71.3 RIVA |
| Retención profesional (ordinary IRPF) | 15 % / 7 % (start) | 15 % / 7 % | art. 101.5 LIRPF, 95.1 RIRPF |
| Retención profesional (Beckham, IRNR) | 24 % | 24 % | art. 114 RIRPF |
| Period for deducting input IVA | 4 years from devengo | 4 years | art. 99–100 LIVA |
| Invoice retention | 4 years (prescripción) | 4 years | art. 66 LGT, art. 19 RD 1619/2012 |
| Deadline for issuing a B2B invoice | by the 16th day of the following month | same | art. 11 RD 1619/2012 |

### Deadlines (calendar)

| Modelo | Period | Deadline | Domiciliación (−5 days) |
|---|---|---|---|
| 303 | 1T/2T/3T | 1–20 Apr / Jul / Oct | by the 15th |
| 303 | 4T | 1–30 January | by 25 January |
| 390 | year | 1–30 January | — |
| 349 quarterly | 1T–3T | 1–20 Apr / Jul / Oct | — |
| 349 | 4T (or December) | 1–30 January | — |
| 347 | year | 1–28(29) February | — |
| 369 (OSS) | quarter | by the end of the month after the quarter | — |
| 036 alta ROI | — | before the first EU operation | — |
| 036 change of domicilio fiscal | — | 1 month from the change (art. 10 RGAT) | — |

If the last day is a weekend day or a public holiday, the deadline moves to the next working day (AEAT calendario).

### Verifactu / e-factura: dates

| Obligation | Date | Status |
|---|---|---|
| SIF adapted: IS taxpayers | 01.01.2027 | in force (RDL 15/2025) |
| SIF adapted: IRPF autónomos and others | 01.07.2027 | in force (RDL 15/2025) |
| Postponement of the whole RRSIF to October 2028 | ~10.2028 | announced 05.10.2026, **rule not published** |
| e-factura B2B, turnover > 8 million € | 06.10.2027 | in force (RD 238/2026 + OM HAC/1028/2026) |
| e-factura B2B, all others (our profile) | 06.10.2028 | in force |
| Reporting of e-factura statuses, individuals | 06.10.2029 | in force |

### Modelo 303 casillas (2025/2026 form): map for our profile

| Operation | Devengado (base/tipo/cuota) | Deducible (base/cuota) | Informativas | 349 |
|---|---|---|---|---|
| Sale to a Spanish customer 21 % | 07 / 08 / 09 | — | — | — |
| Sale B2B to an EU customer (service) | — | — | **59** | S |
| Sale B2B to a customer outside the EU, Canarias/Ceuta/Melilla | — | — | **120** | — |
| Sale B2C outside the EU of art. 69.Dos / electronic services | — | — | 120 | — |
| Sale B2C in the EU of electronic services through OSS | — (in the 369) | — | 123 | — |
| Export of goods (art. 21) | — | — | 60 | — |
| Operations with ISP where the Spanish customer is the taxpayer (art. 84.Uno.2º c–g; not our case) | — | — | 122 | — |
| Purchase from a Spanish supplier (current) | — | 28 / 29 | — | — |
| Purchase of a bien de inversión in Spain | — | 30 / 31 | — | — |
| Import of goods (DUA) | — | 32 / 33 (34/35 investment) | — | — |
| Service from an EU supplier (AIS) | **10 / 11** | **36 / 37** | — | I |
| Goods from the EU (AIB) | 10 / 11 | 36 / 37 (38/39 investment) | — | A |
| Service from a supplier outside the EU (ISP art. 84.Uno.2º.a) | **12 / 13** | **28 / 29** | — | — |
| Rectificativa with IVA (±) | 14 / 15 | 40 / 41 (received) | — | — |
| Totals | 27 = 152+167+03+155+06+09+11+13+15+158+170+18+21+24+26 | 45 = 29+31+33+35+37+39+41+42+43+44 | 46 = 27 − 45 | |
| Result | 64 = 46+58+76; 65 = 100 %; 66 = 64; 110 (prev. balance); 78 (applied); 87 = 110−78; 69 = 66+77−78+68+108; 71 = 69−70+109 | | 72 (compensar) / 73 (devolver, 4T only) | |

### Modelo 390 casillas (2025): key ones

| Content | Casillas |
|---|---|
| Régimen ordinario by rate (0/4/10/21 %) base/cuota | 01–06, 700–703, 667–670 (21 %: pair 05/06 `[INFERENCE: check against the form]`) |
| Adquisiciones intracomunitarias de servicios base/cuota by rate | 545–548, 551–552, 720–723, 687–690 |
| Adquisiciones intracomunitarias de bienes | 21–26, 716–719, 683–686 |
| Otros supuestos de ISP (supplier outside the EU) | 27 / 28 |
| Modificación bases y cuotas | 29 / 30 |
| Total bases / cuotas devengadas | 33 / 34; 47 (cuotas IVA + RE) |
| Deducible interior corrientes (total) | 48 / 49 (by rate 695–698, 190–191 …) |
| Deducible interior bienes de inversión | 50 / 51 |
| Deducible importaciones corrientes / inversión | 52 / 53; 54 / 55 |
| Resultado régimen general / suma / compensación año anterior / resultado liquidación | 84, 85, 86 |
| Totals of autoliquidaciones: a ingresar / a compensar / a devolver | 95, 97, 98 |
| Volumen de operaciones: régimen general / EIB+servicios EU / exportaciones / exentas sin derecho / no sujetas localización / ISP / OSS / total | 99, 103, 104, 105, 110, 125, 126, 108 |

### Claves for libros registro and Verifactu records

| Field | Values |
|---|---|
| Calificación de la operación | S1 sujeta no exenta sin ISP; S2 sujeta con ISP; N1 no sujeta art. 7/14; **N2 no sujeta por reglas de localización** |
| Operación exenta | E1 art. 20; E2 art. 21; E3 art. 22; E4 art. 23–24; E5 art. 25 (EIB); E6 otras |
| Clave de régimen | 01 general; 02 exportación; 07 criterio de caja; 08 IGIC/IPSI; 17 OSS; 18 recargo equivalencia … |
| Tipo de factura (Verifactu) | F1 completa; F2 simplificada; F3 sustitutiva de simplificadas; R1–R4 rectificativas (R1 error de derecho/art. 80.Uno-Dos-Seis, R2 art. 80.Tres, R3 art. 80.Cuatro, R4 resto); R5 rectificativa de simplificada |
| Tipo NIF destinatario (libros) | 02 EU NIF-IVA; 03 pasaporte; 04 doc. oficial país; 05 certificado residencia; 06 otro documento probatorio; 07 no censado |

## Formulas for the engine

Everywhere: amounts in euros, 2 decimals, rounding `ROUND_HALF_UP` (as in the AEAT forms). The cuota is calculated per invoice (per rate). The already rounded cuota is summed into the books and into the 303. AEAT validations (SII/Verifactu) allow a deviation of `|cuota − base×tipo| ≤ 10 €` per invoice `[per the AEAT validaciones document; confirm the version]`.

### 1. Sale classification (place of supply + invoice regime)

```
input: seller{profile: AUTONOMO_IRPF | AUTONOMO_BECKHAM | SL, activity_kind: PROFESIONAL | EMPRESARIAL, years_since_start, oss_registered}
       customer{country, is_business, vat_id (optional, validated in VIES), spanish_withholder: bool}
       service{kind: GENERAL | ELECTRONIC | ART69DOS (consulting, data processing, IP, advertising, translation...) | IMMOVABLE | OTHER_SPECIAL}
       ytd_b2c_eu_electronic_sales (current year and previous year, without IVA)

TAI  = country == ES and region not in {Canarias, Ceuta, Melilla}
EU   = country in EU27 (excluding ES-TAI; Canarias/Ceuta/Melilla treated as NON_EU for IVA)

if service.kind == IMMOVABLE: locate by property (art. 70.Uno.1º) — outside our profile, STOP

# B2B status: vat_id valid in VIES, or (non-EU) other proof of business (Reg. UE 282/2011 art. 18)
b2b = customer.is_business and (customer.country not in EU or vat_id_valid)

case TAI:
    regime = SUJETA_21
    withholding = compute_withholding(seller, customer)          # see point 3
case EU and b2b:
    regime = NO_SUJETA_INTRACOM                                  # art. 69.Uno.1º; casilla 59; 349 clave S
    require seller in ROI (ES-VAT in VIES) else -> WARN_ROI
case EU and not b2b:
    if service.kind == ELECTRONIC and (ytd_prev > 10000 or ytd_cur + amount > 10000 or seller.oss_registered):
        regime = OSS_DESTINO                                     # IVA of the customer's country, Modelo 369, casilla 123
    else:
        regime = SUJETA_21                                       # art. 69.Uno.2º / 70.Uno.8º
case NON_EU and b2b:
    regime = NO_SUJETA_LOCALIZACION                              # art. 69.Uno.1º; casilla 120
case NON_EU and not b2b:
    if service.kind in {ART69DOS, ELECTRONIC}: regime = NO_SUJETA_LOCALIZACION   # art. 69.Dos / criterio AEAT
    else: regime = SUJETA_21                                     # regla general art. 69.Uno.2º
    if effectively_used_in_TAI(service): regime = SUJETA_21     # art. 70.Dos (B2C art. 69.Dos only)
```

For Canarias/Ceuta/Melilla: B2B → NO_SUJETA_LOCALIZACION (casilla 120, not 59, no 349 is filed); B2C → SUJETA_21 (art. 69.Dos excludes them).

### 2. Invoice lines by regime

```
base      = Σ round(qty × unit_price × (1 − discount), 2)
case SUJETA_21:
    tipo = 21.00; cuota = round(base × 0.21, 2)
    retencion = round(base × withholding_rate, 2)            # only if withholding_rate > 0
    total_factura = base + cuota                              # "Total factura" in the libros is NOT reduced by the retención
    total_a_pagar = base + cuota − retencion
    mentions: []  (with retención: the line "Retención IRPF x %: −N €" and the withholding base)
case NO_SUJETA_INTRACOM:
    tipo = none; cuota = 0; total = base
    required: the seller's NIF-IVA (ES…) and the customer's (with country prefix), both valid in VIES on the invoice date
    mentions: «Operación no sujeta al IVA español por reglas de localización (art. 69.Uno.1º Ley 37/1992)»,
              «Inversión del sujeto pasivo / Reverse charge — art. 196 Directiva 2006/112/CE»
    forbidden: factura simplificada
case NO_SUJETA_LOCALIZACION:
    tipo = none; cuota = 0; total = base
    mentions: «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)»
              (for B2C art. 69.Dos: reference to art. 69.Dos)
    forbidden: factura simplificada
case OSS_DESTINO:
    tipo = rate(customer.country); cuota = round(base × tipo, 2); total = base + cuota
    mentions: «IVA … % (país de consumo …) — Régimen de la Unión OSS»; declared in the 369; in the 303 only casilla 123
```

Currency ≠ EUR: all invoice amounts may be shown in the currency, but add the line "Cuota IVA: N EUR (tipo de cambio BCE dd/mm/aaaa: 1 EUR = X CUR)". No sujetas have no IVA, but the EUR equivalent of the base is still recorded in the book at the rate on the devengo date:

```
fx_date   = devengo_date (date the service is provided / prepayment is received), not the payment date
rate      = ECB_reference_rate(fx_date)   # if a non-working day, the last rate published before the date [INFERENCE; DGT V2630-17 only requires consistency]
base_eur  = round(base_cur / rate, 2)     # ECB quotes 1 EUR = X CUR
cuota_eur = round(base_eur × tipo, 2)
```

### 3. IRPF withholding on the invoice (only to Spanish business customers)

```
if not customer.spanish_withholder: rate = 0          # individual consumer, foreign customer without an EP in Spain
elif seller.profile == SL: rate = 0                   # SL services are not subject to retención (except rental etc.)
elif seller.activity_kind == EMPRESARIAL: rate = 0    # both in the ordinary regime and in Beckham
elif seller.profile == AUTONOMO_BECKHAM: rate = 0.24  # art. 114 RIRPF → normas IRNR
elif start_year ≤ year ≤ start_year + 2 and no_professional_activity_prev_year and notice_given: rate = 0.07
else: rate = 0.15
retencion = round(base × rate, 2)    # the base is the base imponible without IVA
```

The withheld amount counts towards IRPF (Modelo 100/151). It is passed to the IRPF/Beckham module. It is not reported in the 303.

### 4. Expense classification (input IVA)

```
input: supplier{country, vat_id}, invoice{base, tipo, cuota, currency}, item{kind: CURRENT | INVESTMENT | VEHICLE | FOOD_HOTEL_TRAVEL | GIFTS | PRIVATE_MIX}
deductible_share:
    kind == GIFTS or (FOOD_HOTEL_TRAVEL and not deductible_in_IRPF_IS) -> 0       # art. 96
    kind == VEHICLE (turismo) and related costs -> 0.50 (unless proven otherwise)  # art. 95.Tres.2ª, Cuatro
    kind == PRIVATE_MIX (water/electricity/internet of the home) -> 0             # art. 95.Uno; criterio AEAT/TEAC
    otherwise -> 1.00 × prorrata (prorrata = 1.00 if there are no art. 20 operations)
investment = (base ≥ 3005.06 and useful_life > 1y)                                # art. 108
if supplier.country == ES:
    casillas: (28,29) if not investment else (30,31)
elif supplier.country in EU and supplier.vat_id valid and seller in ROI:          # AIS
    devengado (10,11) = (base_eur, round(base_eur×0.21,2)); deducible (36,37) = (base_eur, cuota×share) [(38,39) if investment]
    349: clave I, country, supplier NIF-IVA, base_eur
elif supplier.country not in EU (US SaaS etc.):                                   # ISP art. 84.Uno.2º.a
    devengado (12,13) = (base_eur, round(base_eur×0.21,2)); deducible (28,29) = (base_eur, cuota×share) [(30,31) if investment]
else (EU supplier charged foreign VAT because no ROI/VAT-id):
    foreign VAT NOT deductible in 303; record it as an expense; refund only through Modelo 360 (by 30.09 of the following year)
imports of goods (DUA): deducible (32,33) / (34,35), devengado — paid at customs (or casilla 77 with the diferimiento option)
```

For AIS/ISP, the cuota devengada = the cuota deducible (with share = 1) → zero effect on the result. Both sides are still mandatory (art. 97.Uno.4º: deduction only if the operation is "debidamente consignada").

### 5. Building Modelo 303 for quarter Q

```
sales  = invoices issued with devengo in Q (including rectificativas, with sign)
purch  = received invoices registered in Q (may also be later, within 4 years)

c07 = Σ base(SUJETA_21);  c08 = 21;  c09 = Σ cuota(SUJETA_21)
c10 = Σ base(AIS + AIB);  c11 = Σ cuota(AIS + AIB)
c12 = Σ base(ISP non-EU); c13 = Σ cuota(ISP non-EU)
c14/c15 = Σ changes of base/cuota from rectificativas with IVA (if not spread over 07–09)   # sign ±
c27 = c03+c06+c09+c11+c13+c15 (+ other rates/RE = 0)
c28/c29 = Σ ES current + ISP non-EU current (base without prorrateo; cuota × share)
c30/c31 = Σ ES investment (+ ISP non-EU investment)
c32/c33, c34/c35 = imports
c36/c37 = Σ AIS + AIB current;  c38/c39 = AIB investment
c40/c41 = adjustments of deductions (received rectificativas) ±
c43 = regularisation of bienes de inversión (only if the prorrata/use changed); c44 = 4T only, with prorrata
c45 = c29+c31+c33+c35+c37+c39+c41+c42+c43+c44
c46 = c27 − c45
c59  = Σ base(NO_SUJETA_INTRACOM)        # EU B2B services (+ EIB)
c120 = Σ base(NO_SUJETA_LOCALIZACION)    # outside the EU, Canarias/Ceuta/Melilla, B2C 69.Dos
c123 = Σ base(OSS_DESTINO)
c64 = c46 (+c58 +c76 = 0);  c65 = 100;  c66 = c64
c110 = balance to compensate at the start of Q (from casilla 72 of previous periods minus the amount applied)
c78  = min(c110, max(c66 + c77, 0))      # apply the maximum possible
c87  = c110 − c78
c69  = c66 + c77 − c78 + c68 + c108      # c68, c108 = 0 for us
c71  = c69 − c70 + c109                  # c70/c109 only in a rectificativa
if c71 > 0: INGRESAR c71 (IBAN; domiciliación up to −5 days)
elif c71 < 0 and Q in {1T,2T,3T}: COMPENSAR  c72 = |c71|  (forbidden if c78 > 0; then the balance is carried over through c87)
elif c71 < 0 and Q == 4T: choice of DEVOLVER c73 = |c71| (including all of c110) or COMPENSAR c72
elif c71 == 0 and (c27>0 or c45>0): RESULTADO CERO
else: SIN ACTIVIDAD
new balance to compensate = c87 + c72
```

Invariants: `c08 = 21.00` only if c07 > 0; `c11 ≈ c10×0.21`, `c13 ≈ c12×0.21`; `c37 ≤ c11` (equal with 100 % deduction); `c59 + c120 + c123 + c07 (+c04+c01) + c60` = the quarter's revenue according to the book of invoices issued.

### 6. Modelo 349 for the period

```
for each (counterparty, clave) in period:
    clave S: Σ base_eur of NO_SUJETA_INTRACOM services; clave I: Σ base_eur AIS; clave E/A: goods
    registro: country code (DE, FR, …; XI for Northern Ireland, goods only), NIF-IVA without country prefix, nombre, clave, importe
periodicity: monthly if Σ(E+S+…) > 50000 in current quarter or any of previous 4 quarters, else quarterly
file only if ≥ 1 registro; corrections of past periods are separate "rectificación" records with the period and the amount declared earlier
```

Reconciliation: `Σ clave S for the year = casilla 59 (total of 4 quarterly 303) − EIB = casilla 103 (390)`.

### 7. Modelo 347 for the year

```
candidates = counterparties with Σ(total_factura including IVA) > 3005.06 for the year
exclude: counterparties/operations reported in the 349 (EU B2B customers, EU suppliers);
         operations with retención reported in the 190/180 (a professional's Spanish B2B customers, a landlord with retención);
         import/export of goods; operations without an invoicing obligation
include: Spanish suppliers without retención (> 3005.06), Spanish customers without retención (B2C legal entities, with empresarial/SL),
         customers and suppliers outside the EU for services (no sujetas) — the AEAT includes them (there is no exclusion for services) [INFERENCE: confirm in INFORMA]
for each: importe anual (including IVA; for no sujetas, the base) and split by quarter; clave A (compras) / B (ventas)
```

### 8. Modelo 390

Aggregation of the year's 303 returns: devengado by rate → 01–06; AIS → the 545–552 group; ISP non-EU → 27/28; deducible → 48/49, 50/51, 52/53, 54/55 + the intra-community block; 84 = result; 85 = casilla 110 of the first 303 of the year (balance from the previous year); 95 = Σ of positive c71; 97/98 = result of the last 303 (compensar/devolver); volumen: 99 = Σc07(+04,01), 103 = Σc59, 104 = Σc60, 110 = Σc120, 126 = Σc123, 108 = total. Plus datos estadísticos: IAE epígrafe, clave A05 (otras actividades profesionales) or A03 (empresariales), the flag "operaciones con terceras personas" (whether there is a 347).

### 9. Verifactu: records when an invoice is issued

```
on issue(invoice):
    rf = RegistroAlta{
        IDEmisorFactura = seller.NIF, NumSerieFactura = serie+numero, FechaExpedicionFactura = dd-mm-yyyy,
        TipoFactura = F1|F2|R1..R5, Descripcion, Destinatarios[{Nombre, NIF | IDOtro{CodigoPais, IDType, ID}}],
        Desglose[{ClaveRegimen=01, CalificacionOperacion=S1|S2|N1|N2 | OperacionExenta=E1..E6, TipoImpositivo, BaseImponible, CuotaRepercutida}],
        CuotaTotal, ImporteTotal, Encadenamiento{PrimerRegistro | RegistroAnterior{IDEmisor, NumSerie, Fecha, Huella}},
        SistemaInformatico{NombreRazon, NIF, NombreSistemaInformatico, IdSistemaInformatico(2 chars), Version, NumeroInstalacion, TipoUsoPosibleSoloVerifactu=S|N, TipoUsoPosibleMultiOT, IndicadorMultiplesOT},
        FechaHoraHusoGenRegistro = ISO-8601 with time zone (2026-03-10T12:00:00+01:00), TipoHuella = 01 (SHA-256), Huella }
    cadena = "IDEmisorFactura=…&NumSerieFactura=…&FechaExpedicionFactura=…&TipoFactura=…&CuotaTotal=…&ImporteTotal=…&Huella=<prev or empty>&FechaHoraHusoGenRegistro=…"
    Huella = UPPER(HEX(SHA256(UTF8(cadena))))          # 64 characters; values trimmed; Huella= empty for the first record
    AEAT test vector: "IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00"
                     → 3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60
    mode VERIFACTU: POST XML to the AEAT web service (certificate), wait t≥60 s between submissions or until the record limit; retries ≥ 1/hour on failure; CSV in the response
    mode NO_VERIFACTU: sign XAdES Enveloped with a qualified certificate; keep a registro de eventos (start/stop, export, incidents) with its own hash chain
    on the printed/PDF form: QR 30–40 mm, ISO 18004, level M, AEAT cotejo URL with NIF, serie+numero, fecha, importe total; the text "VERI*FACTU" only in VERIFACTU mode
on cancel(invoice): RegistroAnulacion{IDFactura, Encadenamiento, Huella over the fields NIF, NumSerie, Fecha, HuellaAnterior, FechaHoraHuso}
rectificativa: new RegistroAlta TipoFactura=R1..R5, TipoRectificativa=S (por sustitución) | I (por diferencias), FacturasRectificadas[...]
```

Records (XML) and events are kept until prescripción and cannot be changed. Any correction is made only with a new record. The declaración responsable (OM art. 15: name, Id (2 characters), version, components, SoloVerifactu S/N, MultiOT S/N, signature type, producer with NIF and address, date/place) is built into the software menu and is available separately (PDF).

### 10. Libros registro: entry

Sheet `EXPEDIDAS_INGRESOS` (LSI.xlsx): Ejercicio | Periodo (1T…4T) | Actividad: Código, Tipo, Grupo/Epígrafe IAE | Tipo de Factura (F1/F2/R1…) | Concepto de Ingreso (IRPF) | Ingreso Computable | Fecha Expedición | Fecha Operación | Identificación de la Factura: Serie, Número, Número-Final | NIF Destinatario: Tipo (02/03/04/05/06/07), Código País, Identificación | Nombre Destinatario | Clave de Operación (01…) | Calificación (S1/S2/N1/N2) | Operación Exenta (E1–E6) | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Repercutida | Tipo/Cuota Recargo Eq. | Cobro: Fecha, Importe, Medio, Identificación Medio | Tipo Retención IRPF | Importe Retenido IRPF | Registro Acuerdo Facturación | Inmueble: Situación, Ref. Catastral | Referencia Externa.

Sheet `RECIBIDAS_GASTOS`: Ejercicio | Periodo | Actividad | Tipo de Factura | Concepto de Gasto | Gasto Deducible | Fecha Expedición | Fecha Operación | Identificación Factura del Expedidor (Serie-Número, Número-Final) | Fecha Recepción | Número Recepción / Final | NIF Expedidor: Tipo, Código País, Identificación | Nombre Expedidor | Clave de Operación | Bien de Inversión (S/N) | Inversión del Sujeto Pasivo (S/N) | Deducible en Periodo Posterior (S/N) | Periodo Deducción: Ejercicio, Periodo | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Soportado | Cuota Deducible | Tipo/Cuota Recargo Eq. | Pago: Fecha, Importe, Medio, Identificación | Tipo/Importe Retención IRPF | Registro Acuerdo Facturación | Inmueble | Referencia Externa.

Sheet `BIENES-INVERSIÓN`: Ejercicio, Periodo, Actividad, Identificador, Descripción, Fecha Inicio Utilización, Valor Adquisición, Valor Amortizable, Método, % Amortización, Amortización (cuota, acumulada inicio/final, pendiente), Identificación factura, NIF/Nombre expedidor, Base, Tipo IVA, Prorrata definitiva, Cuota deducible, Regularización anual (prorrata, cuota deducible, cuota a regularizar), Baja (fecha, causa, factura de transmisión), Referencia externa.

Mapping of our regimes to the book: SUJETA_21 → S1, clave 01, tipo 21, cuota; NO_SUJETA_INTRACOM → N2, NIF tipo 02 (EU VAT-id), tipo/cuota 0, total = base; NO_SUJETA_LOCALIZACION → N2, NIF tipo 06 (or 04), tipo/cuota 0; AIS/ISP (recibidas) → Inversión del Sujeto Pasivo = S, Cuota Soportado = Cuota Deducible = base×21 %. Pre303 maps N2 → casilla 59 with NIF tipo 02 EU, otherwise 120 `[INFERENCE: check against Traslado_Libros_a_Casillas_IVA 2026.xlsx]`. File: one per year, cumulative, name `{ejercicio}{NIF}T{nombre}.xlsx` (T = unificado IVA+IRPF), ≤ 4 MB.

### 11. Worked examples (1T 2026, autónomo professional, not Beckham, 2nd year of activity → 7 % retención)

**A. EU B2B**: Beispiel GmbH, DE123456789 (VIES ok), development service 3 000 € 2026-01-20.
Invoice: base 3 000,00; IVA: no sujeto; total 3 000,00. Statements: "Operación no sujeta al IVA español (art. 69.Uno.1º LIVA). Inversión del sujeto pasivo — art. 196 Directiva 2006/112/CE". NIF-IVA ES… and DE…. 303: c59 += 3 000. 349 1T: DE | 123456789 | Beispiel GmbH | S | 3 000. Book: N2, NIF tipo 02.

**B. US B2B**: Acme Inc., EIN 12-3456789, 5 000 USD, devengo 2026-02-10, ECB rate 1 EUR = 1,0800 USD → 4 629,63 €.
Invoice: 5 000,00 USD (equiv. 4 629,63 EUR, BCE 10/02/2026 1,0800); IVA: no sujeto; "Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)". No retención. 303: c120 += 4 629,63. 349: none. 347: if the total for the year > 3 005,06 € → include it (clave B) `[INFERENCE]`. Book: N2, NIF tipo 06, país US.

**C. Spanish B2B**: Cliente SL, B12345678, consulting 2 000 €, 2026-03-05.
Invoice: base 2 000,00; IVA 21 % 420,00; retención IRPF 7 % −140,00; total factura 2 420,00; to pay 2 280,00. 303: c07 += 2 000; c08 = 21; c09 += 420. Retención 140 → goes to IRPF (Modelo 130/100); the customer files 111/190. 347: excluded (operation with retención). Book: S1, clave 01, Tipo Retención 7, Importe 140, Total Factura 2 420.
Beckham professional variant: retención 24 % = 480 → to pay 1 940,00; empresarial/SL: retención 0 → to pay 2 420,00.

**D. Spanish B2C**: individual, NIF 12345678Z, 500 €, 2026-03-20.
Invoice (full or simplificada; since it is not ≤ 400 € (605 > 400) → full): base 500,00; IVA 21 % 105,00; total 605,00; no retención. 303: c07 += 500; c09 += 105.

**Expenses 1T**: coworking (ES) 300 + 63; laptop (ES) 1 500 + 315 (< 3 005,06 → not a bien de inversión → 28/29); AWS (US) 100 € → ISP: c12 100 / c13 21; c28 100 / c29 21; SaaS from Ireland (IE, VAT-id, we are in the ROI) 200 € → AIS: c10 200 / c11 42; c36 200 / c37 42; 349 clave I: IE | … | 200.

**303 1T 2026**: c07 2 500; c09 525; c10 200; c11 42; c12 100; c13 21; c27 = 588,00; c28 1 900 (300+1 500+100); c29 399 (63+315+21); c36 200; c37 42; c45 = 441,00; c46 = 147,00; c59 3 000; c120 4 629,63; c66 147; c110 0; c78 0; c69 = c71 = 147,00 → **a ingresar 147,00**.
If sales C and D had not happened: c27 = 63; c45 = 441; c46 = −378 → 1T "a compensar" 378 (c72); in 2T c110 = 378 and so on; in 4T, c73 (devolver) with the whole balance.

## Deadlines and modelos

| Modelo | Who | Period | Deadline | When it is not filed |
|---|---|---|---|---|
| 036 (alta, ROI casilla 582, cambio domicilio, baja) | everyone | event | before the activity starts / before the first EU operation; change of domicilio: 1 month | — |
| 303 | all sujetos pasivos (autónomo and SL) | quarter | 1–20 Apr/Jul/Oct; 4T 1–30 Jan | never (even "sin actividad" is filed) |
| 390 | everyone who files the 303, except módulos/rental/SII | year | 1–30 January | SII; only módulos/rental |
| 349 | those who made operations with clave E/A/S/I… | quarter (month if > 50 000 €) | 1–20 of the following month; last period 1–30 Jan | no operations in the period |
| 347 | everyone with counterparties > 3 005,06 € (outside 349/190) | year | 1–28(29) February | SII; no counterparties above the threshold |
| 369 (OSS) | those registered in the Régimen de la Unión (alta Modelo 035) | quarter | by the last day of the following month (even if zero) | not registered |
| 360 | those who paid foreign VAT in the EU without a right to deduct it in the 303 | year | by 30 September of the following year | optional |
| 111 / 190 | the **customer** who withholds the retención (not us) | quarter / year | 1–20 of the following month; 190: January | — |
| Verifactu registros | everyone with a SIF (IS, IRPF, IRNR-EP) | continuously | from 01.01.2027 (IS) / 01.07.2027 (IRPF); postponement to 10.2028 announced | SII |
| e-factura B2B | the recipient is a business in Spain | — | 06.10.2027 (> 8 million) / 06.10.2028 (all others) | customer abroad; simplificadas |
| Libros registro | everyone | continuously, quarterly totals | entries by the 303 filing deadline of the corresponding period (art. 69 RIVA) | SII (kept in the Sede) |

## Edge cases

- **EU customer without a valid VAT-id** (a start-up before registration, a private person acting as an "entrepreneur"): treat as B2C (Reg. UE 282/2011 art. 18.2) → Spanish 21 %. The invoice can be reissued without IVA with a rectificativa after the VAT-id is received (the DGT allows this if the business status on the date of the operation can be proven).
- **We are not in the ROI, but the EU customer is B2B**: the operation is still no sujeta (location does not depend on the ROI). But the 349 requires a NIF-IVA, and the customer will not find us in VIES → risk. File the 036 with casilla 582 before the first invoice.
- **Prepayment from a foreign customer**: devengo at the time of payment (art. 75.Dos) → the advance invoice belongs to the period in which the payment is received, and the exchange rate is the one on the payment date. No sujetas have no IVA, but the amount goes into 59/120 in the quarter of the advance.
- **Continuous contract (retainer) with a foreign customer** without monthly exigibilidad: devengo on 31 December (art. 75.Uno.7º). For no sujetas this affects only the period of 59/120 and of the 349.
- **Rectificativa for a no sujeta operation** (discount/refund to a US customer): reported as a reduction of casilla 120 in the period in which the rectificativa is issued. If the quarter total is negative: the AEAT forms do not accept negative informative casillas → enter 0 and carry the rest over `[INFERENCE: check in Pre303]`.
- **Expenses with 100 % foreign customers**: the right to deduct is full (art. 94.Uno.2º), and the 303 result is consistently negative. The 4T refund arrives within 6 months (by ~the end of July), often with a requerimiento for the books. This is why books in the AEAT format are critical. The alternative is REDEME (036, in November for the following year) with a monthly 303 and mandatory SII.
- **Beckham**: it does not affect IVA at all. It affects only the retención on Spanish B2B invoices (24 %/0 %) and the fact that the retención is taken into account in Modelo 151, not 100.
- **Moving between autonomous communities**: irrelevant for IVA. The 036 (cambio de domicilio fiscal) is mandatory within one month. The invoice series and numbering do not change. The address on the invoice is the new one from the date of the change.
- **Canarias/Ceuta/Melilla**: a business customer there → no sujeta, casilla 120 (not 59), not in the 349; a consumer customer → 21 %. A supplier from there: ISP as with a third country (12/13 + 28/29). Do not confuse this with exports (casilla 60 is for goods only).
- **Northern Ireland (XI)**: keeps EU status only for goods. B2B services to the UK/XI are outside the EU → casilla 120.
- **Car**: 50 % of the cuota on purchase/leasing/fuel/parking. Proving > 50 % is almost impossible for a consultant. Example: leasing 400 + 84 → deduction 42 (base in the book 400 without prorrateo, Cuota Deducible 42).
- **Home office**: IVA on the utilities of a home used partly for work is not deductible (art. 95.Uno; AEAT/TEAC criterion), although in IRPF 30 % of the share is deductible. Home rental is exenta, so there is no IVA.
- **Restaurant/hotel/travel**: IVA is deductible only if the expense is deductible in IRPF/IS (a business trip with documentary proof) and there is a full invoice with NIF (not a ticket).
- **Laptop/equipment < 3 005,06 €**: not a bien de inversión for IVA → casilla 28/29, no regularisation. ≥ 3 005,06 € → 30/31 and a 5-year regularisation if the prorrata/use changes.
- **SaaS from the USA without an invoice with NIF** (only a receipt): for ISP a justificante contable is enough (art. 97.Uno.4º), but it must identify the supplier, the service, the date and the amount. Keep it.
- **Electronic B2C services in the EU**: selling subscriptions/courses to private persons in Europe → monitor the 10 000 € threshold (including the previous year). If it is exceeded: alta OSS (Modelo 035) and Modelo 369. IVA at the rate of the customer's country. 2 pieces of evidence of the customer's location are needed (IP, address, bank).
- **Factura simplificada to a foreign customer**: forbidden. In Verifactu the type F2 is not suitable either; only F1.
- **SL vs autónomo**: IVA is identical. An SL always files electronically with a certificate. It falls under B2B e-factura as a legal entity (statuses from 06.10.2028) and under Verifactu as an IS taxpayer from 01.01.2027 (if the postponement is not formalised).
- **Verifactu with self-hosted software**: a declaración responsable is mandatory for each version; the producer's NIF = the user's NIF. The VERI*FACTU mode is more convenient (no XAdES signature and no registro de eventos are needed; higher trust for refunds). A free alternative is the AEAT application (but then invoices are kept only in it).
- **The customer is Spanish but pays from abroad / in a foreign currency**: location follows the customer (TAI) → 21 % regardless of the currency; the cuota in euros at the rate on the devengo date.

## Open questions

1. **Verifactu: the real start date.** By law (RDL 15/2025): 01.01.2027 / 01.07.2027. On 05.10.2026 Hacienda announced the postponement of "obligations not yet in force" to October 2028 (to align with e-factura for < 8 million), but the RD has not been published yet. The AEAT writes "previsión". Cautious implementation: build the SIF to the RRSIF/OM requirements now (chain, XML, QR). Switch on mandatory sending/signing according to the date actually in force. Monitor the BOE.
2. **B2B e-factura: technical format for our profile.** RD 238/2026 refers to syntaxes and to the SPFE (solución pública), with an obligation to send a copy when a private platform is used. The details of the formats (Facturae/UBL/CII) and of the SPFE API in Orden HAC/1028/2026 were not checked: **UNVERIFIED**. For one or two Spanish customers it is simpler to use the SPFE directly from 06.10.2028.
3. **Pre303 mapping N2 → 59 vs 120** by the customer's NIF type: not confirmed by a primary source (`Traslado_Libros_a_Casillas_IVA 2026.xlsx` was not read). Cautious: do not rely on the automatic import; calculate 59/120 ourselves.
4. **347 for foreign (non-EU) customers/suppliers for services**: the text of art. 33 RGAT excludes only import/export of *goods*. AEAT practice is to include them; **UNVERIFIED** in INFORMA. Cautious: include them (an excess filing is harmless; an omission is an infracción under art. 198/199 LGT).
5. **Exchange rate for no sujetas and for IRPF**: art. 79.Once formally concerns IVA. For the income amount in IRPF/the books, the same principle (devengo) applies according to DGT doctrine; alternative sources are allowed (V2630-17). Cautious: one source (ECB, devengo day; on non-working days, the last published rate). The exchange difference at payment is a financial result outside IVA.
6. **Negative informative casillas 59/120** with rectificativas: the behaviour of the form was not checked. Cautious: limit to zero and carry the rest of the adjustment to the next quarter, with a note in the book.
7. **Beckham + empresarial vs profesional**: the qualification of the activity (IAE sección 1ª vs 2ª) determines 24 % or 0 % retención. The Beckham/IRPF module decides this; here the engine only accepts the flag. The "actividad emprendedora" status (ENISA) does not affect IVA.
8. **Validation tolerance of ±10 €** between base×tipo and cuota in Verifactu/SII: from memory of the AEAT validations document; the 2026 version was not rechecked: **UNVERIFIED**. The engine calculates exactly anyway; the tolerance is needed only when importing other parties' invoices.
9. **390 casillas by rate** (05/06 for 21 %): derived from the range "01–06" in the instructions, not checked against the form: `[INFERENCE]`. The other 390 numbers (27/28, 545–552, 48–55, 84–86, 95–98, 99–110, 125–126, 108) are taken from Instrucciones 390-2025.
10. **IVA rates for 2027**: no changes have been published. RETA/IRPF are outside this file.
11. **Code XI / UK after Brexit for services**: the UK is fully a "third country" for services (casilla 120); XI only for goods. No additional confirmation was searched for.
12. **REDEME**: the conditions (no debts, SII) and the option deadline (November) are based on general knowledge of art. 30 RIVA and were not re-read: **UNVERIFIED**.

### Main sources

- LIVA (Ley 37/1992), consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- RD 1619/2012 (Reglamento de facturación), consolidated, with the amendments of RD 1007/2023 and RD 238/2026: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Instrucciones Modelo 303 2026 (AEAT): https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
- Form 303 (Manual IVA 2025, anexo): https://sede.agenciatributaria.gob.es/static_files/Sede/Biblioteca/Manual/Practicos/IVA/IVA_2025/Imagenes/Cap_9_303_eu_es.pdf
- Instrucciones 390-2025: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
- Instrucciones 349: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
- 347 excluidas: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
- RD 1007/2023 (RRSIF): https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; RDL 15/2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Hacienda note 05.10.2026 (postponement to 10.2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- AEAT Verifactu FAQ (updated 21.07.2026): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html ; huella spec: https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/Veri-Factu_especificaciones_huella_hash_registros.pdf
- E-factura: RD 238/2026 https://www.boe.es/eli/es/rd/2026/03/25/238/con ; AEAT calendar https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html
- Libros registro format: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; LSI.xlsx: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx ; Orden HAC/773/2019: https://www.boe.es/eli/es/o/2019/06/28/hac773
- Retenciones 2026 (from 10.09.2026): https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; RD 1008/2023 (Beckham 24 %): https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
- Modelo 037 abolished / ROI casilla 582: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 ; https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html
- Electronic B2C services/OSS: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html ; Orden HAC/610/2021 (Modelo 369): https://www.boe.es/eli/es/o/2021/06/16/hac610
- Exchange rate: DGT V2630-17 (via Iberley): https://www.iberley.es/resoluciones/resolucion-vinculante-dgt-v2630-17-16-10-2017-1473112 ; ECB reference rates: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.es.html
