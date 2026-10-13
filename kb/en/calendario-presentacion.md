*Translated from the Russian original [kb/calendario-presentacion.md](../calendario-presentacion.md) on 13.10.2026. The Russian file is the source of truth; facts were checked as of the date stated below.*

## Summary

- Checked against the available primary sources on **08.10.2026**. The income year (`ejercicio`) and the filing year are different fields: annual returns for 2025 are filed in 2026; returns for 2026 are filed mainly in 2027.
- For a small business in territorio común, the quarterly 303/130/111/115 are usually filed by 20 April, July and October. **For the fourth quarter the deadlines differ:** 111/115 by 20 January; 303/130/349 and 390 by 30 January, moved to the next business day when that day is not a business day; 180/190 by 31 January, moved in the same way.
- In 2026 the domiciliación deadline for 303/130 for Q4 2025 is **27 January**, not automatically 25 January. For ordinary quarters it is 15 April/July/October. The calendar cannot be implemented with the formula "filing date minus five days".
- Renta 2025 via the Internet: **08.04–30.06.2026**; domiciliación until **25.06.2026**. Modelo 151 is a separate service, not the ordinary Renta WEB. **Cl@ve is accepted**; a certificate is not the only way to log in.
- For 303 for Q4 2026, AEAT already explicitly publishes **01.02.2027**. The other 2027 dates below that no separate AEAT calendar confirms are marked as calculated. The exact start of Renta 2026 in 2027 is **UNVERIFIED**.
- 303/130 can be generated as a text file according to the diseño de registro and imported into the Sede form. This is **not CSV, not PDF and not arbitrary XML**, despite the enclosing `<T...>` tags.
- Current files checked: **DR303e26v101.xlsx** for 2026; **DR303e25.xlsx** for 2025; **DR130e15v12.xls** for 2019 and later years. The year number in the name of the 130 specification does not mean that the specification is outdated.
- Pre303 is a confirmed service that pre-fills the form. A public documented API of Pre303 itself that lets third-party software calculate or file the return without the form is **not confirmed**. The SII or VERI*FACTU API does not replace filing 303.
- An NIE is enough to obtain a Spanish certificado FNMT and to register in Cl@ve, with proper identity verification. A Russian passport and a TIE **are not a DNIe**. An SL files with the certificado electrónico of its representative or through an authorised representative. A personal Cl@ve does not replace the SL certificate.
- The states "file created", "form validated", "NRC received", "return accepted" and "tax paid" are independent. Completion of filing is confirmed by **justificante + CSV + AEAT date/time**. A domiciliación requires a later check of the debit.
- Voluntary late filing with an amount payable: art. 27 LGT, **1% + 1 percentage point for each full month**; after 12 months, **15% plus interest**. A zero or informative return does not become free of penalties: separate penalties apply.
- Autoliquidación rectificativa was not introduced at the same time for all models: for 303 from 09/3T 2024; for 100 from ejercicio 2024; for 200 for periods starting 01.01.2024. 130 keeps the complementaria. A first missed return is not a complementaria.

## Rules

1. **Deadlines and moves depend on the specific model and the AEAT calendar.** If the last day is not a business day, the deadline ends on the next business day. For electronic filing, the reference is the official Sede calendar, not an arbitrary list of holidays at the place of residence. For domiciliación, AEAT requires a gap of at least **three business days or five calendar days** between the end of domiciliación and the general deadline. When AEAT counts business days, it takes into account Saturdays, Sundays, national holidays and the regional/local holidays of the municipality of the AEAT Departamento de Informática. This applies to the 2025–2026 filings covered here. The 2026 table takes priority over the heuristic. Source: [official deadlines and domiciliación 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html).

2. **A quarterly 349 does not follow from a quarterly 303.** The base frequency of 349 is monthly. A quarter is allowed if the total of the relevant intracomunitarias entregas de bienes/prestaciones de servicios, excluding IVA, did not exceed 50 000 € in the current quarter or in any of the four previous quarters. If the threshold is exceeded within a quarter, a special filing arises for the months that have already ended. Do not use an annual 349. Without operations that must be included, a "zero 349" is not needed. For July there is an extended window until 20 September; for December/Q4 the window runs until 30 January. Applies in 2025–2026. Sources: [AEAT, operaciones intracomunitarias](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/5-impuesto-sobre-valor-anadido/5_9-operaciones-intracomunitarias.html), [349 deadlines, manual IVA 2026](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2026/capitulo-09-declaraciones-informativas-iva-379/declaracion-recapitulativa-operac-intracomunitarias-modelo-349/plazo-presentacion.html).

3. **Modelo 036 is an event-driven obligation, not a quarterly one.** Alta: before the start of the activity or of the relevant operations. Ordinary modificación: within one month from the day after the change. Baja: usually within one month after cessation. For the domicilio fiscal of an autónomo, modificación 036, casilla 122 applies. Do not postpone a change of address until Renta. ROI must be requested before the relevant intracomunitarias operations. Special windows apply to IVA/IS options. For example, the art. 40.3 LIS option for a calendar period is made in February; in 2026 the deadline is 02.03.2026. Modelo 037 was abolished from **03.02.2025**. Sources: [036 in the 2026 calendar](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/modelo-036.html), [modificación deadline](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/plazos-presentacion/declaracion-modificacion-modelo-036.html), [casilla 122](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/modificacion-modelo-036/casilla-122-domicilio-fiscal-modelo-036.html), [02.03.2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html).

4. **Authentication depends on the filer, not only on the model.** Individuals can use Cl@ve for 036, 100, 111, 115, 130, 149, 151, 180, 190, 303, 347, 349, 390, 714, 720, 721. A certificate/DNIe has a wider scope. An SL must file electronically with a certificado. The powers of the administrator/representative must be recognised. The número de referencia is valid only for permitted IRPF procedures; it is not universal access. Applies in 2025–2026; the list was checked against the 2026 calendar. Source: [AEAT, identificación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/recuerde/identificacion-presentar-autoliquidaciones.html).

5. **A foreigner without a DNIe has a fully working FNMT route with an NIE.** Request a certificado de persona física → código de solicitud → in-person identity verification at an oficina de acreditación with valid originals of the TIE/official NIE document and the passport → download the certificate following the FNMT instructions. A cita previa is usually needed. Export a protected backup copy of the private key. For Cl@ve, these routes are available: registration with a certificate, in-person registration, or a carta de invitación sent to the domicilio fiscal with a CSV. With an NIE, the número de soporte of the document is entered. The carta gives nivel básico; not all high-level procedures are available with it. Do not assume that a specific type of vídeoidentificación works with a Russian passport. This is a current procedure, not an annual tax rate. Sources: [FNMT: documents](https://www.sede.fnmt.gob.es/registro-inicio/preguntas-frecuentes/-/asset_publisher/DKnDigPrgk4U/content/4-3-2-3-acreditacion-de-la-identidad-de-una-persona-fisica), [Cl@ve with carta](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/registrarse-clave-pin/registro-internet-csv.html), [número de soporte](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/incidencias-tecnicas-clave-pin/introduzca-soporte-valido.html).

6. **Renta WEB and 151 are different workflows.** Ordinary IRPF: Renta WEB / modelo 100. Beckham: a separate form 151, with Cl@ve or certificado/DNIe, import/export of the BOE file `.151`, validation and `Firmar y enviar`. Do not automatically replace 151 with a return 100. Do not declare 151 to be "manual only, without a file". For 151, a DR is published for ejercicio 2023 and later years; it applies in the years covered here. Sources: [technical instructions 151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html), [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), [instructions 151](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html).

7. **Importing a return is not filing.** After the import, choose the payment method, fix the validator errors, sign and obtain the justificante. `Guardar`, `Vista previa`, `Exportar` and the NRC alone do not confirm filing. The NRC has 22 characters. It confirms a payment, not the filing of the return. Its data must match the NIF/modelo/ejercicio/periodo/importe. With `Reconocimiento de deuda`, the request for aplazamiento/compensación is made separately if it is not completed directly within the workflow. Applies to the current 2025–2026 forms. Sources: [130](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-130.html), [151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html).

8. **Pre303 does not remove the need to check the source data.** The service provides the Ventana Censal IVA, Identificación, and the result/balances of cuotas a compensar. An extended calculation is possible from SII/Libros Agregados or from an import of the libros registro for eligible non-SII filers. A representative needs the relevant powers for all functions, in particular PRE303. As of 08.10.2026, the checked public documentation contains no Pre303 API contract for independent automatic filing. The confirmed route is the form + the official file/books. Sources: [Pre303](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303.html), [functions](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/que-servicios-funcionalidades-tiene-nuevo-pre303.html), [access](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/acceder-pre303.html), [technical instructions 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303.html).

9. **RETA is handled separately from AEAT, in Import@ss.** Through `Base de cotización y rendimientos`, the filer reports or changes the forecast of the average monthly rendimiento neto and the base within the permitted tramo. Up to six effective dates for changes per year. A change does not immediately and retroactively change all previous months. `Consulta de recibos de trabajo autónomo` shows the issued cuotas. Check each issued cuota against the bank debit. The system rules apply from 2023 and are applicable in 2025–2026. Sources: [change of base](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos), [guía autónomo](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo+Autonomo/guia), [recibos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta%2Bde%2Bpagos%2By%2Bdeudas/ConsultaRecibos).

10. **Voluntary late filing before a requerimiento and non-payment of a debt already declared are different grounds.** Art. 27 LGT applies to a voluntarily filed late return for a correctly stated period. Do not mix missed turnover into the current quarter. The recargo is reduced by 25% only if the conditions for paying the debt and the recargo set out in art. 27.5 are met. Do not promise the reduction for any acknowledgement of debt. In case of non-payment, recargos del período ejecutivo under art. 28 may also apply. The current art. 27 scale applies from **11.07.2021**, and therefore in 2025–2026. Source: [LGT, arts. 27–28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27).

11. **No amount payable does not cancel the filing obligation or the penalties.** Art. 198 LGT: ordinary late filing without economic harm, 200 €; censal, 400 €; mandatory informative data, 20 € per dato/conjunto de datos per person, minimum 300 €, maximum 20 000 €. Voluntary late filing without a requerimiento halves these amounts. This is a potential penalty in a separate proceeding. It is not an amount that is automatically added to a tax casilla. If Hacienda suffers harm, art. 191 may apply after a requerimiento: 50–150% of the unpaid tax, depending on the type of offence. Applies in 2025–2026. Source: [LGT, arts. 191, 198, 199](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198).

12. **The correction route depends on the model and the tax period.** 303 from 09/3T 2024: autoliquidación rectificativa is the general route, both when the result increases and when it decreases. There are special exceptions, in particular certain disputes about IVA repercutido and breach of a higher-ranking rule. 100 from ejercicio 2024: rectificativa in the cases provided for; special complementarias remain for certain grounds of regularisation. 200 for periods starting 01.01.2024: rectificativa. 130, the current form 151 and ordinary withholdings keep their own complementaria/solicitud de rectificación mechanisms. Do not automatically extend the change for 100 to them. Sources: [303, corrections](https://sede.agenciatributaria.gob.es/Sede/iva/presentar-declaracion-iva-modelo-303/errores-declaracion.html), [FAQ 303](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/autoliquidacion-rectificativa.html), [100 ejercicio 2024](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2024/c18-cuota-liquida-resultante-autoliquidacion/regularizacion-situaciones-tributarias/general.html), [200](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2024/capitulo-02-identificac-autoliq-compl-incn/autoliquidacion-rectificativa.html), [130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

## Figures

### Constant values for the calendar and risks

| Parameter | 2025 | 2026 | Note |
|---|---:|---:|---|
| Limit for a quarterly 349 | 50 000 € | 50 000 € | Current quarter and each of the four previous quarters; excluding IVA, for the relevant outgoing operations |
| 347 threshold for ordinary operations per counterparty | >3 005,06 € | >3 005,06 € | Annual amount including IVA; the exceptions matter more than the threshold itself |
| Formal 714 obligation regardless of cuota | Assets/rights >2 000 000 € | Same | In addition to the obligation when there is a cuota a ingresar; count the assets of the relevant tax scope, before debts and including exempt assets |
| Initial 720 threshold | >50 000 € per relevant block | Same | Not a single threshold for all foreign assets; there are accounting and personal exceptions |
| Repeat 720 | Increase of the relevant block >20 000 € compared with the last mandatory filing | Same | Consider loss of ownership/powers separately, not only an increase |
| Initial 721 threshold | Total >50 000 € | Same | Foreign custodial cryptocurrency; self-custody is not included |
| Repeat 721 | Increase >20 000 € and certain cases of loss of status | Same | Check the rules of art. 42 quater; do not copy all 720 rules literally |
| Art. 27, before 12 months expire | 1% + 1 p.p./full month | Same | Without requerimiento; not days divided by 30 |
| Art. 27, after 12 months | 15% + intereses | Same | Interest only from the day after these 12 months end |
| Art. 27.5 recargo reduction | 25% of the recargo | 25% | Conditional; this reduction does not reduce the debt or the interest |
| Interés de demora tributario | 4,0625% per year | 4,0625% per the checked table/extension | Do not freeze the rate for future years |
| Art. 28: ejecutivo / apremio reducido / ordinario | 5% / 10% / 20% | Same | Mutually exclusive; 20% is compatible with intereses |
| Art. 198: ordinary return without harm | 200 € / 100 € if voluntary | Same | Before other applicable penalty reductions |
| Art. 198: declaración censal | 400 € / 200 € if voluntary | Same | For the autónomo 036; do not confuse with 100 € under art.198.5 for an individual without an activity |
| Art. 198: informative return | 20 €/dato, min 300 €, max 20 000 € | Same | If voluntary: 10 €/dato, min 150 €, max 10 000 € |
| Web form limit for 349/190/347 | 40 000 records | 40 000 records in the current instructions | Above the limit: fichero/TGVI; a small file is also allowed |

Sources for the table: [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), [interest, Banco de España](https://clientebancario.bde.es/pcb/es/menu-horizontal/productosservici/relacionados/tiposinteres/guia-textual/tiposinteresrefe/tabla_tipos_interes_demora.html), [AEAT, interest 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html), [714](https://sede.agenciatributaria.gob.es/Sede/no-residentes/impuesto-sobre-patrimonio/declaracion-impuesto-patrimonio-no-residentes.html), [347 exceptions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes.html), [721 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html).

### Filing in 2026 and closing ejercicio 2026 in early 2027

All dates are inclusive. `—` means that domiciliación does not apply to an informative return. It does not mean that there is no obligation to file.

| Model / period | Filing window | Last day for domiciliación | Status |
|---|---|---|---|
| 111, 115: 4T 2025 | 01–20.01.2026 | 15.01.2026 | AEAT |
| 303, 130: 4T 2025 | 01–30.01.2026 | **27.01.2026** | AEAT |
| 349: 4T/12M 2025; 390: year 2025 | 01–30.01.2026 | — | AEAT |
| 190, 180: year 2025 | 01.01–02.02.2026 | — | AEAT |
| 347: year 2025 | 01.02–02.03.2026 | — | AEAT |
| 720, 721: year 2025 | 01.01–31.03.2026 | — | AEAT |
| 303, 130, 111, 115: 1T 2026 | 01–20.04.2026 | 15.04.2026 | AEAT |
| 349: 1T 2026 | 01–20.04.2026 | — | AEAT |
| 202: 1P 2026 | 01–20.04.2026 | 15.04.2026 | AEAT; not "Q1 profit" by default |
| 100, 151, 714: year 2025 | Internet campaign 08.04–30.06.2026 | 25.06.2026 | The common end date and domiciliación are confirmed for all three; 151 is a separate service |
| 303, 130, 111, 115: 2T 2026 | 01–20.07.2026 | 15.07.2026 | AEAT |
| 349: 2T 2026 | 01–20.07.2026 | — | AEAT |
| 200: calendar year 2025 | 01–27.07.2026 | **22.07.2026** | AEAT; 25 July is a Saturday |
| 718: year 2025, if ITSGF arises | 01–31.07.2026 | 28.07.2026 | AEAT; not a replacement for 714 |
| 303, 130, 111, 115: 3T 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 349: 3T 2026 | 01–20.10.2026 | — | AEAT |
| 202: 2P 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 102: second payment of ordinary Renta 2025 with a permitted fraccionamiento | Until 05.11.2026 | Separate deadlines for managing domiciliación, see below | AEAT; do not automatically apply this regime to 151 |
| 202: 3P 2026 | 01–21.12.2026 | **16.12.2026** | AEAT; 20 December is a Sunday |
| 111, 115: 4T 2026 | 01–20.01.2027 | 15.01.2027 | Calculated with the current rule; full 2027 calendar UNVERIFIED |
| 303: 4T 2026 | 01.01–**01.02.2027** | Expected 27.01.2027 | AEAT has already published the filing end date; domiciliación 2027 is calculated |
| 130: 4T 2026; 349: 4T/12M 2026; 390: year 2026 | 01.01–01.02.2027 | For 130 expected 27.01.2027; others — | Calculated: 30 January is a Saturday |
| 190, 180: year 2026 | 01.01–01.02.2027 | — | Calculated: 31 January is a Sunday |
| 347: year 2026 | 01.02–01.03.2027 | — | Calculated: 28 February is a Sunday |
| 720, 721: year 2026 | 01.01–31.03.2027 | — | Current annual rule; the 2027 calendar is not yet confirmed |
| 100, 151, 714: year 2026 | Expected April–30.06.2027 | Expected 25.06.2027 | Start/final campaign calendar **UNVERIFIED** |
| 200: calendar year 2026 | Expected 01–26.07.2027 | Expected 21.07.2027 | Calculated: 25 July is a Sunday; check the approved calendar and holidays |

Sources: [annual calendar 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual.html), [domiciliación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [30 January](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/enero/hasta-30-enero.html), [2 February](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/febrero/hasta-2-febrero.html), [2 March](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html), [31 March](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-31-marzo.html), [303 until 1 February 2027](https://sede.agenciatributaria.gob.es/Sede/en_gb/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/calendario-anual/febrero-2027/hasta-1-febrero-2027.html).

For campaña Renta 2025: AEAT telephone assistance **06.05–30.06.2026**, appointments **29.04–29.06**; in-person assistance **01.06–30.06**, appointments **29.05–29.06**. This does not guarantee service for a business or Beckham case: admission criteria for assistance apply. [Campaign dates](https://sede.agenciatributaria.gob.es/Sede/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/fechas-campana-renta-patrimonio.html).

Managing the second 102 payment: at the time of reading, the **live AEAT table** gives **02.11.2026** as the deadline to revocar/rehabilitar/domiciliar for filers with domiciliación of the first payment, and **20.10.2026** as the deadline to change the IBAN. A search snippet of the same page showed an old date of 30 September. Use the live page/current instructions. Do not mix these deadlines with the first Renta domiciliación.

### Monthly regimes: all deadlines in calendar year 2026

A small volume does not cancel the monthly 303 under REDEME/SII on the relevant ground. Monthly 111/115 arise, in particular, for grandes empresas. `M` is the month of the operations. Dates below without a year refer to 2026.

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
| 08M 2026 | 30.09 / 25.09 | 21.09 / 16.09 | **21.09**, separate from July |
| 09M 2026 | 30.10 / 27.10 | 20.10 / 15.10 | 20.10 |
| 10M 2026 | 30.11 / 25.11 | 20.11 / 17.11 | 20.11 |
| 11M 2026 | 30.12 / **24.12** | 21.12 / 16.12 | 21.12 |
| 12M 2026 | Expected 01.02.2027 / 27.01.2027 | Expected 20.01.2027 / 15.01.2027 | Expected 01.02.2027 |

Source: [official 2026 table](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [349 in September](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/septiembre/hasta-21-septiembre.html). Temporary extensions due to extraordinary circumstances take priority over the base calendar.

### Import@ss: windows for changing the base in 2025 and 2026

| Application date | Start date of the new base |
|---|---|
| 01.01–28.02 | 01.03 of the same year |
| 01.03–30.04 | 01.05 |
| 01.05–30.06 | 01.07 |
| 01.07–31.08 | 01.09 |
| 01.09–31.10 | 01.11 |
| 01.11–31.12 | 01.01 of the following year |

Neither of the two years covered is a leap year. These are RETA change windows. They are not filing deadlines for AEAT modelos. They are not a promise that a window moves to a business day under the tax domiciliación rules. Source: [TGSS, Base de cotización y rendimientos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos).

## Formulas for the engine

### 1. Selecting the obligation and the calendar

Input: the profile and its validity intervals; the taxpayer NIF; ejercicio/periodo; censal obligations; type of operation/withholding; REDEME/SII; 349 history; the end date of the SL financial year; history of previously accepted returns; an AEAT requerimiento; the payment method. Output: a list of obligations with evidence of applicability, the filing deadline, a separate domiciliación deadline and the source status.

```text
for each model, tax_period:
    applicable = obligation_rule(model, profile_at_period, activity, transactions, census)
    # The absence of a payment does not by itself mean applicable = false.
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

Do not move 111/115 to 30 January just because 303 moves there. For 202, create `1P`, `2P`, `3P` in April/October/December, not `1T–4T`. For 200, the statutory deadline is 25 calendar days after six months from the end of the tax period, with the move provided for by law. The July date fits only a calendar financial year. Reminders may be sent earlier according to an internal setting. Do not call the internal date a legal deadline.

When the taxpayer moves, store the date of the actual change of domicilio and the date of the 036 notification separately. For general IRPF, the region is determined by the residencia habitual rules for the year. The tax is not split by months between two regions. For Beckham there is no regional scale of ordinary IRPF, but the address/Comunidad in 151 is still updated.

### 2. Formats: register by model and year

**Links to the specifications are a mandatory part of the generator contract.** Select them by `ejercicio`, not by the calendar date of the export.

| Model | Official specification | Filing method and type of structure |
|---|---|---|
| 303 for 2025 | [DR303e25.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/DR303e25.xlsx), updated 04.12.2025 | Pre303/web form with Importar; paged fixed-width with `<T...>` |
| 303 for 2026 | [DR303e26v101.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_26/DR303e26v101.xlsx), updated 28.01.2026 | Same; inside the workbook the version is shown as `10.01`; do not derive the schema number from the file name |
| 130 for 2025/2026 | [DR130e15v12.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/DR130e15v12.xls), March 2019, version 1.2 | Form, Importar/Exportar `.130`; one page and a wrapper |
| 111 | [dr111e16v18.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/dr111e16v18.xls), May 2021, for 2019+ | [Electronic form with Importar](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-111/presentacion-electronica-modelo-111.html); fixed-width with a wrapper |
| 349 | [DR_Anexo_349.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_20/DR_Anexo_349.pdf), Orden HAC/174/2020, 2020+ | [Form ≤40 000 records or presentación mediante fichero](https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/identificacion-realizar-operaciones-otros-empresarios-ue/modelo-349.html); tipo 1 declarante + tipo 2 operaciones/rectificaciones |
| 390 for 2025 | [dr390e2025.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/dr390e2025.xlsx), updated 05.12.2025 | [Form](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390.html) and [separate presentación con fichero](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390/modelo-390-presentacion-mediante-fichero.html); paged fixed-width structure |
| 190 for 2025 | [DISENOS_LOGICOS_190_2025.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos_25/DISENOS_LOGICOS_190_2025.pdf), Orden HAC/1431/2025 | Form ≤40 000 records or [TGVI online](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/declaraciones-informativas-ayuda-tecnica/modelos-190-198/modelo-190-fichero.html); tipo 1 + tipo 2 perceptores |
| 347 for 2025+ | [347.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos/347.pdf), Orden HAC/1431/2025 | [Form ≤40 000 records or TGVI](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/forma-presentacion.html); tipo 1 + tipo 2 declarados/inmuebles |
| 151 for 2025/2026 | [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), 2023+ | Separate web form, Importar/Exportar; export file name `NIF_Ejercicio_0A.151` |
| 100 for 2025 | [Renta2025.xsd](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/Renta2025.xsd), [diccionario](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/diccionarioXSD_2025.properties) | Renta WEB; the published XML/XSD is a different format, not the 303/130 container |

For 390 ejercicio 2026, no separate confirmed DR was found on the check date. Do not present the 2025 file with the year replaced as guaranteed to be accepted. For 190, which is updated every year, also re-check the publication for 2026 before the campaign. Catalogues: [100–199](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-100-199.html), [300–399](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-300-399.html), [303 archive](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/ejercicios-anteriores-modelos-300-399.html).

For the informative models 349/190/347, the fixed-length records are defined by their PDFs, not by the `<T303...>` construction. One registro tipo 1 identifies the filer, the period and the control totals. Registros tipo 2 contain the counterparties/recipients and special records. They cannot be replaced by an accounting CSV. Take the mapping of claves/subclaves and the counters from the **specific DR**, not from the column names of the on-screen form. For 190, AEAT warns separately that the first filing method chosen (form or fichero) determines the allowed route for later filings. Store the channel of the original return. TGVI may allow filing of the correct records and later correction of the rest. Do not treat the whole original set as filed until the accepted/rejected records have been reconciled.

### 3. Common serialisation of 303/130

Below are the checked **1-based positions**, lengths and signs. For a program array, the index equals `position - 1`. Length is measured in bytes of the chosen single-byte encoding, not in UTF-8 code points.

```text
format_amount(value_eur, width, signed):
    # The input has already been calculated by the tax module to the euro cent.
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
# No CSV separators, UTF-8 BOM, XML indentation or line breaks inside a record.
```

Source for the encoding, alignment and `N` for negative values: [AEAT, Diseños de registro — breve manual, pp. 4–6, 10–12](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/Ayudas/Disenyos_registro_Manual_uso.pdf). This is positional text, not an XML document for an XML serializer. Spaces are significant; `trim` is not allowed. Money calculations use Decimal/integer cents. Final rounding to 0,01 € follows the rules of the specific casilla. If the specific instructions do not set another rule, the technical convention is decimal ROUND_HALF_UP, checked against the AEAT form. Do not round every intermediate expression. Do not use binary float.

**The wrapper has the same positions in both checked DRs:**

| Absolute position | Length | Content |
|---:|---:|---|
| 1 | 2 | `<T` |
| 3 | 3 | `303` or `130` |
| 6 | 1 | `0` |
| 7 | 4 | Ejercicio, for example `2026` |
| 11 | 2 | Periodo, for example `3T`; for the monthly 303, `01`…`12` |
| 13 | 5 | `0000>` |
| 18 | 5 | `<AUX>` |
| 23 | 70 | Spaces, reservado AEAT |
| 93 | 4 | Developer program version |
| 97 | 4 | Spaces |
| 101 | 9 | Developer NIF per the DR instructions |
| 110 | 213 | Spaces |
| 323 | 6 | `</AUX>` |
| 329 | Variable | Model pages |
| After the last page | 18 | `</T3030EEEEPP0000>` or `</T1300EEEEPP0000>` |

Example of the start for 303 for 3T 2026: `<T303020263T0000><AUX>`; for 130: `<T130020263T0000><AUX>`. `EEEE`/`PP` here are placeholders for the explanation, not literal values in the file. In DR130 the description of the closing tag contains the typo `T1230`, but the **Contenido** column clearly gives `</T1300AAAAPP0000>`: use 130.

### 4. Modelo 130: a single, fully defined page

After the wrapper comes the **600-byte** page `DR 13001`. The positions given are **local to the page**, so its position 1 is at position 329 of the whole file.

| Position | Length | Field |
|---:|---:|---|
| 1 | 11 | `<T13001000>` |
| 12 | 1 | Space, indicador de página complementaria; this is not the complementaria return flag |
| 13 | 1 | Tipo: `I` ingreso, `U` domiciliación, `G` CCT, `N` negativa, `B` a deducir |
| 14 | 9 | NIF |
| 23 | 60 | Apellidos |
| 83 | 20 | Nombre |
| 103 | 4 | Ejercicio |
| 107 | 2 | `1T`…`4T` |
| 109 + 17×(k−1), k=1…19 | 17 per field | Casillas `[01]`…`[19]` in sequence |
| 432 | 1 | `X` for a declaración complementaria, otherwise a space |
| 433 | 13 | Número justificante of the previous return, if complementaria |
| 446 | 34 | IBAN for domiciliación, left-aligned, followed by spaces |
| 480 | 96 | Reservado AEAT, spaces |
| 576 | 13 | Sello electrónico reservado, spaces |
| 589 | 12 | `</T13001000>` |

Casillas with the `N` sign: **03, 07, 11, 14, 17, 19**. The other money fields are `Num`, without negative values. A 17-character field has two implied decimal digits, without a comma or point. Full length of a simple return: **328 + 600 + 18 = 946 bytes**.

The tax module passes the calculated casilla values; the serializer does not recalculate them. For a complementaria, the whole period is recalculated. `[18]` is the sum of the **a ingresar** results of the previous 130 returns for the same ejercicio/periodo, not the tax for all previous quarters. `[19] = [17] − [18]`. A missed original 130 has `[18]=0`, no `X` and no fictitious previous justificante. Do not turn a zero/negative result into `I` just to make a payment. Sources: DR130 above and the [official 130 instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

### 5. Modelo 303 for 2026: pages and casillas

The workbook contains `DP30300`, `DP30301`, `DP30302`, `DP30303`, `DP30304`, `DP30305`, `DP303DID`. For an ordinary activity under régimen general, the data of page 01, result page 03 and the DID payment section are needed. Page 02 is for régimen simplificado. Page 04 is for annual information of filers exempt from 390. Page 05 is for the relevant prorrata/sectores diferenciados information. **Empty pages 04/05 are not included**, according to the notes in the DR. For an applicable page 02 or repeated pages, follow its own repetition conditions. Do not create page 02 for a consultant without régimen simplificado.

| Page | Start / end | Full length | Key points |
|---|---|---:|---|
| DP30301 | `<T30301000>` / `</T30301000>` | 1 581 | NIF, period, flags and régimen general |
| DP30303 | `<T30303000>` / `</T30303000>` | 1 017 | Additional information, result, rectificativa |
| DP30304 | `<T30304000>` / `</T30304000>` | 998 | Last period for filers exempt from 390; do not add without data |
| DP30305 | `<T30305000>` / `</T30305000>` | 1 528 | Prorratas/sectores; do not add without data |
| DP303DID | `<T303DID00>` / `</T303DID00>` | 823 | IBAN/BIC/foreign bank |

For the combination 01 + 03 + DID, the length is **3 767 bytes** including the wrapper. This is a structural check of that combination. It does not prove that arbitrary zero values will pass AEAT business validation.

**DP30301: positions are local to the page.** Start: position 12 is a space, 13 is tipo declaración; 14/9 NIF; 23/80 nombre o razón social; 103/4 ejercicio; 107/2 periodo. Take the flags at 109–130 from the DR; do not fill them all with zeroes. For example, for an ordinary filer with only régimen general, position 111 = `3`; SII voluntario is 127; exoneración 390 is 128 (`0` outside the last period, `1`/`2` in the last period); volumen anual is 129, per the DR condition. Position 130 is a new special combustible field; for quarters and for 01 it has `0`. This field shifts the offsets compared with some older schemas.

| Casilla | DP30301 position/length | Type |
|---|---|---|
| 01 / 02 / 03 | 209/17; 226/5; 231/17 | Num; rate `00400` |
| 04 / 05 / 06 | 287/17; 304/5; 309/17 | Num; rate `01000` |
| 07 / 08 / 09 | 326/17; 343/5; 348/17 | Num; rate `02100` |
| 10 / 11 | 365/17; 382/17 | Num; adquisiciones intracomunitarias |
| 12 / 13 | 399/17; 416/17 | Num; other inversión del sujeto pasivo |
| 14 / 15 | 433/17; 450/17 | N; modificaciones |
| 27 | 696/17 | N; total cuota devengada |
| 28 / 29 | 713/17; 730/17 | Num; interiores corrientes |
| 30 / 31 | 747/17; 764/17 | Num; interiores bienes de inversión |
| 32 / 33 | 781/17; 798/17 | Num; importaciones corrientes |
| 34 / 35 | 815/17; 832/17 | Num; importaciones inversión |
| 36 / 37 | 849/17; 866/17 | Num; intracomunitarias corrientes |
| 38 / 39 | 883/17; 900/17 | Num; intracomunitarias inversión |
| 40 / 41 | 917/17; 934/17 | N; rectificación deducciones |
| 42 / 43 / 44 | 951/17; 968/17; 985/17 | N |
| 45 / 46 | 1002/17; 1019/17 | N |
| Reservado + sello | 1036/521; 1557/13 | Spaces |
| End | 1570/12 | `</T30301000>` |

The remaining fields, including zero-rate/recargo equivalencia, are still physically present. Fill them **with constants and zeroes per the DR**; do not cut them out. For the IVA total, use all the prescribed terms, not only the popular casillas:

```text
303[27] = [152]+[167]+[03]+[155]+[06]+[09]+[11]+[13]+[15]
          +[158]+[170]+[18]+[21]+[24]+[26]
303[45] = [29]+[31]+[33]+[35]+[37]+[39]+[41]+[42]+[43]+[44]
303[46] = [27] - [45]
```

**DP30303: key result fields.**

| Casilla/field | Position/length | Type/meaning |
|---|---|---|
| 59 | 12/17 | N; intracomunitarias entregas y servicios |
| 60 | 29/17 | N; exportaciones y asimiladas; not automatically any non-EU services |
| 64 | 199/17 | N; `[46]+[58]+[76]` |
| 65 | 216/5 | Num; % Estado, 100% = `10000` |
| 66 | 221/17 | N; atribuible al Estado |
| 77 | 238/17 | Num; IVA importación pendiente |
| 110 / 78 / 87 | 255/17; 272/17; 289/17 | Num; balance, part applied, balance of old periods |
| 68 | 306/17 | N; regularización Estado/forales |
| 108 | 323/17 | N; special ajuste por discrepancia, not a universal "manual adjustment" |
| 69 | 340/17 | N |
| 70 | 357/17 | Num; previous a ingresar results for the same period |
| 109 | 374/17 | Num; devoluciones acordadas by AEAT for the same period |
| 112 | 391/17 | Num; special pagos a cuenta modelo 319 for combustible, usually 0 |
| 71 | 408/17 | N; final resultado |
| Sin actividad | 425/1 | `X` or a space; zero IVA does not automatically mean no activity |
| Rectificativa | 426/1 | `X` or a space |
| Previous justificante | 427/13 | Mandatory under the rectificativa conditions |
| Change/cancel the previous domiciliación | 440/1 | `X` or a space |
| 111 — importe rectificación | 441/17 | Num; per the rectificativa rules, not the total amount of the overpayment |
| Motivo rectificaciones / discrepancia | 458/1; 459/1 | `X` or a space |
| Reservado / closing tag | 460/546; 1006/12 | Spaces / `</T30303000>` |

```text
303[87] = [110] - [78]
303[69] = [66] + [77] - [78] + [68] + [108]
303[71] = [69] - [70] + [109] - [112]
# Original ordinary declaración: [70]=[109]=0; [108]=0 without a special ground.
# The IVA module decides the use of [78] and the refund/carry-forward of a negative result.
# Do not treat [87] as the full new balance: it is the balance of the old periods only.
```

In DID: SWIFT-BIC position 12/11, IBAN 23/34, banco 57/70, dirección 127/35, ciudad 162/30, código país 192/2, SEPA mark 194/1 (`0` empty, `1` España, `2` UE-SEPA, `3` others), reservado 195/617, closing tag 812/12. A Spanish IBAN is the first 24 characters starting with `ES`; the rest of the field is spaces. For a rectificativa with casilla 111>0, bank details are also required in some non-devolución variants, except the case provided for in the DR of a change of the original domiciliación.

Tipo 303: `I` ingreso, `U` domiciliación, `C` compensación, `D` devolución, `N` sin actividad/resultado cero, `G`/`V` CCT, `X` devolución transferencia extranjero. For a rectificativa with `[71]<0` and `[111]>0`, the DR requires the type to be determined by the part of `[71]` that does not relate to `[111]`. Do not choose the type just by the sign of `[71]`.

These offsets apply **only to DR303e26v101**. For 2025, use the corresponding sheets of DR303e25. A real test file was not generated or imported into the Sede here. The structure given was extracted from the official workbooks, not from a sample accepted by the server.

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

For 100 in Renta WEB, use the built-in `Modificar declaración presentada`. For a rectificativa provided for by law, identify the original return and casillas **103/104** per the 2024 manual, but **check the dictionary of the specific ejercicio before generation**. For 200, use Sociedades WEB/its current DR and the rectificativa block; do not borrow the 303 numbers. The informative 190/180/347/349 need their own alta/modificación/baja operations, complementaria/sustitutiva or record rectificaciones, according to the model and the chosen channel. Do not file a second "ordinary" file and assume that the first one is cancelled.

### 7. Recargo and late-filing estimate

Input: the original legal deadline `D`, the actual filing date `F`, the unpaid amount that results from the late return `B`, whether a requerimiento existed before filing, the payment history and the applicable annual interest rates. Output: an **estimate** of the recargo/intereses and the processing route, not a new casilla of the original return.

```text
if F <= D:
    late_filing_recargo = 0
elif previous_requerimiento:
    do not apply voluntary_art27_estimate
    route = review assessment/sanction procedure
elif B <= 0:
    recargo_art27 = 0
    route = evaluate formal_penalty_art198  # not "no penalty"
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

`legally_completed_calendar_months` means calendar months, **not** `floor(days/30)`. The start/end of the monthly interval, months without the corresponding day number and the exact 12-month boundary need checking against an official AEAT calculation/notification. The public wording found repeats the law without a separate example at the boundary itself. Until such a check, the engine must show a range/warning on a disputed boundary date. It must not invent a guaranteed rate. This does not affect unconditional cases: a debt of 1 000 € filed ten days late → 10 € recargo; with an applicable reduction → 7,50 €. After more than 12 months → 150 € plus interest from the stated date, not interest for the whole first year.

AEAT usually assesses the recargo separately. **Do not add it to the resultado in casilla 19 Modelo130 or casilla71 Modelo303**. If the tax return was accepted on time but the bank did not debit the money, check art.28 and the payment circumstances. Do not file a duplicate and do not charge art.27. Withholdings and some other debts do not allow an ordinary aplazamiento. A button for acknowledging a debt does not mean an automatic right to a deferral.

## Deadlines and models

### Who files what

Here "Beckham" means a valid accepted opción under art.93 with the conditions met, not just a business visa. If a model is missing from the list that the gestoría keeps, this does not prove an exemption.

| Modelo | Who/when | When it does not arise / key limitation | Deadline |
|---|---|---|---|
| 303 | Autónomo with either of the two IRPF profiles, and an SL with the relevant IVA activity | Beckham does not exempt from IVA. A purely exempt activity may have no periodic obligation; analyse reverse charge/other events separately. While a periodic obligation is in force, file a zero period too | Quarter/month per the tables |
| 130 | Autónomo in estimación directa; decide applicability to a permitted art.93 activity under the special rules, not by the profile label | For a professional activity under ordinary IRPF, exemption if ≥70% of income in the previous year had retención; in the first year, the applicable period. An SL does not file. Do not automatically include/exclude Beckham without the rules for the type of income | Q1–Q3 by the 20th; Q4 by 30 January, with the move to the next business day |
| 349 | Any of the profiles with relevant intra-EU supplies/acquisitions of goods or services | Non-EU operations alone do not create 349; without operations to include, do not file a zero return. A purchase of EU SaaS can also create the obligation | Month/quarter per its own test |
| 111 | A person/SL that pays salaries, professional fees and other included income with a withholding obligation | These are the withholdings of the **payer**, not the retención taken from one's own issued invoices. If included income was paid without actual withholding because of a zero rate, a negative return may be required; if there were no payments at all, it is a different case | By the 20th after the quarter; monthly for the relevant large payers |
| 115 | A payer of business rent for an urban property that is subject to withholding | Check the exceptions and the landlord certificate; not every rental of housing by a private individual creates 115 | Same as 111 |
| 202 | SL and other IS payers with a pagos fraccionados obligation | For an ordinary small SL with no amount payable, filing is usually not required; large payers have special zero-filing rules. Do not create 202 for an individual owner | April/October/December, not July |
| 390 | IVA resumen anual for filers obliged to file periodic IVA returns | Exemption for SII filers and for the specified quarterly filers with only régimen simplificado/arrendamiento urbano in territorio común; the annual data moves into the last 303. An ordinary consultant with régimen general is not exempt just because the consultant has 12 invoices | By 30 January |
| 190 | Annual included payments/withholdings linked to 111 | Not a report on retenciones withheld by one's own clients. Include the relevant zero/exempt payments according to the model rules | By 31 January |
| 180 | Annual summary of the relevant arrendamientos/retenciones 115 | Does not arise just from one's own home or from the role of the person who receives rent | By 31 January |
| 347 | Autónomo/SL with included operations with third parties above the threshold | Operations already covered by special reporting with the required matching content are excluded: for example, 349 and the relevant withholdings; SII and other personal exceptions. **A non-EU service is not the same as an exported good**; do not automatically apply the export exclusion | February of the following year |
| 100 | Ordinary IRPF autónomo; the SL administrator as an individual, according to the administrator's own obligation | From 2023, anyone in RETA at any time during the year has an obligation to file an IRPF return, but an active Beckham filer files 151 instead of the ordinary 100 | Renta campaign of the following year |
| 151 | Active special regime under art.93, including the relevant administrador/entrepreneur | Does not replace 303/retenciones/the returns of the SL itself. Not granted automatically because of an NIE/visa | Deadline of the annual IRPF campaign; in 2026 by 30 June |
| 200 | SL for its own tax period | Do not exempt because of "no activity" or zero profit; while the entity exists and has an IS obligation, an ordinary SL files | 25 days after six months from the end of the period |
| 714 | An individual with a positive Patrimonio cuota or with assets/rights above 2 million € in the applicable scope | For Beckham: obligación real for the relevant Spanish assets, not automatically worldwide property. Regional minimums/reliefs are calculated separately | Together with Renta; in 2026 by 30 June |
| 720 | Ordinary resident/SL with foreign assets, roles and thresholds, without an exception | AEAT explicitly exempts an individual under art.93. For an SL/individual with proper accounting, separate accounting exceptions are possible. The personal assets of the administrator and the assets of the SL are checked separately | 1 January–31 March |
| 721 | Foreign cryptocurrency held by a custodio, relevant roles/threshold | Self-custody is not included. Do not derive a separate Beckham exemption only from the FAQ 720 text; see "Open questions" | 1 January–31 March |
| 036 | Alta/modificación/baja, domicilio, IAE/obligations, ROI, the tax options provided for by law | Not an annual filing to confirm that nothing changed. Do not use 037 any more | Event-driven, usually one month; alta/ROI before the operations; separate windows for options |
| 102 | Second payment under a permitted 60/40 fraccionamiento of ordinary Renta | Not a universal instalment plan for all models; a late original return and 151 need separate rules | 05.11.2026 for Renta2025 |
| 718 | An individual when the Impuesto Temporal de Solidaridad de las Grandes Fortunas arises | Do not create it automatically for everyone who files 714; separate test of cuota/tax scope | July of the following year; in 2026 by 31 July |

Primary sources for the conditions: [130, instructions](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html), [202, when to file](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/4-impuesto-sobre-sociedades/4_8-pagos-fraccionados/4_8_2-modelos-pagos-fraccionados.html), [390, obliged filers](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-09-declaraciones-informativas-iva-379/declaracion-resumen-anual-modelo-390/obligados-presentar-declaracion.html), [347, exceptions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 and art.93](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes/contribuyentes-obligados-declarar.html), [721](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html). The legal calculations of each tax and the Beckham conditions must come from the relevant tax module. The calendar must not duplicate them.

Include additional obligations by event: 149 for an opción/renuncia/exclusión under Beckham; 123/193 for relevant capital payments, for example SL dividends; 216/296 for certain payments to non-residents. These are not obligations of every freelancer and do not replace the models listed. The owner of a self-hosted application who files for themselves does not need colaborador social status. Filing for another legal entity requires proper powers.

For **149** in 2025–2026: opción principal, at most **6 months** from the start of activity per the alta in Seguridad Social/an acceptable document; asociado, the later of the end of the associate's own six-month period from entry and the deadline of the principal. Renuncia: **November–December of the year before the year in which it takes effect**; for example, to renounce from 2027, 01.11–31.12.2026. Exclusión: **one month from the breach of the conditions**. Fin del desplazamiento while residencia fiscal for the year is kept: **one month from the end of the desplazamiento**. Submitting 149 and its attachments is a separate procedure. It is not an optional attachment to the annual 151. Sources: [calendar of non-periodic IRPF models 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/impuesto-sobre-renta-personas-fisicas.html), [149 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-149-irpf-comunicacion-opcion-exclusion_/instrucciones-cumplimentar-comunicacion.html).

### Practical user path

1. Obtain FNMT/Cl@ve. Check the NIE/NIF and the domicilio in AEAT. For an SL: the certificate/powers of the representative. Do not store the private key in plain form on the server. Do not give it to a marketplace without a deliberate formal representation arrangement.
2. Choose the exact model, ejercicio, periodo and filing mode. Export the file in the relevant version, or use the libros registro in the prescribed format.
3. In the Sede, choose `Presentación`/`Importar`, or the separate `Presentación mediante fichero` where it exists. The built-in web import of a file is not a separate API. 349/190/347 support TGVI; 390 supports separate filing con fichero. For individual 303/130/111 returns, the ordinary route through the form with Importar is confirmed.
4. Check the casillas against the libros, the history of compensaciones and the returns already accepted. Fix the errores and read the avisos. The data that Pre303 pre-fills automatically may not cover the whole activity.
5. If the result is positive, choose an available payment method. After the domiciliación deadline, the return can still be filed within the general deadline with an allowed payment method. Do not wait for the next quarter. A foreign bank/SEPA and `pago por transferencia` have their own conditions and crediting times.
6. `Firmar y enviar` → save the PDF/CSV/justificante and the payment confirmation separately. For transferencia/acknowledgement of debt, track the unfinished steps. For domiciliación, track the actual execution, a bank refusal and the saldo.
7. In Import@ss, separately check the RETA alta, rendimientos/base, the regularización notice and the recibos. Login is possible with an available certificado/Cl@ve/SMS, if the phone number is registered with TGSS. An NIE in AEAT does not guarantee that the phone is linked in TGSS.

## Edge cases

### Taxes, deadlines and filing

- **One EU client, 60 000 € per quarter:** 303 may stay quarterly while 349 moves to monthly. The 349 threshold is not checked only by the number of invoices. If it is exceeded in the second month, do not wait for the end of the quarter and then send an ordinary quarterly 349.
- **A client from the USA and a service from Ireland:** the sale does not create 349, but the purchase may. The absence of Spanish IVA on both invoices does not mean the same regime. Check non-EU service turnover for 347 separately from exports of goods.
- **A Spanish client withheld IRPF from our invoice:** that withholding enters our IRPF calculations, but it does not create our 111. If we ourselves paid an invoice with retención to a Spanish professional, 111/190 may arise.
- **IVA payable is zero because of foreign clients, but there was activity:** do not set `Sin actividad` automatically. If expenses were higher, choose the correct carry-forward/refund, not just a zero result. A negative 303 is still a return.
- **Closing as an autónomo in the middle of the year:** quarterly and annual obligations that have already arisen remain. In some cases, the 390 exemption is lost if the last 303 of the year is no longer required. A single baja date in RETA does not prove a simultaneous baja from all AEAT obligations.
- **Moving between autonomous communities:** this does not change the national art.93 rates, but it requires a correct domicilio/151 data and a separate determination of the region for ordinary IRPF and Patrimonio. Do not calculate half a year on one regional scale and half a year on another.
- **Beckham and family:** FAQ 720 contains an old general remark that the regime does not extend to the family. After the 2023 extension of art.93, qualifying family members may have their own opción. Check the personal status of each person. Do not exempt a wife just because of her husband's regime. Do not deny her separate opción on the basis of an outdated FAQ sentence.
- **SL and administrador:** the NIF, returns, certificado and payments of the SL are separate from the administrator's own 100/151/714. Filing 200 with the individual's data is not allowed. A personal Cl@ve does not replace the corporate certificado.
- **The last domiciliación day has passed, but the general deadline has not:** this is not extemporánea. Offer NRC/another allowed payment method. Do not charge a recargo in advance.
- **Tax paid, the connection dropped during signing:** look for an accepted return and the NRC. Do not pay again blindly. **Signing succeeded, the debit failed:** look for the debt/domiciliación status. Do not send a duplicate return.
- **Correcting an accepted 303 with an earlier domiciliación:** a new rectificativa does not guarantee automatic cancellation of the old debit. Check the special flag, the allowed change window and the AEAT confirmation. Otherwise a double debit/wrong difference is possible.
- **Deadline missed with a requerimiento:** the voluntary safe art.27 calculation may no longer apply. A requerimiento is not only a paper letter: take into account officially served electronic notifications. Do not promise "only 1%".
- **An error in a past quarter is found after the annual return is filed:** a consistent correction of the relevant quarter and the annual information is required. Increasing the current 303/130 without the correct link to the past period is not always a lawful regularización.
- **An informative return accepted part of the records:** store the identifiers and counters of the accepted set. "File sent" does not mean "all 190/349 operations accepted". Correct the rejected records in the way that the channel used allows.

## Open questions

1. **2027: not the whole calendar is published.** Direct confirmation of 01.02.2027 was found for 303 for 4T2026. Other future dates were derived from the current deadlines and calendar moves and are clearly marked. The start of Renta2026, its annual order and the final domiciliación windows must be loaded after publication. Do not present the expected 7/8 April 2027 as a set date. A regional holiday on 25/26 July 2027 may affect the specific official calendar for 200: the calculated 26 July is not final.

2. **Pre303 API is UNVERIFIED.** The Pre303 pages, gestiones, the description of functions and the 303 technical help were checked. No published WSDL/OpenAPI for Pre303 itself was found. This does not prove that no closed integration channel exists. The confirmed project route is the official import of a file/books into the form and the user's signature. Do not declare undocumented HTTP calls or the SII/VERI*FACTU API as a supported replacement for filing.

3. **The files are described, but the server import is not tested.** The byte positions for 303/130 were extracted from the official Excel files. No test returns, real payments or filings were made. Before production, the main agent must check export→import on the official simulator/form without sending: 2025/2026, ingreso/negativa/compensación, negative `N`, NIE, Ñ, IBAN, rectificativa. This is a mandatory compatibility check, not a stated result of the current research.

4. **DR versions and conditional flags change.** For 303 2026, additional combustible/modelo 319 fields were found. Using the 2025 offsets is dangerous even for a user who does not trade in fuel. DR 390 2026 is not confirmed. Exports must be blocked for an unsupported ejercicio. They must not use the "last known" format without a warning.

5. **NIF Empresa Desarrollo for a self-hosted developer.** The DR requires the NIFED and the SW version, but the checked instructions do not explain a separate developer registration for a personal one-off import. Do not insert an invented supplier NIF. Do not claim that an empty field is enough. For a Spanish developer working on their own behalf, use a valid NIF checked by the validator. Clarify unknown requirements of a specific channel with AEAT.

6. **721 for Beckham is a separate unverified qualification.** FAQ 720 explicitly exempts art93. The FAQ 721 that was read lists residents and the custodia criteria, but it contains no similar direct clarification for art93. Do not grant an automatic 721 exemption only by analogy. If the user has foreign custodial cryptocurrency above the threshold, keep the potential obligation with a manual review/a primary consulta DGT. Do not automatically file an unnecessary return "just in case".

7. **The full-month/12-month boundary in the recargo.** The sources confirm the formula, but no official example was found for the boundary day itself. An exact estimate on such dates is marked UNVERIFIED and is checked against the AEAT calculation/notification. Do not replace months with thirty-day blocks. The 2026 interest table confirms 4,0625%, but future years need a separate version, not an extrapolation.

8. **Conflicting domiciliación deadlines in AEAT sources.** For **151**, the calendario 2026 table explicitly gives **25 June**, but the [151 instructions for ejercicio 2023+](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html) twice give **26 June**. An additional check of the primary act resolves the conflict in favour of **25.06.2026**: [Orden HFP/1338/2023, art. 4.2, p. 5 of the PDF](https://www.boe.es/boe/dias/2023/12/15/pdfs/BOE-A-2023-25416.pdf) sets "hasta, con carácter general, cinco días antes" the end of filing, that is, 25 June when filing ends on 30 June. This matches the calendar. Do not use the 26 June date from the instructions to allow a new 151 domiciliación for 2025. For **102**, a search showed 30 September; the live 2026 table that was read shows **02 November**, with a separate **20 October** for the IBAN. This document reproduces the live table. Before the operation, take the current statutory deadline and the specific availability of the action in the Sede. Do not mix the original filing with a change of a previously ordered payment.

9. **This document does not replace the tax calculation modules.** It lists all the requested modelos and deadlines/channels in full. However, the right to Beckham, the need for 130 for a specific art93 income, the 714/718 calculation, regional deductions and the admissibility of an aplazamiento are determined by the relevant rules, not by the presence of a button or a subscription. Do not switch a model off because of uncertainty: show which input facts are needed for the decision.
