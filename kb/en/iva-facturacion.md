*Translated from the Spanish original [kb/iva-facturacion.md](../iva-facturacion.md) on 13.10.2026. The Spanish file is the source of truth.*

# IVA and invoicing for autónomos / SL that provide services

Status as of 2026-10-08. Primary sources (BOE, AEAT Sede, DGT). Everything that could not be confirmed with a primary source is marked as **UNVERIFIED** or `[INFERENCE]`.

## Summary

- IVA does not depend on the régimen Beckham, on the autonomous community (Valencia/Asturias) or on the legal form (autónomo/SL): the rules are the same. The region only matters in Canarias/Ceuta/Melilla (there is no IVA there, but IGIC/IPSI).
- B2B services to a business customer in another EU country: the transaction is **not subject** (*no sujeta*) in Spain (art. 69.Uno.1º LIVA). The customer pays the IVA through inversión del sujeto pasivo (reverse charge). Registration (alta) in the ROI is required (Modelo 036, casilla 582). The customer's NIF-IVA is checked in VIES. Modelo 303 → casilla **59**; Modelo 349 → key **S**.
- B2B services to a customer outside the EU (USA, etc.): **not subject** (art. 69.Uno.1º), with no inversión del sujeto pasivo mention. Since 2023 the rule of «utilización o explotación efectivas» ("effective use or exploitation", art. 70.Dos) does not apply to B2B services like ours. Modelo 303 → casilla **120**; not included in the 349.
- Spanish customer (B2B or B2C): IVA 21 %. If the customer is a business/professional and the provider is a natural person with a *professional* activity, the invoice includes the IRPF withholding (retención): 15 % (7 % in the first 3 years) under the general regime; **24 %** under the régimen Beckham. With a *business* (empresarial) activity and in an SL there is no withholding.
- B2C to an EU customer: Spanish IVA 21 % (art. 69.Uno.2º). Exception: electronic and telecommunications services. Up to 10 000 €/year Spanish IVA applies. Above that (or by option) the IVA of the customer's country applies through OSS (Modelo 369, casilla 123 of the 303).
- B2C to a customer outside the EU: consulting, development and data processing (list in art. 69.Dos) and electronic services are **not subject** (casilla 120). Everything else is taxed at 21 %.
- The right to deduct input IVA (IVA soportado) **is kept** when services are provided to foreign customers (art. 94.Uno.2º LIVA). No prorrata (pro-rata) is needed if there are no exempt transactions without the right to deduct (art. 20). Typical profile (all customers abroad) ⇒ the 303 almost always comes out «a compensar» ("to be offset"). The refund is only obtained in Q4 (4T, casilla 73) or through REDEME/SII.
- Services received from EU suppliers (SaaS, etc.): self-assessment (autorrepercusión), casillas 10/11 and 36/37, 349 key **I**. From suppliers outside the EU: casillas 12/13 and 28/29; not included in the 349.
- Invoice (RD 1619/2012 art. 6): number/series, date, parties with NIF and address, description, base, rate, tax amount (cuota), date of the transaction if different, mandatory mentions for exempt/not subject/ISP. The currency can be any currency, but the **IVA cuota must be stated in euros** at the exchange rate of the accrual date (devengo). The simplified invoice (factura simplificada) is allowed up to 400 € including IVA, but it is forbidden for invoices to foreign customers (art. 4.4.d).
- Modelo 390 is **mandatory** for our profile (only módulos, rental of real estate and SII are exempted). Modelo 347: only counterparties with more than 3 005,06 €/year, excluding transactions declared in the 349 and transactions with withholding.
- Verifactu (RD 1007/2023, Orden HAC/1177/2024): under RDL 15/2025, the deadlines are: IS taxpayers from 01.01.2027; all others (autónomos in IRPF) from 01.07.2027. **On 05.10.2026 Hacienda announced a postponement until October 2028**; the rule has not been published yet. Self-developed software must also meet the requirements (SHA-256 hash chain, QR of 30–40 mm, XML records) and must have its own declaración responsable (statement of compliance).
- B2B electronic invoice (Ley Crea y Crece, RD 238/2026, Orden HAC/1028/2026): mandatory when the recipient is a business in Spain, from **06.10.2027** (volume of operations > 8 million) and from **06.10.2028** (all others). It does not apply to foreign customers.
- Libros registro (record books): issued invoices, received invoices and capital goods (bienes de inversión). The official AEAT format is XLSX (LSI.xlsx), with the sheets EXPEDIDAS_INGRESOS / RECIBIDAS_GASTOS / BIENES-INVERSIÓN. That same file is imported into Pre303, Renta Web and Modelo 130.
- Retention of invoices: the LGT limitation period (4 years from the end of the filing period of the corresponding return). For capital goods the period is longer (regularisation period + 4 years). An SL must also keep them for 6 years under the Código de Comercio (Commercial Code).

## Rules

1. **General place-of-supply rule for B2B services**: the service is located where the business customer is (seat/permanent establishment (EP)/domicile). If the customer is not in the TAI (Peninsula+Balearic Islands), the transaction is *not subject* in Spain. In force since 01.01.2010 (Ley 2/2010). Source: art. 69.Uno.1º LIVA — https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a69
2. **General B2C rule**: the service is located where the provider is (TAI) ⇒ Spanish IVA 21 %. Exception in art. 69.Dos: the listed services (intellectual property rights, advertising, advice/consultants/engineering/legal services, data processing and supply of information, translation, assignment of staff, rental of movable goods, etc.) provided to a non-business customer **outside the EU** (not Canarias/Ceuta/Melilla) are not subject. Source: art. 69.Dos LIVA (same link).
3. **B2C electronic services** (hosting, SaaS/subscriptions, downloadable software, online courses without human intervention — art. 69.Tres.4º): if the customer is in another EU country, Spanish IVA applies as long as the amount of these services plus distance sales does not exceed **10 000 €** (without IVA) in the current year and in the previous year, and the provider has not opted for taxation at destination (art. 70.Uno.8º, art. 73). Above that, the IVA of the customer's country applies (OSS/Modelo 369). If the customer is outside the EU, the transaction is not subject (AEAT). Sources: art. 70.Uno.4º/8º, art. 73 LIVA; AEAT «IVA telecomunicaciones y servicios electrónicos» ("IVA on telecommunications and electronic services") https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html
4. **Effective use or exploitation (art. 70.Dos)**: after Ley 31/2022 and Ley 13/2023 it only applies to (1) the services of art. 69.Dos provided to non-business customers and (2) the rental of means of transport, if they are effectively used in the TAI. It does not apply to B2B consulting or development for a customer outside the EU. Source: art. 70.Dos LIVA (consolidated text).
5. **Taxable person (sujeto pasivo) for services received from a non-resident** (art. 84.Uno.2º.a): the business recipient in the TAI charges the IVA to itself (inversión del sujeto pasivo). The document that allows the deduction is the supplier's invoice or an accounting document (justificante contable) (art. 97.Uno.4º). A separate «autofactura» ("self-invoice") is not needed. Source: art. 84, 97 LIVA.
6. **Right to deduct** (art. 94.Uno): it is granted, among others, by the transactions in point 2º: «Las operaciones realizadas fuera del territorio de aplicación del impuesto que originarían el derecho a la deducción si se hubieran efectuado en el interior del mismo» ("Transactions carried out outside the territory where the tax applies that would give rise to the right to deduct if they had been carried out inside it"). ⇒ Services to foreign customers (B2B EU/outside the EU, not subject) **give the right to deduct**. The prorrata (art. 102–106) only applies if there are at the same time transactions with and without the right to deduct (exempt under art. 20). Source: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a94
7. **Limits on deduction**: art. 95: only expenses directly and exclusively related to the activity. Capital goods in partial use: in proportion to the use. Cars (turismos): presumption of **50 %** (and the same 50 % for fuel, parking, repairs and spare parts, art. 95.Cuatro). Art. 96: jewellery, food/drinks/tobacco, shows, gifts and hospitality to customers, travel/hotels/restaurants are never deducted, unless the expense is deductible in IRPF/IS. Source: art. 95–96 LIVA.
8. **Formal requirements for deduction** (art. 97): original invoice in the taxpayer's name with all the data of art. 6 RD 1619/2012. A «tique» ("receipt", a simplified invoice without the recipient's NIF) does not give the right to deduct, unless the seller has added the recipient's NIF and address and the cuota on a separate line (art. 7.2 RD 1619/2012). Deadline to exercise the deduction: 4 years from the devengo (art. 99.Tres, 100 LIVA).
9. **Devengo (accrual) for services** (art. 75): when the service is provided (75.Uno.2º). With advance payment: at the moment of collection (75.Dos). Continuous services (tracto sucesivo, 75.Uno.7º): when each part of the price becomes due. If it does not become due within one year: on 31 December of each year. Source: art. 75 LIVA.
10. **Obligation to issue an invoice** (RD 1619/2012 art. 2): for all transactions, including not subject and exempt ones, if the customer is a business/professional or a legal person. Also when the transaction is located outside the TAI but the provider is in the TAI (art. 2.3.b.b’). Deadline: B2B, before the 16th day of the month following the devengo (art. 11); B2C, at the moment of the transaction. Sending to the customer happens within the same deadline (art. 18). Source: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
11. **Content of the invoice** (art. 6 RD 1619/2012): a) number and series (consecutive numbering within the series; separate series are mandatory for rectificativas and for invoices issued by the recipient or by a third party); b) date of issue; c) full first name and surnames or company name of the parties; d) provider's NIF; the customer's NIF is mandatory for ISP, for transactions in the TAI and for EIB; e) addresses of the parties; f) description, unit price without IVA, discounts; g) rate; h) cuota shown separately; i) date of the transaction, if different; j) in case of exemption, reference to the article of Directive 2006/112/EC or of the LIVA, or «indicación de que la operación está exenta» ("indication that the transaction is exempt"); m) «inversión del sujeto pasivo», if the taxable person is the recipient; p) «régimen especial del criterio de caja» ("special cash accounting scheme"). For the transactions of art. 2.3.b.b’.a’’ (B2B EU) f/g/h can be omitted, stating the quantity and the nature of the service and the taxable amount (art. 6.3). Since 07.12.2023, art. 6.5: if a SIF is used, the invoice includes the QR and (only in the VERI*FACTU mode) the phrase «VERI*FACTU»/«Factura verificable en la sede electrónica de la AEAT» ("Invoice verifiable on the AEAT electronic office").
12. **Factura simplificada** (art. 4, 7): up to 400 € including IVA (up to 3 000 € for the listed retail activities) and for rectificativas. It **cannot** be used for EIB or for transactions located outside the TAI (art. 4.4.d → art. 2.3.b.b’). This means that foreign customers always receive a full invoice.
13. **Factura rectificativa** (art. 15): mandatory if there is an error in the data, an incorrect cuota or a change of the base (art. 80 LIVA). It is issued as soon as the cause is known, within 4 years from the devengo. It goes in a separate series. It contains the data of the corrected invoice and the content of the correction. The amounts are stated as a difference (with sign) or «tal y como queden tras la rectificación efectuada» ("as they stand after the correction made"), stating the difference. Effect on the 303: casillas 14/15 («Modificación bases y cuotas») for transactions with IVA; for not subject transactions the amount of casilla 59/120 of the period is corrected.
14. **Currency and language** (art. 12 RD 1619/2012; art. 79.Once LIVA): the amounts can be in any currency, but the IVA cuota is stated in euros at the «tipo de cambio vendedor, fijado por el Banco de España» ("selling exchange rate set by the Banco de España") on the devengo date. According to DGT V2630-17, the BdE does not set that rate: the ECB reference rate (published by the BdE) applies. Another public source is allowed if it is applied consistently and does not deviate significantly. Language: any; the AEAT can require a translation into Castilian Spanish.
15. **Retention** (art. 19–23 RD 1619/2012; art. 66–70 LGT): received invoices, copies of issued invoices, accounting documents and DUA, for the limitation period (4 years). Authenticity, integrity, legibility and online access by the AEAT must be guaranteed. Storage outside Spain is only allowed in electronic format, with remote access and with prior notice to the AEAT. Capital goods: until the end of the regularisation period (5 years; real estate, 10) + limitation period. SL: 6 years under art. 30 of the Código de Comercio.
16. **ROI / NIF-IVA**: before the first intra-Community transaction, file Modelo 036 with casilla **582** (alta in the ROI) and the date of the first transaction in casilla **584**. Modelo 037 was abolished on 03.02.2025 (Orden HAC/1526/2024). If the AEAT does not reply within 3 months, the application is deemed rejected. Source: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html ; BOE-A-2025-410.
17. **Modelo 303**: quarterly (1–20 April/July/October; Q4 (4T): 1–30 January). Refund (casilla 73): only in the last return of the year, if the taxpayer is not in REDEME (art. 30 RIVA). In Q1–Q3 (1T–3T) a negative result can only be «a compensar» (casilla 72). The instructions say: «El resultado de la autoliquidación no podrá ser A COMPENSAR, si la casilla (78) está cumplimentada, es decir, si se hubieran aplicado a la autoliquidación que se esté presentando cuotas pendientes de compensación generadas en períodos anteriores» ("The result of the self-assessment cannot be TO BE OFFSET if casilla (78) is filled in, that is, if amounts pending offset generated in previous periods have been applied to the self-assessment being filed"). Source: Instrucciones 303 2026 — https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
18. **Modelo 390**: mandatory for everyone who files periodic 303 returns, except (a) those who file quarterly only under the simplified regime and/or for the rental of urban real estate and (b) those obliged to use SII. Deadline: 1–30 January. Source: Instrucciones 390-2025 — https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
19. **Modelo 349**: it is filed for each period in which there are transactions with the keys E/A/S/I/T/M/H/R/D/C. The filing frequency is quarterly if the amount of EIB + EU services (keys E, S and others) has not exceeded **50 000 €** without IVA in the current quarter or in any of the 4 previous quarters. Otherwise it is monthly (if the threshold is exceeded in the 2nd month, a monthly return is filed with the first two months of the quarter and the field «INDICADOR CAMBIO PERIODICIDAD EN LA OBLIGACIÓN DE DECLARAR» ("indicator of change of filing frequency") is ticked). Deadlines: 1–20 of the following month; for the last period of the year, 1–30 January; July, until 20 September (monthly filers). Source: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
20. **Modelo 347**: annual, in February (1–28/29). It includes the counterparties with which **3 005,06 €** (including IVA) is exceeded in the year, broken down by quarter. Excluded: transactions without an obligation to issue an invoice, imports/exports of goods and transactions already declared in other periodic returns with the same content (349, withholdings 190/180). It is not filed by: those obliged to use SII and persons who only have excluded transactions. Source: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
21. **IRPF withholding on a professional's invoice** to a Spanish business payer: 15 % (art. 101.5.a LIRPF). 7 % in the start year and in the next two years, if no professional activity was carried out in the previous year and a written notice has been given to the customer (art. 95.1 RIRPF). Régimen Beckham: withholdings under the IRNR rules. Professional activity, **24 %**; business activity, no withholding (art. 114 RIRPF as worded by RD 1008/2023). Sources: https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
22. **Verifactu: scope and deadlines**: the RRSIF (RD 1007/2023) applies to IS taxpayers, IRPF taxpayers with economic activities, IRNR taxpayers with an EP and to ERAR (entities under the income attribution regime). It does not apply to those obliged to use SII. Deadlines under RDL 15/2025: IS, until 01.01.2027; all others, until 01.07.2027. On 05.10.2026 the Ministry announced the intention to postpone it until **October 2028** (to coordinate it with the electronic invoice). As long as the rule is not published, the 2027 dates apply. Sources: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf ; https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
23. **Verifactu: SIF requirements** (RRSIF art. 8–16; Orden HAC/1177/2024 art. 10–21): for each invoice, one invoicing registration record (registro de facturación de alta, XML UTF-8); for each cancellation, one cancellation record (registro de anulación). Chained SHA-256 fingerprint (Huella field of the previous record). In addition, one of these two options: sending all records to the AEAT (VERI*FACTU mode, web service, flow control of 60 s), or XAdES signature with a qualified certificate + event log. QR of 30×30–40×40 mm, ISO/IEC 18004, level M, with the AEAT URL (NIF, series+number, date, total amount). The phrase «VERI*FACTU» is only included if the records are sent. Source: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
24. **Declaración responsable** (RRSIF art. 13; OM art. 15): mandatory for each version of any SIF, including **self-developed software for own use**. In that case the developer-user signs it. There is no external certification or registration. Source: AEAT FAQ — https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
25. **B2B electronic invoice** (Ley 18/2022 art. 12; RD 238/2026; Orden HAC/1028/2026, in force since 06.10.2026): mandatory when the recipient is a business/professional with a seat/EP/domicile in Spain. It does not apply to simplified invoices (except those of art. 7.2). Deadlines: 06.10.2027, issuers with a volume of operations > 8 million €; 06.10.2028, all others. Status reporting (accepted/paid): 06.10.2027 / 06.10.2028 (legal persons) / 06.10.2029 (natural persons). Source: https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html ; https://www.boe.es/eli/es/rd/2026/03/25/238/con
26. **Libros registro** (art. 62–70 RIVA; Orden HAC/773/2019 for IRPF): issued invoices, received invoices, capital goods (+ certain intra-Community transactions, which do not affect us). Entries in euros, in chronological order, with totals per quarter; rectificativas, separately. AEAT electronic format: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; field design: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx
27. **Volume of operations** (volumen de operaciones, art. 121 LIVA) = sum of the consideration of all transactions of the year (including those not subject under place-of-supply rules and exempt ones), without IVA. Deliveries of capital goods and non-habitual financial/real estate transactions are excluded. It is used in the 303 (Q4, casilla 88 «Total volumen de operaciones», for those exempted from the 390), in the 390 (casilla 108 «Volumen de operaciones») and for the 8 million threshold of the electronic invoice.

## Figures

### Rates and thresholds (2025 and 2026, no changes for our profile)

| Parameter | 2025 | 2026 | Source |
|---|---|---|---|
| General IVA rate | 21 % | 21 % | art. 90 LIVA |
| Reduced / super-reduced rate | 10 % / 4 % (0 % and 5 %/7,5 % only applied to food until 2024) | 10 % / 4 % | art. 91 LIVA |
| OSS threshold (B2C electronic + EU distance sales) | 10 000 € without IVA | 10 000 € | art. 73 LIVA |
| Threshold for the monthly 349 | 50 000 € without IVA (quarter and 4 previous) | 50 000 € | art. 81 RIVA |
| 347 threshold per counterparty | > 3 005,06 € including IVA | > 3 005,06 € | art. 33 RGAT |
| Capital good (IVA) | ≥ 3 005,06 € and use > 1 year | same | art. 108 LIVA |
| Factura simplificada | ≤ 400 € including IVA (≤ 3 000 € in retail trade) | same | art. 4 RD 1619/2012 |
| Presumption of business use of a car | 50 % | 50 % | art. 95.Tres.2ª LIVA |
| Prorrata: rounding | upwards, to the whole % | same | art. 104.Dos LIVA |
| Mandatory special prorrata | if the general one gives a deduction ≥ 10 % higher | same | art. 103.Dos.2º |
| Large company (monthly 303, SII) | > 6 010 121,04 € volume of operations in the previous year | same | art. 71.3 RIVA |
| Professional withholding (general IRPF) | 15 % / 7 % (start) | 15 % / 7 % | art. 101.5 LIRPF, 95.1 RIRPF |
| Professional withholding (Beckham, IRNR) | 24 % | 24 % | art. 114 RIRPF |
| Deadline to deduct input IVA | 4 years from the devengo | 4 years | art. 99–100 LIVA |
| Retention of invoices | 4 years (limitation period) | 4 years | art. 66 LGT, art. 19 RD 1619/2012 |
| Deadline to issue the B2B invoice | before the 16th day of the following month | same | art. 11 RD 1619/2012 |

### Deadlines (calendar)

| Modelo | Period | Deadline | Domiciliación (−5 days) |
|---|---|---|---|
| 303 | Q1/Q2/Q3 (1T/2T/3T) | 1–20 Apr / Jul / Oct | until the 15th |
| 303 | Q4 (4T) | 1–30 January | until 25 January |
| 390 | year | 1–30 January | — |
| 349 quarterly | Q1–Q3 (1T–3T) | 1–20 Apr / Jul / Oct | — |
| 349 | Q4 (4T) (or December) | 1–30 January | — |
| 347 | year | 1–28(29) February | — |
| 369 (OSS) | quarter | until the last day of the month following the quarter | — |
| 036 alta ROI | — | before the first EU transaction | — |
| 036 change of tax domicile | — | 1 month from the change (art. 10 RGAT) | — |

If the last day is a non-working day (weekend or public holiday), the deadline moves to the next working day (AEAT calendar).

### Verifactu / electronic invoice: dates

| Obligation | Date | Status |
|---|---|---|
| Adapted SIF: IS taxpayers | 01.01.2027 | in force (RDL 15/2025) |
| Adapted SIF: autónomos in IRPF and others | 01.07.2027 | in force (RDL 15/2025) |
| Postponement of the whole RRSIF to October 2028 | ~10.2028 | announced on 05.10.2026, **rule not published** |
| B2B electronic invoice, volume of operations > 8 million € | 06.10.2027 | in force (RD 238/2026 + OM HAC/1028/2026) |
| B2B electronic invoice, all others (our profile) | 06.10.2028 | in force |
| Status reporting for the electronic invoice, natural persons | 06.10.2029 | in force |

### Modelo 303 casillas (2025/2026 form): map for our profile

| Transaction | Output IVA (IVA devengado) (base/rate/cuota) | Deductible IVA (base/cuota) | Additional information | 349 |
|---|---|---|---|---|
| Sale to a Spanish customer at 21 % | 07 / 08 / 09 | — | — | — |
| B2B sale to an EU customer (service) | — | — | **59** | S |
| B2B sale to a customer outside the EU, Canarias/Ceuta/Melilla | — | — | **120** | — |
| B2C sale outside the EU of art. 69.Dos / electronic services | — | — | 120 | — |
| B2C sale in the EU of electronic services through OSS | — (in the 369) | — | 123 | — |
| Export of goods (art. 21) | — | — | 60 | — |
| ISP transactions where the taxable person is the Spanish customer (art. 84.Uno.2º c–g; not our case) | — | — | 122 | — |
| Purchase from a Spanish supplier (current) | — | 28 / 29 | — | — |
| Purchase of a capital good in Spain | — | 30 / 31 | — | — |
| Import of goods (DUA) | — | 32 / 33 (34/35 capital goods) | — | — |
| Service from an EU supplier (AIS) | **10 / 11** | **36 / 37** | — | I |
| Good coming from the EU (AIB) | 10 / 11 | 36 / 37 (38/39 capital goods) | — | A |
| Service from a supplier outside the EU (ISP art. 84.Uno.2º.a) | **12 / 13** | **28 / 29** | — | — |
| Rectificativa with IVA (±) | 14 / 15 | 40 / 41 (received) | — | — |
| Totals | 27 = 152+167+03+155+06+09+11+13+15+158+170+18+21+24+26 | 45 = 29+31+33+35+37+39+41+42+43+44 | 46 = 27 − 45 | |
| Result | 64 = 46+58+76 (Suma de resultados); 65 = 100 %; 66 = 64; 110 (Cuotas a compensar pendientes de periodos anteriores); 78 (Cuotas a compensar de periodos anteriores aplicadas en este periodo); 87 = 110−78; 69 = 66+77−78+68+108 (Resultado de la autoliquidación); 71 = 69−70+109 | | 72 (Compensación) / 73 (Devolución, Q4 (4T) only) | |

### Modelo 390 casillas (2025): main ones

| Content | Casillas |
|---|---|
| Ordinary regime by rate (0/4/10/21 %) base/cuota | 01–06, 700–703, 667–670 (21 %: pair 05/06 `[INFERENCE: check against the form]`) |
| Adquisiciones intracomunitarias de servicios (intra-Community acquisitions of services) base/cuota by rate | 545–548, 551–552, 720–723, 687–690 |
| Adquisiciones intracomunitarias de bienes (intra-Community acquisitions of goods) | 21–26, 716–719, 683–686 |
| IVA devengado en otros supuestos de inversión del sujeto pasivo (supplier outside the EU) | 27 / 28 |
| Modificación de bases y cuotas | 29 / 30 |
| Total bases y cuotas IVA / Total cuotas de IVA y recargo de equivalencia | 33 / 34; 47 |
| IVA deducible en operaciones interiores. Bienes y servicios corrientes (sum) | 48 / 49 (by rate 695–698, 190–191 …) |
| IVA deducible en operaciones interiores. Bienes de inversión | 50 / 51 |
| IVA deducible en importaciones. Bienes corrientes / Bienes de inversión | 52 / 53; 54 / 55 |
| Suma de resultados / Compensación de cuotas del ejercicio anterior / Resultado de la liquidación | 84, 85, 86 |
| Total resultados a ingresar en las autoliquidaciones de IVA del ejercicio / A compensar / A devolver | 95, 97, 98 |
| Volumen de operaciones: Operaciones en régimen general / Entregas intracomunitarias de bienes y servicios / Exportaciones y otras operaciones exentas con derecho a deducción / Operaciones exentas sin derecho a deducción / Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 126) / Operaciones sujetas con inversión del sujeto pasivo / Operaciones no sujetas por reglas de localización acogidas a los regímenes especiales de ventanilla única / Volumen de operaciones | 99, 103, 104, 105, 110, 125, 126, 108 |

### Keys for the libros registro and the Verifactu records

| Field | Values |
|---|---|
| Classification of the transaction (Calificación de la operación) | S1 subject, not exempt, without ISP; S2 subject with ISP; N1 not subject art. 7/14; **N2 not subject under place-of-supply rules** |
| Exempt transaction (Operación exenta) | E1 art. 20; E2 art. 21; E3 art. 22; E4 art. 23–24; E5 art. 25 (EIB); E6 others |
| Regime key (Clave de régimen) | 01 general; 02 export; 07 cash accounting (criterio de caja); 08 IGIC/IPSI; 17 OSS; 18 equivalence surcharge (recargo equivalencia) … |
| Invoice type (Tipo de factura, Verifactu) | F1 full; F2 simplified; F3 replacing simplified invoices; R1–R4 rectificativas (R1 error of law/art. 80.Uno-Dos-Seis, R2 art. 80.Tres, R3 art. 80.Cuatro, R4 others); R5 rectificativa of a simplified invoice |
| Recipient NIF type (Tipo NIF destinatario, libros) | 02 EU NIF-IVA; 03 passport; 04 official document of the country; 05 residence certificate; 06 other supporting document; 07 not registered (no censado) |

## Formulas for the engine

In all cases: amounts in euros, with 2 decimals, rounding `ROUND_HALF_UP` (as in the AEAT forms). The cuota is calculated for each invoice (for each rate). The already rounded cuota is summed in the books and in the 303. The AEAT validations (SII/Verifactu) allow a deviation `|cuota − base×tipo| ≤ 10 €` per invoice `[according to the AEAT validations document; confirm the version]`.

### 1. Classification of the sale (place of supply + invoice regime)

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
    regime = NO_SUJETA_INTRACOM                                  # art. 69.Uno.1º; casilla 59; 349 key S
    require seller in ROI (ES-VAT in VIES) else -> WARN_ROI
case EU and not b2b:
    if service.kind == ELECTRONIC and (ytd_prev > 10000 or ytd_cur + amount > 10000 or seller.oss_registered):
        regime = OSS_DESTINO                                     # IVA of the customer's country, Modelo 369, casilla 123
    else:
        regime = SUJETA_21                                       # art. 69.Uno.2º / 70.Uno.8º
case NON_EU and b2b:
    regime = NO_SUJETA_LOCALIZACION                              # art. 69.Uno.1º; casilla 120
case NON_EU and not b2b:
    if service.kind in {ART69DOS, ELECTRONIC}: regime = NO_SUJETA_LOCALIZACION   # art. 69.Dos / AEAT criterion
    else: regime = SUJETA_21                                     # general rule art. 69.Uno.2º
    if effectively_used_in_TAI(service): regime = SUJETA_21     # art. 70.Dos (only B2C art. 69.Dos)
```

Canarias/Ceuta/Melilla: B2B → NO_SUJETA_LOCALIZACION (casilla 120, not 59; the 349 is not filed); B2C → SUJETA_21 (art. 69.Dos excludes them).

### 2. Invoice lines by regime

```
base      = Σ round(qty × unit_price × (1 − discount), 2)
case SUJETA_21:
    tipo = 21.00; cuota = round(base × 0.21, 2)
    retencion = round(base × withholding_rate, 2)            # only if withholding_rate > 0
    total_factura = base + cuota                              # the «Total Factura» of the books is NOT reduced by the withholding
    total_a_pagar = base + cuota − retencion
    mentions: []  (with withholding: line «Retención IRPF x %: −N €» ("IRPF withholding x %: −N €") and the withholding base)
case NO_SUJETA_INTRACOM:
    tipo = none; cuota = 0; total = base
    required: seller's NIF-IVA (ES…) and customer's NIF-IVA (with country prefix), both valid in VIES on the invoice date
    mentions: «Operación no sujeta al IVA español por reglas de localización (art. 69.Uno.1º Ley 37/1992)» ("Transaction not subject to Spanish IVA under place-of-supply rules"),
              «Inversión del sujeto pasivo / Reverse charge — art. 196 Directiva 2006/112/CE»
    forbidden: factura simplificada
case NO_SUJETA_LOCALIZACION:
    tipo = none; cuota = 0; total = base
    mentions: «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)» ("Transaction not subject to Spanish IVA (recipient established outside the EU)")
              (for B2C art. 69.Dos: reference to art. 69.Dos)
    forbidden: factura simplificada
case OSS_DESTINO:
    tipo = rate(customer.country); cuota = round(base × tipo, 2); total = base + cuota
    mentions: «IVA … % (país de consumo …) — Régimen de la Unión OSS» ("IVA … % (country of consumption …) — Union OSS scheme"); declared in the 369; in the 303 only casilla 123
```

Currency other than EUR: all invoice amounts can be shown in that currency, but the line «Cuota IVA: N EUR (tipo de cambio BCE dd/mm/aaaa: 1 EUR = X CUR)» ("IVA cuota: N EUR (ECB exchange rate dd/mm/yyyy: 1 EUR = X CUR)") must be added. Not subject transactions have no IVA, but the EUR equivalent of the base is still entered in the book at the exchange rate of the devengo date:

```
fx_date   = devengo_date (date the service is provided / the advance is collected), not the payment date
rate      = ECB_reference_rate(fx_date)   # if it is a non-working day, the last rate published before that date [INFERENCE; DGT V2630-17 only requires consistency]
base_eur  = round(base_cur / rate, 2)     # the ECB quotes 1 EUR = X CUR
cuota_eur = round(base_eur × tipo, 2)
```

### 3. IRPF withholding on the invoice (only to Spanish business customers)

```
if not customer.spanish_withholder: rate = 0          # consumer natural person, foreign customer without an EP in Spain
elif seller.profile == SL: rate = 0                   # services of an SL carry no withholding (except rentals, etc.)
elif seller.activity_kind == EMPRESARIAL: rate = 0    # both under the general regime and under Beckham
elif seller.profile == AUTONOMO_BECKHAM: rate = 0.24  # art. 114 RIRPF → IRNR rules
elif start_year ≤ year ≤ start_year + 2 and no_professional_activity_prev_year and notice_given: rate = 0.07
else: rate = 0.15
retencion = round(base × rate, 2)    # the base is the taxable base without IVA
```

The amount withheld is deducted in IRPF (Modelo 100/151). This figure is passed to the IRPF/Beckham module. It is not reflected in the 303.

### 4. Classification of the expense (input IVA)

```
input: supplier{country, vat_id}, invoice{base, tipo, cuota, currency}, item{kind: CURRENT | INVESTMENT | VEHICLE | FOOD_HOTEL_TRAVEL | GIFTS | PRIVATE_MIX}
deductible_share:
    kind == GIFTS or (FOOD_HOTEL_TRAVEL and not deductible_in_IRPF_IS) -> 0       # art. 96
    kind == VEHICLE (turismo) and related costs -> 0.50 (unless proven otherwise)   # art. 95.Tres.2ª, Cuatro
    kind == PRIVATE_MIX (water/electricity/internet of the home) -> 0              # art. 95.Uno; AEAT/TEAC criterion
    otherwise -> 1.00 × prorrata (prorrata = 1.00 if there are no art. 20 transactions)
investment = (base ≥ 3005.06 and useful_life > 1y)                                # art. 108
if supplier.country == ES:
    casillas: (28,29) if not investment else (30,31)
elif supplier.country in EU and supplier.vat_id valid and seller in ROI:          # AIS
    devengado (10,11) = (base_eur, round(base_eur×0.21,2)); deducible (36,37) = (base_eur, cuota×share) [(38,39) if investment]
    349: key I, country, supplier's NIF-IVA, base_eur
elif supplier.country not in EU (SaaS from the USA, etc.):                        # ISP art. 84.Uno.2º.a
    devengado (12,13) = (base_eur, round(base_eur×0.21,2)); deducible (28,29) = (base_eur, cuota×share) [(30,31) if investment]
else (EU supplier charged foreign VAT because no ROI/VAT-id):
    foreign VAT NOT deductible in 303; record it as an expense; refund only through Modelo 360 (until 30.09 of the following year)
imports of goods (DUA): deducible (32,33) / (34,35), devengado: paid at customs (or casilla 77 if deferral is chosen)
```

In AIS/ISP, output cuota = deductible cuota (with share = 1) → zero effect on the result. But both parts are mandatory (art. 97.Uno.4º: the deduction is only allowed if the transaction is «debidamente consignada» ("duly recorded")).

### 5. Calculation of the Modelo 303 for quarter Q

```
sales  = invoices issued with devengo in Q (including rectificativas, with sign)
purch  = received invoices registered in Q (also later, within the 4-year deadline)

c07 = Σ base(SUJETA_21);  c08 = 21;  c09 = Σ cuota(SUJETA_21)
c10 = Σ base(AIS + AIB);  c11 = Σ cuota(AIS + AIB)
c12 = Σ base(ISP non-EU); c13 = Σ cuota(ISP non-EU)
c14/c15 = Σ of the base/cuota changes from rectificativas with IVA (if not spread over 07–09)   # sign ±
c27 = c03+c06+c09+c11+c13+c15 (+ other rates/RE = 0)
c28/c29 = Σ ES current + ISP non-EU current (base without pro-rating; cuota × share)
c30/c31 = Σ ES investment (+ ISP non-EU investment)
c32/c33, c34/c35 = imports
c36/c37 = Σ AIS + AIB current;  c38/c39 = AIB investment
c40/c41 = correction of deductions (received rectificativas) ±
c43 = regularisation of capital goods (only if the prorrata/use changed); c44 = only Q4 (4T) with prorrata
c45 = c29+c31+c33+c35+c37+c39+c41+c42+c43+c44
c46 = c27 − c45
c59  = Σ base(NO_SUJETA_INTRACOM)        # B2B EU services (+ EIB)
c120 = Σ base(NO_SUJETA_LOCALIZACION)    # outside the EU, Canarias/Ceuta/Melilla, B2C 69.Dos
c123 = Σ base(OSS_DESTINO)
c64 = c46 (+c58 +c76 = 0);  c65 = 100;  c66 = c64
c110 = balance to be offset at the start of Q (from casilla 72 of previous periods, minus what was applied)
c78  = min(c110, max(c66 + c77, 0))      # the maximum possible is applied
c87  = c110 − c78
c69  = c66 + c77 − c78 + c68 + c108      # c68, c108 = 0 in our case
c71  = c69 − c70 + c109                  # c70/c109 only in a rectificativa (corrective return)
if c71 > 0: INGRESAR c71 (IBAN; domiciliación until −5 days)
elif c71 < 0 and Q in {1T,2T,3T}: COMPENSAR  c72 = |c71|  (forbidden if c78 > 0; in that case the balance is carried over through c87)
elif c71 < 0 and Q == 4T: choose DEVOLVER c73 = |c71| (including all of c110) or COMPENSAR c72
elif c71 == 0 and (c27>0 or c45>0): RESULTADO CERO
else: SIN ACTIVIDAD
new balance to be offset = c87 + c72
```

Invariants: `c08 = 21.00` only if c07 > 0; `c11 ≈ c10×0.21`, `c13 ≈ c12×0.21`; `c37 ≤ c11` (with a 100 % deduction they are equal); `c59 + c120 + c123 + c07 (+c04+c01) + c60` = income of the quarter according to the issued invoices book.

### 6. Modelo 349 for the period

```
for each (counterparty, clave) in period:
    clave S: Σ base_eur of NO_SUJETA_INTRACOM services; clave I: Σ base_eur AIS; clave E/A: goods
    record: country code (DE, FR, …; XI for Northern Ireland, goods only), NIF-IVA without country prefix, name, clave, amount
periodicity: monthly if Σ(E+S+…) > 50000 in current quarter or any of previous 4 quarters, else quarterly
file only if ≥ 1 record; corrections of previous periods: separate «rectificación» ("correction") records with the period and the amount declared before
```

Reconciliation: `Σ key S of the year = casilla 59 (sum of the 4 quarters of the 303) − EIB = casilla 103 (390)`.

### 7. Modelo 347 for the year

```
candidates = counterparties with Σ(total_factura including IVA) > 3005.06 in the year
exclude: counterparties/transactions declared in the 349 (EU B2B customers, EU suppliers);
         transactions with withholding included in the 190/180 (the professional's Spanish B2B customers, landlord with withholding);
         import/export of goods; transactions without an invoice obligation
include: Spanish suppliers without withholding (> 3005.06), Spanish customers without withholding (legal persons B2C, in the case of empresarial/SL),
         customers and suppliers outside the EU for services (not subject): the AEAT includes them (there is no exclusion for services) [INFERENCE: confirm in INFORMA]
for each one: annual amount (including IVA; for not subject transactions, the base) and breakdown by quarter; key A (purchases) / B (sales)
```

### 8. Modelo 390

Aggregation of the 303 returns of the year: output IVA by rate → 01–06; AIS → group 545–552; ISP non-EU → 27/28; deductible → 48/49, 50/51, 52/53, 54/55 + intra-Community block; 84 = Suma de resultados; 85 = casilla 110 of the first 303 of the year (balance of the previous year); 95 = Σ of the positive c71; 97/98 = result of the last 303 (offset/refund); volume: 99 = Σc07(+04,01), 103 = Σc59, 104 = Σc60, 110 = Σc120, 126 = Σc123, 108 = sum. In addition, statistical data: IAE epígrafe (heading), key A05 («Resto de actividades profesionales», "Other professional activities") or A03 («Resto de actividades empresariales no incluidas en los dos subtipos anteriores», "Other business activities not included in the two previous subtypes"), indicator «Operaciones económicas con terceras personas» ("Economic transactions with third parties") (if there is a 347).

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
    Huella = UPPER(HEX(SHA256(UTF8(cadena))))          # 64 characters; values trimmed; Huella= empty in the first record
    AEAT test vector: "IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00"
                     → 3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60
    mode VERIFACTU: POST XML to the AEAT web service (certificate), wait t≥60 s between submissions or until the record limit; retries ≥ 1/hour on failure; CSV in the response
    mode NO_VERIFACTU: sign XAdES Enveloped with a qualified certificate; keep an event log (start/stop, export, incidents) with its own hash chain
    on the printed/PDF version: QR 30–40 mm, ISO 18004, level M, AEAT verification URL with NIF, serie+numero, date, total amount; text «VERI*FACTU» only in VERIFACTU mode
on cancel(invoice): RegistroAnulacion{IDFactura, Encadenamiento, Huella over the fields NIF, NumSerie, Fecha, HuellaAnterior, FechaHoraHuso}
rectificativa: new RegistroAlta TipoFactura=R1..R5, TipoRectificativa=S (by substitution) | I (by differences), FacturasRectificadas[...]
```

The records (XML) and the events are kept until the limitation period ends and cannot be modified. Any correction is made only with a new record. The declaración responsable (OM art. 15: name, Id (2 characters), version, components, SoloVerifactu S/N, MultiOT S/N, signature type, producer with NIF and address, date/place) is built into the software menu and is also available separately (PDF).

### 10. Libros registro: entries

Sheet `EXPEDIDAS_INGRESOS` (LSI.xlsx): Ejercicio | Periodo (1T…4T) | Actividad: Código, Tipo, Grupo/Epígrafe IAE | Tipo de Factura (F1/F2/R1…) | Concepto de Ingreso (IRPF) | Ingreso Computable | Fecha Expedición | Fecha Operación | Identificación de la Factura: Serie, Número, Número-Final | NIF Destinatario: Tipo (02/03/04/05/06/07), Código País, Identificación | Nombre Destinatario | Clave de Operación (01…) | Calificación (S1/S2/N1/N2) | Operación Exenta (E1–E6) | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Repercutida | Tipo/Cuota Recargo Eq. | Cobro: Fecha, Importe, Medio, Identificación Medio | Tipo Retención IRPF | Importe Retenido IRPF | Registro Acuerdo Facturación | Inmueble: Situación, Ref. Catastral | Referencia Externa.

Sheet `RECIBIDAS_GASTOS`: Ejercicio | Periodo | Actividad | Tipo de Factura | Concepto de Gasto | Gasto Deducible | Fecha Expedición | Fecha Operación | Identificación Factura del Expedidor (Serie-Número, Número-Final) | Fecha Recepción | Número Recepción / Final | NIF Expedidor: Tipo, Código País, Identificación | Nombre Expedidor | Clave de Operación | Bien de Inversión (S/N) | Inversión del Sujeto Pasivo (S/N) | Deducible en Periodo Posterior (S/N) | Periodo Deducción: Ejercicio, Periodo | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Soportado | Cuota Deducible | Tipo/Cuota Recargo Eq. | Pago: Fecha, Importe, Medio, Identificación | Tipo/Importe Retención IRPF | Registro Acuerdo Facturación | Inmueble | Referencia Externa.

Sheet `BIENES-INVERSIÓN`: Ejercicio, Periodo, Actividad, Identificador, Descripción, Fecha Inicio Utilización, Valor Adquisición, Valor Amortizable, Método, % Amortización, Amortización (cuota, acumulada inicio/final, pendiente), Identificación factura, NIF/Nombre expedidor, Base, Tipo IVA, Prorrata definitiva, Cuota deducible, Regularización anual (prorrata, cuota deducible, cuota a regularizar), Baja (fecha, causa, factura de transmisión), Referencia externa.

Mapping of our regimes to the book: SUJETA_21 → S1, key 01, rate 21, cuota; NO_SUJETA_INTRACOM → N2, NIF type 02 (EU VAT-id), rate/cuota 0, total = base; NO_SUJETA_LOCALIZACION → N2, NIF type 06 (or 04), rate/cuota 0; AIS/ISP (received) → Inversión del Sujeto Pasivo = S, Cuota Soportado = Cuota Deducible = base×21 %. Mapping in Pre303: N2 → casilla 59 if the NIF is EU type 02; otherwise, 120 `[INFERENCE: check against Traslado_Libros_a_Casillas_IVA 2026.xlsx]`. File: one per year, cumulative, named `{ejercicio}{NIF}T{nombre}.xlsx` (T = unified IVA+IRPF), ≤ 4 MB.

### 11. Worked examples (Q1 (1T) 2026, professional autónomo, no Beckham, 2nd year of activity → 7 % withholding)

**A. B2B EU**: Beispiel GmbH, DE123456789 (VIES ok), development service of 3 000 €, 2026-01-20.
Invoice: base 3 000,00; IVA: not subject; total 3 000,00. Mentions: «Operación no sujeta al IVA español (art. 69.Uno.1º LIVA). Inversión del sujeto pasivo — art. 196 Directiva 2006/112/CE» ("Transaction not subject to Spanish IVA. Reverse charge"). NIF-IVA ES… and DE…. 303: c59 += 3 000. 349 Q1 (1T): DE | 123456789 | Beispiel GmbH | S | 3 000. Book: N2, NIF type 02.

**B. B2B USA**: Acme Inc., EIN 12-3456789, 5 000 USD, devengo 2026-02-10, ECB exchange rate 1 EUR = 1,0800 USD → 4 629,63 €.
Invoice: 5 000,00 USD (equiv. 4 629,63 EUR, ECB 10/02/2026 1,0800); IVA: not subject; «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)» ("Transaction not subject to Spanish IVA (recipient established outside the EU)"). No withholding. 303: c120 += 4 629,63. 349: no. 347: if 3 005,06 € is exceeded in the year → include (key B) `[INFERENCE]`. Book: N2, NIF type 06, country US.

**C. B2B Spain**: Cliente SL, B12345678, consulting of 2 000 €, 2026-03-05.
Invoice: base 2 000,00; IVA 21 % 420,00; IRPF withholding 7 % −140,00; invoice total 2 420,00; to pay 2 280,00. 303: c07 += 2 000; c08 = 21; c09 += 420. Withholding 140 → to IRPF (Modelo 130/100); the customer files the 111/190. 347: excluded (transaction with withholding). Book: S1, key 01, Tipo Retención 7, Importe 140, Total Factura 2 420.
Variant for a professional under Beckham: withholding 24 % = 480 → to pay 1 940,00; empresarial/SL: withholding 0 → to pay 2 420,00.

**D. B2C Spain**: natural person, NIF 12345678Z, 500 €, 2026-03-20.
Invoice (full or simplified depending on the ≤ 400 € limit: 605 > 400 → full): base 500,00; IVA 21 % 105,00; total 605,00; no withholding. 303: c07 += 500; c09 += 105.

**Q1 (1T) expenses**: coworking (ES) 300 + 63; laptop (ES) 1 500 + 315 (< 3 005,06 → not a capital good → 28/29); AWS (US) 100 € → ISP: c12 100 / c13 21; c28 100 / c29 21; SaaS from Ireland (IE, VAT-id, we are in the ROI) 200 € → AIS: c10 200 / c11 42; c36 200 / c37 42; 349 key I: IE | … | 200.

**303 Q1 (1T) 2026**: c07 2 500; c09 525; c10 200; c11 42; c12 100; c13 21; c27 = 588,00; c28 1 900 (300+1 500+100); c29 399 (63+315+21); c36 200; c37 42; c45 = 441,00; c46 = 147,00; c59 3 000; c120 4 629,63; c66 147; c110 0; c78 0; c69 = c71 = 147,00 → **to pay 147,00** (a ingresar).
If there were no sales C and D: c27 = 63; c45 = 441; c46 = −378 → Q1 (1T) «a compensar» 378 (c72); in Q2 (2T) c110 = 378, etc.; in Q4 (4T), c73 (refund) for the whole balance.

## Deadlines and modelos

| Modelo | Who | Period | Deadline | When it is not filed |
|---|---|---|---|---|
| 036 (alta, ROI casilla 582, change of address, baja) | everyone | per event | before the start of the activity / of the first EU transaction; change of address: 1 month | — |
| 303 | all taxable persons (autónomo and SL) | quarter | 1–20 Apr/Jul/Oct; Q4 (4T) 1–30 Jan | never (it is also filed «sin actividad», "no activity") |
| 390 | everyone who files the 303, except módulos/rental/SII | year | 1–30 January | SII; only módulos/rental |
| 349 | whoever has carried out transactions with key E/A/S/I… | quarter (month if > 50 000 €) | 1–20 of the following month; last period, 1–30 Jan | there are no transactions in the period |
| 347 | everyone with counterparties > 3 005,06 € (outside the 349/190) | year | 1–28(29) February | SII; there are no counterparties above the threshold |
| 369 (OSS) | registered in the Union scheme (Régimen de la Unión) (alta Modelo 035) | quarter | until the last day of the following month (also if zero) | not registered |
| 360 | whoever has paid foreign IVA in the EU without the right to deduct it in the 303 | year | until 30 September of the following year | optional |
| 111 / 190 | the **customer** who applies the withholding (not us) | quarter / year | 1–20 of the following month; 190: January | — |
| Verifactu records | everyone who uses a SIF (IS, IRPF, IRNR-EP) | continuously | from 01.01.2027 (IS) / 01.07.2027 (IRPF); postponement to 10.2028 announced | SII |
| B2B electronic invoice | business recipient in Spain | — | 06.10.2027 (> 8 million) / 06.10.2028 (all others) | customer abroad; simplified invoices |
| Libros registro | everyone | continuously, with totals per quarter | entries: before the end of the filing period of the 303 for the corresponding period (art. 69 RIVA) | SII (kept in the Sede) |

## Edge cases

- **EU customer without a valid VAT-id** (a startup before registration, an individual who presents themselves as a «empresario», "business"): treat as B2C (Reg. UE 282/2011 art. 18.2) → Spanish IVA 21 %. When the VAT-id is obtained, the invoice can be reissued without IVA through a rectificativa (the DGT allows this if the business status on the date of the transaction can be proven).
- **We have no ROI, but have an EU B2B customer**: the transaction is still not subject (the place of supply does not depend on the ROI). But the 349 requires the NIF-IVA, and the customer will not find us in VIES → risk. File the 036, casilla 582, before the first invoice.
- **Advance payment from a foreign customer**: devengo at the moment of collection (art. 75.Dos) → advance invoice in the period in which it is collected, at the exchange rate of the collection date. Not subject transactions have no IVA, but the amount goes to casilla 59/120 of the quarter of the advance.
- **Continuous contract (retainer) with a foreign customer** without monthly due dates: devengo on 31 December (art. 75.Uno.7º). For not subject transactions it only affects the period of the 59/120 and of the 349.
- **Rectificativa of a not subject transaction** (discount/refund to a US customer): it is reflected by reducing casilla 120 in the period in which the rectificativa is issued. If the quarter total is negative: the AEAT forms do not accept negative information casillas → enter 0 and carry over the rest `[INFERENCE: check in Pre303]`.
- **Expenses with 100 % foreign customers**: the right to deduct is full (art. 94.Uno.2º) and the result of the 303 is consistently negative. The Q4 (4T) refund arrives within 6 months (until ~end of July), often with a request (requerimiento) for the books. That is why keeping the books in the AEAT format is essential. Alternative: REDEME (036, in November for the following year), with a monthly 303 and mandatory SII.
- **Beckham**: it has no influence at all on IVA. It only affects the withholding on B2B invoices to Spanish customers (24 %/0 %) and the fact that the withholding is credited in Modelo 151, not in the 100.
- **Move between autonomous communities**: it does not matter for IVA. Filing the 036 (change of tax domicile) within one month is mandatory. The invoice series and numbering do not change. The address on the invoice is the new one from the date of the change.
- **Canarias/Ceuta/Melilla**: business customer there → not subject, casilla 120 (not 59), does not go to the 349. Consumer customer → 21 %. Supplier from there → ISP as with a third country (12/13 + 28/29). Do not confuse with export (casilla 60 is only for goods).
- **Northern Ireland (XI)**: keeps EU status only for goods. B2B services in UK/XI are outside the EU → casilla 120.
- **Car**: 50 % of the cuota on purchase/leasing/fuel/parking. For a consultant it is almost impossible to prove use above 50 %. Example: leasing 400 + 84 → deduction 42 (base in the book 400 without pro-rating, Cuota Deducible 42).
- **Home office**: the IVA on utilities of a home used partly for the activity is not deductible (art. 95.Uno; AEAT/TEAC criterion), although in IRPF 30 % of the proportional part is deducted. Residential rent is exempt: it carries no IVA.
- **Restaurant/hotel/travel**: the IVA is only deductible if the expense is deductible in IRPF/IS (business trip supported by documents) and there is a full invoice with NIF (not a tique).
- **Laptop/equipment < 3 005,06 €**: not a capital good for IVA purposes → casilla 28/29, no regularisation. If ≥ 3 005,06 € → 30/31 and regularisation over 5 years if the prorrata or the use changes.
- **SaaS from the USA without an invoice with NIF** (only a receipt): for ISP an accounting document (justificante contable) is enough (art. 97.Uno.4º). But the document must identify the supplier, the service, the date and the amount. It must be kept.
- **B2C electronic services in the EU**: sale of subscriptions/courses to European individuals → watch the 10 000 € threshold (including the previous year). If it is exceeded: alta in OSS (Modelo 035) and Modelo 369; IVA at the rate of the customer's country; 2 pieces of evidence of the customer's location are needed (IP, address, bank).
- **Factura simplificada to a foreign customer**: forbidden. In Verifactu the F2 type is not valid either: only F1.
- **SL versus autónomo**: IVA is identical. The SL always files electronically with a certificate. As a legal person it is subject to the B2B electronic invoice (statuses from 06.10.2028) and to Verifactu as an IS taxpayer from 01.01.2027 (if the postponement is not formalised).
- **Verifactu with software hosted by the user**: the declaración responsable is mandatory for each version; producer's NIF = user's NIF. The VERI*FACTU mode is more convenient (no XAdES signature or event log is needed, and it builds more trust for refunds). Free alternative: the AEAT application (but then the invoices are kept only in it).
- **Spanish customer who pays from abroad / in another currency**: the place of supply depends on the customer (TAI) → 21 % regardless of the currency; cuota in euros at the exchange rate of the devengo date.

## Open points

1. **Verifactu: real start date.** Under the rule (RDL 15/2025): 01.01.2027 / 01.07.2027. On 05.10.2026 Hacienda announced the «aplazamiento de las obligaciones pendientes de aplicación del Real Decreto 1007/2023, de 5 de diciembre, hasta octubre de 2028» ("postponement of the obligations of Real Decreto 1007/2023 of 5 December that are pending application until October 2028") (to coordinate them with the electronic invoice for < 8 million). But the RD has not been published yet; the AEAT speaks of a «previsión de ampliación del plazo» ("expected extension of the deadline"). Careful implementation: build the SIF now according to the RRSIF/OM requirements (chain, XML, QR) and activate mandatory sending/signing according to the date actually in force; follow the BOE.
2. **B2B electronic invoice: technical format for our profile.** RD 238/2026 refers to the syntaxes and to the SPFE (public solution), with an obligation to send a copy if a private platform is used. The details of the formats (Facturae/UBL/CII) and of the SPFE API in Orden HAC/1028/2026 have not been checked: **UNVERIFIED**. With one or two Spanish customers it is simpler to use the SPFE directly from 06.10.2028.
3. **Mapping in Pre303 N2 → 59 or 120** depending on the customer's NIF type: not confirmed with a primary source (`Traslado_Libros_a_Casillas_IVA 2026.xlsx` has not been read). Careful approach: do not rely on automatic import and calculate 59/120 ourselves.
4. **347 for foreign customers/suppliers (outside the EU) for services**: the text of art. 33 RGAT only excludes the import/export of *goods*; AEAT practice is to include them; **UNVERIFIED** in INFORMA. Careful approach: include them (one extra declaration causes no harm; an omission is an infringement under art. 198/199 LGT).
5. **Exchange rate for not subject transactions and for IRPF**: art. 79.Once formally refers to IVA. For the income amount in IRPF and in the books the same principle (devengo) applies according to DGT doctrine; alternative sources are allowed (V2630-17). Careful approach: a single source (ECB, day of the devengo; on non-working days, the last published rate). The exchange difference on collection is a financial result unrelated to IVA.
6. **Negative information casillas 59/120** in rectificativas: how the form behaves has not been checked. Careful approach: limit them to zero and carry over the rest of the correction to the next quarter, with a note in the book.
7. **Beckham + empresarial versus profesional**: the classification of the activity (IAE section 1 or 2) determines the 24 % or 0 % withholding. The Beckham/IRPF module decides this; here the engine only receives the flag. The status of «actividad emprendedora» ("entrepreneurial activity", ENISA) does not affect IVA.
8. **Validation margin of ±10 €** between base×rate and the cuota in Verifactu/SII: figure from memory of the AEAT validations document; the 2026 version has not been checked again: **UNVERIFIED**. The engine calculates exactly in any case; the margin is only needed when importing third-party invoices.
9. **390 casillas by rate** (05/06 for 21 %): derived from the range «01–06» in the instructions, not compared with the form: `[INFERENCE]`. The other 390 numbers (27/28, 545–552, 48–55, 84–86, 95–98, 99–110, 125–126, 108) come from the Instrucciones 390-2025.
10. **IVA rates for 2027**: no changes have been published; RETA/IRPF are outside the scope of this file.
11. **Code XI / UK after Brexit for services**: the UK is a full «third country» (país tercero) for services (casilla 120); XI only counts as EU for goods. No additional confirmation has been searched for.
12. **REDEME**: the conditions (no debts, SII) and the option deadline (November) come from general knowledge of art. 30 RIVA; they have not been re-read: **UNVERIFIED**.

### Main sources

- LIVA (Ley 37/1992) consolidated: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- RD 1619/2012 (Invoicing Regulation, Reglamento de facturación) consolidated, with the amendments of RD 1007/2023 and RD 238/2026: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Instrucciones Modelo 303 2026 (AEAT): https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
- Form 303 (Manual IVA 2025, annex): https://sede.agenciatributaria.gob.es/static_files/Sede/Biblioteca/Manual/Practicos/IVA/IVA_2025/Imagenes/Cap_9_303_eu_es.pdf
- Instrucciones 390-2025: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
- Instrucciones 349: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
- 347 excluded transactions: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
- RD 1007/2023 (RRSIF): https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; RDL 15/2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Hacienda note of 05.10.2026 (postponement to 10.2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- AEAT Verifactu FAQ (updated on 21.07.2026): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html ; fingerprint (huella) specification: https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/Veri-Factu_especificaciones_huella_hash_registros.pdf
- Electronic invoice: RD 238/2026 https://www.boe.es/eli/es/rd/2026/03/25/238/con ; AEAT calendar https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html
- Libros registro format: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; LSI.xlsx: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx ; Orden HAC/773/2019: https://www.boe.es/eli/es/o/2019/06/28/hac773
- Withholdings 2026 (from 10.09.2026): https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; RD 1008/2023 (Beckham 24 %): https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
- Modelo 037 abolished / ROI casilla 582: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 ; https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html
- B2C electronic services/OSS: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html ; Orden HAC/610/2021 (Modelo 369): https://www.boe.es/eli/es/o/2021/06/16/hac610
- Exchange rate: DGT V2630-17 (via Iberley): https://www.iberley.es/resoluciones/resolucion-vinculante-dgt-v2630-17-16-10-2017-1473112 ; ECB reference rates: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.es.html
