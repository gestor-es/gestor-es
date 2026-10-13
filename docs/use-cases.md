# Casos de uso

Perfiles: **A** — autónomo + Beckham, **B** — autónomo en el IRPF general, **C** — Sociedad Limitada.
La situación de residencia se elige en el perfil: visado de emprendedor, visado de nómada digital, autorización de residencia por cuenta propia, UE / sin restricciones. Un perfil nuevo empieza como autónomo con visado de nómada digital en el IRPF general (perfil B), el caso más frecuente.
Fuentes de las reglas: `kb/*.md`.

## Cada mes

| # | Escenario | Perfiles | Qué hace el servicio |
|---|---|---|---|
| 1 | Emitir una factura a un cliente extranjero (fuera de la UE) | A B C | Régimen de IVA «no sujeta» según el país del cliente, mención art. 69.Uno.1º, tipo de cambio del BCE en la fecha de la operación (o manual), base y cuota en EUR. El número se asigna al emitir, de forma correlativa y por fechas, con el formato del cuestionario (por ejemplo FACT-{YYYY}-{NNNNN} → FACT-2026-00001). Los datos de las partes quedan fijados en la factura. |
| 2 | Factura a un cliente de la UE (B2B) | A B C | Mención «inversión del sujeto pasivo», casilla 59 del 303, línea con clave S en el 349. Sin el VAT ID y la dirección del cliente, la factura no se emite. |
| 3 | Factura a una empresa española | A B C | IVA 21 %. Retención: 15 % (7 % el año de inicio y los 2 siguientes) — B; 24 % — A; 0 % — C y actividad empresarial. |
| 4 | Corregir una factura emitida | A B C | Solo con factura rectificativa (serie R), con motivo obligatorio y referencia a la factura original. El borrador se puede modificar y eliminar. |
| 5 | Marcar el cobro | A B C | Fecha de cobro en la factura. |
| 6 | Registrar un gasto con justificante | A B C | La categoría fija el % que entra en la base imponible y el % de IVA deducible. El justificante se guarda en `<data>/receipts`. Proveedor de la UE / de fuera de la UE sin IVA → autorrepercusión (10/11 + 36/37 o 12/13 + 28/29). Los equipos de más de 300 € se amortizan (26 % autónomo, 25 % SL). Seguro médico: no más de 500 € al año. Comidas: solo el % que usted indique (límites por día). |
| 7 | Registrar la cuota RETA | A B C | Categoría «Cuota RETA»: B — gasto (casilla 0186); A — no reduce la base del 151; C — retribución en especie del administrador (111). |
| 8 | Pagar a un profesional español o el alquiler de una oficina con retención | A B C | El campo «Retención que usted practicó» del gasto → Modelo 111 (profesionales) o 115 (alquiler). Los anuales 190/180 aparecen en el calendario. |

## Cada trimestre

| # | Escenario | Perfiles | Qué hace el servicio |
|---|---|---|---|
| 9 | Modelo 303 | A B C | Todas las casillas según las operaciones del trimestre, cuotas «a compensar» entre trimestres, solicitud de devolución en el 4T. |
| 10 | Modelo 130 | B | Importe acumulado, 20 %, 5 % gastos de difícil justificación (≤ 2 000 €), minoración art. 110.3.c (sin datos del año anterior: 0), traslado de resultados negativos. No se presenta si en el año anterior ≥ 70 % de los ingresos tuvo retención (solo profesional). |
| 11 | Sin 130 ni 210 con Beckham | A | El 130 no se muestra (si el 130 general se aplica a la actividad dentro del régimen es discutible; ver «Dónde puede equivocarse gestor»). El 210 trimestral no hace falta: es un modelo de no residentes, y un cliente sin presencia en España no practica retención (fuentes: `gestor/sources/beckham.json`). En el resumen aparece el importe «a reservar» según la escala 24 % / 47 %. |
| 12 | Modelo 349 | A B C | Solo si hubo operaciones con la UE: clientes (S) y proveedores (I). Si superan 50 000 € en un trimestre: aviso de presentación mensual. |
| 13 | Modelo 202 | C | Modalidad 40.2: 18 % de la base del último Modelo 200 (se introduce en el perfil; sin ella, estimación según las facturas o recordatorio para introducirla). El primer año no se presenta. |
| 14 | Modelo 111 / 115 | A B C | SL: retención 19 % / 35 % sobre la retribución del administrador y el RETA pagado por la SL (sin volumen de operaciones del año anterior: 35 %). Todos: retenciones practicadas a profesionales y arrendadores. |
| 15 | Marcar la presentación | A B C | Importe de la declaración presentada, fecha, Código Seguro de Verificación (CSV) del justificante de presentación. La marca se puede anular. Los anuales 100/200 solo tienen en cuenta los pagos fraccionados presentados. |

## Cada año

| # | Escenario | Perfiles | Qué hace el servicio |
|---|---|---|---|
| 16 | Modelo 390 | A B C | Declaración-resumen anual de los 303 del año, rectificativas, volumen de operaciones. |
| 17 | Modelo 347 | A B C | Operaciones con terceras personas > 3 005,06 € con IVA, sin las operaciones del 349, sin las operaciones con retención y sin las retribuciones del administrador. |
| 18 | Modelo 100 (estimación) | B | Escala estatal + autonómica del año (Valencia 2025/2026/2027, Asturias 2025/2026 con cuota fija publicada), mínimo personal, reducción por inicio 20 % (si el perfil indica el primer año con rendimiento positivo), menos los 130 presentados y las retenciones. Comunidad: aquella en la que pasó más días del año (art. 72). |
| 19 | Modelo 151 (estimación) | A | 24 % / 47 % sobre todos los ingresos (los gastos y el RETA no reducen la base), menos las retenciones y los 210 pagados voluntariamente según el cuestionario (en [34]/[37]; dónde declararlos después del año del traslado es discutible). |
| 20 | Modelo 200 (estimación) | C | Tipos micro: 2024 — 23 %, 2025 — 21/22 %, 2026 — 19/21 %, 2027 — 17/20 % (el umbral de 50 000 € es proporcional a un primer periodo corto); 15 % empresa emergente; menos los 202 presentados. |
| 21 | RETA: tramo y regularización | A B C | Rendimiento para la SS → tramo → base mín./máx. → regularización esperada (a pagar o a devolver) respecto a la base actual, solo por los meses posteriores a la tarifa plana. Para C: base mínima de societario. Para A: nota de que la TGSS no ha fijado un criterio para el 151. |
| 22 | Cuotas de IVA a compensar entre ejercicios | A B C | Por defecto, en el 4T: solicitud de devolución. Si lo dejó «a compensar», el importe se introduce en el perfil y pasa a la casilla 110 («Cuotas a compensar pendientes de períodos anteriores») del primer trimestre. |
| 23 | Libros registro | A B C | CSV libro de facturas emitidas y recibidas (separador `;`, BOM para Excel). |

## Confianza en las cifras

| # | Escenario | Qué hace el servicio |
|---|---|---|
| 31 | ¿Por qué esta casilla tiene este valor? | Símbolo § en cada casilla, nota y aviso. En la ficha: qué significa, estado (literal en el texto / interpretación / discutible), cita en español, traducción, enlaces al original y a la traducción automática de la página, práctica de la DGT y de los tribunales. |
| 32 | ¿Qué significa este campo? | Debajo de cada campo del cuestionario, de la factura, del gasto y del cliente: en qué influye. Después, cada norma: su contenido en una frase, enlace a la entrada en «Fuentes» y al original. Para la categoría de gasto y el tipo de IVA, el bloque cambia con la selección. |
| 34 | ¿Cómo me ha entendido gestor? | En «Perfil», encima del cuestionario: conclusiones de sus respuestas en frases sencillas; qué declaraciones presenta y por qué le corresponden a usted (con la norma); cuáles no presenta y por qué; dónde la ley no es clara en su caso. |
| 35 | ¿Coincide mi presentación con el cálculo? | El importe de la Sede indicado al marcar «presentada» se compara con el cálculo actual. Si hay diferencia: aviso y enlace a la autoliquidación rectificativa. |
| 36 | ¿Cómo presento y qué hago después? | Cada declaración tiene un bloque «Siguiente paso»: qué hacer ahora (presentar «a ingresar», presentar «sin ingreso», esperar a que se abra el plazo de presentación, presentación fuera de plazo, guardar el justificante de presentación, esperar la regularización de la TGSS) y los enlaces «Cómo presentarlo» (/guide: pasos según la ayuda técnica de la AEAT) y «Abrir en la Sede». Las casillas llevan su nombre en español, como en el formulario; en inglés y en ruso, debajo hay una línea en el idioma de la interfaz. |
| 37 | ¿Puedo evitar volver a teclear las casillas? | «Descargar el fichero para la Sede» en el bloque «Siguiente paso» del 130, 303 (2026), 349 y 151: fichero de texto según el diseño de registro oficial de la AEAT (`gestor/dr/*.json`, extraído con `scripts/dr_extract.py`). En el formulario de la Sede: «Importar», después «Validar declaración» y «Firmar y enviar». El sexo, la fecha de nacimiento, el epígrafe IAE y el teléfono del 151 se toman del cuestionario. La dirección la pedirá el formulario. Los ficheros aún no se han probado en la Sede real. |
| 38 | Ayuda para rellenar el formulario en la Sede | Servidor MCP `gestor/mcp.py` para Claude Code y Codex con la suscripción del usuario: casillas en el formato de la Sede, fichero para «Importar», estado y plazo. El agente rellena el formulario en el navegador y lo comprueba después de «Validar declaración», pero no pulsa «Firmar y enviar». Aún no se ha probado en la Sede real. El mismo servidor guía la primera sesión: el agente rellena el cuestionario, clientes, gastos y borradores de facturas y marca las declaraciones presentadas, siempre después del «sí» del usuario; trabaja con todos los perfiles. No emite facturas: el número lo asigna el usuario en la interfaz. |
| 39 | ¿Coincide mi censo con lo que calcula gestor? | En el cuestionario: fecha del certificado de situación censal y obligaciones en situación de ALTA (303, 130, 111, 115, ROI). En «Cómo le ha entendido gestor»: las diferencias (gestor espera una declaración sin alta, hay alta sin declaración, 349 sin alta en el Registro de Operadores Intracomunitarios). Las modificaciones censales se comunican con el Modelo 036 en el plazo de un mes. El teléfono del cuestionario se incluye en los ficheros del 349 y del 151. |
| 40 | ¿Cuánto he pagado y cuánto queda? | En el resumen, «Impuestos y RETA del año»: columnas por trimestre y del año, tabla modelo × trimestre. Pagado: marcas de presentación (130, 303, 111, 115, 202), 210 por trimestre según el cuestionario, RETA según los gastos. Pendiente: cálculo de gestor, RETA hasta final de año según la última cuota, anual 100/151/200. Para Beckham el total es una horquilla: solo lo facturado, o lo facturado más un trimestre medio del último año. |
| 41 | Interfaz en inglés, ruso y español | El idioma se guarda en el perfil: se elige en el «Cuestionario» o en el menú del perfil (EN RU ES). Por defecto se usa el idioma del navegador. Fichas de fuentes legales: título, contenido y traducción de la cita en el idioma elegido; en español, solo el original. El servidor MCP responde en el idioma del perfil. |
| 42 | Cotejar el extracto bancario | El usuario da el extracto (CSV o Excel) a su propio agente: `/mcp__gestor__statement` en Claude Code o una petición en Codex. El agente coteja los cobros con las facturas y los cargos con los gastos, pregunta por los dudosos y, después del «sí», crea clientes, borradores de facturas y gastos. Para un cobro sin factura: la fecha de operación es cuando se hizo el trabajo y la fecha de expedición es hoy. Un gasto se registra con su factura; la cuota del RETA y las comisiones bancarias, desde el extracto. gestor no guarda el extracto. Hay un aviso en las páginas «Facturas» y «Gastos». |
| 33 | ¿Dónde puede equivocarse gestor? | «Fuentes» empieza por los puntos discutibles e indica qué opción prudente se ha elegido. Cada fuente tiene su fecha de comprobación. |

## Situación de residencia y regímenes

| # | Escenario | Qué hace el servicio |
|---|---|---|
| 24 | Visado de nómada digital | Aviso cuando los clientes españoles superan el 18 % de los ingresos en 12 meses (límite 20 %). |
| 25 | Beckham + nómada / cuenta propia | Aviso: el trabajo por cuenta propia normal = establecimiento permanente → exclusión del régimen. |
| 26 | Fin de Beckham | El último año: aviso. Desde el año siguiente, el servicio pasa por sí mismo al 100/130. |
| 27 | Plazo del Modelo 149 | Recordatorio antes de la fecha «alta RETA + 6 meses». |
| 28 | Traslado entre comunidades autónomas | Líneas «fecha comunidad» en el perfil. La comunidad del año se calcula por días. Para cuenta propia: aviso sobre la vinculación territorial de la primera autorización. |
| 29 | Renovación de la autorización de residencia | 120 días antes de la fecha de caducidad: lista de documentos. |
| 30 | Varios perfiles | Una base de datos por perfil (autónomo personal, SL), selector en la cabecera. |

## Qué no hace (a propósito)

- No presenta declaraciones ante la AEAT: la presentación se hace en la Sede electrónica (Cl@ve / certificado electrónico). gestor da las casillas y el fichero para «Importar». El usuario pulsa «Firmar y enviar».
- No genera registros Verifactu (obligatorio para autónomos desde 01.07.2027; se ha anunciado un aplazamiento a 10.2028).
- No calcula dividendos, ahorro, hijos, hipoteca, deducciones autonómicas, reserva de capitalización, OSS (369), 720/721: solo recordatorios.
- 349: el desglose mensual y los registros de rectificación de periodos anteriores se hacen a mano (el servicio avisa).
