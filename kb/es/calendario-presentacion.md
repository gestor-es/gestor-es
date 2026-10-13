*Traducido del original ruso [kb/calendario-presentacion.md](../calendario-presentacion.md) el 13.10.2026. El archivo ruso es la fuente de verdad; los datos se comprobaron en la fecha indicada abajo.*

## Resumen

- Comprobado con las fuentes primarias disponibles a **08.10.2026**. El año de las rentas (`ejercicio`) y el año de presentación son campos distintos: las declaraciones anuales del ejercicio 2025 se presentan en 2026; las del ejercicio 2026, principalmente en 2027.
- Para una pequeña empresa en territorio común, los modelos trimestrales 303/130/111/115 se presentan normalmente hasta el 20 de abril, de julio y de octubre. **Para el 4T los plazos son distintos:** 111/115, hasta el 20 de enero; 303/130/349 y 390, hasta el 30 de enero, con traslado si el día es inhábil; 180/190, hasta el 31 de enero, con traslado.
- En 2026 el plazo de domiciliación de los modelos 303/130 del 4T de 2025 es el **27 de enero**, no automáticamente el 25 de enero. Para los trimestres ordinarios es el 15 de abril, de julio o de octubre. El calendario no se puede implementar con la fórmula «fecha de presentación menos cinco días».
- Renta 2025 por Internet: **08.04–30.06.2026**; domiciliación, hasta el **25.06.2026**. El modelo 151 es un servicio aparte, no el Renta WEB ordinario; **se admite Cl@ve**, y el certificado no es la única forma de acceso.
- Para el modelo 303 del 4T de 2026 la AEAT ya publica expresamente el **01.02.2027**. Las demás fechas de 2027 que figuran abajo y que no están confirmadas por un calendario propio de la AEAT se marcan como calculadas; la fecha exacta de inicio de Renta 2026 en 2027 es **UNVERIFIED**.
- Los modelos 303/130 se pueden generar como fichero de texto según el diseño de registro e importar en el formulario de la Sede. **No es CSV, ni PDF, ni un XML libre**, aunque lleve etiquetas de cierre `<T...>`.
- Ficheros vigentes comprobados: **DR303e26v101.xlsx** para 2026; **DR303e25.xlsx** para 2025; **DR130e15v12.xls** para 2019 y ejercicios siguientes. El año que figura en el nombre de la especificación del 130 no significa que esté obsoleta.
- Pre303 es un servicio confirmado de cumplimentación previa del formulario. **No está confirmada** una API pública y documentada de Pre303 que permita a un programa de terceros calcular o presentar la declaración sin el formulario. La API del SII o de VERI*FACTU no sustituye la presentación del 303.
- El NIE es suficiente para obtener un certificado FNMT español y para registrarse en Cl@ve, con la debida acreditación de la identidad. El pasaporte ruso y la TIE **no son DNIe**. Una SL presenta con el certificado electrónico de su representante o mediante un representante apoderado; no con el Cl@ve personal como sustituto del certificado de la SL.
- Los estados «fichero creado», «formulario validado», «NRC obtenido», «declaración aceptada» e «impuesto pagado» son independientes. La presentación se acredita con el **justificante + CSV + fecha y hora de la AEAT**; la domiciliación exige comprobar después el cargo en cuenta.
- Presentación fuera de plazo sin requerimiento previo con importe a ingresar: recargo por declaración extemporánea del art. 27 LGT, **«1 por ciento más otro 1 por ciento adicional por cada mes completo de retraso»**; pasados 12 meses, **15% e intereses**. Una declaración con resultado cero o una declaración informativa no queda libre de sanción: se aplican sanciones propias.
- La autoliquidación rectificativa no se introdujo a la vez para todos los modelos: para el 303, desde el 09/3T de 2024; para el 100, desde el ejercicio 2024; para el 200, para los periodos iniciados a partir del 01.01.2024. El 130 mantiene la complementaria. Una declaración inicial no presentada no es una complementaria.

## Reglas

1. **Los plazos y sus traslados dependen del modelo concreto y del calendario de la AEAT.** Según la AEAT, «si el vencimiento del plazo de presentación coincide con un día inhábil, el plazo finaliza el primer día hábil siguiente». Para la atención electrónica, la referencia es el calendario oficial de la Sede, no una lista cualquiera de festivos del lugar de residencia. Para la domiciliación bancaria, la AEAT establece que «entre la finalización del plazo de presentación de una autoliquidación con domiciliación del pago y la finalización del plazo genérico de presentación e ingreso voluntario de esa misma autoliquidación, **deberá existir un mínimo de tres días hábiles o cinco naturales**. A estos efectos, se considerarán días inhábiles los sábados, los domingos, las festividades nacionales y las festividades autonómicas o locales que afecten al municipio en el que radique el Departamento de Informática de la Agencia Tributaria». Se aplica a las presentaciones de 2025–2026 aquí tratadas; la tabla de 2026 prevalece sobre la regla aproximada. Fuente: [Plazos de presentación de autoliquidaciones con domiciliación bancaria, 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html).

2. **La periodicidad trimestral del 349 no se deriva de la periodicidad trimestral del 303.** La periodicidad básica de la declaración recapitulativa (349) es mensual. Se admite la trimestral «cuando ni durante el trimestre de referencia ni en cada uno de los cuatro trimestres naturales anteriores el importe total de las entregas de bienes y prestaciones de servicios que deban consignarse en la declaración recapitulativa sea superior a 50.000 euros, excluido el Impuesto sobre el Valor Añadido». Si se supera dentro del trimestre, «deberá presentarse una declaración recapitulativa para el mes o los meses transcurridos desde el comienzo de dicho trimestre natural»; no se debe usar el 349 anual. Si no hay operaciones que declarar, no hace falta un «349 a cero». Para julio existe un plazo ampliado hasta el 20 de septiembre; para diciembre o el 4T, hasta el 30 de enero. Se aplica en 2025–2026. Fuentes: [AEAT, operaciones intracomunitarias](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/5-impuesto-sobre-valor-anadido/5_9-operaciones-intracomunitarias.html), [plazos del 349, manual IVA 2026](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2026/capitulo-09-declaraciones-informativas-iva-379/declaracion-recapitulativa-operac-intracomunitarias-modelo-349/plazo-presentacion.html).

3. **El modelo 036 es una obligación vinculada a hechos concretos, no trimestral.** Declaración de alta: «antes de iniciar las correspondientes actividades o del nacimiento de la obligación de retener o ingresar a cuenta». Declaración de modificación: «1 mes desde el día siguiente al de la modificación». Declaración de baja: «1 mes desde el cese o la cancelación efectiva de los asientos en el Registro Mercantil». Para el domicilio fiscal del autónomo se usa la declaración censal de modificación (036), casilla 122; el cambio de domicilio no debe esperar a la Renta. La solicitud de alta en el Registro de Operadores Intracomunitarios (ROI) se debe presentar antes de las operaciones intracomunitarias correspondientes. Para las opciones de IVA y del IS hay plazos especiales: por ejemplo, la «Opción por el pago fraccionado sobre la parte de la base imponible del período de los 3, 9 u 11 primeros meses de cada año natural» (art. 40.3 LIS) se ejerce en el «mes de febrero del año en que deba surtir efectos, solo para periodos impositivos que coincidan con el año natural»; en 2026, hasta el 02.03.2026. El modelo 037 está suprimido desde el **03.02.2025**. Fuentes: [036 en el calendario 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/modelo-036.html), [plazo de modificación](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/plazos-presentacion/declaracion-modificacion-modelo-036.html), [casilla 122](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/modificacion-modelo-036/casilla-122-domicilio-fiscal-modelo-036.html), [02.03.2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html).

4. **La identificación depende del declarante, no solo del modelo.** Las personas físicas pueden usar Cl@ve para los modelos 036, 100, 111, 115, 130, 149, 151, 180, 190, 303, 347, 349, 390, 714, 720 y 721. El certificado o el DNIe sirven para más trámites. La SL está obligada a presentar por vía electrónica con certificado; las facultades del administrador o representante deben estar reconocidas. El número de referencia sirve solo para los trámites del IRPF autorizados, no como acceso universal. Se aplica en 2025–2026; la lista se comprobó con el calendario de 2026. Fuente: [AEAT, identificación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/recuerde/identificacion-presentar-autoliquidaciones.html).

5. **Para un extranjero sin DNIe existe una vía FNMT plenamente operativa con NIE.** «Solicitud vía internet de su Certificado» de persona física → «Código de Solicitud» → «Acreditación de la identidad en una Oficina de Acreditación de Identidad», en persona, con los originales vigentes de la TIE o del documento oficial del NIE y del pasaporte → «Descarga de su Certificado de Usuario» según las instrucciones de la FNMT. Normalmente se necesita cita previa. Conviene exportar una copia de seguridad protegida de la clave privada. Para Cl@ve están disponibles el «Registro por Internet en el sistema Cl@ve con certificado o DNI electrónico», el registro presencial o el «Registro en Cl@ve por internet con carta de invitación y CSV», con la carta enviada al domicilio fiscal; con NIE se indica el número de soporte del documento. La carta da un nivel de registro básico; no todos los trámites de nivel avanzado están disponibles. No se debe suponer que un tipo concreto de videoidentificación está disponible para el pasaporte ruso. Es un procedimiento vigente, no un tipo impositivo anual. Fuentes: [FNMT: documentos](https://www.sede.fnmt.gob.es/registro-inicio/preguntas-frecuentes/-/asset_publisher/DKnDigPrgk4U/content/4-3-2-3-acreditacion-de-la-identidad-de-una-persona-fisica), [Cl@ve con carta](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/registrarse-clave-pin/registro-internet-csv.html), [número de soporte](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/incidencias-tecnicas-clave-pin/introduzca-soporte-valido.html).

6. **Renta WEB y el modelo 151 son flujos de trabajo distintos.** El IRPF ordinario se presenta con Renta WEB / modelo 100. El régimen Beckham usa el formulario propio del 151, con Cl@ve o certificado/DNIe, `Importar` y `Exportar` del fichero con formato BOE `.151`, `Validar declaración` y `Firmar y enviar`. No se puede sustituir automáticamente el 151 por la declaración 100 ni declarar que el 151 es «solo manual, sin fichero». Para el 151 está publicado el DR del ejercicio 2023 y siguientes, aplicable a los años aquí tratados. Fuentes: [ayuda técnica del 151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html), [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), [instrucciones del 151](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html).

7. **Importar la declaración no es presentarla.** Después de `Importar` hay que elegir el tipo de declaración (a ingresar, domiciliación, reconocimiento de deuda, etc.), corregir los errores que muestre `Validar declaración`, `Firmar y enviar` y obtener el justificante. `Guardar`, `Vista previa`, `Exportar` y el NRC, por separado, no lo acreditan. El NRC es el «Número de Referencia Completo de 22 caracteres que sirve como justificante del pago», no de la presentación de la declaración; sus datos deben coincidir con NIF/modelo/ejercicio/periodo/importe. Con `Reconocimiento de deuda`, la solicitud de aplazamiento o compensación se tramita por separado, desde el enlace `Tramitar deuda` del recibo de presentación, si no se completa directamente en el flujo. Se aplica a los formularios vigentes de 2025–2026. Fuentes: [130](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-130.html), [151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html).

8. **Pre303 no exime de comprobar los datos de origen.** El servicio ofrece la Ventana Censal IVA, la Identificación, el Resultado y la Cartera de cuotas a compensar. Un cálculo ampliado es posible con el SII o los Libros Agregados, o con la importación de los libros registro para los obligados no SII que reúnan los requisitos. El representante necesita los apoderamientos correspondientes para todas las funciones, en particular PRE303. A 08.10.2026 no se ha encontrado, en la documentación pública revisada, un contrato de API de Pre303 para una presentación automática independiente; está confirmada la vía del formulario + fichero oficial o libros. Fuentes: [Pre303](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303.html), [funciones](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/que-servicios-funcionalidades-tiene-nuevo-pre303.html), [acceso](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/acceder-pre303.html), [ayuda técnica del 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303.html).

9. **El RETA se gestiona aparte de la AEAT, en Import@ss.** En `Base de cotización y rendimientos` se comunica o modifica la previsión del rendimiento neto medio mensual y la base dentro del tramo permitido. Hay hasta seis fechas de efecto de los cambios al año, sin cambio retroactivo inmediato de todos los meses anteriores. En `Consulta de recibos de trabajo autónomo` están disponibles las cuotas emitidas; la emisión se debe cotejar con el cargo bancario. Las reglas del sistema se aplican desde 2023 y son aplicables en 2025–2026. Fuentes: [modificación de la base](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos), [guía autónomo](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo+Autonomo/guia), [recibos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta%2Bde%2Bpagos%2By%2Bdeudas/ConsultaRecibos).

10. **La presentación fuera de plazo sin requerimiento previo y la falta de pago de una deuda ya declarada son supuestos distintos.** El art. 27 LGT se aplica a una autoliquidación presentada voluntariamente fuera de plazo por un periodo correctamente indicado. No se deben mezclar las operaciones omitidas con el trimestre en curso. El recargo se reduce en un 25% solo si se cumplen las condiciones de pago de la deuda y del recargo del art. 27.5; no se debe prometer la reducción ante cualquier reconocimiento de deuda. Si no se paga, pueden añadirse los recargos del período ejecutivo del art. 28. La escala actual del art. 27 se aplica desde el **11.07.2021** y, por tanto, en 2025–2026. Fuente: [LGT, arts. 27–28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27).

11. **No tener importe a ingresar no elimina la obligación de declarar ni las sanciones.** Art. 198 LGT, por no presentar en plazo sin perjuicio económico: «multa pecuniaria fija de 200 euros o, si se trata de declaraciones censales […], de 400 euros»; en las declaraciones informativas, «multa pecuniaria fija de 20 euros por cada dato o conjunto de datos referidos a una misma persona o entidad que hubiera debido incluirse en la declaración con un mínimo de 300 euros y un máximo de 20.000 euros». Si se presentan «fuera de plazo sin requerimiento previo de la Administración tributaria, la sanción y los límites mínimo y máximo serán la mitad de los previstos en el apartado anterior». Es una posible sanción en un procedimiento aparte, no un importe que se añade automáticamente a una casilla del impuesto. Si hay perjuicio para Hacienda tras un requerimiento, puede aplicarse el art. 191: del 50 al 150% de la cuota dejada de ingresar, según la infracción. Se aplica en 2025–2026. Fuente: [LGT, arts. 191, 198, 199](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198).

12. **La forma de rectificar depende del modelo y del periodo impositivo.** Para el 303, desde el 09/3T de 2024, la autoliquidación rectificativa es la vía general tanto si el resultado aumenta como si disminuye. Existen excepciones especiales, en particular ciertas controversias sobre el IVA repercutido y sobre la vulneración de una norma de rango superior. Para el 100, desde el ejercicio 2024, se usa la rectificativa en los casos previstos, y se mantienen complementarias especiales para determinados supuestos de regularización. Para el 200, en los periodos iniciados a partir del 01.01.2024, se usa la rectificativa. El 130, el formulario vigente del 151 y las retenciones ordinarias mantienen sus propios mecanismos de complementaria o solicitud de rectificación; no se les debe aplicar automáticamente la novedad del 100. Fuentes: [303, rectificaciones](https://sede.agenciatributaria.gob.es/Sede/iva/presentar-declaracion-iva-modelo-303/errores-declaracion.html), [FAQ 303](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/autoliquidacion-rectificativa.html), [100 ejercicio 2024](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2024/c18-cuota-liquida-resultante-autoliquidacion/regularizacion-situaciones-tributarias/general.html), [200](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2024/capitulo-02-identificac-autoliq-compl-incn/autoliquidacion-rectificativa.html), [130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

## Cifras

### Valores fijos para el calendario y los riesgos

| Parámetro | 2025 | 2026 | Precisión |
|---|---:|---:|---|
| Límite del 349 trimestral | 50 000 € | 50 000 € | Trimestre en curso y cada uno de los cuatro anteriores; sin IVA, por las operaciones de salida correspondientes |
| Umbral de operaciones ordinarias por contraparte para el 347 | >3 005,06 € | >3 005,06 € | Importe anual con IVA; las exclusiones pesan más que el propio umbral |
| Obligación formal del 714 con independencia de la cuota | Bienes o derechos >2 000 000 € | Igual | Además de la obligación cuando hay cuota a ingresar; computar los bienes del ámbito impositivo correspondiente, antes de deudas y teniendo en cuenta los bienes exentos |
| Umbral inicial del 720 | >50 000 € por bloque correspondiente | Igual | No es un umbral único para todo el patrimonio en el extranjero; hay exclusiones contables y personales |
| 720 sucesivo | Aumento del bloque correspondiente >20 000 € respecto de la última presentación obligatoria | Igual | Tener en cuenta también la extinción de la titularidad o de las facultades, no solo el aumento |
| Umbral inicial del 721 | En conjunto >50 000 € | Igual | Criptomonedas custodiadas en el extranjero; la autocustodia no se incluye |
| 721 sucesivo | Aumento >20 000 € y ciertos casos de extinción de la condición | Igual | Comprobar las reglas del art. 42 quater; no copiar literalmente todas las reglas del 720 |
| Art. 27, antes de 12 meses | 1% + 1 p.p./mes completo | Igual | Sin requerimiento; no se dividen los días entre 30 |
| Art. 27, pasados 12 meses | 15% + intereses | Igual | Intereses solo desde el día siguiente al fin de esos 12 meses |
| Reducción del recargo del art. 27.5 | 25% del recargo | 25% | Condicionada; la deuda y los intereses no se reducen con esta rebaja |
| Interés de demora tributario | 4,0625% anual | 4,0625% según la tabla comprobada o su prórroga | No congelar el tipo para años futuros |
| Art. 28: ejecutivo / apremio reducido / ordinario | 5% / 10% / 20% | Igual | Excluyentes entre sí; el 20% es compatible con los intereses |
| Art. 198: declaración ordinaria sin perjuicio | 200 € / 100 € de forma voluntaria | Igual | Antes de otras reducciones de la sanción aplicables |
| Art. 198: declaración censal | 400 € / 200 € de forma voluntaria | Igual | Para el 036 del autónomo; no confundir con los 100 € del art.198.5 para una persona física sin actividad |
| Art. 198: declaración informativa | 20 €/dato, mín. 300 €, máx. 20 000 € | Igual | De forma voluntaria: 10 €/dato, mín. 150 €, máx. 10 000 € |
| Límite de los formularios web 349/190/347 | 40 000 registros | 40 000 registros en las instrucciones vigentes | Si se supera, fichero/TGVI; un fichero pequeño también se admite |

Fuentes de la tabla: [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), [intereses, Banco de España](https://clientebancario.bde.es/pcb/es/menu-horizontal/productosservici/relacionados/tiposinteres/guia-textual/tiposinteresrefe/tabla_tipos_interes_demora.html), [AEAT, intereses 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html), [714](https://sede.agenciatributaria.gob.es/Sede/no-residentes/impuesto-sobre-patrimonio/declaracion-impuesto-patrimonio-no-residentes.html), [exclusiones del 347](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes.html), [721 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html).

### Presentaciones en 2026 y cierre del ejercicio 2026 a principios de 2027

Todas las fechas son inclusivas. `—` significa que la domiciliación no se aplica a una declaración informativa; no significa que no haya obligación de presentar.

| Modelo / periodo | Plazo de presentación | Último día de domiciliación | Estado |
|---|---|---|---|
| 111, 115: 4T 2025 | 01–20.01.2026 | 15.01.2026 | AEAT |
| 303, 130: 4T 2025 | 01–30.01.2026 | **27.01.2026** | AEAT |
| 349: 4T/12M 2025; 390: año 2025 | 01–30.01.2026 | — | AEAT |
| 190, 180: año 2025 | 01.01–02.02.2026 | — | AEAT |
| 347: año 2025 | 01.02–02.03.2026 | — | AEAT |
| 720, 721: año 2025 | 01.01–31.03.2026 | — | AEAT |
| 303, 130, 111, 115: 1T 2026 | 01–20.04.2026 | 15.04.2026 | AEAT |
| 349: 1T 2026 | 01–20.04.2026 | — | AEAT |
| 202: 1P 2026 | 01–20.04.2026 | 15.04.2026 | AEAT; no es por defecto un «beneficio trimestral del 1T» |
| 100, 151, 714: año 2025 | Campaña por Internet 08.04–30.06.2026 | 25.06.2026 | Fin general y domiciliación confirmados para los tres; el 151 es un servicio aparte |
| 303, 130, 111, 115: 2T 2026 | 01–20.07.2026 | 15.07.2026 | AEAT |
| 349: 2T 2026 | 01–20.07.2026 | — | AEAT |
| 200: año natural 2025 | 01–27.07.2026 | **22.07.2026** | AEAT; el 25 de julio es sábado |
| 718: año 2025, si surge el ITSGF | 01–31.07.2026 | 28.07.2026 | AEAT; no sustituye al 714 |
| 303, 130, 111, 115: 3T 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 349: 3T 2026 | 01–20.10.2026 | — | AEAT |
| 202: 2P 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 102: segundo plazo de la Renta 2025 ordinaria con fraccionamiento admisible | Hasta el 05.11.2026 | Plazos propios de gestión de la domiciliación, véase abajo | AEAT; no trasladar este régimen automáticamente al 151 |
| 202: 3P 2026 | 01–21.12.2026 | **16.12.2026** | AEAT; el 20 de diciembre es domingo |
| 111, 115: 4T 2026 | 01–20.01.2027 | 15.01.2027 | Cálculo según la regla vigente; calendario completo de 2027 UNVERIFIED |
| 303: 4T 2026 | 01.01–**01.02.2027** | Previsto 27.01.2027 | La AEAT ya ha publicado el fin de la presentación; la domiciliación de 2027 es calculada |
| 130: 4T 2026; 349: 4T/12M 2026; 390: año 2026 | 01.01–01.02.2027 | Para el 130, previsto 27.01.2027; resto — | Cálculo: el 30 de enero es sábado |
| 190, 180: año 2026 | 01.01–01.02.2027 | — | Cálculo: el 31 de enero es domingo |
| 347: año 2026 | 01.02–01.03.2027 | — | Cálculo: el 28 de febrero es domingo |
| 720, 721: año 2026 | 01.01–31.03.2027 | — | Regla anual vigente; el calendario de 2027 aún no está confirmado |
| 100, 151, 714: año 2026 | Previsto abril–30.06.2027 | Previsto 25.06.2027 | Inicio y calendario definitivo de la campaña **UNVERIFIED** |
| 200: año natural 2026 | Previsto 01–26.07.2027 | Previsto 21.07.2027 | Cálculo: el 25 de julio es domingo; comprobar el calendario aprobado y los festivos |

Fuentes: [calendario anual 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual.html), [domiciliación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [30 de enero](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/enero/hasta-30-enero.html), [2 de febrero](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/febrero/hasta-2-febrero.html), [2 de marzo](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html), [31 de marzo](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-31-marzo.html), [303 hasta el 1 de febrero de 2027](https://sede.agenciatributaria.gob.es/Sede/en_gb/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/calendario-anual/febrero-2027/hasta-1-febrero-2027.html).

Para la campaña de Renta 2025: asistencia telefónica de la AEAT **06.05–30.06.2026**, con cita **29.04–29.06**; asistencia presencial **01.06–30.06**, con cita **29.05–29.06**. Esto no garantiza la atención de un caso empresarial o de régimen Beckham: se aplican criterios de admisión a la asistencia. [Fechas de la campaña](https://sede.agenciatributaria.gob.es/Sede/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/fechas-campana-renta-patrimonio.html).

Gestión del segundo plazo del 102: la **tabla vigente de la AEAT**, en el momento de su consulta, indica para el **02.11.2026** «Hasta 2 de noviembre (para contribuyentes que hayan domiciliado el primer plazo - revocar/rehabilitar o domiciliar)» y para el **20.10.2026** «Hasta el 20 de octubre para modificar el IBAN». En un extracto de búsqueda de esa misma página aparecía una fecha antigua del 30 de septiembre. Se debe usar la página vigente o las instrucciones actuales, y no mezclar estos plazos con la primera domiciliación de la Renta.

### Regímenes mensuales: todos los plazos del año natural 2026

Un volumen pequeño no elimina el 303 mensual cuando existe REDEME/SII por el motivo correspondiente; los 111/115 mensuales surgen, en particular, en las grandes empresas. `M` es el mes de las operaciones; las fechas sin año que figuran abajo corresponden a 2026.

| Periodo | 303: presentar / domiciliación | 111/115: presentar / domiciliación | 349: presentar |
|---|---|---|---|
| 12M 2025 | 30.01 / 27.01 | 20.01 / 15.01 | 30.01 |
| 01M 2026 | 02.03 / 25.02 | 20.02 / 17.02 | 20.02 |
| 02M 2026 | 30.03 / 25.03 | 20.03 / 16.03 | 20.03 |
| 03M 2026 | 30.04 / 27.04 | 20.04 / 15.04 | 20.04 |
| 04M 2026 | 01.06 / 27.05 | 20.05 / 15.05 | 20.05 |
| 05M 2026 | 30.06 / 25.06 | 22.06 / 17.06 | 22.06 |
| 06M 2026 | 30.07 / 27.07 | 20.07 / 15.07 | 20.07 |
| 07M 2026 | 31.08 / 26.08 | 20.08 / 17.08 | **21.09** |
| 08M 2026 | 30.09 / 25.09 | 21.09 / 16.09 | **21.09**, por separado de julio |
| 09M 2026 | 30.10 / 27.10 | 20.10 / 15.10 | 20.10 |
| 10M 2026 | 30.11 / 25.11 | 20.11 / 17.11 | 20.11 |
| 11M 2026 | 30.12 / **24.12** | 21.12 / 16.12 | 21.12 |
| 12M 2026 | Previsto 01.02.2027 / 27.01.2027 | Previsto 20.01.2027 / 15.01.2027 | Previsto 01.02.2027 |

Fuente: [tabla oficial 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [349 en septiembre](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/septiembre/hasta-21-septiembre.html). Las prórrogas temporales por circunstancias extraordinarias prevalecen sobre el calendario básico.

### Import@ss: plazos de cambio de la base en 2025 y 2026

| Fecha de la solicitud | Fecha de efecto de la nueva base |
|---|---|
| 01.01–28.02 | 01.03 del mismo año |
| 01.03–30.04 | 01.05 |
| 01.05–30.06 | 01.07 |
| 01.07–31.08 | 01.09 |
| 01.09–31.10 | 01.11 |
| 01.11–31.12 | 01.01 del año siguiente |

Ninguno de los dos años tratados es bisiesto. Son los plazos de cambio del RETA, no los plazos de presentación de los modelos de la AEAT. Tampoco se garantiza que el plazo se traslade al día hábil siguiente según las reglas de la domiciliación tributaria. Fuente: [TGSS, Base de cotización y rendimientos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos).

## Fórmulas para el motor

### 1. Selección de la obligación y calendario

Entrada: el perfil y sus intervalos de vigencia; el NIF del contribuyente; ejercicio/periodo; obligaciones censales; tipo de operación o retención; REDEME/SII; historial del 349; fecha de cierre del ejercicio económico de la SL; historial de declaraciones aceptadas anteriormente; requerimiento de la AEAT; forma de pago. Salida: la lista de obligaciones con la prueba de que se aplican, el plazo de presentación, el plazo propio de domiciliación y el estado de la fuente.

```text
for each model, tax_period:
    applicable = obligation_rule(model, profile_at_period, activity, transactions, census)
    # La ausencia de pago no significa por sí sola applicable = false.
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

No trasladar los 111/115 al 30 de enero por seguir al 303. Para el 202, crear `1P`, `2P`, `3P` en abril, octubre y diciembre, no `1T–4T`. Para el 200, el plazo legal es de 25 días naturales tras los seis meses siguientes a la conclusión del periodo impositivo, con el traslado previsto; la fecha de julio solo corresponde a un ejercicio económico que coincide con el año natural. Se pueden enviar recordatorios con antelación según un ajuste interno, pero la fecha interna no se debe presentar como plazo legal.

En caso de cambio de domicilio, guardar por separado la fecha real del cambio de domicilio y la fecha de comunicación en el 036. Para el IRPF general, la comunidad se determina según las reglas de residencia habitual del año, no repartiendo el impuesto por meses entre dos comunidades. En el régimen Beckham no hay escala autonómica del IRPF ordinario, pero la dirección y la Comunidad del 151 se deben actualizar igualmente.

### 2. Formatos: registro por modelo y año

**Los enlaces a las especificaciones son parte obligatoria del contrato del generador.** Se eligen según el `ejercicio`, no según la fecha natural de la exportación.

| Modelo | Especificación oficial | Forma de presentación y tipo de estructura |
|---|---|---|
| 303 de 2025 | [DR303e25.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/DR303e25.xlsx), actualizada el 04.12.2025 | Pre303/formulario web con Importar; ancho fijo por páginas con `<T...>` |
| 303 de 2026 | [DR303e26v101.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_26/DR303e26v101.xlsx), actualizada el 28.01.2026 | Igual; dentro del libro la versión figura como `10.01`; no deducir el número de esquema del nombre del fichero |
| 130 de 2025/2026 | [DR130e15v12.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/DR130e15v12.xls), marzo de 2019, versión 1.2 | Formulario, Importar/Exportar `.130`; una página y envoltorio |
| 111 | [dr111e16v18.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/dr111e16v18.xls), mayo de 2021, para 2019+ | [Formulario electrónico con Importar](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-111/presentacion-electronica-modelo-111.html); ancho fijo con envoltorio |
| 349 | [DR_Anexo_349.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_20/DR_Anexo_349.pdf), Orden HAC/174/2020, 2020+ | [Formulario ≤40 000 registros o presentación mediante fichero](https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/identificacion-realizar-operaciones-otros-empresarios-ue/modelo-349.html); tipo 1 declarante + tipo 2 operaciones/rectificaciones |
| 390 de 2025 | [dr390e2025.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/dr390e2025.xlsx), actualizada el 05.12.2025 | [Formulario](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390.html) y [presentación con fichero aparte](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390/modelo-390-presentacion-mediante-fichero.html); estructura de ancho fijo por páginas |
| 190 de 2025 | [DISENOS_LOGICOS_190_2025.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos_25/DISENOS_LOGICOS_190_2025.pdf), Orden HAC/1431/2025 | Formulario ≤40 000 registros o [TGVI online](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/declaraciones-informativas-ayuda-tecnica/modelos-190-198/modelo-190-fichero.html); tipo 1 + tipo 2 perceptores |
| 347 de 2025+ | [347.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos/347.pdf), Orden HAC/1431/2025 | [Formulario ≤40 000 registros o TGVI](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/forma-presentacion.html); tipo 1 + tipo 2 declarados/inmuebles |
| 151 de 2025/2026 | [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), 2023+ | Formulario web propio, Importar/Exportar; nombre de la exportación `NIF_Ejercicio_0A.151` |
| 100 de 2025 | [Renta2025.xsd](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/Renta2025.xsd), [diccionario](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/diccionarioXSD_2025.properties) | Renta WEB; el XML/XSD publicado es otro formato, no el contenedor del 303/130 |

Para el 390 del ejercicio 2026 no se ha encontrado, en la fecha de comprobación, un DR propio confirmado. No se debe presentar el fichero de 2025 con el año cambiado como si fuera admisible con garantía. Para el 190 de 2026, que se actualiza cada año, también hay que volver a comprobar su publicación antes de la campaña. Catálogos: [100–199](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-100-199.html), [300–399](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-300-399.html), [archivo del 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/ejercicios-anteriores-modelos-300-399.html).

En los modelos informativos 349/190/347, los registros de longitud fija se definen en sus PDF, no con la estructura `<T303...>`. Un registro de tipo 1 identifica al declarante, el periodo y los totales de control. Los registros de tipo 2 contienen las contrapartes o perceptores y los registros especiales. No se pueden sustituir por un CSV contable. Las asociaciones de claves y subclaves y los contadores se toman del **DR concreto**, no de los nombres de las columnas del formulario en pantalla. Para el 190, la AEAT advierte expresamente que la primera forma de presentación elegida (formulario o fichero) determina la vía admisible de las presentaciones posteriores; hay que guardar el canal de la declaración original. TGVI puede permitir presentar los registros correctos y corregir después los demás. No se debe considerar presentado todo el conjunto original hasta cotejar los registros aceptados y rechazados.

### 3. Serialización común del 303/130

Abajo figuran las **posiciones comprobadas, contadas desde uno**, las longitudes y los signos. Para un array en un programa, el índice es `position - 1`. La longitud se mide en bytes de la codificación de un byte elegida, no en code points de UTF-8.

```text
format_amount(value_eur, width, signed):
    # La entrada ya viene calculada por el módulo fiscal hasta el céntimo de euro.
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
# Sin separadores CSV, sin BOM UTF-8, sin sangría XML y sin saltos de línea dentro del registro.
```

Fuente de la codificación, la alineación y la `N` para valores negativos: [AEAT, Diseños de registro — breve manual, págs. 4–6, 10–12](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/Ayudas/Disenyos_registro_Manual_uso.pdf). Es un texto posicional, no un documento XML para un serializador XML: los espacios son significativos y no se admite `trim`. Los cálculos monetarios se hacen con Decimal o céntimos enteros; el redondeo final a 0,01 € sigue las reglas de cada casilla. Si la instrucción concreta no indica otra cosa, la convención técnica es decimal ROUND_HALF_UP, cotejada con el formulario de la AEAT. No se debe redondear cada expresión intermedia ni usar float binario.

**El envoltorio tiene las mismas posiciones en los dos DR comprobados:**

| Posición absoluta | Longitud | Contenido |
|---:|---:|---|
| 1 | 2 | `<T` |
| 3 | 3 | `303` o `130` |
| 6 | 1 | `0` |
| 7 | 4 | Ejercicio, por ejemplo `2026` |
| 11 | 2 | Periodo, por ejemplo `3T`; en el 303 mensual, `01`…`12` |
| 13 | 5 | `0000>` |
| 18 | 5 | `<AUX>` |
| 23 | 70 | Espacios, reservado AEAT |
| 93 | 4 | Versión del programa del desarrollador |
| 97 | 4 | Espacios |
| 101 | 9 | NIF del desarrollador según la instrucción del DR |
| 110 | 213 | Espacios |
| 323 | 6 | `</AUX>` |
| 329 | Variable | Páginas del modelo |
| Tras la última página | 18 | `</T3030EEEEPP0000>` o `</T1300EEEEPP0000>` |

Ejemplo de inicio para el 303 del 3T de 2026: `<T303020263T0000><AUX>`; para el 130: `<T130020263T0000><AUX>`. `EEEE`/`PP` son aquí metacaracteres de la explicación, no valores literales del fichero. En el DR130, la descripción del cierre contiene la errata `T1230`, pero la columna **Contenido** indica sin ambigüedad `</T1300AAAAPP0000>`: usar 130.

### 4. Modelo 130: página única totalmente determinada

Tras el envoltorio va la página `DR 13001` de **600 bytes**. Las posiciones indicadas son **locales de la página**; por tanto, su posición 1 está en la posición 329 del fichero completo.

| Posición | Longitud | Campo |
|---:|---:|---|
| 1 | 11 | `<T13001000>` |
| 12 | 1 | Espacio, indicador de página complementaria; no indica que la declaración sea complementaria |
| 13 | 1 | Tipo: `I` ingreso, `U` domiciliación, `G` CCT, `N` negativa, `B` a deducir |
| 14 | 9 | NIF |
| 23 | 60 | Apellidos |
| 83 | 20 | Nombre |
| 103 | 4 | Ejercicio |
| 107 | 2 | `1T`…`4T` |
| 109 + 17×(k−1), k=1…19 | 17 por campo | Casillas `[01]`…`[19]` consecutivas |
| 432 | 1 | `X` para declaración complementaria; si no, espacio |
| 433 | 13 | Número de justificante de la declaración anterior, si es complementaria |
| 446 | 34 | IBAN para la domiciliación, alineado a la izquierda y seguido de espacios |
| 480 | 96 | Reservado AEAT, espacios |
| 576 | 13 | Sello electrónico reservado, espacios |
| 589 | 12 | `</T13001000>` |

Casillas con signo `N`: **03, 07, 11, 14, 17, 19**. Los demás campos monetarios son `Num`, sin valores negativos. En un campo de 17 caracteres hay dos decimales implícitos, sin coma ni punto. Longitud total de una declaración simple: **328 + 600 + 18 = 946 bytes**.

El módulo fiscal entrega los valores calculados de las casillas, y el serializador no los vuelve a calcular. En la complementaria se recalcula todo el periodo. `[18]` es la suma de los resultados **a ingresar** de los 130 anteriores del mismo ejercicio/periodo, no el impuesto de todos los trimestres anteriores; `[19] = [17] − [18]`. Un 130 inicial no presentado lleva `[18]=0`, sin `X` y sin un justificante anterior ficticio. Un resultado cero o negativo no se debe convertir en `I` solo para poder pagar. Fuentes: el DR130 citado arriba y las [instrucciones oficiales del 130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

### 5. Modelo 303 de 2026: páginas y casillas

El libro de trabajo contiene `DP30300`, `DP30301`, `DP30302`, `DP30303`, `DP30304`, `DP30305` y `DP303DID`. Para una actividad ordinaria en régimen general se necesitan los datos de la página 01, del resultado de la página 03 y de la sección de pago DID. La página 02 corresponde al régimen simplificado. La 04 contiene la información anual de los exonerados del 390. La 05 contiene la información correspondiente de prorrata o sectores diferenciados. **Las páginas 04/05 vacías no se incluyen**, según las notas del DR. Para la página 02 aplicable y las páginas repetibles, se deben respetar sus propias condiciones de repetición; no se debe crear para un consultor que no esté en régimen simplificado.

| Página | Inicio / fin | Longitud total | Importante |
|---|---|---:|---|
| DP30301 | `<T30301000>` / `</T30301000>` | 1 581 | NIF, periodo, indicadores y régimen general |
| DP30303 | `<T30303000>` / `</T30303000>` | 1 017 | Información adicional, resultado, rectificativa |
| DP30304 | `<T30304000>` / `</T30304000>` | 998 | Último periodo de los exonerados del 390; no añadir sin datos |
| DP30305 | `<T30305000>` / `</T30305000>` | 1 528 | Prorratas/sectores; no añadir sin datos |
| DP303DID | `<T303DID00>` / `</T303DID00>` | 823 | IBAN/BIC/banco extranjero |

Para la combinación 01 + 03 + DID, la longitud es de **3 767 bytes** con el envoltorio. Es una comprobación estructural de esa combinación, no una prueba de que cualquier valor cero supere la validación de negocio de la AEAT.

**DP30301: las posiciones son locales de la página.** Inicio: posición 12, espacio; 13, tipo de declaración; 14/9, NIF; 23/80, nombre o razón social; 103/4, ejercicio; 107/2, periodo. Los indicadores 109–130 se toman del DR; no se deben rellenar todos con ceros. Por ejemplo, para quien solo tributa en régimen general ordinario, la posición 111 = `3`; SII voluntario, 127; exoneración del 390, 128 (`0` fuera del último periodo; en el último, `1`/`2`); volumen anual, 129 según la condición del DR. La posición 130 es un nuevo campo especial de combustible; para los trimestres y para 01 vale `0`. Su presencia cambia los desplazamientos respecto de algunos esquemas antiguos.

| Casilla | Posición/longitud DP30301 | Tipo |
|---|---|---|
| 01 / 02 / 03 | 209/17; 226/5; 231/17 | Num; tipo `00400` |
| 04 / 05 / 06 | 287/17; 304/5; 309/17 | Num; tipo `01000` |
| 07 / 08 / 09 | 326/17; 343/5; 348/17 | Num; tipo `02100` |
| 10 / 11 | 365/17; 382/17 | Num; adquisiciones intracomunitarias |
| 12 / 13 | 399/17; 416/17 | Num; otros supuestos de inversión del sujeto pasivo |
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
| Reservado + sello | 1036/521; 1557/13 | Espacios |
| Fin | 1570/12 | `</T30301000>` |

Los demás campos, incluidos los de tipo cero y recargo de equivalencia, siguen estando presentes físicamente. Se rellenan **con las constantes y los ceros del DR**; no se eliminan. Para el total de IVA se usan todos los sumandos prescritos, no solo las casillas habituales:

```text
303[27] = [152]+[167]+[03]+[155]+[06]+[09]+[11]+[13]+[15]
          +[158]+[170]+[18]+[21]+[24]+[26]
303[45] = [29]+[31]+[33]+[35]+[37]+[39]+[41]+[42]+[43]+[44]
303[46] = [27] - [45]
```

**DP30303: campos clave del resultado.**

| Casilla/campo | Posición/longitud | Tipo/significado |
|---|---|---|
| 59 | 12/17 | N; entregas y servicios intracomunitarios |
| 60 | 29/17 | N; exportaciones y asimiladas; no incluye automáticamente cualquier servicio fuera de la UE |
| 64 | 199/17 | N; `[46]+[58]+[76]` |
| 65 | 216/5 | Num; % Estado, 100% = `10000` |
| 66 | 221/17 | N; atribuible al Estado |
| 77 | 238/17 | Num; IVA importación pendiente |
| 110 / 78 / 87 | 255/17; 272/17; 289/17 | Num; saldo, parte aplicada, saldo de periodos anteriores |
| 68 | 306/17 | N; regularización Estado/forales |
| 108 | 323/17 | N; ajuste especial por discrepancia; no es una «corrección manual» universal |
| 69 | 340/17 | N |
| 70 | 357/17 | Num; resultados anteriores a ingresar del mismo periodo |
| 109 | 374/17 | Num; devoluciones acordadas por la AEAT del mismo periodo |
| 112 | 391/17 | Num; pagos a cuenta especiales del modelo 319 por combustible, normalmente 0 |
| 71 | 408/17 | N; resultado final |
| Sin actividad | 425/1 | `X` o espacio; un IVA cero no significa automáticamente que no haya actividad |
| Rectificativa | 426/1 | `X` o espacio |
| Justificante anterior | 427/13 | Obligatorio según las condiciones de la rectificativa |
| Modificar o anular la domiciliación anterior | 440/1 | `X` o espacio |
| 111 — importe rectificación | 441/17 | Num; según las reglas de la rectificativa, no el importe total del exceso ingresado |
| Motivo rectificaciones / discrepancia | 458/1; 459/1 | `X` o espacio |
| Reservado / cierre | 460/546; 1006/12 | Espacios / `</T30303000>` |

```text
303[87] = [110] - [78]
303[69] = [66] + [77] - [78] + [68] + [108]
303[71] = [69] - [70] + [109] - [112]
# Declaración ordinaria inicial: [70]=[109]=0; [108]=0 si no hay un motivo especial.
# La aplicación de [78] y la devolución o compensación de un resultado negativo las decide el módulo de IVA.
# No se puede considerar [87] como el nuevo saldo completo: es el saldo de los periodos anteriores.
```

En DID: SWIFT-BIC, posición 12/11; IBAN, 23/34; banco, 57/70; dirección, 127/35; ciudad, 162/30; código país, 192/2; marca SEPA, 194/1 (`0` vacío, `1` España, `2` UE-SEPA, `3` resto); reservado, 195/617; fin, 812/12. El IBAN español son los primeros 24 caracteres con `ES`; el resto del campo son espacios. En una rectificativa con casilla 111>0, los datos bancarios también se exigen en algunas variantes que no son devolución, salvo el caso previsto en el DR de modificación de la domiciliación original.

Tipo del 303: `I` ingreso, `U` domiciliación, `C` compensación, `D` devolución, `N` sin actividad/resultado cero, `G`/`V` CCT, `X` devolución por transferencia al extranjero. Para una rectificativa con `[71]<0` y `[111]>0`, el DR exige determinar el tipo por la parte de `[71]` que no corresponde a `[111]`; no se debe elegir el tipo solo por el signo de `[71]`.

Estos desplazamientos corresponden **solo a DR303e26v101**. Para 2025 se usan las hojas correspondientes de DR303e25. Aquí no se ha generado ni importado en la Sede un fichero de prueba real; la estructura indicada se ha extraído de los libros oficiales, no de una muestra aceptada por el servidor.

### 6. Aceptación, rectificación y pagos

```text
if no accepted_return_for_same_model_year_period:
    mode = ORIGINAL  # incluso fuera de plazo
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

Para el 100 en Renta WEB se usa la opción integrada `Modificar declaración presentada`. Para la rectificativa prevista, se identifica la declaración original y las casillas **103/104** según el manual de 2024, pero **hay que comprobar el diccionario del ejercicio concreto antes de generar**. Para el 200 se usa Sociedades WEB o su DR vigente y el bloque de rectificativa; no se toman los números del 303. Para los informativos 190/180/347/349 se necesitan sus propias operaciones de alta, modificación o baja, complementaria o sustitutiva, o rectificaciones de registros, según el modelo y el canal elegido. No se puede presentar un segundo fichero «ordinario» y considerar anulado el primero.

### 7. Recargo y estimación del retraso

Entrada: el plazo legal original `D`, la fecha real de presentación `F`, el importe no ingresado que resulta de la autoliquidación tardía `B`, la existencia de un requerimiento antes de la presentación, el historial de pagos y los tipos de interés anuales aplicables. Salida: una **estimación** del recargo y de los intereses y la vía de tramitación; no una nueva casilla de la declaración original.

```text
if F <= D:
    late_filing_recargo = 0
elif previous_requerimiento:
    do not apply voluntary_art27_estimate
    route = review assessment/sanction procedure
elif B <= 0:
    recargo_art27 = 0
    route = evaluate formal_penalty_art198  # no significa «no hay sanción»
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

`legally_completed_calendar_months` son meses naturales, **no** `floor(days/30)`. El inicio y el fin del intervalo mensual, los meses sin el día correspondiente y el límite exacto de 12 meses se deben comprobar con el cálculo o la notificación oficial de la AEAT: la redacción pública encontrada repite la ley sin un ejemplo propio para el límite exacto. Hasta esa comprobación, el motor debe mostrar un rango o una advertencia en la fecha límite dudosa, y no inventar un tipo garantizado. Esto no afecta a los casos claros: deuda de 1 000 € y presentación diez días después → recargo de 10 €; con la reducción aplicable → 7,50 €. Pasados más de 12 meses → 150 € más intereses desde la fecha indicada, no intereses de todo el primer año.

Normalmente la AEAT liquida el recargo por separado; **no se debe añadir al resultado de la casilla 19 del Modelo130 ni de la casilla71 del Modelo303**. Si la declaración ya se aceptó en plazo pero el banco no cargó el importe, hay que comprobar el art.28 y las circunstancias del pago, en lugar de presentar un duplicado y calcular el art.27. Las retenciones y algunas otras deudas no admiten el aplazamiento ordinario: que exista la opción de reconocimiento de deuda no da automáticamente derecho al aplazamiento.

## Plazos y modelos

### Quién presenta qué

Aquí «Beckham» significa una opción del art.93 válida y aceptada, con cumplimiento de sus condiciones; no basta con tener un visado de emprendedor. Que un modelo no figure en la lista que lleva una gestoría no prueba que haya exención.

| Modelo | Quién/cuándo | Cuándo no surge / limitación importante | Plazo |
|---|---|---|---|
| 303 | Autónomo de cualquiera de los dos perfiles de IRPF y SL con la actividad sujeta a IVA correspondiente | El régimen Beckham no exime del IVA. Una actividad exclusivamente exenta puede no tener obligación periódica; la inversión del sujeto pasivo y otros hechos se analizan por separado. Si existe obligación periódica, también se presenta el periodo con resultado cero | Trimestre/mes según las tablas |
| 130 | Autónomo en estimación directa; la aplicación a una actividad admitida en el art.93 se decide por las normas especiales, no por la etiqueta del perfil | En actividades profesionales del IRPF ordinario, exención si ≥70% de los ingresos del año anterior tuvieron retención; en el año de inicio, el periodo aplicable. La SL no lo presenta. En el régimen Beckham no se puede incluir ni excluir automáticamente sin reglas por tipo de renta | 1T–3T hasta el día 20; 4T hasta el 30 de enero, con traslado |
| 349 | Cualquiera de los perfiles con las entregas o adquisiciones intracomunitarias de bienes o servicios correspondientes | Las operaciones fuera de la UE no generan por sí solas el 349; sin operaciones que declarar no se presenta a cero. La compra de un SaaS de la UE también puede generar la obligación | Mes/trimestre según su propia prueba |
| 111 | Persona o SL que paga salarios, rendimientos profesionales u otras rentas incluidas con obligación de retener | Son las retenciones **del pagador**, no la retención de las propias facturas emitidas. Si se pagó una renta incluida sin retención efectiva por un tipo cero, puede exigirse una declaración negativa; si no hubo ningún pago, es otro caso | Hasta el día 20 tras el trimestre; mensual para los grandes pagadores correspondientes |
| 115 | Pagador de un arrendamiento empresarial de inmueble urbano sujeto a retención | Comprobar las excepciones y el certificado del arrendador; no todo alquiler de vivienda por un particular genera el 115 | Como el 111 |
| 202 | SL y otros contribuyentes del IS obligados a pagos fraccionados | Para una SL pequeña ordinaria sin importe a ingresar, normalmente no hace falta presentarlo; los grandes contribuyentes tienen reglas especiales de presentación a cero. No crear el 202 para el socio persona física | Abril/octubre/diciembre, no julio |
| 390 | Declaración-resumen anual del IVA para los obligados a presentar declaraciones periódicas de IVA | Exención para el SII y para los obligados trimestrales que solo tributan en régimen simplificado o arrendamiento urbano en territorio común; los datos anuales pasan al último 303. Un consultor ordinario en régimen general no queda exento solo por tener 12 facturas | Hasta el 30 de enero |
| 190 | Pagos y retenciones anuales incluidos, vinculados al 111 | No es un informe de las retenciones que practicaron los propios clientes. Incluir los pagos a cero o exentos correspondientes según las reglas del modelo | Hasta el 31 de enero |
| 180 | Resumen anual de los arrendamientos y retenciones del 115 correspondientes | No surge solo por tener vivienda propia o por ser el que cobra el alquiler | Hasta el 31 de enero |
| 347 | Autónomo/SL con operaciones con terceros incluidas que superen el umbral | Se excluyen las operaciones ya cubiertas por otra información especial con la coincidencia de contenido exigida: por ejemplo, el 349 y las retenciones correspondientes; el SII y otras exclusiones personales. **Un servicio fuera de la UE no equivale a un bien exportado**; la exclusión de las exportaciones no se traslada automáticamente | Febrero del año siguiente |
| 100 | IRPF ordinario del autónomo; el administrador de la SL como persona física, según su propia obligación | Desde 2023, quien haya estado en el RETA en algún momento del año está obligado a declarar el IRPF; pero con el régimen Beckham vigente se aplica el 151 en lugar del 100 ordinario | Campaña de Renta del año siguiente |
| 151 | Régimen especial del art.93 vigente, incluido el administrador o emprendedor correspondiente | No sustituye al 303, a las retenciones ni a las declaraciones de la propia SL. No se concede automáticamente por tener NIE o visado | Plazo de la campaña anual del IRPF; en 2026, hasta el 30 de junio |
| 200 | SL por su propio periodo impositivo | No queda exenta por «no tener actividad» ni por un beneficio cero; mientras exista el sujeto y la obligación del IS, la SL ordinaria presenta | 25 días tras los seis meses siguientes al fin del periodo |
| 714 | Persona física con cuota positiva de Patrimonio o con bienes y derechos superiores a 2 millones de € en el ámbito aplicable | En el régimen Beckham, obligación real por los bienes españoles correspondientes, no automáticamente por el patrimonio mundial. Los mínimos y beneficios autonómicos se calculan por separado | Junto con la Renta; en 2026, hasta el 30 de junio |
| 720 | Residente ordinario o SL con bienes, posiciones y umbrales en el extranjero, sin exclusión | La AEAT exime expresamente a la persona física acogida al art.93. Para una SL o persona física con la debida contabilidad, puede haber exclusiones contables propias. Los bienes personales del administrador y los de la SL se comprueban por separado | 1 de enero–31 de marzo |
| 721 | Criptomonedas en el extranjero en manos de un custodio, posiciones y umbral correspondientes | La autocustodia no se incluye. No se debe deducir una exención propia del régimen Beckham solo del texto de la FAQ720; véase «Cuestiones abiertas» | 1 de enero–31 de marzo |
| 036 | Alta, modificación o baja, domicilio, IAE y obligaciones, ROI, opciones fiscales previstas | No se presenta cada año para confirmar que nada ha cambiado. El 037 ya no se usa | Según el hecho, normalmente un mes; alta/ROI antes de las operaciones; plazos propios para las opciones |
| 102 | Segundo plazo del fraccionamiento 60/40 admisible de la Renta ordinaria | No es un aplazamiento universal para todos los modelos; una autoliquidación inicial fuera de plazo y el 151 requieren reglas propias | 05.11.2026 para la Renta2025 |
| 718 | Persona física cuando surge el Impuesto Temporal de Solidaridad de las Grandes Fortunas | No crearlo automáticamente para todo el que presenta el 714; prueba propia de cuota y ámbito de sujeción | Julio del año siguiente; en 2026, hasta el 31 de julio |

Fuentes primarias de las condiciones: [130, instrucciones](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html), [202, cuándo presentarlo](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/4-impuesto-sobre-sociedades/4_8-pagos-fraccionados/4_8_2-modelos-pagos-fraccionados.html), [390, obligados](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-09-declaraciones-informativas-iva-379/declaracion-resumen-anual-modelo-390/obligados-presentar-declaracion.html), [347, exclusiones](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 y art.93](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes/contribuyentes-obligados-declarar.html), [721](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html). Los cálculos jurídicos de cada impuesto y las condiciones del régimen Beckham se deben tomar del módulo fiscal correspondiente; el calendario no los duplica.

Las obligaciones adicionales se incluyen según el hecho: el 149 en caso de opción, renuncia o exclusión del régimen Beckham; el 123/193 en caso de los pagos de capital correspondientes, por ejemplo dividendos de la SL; el 216/296 en caso de determinados pagos a no residentes. No son obligaciones de todo profesional independiente ni sustituyen a los modelos de la lista. Para que el propio titular presente con una aplicación autoalojada no hace falta la condición de colaborador social; para presentar en nombre de otra persona jurídica se necesitan los apoderamientos debidos.

Para el **149** en 2025–2026: la opción principal, como máximo **6 meses** desde el inicio de la actividad según el alta en la Seguridad Social o el documento admisible; el asociado, el plazo que termine más tarde entre el fin de sus seis meses desde la entrada y el plazo del principal. Renuncia: **noviembre–diciembre del año anterior al año de efecto**; por ejemplo, para renunciar con efecto en 2027, 01.11–31.12.2026. Exclusión: **un mes desde el incumplimiento de las condiciones**; fin del desplazamiento manteniendo la residencia fiscal del año: **un mes desde el fin del desplazamiento**. La presentación del 149 y de sus anexos es un procedimiento propio, no un anexo opcional del 151 anual. Fuentes: [calendario de modelos no periódicos del IRPF 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/impuesto-sobre-renta-personas-fisicas.html), [instrucciones del 149](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-149-irpf-comunicacion-opcion-exclusion_/instrucciones-cumplimentar-comunicacion.html).

### Recorrido práctico del usuario

1. Obtener el certificado FNMT o Cl@ve, cotejar el NIE/NIF y el domicilio en la AEAT; para la SL, el certificado o los apoderamientos del representante. No guardar la clave privada sin protección en el servidor ni entregarla a un marketplace sin formalizar conscientemente la representación.
2. Elegir el modelo, el ejercicio, el periodo y la forma de presentación exactos; exportar el fichero de la versión correspondiente o usar los libros registro en el formato establecido.
3. En la Sede, elegir `Presentación`/`Importar` o la `Presentación mediante fichero` propia, donde exista. La importación web integrada de un fichero no equivale a una API propia. Los modelos 349/190/347 admiten TGVI; el 390, la presentación con fichero propia. Para los modelos 303/130/111 individuales está confirmada la vía ordinaria del formulario con Importar.
4. Cotejar las casillas con los libros, el historial de compensaciones y las declaraciones ya aceptadas; corregir los errores y leer los avisos. Los datos precargados automáticamente en Pre303 pueden no cubrir toda la actividad.
5. Si el resultado es positivo, elegir un medio de pago disponible. Pasado el plazo de domiciliación, todavía se puede presentar dentro del plazo general con un medio de pago admisible; no hay que esperar al trimestre siguiente. El banco extranjero/SEPA y el `Reconocimiento de deuda y pago por transferencia` tienen sus propias condiciones y plazos de abono.
6. `Formalizar ingreso / devolución` → `Firmar y enviar` → guardar por separado el PDF, el CSV, el justificante y la confirmación del pago. Para la transferencia o el reconocimiento de deuda, seguir los pasos pendientes; para la domiciliación, comprobar el cargo efectivo, el rechazo del banco y el saldo.
7. En Import@ss, cotejar por separado el alta en el RETA, los rendimientos y la base, la notificación de regularización y los recibos. Se puede acceder con el certificado, Cl@ve o SMS disponibles, si el número está registrado en la TGSS; tener NIE en la AEAT no garantiza que el teléfono esté vinculado en la TGSS.

## Casos límite

### Impuestos, plazos y presentación

- **Un cliente de la UE, 60 000 € en un trimestre:** el 303 puede seguir siendo trimestral, y el 349 pasar a mensual. El umbral del 349 no se comprueba solo por el número de facturas. Si se supera en el segundo mes, no se puede esperar al fin del trimestre y enviar después un 349 trimestral ordinario.
- **Cliente de EE. UU. y servicio de Irlanda:** la venta no genera el 349, pero la compra puede generarlo. Que no haya IVA español en ninguna de las dos facturas no significa que el régimen sea el mismo. Las operaciones de servicios fuera de la UE se comprueban para el 347 por separado de las exportaciones de bienes.
- **Un cliente español retuvo IRPF de nuestra factura:** su retención entra en nuestros cálculos del IRPF, pero no genera nuestro 111. Si nosotros pagamos a un profesional español una factura con retención, pueden surgir el 111/190.
- **IVA a ingresar cero por tener clientes extranjeros, pero hubo actividad:** no marcar `Sin actividad` automáticamente. Si los gastos fueron mayores, elegir la compensación o devolución correcta, no un simple resultado cero; un 303 negativo sigue siendo una declaración.
- **Baja del autónomo a mitad de año:** se mantienen las obligaciones trimestrales y anuales ya surgidas. En algunos casos se pierde la exención del 390 si ya no se exige el último 303 del año. Una fecha de baja en el RETA no prueba la baja simultánea de todas las obligaciones ante la AEAT.
- **Traslado entre comunidades autónomas:** no cambia los tipos estatales del art.93, pero exige el domicilio y los datos del 151 correctos y una determinación propia de la comunidad para el IRPF ordinario y Patrimonio. No se calcula medio año con una escala autonómica y medio año con otra.
- **Régimen Beckham y familia:** la FAQ720 contiene una antigua observación general de que el régimen no se extiende a la familia. Tras la ampliación del art.93 en 2023, los familiares que cumplan los requisitos pueden ejercer su propia opción. Se comprueba la situación personal de cada uno; no se exime a la esposa solo por el régimen del marido, ni se le niega su propia opción por una frase obsoleta de la FAQ.
- **SL y administrador:** el NIF, las declaraciones, el certificado y los pagos de la SL están separados de los modelos 100/151/714 propios del administrador. No se admite presentar el 200 con los datos de la persona física; el Cl@ve personal no sustituye al certificado de la sociedad.
- **Ha pasado el último día de domiciliación, pero no el plazo general:** no es una presentación extemporánea. Ofrecer el NRC u otro pago admisible; no calcular el recargo por adelantado.
- **Impuesto pagado, pero la conexión se cortó al firmar:** buscar la declaración aceptada y el NRC; no volver a pagar a ciegas. **La firma se completó, pero el cargo no:** buscar la deuda o el estado de la domiciliación; no enviar una declaración duplicada.
- **Rectificación de un 303 aceptado con una domiciliación anterior:** la nueva rectificativa no garantiza la anulación automática del cargo anterior. Comprobar el indicador especial, el plazo de modificación admisible y la confirmación de la AEAT; si no, puede haber un doble cargo o una diferencia incorrecta.
- **Plazo incumplido con requerimiento:** el cálculo voluntario seguro del art27 puede no ser ya aplicable. El requerimiento no es solo una carta en papel: se tienen en cuenta las notificaciones electrónicas practicadas oficialmente. No prometer «solo el 1%».
- **Error de un trimestre anterior detectado tras presentar la anual:** se exige una rectificación coherente del trimestre correspondiente y de la información anual. Aumentar el 303/130 en curso sin vincularlo correctamente al periodo anterior no siempre es una regularización legal.
- **Una declaración informativa aceptó parte de los registros:** guardar los identificadores y los contadores del conjunto aceptado; «fichero enviado» no significa «todas las operaciones del 190/349 aceptadas». Los registros rechazados se corrigen de la forma que admita el canal utilizado.

## Cuestiones abiertas

1. **2027: no está publicado todo el calendario.** Se ha encontrado la confirmación directa del 01.02.2027 para el 303 del 4T 2026. Las demás fechas futuras se han obtenido de los plazos vigentes y de los traslados del calendario, y están marcadas expresamente. El inicio de la Renta2026, su orden anual y los plazos definitivos de domiciliación se deben cargar tras su publicación. No se puede presentar el previsto 7/8 de abril de 2027 como fecha establecida. Un festivo autonómico del 25/26 de julio de 2027 puede afectar al calendario oficial concreto del 200: el cálculo del 26 de julio no es definitivo.

2. **API de Pre303: UNVERIFIED.** Se han revisado las páginas de Pre303, las gestiones, la descripción de las funciones y la ayuda técnica del 303; no se ha encontrado un WSDL/OpenAPI publicado específicamente para Pre303. Esto no prueba que no exista ningún canal de integración cerrado. La vía confirmada para el proyecto es la importación oficial del fichero o de los libros en el formulario y la firma del usuario. No se deben declarar como sustituto admitido de la presentación ni las llamadas HTTP no documentadas ni la API del SII o de VERI*FACTU.

3. **Los ficheros están descritos, pero la importación en el servidor no se ha probado.** Las posiciones en bytes del 303/130 se han extraído de los Excel oficiales; no se han hecho declaraciones de prueba, pagos reales ni presentaciones. Antes de la puesta en producción, el agente principal debe comprobar exportación→importación en el simulador o formulario oficial sin enviar: 2025/2026, ingreso/negativa/compensación, `N` negativos, NIE, Ñ, IBAN, rectificativa. Es una comprobación de compatibilidad obligatoria, no un resultado declarado de esta investigación.

4. **Las versiones del DR y los indicadores condicionales cambian.** En el 303 de 2026 se han detectado campos adicionales de combustible/modelo 319; usar los desplazamientos de 2025 es peligroso incluso para un usuario que no comercia con combustible. El DR del 390 de 2026 no está confirmado. Las exportaciones se deben bloquear si el ejercicio no está admitido, en lugar de usar el «último formato conocido» sin advertencia.

5. **NIF Empresa Desarrollo para un desarrollador autoalojado.** El DR exige el NIFED y la versión SW, pero la instrucción revisada no explica un registro propio del desarrollador para una importación personal aislada. No se debe poner un NIF de proveedor inventado ni afirmar que basta con dejar el campo vacío. Para un desarrollador español propio, usar un NIF válido y comprobarlo con el validador; los requisitos desconocidos de un canal concreto se consultan a la AEAT.

6. **El 721 en el régimen Beckham es una calificación propia no comprobada.** La FAQ720 exime expresamente al art93. La FAQ721 leída enumera los residentes y los criterios de custodia, pero no contiene una aclaración directa equivalente para el art93. No se debe conceder la exención automática del 721 solo por analogía. Si el usuario tiene criptomonedas custodiadas en el extranjero por encima del umbral, se mantiene la posible obligación con revisión manual o consulta previa a la DGT; no se presenta automáticamente una declaración innecesaria «por si acaso».

7. **Límite del mes completo y de los 12 meses en el recargo.** Las fuentes confirman la fórmula, pero no se ha encontrado un ejemplo oficial justo en el límite. La estimación exacta en esas fechas se marca como UNVERIFIED y se coteja con el cálculo o la notificación de la AEAT; los meses no se sustituyen por bloques de treinta días. La tabla de intereses de 2026 confirma el 4,0625%, pero para los años futuros hace falta una versión propia, no una extrapolación.

8. **Conflicto de plazos de domiciliación en las fuentes de la AEAT.** Para el **151**, la tabla del calendario 2026 indica expresamente el **25 de junio**, pero las [instrucciones del 151 para el ejercicio 2023 y siguientes](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html) indican dos veces el **26 de junio**. Una comprobación adicional de la norma primaria resuelve la contradicción a favor del **25.06.2026**: la [Orden HFP/1338/2023, art. 4.2, pág. 5 del PDF](https://www.boe.es/boe/dias/2023/12/15/pdfs/BOE-A-2023-25416.pdf) establece que la domiciliación «podrá realizarse desde el inicio del plazo hasta, con carácter general, cinco días antes de que finalice el plazo de presentación», es decir, el 25 de junio si el fin es el 30 de junio; coincide con el calendario. La fecha del 26 de junio de las instrucciones no se debe usar para admitir una nueva domiciliación del 151 de 2025. Para el **102**, la búsqueda mostraba el 30 de septiembre; la tabla vigente de 2026 leída indica el **02 de noviembre**, con un plazo propio del **20 de octubre** para el IBAN. El documento reproduce la tabla vigente. Antes de cada operación, tomar el plazo normativo vigente y la disponibilidad concreta de la acción en la Sede; no mezclar la presentación inicial con la modificación de un pago ya ordenado.

9. **Este documento no sustituye a los módulos de cálculo de los impuestos.** Enumera completos los modelos solicitados y sus plazos y canales. Pero el derecho al régimen Beckham, la necesidad del 130 para una renta concreta del art93, el cálculo del 714/718, las deducciones autonómicas y la admisibilidad del aplazamiento se determinan por las normas correspondientes, no por la existencia de un botón o de una suscripción. No se debe desactivar un modelo por una incertidumbre: hay que mostrar qué hechos de entrada se necesitan para decidir.
