*Traducido del original ruso [kb/iva-facturacion.md](../iva-facturacion.md) el 13.10.2026. El archivo ruso es la fuente de verdad; los datos se comprobaron en la fecha indicada abajo.*

# IVA y facturación para autónomos / SL que prestan servicios

Situación a 2026-10-08. Fuentes primarias (BOE, AEAT Sede, DGT). Todo lo que no se ha podido confirmar con una fuente primaria está marcado como **UNVERIFIED** o `[INFERENCE]`.

## Resumen

- El IVA no depende del régimen Beckham, de la comunidad autónoma (Valencia/Asturias) ni de la forma jurídica (autónomo/SL): las reglas son las mismas. La región solo importa en Canarias/Ceuta/Melilla (allí no hay IVA, sino IGIC/IPSI).
- Servicios B2B a un cliente empresario de otro país de la UE: operación **no sujeta** en España (art. 69.Uno.1º LIVA). El IVA lo paga el cliente por inversión del sujeto pasivo (reverse charge). Es necesario el alta en el ROI (Modelo 036, casilla 582). El NIF-IVA del cliente se comprueba en VIES. Modelo 303 → casilla **59**; Modelo 349 → clave **S**.
- Servicios B2B a un cliente fuera de la UE (EE. UU., etc.): **no sujeta** (art. 69.Uno.1º), sin mención de inversión del sujeto pasivo. Desde 2023 la regla de «uso efectivo» (art. 70.Dos) no se aplica a servicios B2B como los nuestros. Modelo 303 → casilla **120**; no se incluye en el 349.
- Cliente español (B2B o B2C): IVA 21 %. Si el cliente es empresario/profesional y el prestador es una persona física con actividad *profesional*, la factura incluye la retención IRPF: 15 % (7 % los 3 primeros años) en el régimen general; **24 %** en el régimen Beckham. Con actividad *empresarial* y en una SL no hay retención.
- B2C a un cliente de la UE: IVA español 21 % (art. 69.Uno.2º). Excepción: servicios electrónicos y de telecomunicaciones. Hasta 10 000 €/año se aplica el IVA español. Por encima (o por opción) se aplica el IVA del país del cliente mediante OSS (Modelo 369, casilla 123 del 303).
- B2C a un cliente fuera de la UE: la consultoría, el desarrollo y el tratamiento de datos (lista del art. 69.Dos) y los servicios electrónicos son **no sujetos** (casilla 120). El resto tributa al 21 %.
- El derecho a deducir el IVA soportado **se mantiene** cuando se prestan servicios a clientes extranjeros (art. 94.Uno.2º LIVA). No hace falta prorrata si no hay operaciones exentas sin derecho a deducción (art. 20). Perfil típico (todos los clientes en el extranjero) ⇒ el 303 sale casi siempre «a compensar». La devolución solo se obtiene en el 4T (casilla 73) o mediante REDEME/SII.
- Servicios recibidos de proveedores de la UE (SaaS, etc.): autorrepercusión, casillas 10/11 y 36/37, 349 clave **I**. De proveedores fuera de la UE: casillas 12/13 y 28/29; no se incluyen en el 349.
- Factura (RD 1619/2012 art. 6): número/serie, fecha, partes con NIF y domicilio, descripción, base, tipo, cuota, fecha de la operación si es distinta, menciones obligatorias para exentas/no sujetas/ISP. La moneda puede ser cualquiera, pero la **cuota de IVA debe expresarse en euros** al tipo de cambio de la fecha de devengo. La factura simplificada se admite hasta 400 € con IVA, pero está prohibida en facturas a clientes extranjeros (art. 4.4.d).
- El Modelo 390 es **obligatorio** para nuestro perfil (solo quedan exonerados los módulos, el arrendamiento de inmuebles y el SII). Modelo 347: solo contrapartes con más de 3 005,06 €/año, excluidas las operaciones declaradas en el 349 y las operaciones con retención.
- Verifactu (RD 1007/2023, Orden HAC/1177/2024): según el RDL 15/2025, los plazos son: contribuyentes del IS desde el 01.01.2027; el resto (autónomos en IRPF) desde el 01.07.2027. **El 05.10.2026 Hacienda anunció un aplazamiento hasta octubre de 2028**; la norma todavía no se ha publicado. El software de desarrollo propio también debe cumplir los requisitos (cadena de hash SHA-256, QR de 30–40 mm, registros XML) y debe tener su propia declaración responsable.
- Factura electrónica B2B (Ley Crea y Crece, RD 238/2026, Orden HAC/1028/2026): obligatoria cuando el destinatario es un empresario en España, desde el **06.10.2027** (volumen de operaciones > 8 millones) y desde el **06.10.2028** (todos los demás). No se aplica a clientes extranjeros.
- Libros registro: facturas expedidas, facturas recibidas y bienes de inversión. El formato oficial de la AEAT es XLSX (LSI.xlsx), con las hojas EXPEDIDAS_INGRESOS / RECIBIDAS_GASTOS / BIENES-INVERSIÓN. Ese mismo archivo se importa en Pre303, Renta Web y el Modelo 130.
- Conservación de facturas: plazo de prescripción de la LGT (4 años desde el fin del plazo de presentación de la declaración correspondiente). Para bienes de inversión el plazo es mayor (periodo de regularización + 4 años). Una SL debe conservarlas además 6 años según el Código de Comercio.

## Reglas

1. **Regla general de localización de los servicios B2B**: el servicio se localiza donde está el cliente empresario (sede/EP/domicilio). Si el cliente no está en el TAI (Península+Baleares), la operación es *no sujeta* en España. En vigor desde el 01.01.2010 (Ley 2/2010). Fuente: art. 69.Uno.1º LIVA — https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a69
2. **Regla general B2C**: el servicio se localiza donde está el prestador (TAI) ⇒ IVA español 21 %. Excepción del art. 69.Dos: los servicios enumerados (derechos de propiedad intelectual, publicidad, asesoramiento/consultores/ingeniería/abogacía, tratamiento de datos y suministro de informaciones, traducción, cesión de personal, arrendamiento de bienes muebles, etc.) prestados a un cliente no empresario **fuera de la UE** (no Canarias/Ceuta/Melilla) son no sujetos. Fuente: art. 69.Dos LIVA (mismo enlace).
3. **Servicios electrónicos B2C** (hosting, SaaS/suscripciones, software descargable, cursos en línea sin intervención humana — art. 69.Tres.4º): si el cliente está en otro país de la UE, se aplica el IVA español mientras el importe de estos servicios más las ventas a distancia no supere **10 000 €** (sin IVA) en el año en curso y en el anterior, y no se haya optado por tributar en destino (art. 70.Uno.8º, art. 73). Por encima, se aplica el IVA del país del cliente (OSS/Modelo 369). Si el cliente está fuera de la UE, la operación es no sujeta (AEAT). Fuentes: art. 70.Uno.4º/8º, art. 73 LIVA; AEAT «IVA telecomunicaciones y servicios electrónicos» https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html
4. **Uso efectivo (art. 70.Dos)**: tras la Ley 31/2022 y la Ley 13/2023 solo se aplica a (1) los servicios del art. 69.Dos prestados a clientes no empresarios y (2) el arrendamiento de medios de transporte, si se utilizan efectivamente en el TAI. No se aplica a la consultoría ni al desarrollo B2B para un cliente fuera de la UE. Fuente: art. 70.Dos LIVA (texto consolidado).
5. **Sujeto pasivo en los servicios recibidos de un no residente** (art. 84.Uno.2º.a): el destinatario empresario en el TAI repercute él mismo el IVA (inversión del sujeto pasivo). El documento que permite la deducción es la factura del proveedor o un justificante contable (art. 97.Uno.4º). No hace falta una «autofactura» aparte. Fuente: art. 84, 97 LIVA.
6. **Derecho a deducir** (art. 94.Uno): lo otorgan, entre otras, las operaciones del punto 2º: operaciones fuera del TAI que darían derecho a deducir si se realizaran dentro. ⇒ Los servicios a clientes extranjeros (B2B UE/fuera de la UE, no sujetos) **dan derecho a deducir**. La prorrata (art. 102–106) solo se aplica si hay a la vez operaciones con derecho y sin derecho a deducción (exentas del art. 20). Fuente: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a94
7. **Limitaciones de la deducción**: art. 95: solo los gastos relacionados directa y exclusivamente con la actividad. Bienes de inversión de uso parcial: en proporción al uso. Automóviles (turismos): presunción del **50 %** (y el mismo 50 % para combustible, aparcamiento, reparaciones y recambios, art. 95.Cuatro). Art. 96: nunca se deducen joyas, alimentos/bebidas/tabaco, espectáculos, atenciones a clientes, viajes/hoteles/restaurantes, salvo que el gasto sea deducible en el IRPF/IS. Fuente: art. 95–96 LIVA.
8. **Requisitos formales de la deducción** (art. 97): factura original a nombre del contribuyente con todos los datos del art. 6 RD 1619/2012. Un «tique» (factura simplificada sin NIF del destinatario) no da derecho a deducción, salvo que el vendedor haya añadido el NIF y el domicilio del destinatario y la cuota en una línea separada (art. 7.2 RD 1619/2012). Plazo para ejercer la deducción: 4 años desde el devengo (art. 99.Tres, 100 LIVA).
9. **Devengo en los servicios** (art. 75): cuando se presta el servicio (75.Uno.2º). Con pago anticipado: en el momento del cobro (75.Dos). Servicios continuados (tracto sucesivo, 75.Uno.7º): cuando resulta exigible cada parte del precio. Si la exigibilidad no se produce en el plazo de un año: el 31 de diciembre de cada año. Fuente: art. 75 LIVA.
10. **Obligación de expedir factura** (RD 1619/2012 art. 2): en todas las operaciones, incluidas las no sujetas y las exentas, si el cliente es empresario/profesional o persona jurídica. También cuando la operación se localiza fuera del TAI pero el prestador está en el TAI (art. 2.3.b.b’). Plazo: B2B, antes del día 16 del mes siguiente al devengo (art. 11); B2C, en el momento de la operación. El envío al cliente se hace en el mismo plazo (art. 18). Fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
11. **Contenido de la factura** (art. 6 RD 1619/2012): a) número y serie (numeración correlativa dentro de la serie; las series separadas son obligatorias para las rectificativas y para las facturas expedidas por el destinatario o por un tercero); b) fecha de expedición; c) nombre y apellidos o razón social completos de las partes; d) NIF del prestador; el NIF del cliente es obligatorio en la ISP, en las operaciones en el TAI y en las EIB; e) domicilios de las partes; f) descripción, precio unitario sin IVA, descuentos; g) tipo; h) cuota por separado; i) fecha de la operación, si es distinta; j) en caso de exención, referencia al artículo de la Directiva 2006/112/CE o de la LIVA, o la palabra «exenta»; m) «inversión del sujeto pasivo», si el sujeto pasivo es el destinatario; p) «régimen especial del criterio de caja». En las operaciones del art. 2.3.b.b’.a’’ (B2B UE) se pueden omitir f/g/h, indicando la cantidad y la naturaleza del servicio y el importe imponible (art. 6.3). Desde el 07.12.2023, art. 6.5: si se usa un SIF, se incluye el QR y (solo en la modalidad VERI*FACTU) la frase «VERI*FACTU»/«Factura verificable en la sede electrónica de la AEAT».
12. **Factura simplificada** (art. 4, 7): hasta 400 € con IVA (hasta 3 000 € en las actividades minoristas enumeradas) y para las rectificativas. **No se puede** usar en las EIB ni en las operaciones localizadas fuera del TAI (art. 4.4.d → art. 2.3.b.b’). Es decir, a los clientes extranjeros siempre se les expide factura completa.
13. **Factura rectificativa** (art. 15): obligatoria si hay un error en los datos, una cuota incorrecta o una modificación de la base (art. 80 LIVA). Se expide en cuanto se conoce la causa, dentro de los 4 años desde el devengo. Va en una serie separada. Contiene los datos de la factura rectificada y el contenido de la corrección. Los importes se indican como diferencia (con signo) o «como deben quedar», indicando la diferencia. Reflejo en el 303: casillas 14/15 (modificación de base/cuota) en las operaciones con IVA; en las no sujetas se corrige el importe de la casilla 59/120 del periodo.
14. **Moneda e idioma** (art. 12 RD 1619/2012; art. 79.Once LIVA): los importes pueden estar en cualquier moneda, pero la cuota de IVA va en euros al «tipo de cambio vendedor fijado por el Banco de España» en la fecha de devengo. Según la DGT V2630-17, el BdE no fija ese tipo: se aplica el tipo de referencia del BCE (publicado por el BdE). Se admite otra fuente pública si se aplica de forma constante y no se desvía de forma significativa. Idioma: cualquiera; la AEAT puede exigir una traducción al castellano.
15. **Conservación** (art. 19–23 RD 1619/2012; art. 66–70 LGT): facturas recibidas, copias de las expedidas, justificantes contables y DUA, durante el plazo de prescripción (4 años). Debe garantizarse la autenticidad, la integridad, la legibilidad y el acceso en línea de la AEAT. La conservación fuera de España solo se admite en formato electrónico, con acceso remoto y con comunicación previa a la AEAT. Bienes de inversión: hasta el fin del periodo de regularización (5 años; inmuebles, 10) + prescripción. SL: 6 años según el art. 30 del Código de Comercio.
16. **ROI / NIF-IVA**: antes de la primera operación intracomunitaria, presente el Modelo 036 con la casilla **582** (alta en el ROI) y la fecha de la primera operación en la casilla **584**. El Modelo 037 se suprimió el 03.02.2025 (Orden HAC/1526/2024). Si la AEAT no responde en 3 meses, la solicitud se entiende denegada. Fuente: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html ; BOE-A-2025-410.
17. **Modelo 303**: trimestral (1–20 de abril/julio/octubre; 4T: 1–30 de enero). Devolución (casilla 73): solo en la última declaración del año, si no se está en el REDEME (art. 30 RIVA). En 1T–3T un resultado negativo solo puede quedar «a compensar» (casilla 72). No se puede obtener un resultado «a compensar» si en ese mismo periodo se aplican cuotas de periodos anteriores (casilla 78 cumplimentada). Fuente: Instrucciones 303 2026 — https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
18. **Modelo 390**: obligatorio para todos los que presentan 303 periódicos, excepto (a) quienes declaran trimestralmente solo en el régimen simplificado y/o por arrendamiento de inmuebles urbanos y (b) los obligados al SII. Plazo: 1–30 de enero. Fuente: Instrucciones 390-2025 — https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
19. **Modelo 349**: se presenta por cada periodo en el que haya operaciones con las claves E/A/S/I/T/M/H/R/D/C. La periodicidad es trimestral si el importe de EIB + servicios UE (claves E, S y otras) no ha superado **50 000 €** sin IVA ni en el trimestre en curso ni en ninguno de los 4 trimestres anteriores. En otro caso es mensual (si se supera en el 2.º mes: «trimestre truncado»). Plazos: 1–20 del mes siguiente; por el último periodo del año, 1–30 de enero; julio, hasta el 20 de septiembre (mensuales). Fuente: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
20. **Modelo 347**: anual, en febrero (1–28/29). Incluye las contrapartes con las que en el año se superan **3 005,06 €** (con IVA), con desglose por trimestres. Se excluyen: las operaciones sin obligación de expedir factura, las importaciones/exportaciones de bienes y las operaciones ya declaradas en otras declaraciones periódicas con el mismo contenido (349, retenciones 190/180). No lo presentan: los obligados al SII y las personas que solo tienen operaciones excluidas. Fuente: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
21. **Retención IRPF en la factura de un profesional** a un pagador empresario español: 15 % (art. 101.5.a LIRPF). 7 % en el año de inicio y en los dos siguientes, si en el año anterior no se ejerció actividad profesional y se ha entregado al cliente una comunicación por escrito (art. 95.1 RIRPF). Régimen Beckham: retenciones según las normas del IRNR. Actividad profesional, **24 %**; actividad empresarial, sin retención (art. 114 RIRPF en la redacción del RD 1008/2023). Fuentes: https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
22. **Verifactu: ámbito y plazos**: el RRSIF (RD 1007/2023) se aplica a los contribuyentes del IS, del IRPF con actividades económicas, del IRNR con EP y a las ERAR. No se aplica a los obligados al SII. Plazos según el RDL 15/2025: IS, hasta el 01.01.2027; los demás, hasta el 01.07.2027. El 05.10.2026 el Ministerio anunció la intención de aplazarlo hasta **octubre de 2028** (para coordinarlo con la factura electrónica). Mientras no se publique la norma, rigen las fechas de 2027. Fuentes: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf ; https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
23. **Verifactu: requisitos del SIF** (RRSIF art. 8–16; Orden HAC/1177/2024 art. 10–21): por cada factura, un registro de facturación de alta (XML UTF-8); por cada anulación, un registro de anulación. Huella SHA-256 encadenada (campo Huella del registro anterior). Además, una de estas dos opciones: el envío de todos los registros a la AEAT (modalidad VERI*FACTU, servicio web, control de flujo de 60 s), o la firma XAdES con certificado cualificado + registro de eventos. QR de 30×30–40×40 mm, ISO/IEC 18004, nivel M, con la URL de la AEAT (NIF, serie+número, fecha, importe total). La frase «VERI*FACTU» solo se incluye si se envían los registros. Fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
24. **Declaración responsable** (RRSIF art. 13; OM art. 15): obligatoria para cada versión de cualquier SIF, incluido el **software de desarrollo propio para uso propio**. En ese caso la firma el propio desarrollador-usuario. No hay certificación externa ni registro. Fuente: FAQ AEAT — https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
25. **Factura electrónica B2B** (Ley 18/2022 art. 12; RD 238/2026; Orden HAC/1028/2026, en vigor desde el 06.10.2026): obligatoria cuando el destinatario es un empresario/profesional con sede/EP/domicilio en España. No se aplica a las simplificadas (salvo las del art. 7.2). Plazos: 06.10.2027, emisores con un volumen de operaciones > 8 millones €; 06.10.2028, los demás. Comunicación de estados (aceptada/pagada): 06.10.2027 / 06.10.2028 (personas jurídicas) / 06.10.2029 (personas físicas). Fuente: https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html ; https://www.boe.es/eli/es/rd/2026/03/25/238/con
26. **Libros registro** (art. 62–70 RIVA; Orden HAC/773/2019 para el IRPF): facturas expedidas, facturas recibidas, bienes de inversión (+ determinadas operaciones intracomunitarias, que no nos afectan). Anotaciones en euros, por orden cronológico, con totales por trimestre; las rectificativas, por separado. Formato electrónico de la AEAT: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; diseño de campos: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx
27. **Volumen de operaciones** (art. 121 LIVA) = suma de las contraprestaciones de todas las operaciones del año (incluidas las no sujetas por reglas de localización y las exentas), sin IVA. Se excluyen las entregas de bienes de inversión y las operaciones financieras/inmobiliarias no habituales. Se usa en el 303 (4T, casilla 88, para quienes están exonerados del 390), en el 390 (casilla 108) y para el umbral de 8 millones de la factura electrónica.

## Cifras

### Tipos y umbrales (2025 y 2026, sin cambios para nuestro perfil)

| Parámetro | 2025 | 2026 | Fuente |
|---|---|---|---|
| Tipo general IVA | 21 % | 21 % | art. 90 LIVA |
| Tipo reducido / superreducido | 10 % / 4 % (el 0 % y el 5 %/7,5 % solo se aplicaron a alimentos hasta 2024) | 10 % / 4 % | art. 91 LIVA |
| Umbral OSS (B2C electrónicos + ventas a distancia UE) | 10 000 € sin IVA | 10 000 € | art. 73 LIVA |
| Umbral del 349 mensual | 50 000 € sin IVA (trimestre y 4 anteriores) | 50 000 € | art. 81 RIVA |
| Umbral del 347 por contraparte | > 3 005,06 € con IVA | > 3 005,06 € | art. 33 RGAT |
| Bien de inversión (IVA) | ≥ 3 005,06 € y uso > 1 año | igual | art. 108 LIVA |
| Factura simplificada | ≤ 400 € con IVA (≤ 3 000 € en comercio minorista) | igual | art. 4 RD 1619/2012 |
| Presunción de afectación del automóvil | 50 % | 50 % | art. 95.Tres.2ª LIVA |
| Prorrata: redondeo | al alza, hasta el % entero | igual | art. 104.Dos LIVA |
| Prorrata especial obligatoria | si la general da una deducción ≥ 10 % mayor | igual | art. 103.Dos.2º |
| Gran empresa (303 mensual, SII) | > 6 010 121,04 € de volumen de operaciones del año anterior | igual | art. 71.3 RIVA |
| Retención profesional (IRPF general) | 15 % / 7 % (inicio) | 15 % / 7 % | art. 101.5 LIRPF, 95.1 RIRPF |
| Retención profesional (Beckham, IRNR) | 24 % | 24 % | art. 114 RIRPF |
| Plazo para deducir el IVA soportado | 4 años desde el devengo | 4 años | art. 99–100 LIVA |
| Conservación de facturas | 4 años (prescripción) | 4 años | art. 66 LGT, art. 19 RD 1619/2012 |
| Plazo de expedición de la factura B2B | antes del día 16 del mes siguiente | igual | art. 11 RD 1619/2012 |

### Plazos (calendario)

| Modelo | Periodo | Plazo | Domiciliación (−5 días) |
|---|---|---|---|
| 303 | 1T/2T/3T | 1–20 abr / jul / oct | hasta el día 15 |
| 303 | 4T | 1–30 de enero | hasta el 25 de enero |
| 390 | año | 1–30 de enero | — |
| 349 trimestral | 1T–3T | 1–20 abr / jul / oct | — |
| 349 | 4T (o diciembre) | 1–30 de enero | — |
| 347 | año | 1–28(29) de febrero | — |
| 369 (OSS) | trimestre | hasta el último día del mes siguiente al trimestre | — |
| 036 alta ROI | — | antes de la primera operación UE | — |
| 036 cambio de domicilio fiscal | — | 1 mes desde el cambio (art. 10 RGAT) | — |

Si el último día es inhábil (fin de semana o festivo), el plazo pasa al siguiente día hábil (calendario de la AEAT).

### Verifactu / factura electrónica: fechas

| Obligación | Fecha | Estado |
|---|---|---|
| SIF adaptado: contribuyentes del IS | 01.01.2027 | en vigor (RDL 15/2025) |
| SIF adaptado: autónomos en IRPF y demás | 01.07.2027 | en vigor (RDL 15/2025) |
| Aplazamiento de todo el RRSIF a octubre de 2028 | ~10.2028 | anunciado el 05.10.2026, **norma no publicada** |
| Factura electrónica B2B, volumen de operaciones > 8 millones € | 06.10.2027 | en vigor (RD 238/2026 + OM HAC/1028/2026) |
| Factura electrónica B2B, los demás (nuestro perfil) | 06.10.2028 | en vigor |
| Comunicación de estados de la factura electrónica, personas físicas | 06.10.2029 | en vigor |

### Casillas del Modelo 303 (formulario 2025/2026): mapa para nuestro perfil

| Operación | Devengado (base/tipo/cuota) | Deducible (base/cuota) | Informativas | 349 |
|---|---|---|---|---|
| Venta a cliente español al 21 % | 07 / 08 / 09 | — | — | — |
| Venta B2B a cliente UE (servicio) | — | — | **59** | S |
| Venta B2B a cliente fuera de la UE, Canarias/Ceuta/Melilla | — | — | **120** | — |
| Venta B2C fuera de la UE de servicios del art. 69.Dos / electrónicos | — | — | 120 | — |
| Venta B2C en la UE de servicios electrónicos mediante OSS | — (en el 369) | — | 123 | — |
| Exportación de bienes (art. 21) | — | — | 60 | — |
| Operaciones con ISP en las que el sujeto pasivo es el cliente español (art. 84.Uno.2º c–g; no es nuestro caso) | — | — | 122 | — |
| Compra a proveedor español (corrientes) | — | 28 / 29 | — | — |
| Compra de bien de inversión en España | — | 30 / 31 | — | — |
| Importación de bienes (DUA) | — | 32 / 33 (34/35 inversión) | — | — |
| Servicio de proveedor UE (AIS) | **10 / 11** | **36 / 37** | — | I |
| Bien procedente de la UE (AIB) | 10 / 11 | 36 / 37 (38/39 inversión) | — | A |
| Servicio de proveedor fuera de la UE (ISP art. 84.Uno.2º.a) | **12 / 13** | **28 / 29** | — | — |
| Rectificativa con IVA (±) | 14 / 15 | 40 / 41 (recibidas) | — | — |
| Totales | 27 = 152+167+03+155+06+09+11+13+15+158+170+18+21+24+26 | 45 = 29+31+33+35+37+39+41+42+43+44 | 46 = 27 − 45 | |
| Resultado | 64 = 46+58+76; 65 = 100 %; 66 = 64; 110 (saldo de periodos anteriores); 78 (aplicado); 87 = 110−78; 69 = 66+77−78+68+108; 71 = 69−70+109 | | 72 (compensar) / 73 (devolver, solo 4T) | |

### Casillas del Modelo 390 (2025): principales

| Contenido | Casillas |
|---|---|
| Régimen ordinario por tipos (0/4/10/21 %) base/cuota | 01–06, 700–703, 667–670 (21 %: par 05/06 `[INFERENCE: comprobar en el formulario]`) |
| Adquisiciones intracomunitarias de servicios base/cuota por tipos | 545–548, 551–552, 720–723, 687–690 |
| Adquisiciones intracomunitarias de bienes | 21–26, 716–719, 683–686 |
| Otros supuestos de ISP (proveedor fuera de la UE) | 27 / 28 |
| Modificación bases y cuotas | 29 / 30 |
| Total bases / cuotas devengadas | 33 / 34; 47 (cuotas IVA + RE) |
| Deducible interior corrientes (suma) | 48 / 49 (por tipos 695–698, 190–191 …) |
| Deducible interior bienes de inversión | 50 / 51 |
| Deducible importaciones corrientes / inversión | 52 / 53; 54 / 55 |
| Resultado régimen general / suma / compensación año anterior / resultado liquidación | 84, 85, 86 |
| Totales de las autoliquidaciones: a ingresar / a compensar / a devolver | 95, 97, 98 |
| Volumen de operaciones: régimen general / EIB+servicios UE / exportaciones / exentas sin derecho / no sujetas localización / ISP / OSS / total | 99, 103, 104, 105, 110, 125, 126, 108 |

### Claves para los libros registro y los registros Verifactu

| Campo | Valores |
|---|---|
| Calificación de la operación | S1 sujeta no exenta sin ISP; S2 sujeta con ISP; N1 no sujeta art. 7/14; **N2 no sujeta por reglas de localización** |
| Operación exenta | E1 art. 20; E2 art. 21; E3 art. 22; E4 art. 23–24; E5 art. 25 (EIB); E6 otras |
| Clave de régimen | 01 general; 02 exportación; 07 criterio de caja; 08 IGIC/IPSI; 17 OSS; 18 recargo equivalencia … |
| Tipo de factura (Verifactu) | F1 completa; F2 simplificada; F3 sustitutiva de simplificadas; R1–R4 rectificativas (R1 error de derecho/art. 80.Uno-Dos-Seis, R2 art. 80.Tres, R3 art. 80.Cuatro, R4 resto); R5 rectificativa de simplificada |
| Tipo NIF destinatario (libros) | 02 NIF-IVA UE; 03 pasaporte; 04 doc. oficial país; 05 certificado residencia; 06 otro documento probatorio; 07 no censado |

## Fórmulas para el motor

En todos los casos: importes en euros, con 2 decimales, redondeo `ROUND_HALF_UP` (como en los formularios de la AEAT). La cuota se calcula por cada factura (por cada tipo). La cuota ya redondeada se suma en los libros y en el 303. Las validaciones de la AEAT (SII/Verifactu) admiten una desviación `|cuota − base×tipo| ≤ 10 €` por factura `[según el documento de validaciones de la AEAT; confirmar la versión]`.

### 1. Clasificación de la venta (lugar de prestación + régimen de la factura)

```
input: seller{profile: AUTONOMO_IRPF | AUTONOMO_BECKHAM | SL, activity_kind: PROFESIONAL | EMPRESARIAL, years_since_start, oss_registered}
       customer{country, is_business, vat_id (optional, validated in VIES), spanish_withholder: bool}
       service{kind: GENERAL | ELECTRONIC | ART69DOS (consulting, data processing, IP, advertising, translation...) | IMMOVABLE | OTHER_SPECIAL}
       ytd_b2c_eu_electronic_sales (current year and previous year, without IVA)

TAI  = country == ES and region not in {Canarias, Ceuta, Melilla}
EU   = country in EU27 (excluding ES-TAI; Canarias/Ceuta/Melilla treated as NON_EU for IVA)

if service.kind == IMMOVABLE: locate by property (art. 70.Uno.1º) — fuera de nuestro perfil, STOP

# B2B status: vat_id valid in VIES, or (non-EU) other proof of business (Reg. UE 282/2011 art. 18)
b2b = customer.is_business and (customer.country not in EU or vat_id_valid)

case TAI:
    regime = SUJETA_21
    withholding = compute_withholding(seller, customer)          # ver punto 3
case EU and b2b:
    regime = NO_SUJETA_INTRACOM                                  # art. 69.Uno.1º; casilla 59; 349 clave S
    require seller in ROI (ES-VAT in VIES) else -> WARN_ROI
case EU and not b2b:
    if service.kind == ELECTRONIC and (ytd_prev > 10000 or ytd_cur + amount > 10000 or seller.oss_registered):
        regime = OSS_DESTINO                                     # IVA del país del cliente, Modelo 369, casilla 123
    else:
        regime = SUJETA_21                                       # art. 69.Uno.2º / 70.Uno.8º
case NON_EU and b2b:
    regime = NO_SUJETA_LOCALIZACION                              # art. 69.Uno.1º; casilla 120
case NON_EU and not b2b:
    if service.kind in {ART69DOS, ELECTRONIC}: regime = NO_SUJETA_LOCALIZACION   # art. 69.Dos / criterio AEAT
    else: regime = SUJETA_21                                     # regla general art. 69.Uno.2º
    if effectively_used_in_TAI(service): regime = SUJETA_21     # art. 70.Dos (solo B2C art. 69.Dos)
```

Canarias/Ceuta/Melilla: B2B → NO_SUJETA_LOCALIZACION (casilla 120, no la 59; no se presenta el 349); B2C → SUJETA_21 (el art. 69.Dos las excluye).

### 2. Líneas de la factura según el régimen

```
base      = Σ round(qty × unit_price × (1 − discount), 2)
case SUJETA_21:
    tipo = 21.00; cuota = round(base × 0.21, 2)
    retencion = round(base × withholding_rate, 2)            # solo si withholding_rate > 0
    total_factura = base + cuota                              # el «Total factura» de los libros NO se reduce por la retención
    total_a_pagar = base + cuota − retencion
    mentions: []  (con retención: línea «Retención IRPF x %: −N €» y la base de la retención)
case NO_SUJETA_INTRACOM:
    tipo = none; cuota = 0; total = base
    required: NIF-IVA del vendedor (ES…) y del cliente (con prefijo de país), ambos válidos en VIES en la fecha de la factura
    mentions: «Operación no sujeta al IVA español por reglas de localización (art. 69.Uno.1º Ley 37/1992)»,
              «Inversión del sujeto pasivo / Reverse charge — art. 196 Directiva 2006/112/CE»
    forbidden: factura simplificada
case NO_SUJETA_LOCALIZACION:
    tipo = none; cuota = 0; total = base
    mentions: «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)»
              (para B2C art. 69.Dos: referencia al art. 69.Dos)
    forbidden: factura simplificada
case OSS_DESTINO:
    tipo = rate(customer.country); cuota = round(base × tipo, 2); total = base + cuota
    mentions: «IVA … % (país de consumo …) — Régimen de la Unión OSS»; se declara en el 369; en el 303 solo la casilla 123
```

Moneda distinta del EUR: todos los importes de la factura pueden mostrarse en esa moneda, pero hay que añadir la línea «Cuota IVA: N EUR (tipo de cambio BCE dd/mm/aaaa: 1 EUR = X CUR)». En las no sujetas no hay IVA, pero el equivalente en EUR de la base se anota igualmente en el libro al tipo de cambio de la fecha de devengo:

```
fx_date   = devengo_date (fecha de prestación del servicio / de cobro del anticipo), no la fecha de pago
rate      = ECB_reference_rate(fx_date)   # si es inhábil, el último publicado antes de esa fecha [INFERENCE; la DGT V2630-17 solo exige coherencia]
base_eur  = round(base_cur / rate, 2)     # el BCE cotiza 1 EUR = X CUR
cuota_eur = round(base_eur × tipo, 2)
```

### 3. Retención IRPF en la factura (solo a clientes empresarios españoles)

```
if not customer.spanish_withholder: rate = 0          # persona física consumidora, cliente extranjero sin EP en España
elif seller.profile == SL: rate = 0                   # los servicios de una SL no llevan retención (salvo arrendamientos, etc.)
elif seller.activity_kind == EMPRESARIAL: rate = 0    # tanto en el régimen general como en Beckham
elif seller.profile == AUTONOMO_BECKHAM: rate = 0.24  # art. 114 RIRPF → normas IRNR
elif start_year ≤ year ≤ start_year + 2 and no_professional_activity_prev_year and notice_given: rate = 0.07
else: rate = 0.15
retencion = round(base × rate, 2)    # la base es la base imponible sin IVA
```

Lo retenido se descuenta en el IRPF (Modelo 100/151). Este dato se pasa al módulo IRPF/Beckham. No se refleja en el 303.

### 4. Clasificación del gasto (IVA soportado)

```
input: supplier{country, vat_id}, invoice{base, tipo, cuota, currency}, item{kind: CURRENT | INVESTMENT | VEHICLE | FOOD_HOTEL_TRAVEL | GIFTS | PRIVATE_MIX}
deductible_share:
    kind == GIFTS or (FOOD_HOTEL_TRAVEL and not deductible_in_IRPF_IS) -> 0       # art. 96
    kind == VEHICLE (turismo) and related costs -> 0.50 (salvo prueba en contrario) # art. 95.Tres.2ª, Cuatro
    kind == PRIVATE_MIX (agua/luz/internet de la vivienda) -> 0                    # art. 95.Uno; criterio AEAT/TEAC
    en otro caso -> 1.00 × prorrata (prorrata = 1.00 si no hay operaciones del art. 20)
investment = (base ≥ 3005.06 and useful_life > 1y)                                # art. 108
if supplier.country == ES:
    casillas: (28,29) si not investment else (30,31)
elif supplier.country in EU and supplier.vat_id valid and seller in ROI:          # AIS
    devengado (10,11) = (base_eur, round(base_eur×0.21,2)); deducible (36,37) = (base_eur, cuota×share) [(38,39) si investment]
    349: clave I, país, NIF-IVA del proveedor, base_eur
elif supplier.country not in EU (SaaS de EE. UU., etc.):                          # ISP art. 84.Uno.2º.a
    devengado (12,13) = (base_eur, round(base_eur×0.21,2)); deducible (28,29) = (base_eur, cuota×share) [(30,31) si investment]
else (EU supplier charged foreign VAT because no ROI/VAT-id):
    foreign VAT NOT deductible in 303; anotarlo como gasto; devolución solo mediante el Modelo 360 (hasta el 30.09 del año siguiente)
imports of goods (DUA): deducible (32,33) / (34,35), devengado: pagado en la aduana (o casilla 77 si se opta por el diferimiento)
```

En AIS/ISP, cuota devengada = cuota deducible (con share = 1) → efecto nulo en el resultado. Pero las dos partes son obligatorias (art. 97.Uno.4º: solo se deduce si la operación está «debidamente consignada»).

### 5. Cálculo del Modelo 303 del trimestre Q

```
sales  = invoices issued with devengo in Q (incluidas las rectificativas, con signo)
purch  = received invoices registered in Q (también más tarde, dentro del plazo de 4 años)

c07 = Σ base(SUJETA_21);  c08 = 21;  c09 = Σ cuota(SUJETA_21)
c10 = Σ base(AIS + AIB);  c11 = Σ cuota(AIS + AIB)
c12 = Σ base(ISP non-EU); c13 = Σ cuota(ISP non-EU)
c14/c15 = Σ de las modificaciones de base/cuota por rectificativas con IVA (si no se han repartido en 07–09)   # signo ±
c27 = c03+c06+c09+c11+c13+c15 (+ otros tipos/RE = 0)
c28/c29 = Σ ES current + ISP non-EU current (base sin prorrateo; cuota × share)
c30/c31 = Σ ES investment (+ ISP non-EU investment)
c32/c33, c34/c35 = importaciones
c36/c37 = Σ AIS + AIB current;  c38/c39 = AIB investment
c40/c41 = rectificación de deducciones (rectificativas recibidas) ±
c43 = regularización de bienes de inversión (solo si cambió la prorrata/el uso); c44 = solo 4T con prorrata
c45 = c29+c31+c33+c35+c37+c39+c41+c42+c43+c44
c46 = c27 − c45
c59  = Σ base(NO_SUJETA_INTRACOM)        # servicios B2B UE (+ EIB)
c120 = Σ base(NO_SUJETA_LOCALIZACION)    # fuera de la UE, Canarias/Ceuta/Melilla, B2C 69.Dos
c123 = Σ base(OSS_DESTINO)
c64 = c46 (+c58 +c76 = 0);  c65 = 100;  c66 = c64
c110 = saldo a compensar al inicio de Q (de la casilla 72 de periodos anteriores, menos lo aplicado)
c78  = min(c110, max(c66 + c77, 0))      # se aplica el máximo posible
c87  = c110 − c78
c69  = c66 + c77 − c78 + c68 + c108      # c68, c108 = 0 en nuestro caso
c71  = c69 − c70 + c109                  # c70/c109 solo en una rectificativa
if c71 > 0: INGRESAR c71 (IBAN; domiciliación hasta −5 días)
elif c71 < 0 and Q in {1T,2T,3T}: COMPENSAR  c72 = |c71|  (prohibido si c78 > 0; en ese caso el saldo se traslada mediante c87)
elif c71 < 0 and Q == 4T: a elegir DEVOLVER c73 = |c71| (incluido todo c110) o COMPENSAR c72
elif c71 == 0 and (c27>0 or c45>0): RESULTADO CERO
else: SIN ACTIVIDAD
nuevo saldo a compensar = c87 + c72
```

Invariantes: `c08 = 21.00` solo si c07 > 0; `c11 ≈ c10×0.21`, `c13 ≈ c12×0.21`; `c37 ≤ c11` (con deducción del 100 % son iguales); `c59 + c120 + c123 + c07 (+c04+c01) + c60` = ingresos del trimestre según el libro de facturas expedidas.

### 6. Modelo 349 del periodo

```
for each (counterparty, clave) in period:
    clave S: Σ base_eur de servicios NO_SUJETA_INTRACOM; clave I: Σ base_eur AIS; clave E/A: bienes
    registro: código país (DE, FR, …; XI para Irlanda del Norte, solo bienes), NIF-IVA sin prefijo de país, nombre, clave, importe
periodicity: monthly if Σ(E+S+…) > 50000 in current quarter or any of previous 4 quarters, else quarterly
file only if ≥ 1 registro; rectificaciones de periodos anteriores: registros separados de «rectificación» con el periodo y el importe declarado antes
```

Conciliación: `Σ clave S del año = casilla 59 (suma de los 4 trimestres del 303) − EIB = casilla 103 (390)`.

### 7. Modelo 347 del año

```
candidates = counterparties con Σ(total_factura con IVA) > 3005.06 en el año
exclude: contrapartes/operaciones declaradas en el 349 (clientes UE B2B, proveedores UE);
         operaciones con retención incluidas en el 190/180 (clientes B2B españoles del profesional, arrendador con retención);
         importación/exportación de bienes; operaciones sin obligación de factura
include: proveedores españoles sin retención (> 3005.06), clientes españoles sin retención (personas jurídicas B2C, en caso de empresarial/SL),
         clientes y proveedores fuera de la UE por servicios (no sujetas): la AEAT los incluye (no hay exclusión para servicios) [INFERENCE: confirmar en INFORMA]
por cada uno: importe anual (con IVA; para no sujetas, la base) y desglose por trimestres; clave A (compras) / B (ventas)
```

### 8. Modelo 390

Agregación de los 303 del año: devengado por tipos → 01–06; AIS → grupo 545–552; ISP non-EU → 27/28; deducible → 48/49, 50/51, 52/53, 54/55 + bloque intracomunitario; 84 = resultado; 85 = casilla 110 del primer 303 del año (saldo del año anterior); 95 = Σ de los c71 positivos; 97/98 = resultado del último 303 (compensar/devolver); volumen: 99 = Σc07(+04,01), 103 = Σc59, 104 = Σc60, 110 = Σc120, 126 = Σc123, 108 = suma. Además, datos estadísticos: IAE epígrafe, clave A05 (otras actividades profesionales) o A03 (empresariales), indicador «operaciones con terceras personas» (si hay 347).

### 9. Verifactu: registros al expedir una factura

```
on issue(invoice):
    rf = RegistroAlta{
        IDEmisorFactura = seller.NIF, NumSerieFactura = serie+numero, FechaExpedicionFactura = dd-mm-yyyy,
        TipoFactura = F1|F2|R1..R5, Descripcion, Destinatarios[{Nombre, NIF | IDOtro{CodigoPais, IDType, ID}}],
        Desglose[{ClaveRegimen=01, CalificacionOperacion=S1|S2|N1|N2 | OperacionExenta=E1..E6, TipoImpositivo, BaseImponible, CuotaRepercutida}],
        CuotaTotal, ImporteTotal, Encadenamiento{PrimerRegistro | RegistroAnterior{IDEmisor, NumSerie, Fecha, Huella}},
        SistemaInformatico{NombreRazon, NIF, NombreSistemaInformatico, IdSistemaInformatico(2 chars), Version, NumeroInstalacion, TipoUsoPosibleSoloVerifactu=S|N, TipoUsoPosibleMultiOT, IndicadorMultiplesOT},
        FechaHoraHusoGenRegistro = ISO-8601 con zona horaria (2026-03-10T12:00:00+01:00), TipoHuella = 01 (SHA-256), Huella }
    cadena = "IDEmisorFactura=…&NumSerieFactura=…&FechaExpedicionFactura=…&TipoFactura=…&CuotaTotal=…&ImporteTotal=…&Huella=<prev or empty>&FechaHoraHusoGenRegistro=…"
    Huella = UPPER(HEX(SHA256(UTF8(cadena))))          # 64 caracteres; valores con trim; Huella= vacío en el primer registro
    vector de prueba AEAT: "IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00"
                     → 3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60
    mode VERIFACTU: POST XML al web-service de la AEAT (certificado), esperar t≥60 s entre envíos o hasta el límite de registros; reintentos ≥ 1/hora si hay fallo; CSV en la respuesta
    mode NO_VERIFACTU: firmar XAdES Enveloped con certificado cualificado; llevar registro de eventos (arranque/parada, exportación, incidencias) con su propia cadena de hash
    en la versión impresa/PDF: QR 30–40 mm, ISO 18004, nivel M, URL de cotejo AEAT con NIF, serie+numero, fecha, importe total; texto «VERI*FACTU» solo en modo VERIFACTU
on cancel(invoice): RegistroAnulacion{IDFactura, Encadenamiento, Huella sobre los campos NIF, NumSerie, Fecha, HuellaAnterior, FechaHoraHuso}
rectificativa: nuevo RegistroAlta TipoFactura=R1..R5, TipoRectificativa=S (por sustitución) | I (por diferencias), FacturasRectificadas[...]
```

Los registros (XML) y los eventos se conservan hasta la prescripción y no se pueden modificar. Cualquier corrección se hace solo con un registro nuevo. La declaración responsable (OM art. 15: nombre, Id (2 caracteres), versión, componentes, SoloVerifactu S/N, MultiOT S/N, tipo de firma, productor con NIF y domicilio, fecha/lugar) está integrada en el menú del software y también está disponible por separado (PDF).

### 10. Libros registro: anotación

Hoja `EXPEDIDAS_INGRESOS` (LSI.xlsx): Ejercicio | Periodo (1T…4T) | Actividad: Código, Tipo, Grupo/Epígrafe IAE | Tipo de Factura (F1/F2/R1…) | Concepto de Ingreso (IRPF) | Ingreso Computable | Fecha Expedición | Fecha Operación | Identificación de la Factura: Serie, Número, Número-Final | NIF Destinatario: Tipo (02/03/04/05/06/07), Código País, Identificación | Nombre Destinatario | Clave de Operación (01…) | Calificación (S1/S2/N1/N2) | Operación Exenta (E1–E6) | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Repercutida | Tipo/Cuota Recargo Eq. | Cobro: Fecha, Importe, Medio, Identificación Medio | Tipo Retención IRPF | Importe Retenido IRPF | Registro Acuerdo Facturación | Inmueble: Situación, Ref. Catastral | Referencia Externa.

Hoja `RECIBIDAS_GASTOS`: Ejercicio | Periodo | Actividad | Tipo de Factura | Concepto de Gasto | Gasto Deducible | Fecha Expedición | Fecha Operación | Identificación Factura del Expedidor (Serie-Número, Número-Final) | Fecha Recepción | Número Recepción / Final | NIF Expedidor: Tipo, Código País, Identificación | Nombre Expedidor | Clave de Operación | Bien de Inversión (S/N) | Inversión del Sujeto Pasivo (S/N) | Deducible en Periodo Posterior (S/N) | Periodo Deducción: Ejercicio, Periodo | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Soportado | Cuota Deducible | Tipo/Cuota Recargo Eq. | Pago: Fecha, Importe, Medio, Identificación | Tipo/Importe Retención IRPF | Registro Acuerdo Facturación | Inmueble | Referencia Externa.

Hoja `BIENES-INVERSIÓN`: Ejercicio, Periodo, Actividad, Identificador, Descripción, Fecha Inicio Utilización, Valor Adquisición, Valor Amortizable, Método, % Amortización, Amortización (cuota, acumulada inicio/final, pendiente), Identificación factura, NIF/Nombre expedidor, Base, Tipo IVA, Prorrata definitiva, Cuota deducible, Regularización anual (prorrata, cuota deducible, cuota a regularizar), Baja (fecha, causa, factura de transmisión), Referencia externa.

Correspondencia de nuestros regímenes con el libro: SUJETA_21 → S1, clave 01, tipo 21, cuota; NO_SUJETA_INTRACOM → N2, NIF tipo 02 (VAT-id UE), tipo/cuota 0, total = base; NO_SUJETA_LOCALIZACION → N2, NIF tipo 06 (o 04), tipo/cuota 0; AIS/ISP (recibidas) → Inversión del Sujeto Pasivo = S, Cuota Soportado = Cuota Deducible = base×21 %. Correspondencia en Pre303: N2 → casilla 59 si el NIF es tipo 02 UE; en otro caso, 120 `[INFERENCE: comprobar con Traslado_Libros_a_Casillas_IVA 2026.xlsx]`. Archivo: uno por año, acumulativo, con el nombre `{ejercicio}{NIF}T{nombre}.xlsx` (T = unificado IVA+IRPF), ≤ 4 MB.

### 11. Ejemplos resueltos (1T 2026, autónomo profesional, sin Beckham, 2.º año de actividad → retención del 7 %)

**A. B2B UE**: Beispiel GmbH, DE123456789 (VIES ok), servicio de desarrollo de 3 000 €, 2026-01-20.
Factura: base 3 000,00; IVA: no sujeto; total 3 000,00. Menciones: «Operación no sujeta al IVA español (art. 69.Uno.1º LIVA). Inversión del sujeto pasivo — art. 196 Directiva 2006/112/CE». NIF-IVA ES… y DE…. 303: c59 += 3 000. 349 1T: DE | 123456789 | Beispiel GmbH | S | 3 000. Libro: N2, NIF tipo 02.

**B. B2B EE. UU.**: Acme Inc., EIN 12-3456789, 5 000 USD, devengo 2026-02-10, tipo de cambio del BCE 1 EUR = 1,0800 USD → 4 629,63 €.
Factura: 5 000,00 USD (equiv. 4 629,63 EUR, BCE 10/02/2026 1,0800); IVA: no sujeto; «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)». Sin retención. 303: c120 += 4 629,63. 349: no. 347: si en el año se superan 3 005,06 € → incluir (clave B) `[INFERENCE]`. Libro: N2, NIF tipo 06, país US.

**C. B2B España**: Cliente SL, B12345678, consultoría de 2 000 €, 2026-03-05.
Factura: base 2 000,00; IVA 21 % 420,00; retención IRPF 7 % −140,00; total factura 2 420,00; a pagar 2 280,00. 303: c07 += 2 000; c08 = 21; c09 += 420. Retención 140 → al IRPF (Modelo 130/100); el cliente presenta el 111/190. 347: excluido (operación con retención). Libro: S1, clave 01, Tipo Retención 7, Importe 140, Total Factura 2 420.
Variante profesional en Beckham: retención 24 % = 480 → a pagar 1 940,00; empresarial/SL: retención 0 → a pagar 2 420,00.

**D. B2C España**: persona física, NIF 12345678Z, 500 €, 2026-03-20.
Factura (completa o simplificada según el límite de ≤ 400 €: 605 > 400 → completa): base 500,00; IVA 21 % 105,00; total 605,00; sin retención. 303: c07 += 500; c09 += 105.

**Gastos 1T**: coworking (ES) 300 + 63; portátil (ES) 1 500 + 315 (< 3 005,06 → no es bien de inversión → 28/29); AWS (US) 100 € → ISP: c12 100 / c13 21; c28 100 / c29 21; SaaS de Irlanda (IE, VAT-id, estamos en el ROI) 200 € → AIS: c10 200 / c11 42; c36 200 / c37 42; 349 clave I: IE | … | 200.

**303 1T 2026**: c07 2 500; c09 525; c10 200; c11 42; c12 100; c13 21; c27 = 588,00; c28 1 900 (300+1 500+100); c29 399 (63+315+21); c36 200; c37 42; c45 = 441,00; c46 = 147,00; c59 3 000; c120 4 629,63; c66 147; c110 0; c78 0; c69 = c71 = 147,00 → **a ingresar 147,00**.
Si no hubiera ventas C y D: c27 = 63; c45 = 441; c46 = −378 → 1T «a compensar» 378 (c72); en el 2T c110 = 378, etc.; en el 4T, c73 (devolver) por todo el saldo.

## Plazos y modelos

| Modelo | Quién | Periodo | Plazo | Cuándo no se presenta |
|---|---|---|---|---|
| 036 (alta, ROI casilla 582, cambio de domicilio, baja) | todos | por evento | antes del inicio de la actividad / de la primera operación UE; cambio de domicilio: 1 mes | — |
| 303 | todos los sujetos pasivos (autónomo y SL) | trimestre | 1–20 abr/jul/oct; 4T 1–30 ene | nunca (también se presenta «sin actividad») |
| 390 | todos los que presentan el 303, excepto módulos/arrendamiento/SII | año | 1–30 de enero | SII; solo módulos/arrendamiento |
| 349 | quien haya realizado operaciones con clave E/A/S/I… | trimestre (mes si > 50 000 €) | 1–20 del mes siguiente; último periodo, 1–30 ene | no hay operaciones en el periodo |
| 347 | todos los que tengan contrapartes > 3 005,06 € (fuera del 349/190) | año | 1–28(29) de febrero | SII; no hay contrapartes por encima del umbral |
| 369 (OSS) | inscritos en el Régimen de la Unión (alta Modelo 035) | trimestre | hasta el último día del mes siguiente (también si es cero) | no inscrito |
| 360 | quien haya pagado IVA extranjero en la UE sin derecho a deducirlo en el 303 | año | hasta el 30 de septiembre del año siguiente | opcional |
| 111 / 190 | el **cliente** que practica la retención (no nosotros) | trimestre / año | 1–20 del mes siguiente; 190: enero | — |
| Verifactu registros | todos los que usan un SIF (IS, IRPF, IRNR-EP) | de forma continua | desde el 01.01.2027 (IS) / 01.07.2027 (IRPF); anunciado el aplazamiento a 10.2028 | SII |
| Factura electrónica B2B | destinatario empresario en España | — | 06.10.2027 (> 8 millones) / 06.10.2028 (los demás) | cliente en el extranjero; simplificadas |
| Libros registro | todos | de forma continua, con totales por trimestre | anotaciones: antes del fin del plazo de presentación del 303 del periodo correspondiente (art. 69 RIVA) | SII (se llevan en la Sede) |

## Casos límite

- **Cliente UE sin VAT-id válido** (startup antes de registrarse, particular que se presenta como «empresario»): tratarlo como B2C (Reg. UE 282/2011 art. 18.2) → IVA español 21 %. Cuando se obtenga el VAT-id, se puede volver a facturar sin IVA mediante una rectificativa (la DGT lo admite si se puede probar la condición de empresario en la fecha de la operación).
- **Nosotros sin ROI, pero con cliente UE B2B**: la operación sigue siendo no sujeta (la localización no depende del ROI). Pero el 349 exige el NIF-IVA, y el cliente no nos encontrará en VIES → riesgo. Presente el 036, casilla 582, antes de la primera factura.
- **Anticipo de un cliente extranjero**: devengo en el momento del cobro (art. 75.Dos) → factura del anticipo en el periodo en que se cobra, con el tipo de cambio de la fecha de cobro. En las no sujetas no hay IVA, pero el importe va a la casilla 59/120 del trimestre del anticipo.
- **Contrato continuado (retainer) con un cliente extranjero** sin exigibilidad mensual: devengo el 31 de diciembre (art. 75.Uno.7º). En las no sujetas solo afecta al periodo de la 59/120 y del 349.
- **Rectificativa de una operación no sujeta** (descuento/devolución a un cliente de EE. UU.): se refleja reduciendo la casilla 120 en el periodo en que se expide la rectificativa. Si el total del trimestre es negativo: los formularios de la AEAT no aceptan casillas informativas negativas → poner 0 y trasladar el resto `[INFERENCE: comprobar en Pre303]`.
- **Gastos con un 100 % de clientes extranjeros**: el derecho a deducir es completo (art. 94.Uno.2º) y el resultado del 303 es negativo de forma estable. La devolución del 4T llega en un plazo de 6 meses (hasta ~finales de julio), a menudo con un requerimiento de los libros. Por eso es esencial llevar los libros en el formato de la AEAT. Alternativa: REDEME (036, en noviembre para el año siguiente), con 303 mensual y SII obligatorio.
- **Beckham**: no influye en absoluto en el IVA. Solo influye en la retención de las facturas B2B a clientes españoles (24 %/0 %) y en que la retención se computa en el Modelo 151, no en el 100.
- **Traslado entre comunidades autónomas**: no importa para el IVA. Es obligatorio presentar el 036 (cambio de domicilio fiscal) en el plazo de un mes. La serie y la numeración de las facturas no cambian. El domicilio de la factura es el nuevo desde la fecha del cambio.
- **Canarias/Ceuta/Melilla**: cliente empresario allí → no sujeta, casilla 120 (no la 59), no va al 349. Cliente consumidor → 21 %. Proveedor de allí → ISP como con un país tercero (12/13 + 28/29). No confundir con la exportación (la casilla 60 es solo para bienes).
- **Irlanda del Norte (XI)**: mantiene la condición de UE solo para los bienes. Los servicios B2B en UK/XI están fuera de la UE → casilla 120.
- **Automóvil**: 50 % de la cuota en compra/leasing/combustible/aparcamiento. Para un consultor es casi imposible probar un uso superior al 50 %. Ejemplo: leasing 400 + 84 → deducción 42 (base en el libro 400 sin prorrateo, Cuota Deducible 42).
- **Oficina en casa**: el IVA de los suministros de una vivienda usada en parte para la actividad no es deducible (art. 95.Uno; criterio AEAT/TEAC), aunque en el IRPF se deduce el 30 % de la parte proporcional. El alquiler de vivienda está exento: no lleva IVA.
- **Restaurante/hotel/viajes**: el IVA solo es deducible si el gasto es deducible en el IRPF/IS (viaje de trabajo justificado documentalmente) y hay factura completa con NIF (no un tique).
- **Portátil/equipos < 3 005,06 €**: no son bien de inversión a efectos del IVA → casilla 28/29, sin regularización. Si son ≥ 3 005,06 € → 30/31 y regularización durante 5 años si cambia la prorrata o el uso.
- **SaaS de EE. UU. sin factura con NIF** (solo un receipt): para la ISP basta un justificante contable (art. 97.Uno.4º). Pero el justificante debe identificar al proveedor, el servicio, la fecha y el importe. Hay que conservarlo.
- **Servicios electrónicos B2C en la UE**: venta de suscripciones/cursos a particulares europeos → vigile el umbral de 10 000 € (incluido el año anterior). Si se supera: alta en OSS (Modelo 035) y Modelo 369; IVA al tipo del país del cliente; se necesitan 2 pruebas de la ubicación del cliente (IP, domicilio, banco).
- **Factura simplificada a un cliente extranjero**: prohibida. En Verifactu tampoco sirve el tipo F2: solo F1.
- **SL frente a autónomo**: el IVA es idéntico. La SL siempre presenta por vía electrónica con certificado. Como persona jurídica está sujeta a la factura electrónica B2B (estados desde el 06.10.2028) y a Verifactu como contribuyente del IS desde el 01.01.2027 (si no se formaliza el aplazamiento).
- **Verifactu con software alojado por el propio usuario**: la declaración responsable es obligatoria para cada versión; NIF del productor = NIF del usuario. Es más cómoda la modalidad VERI*FACTU (no hace falta firma XAdES ni registro de eventos, y genera más confianza en las devoluciones). Alternativa gratuita: la aplicación de la AEAT (pero entonces las facturas se llevan solo en ella).
- **Cliente español que paga desde el extranjero / en otra moneda**: la localización depende del cliente (TAI) → 21 % con independencia de la moneda; cuota en euros al tipo de cambio de la fecha de devengo.

## Puntos no aclarados

1. **Verifactu: fecha real de inicio.** Según la norma (RDL 15/2025): 01.01.2027 / 01.07.2027. El 05.10.2026 Hacienda anunció el aplazamiento de las «obligaciones que aún no han entrado en vigor» hasta octubre de 2028 (para coordinarlas con la factura electrónica de < 8 millones). Pero el RD todavía no se ha publicado; la AEAT habla de «previsión». Implementación con cautela: construir ya el SIF según los requisitos del RRSIF/OM (cadena, XML, QR) y activar el envío/la firma obligatorios según la fecha realmente en vigor; seguir el BOE.
2. **Factura electrónica B2B: formato técnico para nuestro perfil.** El RD 238/2026 remite a las sintaxis y a la SPFE (solución pública), con obligación de enviar una copia si se usa una plataforma privada. Los detalles de los formatos (Facturae/UBL/CII) y de la API de la SPFE en la Orden HAC/1028/2026 no se han comprobado: **UNVERIFIED**. Con uno o dos clientes españoles es más sencillo usar directamente la SPFE desde el 06.10.2028.
3. **Correspondencia en Pre303 N2 → 59 o 120** según el tipo de NIF del cliente: no está confirmada con una fuente primaria (no se ha leído `Traslado_Libros_a_Casillas_IVA 2026.xlsx`). Con cautela: no confiar en la importación automática y calcular nosotros mismos la 59/120.
4. **347 para clientes/proveedores extranjeros (fuera de la UE) por servicios**: el texto del art. 33 RGAT solo excluye la importación/exportación de *bienes*; la práctica de la AEAT es incluirlos; **UNVERIFIED** en INFORMA. Con cautela: incluirlos (una declaración de más no causa daño; una omisión es una infracción del art. 198/199 LGT).
5. **Tipo de cambio para las no sujetas y para el IRPF**: el art. 79.Once se refiere formalmente al IVA. Para el importe del ingreso en el IRPF y en los libros se aplica el mismo principio (devengo) según la doctrina de la DGT; se admiten fuentes alternativas (V2630-17). Con cautela: una sola fuente (BCE, día del devengo; en días inhábiles, el último publicado). La diferencia de cambio en el cobro es un resultado financiero ajeno al IVA.
6. **Casillas informativas 59/120 negativas** en las rectificativas: no se ha comprobado cómo se comporta el formulario. Con cautela: limitarlas a cero y trasladar el resto de la corrección al trimestre siguiente, con una nota en el libro.
7. **Beckham + empresarial frente a profesional**: la calificación de la actividad (IAE sección 1ª o 2ª) determina la retención del 24 % o del 0 %. Lo decide el módulo Beckham/IRPF; aquí el motor solo recibe el indicador. La condición de «actividad emprendedora» (ENISA) no influye en el IVA.
8. **Margen de validación de ±10 €** entre base×tipo y la cuota en Verifactu/SII: dato de memoria del documento de validaciones de la AEAT; la versión de 2026 no se ha vuelto a comprobar: **UNVERIFIED**. El motor calcula de todas formas con exactitud; el margen solo hace falta al importar facturas de terceros.
9. **Casillas del 390 por tipos** (05/06 para el 21 %): deducidas del rango «01–06» de las instrucciones, no cotejadas con el formulario: `[INFERENCE]`. Los demás números del 390 (27/28, 545–552, 48–55, 84–86, 95–98, 99–110, 125–126, 108) proceden de las Instrucciones 390-2025.
10. **Tipos de IVA de 2027**: no se han publicado cambios; RETA/IRPF quedan fuera de este archivo.
11. **Código XI / UK después del Brexit para servicios**: el UK es un «país tercero» completo para los servicios (casilla 120); XI solo cuenta como UE para los bienes. No se ha buscado una confirmación adicional.
12. **REDEME**: las condiciones (ausencia de deudas, SII) y el plazo de la opción (noviembre) proceden del conocimiento general del art. 30 RIVA; no se han releído: **UNVERIFIED**.

### Fuentes principales

- LIVA (Ley 37/1992) consolidada: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- RD 1619/2012 (Reglamento de facturación) consolidado, con las modificaciones del RD 1007/2023 y del RD 238/2026: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Instrucciones Modelo 303 2026 (AEAT): https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
- Formulario 303 (Manual IVA 2025, anexo): https://sede.agenciatributaria.gob.es/static_files/Sede/Biblioteca/Manual/Practicos/IVA/IVA_2025/Imagenes/Cap_9_303_eu_es.pdf
- Instrucciones 390-2025: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
- Instrucciones 349: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
- 347 excluidas: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
- RD 1007/2023 (RRSIF): https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; RDL 15/2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Nota de Hacienda del 05.10.2026 (aplazamiento a 10.2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- AEAT Verifactu FAQ (actualizado el 21.07.2026): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html ; especificación de la huella: https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/Veri-Factu_especificaciones_huella_hash_registros.pdf
- Factura electrónica: RD 238/2026 https://www.boe.es/eli/es/rd/2026/03/25/238/con ; calendario de la AEAT https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html
- Formato de los libros registro: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; LSI.xlsx: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx ; Orden HAC/773/2019: https://www.boe.es/eli/es/o/2019/06/28/hac773
- Retenciones 2026 (desde el 10.09.2026): https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; RD 1008/2023 (Beckham 24 %): https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
- Modelo 037 suprimido / ROI casilla 582: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 ; https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html
- Servicios electrónicos B2C/OSS: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html ; Orden HAC/610/2021 (Modelo 369): https://www.boe.es/eli/es/o/2021/06/16/hac610
- Tipo de cambio: DGT V2630-17 (a través de Iberley): https://www.iberley.es/resoluciones/resolucion-vinculante-dgt-v2630-17-16-10-2017-1473112 ; ECB reference rates: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.es.html
