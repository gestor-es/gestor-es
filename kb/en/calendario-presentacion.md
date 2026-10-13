*Translated from the Spanish original [kb/calendario-presentacion.md](../calendario-presentacion.md) on 13.10.2026. The Spanish file is the source of truth.*

## Summary

- Checked against the available primary sources as of **08.10.2026**. The income year (`ejercicio`) and the filing year are separate fields. Annual returns for the 2025 ejercicio are filed in 2026. Annual returns for the 2026 ejercicio are filed mainly in 2027.
- For a small business in common territory, the quarterly modelos 303/130/111/115 are normally filed by 20 April, 20 July and 20 October. **For 4T the deadlines are different:** 111/115 by 20 January; 303/130/349 and 390 by 30 January, moved forward if the day is a non-business day; 180/190 by 31 January, moved forward if needed.
- In 2026 the domiciliación deadline for modelos 303/130 for 4T 2025 is **27 January**. It is not automatically 25 January. For ordinary quarters it is 15 April, 15 July or 15 October. The calendar cannot be implemented with the formula «filing date minus five days».
- Renta 2025 online: **08.04–30.06.2026**. Domiciliación: until **25.06.2026**. Modelo 151 is a separate service. It is not the ordinary Renta WEB. **Cl@ve is accepted**, and the certificate is not the only way to access it.
- For modelo 303 for 4T 2026 the AEAT already publishes **01.02.2027** explicitly. The other 2027 dates below that are not confirmed by an AEAT calendar of their own are marked as calculated. The exact start date of Renta 2026 in 2027 is **UNVERIFIED**.
- Modelos 303/130 can be generated as a text file according to the record layout (diseño de registro) and imported into the Sede form. **It is not CSV, not PDF and not free-form XML**, even though it has closing tags `<T...>`.
- Current files checked: **DR303e26v101.xlsx** for 2026; **DR303e25.xlsx** for 2025; **DR130e15v12.xls** for 2019 and later ejercicios. The year in the name of the 130 specification does not mean that the specification is obsolete.
- Pre303 is a confirmed service for pre-filling the form. A public, documented Pre303 API that lets a third-party program calculate or file the return without the form is **not confirmed**. The SII or VERI*FACTU API does not replace filing the 303.
- The NIE is enough to obtain a Spanish FNMT certificate and to register in Cl@ve, with proper proof of identity. The Russian passport and the TIE **are not DNIe**. An SL files with the electronic certificate of its representative or through an authorised representative. It does not file with a personal Cl@ve as a substitute for the SL's certificate.
- The states «file created», «form validated», «NRC obtained», «return accepted» and «tax paid» are independent. Filing is proven by the **justificante + CSV + AEAT date and time**. With domiciliación you must check the debit to the account afterwards.
- Late filing without a prior requerimiento (formal request from the AEAT), with an amount payable: recargo por declaración extemporánea under art. 27 LGT, **«1 percent plus an additional 1 percent for each full month of delay»**. After 12 months: **15% plus interest**. A return with a zero result or an informative return is not exempt from penalties: its own penalties apply.
- The autoliquidación rectificativa was not introduced at the same time for all modelos. For the 303: from 09/3T 2024. For the 100: from the 2024 ejercicio. For the 200: for periods starting on or after 01.01.2024. The 130 keeps the complementaria. An initial return that was never filed is not a complementaria.

## Rules

1. **Deadlines and their moves depend on the specific modelo and on the AEAT calendar.** According to the AEAT, «if the end of the filing period falls on a non-business day, the period ends on the first following business day». For regional and local holidays, the AEAT states: «If the deadline falls on a local or regional holiday, the period ends on the first business day after the one indicated in this calendar, except for modelo 369». In a note of 03.04.2025, its Collection Department applied this move to «Taxpayers for whom Easter Monday is a holiday (the payment deadline moves to 22 April)». This is an administrative criterion, not an express legal rule (interpretation). Art. 30.6 of Ley 39/2015 (holidays of the place of residence) is not its basis: art. 31.3 provides that the calendar of the electronic office «shall be the only calendar of non-business days applied for computing periods in electronic registers, without article 30.6 applying to them». In addition, in the application of taxes that law applies only «supplementarily» (DA 1.ª.2.a). The official calendar linked from the AEAT Sede (BOE-A-2025-23702) also includes non-business days «Within the territory of the Autonomous Communities». But no source consulted says which municipality counts for electronic filing. The prudent course is to file by the nationwide deadline and treat the day added by a local holiday only as a margin. For bank domiciliación, the AEAT states that «between the end of the filing period for a self-assessment with domiciliación of payment and the end of the general period for filing and voluntary payment of that same self-assessment, **there must be a minimum of three business days or five calendar days**. For these purposes, Saturdays, Sundays, national holidays and regional or local holidays that affect the municipality where the IT Department of the Tax Agency is located shall be considered non-business days». This applies to the 2025–2026 filings covered here. The 2026 table takes precedence over the approximate rule. Sources: [Plazos de presentación de autoliquidaciones con domiciliación bancaria, 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [Vencimientos en días inhábiles, sábados y festivos, 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/recuerde/vencimientos-dias-inhabiles-sabados-festivos.html), [AEAT note of 03.04.2025 (AECE copy)](https://www.aece.es/descargararchivo_docnoticias_3299), [Ley 39/2015, art. 31](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#a31), [Ley 39/2015, DA 1.ª](https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565#daprimera), [Sede, official calendar](https://sede.agenciatributaria.gob.es/Sede/Calendario_fecha_y_hora_oficial.html).

2. **Quarterly periodicity of the 349 does not follow from quarterly periodicity of the 303.** The basic periodicity of the recapitulative statement (349) is monthly. Quarterly filing is allowed «when neither during the reference quarter nor in each of the four previous calendar quarters the total amount of the supplies of goods and services that must be entered in the recapitulative statement exceeds 50.000 euros, excluding Value Added Tax». If the threshold is exceeded within the quarter, «a recapitulative statement must be filed for the month or months elapsed since the start of that calendar quarter». The annual 349 must not be used. If there are no transactions to declare, a «zero 349» is not needed. For July there is an extended deadline until 20 September. For December or 4T, until 30 January. This applies in 2025–2026. Sources: [AEAT, operaciones intracomunitarias](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/5-impuesto-sobre-valor-anadido/5_9-operaciones-intracomunitarias.html), [349 deadlines, IVA manual 2026](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2026/capitulo-09-declaraciones-informativas-iva-379/declaracion-recapitulativa-operac-intracomunitarias-modelo-349/plazo-presentacion.html).

3. **Modelo 036 is an obligation tied to specific events. It is not quarterly.** Registration return (alta): «before starting the corresponding activities or before the obligation to withhold or make payments on account arises». Modification return: «1 month from the day after the modification». Deregistration return (baja): «1 month from the cessation or the effective cancellation of the entries in the Commercial Register». For the autónomo's tax domicile, the census modification return (036), casilla 122, is used. The change of domicile must not wait for the Renta. The application for registration in the Register of Intra-Community Operators (ROI) must be filed before the corresponding intra-community transactions. IVA and IS options have special deadlines. For example, the «Option for the instalment payment on the part of the tax base for the period of the first 3, 9 or 11 months of each calendar year» (art. 40.3 LIS) is exercised in the «month of February of the year in which it is to take effect, only for tax periods that coincide with the calendar year». In 2026 this ran until 02.03.2026. Modelo 037 has been abolished since **03.02.2025**. Sources: [036 in the 2026 calendar](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/modelo-036.html), [modification deadline](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/plazos-presentacion/declaracion-modificacion-modelo-036.html), [casilla 122](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/modificacion-modelo-036/casilla-122-domicilio-fiscal-modelo-036.html), [02.03.2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html).

4. **Identification depends on the filer, not only on the modelo.** Individuals can use Cl@ve for modelos 036, 100, 111, 115, 130, 149, 151, 180, 190, 303, 347, 349, 390, 714, 720 and 721. The certificate or the DNIe work for more procedures. The SL must file electronically with a certificate. The powers of the director or representative must be recognised. The reference number works only for the authorised IRPF procedures. It is not universal access. This applies in 2025–2026. The list was checked against the 2026 calendar. Source: [AEAT, identification](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/recuerde/identificacion-presentar-autoliquidaciones.html).

5. **For a foreign national without a DNIe there is a fully working FNMT route with an NIE.** «Online application for your Certificate» for an individual → «Application Code» → «Proof of identity at an Identity Verification Office», in person, with the valid originals of the TIE or the official NIE document and of the passport → «Download of your User Certificate» following the FNMT instructions. An appointment (cita previa) is normally needed. It is advisable to export a protected backup copy of the private key. For Cl@ve the following are available: «Online registration in the Cl@ve system with a certificate or electronic DNI», in-person registration, or «Online registration in Cl@ve with an invitation letter and CSV», with the letter sent to the tax domicile. With an NIE you enter the support number (número de soporte) of the document. The letter gives a basic registration level. Not all advanced-level procedures are available. Do not assume that a specific type of video identification is available for the Russian passport. This is a current procedure, not an annual tax rate. Sources: [FNMT: documents](https://www.sede.fnmt.gob.es/registro-inicio/preguntas-frecuentes/-/asset_publisher/DKnDigPrgk4U/content/4-3-2-3-acreditacion-de-la-identidad-de-una-persona-fisica), [Cl@ve with a letter](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/registrarse-clave-pin/registro-internet-csv.html), [support number](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/incidencias-tecnicas-clave-pin/introduzca-soporte-valido.html).

6. **Renta WEB and modelo 151 are different workflows.** Ordinary IRPF is filed with Renta WEB / modelo 100. The régimen Beckham uses the 151's own form, with Cl@ve or certificate/DNIe, `Importar` and `Exportar` of the file in BOE format `.151`, `Validar declaración` and `Firmar y enviar`. You cannot automatically replace the 151 with return 100. You cannot state that the 151 is «manual only, without a file». For the 151 the DR for the 2023 ejercicio and later is published. It applies to the years covered here. Sources: [151 technical help](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html), [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), [151 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html).

7. **Importing the return is not filing it.** After `Importar` you must choose the type of return (payable, domiciliación, debt recognition, etc.), correct the errors shown by `Validar declaración`, run `Firmar y enviar` and obtain the justificante. `Guardar`, `Vista previa`, `Exportar` and the NRC, each on its own, do not prove filing. The NRC is the «22-character Complete Reference Number that serves as proof of payment». It is not proof of filing the return. Its data must match NIF/modelo/ejercicio/period/amount. With `Reconocimiento de deuda`, the application for deferral or offset is processed separately, from the `Tramitar deuda` link on the filing receipt, if it is not completed directly in the flow. This applies to the current 2025–2026 forms. Sources: [130](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-130.html), [151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html).

8. **Pre303 does not remove the need to check the source data.** The service offers the Ventana Censal IVA, the Identificación, the Resultado and the Cartera de cuotas a compensar. An extended calculation is possible with the SII or the Libros Agregados, or by importing the record books (libros registro) for non-SII filers that meet the requirements. The representative needs the corresponding powers of attorney (apoderamientos) for all functions, in particular PRE303. As of 08.10.2026, no Pre303 API contract for independent automatic filing was found in the public documentation reviewed. The confirmed route is the form + official file or record books. Sources: [Pre303](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303.html), [functions](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/que-servicios-funcionalidades-tiene-nuevo-pre303.html), [access](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/acceder-pre303.html), [303 technical help](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303.html).

9. **The RETA is managed separately from the AEAT, in Import@ss.** In `Base de cotización y rendimientos` you report or change the forecast of the average monthly net income and the base within the permitted bracket. There are up to six effective dates for changes per year. There is no immediate retroactive change of all previous months. In `Consulta de recibos de trabajo autónomo` the issued contributions are available. The issue must be checked against the bank debit. The system rules apply from 2023 and are applicable in 2025–2026. Sources: [base change](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos), [autónomo guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo+Autonomo/guia), [receipts](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta%2Bde%2Bpagos%2By%2Bdeudas/ConsultaRecibos).

10. **Late filing without a prior requerimiento and non-payment of a debt already declared are different cases.** Art. 27 LGT applies to a self-assessment filed voluntarily after the deadline for a correctly stated period. Do not mix omitted transactions with the current quarter. The recargo is reduced by 25% only if the conditions for paying the debt and the recargo in art. 27.5 are met. Do not promise the reduction for any debt recognition. If the debt is not paid, the enforcement-period recargos of art. 28 may be added. The current scale of art. 27 applies from **11.07.2021** and therefore in 2025–2026. Source: [LGT, arts. 27–28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27).

11. **Having no amount payable does not remove the obligation to file or the penalties.** Art. 198 LGT, for not filing on time without economic harm: «fixed monetary fine of 200 euros or, in the case of census returns […], of 400 euros». For informative returns: «fixed monetary fine of 20 euros for each item or set of items relating to the same person or entity that should have been included in the return, with a minimum of 300 euros and a maximum of 20.000 euros». If they are filed «late without a prior requerimiento from the Tax Administration, the penalty and the minimum and maximum limits shall be half of those provided for in the previous paragraph». This is a possible penalty in a separate procedure. It is not an amount that is added automatically to a tax casilla. If the Treasury suffers harm after a requerimiento, art. 191 may apply: from 50 to 150% of the unpaid tax, depending on the infringement. This applies in 2025–2026. Source: [LGT, arts. 191, 198, 199](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198).

12. **The way to correct a return depends on the modelo and the tax period.** For the 303, from 09/3T 2024, the autoliquidación rectificativa is the general route whether the result increases or decreases. There are special exceptions, in particular certain disputes about output IVA and about breach of a higher-ranking rule. For the 100, from the 2024 ejercicio, the rectificativa is used in the cases provided for. Special complementarias remain for certain regularisation cases. For the 200, in periods starting on or after 01.01.2024, the rectificativa is used. The 130, the current 151 form and ordinary withholdings keep their own mechanisms of complementaria or application for correction. Do not apply the new 100 rule to them automatically. Sources: [303, corrections](https://sede.agenciatributaria.gob.es/Sede/iva/presentar-declaracion-iva-modelo-303/errores-declaracion.html), [FAQ 303](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/autoliquidacion-rectificativa.html), [100 ejercicio 2024](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2024/c18-cuota-liquida-resultante-autoliquidacion/regularizacion-situaciones-tributarias/general.html), [200](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2024/capitulo-02-identificac-autoliq-compl-incn/autoliquidacion-rectificativa.html), [130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

## Figures

### Fixed values for the calendar and the risks

| Parameter | 2025 | 2026 | Detail |
|---|---:|---:|---|
| Quarterly 349 limit | 50 000 € | 50 000 € | Current quarter and each of the four previous ones; without IVA, for the corresponding outgoing transactions |
| Threshold of ordinary transactions per counterparty for the 347 | >3 005,06 € | >3 005,06 € | Annual amount including IVA; the exclusions matter more than the threshold itself |
| Formal 714 obligation regardless of the tax due | Assets or rights >2 000 000 € | Same | In addition to the obligation when tax is payable; count the assets of the relevant tax scope, before debts and taking exempt assets into account |
| Initial 720 threshold | >50 000 € per relevant block | Same | It is not a single threshold for all assets abroad; there are accounting and personal exclusions |
| Subsequent 720 | Increase of the relevant block >20 000 € compared with the last mandatory filing | Same | Also take into account the end of ownership or of powers, not only the increase |
| Initial 721 threshold | In total >50 000 € | Same | Cryptocurrencies held by a custodian abroad; self-custody is not included |
| Subsequent 721 | Increase >20 000 € and certain cases where the status ends | Same | Check the rules of art. 42 quater; do not copy all the 720 rules literally |
| Art. 27, before 12 months | 1% + 1 p.p./full month | Same | Without a requerimiento; days are not divided by 30 |
| Art. 27, after 12 months | 15% + interest | Same | Interest only from the day after the end of those 12 months |
| Reduction of the recargo under art. 27.5 | 25% of the recargo | 25% | Conditional; the debt and the interest are not reduced by this reduction |
| Tax late-payment interest | 4,0625% per year | 4,0625% according to the checked table or its extension | Do not freeze the rate for future years |
| Art. 28: ejecutivo / reduced apremio / ordinary | 5% / 10% / 20% | Same | Mutually exclusive; the 20% is compatible with interest |
| Art. 198: ordinary return without harm | 200 € / 100 € voluntarily | Same | Before other applicable penalty reductions |
| Art. 198: census return | 400 € / 200 € voluntarily | Same | For the autónomo's 036; do not confuse with the 100 € of art.198.5 for an individual without an activity |
| Art. 198: informative return | 20 €/item, min. 300 €, max. 20 000 € | Same | Voluntarily: 10 €/item, min. 150 €, max. 10 000 € |
| Limit of the 349/190/347 web forms | 40 000 records | 40 000 records in the current instructions | If exceeded, file/TGVI; a small file is also accepted |

Sources for the table: [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), [interest, Banco de España](https://clientebancario.bde.es/pcb/es/menu-horizontal/productosservici/relacionados/tiposinteres/guia-textual/tiposinteresrefe/tabla_tipos_interes_demora.html), [AEAT, interest 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html), [714](https://sede.agenciatributaria.gob.es/Sede/no-residentes/impuesto-sobre-patrimonio/declaracion-impuesto-patrimonio-no-residentes.html), [347 exclusions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes.html), [721 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html).

### Filings in 2026 and closing of the 2026 ejercicio in early 2027

All dates are inclusive. `—` means that domiciliación does not apply to an informative return. It does not mean that there is no obligation to file.

| Modelo / period | Filing period | Last day for domiciliación | Status |
|---|---|---|---|
| 111, 115: 4T 2025 | 01–20.01.2026 | 15.01.2026 | AEAT |
| 303, 130: 4T 2025 | 01–30.01.2026 | **27.01.2026** | AEAT |
| 349: 4T/12M 2025; 390: year 2025 | 01–30.01.2026 | — | AEAT |
| 190, 180: year 2025 | 01.01–02.02.2026 | — | AEAT |
| 347: year 2025 | 01.02–02.03.2026 | — | AEAT |
| 720, 721: year 2025 | 01.01–31.03.2026 | — | AEAT |
| 303, 130, 111, 115: 1T 2026 | 01–20.04.2026 | 15.04.2026 | AEAT |
| 349: 1T 2026 | 01–20.04.2026 | — | AEAT |
| 202: 1P 2026 | 01–20.04.2026 | 15.04.2026 | AEAT; it is not by default a «1T quarterly profit» |
| 100, 151, 714: year 2025 | Online campaign 08.04–30.06.2026 | 25.06.2026 | General end and domiciliación confirmed for all three; the 151 is a separate service |
| 303, 130, 111, 115: 2T 2026 | 01–20.07.2026 | 15.07.2026 | AEAT |
| 349: 2T 2026 | 01–20.07.2026 | — | AEAT |
| 200: calendar year 2025 | 01–27.07.2026 | **22.07.2026** | AEAT; 25 July is a Saturday |
| 718: year 2025, if the ITSGF arises | 01–31.07.2026 | 28.07.2026 | AEAT; it does not replace the 714 |
| 303, 130, 111, 115: 3T 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 349: 3T 2026 | 01–20.10.2026 | — | AEAT |
| 202: 2P 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 102: second instalment of the ordinary Renta 2025 with admissible split payment | Until 05.11.2026 | Own deadlines for managing the domiciliación, see below | AEAT; do not transfer this regime automatically to the 151 |
| 202: 3P 2026 | 01–21.12.2026 | **16.12.2026** | AEAT; 20 December is a Sunday |
| 111, 115: 4T 2026 | 01–20.01.2027 | 15.01.2027 | Calculated from the current rule; full 2027 calendar UNVERIFIED |
| 303: 4T 2026 | 01.01–**01.02.2027** | Expected 27.01.2027 | The AEAT has already published the end of filing; the 2027 domiciliación is calculated |
| 130: 4T 2026; 349: 4T/12M 2026; 390: year 2026 | 01.01–01.02.2027 | For the 130, expected 27.01.2027; others — | Calculated: 30 January is a Saturday |
| 190, 180: year 2026 | 01.01–01.02.2027 | — | Calculated: 31 January is a Sunday |
| 347: year 2026 | 01.02–01.03.2027 | — | Calculated: 28 February is a Sunday |
| 720, 721: year 2026 | 01.01–31.03.2027 | — | Current annual rule; the 2027 calendar is not yet confirmed |
| 100, 151, 714: year 2026 | Expected April–30.06.2027 | Expected 25.06.2027 | Start and final calendar of the campaign **UNVERIFIED** |
| 200: calendar year 2026 | Expected 01–26.07.2027 | Expected 21.07.2027 | Calculated: 25 July is a Sunday; check the approved calendar and the public holidays |

Sources: [annual calendar 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual.html), [domiciliación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [30 January](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/enero/hasta-30-enero.html), [2 February](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/febrero/hasta-2-febrero.html), [2 March](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html), [31 March](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-31-marzo.html), [303 until 1 February 2027](https://sede.agenciatributaria.gob.es/Sede/en_gb/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/calendario-anual/febrero-2027/hasta-1-febrero-2027.html).

For the Renta 2025 campaign: AEAT telephone assistance **06.05–30.06.2026**, with appointments **29.04–29.06**; in-person assistance **01.06–30.06**, with appointments **29.05–29.06**. This does not guarantee service for a business case or a régimen Beckham case: admission criteria for assistance apply. [Campaign dates](https://sede.agenciatributaria.gob.es/Sede/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/fechas-campana-renta-patrimonio.html).

Managing the second instalment of the 102: the **current AEAT table**, at the time it was consulted, states for **02.11.2026** «Until 2 November (for taxpayers who have set up domiciliación for the first instalment - revoke/reinstate or set up domiciliación)» and for **20.10.2026** «Until 20 October to change the IBAN». A search extract of that same page showed an old date of 30 September. Use the current page or the current instructions. Do not mix these deadlines with the first domiciliación of the Renta.

### Monthly regimes: all deadlines of calendar year 2026

A small volume does not remove the monthly 303 when REDEME/SII applies for the corresponding reason. Monthly 111/115 arise in particular for large companies. `M` is the month of the transactions. Dates below without a year are in 2026.

| Period | 303: file / domiciliación | 111/115: file / domiciliación | 349: file |
|---|---|---|---|
| 12M 2025 | 30.01 / 27.01 | 20.01 / 15.01 | 30.01 |
| 01M 2026 | 02.03 / 25.02 | 20.02 / 17.02 | 20.02 |
| 02M 2026 | 30.03 / 25.03 | 20.03 / 16.03 | 20.03 |
| 03M 2026 | 30.04 / 27.04 | 20.04 / 15.04 | 20.04 |
| 04M 2026 | 01.06 / 27.05 | 20.05 / 15.05 | 20.05 |
| 05M 2026 | 30.06 / 25.06 | 22.06 / 17.06 | 22.06 |
| 06M 2026 | 30.07 / 27.07 | 20.07 / 15.07 | 20.07 |
| 07M 2026 | 31.08 / 26.08 | 20.08 / 17.08 | **21.09** |
| 08M 2026 | 30.09 / 25.09 | 21.09 / 16.09 | **21.09**, separately from July |
| 09M 2026 | 30.10 / 27.10 | 20.10 / 15.10 | 20.10 |
| 10M 2026 | 30.11 / 25.11 | 20.11 / 17.11 | 20.11 |
| 11M 2026 | 30.12 / **24.12** | 21.12 / 16.12 | 21.12 |
| 12M 2026 | Expected 01.02.2027 / 27.01.2027 | Expected 20.01.2027 / 15.01.2027 | Expected 01.02.2027 |

Source: [official 2026 table](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [349 in September](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/septiembre/hasta-21-septiembre.html). Temporary extensions for extraordinary circumstances take precedence over the basic calendar.

### Import@ss: base change deadlines in 2025 and 2026

| Application date | Effective date of the new base |
|---|---|
| 01.01–28.02 | 01.03 of the same year |
| 01.03–30.04 | 01.05 |
| 01.05–30.06 | 01.07 |
| 01.07–31.08 | 01.09 |
| 01.09–31.10 | 01.11 |
| 01.11–31.12 | 01.01 of the following year |

Neither of the two years covered is a leap year. These are the RETA change deadlines, not the filing deadlines of the AEAT modelos. It is also not guaranteed that the deadline moves to the next business day under the rules of tax domiciliación. Source: [TGSS, Base de cotización y rendimientos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos).

## Formulas for the engine

### 1. Choosing the obligation and the calendar

Input: the profile and its validity intervals; the taxpayer's NIF; ejercicio/period; census obligations; type of transaction or withholding; REDEME/SII; 349 history; financial year-end date of the SL; history of previously accepted returns; AEAT requerimiento; payment method. Output: the list of obligations with the proof that they apply, the filing deadline, the separate domiciliación deadline and the status of the source.

```text
for each model, tax_period:
    applicable = obligation_rule(model, profile_at_period, activity, transactions, census)
    # The absence of a payment does not on its own mean applicable = false.
    if applicable:
        if official_AEAT_calendar contains (model, tax_period):
            filing_deadline, debit_deadline = published_dates
            confidence = VERIFIED
        else:
            filing_deadline = next_official_business_day(statutory_due_date)
            debit_deadline = provisional_debit_rule(model, filing_deadline)
            confidence = PROVISIONAL_UNVERIFIED
        display separately tax_period, filing_window, filing_deadline, debit_deadline
        if today > debit_deadline and today <= filing_deadline:
            disable new domiciliación; offer admitted payment/NRC routes
        if today > filing_deadline:
            preserve period; select late-original or correction workflow
```

Do not move the 111/115 to 30 January to follow the 303. For the 202, create `1P`, `2P`, `3P` in April, October and December, not `1T–4T`. For the 200, the legal deadline is 25 calendar days after the six months following the end of the tax period, with the move provided for. The July date applies only to a financial year that coincides with the calendar year. Reminders can be sent in advance according to an internal setting. The internal date must not be shown as the legal deadline.

If the domicile changes, store separately the actual date of the change of domicile and the date it was reported in the 036. For general IRPF, the region (comunidad) is determined by the rules of habitual residence for the year. The tax is not split by months between two regions. In the régimen Beckham there is no regional scale of ordinary IRPF. The address and the Comunidad in the 151 must still be updated.

### 2. Formats: record by modelo and year

**The links to the specifications are a mandatory part of the generator contract.** They are chosen according to the `ejercicio`, not according to the calendar date of the export.

| Modelo | Official specification | Filing method and type of structure |
|---|---|---|
| 303 of 2025 | [DR303e25.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/DR303e25.xlsx), updated on 04.12.2025 | Pre303/web form with Importar; fixed width by pages with `<T...>` |
| 303 of 2026 | [DR303e26v101.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_26/DR303e26v101.xlsx), updated on 28.01.2026 | Same; inside the workbook the version is shown as `10.01`; do not infer the schema number from the file name |
| 130 of 2025/2026 | [DR130e15v12.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/DR130e15v12.xls), March 2019, version 1.2 | Form, Importar/Exportar `.130`; one page and wrapper |
| 111 | [dr111e16v18.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/dr111e16v18.xls), May 2021, for 2019+ | [Electronic form with Importar](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-111/presentacion-electronica-modelo-111.html); fixed width with wrapper |
| 349 | [DR_Anexo_349.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_20/DR_Anexo_349.pdf), Orden HAC/174/2020, 2020+ | [Form ≤40 000 records or filing by file](https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/identificacion-realizar-operaciones-otros-empresarios-ue/modelo-349.html); type 1 filer + type 2 transactions/corrections |
| 390 of 2025 | [dr390e2025.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/dr390e2025.xlsx), updated on 05.12.2025 | [Form](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390.html) and [separate filing by file](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390/modelo-390-presentacion-mediante-fichero.html); fixed-width structure by pages |
| 190 of 2025 | [DISENOS_LOGICOS_190_2025.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos_25/DISENOS_LOGICOS_190_2025.pdf), Orden HAC/1431/2025 | Form ≤40 000 records or [TGVI online](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/declaraciones-informativas-ayuda-tecnica/modelos-190-198/modelo-190-fichero.html); type 1 + type 2 recipients |
| 347 of 2025+ | [347.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos/347.pdf), Orden HAC/1431/2025 | [Form ≤40 000 records or TGVI](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/forma-presentacion.html); type 1 + type 2 declared parties/properties |
| 151 of 2025/2026 | [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), 2023+ | Own web form, Importar/Exportar; export name `NIF_Ejercicio_0A.151` |
| 100 of 2025 | [Renta2025.xsd](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/Renta2025.xsd), [dictionary](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/diccionarioXSD_2025.properties) | Renta WEB; the published XML/XSD is a different format, not the 303/130 container |

For the 390 of the 2026 ejercicio, no confirmed DR of its own was found on the check date. Do not file the 2025 file with the year changed as if it were guaranteed to be accepted. For the 190 of 2026, which is updated every year, you must also check its publication again before the campaign. Catalogues: [100–199](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-100-199.html), [300–399](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-300-399.html), [303 archive](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/ejercicios-anteriores-modelos-300-399.html).

In the informative modelos 349/190/347, the fixed-length records are defined in their PDFs, not with the `<T303...>` structure. A type 1 record identifies the filer, the period and the control totals. Type 2 records contain the counterparties or recipients and the special records. They cannot be replaced by an accounting CSV. The mappings of keys and subkeys and the counters are taken from the **specific DR**, not from the column names of the on-screen form. For the 190, the AEAT warns explicitly that the first filing method chosen (form or file) determines the admissible route for later filings. You must store the channel of the original return. TGVI may allow you to file the correct records and correct the others later. Do not treat the whole original set as filed until you have checked the accepted and rejected records.

### 3. Common serialisation of the 303/130

Below are the **checked positions, counted from one**, the lengths and the signs. For an array in a program, the index is `position - 1`. Length is measured in bytes of the chosen single-byte encoding, not in UTF-8 code points.

```text
format_amount(value_eur, width, signed):
    # The input is already calculated by the tax module to the euro cent.
    cents = exact_integer(abs(value_eur) * 100)
    if value_eur < 0:
        require signed
        return "N" + decimal_digits(cents).left_pad("0", width - 1)
    return decimal_digits(cents).left_pad("0", width)

format_text(value, width):
    normalize according to DR: uppercase, no accented vowels,
    allow the specified Spanish Ñ/Ç; encode ISO-8859-1
    reject unsupported characters or overflow; right_pad spaces to width

serialize_page(schema, values):
    allocate exactly schema.total_length bytes
    fill An/A/reserved fields with spaces and numeric fields with zeroes
    write every constant and conditional flag as defined by that schema
    write each value into [position-1 : position-1+length]
    reject overflows, unsupported signs, incompatible year/period and missing mandatory data

file = opening_17_bytes + AUX_311_bytes + concatenated_pages + closing_18_bytes
# No CSV separators, no UTF-8 BOM, no XML indentation and no line breaks inside the record.
```

Source for the encoding, the alignment and the `N` for negative values: [AEAT, Diseños de registro — short manual, pp. 4–6, 10–12](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/Ayudas/Disenyos_registro_Manual_uso.pdf). It is positional text, not an XML document for an XML serialiser: spaces are significant and `trim` is not allowed. Money calculations are done with Decimal or integer cents. The final rounding to 0,01 € follows the rules of each casilla. If the specific instruction does not say otherwise, the technical convention is decimal ROUND_HALF_UP, checked against the AEAT form. Do not round each intermediate expression. Do not use binary float.

**The wrapper has the same positions in both DRs checked:**

| Absolute position | Length | Content |
|---:|---:|---|
| 1 | 2 | `<T` |
| 3 | 3 | `303` or `130` |
| 6 | 1 | `0` |
| 7 | 4 | Ejercicio, for example `2026` |
| 11 | 2 | Period, for example `3T`; in the monthly 303, `01`…`12` |
| 13 | 5 | `0000>` |
| 18 | 5 | `<AUX>` |
| 23 | 70 | Spaces, reserved for the AEAT |
| 93 | 4 | Version of the developer's program |
| 97 | 4 | Spaces |
| 101 | 9 | Developer's NIF according to the DR instruction |
| 110 | 213 | Spaces |
| 323 | 6 | `</AUX>` |
| 329 | Variable | Pages of the modelo |
| After the last page | 18 | `</T3030EEEEPP0000>` or `</T1300EEEEPP0000>` |

Example start for the 303 for 3T 2026: `<T303020263T0000><AUX>`; for the 130: `<T130020263T0000><AUX>`. Here `EEEE`/`PP` are metacharacters of the explanation, not literal values in the file. In the DR130, the description of the closing tag contains the typo `T1230`, but the **Contenido** column states unambiguously `</T1300AAAAPP0000>`: use 130.

### 4. Modelo 130: single, fully defined page

After the wrapper comes page `DR 13001` of **600 bytes**. The positions given are **local to the page**. Therefore its position 1 is at position 329 of the complete file.

| Position | Length | Field |
|---:|---:|---|
| 1 | 11 | `<T13001000>` |
| 12 | 1 | Space, complementary-page indicator; it does not indicate that the return is a complementaria |
| 13 | 1 | Type: `I` payment, `U` domiciliación, `G` CCT, `N` negative, `B` to deduct |
| 14 | 9 | NIF |
| 23 | 60 | Surnames |
| 83 | 20 | First name |
| 103 | 4 | Ejercicio |
| 107 | 2 | `1T`…`4T` |
| 109 + 17×(k−1), k=1…19 | 17 per field | Consecutive casillas `[01]`…`[19]` |
| 432 | 1 | `X` for a complementaria return; otherwise a space |
| 433 | 13 | Justificante number of the previous return, if it is a complementaria |
| 446 | 34 | IBAN for domiciliación, left-aligned and followed by spaces |
| 480 | 96 | Reserved for the AEAT, spaces |
| 576 | 13 | Reserved electronic seal, spaces |
| 589 | 12 | `</T13001000>` |

Casillas with the `N` sign: **03, 07, 11, 14, 17, 19**. The other money fields are `Num`, without negative values. A 17-character field has two implied decimals, without a comma or a point. Total length of a simple return: **328 + 600 + 18 = 946 bytes**.

The tax module supplies the calculated casilla values, and the serialiser does not recalculate them. In the complementaria the whole period is recalculated. `[18]` is the sum of the **payable** results of the previous 130s for the same ejercicio/period. It is not the tax for all previous quarters. `[19] = [17] − [18]`. An initial 130 that was never filed has `[18]=0`, no `X` and no fictitious previous justificante. A zero or negative result must not be turned into `I` just to be able to pay. Sources: the DR130 cited above and the [official 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

### 5. Modelo 303 of 2026: pages and casillas

The workbook contains `DP30300`, `DP30301`, `DP30302`, `DP30303`, `DP30304`, `DP30305` and `DP303DID`. For an ordinary activity under the general regime you need the data of page 01, the result of page 03 and the DID payment section. Page 02 is for the simplified regime. Page 04 contains the annual information of filers exempt from the 390. Page 05 contains the corresponding information on the pro-rata or differentiated sectors. **Empty pages 04/05 are not included**, according to the DR notes. For the applicable page 02 and the repeatable pages, follow their own repetition conditions. Do not create page 02 for a consultant who is not in the simplified regime.

| Page | Start / end | Total length | Important |
|---|---|---:|---|
| DP30301 | `<T30301000>` / `</T30301000>` | 1 581 | NIF, period, indicators and general regime |
| DP30303 | `<T30303000>` / `</T30303000>` | 1 017 | Additional information, result, rectificativa |
| DP30304 | `<T30304000>` / `</T30304000>` | 998 | Last period of filers exempt from the 390; do not add without data |
| DP30305 | `<T30305000>` / `</T30305000>` | 1 528 | Pro-rata/sectors; do not add without data |
| DP303DID | `<T303DID00>` / `</T303DID00>` | 823 | IBAN/BIC/foreign bank |

For the combination 01 + 03 + DID, the length is **3 767 bytes** including the wrapper. This is a structural check of that combination. It is not proof that any zero value passes the AEAT business validation.

**DP30301: the positions are local to the page.** Start: position 12, space; 13, type of return; 14/9, NIF; 23/80, name or company name; 103/4, ejercicio; 107/2, period. Indicators 109–130 are taken from the DR. Do not fill them all with zeroes. For example, for someone who is taxed only under the ordinary general regime, position 111 = `3`; voluntary SII, 127; exemption from the 390, 128 (`0` outside the last period; in the last one, `1`/`2`); annual volume, 129 according to the DR condition. Position 130 is a new special fuel field. For the quarters and for 01 its value is `0`. Its presence changes the offsets compared with some old schemas.

| Casilla | Position/length DP30301 | Type |
|---|---|---|
| 01 / 02 / 03 | 209/17; 226/5; 231/17 | Num; rate `00400` |
| 04 / 05 / 06 | 287/17; 304/5; 309/17 | Num; rate `01000` |
| 07 / 08 / 09 | 326/17; 343/5; 348/17 | Num; rate `02100` |
| 10 / 11 | 365/17; 382/17 | Num; intra-community acquisitions |
| 12 / 13 | 399/17; 416/17 | Num; other cases of inversión del sujeto pasivo |
| 14 / 15 | 433/17; 450/17 | N; modifications |
| 27 | 696/17 | N; total output tax (cuota devengada) |
| 28 / 29 | 713/17; 730/17 | Num; domestic current goods and services |
| 30 / 31 | 747/17; 764/17 | Num; domestic investment goods |
| 32 / 33 | 781/17; 798/17 | Num; current imports |
| 34 / 35 | 815/17; 832/17 | Num; investment imports |
| 36 / 37 | 849/17; 866/17 | Num; current intra-community |
| 38 / 39 | 883/17; 900/17 | Num; investment intra-community |
| 40 / 41 | 917/17; 934/17 | N; correction of deductions |
| 42 / 43 / 44 | 951/17; 968/17; 985/17 | N |
| 45 / 46 | 1002/17; 1019/17 | N |
| Reserved + seal | 1036/521; 1557/13 | Spaces |
| End | 1570/12 | `</T30301000>` |

The other fields, including the zero-rate and equivalence surcharge (recargo de equivalencia) fields, are still physically present. They are filled **with the constants and zeroes of the DR**. They are not removed. For the IVA total, use all the prescribed addends, not only the usual casillas:

```text
303[27] = [152]+[167]+[03]+[155]+[06]+[09]+[11]+[13]+[15]
          +[158]+[170]+[18]+[21]+[24]+[26]
303[45] = [29]+[31]+[33]+[35]+[37]+[39]+[41]+[42]+[43]+[44]
303[46] = [27] - [45]
```

**DP30303: key result fields.**

| Casilla/field | Position/length | Type/meaning |
|---|---|---|
| 59 | 12/17 | N; intra-community supplies and services |
| 60 | 29/17 | N; exports and similar transactions; does not automatically include every service outside the EU |
| 64 | 199/17 | N; `[46]+[58]+[76]` |
| 65 | 216/5 | Num; % State, 100% = `10000` |
| 66 | 221/17 | N; attributable to the State |
| 77 | 238/17 | Num; import IVA pending |
| 110 / 78 / 87 | 255/17; 272/17; 289/17 | Num; balance, part applied, balance of previous periods |
| 68 | 306/17 | N; State/foral regularisation |
| 108 | 323/17 | N; special adjustment for a discrepancy; it is not a universal «manual correction» |
| 69 | 340/17 | N |
| 70 | 357/17 | Num; previous payable results of the same period |
| 109 | 374/17 | Num; refunds agreed by the AEAT for the same period |
| 112 | 391/17 | Num; special payments on account of modelo 319 for fuel, normally 0 |
| 71 | 408/17 | N; final result |
| No activity | 425/1 | `X` or space; zero IVA does not automatically mean that there is no activity |
| Rectificativa | 426/1 | `X` or space |
| Previous justificante | 427/13 | Mandatory according to the conditions of the rectificativa |
| Change or cancel the previous domiciliación | 440/1 | `X` or space |
| 111 — correction amount | 441/17 | Num; according to the rectificativa rules, not the total amount overpaid |
| Reason for corrections / discrepancy | 458/1; 459/1 | `X` or space |
| Reserved / closing | 460/546; 1006/12 | Spaces / `</T30303000>` |

```text
303[87] = [110] - [78]
303[69] = [66] + [77] - [78] + [68] + [108]
303[71] = [69] - [70] + [109] - [112]
# Initial ordinary return: [70]=[109]=0; [108]=0 if there is no special reason.
# The IVA module decides how [78] is applied and whether a negative result is refunded or offset.
# [87] cannot be treated as the new full balance: it is the balance of previous periods.
```

In DID: SWIFT-BIC, position 12/11; IBAN, 23/34; bank, 57/70; address, 127/35; city, 162/30; country code, 192/2; SEPA flag, 194/1 (`0` empty, `1` Spain, `2` EU-SEPA, `3` other); reserved, 195/617; end, 812/12. A Spanish IBAN is the first 24 characters with `ES`. The rest of the field is spaces. In a rectificativa with casilla 111>0, bank details are also required in some variants that are not refunds, except in the case provided for in the DR of changing the original domiciliación.

303 type: `I` payment, `U` domiciliación, `C` offset, `D` refund, `N` no activity/zero result, `G`/`V` CCT, `X` refund by transfer abroad. For a rectificativa with `[71]<0` and `[111]>0`, the DR requires determining the type from the part of `[71]` that does not correspond to `[111]`. Do not choose the type only from the sign of `[71]`.

These offsets apply **only to DR303e26v101**. For 2025 use the corresponding sheets of DR303e25. No real test file was generated or imported into the Sede here. The structure given was extracted from the official workbooks, not from a sample accepted by the server.

### 6. Acceptance, correction and payments

```text
if no accepted_return_for_same_model_year_period:
    mode = ORIGINAL  # even after the deadline
else:
    mode = model_period_correction_rules(model, year, period, error_reason)
    attach previous_justificante
    recompute complete corrected return; do not send only differences

after user imports file:
    keep local draft until receipt proves successful submission
    persist NIF, model, year, period, submission_timestamp, justificante, CSV,
            accepted_document, result, chosen_payment_method
    if payment_method == NRC:
        require NRC corresponds to that exact obligation and amount
    if payment_method == DOMICILIACION:
        mark PAYMENT_PENDING until debit is confirmed
    if payment_method == DEBT_RECOGNITION:
        retain separate debt/payment/deferral application status
```

For the 100 in Renta WEB, use the built-in option `Modificar declaración presentada`. For the rectificativa provided for, you identify the original return and casillas **103/104** according to the 2024 manual, but **you must check the dictionary of the specific ejercicio before generating**. For the 200, use Sociedades WEB or its current DR and the rectificativa block. Do not take the numbers from the 303. For the informative 190/180/347/349 you need their own operations of registration, modification or deletion, complementaria or substitute return, or record corrections, depending on the modelo and the chosen channel. You cannot file a second «ordinary» file and treat the first one as cancelled.

### 7. Recargo and estimate of the delay

Input: the original legal deadline `D`, the actual filing date `F`, the unpaid amount resulting from the late self-assessment `B`, whether there was a requerimiento before filing, the payment history and the applicable annual interest rates. Output: an **estimate** of the recargo and the interest and the processing route. It is not a new casilla of the original return.

```text
if F <= D:
    late_filing_recargo = 0
elif previous_requerimiento:
    do not apply voluntary_art27_estimate
    route = review assessment/sanction procedure
elif B <= 0:
    recargo_art27 = 0
    route = evaluate formal_penalty_art198  # does not mean «no penalty»
else:
    if F is within first 12 calendar months after deadline:
        m = legally_completed_calendar_months(D, F)
        recargo = cents_round(B * (0.01 + 0.01*m))
        interest_art27 = 0
    else:
        recargo = cents_round(B * 0.15)
        interest_start = day_after(add_calendar_months(D,12))
        interest = cents_round(sum_for_each_rate_year(
            B * annual_rate * chargeable_days_in_year / days_in_year))
    if all conditions of art27.5 are established:
        recargo_payable = cents_round(recargo * 0.75)
    else:
        recargo_payable = recargo
```

`legally_completed_calendar_months` are calendar months, **not** `floor(days/30)`. The start and end of the monthly interval, months without the corresponding day and the exact 12-month limit must be checked against the official AEAT calculation or notification. The public wording found repeats the law without an example of its own for the exact limit. Until that check, the engine must show a range or a warning on the doubtful boundary date, and must not invent a guaranteed rate. This does not affect clear cases: a debt of 1 000 € and filing ten days late → recargo of 10 €; with the applicable reduction → 7,50 €. After more than 12 months → 150 € plus interest from the date stated, not interest for the whole first year.

The AEAT normally assesses the recargo separately. **It must not be added to the result of casilla 19 of Modelo130 or casilla71 of Modelo303**. If the return was already accepted on time but the bank did not debit the amount, check art.28 and the payment circumstances instead of filing a duplicate and calculating art.27. Withholdings and some other debts do not allow ordinary deferral: the existence of the debt recognition option does not automatically give a right to deferral.

## Deadlines and modelos

### Who files what

Here «Beckham» means a valid and accepted art.93 option, with its conditions met. Having an entrepreneur visa is not enough. The fact that a modelo is not on the list that a gestoría handles does not prove an exemption.

| Modelo | Who/when | When it does not arise / important limitation | Deadline |
|---|---|---|---|
| 303 | Autónomo with either of the two IRPF profiles and SL with the corresponding activity subject to IVA | The régimen Beckham does not exempt from IVA. An exclusively exempt activity may have no periodic obligation; inversión del sujeto pasivo and other events are analysed separately. If there is a periodic obligation, the period with a zero result is also filed | Quarter/month according to the tables |
| 130 | Autónomo in direct estimation (estimación directa); application to an activity admitted under art.93 is decided by the special rules, not by the profile label | In professional activities under ordinary IRPF, exempt if ≥70% of the previous year's income had withholding; in the start year, the applicable period. The SL does not file it. In the régimen Beckham it cannot be included or excluded automatically without rules by type of income | 1T–3T by day 20; 4T by 30 January, moved if needed |
| 349 | Any of the profiles with the corresponding intra-community supplies or acquisitions of goods or services | Transactions outside the EU do not on their own give rise to the 349; without transactions to declare it is not filed as zero. Buying SaaS from the EU can also create the obligation | Month/quarter according to its own test |
| 111 | Individual or SL that pays salaries, professional income or other included income with an obligation to withhold | These are the **payer's** withholdings, not the withholding on your own issued invoices. If included income was paid without effective withholding because of a zero rate, a negative return may be required; if there was no payment at all, it is a different case | By day 20 after the quarter; monthly for the corresponding large payers |
| 115 | Payer of a business lease of urban property subject to withholding | Check the exceptions and the landlord's certificate; not every rental of a home by a private individual gives rise to the 115 | Like the 111 |
| 202 | SL and other IS taxpayers obliged to make instalment payments | For a small ordinary SL with no amount payable, filing is normally not needed; large taxpayers have special rules for zero filing. Do not create the 202 for the individual shareholder | April/October/December, not July |
| 390 | Annual IVA summary return for those obliged to file periodic IVA returns | Exempt for the SII and for quarterly filers taxed only under the simplified regime or urban leasing in common territory; the annual data move to the last 303. An ordinary consultant under the general regime is not exempt just for having 12 invoices | By 30 January |
| 190 | Included annual payments and withholdings, linked to the 111 | It is not a report of the withholdings that your own clients made. Include the corresponding zero or exempt payments according to the modelo rules | By 31 January |
| 180 | Annual summary of the corresponding leases and 115 withholdings | It does not arise just from owning a home or from being the person who collects the rent | By 31 January |
| 347 | Autónomo/SL with included transactions with third parties above the threshold | Transactions already covered by other special reporting with the required match of content are excluded: for example, the 349 and the corresponding withholdings; the SII and other personal exclusions. **A service outside the EU is not the same as an exported good**; the export exclusion does not transfer automatically | February of the following year |
| 100 | Ordinary IRPF of the autónomo; the SL director as an individual, according to their own obligation | Since 2023, anyone who was in the RETA at any time in the year must file IRPF; but with a valid régimen Beckham the 151 applies instead of the ordinary 100 | Renta campaign of the following year |
| 151 | Valid special regime of art.93, including the corresponding director or entrepreneur | It does not replace the 303, the withholdings or the SL's own returns. It is not granted automatically for having an NIE or a visa | Annual IRPF campaign deadline; in 2026, until 30 June |
| 200 | SL for its own tax period | It is not exempt for «having no activity» or for a zero profit; as long as the entity and the IS obligation exist, the ordinary SL files | 25 days after the six months following the end of the period |
| 714 | Individual with a positive Patrimonio tax due or with assets and rights above 2 million € in the applicable scope | In the régimen Beckham, real obligation for the corresponding Spanish assets, not automatically for worldwide assets. Regional minimums and benefits are calculated separately | Together with the Renta; in 2026, until 30 June |
| 720 | Ordinary resident or SL with assets, positions and thresholds abroad, without an exclusion | The AEAT explicitly exempts the individual under art.93. For an SL or individual with proper accounting, there may be accounting exclusions of their own. The director's personal assets and the SL's assets are checked separately | 1 January–31 March |
| 721 | Cryptocurrencies abroad held by a custodian, corresponding positions and threshold | Self-custody is not included. Do not infer an exemption of its own for the régimen Beckham only from the text of FAQ720; see «Open questions» | 1 January–31 March |
| 036 | Alta, modification or baja, domicile, IAE and obligations, ROI, tax options provided for | It is not filed every year to confirm that nothing has changed. The 037 is no longer used | According to the event, normally one month; alta/ROI before the transactions; own deadlines for the options |
| 102 | Second instalment of the admissible 60/40 split payment of the ordinary Renta | It is not a universal deferral for all modelos; a late initial self-assessment and the 151 require their own rules | 05.11.2026 for Renta2025 |
| 718 | Individual when the Temporary Solidarity Tax on Large Fortunes arises | Do not create it automatically for everyone who files the 714; separate test of tax due and scope of liability | July of the following year; in 2026, until 31 July |

Primary sources for the conditions: [130, instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html), [202, when to file](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/4-impuesto-sobre-sociedades/4_8-pagos-fraccionados/4_8_2-modelos-pagos-fraccionados.html), [390, who must file](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-09-declaraciones-informativas-iva-379/declaracion-resumen-anual-modelo-390/obligados-presentar-declaracion.html), [347, exclusions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 and art.93](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes/contribuyentes-obligados-declarar.html), [721](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html). The legal calculations for each tax and the conditions of the régimen Beckham must be taken from the corresponding tax module. The calendar does not duplicate them.

Additional obligations are included according to the event: the 149 for an option, waiver or exclusion from the régimen Beckham; the 123/193 for the corresponding capital payments, for example SL dividends; the 216/296 for certain payments to non-residents. They are not obligations of every independent professional, and they do not replace the modelos in the list. The holder does not need collaborator status (colaborador social) to file personally with a self-hosted application. To file on behalf of another legal entity, the proper apoderamientos are needed.

For the **149** in 2025–2026: the main option, at most **6 months** from the start of the activity according to the registration with Social Security or the admissible document; the associated person, whichever deadline ends later between the end of their six months from entry and the main person's deadline. Waiver: **November–December of the year before the year in which it takes effect**; for example, to waive with effect in 2027, 01.11–31.12.2026. Exclusion: **one month from the failure to meet the conditions**; end of the posting while keeping tax residence for the year: **one month from the end of the posting**. Filing the 149 and its annexes is a procedure of its own, not an optional annex of the annual 151. Sources: [calendar of non-periodic IRPF modelos 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/impuesto-sobre-renta-personas-fisicas.html), [149 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-149-irpf-comunicacion-opcion-exclusion_/instrucciones-cumplimentar-comunicacion.html).

### Practical user path

1. Obtain the FNMT certificate or Cl@ve, and check the NIE/NIF and the domicile at the AEAT. For the SL, obtain the certificate or the representative's apoderamientos. Do not store the private key unprotected on the server. Do not hand it to a marketplace without consciously formalising the representation.
2. Choose the exact modelo, ejercicio, period and filing method. Export the file of the corresponding version or use the record books in the prescribed format.
3. In the Sede, choose `Presentación`/`Importar` or the dedicated `Presentación mediante fichero`, where it exists. The built-in web import of a file is not the same as a dedicated API. Modelos 349/190/347 accept TGVI. The 390 accepts its own filing by file. For individual modelos 303/130/111 the ordinary route of the form with Importar is confirmed.
4. Check the casillas against the books, the offset history and the returns already accepted. Correct the errors and read the warnings. The data pre-loaded automatically in Pre303 may not cover the whole activity.
5. If the result is positive, choose an available payment method. After the domiciliación deadline, you can still file within the general deadline with an admissible payment method. You do not need to wait for the next quarter. The foreign bank/SEPA and `Reconocimiento de deuda y pago por transferencia` have their own conditions and payment deadlines.
6. `Formalizar ingreso / devolución` → `Firmar y enviar` → store the PDF, the CSV, the justificante and the payment confirmation separately. For a transfer or debt recognition, follow the pending steps. For domiciliación, check the actual debit, any bank rejection and the balance.
7. In Import@ss, check separately the RETA alta, the income and the base, the regularisation notice and the receipts. You can access it with a certificate, Cl@ve or SMS where available, if the number is registered with the TGSS. Having an NIE at the AEAT does not guarantee that the phone is linked at the TGSS.

## Edge cases

### Taxes, deadlines and filing

- **One EU client, 60 000 € in a quarter:** the 303 can stay quarterly, and the 349 can become monthly. The 349 threshold is not checked only by the number of invoices. If it is exceeded in the second month, you cannot wait for the end of the quarter and then send an ordinary quarterly 349.
- **US client and a service from Ireland:** the sale does not give rise to the 349, but the purchase can. The absence of Spanish IVA on both invoices does not mean that the regime is the same. Service transactions outside the EU are checked for the 347 separately from exports of goods.
- **A Spanish client withheld IRPF from our invoice:** their withholding goes into our IRPF calculations, but it does not give rise to our 111. If we pay a Spanish professional an invoice with withholding, the 111/190 may arise.
- **Zero IVA payable because of foreign clients, but there was activity:** do not mark `Sin actividad` automatically. If expenses were higher, choose the correct offset or refund, not a simple zero result. A negative 303 is still a return.
- **Baja of the autónomo in the middle of the year:** quarterly and annual obligations that have already arisen remain. In some cases the exemption from the 390 is lost if the last 303 of the year is no longer required. A baja date in the RETA does not prove the simultaneous baja of all obligations with the AEAT.
- **Move between autonomous regions:** it does not change the state rates of art.93. It requires the correct domicile and 151 data, and a separate determination of the region for ordinary IRPF and Patrimonio. You do not calculate half a year with one regional scale and half a year with another.
- **Régimen Beckham and family:** FAQ720 contains an old general remark that the regime does not extend to the family. After the extension of art.93 in 2023, family members who meet the requirements can exercise their own option. Each person's situation is checked. The wife is not exempted just because of the husband's regime. Her own option is not denied because of an obsolete FAQ sentence.
- **SL and director:** the SL's NIF, returns, certificate and payments are separate from the director's own modelos 100/151/714. Filing the 200 with the individual's data is not accepted. The personal Cl@ve does not replace the company's certificate.
- **The last domiciliación day has passed, but not the general deadline:** this is not a late filing. Offer the NRC or another admissible payment. Do not calculate the recargo in advance.
- **Tax paid, but the connection dropped during signing:** look for the accepted return and the NRC. Do not pay again blindly. **The signature was completed, but the debit was not:** look for the debt or the domiciliación status. Do not send a duplicate return.
- **Correction of an accepted 303 with a previous domiciliación:** the new rectificativa does not guarantee the automatic cancellation of the previous debit. Check the special indicator, the admissible modification deadline and the AEAT confirmation. Otherwise there may be a double debit or an incorrect difference.
- **Missed deadline with a requerimiento:** the safe voluntary art27 calculation may no longer apply. The requerimiento is not only a paper letter: electronic notifications officially served are taken into account. Do not promise «only 1%».
- **Error in a previous quarter found after filing the annual return:** a consistent correction of the corresponding quarter and of the annual information is required. Increasing the current 303/130 without linking it correctly to the previous period is not always a legal regularisation.
- **An informative return accepted part of the records:** store the identifiers and counters of the accepted set. «File sent» does not mean «all 190/349 transactions accepted». Rejected records are corrected in the way that the channel used allows.

## Open questions

1. **2027: the full calendar is not published.** Direct confirmation of 01.02.2027 for the 303 for 4T 2026 was found. The other future dates were derived from the current deadlines and the calendar moves, and they are marked explicitly. The start of Renta2026, its annual order and the final domiciliación deadlines must be loaded after publication. The expected 7/8 April 2027 cannot be shown as an established date. A regional public holiday on 25/26 July 2027 may affect the specific official calendar of the 200: the calculation of 26 July is not final.

2. **Pre303 API: UNVERIFIED.** The Pre303 pages, the procedures, the description of the functions and the 303 technical help were reviewed. No WSDL/OpenAPI published specifically for Pre303 was found. This does not prove that no closed integration channel exists. The confirmed route for the project is the official import of the file or of the books into the form and the user's signature. Neither undocumented HTTP calls nor the SII or VERI*FACTU API may be declared an accepted substitute for filing.

3. **The files are described, but import on the server has not been tested.** The byte positions of the 303/130 were extracted from the official Excel files. No test returns, real payments or filings were made. Before going into production, the main agent must check export→import in the official simulator or form without sending: 2025/2026, payment/negative/offset, negative `N`, NIE, Ñ, IBAN, rectificativa. This is a mandatory compatibility check, not a stated result of this research.

4. **DR versions and conditional indicators change.** In the 2026 303, additional fuel/modelo 319 fields were found. Using the 2025 offsets is dangerous even for a user who does not trade in fuel. The 2026 DR for the 390 is not confirmed. Exports must be blocked if the ejercicio is not supported, instead of using the «last known format» without a warning.

5. **NIF Empresa Desarrollo for a self-hosted developer.** The DR requires the NIFED and the SW version, but the instruction reviewed does not explain a developer registration of its own for an isolated personal import. Do not enter an invented vendor NIF. Do not claim that leaving the field empty is enough. For your own Spanish developer, use a valid NIF and check it with the validator. Unknown requirements of a specific channel are referred to the AEAT.

6. **The 721 under the régimen Beckham is a separate, unchecked qualification.** FAQ720 explicitly exempts art93. The FAQ721 that was read lists the residents and the custody criteria, but it contains no equivalent direct clarification for art93. Do not grant the automatic 721 exemption only by analogy. If the user has cryptocurrencies held by a custodian abroad above the threshold, the possible obligation is kept, with manual review or a prior consultation with the DGT. An unnecessary return is not filed automatically «just in case».

7. **Full-month and 12-month boundary for the recargo.** The sources confirm the formula, but no official example exactly at the boundary was found. The exact estimate on those dates is marked UNVERIFIED and is checked against the AEAT calculation or notification. Months are not replaced by blocks of thirty days. The 2026 interest table confirms 4,0625%, but future years need a version of their own, not an extrapolation.

8. **Conflict of domiciliación deadlines in the AEAT sources.** For the **151**, the 2026 calendar table explicitly states **25 June**, but the [151 instructions for the 2023 ejercicio and later](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html) state **26 June** twice. An additional check of the primary rule resolves the contradiction in favour of **25.06.2026**: [Orden HFP/1338/2023, art. 4.2, p. 5 of the PDF](https://www.boe.es/boe/dias/2023/12/15/pdfs/BOE-A-2023-25416.pdf) states that domiciliación «may be carried out from the start of the period until, as a general rule, five days before the end of the filing period». That is 25 June if the end is 30 June. It matches the calendar. The 26 June date in the instructions must not be used to accept a new domiciliación of the 2025 151. For the **102**, the search showed 30 September. The current 2026 table that was read states **02 November**, with a separate deadline of **20 October** for the IBAN. The document reproduces the current table. Before each operation, take the current regulatory deadline and the actual availability of the action in the Sede. Do not mix the initial filing with the change of a payment already ordered.

9. **This document does not replace the tax calculation modules.** It lists in full the requested modelos and their deadlines and channels. But the right to the régimen Beckham, the need for the 130 for a specific art93 income, the calculation of the 714/718, the regional deductions and the admissibility of deferral are determined by the corresponding rules, not by the existence of a button or a subscription. Do not disable a modelo because of uncertainty: show which input facts are needed to decide.
