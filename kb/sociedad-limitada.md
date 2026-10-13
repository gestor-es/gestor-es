# Sociedad Limitada (SL/SLU) с одним socio-administrador: налоги, отчётность, учёт

Дата актуальности: 2026-10-08. Область: сервисная SL/SLU с одним socio-administrador — налоговым резидентом Испании; внутренние и трансграничные B2B-операции; INCN заведомо < 1 000 000 €. Примеры условные.

## Кратко

- IS (Impuesto sobre Sociedades) платит сама SL, а не socio. Общая ставка 25 %, но для «микропредприятия» (INCN предыдущего периода < 1 M€) действует переходная шкала: **2025 — 21 % до 50 000 € базы / 22 % остальное; 2026 — 19 % / 21 %; 2027 и далее — 17 % / 20 %** (art. 29.1 + DT 44ª LIS, Ley 7/2024). Для ERD с INCN 1–10 M€: 24 % (2025), 23 % (2026), 22 % (2027), 21 % (2028), 20 % (2029+).
- Entidad de nueva creación (ENC): 15 % в первом периоде с положительной базой и в следующем. **Не применяется, если ту же деятельность в предыдущем году вёл как физлицо человек, владеющий > 50 % новой SL** — т.е. автономо, «переливающий» свой бизнес в свою SL, 15 % не получит.
- Empresa emergente (Ley 28/2022): 15 % четыре периода, отсрочка IS без процентов, нет pagos fraccionados — только при сертификации ENISA; для одиночной сервисной SL практически недостижимо.
- Три modelo 202 (1–20 апреля, октября, декабря) по умолчанию = 18 % от cuota последнего поданного modelo 200 (минус retenciones). Если она ≤ 0 (в т.ч. первый год) — 202 не подаётся вообще. Опция art. 40.3 (по текущей базе) — через 036 в феврале.
- Modelo 200 — всегда, даже при убытке/нулевой активности: 1–25 июля (за 2025 → до **27.07.2026**, domiciliación до 22.07.2026).
- Вознаграждение administrador «за должность»: retención фикс. **35 %**, или **19 %**, если INCN последнего закрытого периода < 100 000 €; modelo 111 + 190 (clave E). Если socio лично оказывает SL профессиональные услуги (sección 2ª IAE, напр. 763 программисты) и состоит в RETA — по art. 27.1 LIRPF это **actividad económica**: он выставляет SL счёт с retención 15 % (7 % первые 3 года), не nómina.
- Дивиденды: retención 19 %, modelo 123 (квартал) + 193 (январь). У получателя — base del ahorro 19/21/23/27/30 %. Под Beckham дивиденды испанской SL — испанский источник, облагаются по той же шкале ahorro в modelo 151.
- Beckham + SL: вход через должность administrador возможен при любой доле (ограничение < 25 % только для entidad patrimonial); доход от своей SL как профессионал (art. 27.1) = actividad económica → допустим только при входе по «emprendedor»-основанию (93.1.b.3º). Регион для IS и для Beckham значения не имеет.
- Registro Mercantil: legalización de libros ≤ 4 мес. после закрытия года (30 апреля), formulación cuentas ≤ 3 мес. (31 марта), aprobación ≤ 6 мес. (30 июня), depósito ≤ 1 мес. после утверждения (≈ 30 июля) + hoja de titularidad real. Штраф ICAC за недепозит 1 200–60 000 €, cierre registral через год.
- RETA autónomo societario: мин. база 1 000 € (2025) → **1 424,40 € (2026, окончательно после регуляризации)**; взнос ≈ 314 €/мес (2025) → ≈ 449 €/мес (2026). Если платит SL — это retribución en especie администратора (DGT V0067-19, V2121-25).
- Verifactu для плательщиков IS юридически с 01.01.2027 (RDL 15/2025); 05.10.2026 Hacienda анонсировала перенос на октябрь 2028 — пока не в BOE.
- Экономика: при полной выплате прибыли SL выигрывает у autónomo (обычный IRPF) примерно с 90–100 k€ выручки; при 60 k€ — паритет/минус. Под Beckham (24 % flat) autónomo выгоднее SL во всех сценариях, кроме реинвестирования прибыли внутри SL.

## Правила

1. **Субъект и период.** SL — contribuyente IS с момента приобретения правосубъектности; период = ejercicio social (обычно год), заканчивается 31.12; первый период — от даты escritura до 31.12 (sociedad en formación, впоследствии зарегистрированная, облагается IS с даты escritura). Действует постоянно. Ley 27/2014 (LIS) art. 7, 27: https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328
2. **Ставки IS** (периоды, начавшиеся в 2025/2026/2027): см. таблицу в «Цифры». Микропредприятие = INCN *предыдущего* периода < 1 M€ и не entidad patrimonial; порог 50 000 € пропорционально уменьшается, если период < 12 мес. LIS art. 29.1, DT 44ª (ред. Ley 7/2024 DF 8ª): https://www.boe.es/buscar/act.php?id=BOE-A-2024-26694 ; таблица AEAT: https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades/que-base-imponible-se-determina-sociedades/tipo-impositivo.html
3. **ENC 15 %** (art. 29.1 párr. 2): первый период с BI > 0 и следующий; исключения — entidad patrimonial, группа art. 42 CCom, деятельность ранее велась vinculada-лицом, либо в году до учреждения велась физлицом, которое потом владеет > 50 %. Если законом положена более низкая ставка — применяется она. Критерий TEAC: условия проверяются на devengo каждого из двух периодов.
4. **Empresa emergente** (Ley 28/2022 art. 7–8): 15 % в первом периоде с BI > 0 и трёх следующих, aplazamiento 12 и 6 мес. без гарантий и процентов, освобождение от pagos fraccionados за 2 следующих периода — только при наличии статуса, сертифицированного ENISA и вписанного в RM. https://www.boe.es/buscar/act.php?id=BOE-A-2022-21739 ; AEAT: https://sede.agenciatributaria.gob.es/Sede/impuesto-sobre-sociedades/novedades-impuesto-sobre-sociedades/novedades-normativa________.html
5. **Reserva de capitalización** (art. 25 LIS, с 01.01.2025): уменьшение BI на 20 % прироста fondos propios (23 / 26,5 / 30 % при росте средней численности на ≥2 %, ≥5 %, >10 %, удерживаемом 3 года); лимит 20 % положительной BI previa (25 %, если INCN < 1 M€); остаток переносится на 2 следующих периода; прирост FP и indisponible-резерв держать 3 года. В прирост FP не входят результат года, взносы socios, reserva legal/estatutaria, reserva de nivelación. https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/principales-novedades-impuesto-sobre-sociedades-2025/reserva-capitalizacion.html
6. **Reserva de nivelación** (art. 105 LIS): только ERD (в т.ч. микро по шкале art. 29.1 párr. 1; **не** ENC на 15 %): минус до 10 % положительной BI (≤ 1 M€), обязательная indisponible-резерва; добавляется обратно против BIN следующих 5 лет, остаток — в 5-м году. Учитывается и в pagos fraccionados 40.3. https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/capitulo-10-regimenes-tributarios-especiales-ii/regimen-especial-empresas-reducida-dimension/incentivos-fiscales/reserva-nivelacion.html
7. **BIN** (art. 26): компенсация до 70 % BI previa, но не менее 1 M€ в год — для нашей SL фактически без лимита; перенос бессрочный.
8. **Невычитаемые расходы** (art. 15 LIS): retribución de fondos propios (дивиденды), сам IS, штрафы/санкции/recargos, donativos y liberalidades (кроме atenciones a clientes ≤ 1 % INCN и promoción), расходы contrarios al ordenamiento, операции с «paraísos». Вознаграждение administrador за функции alta dirección/по трудовому договору — не liberalidad по прямому тексту 15.e). ТС (STS 13.03.2024 rec. 9078/2022; 30.04.2024 rec. 7481/2022; 13.06.2024 rec. 78/2023): отсутствие статутной оговорки само по себе не делает реальное, учтённое вознаграждение невычитаемым; осторожная практика — статуты «cargo retribuido» + решение socio único о сумме (art. 217 LSC). https://www.boe.es/buscar/act.php?id=BOE-A-2014-12328 ; обзор ТС: https://www.poderjudicial.es/stfls/TRIBUNAL%20SUPREMO/ACUERDOS%20y%20ESTUDIOS%20DOCTRINALES/FICHERO/20240722%20Cr%C3%B3nicaJurisprudencia%202023-2024%20Sala%203.pdf
9. **Amortización** (art. 12, 102, 103 LIS): по таблице art. 12.1 (equipos para procesos de información 25 %/8 лет, software 33 %/6, mobiliario 10 %/20, equipos electrónicos 20 %/10); ERD — ускоренная ×2 коэффициент; bienes de escaso valor ≤ 300 €/ед. свободно, до 25 000 €/год; libertad de amortización при росте численности (120 000 € × Δ плантилья).
10. **Operaciones vinculadas** (art. 18 LIS): socio ≥ 25 % и administrador — vinculados (кроме оплаты за саму должность). Оценка по рынку; safe harbour для socio-profesional (18.6): ≥ 75 % доходов SL — профессиональные, ≥ 75 % результата до вычета этих выплат идёт socios, каждому ≥ 1,5× средней зарплаты аналогов или ≥ 5× IPREM. **Modelo 232** (1–30 ноября) обязателен, если операции одного типа и метода с vinculados > 50 % INCN — для одиночной SL, платящей socio как профессионалу, это почти всегда так. https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2025/capitulo-08-operaciones-personas-entidades-vinculadas/obligaciones-informacion/informacion-sobre-operaciones-vinculadas-modelo-232/obligados-presentar-modelo-232.html
11. **Pagos fraccionados** (art. 40 LIS): modalidad 40.2 — 18 % от (cuota íntegra − deducciones − bonificaciones − retenciones − ingresos a cuenta) последнего 200, срок подачи которого истёк к 1 апреля/октября/декабря; при результате ≤ 0 подавать не нужно (кроме INCN > 6 M€). Modalidad 40.3 — опция через 036 в феврале (обязательна при INCN > 6 M€): база за 3/9/11 месяцев, процент = floor(5/7 × ставка). https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-sociedades/modelo-202-is-i_____resencia-territorio-fraccionado_/instrucciones/Instrucciones-para-2025.html
12. **Modelo 200** (art. 124): 25 календарных дней после 6 месяцев с конца периода; при годе = календарному — 1–25 июля (перенос на ближайший рабочий день). Подаётся всегда, включая убыток, ноль, бездействие. https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/4-impuesto-sobre-sociedades/4_9-declaracion/4_9_1-plazo-presentacion.html
13. **Retención administrador** (art. 101.2 LIRPF, art. 80.1.3º RIRPF): 35 %; 19 %, если INCN последнего периода, закрытого до выплаты, < 100 000 € (ровно 100 000 — уже 35 %). Modelo 111 квартал, 190 годовой clave E (E.01/E.02 — asimilado cuenta ajena; E.03 — в RETA и INCN < 100k; E.04 — остальные). https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026.pdf
14. **Socio-profesional** (art. 27.1 párr. 3 LIRPF): если SL оказывает профессиональные услуги sección 2ª IAE, socio выполняет для неё эти же услуги и состоит (или обязан состоять — STS 1250/2025) в RETA, его доход от SL = rendimientos de actividades económicas: счёт SL с retención 15 % (7 % год начала и два следующих, по письменному уведомлению), 111/190 clave G; IVA 21 % по умолчанию (см. «Неясности»). https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c06-rendimientos-actividades-economicas-cuestiones-generales/concepto-rendimientos-actividades-economicas.html ; DGT V1500-15 (программист, epígrafe 763): https://www.iberley.es/resoluciones/resolucion-vinculante-dgt-v1500-15-18-05-2015-1416571
15. **RETA, оплаченная SL** — retribución en especie администратора/socio (dineraria, если деньги отдали ему): входит в базу retención, отражается в 190, у получателя вычитается как SS. DGT V0067-19, V2121-25: https://bm.consulting/es/consultas-vinculantes/V2121-25/
16. **Дивиденды** (art. 101.4 LIRPF, 25.1.a): retención 19 %, modelo 123 (1–20 апреля/июля/октября/января), 193 (1–31 января; за 2025 — до 02.02.2026). https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/7-otras-obligaciones-fiscales-retenciones/7_4-retenciones-capital-mobiliario-modelos-193.html
17. **Аренда офиса** у физлица/юрлица: retención 19 %, modelo 115 (квартал) + 180 (январь); не нужна, если аренда ≤ 900 €/год одному арендодателю или арендодатель в IAE epígrafe 861 с cuota > 0 (крупные арендодатели), или это leasing. Art. 75.3.g RIRPF.
18. **Beckham и administrador** (art. 93.1.b.2º LIRPF, ред. Ley 28/2022): назначение administrador — основание переезда при любой доле, кроме entidad patrimonial (тогда доля < 25 %). Основание 93.1.b.3º (actividad emprendedora) — единственное, допускающее доход через EP/actividad económica; для visa de emprendedor (Ley 14/2013 art. 70) требование «informe ENISA» считается выполненным (art. 113 RIRPF). Дивиденды и зарплата от испанской SL — испанский источник → облагаются в modelo 151. https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c02-irpf-cuestiones-generales/sujecion-irpf-aspectos-personales/regimen-fiscal-especial-aplicable-trabajadores-desplazados/regimen-aplicable-trabajadores-desplazados/ambito-aplicacion.html
19. **Registro Mercantil — libros** (art. 18 Ley 14/2013, Instrucción DGRN 12.02.2015): все обязательные книги (Diario, Inventarios y Cuentas Anuales, Actas, Registro de socios, Registro de contratos socio único–sociedad) легализуются телематически в электронном формате не позднее 4 месяцев после закрытия года. https://www.boe.es/buscar/doc.php?id=BOE-A-2015-1481
20. **Cuentas anuales** (LSC art. 253, 164, 279, 282, 283): formulación ≤ 3 мес., aprobación junta ≤ 6 мес., depósito ≤ 1 мес. после утверждения; модели PYME/abreviado при 2 из 3 порогов (activo ≤ 4 M€, INCN ≤ 8 M€, ≤ 50 работников); hoja de titularidad real вместе с depósito (RD 609/2023), изменения титульного владельца — в RM в течение 10 дней. Санкция 1 200–60 000 €; cierre registral по art. 378 RRM через год без депозита. https://boe.es/buscar/act.php?id=BOE-A-2010-10544 ; https://www.boe.es/eli/es/rd/2023/07/11/609
21. **SLU** (LSC art. 12–17): унипersonalidad регистрируется в RM и указывается во всех документах («SLU»); решения socio único — в acta; контракты socio único ↔ SL — письменно и в libro-registro de contratos, упоминание в memoria; иначе не противопоставимы при банкротстве, socio отвечает за выгоды из них 2 года.
22. **Capital** (Ley 18/2022 «Crea y Crece»): минимум 1 €; при капитале < 3 000 € — 20 % прибыли в reserva legal, пока капитал + RL ≥ 3 000 €, и солидарная ответственность socios до 3 000 € при ликвидации; иначе reserva legal 10 % прибыли до 20 % капитала (art. 274 LSC).
23. **036**: alta/NIF provisional (casillas 110/111) до начала операций, NIF definitivo (casilla 120) после регистрации в RM; IAE epígrafe (casilla 402) — SL в sección 1ª (напр. 845 «Explotación electrónica por cuenta de terceros» или 843.9); освобождение от IAE первые 2 периода и пока INCN < 1 M€; обязанности retenedor (111/115/123) активировать только когда реально возникают; ROI (349) при услугах контрагентам ЕС; опция 40.3 — casilla 621 (alta) в феврале. https://sede.agenciatributaria.gob.es/Sede/Ayuda/guia-practica-declaracion-censal.html
24. **IVA/347/349** — те же правила, что у autónomo (см. kb KbIva): 303 квартал, 390 январь, 349 по операциям ЕС, 347 февраль (контрагенты > 3 005,06 €, не вошедшие в 349/190/180). Разница: на счета SL за услуги испанские клиенты **не** удерживают IRPF (retención на профессиональные услуги применяется только к физлицам).
25. **Verifactu / factura electrónica**: RD 1007/2023 для плательщиков IS — адаптация до 01.01.2027 (RDL 15/2025); нота Hacienda 05.10.2026 анонсирует перенос на октябрь 2028 (не опубликовано в BOE). B2B e-factura (RD 238/2026, Orden HAC/1028/2026): INCN > 8 M€ с 06.10.2027, остальные с 06.10.2028, только для операций между испанскими empresarios. https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html ; https://boe.es/diario_boe/txt.php?id=BOE-A-2026-20587

## Цифры

### Ставки IS по году начала периода

| Контрибуйент | 2025 | 2026 | 2027 | 2028 | 2029+ |
|---|---|---|---|---|---|
| Общая | 25 % | 25 % | 25 % | 25 % | 25 % |
| Micropyme (INCN пред. < 1 M€), BI ≤ 50 000 € | 21 % | 19 % | 17 % | 17 % | 17 % |
| Micropyme, BI > 50 000 € | 22 % | 21 % | 20 % | 20 % | 20 % |
| ERD (1 M€ ≤ INCN < 10 M€) | 24 % | 23 % | 22 % | 21 % | 20 % |
| ENC (2 периода) | 15 % | 15 % | 15 % | 15 % | 15 % |
| Empresa emergente (4 периода) | 15 % | 15 % | 15 % | 15 % | 15 % |
| Entidad patrimonial | 25 % | 25 % | 25 % | 25 % | 25 % |

2027–2029 — по тексту DT 44ª / art. 29.1 Ley 7/2024 (таблица AEAT показывает только 2024–2026).

### Pagos fraccionados (modelo 202)

| Параметр | Значение |
|---|---|
| Сроки | 1–20 апреля (1/P), 1–20 октября (2/P), 1–20 декабря (3/P); domiciliación 1–15 |
| 40.2 | 18 % базы |
| 40.3, INCN < 10 M€ | floor(5/7 × tipo): 25 % → 17 %; micro 2025 21/22 → 15/15; micro 2026 19/21 → 13/15; micro 2027 17/20 → 12/14; ENC 15 % → 10 % |
| 40.3 минимальный платёж 23 % | только INCN ≥ 10 M€ — не применимо |
| Обязательная 40.3 / подача при нуле | INCN > 6 M€ — не применимо |

### Reservas

| | Значение |
|---|---|
| Reserva de capitalización, % от ΔFP | 20 % (23 % / 26,5 % / 30 % при Δ плантилья ≥2 / ≥5 / >10 %) |
| Лимит | 20 % BI previa; 25 % при INCN < 1 M€; остаток 2 года |
| Удержание ΔFP и резерва | 3 года |
| Reserva de nivelación | ≤ 10 % BI, ≤ 1 M€, реверс 5 лет |

### Retenciones (2025 и 2026 без изменений)

| Доход | Тип | Модели |
|---|---|---|
| Administrador за должность, INCN пред. ≥ 100 000 € | 35 % | 111 / 190 E.01, E.04 |
| Administrador за должность, INCN пред. < 100 000 € | 19 % | 111 / 190 E.02, E.03 |
| Трудовой доход (не администратор) | по алгоритму art. 80–89 RIRPF | 111 / 190 A |
| Профессиональный счёт socio (art. 27.1) | 15 % (7 % первые 3 года) | 111 / 190 G |
| Дивиденды | 19 % | 123 / 193 |
| Аренда помещения | 19 % | 115 / 180 |
| Проценты по счёту (банк удерживает у SL) | 19 % | casilla 01785 modelo 200 |

### IRPF получателя (base del ahorro, с 2025 по Ley 7/2024, одинаково для residentes и Beckham)

| Тramo | Ставка | Накопленная cuota на верхней границе |
|---|---|---|
| до 6 000 € | 19 % | 1 140 |
| 6 000–50 000 | 21 % | 10 380 |
| 50 000–200 000 | 23 % | 44 880 |
| 200 000–300 000 | 27 % | 71 880 |
| > 300 000 | 30 % | — |

Beckham: rendimientos del trabajo (зарплата administrador) 24 % до 600 000 €, 47 % выше.

### RETA autónomo societario

| | 2025 | 2026 |
|---|---|---|
| Мин. база (после 90 дней alta) | 1 000,00 € | 1 424,40 € (= мин. grupo 7 RG; окончательно при регуляризации) |
| Тип | 31,4 % | 31,5 % |
| Мин. взнос/мес | ≈ 314 € | ≈ 448,69 € |

Источник: Seg. Social BNR 5/2026: https://www.seg-social.es/wps/wcm/connect/wss/61f4db39-8366-4d8f-863b-34332b1d527a/BNR%2B5_2026.pdf?MOD=AJPERES (детали — kb RETA).

### Registro Mercantil / cuentas (год = календарный)

| Обязанность | Срок |
|---|---|
| Legalización libros | 30 апреля |
| Formulación cuentas | 31 марта |
| Aprobación (socio único) | 30 июня |
| Depósito + titularidad real | ≤ 1 мес. после утверждения (≈ 30 июля) |
| Cierre registral | через 1 год без депозита |
| Санкция ICAC | 1 200–60 000 € (0,5 ‰ активов + 0,5 ‰ продаж; −50 % при добровольной сдаче до expediente) |
| Модель PYME/abreviado | 2 из 3: activo ≤ 4 M€, INCN ≤ 8 M€, ≤ 50 работников |

### Прочие пороги

| | |
|---|---|
| Modelo 232 | > 250 000 € с одним vinculado; или операции одного типа/метода > 50 % INCN; или específicas > 100 000 € |
| Modelo 347 | > 3 005,06 €/контрагент/год |
| IAE | освобождение 2 первых периода и при INCN < 1 M€ |
| 720 (SL) | не требуется, если иностранные активы индивидуально отражены в учёте |
| Capital mínimo | 1 € (reserva legal 20 % пока capital+RL < 3 000 €) |

## Формулы для движка

Все деньги — в центах или Decimal; итоговые суммы в casillas — евро с 2 знаками, округление half-up (инструкция 202: «mitad de céntimo → cifra superior»).

### 1. Параметры периода

```
period = {start, end}                      # первый период: start = fecha escritura
days = (end - start).days + 1
is_full_year = days >= 365
incn_prev = INCN предыдущего периода (0/None, если периода не было)
```

### 2. Выбор ставки

```
def rate_schedule(year, incn_prev, enc_window, startup_certified, patrimonial, days):
    if startup_certified:           return [(INF, 0.15)]
    if enc_window and not patrimonial: return [(INF, 0.15)]
    if patrimonial:                 return [(INF, 0.25)]
    if incn_prev is None or incn_prev < 1_000_000:
        t1, t2 = {2025:(0.21,0.22), 2026:(0.19,0.21)}.get(year, (0.17,0.20))
        tramo = 50_000 * min(days,365)/365          # прорратео, если период < года
        return [(tramo, t1), (INF, t2)]
    if incn_prev < 10_000_000:
        return [(INF, {2025:0.24, 2026:0.23, 2027:0.22, 2028:0.21}.get(year, 0.20))]
    return [(INF, 0.25)]

# enc_window: True в первом периоде с BI>0 и в следующем за ним периоде,
# если entity.is_new_creation and not activity_previously_by_owner_gt50 and not grupo42.
# Состояние: enc_periods_used ∈ {0,1,2}; инкремент в конце периода, если применяли 15 %.
```

Для «первый период с BI > 0» решение принимается после расчёта BI (01330); если BI ≤ 0 — ENC-окно не стартует.

### 3. Modelo 200 — цепочка casillas

```
C00500 = resultado P&G (после IS)                       # из учёта: saldo 129 после 630
C00501 = resultado antes de IS                          # C00500 + gasto IS (630) 
ajustes_pos = Σ невычитаемые (art.15): sanciones, liberalidades, gasto IS(630 → C00301/00302 в 200),
              exceso amortización contable над fiscal, provisiones no deducibles...
ajustes_neg = Σ amortización fiscal acelerada сверх contable (ERD ×2, escaso valor, libertad)...
C00550 = C00500 + ajustes_pos − ajustes_neg             # BI antes RC y BIN

# Reserva de capitalización (только если C00550 > 0)
dFP = FP_fin − FP_inicio, где FP = capital + prima + reservas voluntarias (+ RC прошлых лет),
      исключая resultado ejercicio, aportaciones socios, reserva legal/estatutaria, reserva nivelación
pct_rc = 0.20 (0.23/0.265/0.30 по Δ плантилья)
rc_derecho = max(0, dFP) * pct_rc + rc_remanente_anterior(≤2 года)
lim_rc = C00550 * (0.25 if incn_prev < 1_000_000 else 0.20)
C01032 = min(rc_derecho, lim_rc, C00550)
rc_remanente_nuevo = rc_derecho − C01032

# BIN
lim_bin = max(0.70 * (C00550 − C01032), 1_000_000)
C00547 = min(BIN_pendientes, lim_bin, C00550 − C01032) if C00550 − C01032 > 0 else 0
C00552 = C00550 − C01032 − C00547                        # Base imponible

# Reserva de nivelación (ERD, не ENC-15 %)
if C00552 > 0 and erd and not enc_window:
    C01034 = min(0.10 * C00552, 1_000_000 * min(days,365)/365)   # disminución (опция, по решению)
    C01033 = 0
elif C00552 < 0:
    C01033 = min(−C00552, niv_pendiente)                  # aumento: реверс прошлых минораций
    C01034 = 0
# + принудительный реверс остатка, которому исполнилось 5 лет → C01033
C01330 = C00552 + C01033 − C01034                         # BI después de reserva de nivelación

# Cuota
C00558 = tipo(s)                                          # для micro — оба tramos
C00562 = Σ_tramos max(0, min(C01330, lim) − prev) * t     # cuota íntegra (0, если C01330 ≤ 0)
C00582 = C00562 − bonificaciones − DDI (обычно 0)
C00592 = C00582 − otras deducciones (обычно 0)            # cuota líquida
C01785 = retenciones capital mobiliario (банк. проценты)
C01787 = retenciones arrendamientos (если SL сдаёт)
C01766 = Σ retenciones
C00599 = C00592 − C01766
C00601, C00603, C00605 = pagos fraccionados 1/P, 2/P, 3/P
C00611 = C00599 − C00601 − C00603 − C00605                # cuota diferencial
C00621 = C00611 (+/− rectificativa)                       # resultado: >0 ingresar, <0 devolver
```

Проводки/резервы, которые движок обязан предложить после утверждения результата: dotación reserva de capitalización = C01032; dotación reserva de nivelación = C01034 (обе indisponibles); страница 20 bis — таблицы RC/RN по годам генерации.

### 4. Modelo 202 — modalidad 40.2 (по умолчанию)

```
def pago_202_402(mes, year):
    # последний 200, срок которого истёк к 1-му числу mes:
    ref_year = year − 2 if mes == 4 else year − 1
    m200 = filed_200[ref_year]           # None → base = 0 → не подавать
    if m200 is None: return NO_FILING
    if not m200.full_year:  # период < 365 дней → суммировать cuotas предыдущих периодов до 365 дней
        base = Σ cuotas периодов (пропорция для самого дальнего: días_restantes/duración × cuota)
    else:
        base = m200.C00562 − deducciones − bonificaciones − m200.C01766   # casilla [01]
    importe = round_half_up(0.18 * base, 2)                              # casilla [03]
    return NO_FILING if importe <= 0 else importe
```

Первый год SL: `filed_200` пуст → ни одного 202. Второй год: апрель — пусто (200 за год 1 ещё не подан), октябрь и декабрь — 18 % от cuota года 1.

### 5. Modelo 202 — modalidad 40.3 (опция; выгодна, если текущий год хуже прошлого)

```
def pago_202_403(mes, year, ledger):
    meses = {4:3, 10:9, 12:11}[mes]
    C04 = resultado contable 1.1–конец meses (после IS)
    C05/C06 = корр. по IS; C07/C08 = прочие ajustes
    C13 = C04 + C05 + C07 − C06 − C08                     # BI previa
    C44 = remanente RC прошлых лет (текущую RC применять нельзя)
    C14 = min(BIN, 0.70*(C13−C44) …) если C13−C44 > 0
    C45/C46 = reserva de nivelación (aumento/disminución), как в п.3
    C16 = max(0, C13 − C44 − C14 + C45 − C46)
    tramos = rate_schedule(...);  pct_i = floor(5/7 * t_i * 100)/100   # 21→15, 22→15, 19→13, 21→15, 15→10, 25→17
    cuota = Σ_tramos (часть C16 в tramo_i) * pct_i                    # tramo 50k прорратируется по meses/12? — см. Неясности
    importe = cuota − retenciones_ytd − pagos_202_ytd
    return NO_FILING if importe <= 0 else round_half_up(importe, 2)
```

Выбор: в феврале (036 casilla 621) — если прогноз BI_текущего × ставка × 5/7 заметно < 18 % cuota прошлого года.

### 6. Retenciones administrador / socio

```
def retencion_admin(pago_bruto, incn_last_closed):
    pct = 0.19 if (incn_last_closed is not None and incn_last_closed < 100_000) else 0.35
    return round(pago_bruto * pct, 2)
# RETA, оплаченная SL: especie = cuota_RETA; base_retención += especie; ingreso a cuenta = especie*pct (если не repercutido)
# 111: casilla 01 nº perceptores, 02 importe (dinerario), 03 retenciones; especie → 04/05/06
# 190: clave E, subclave E.03 (RETA, INCN<100k) / E.04; percepción íntegra dineraria + en especie отдельно

def retencion_profesional(base_sin_iva, inicio_actividad_year, year, comunicado_7):
    pct = 0.07 if comunicado_7 and year <= inicio_actividad_year + 2 else 0.15
    return round(base_sin_iva * pct, 2)         # 111 (apartado "actividades económicas"), 190 clave G
```

Если socio под Beckham получает зарплату от SL: retención 24 % (47 % > 600 000 €) по правилам IRNR; декларируется в 111/190 (см. Неясности).

### 7. Дивиденды

```
def dividendo(bruto):
    ret = round(bruto * 0.19, 2)             # 123: casilla 01 perceptores, 02 base, 03 retención; 193 clave A
    neto = bruto − ret
# У получателя-резидента (modelo 100) или Beckham (modelo 151): cuota_ahorro(bruto) − ret
def cuota_ahorro(base):
    tramos = [(6000,.19),(50000,.21),(200000,.23),(300000,.27),(INF,.30)]
```

Ограничение распределения (art. 273 LSC): дивиденд ≤ beneficio distribuible после reserva legal (10 % → до 20 % capital; 20 % при capital < 3 000) и обязательных RC/RN; patrimonio neto после выплаты ≥ capital.

### 8. Учёт (PGC PYMEs, RD 1515/2007) — минимальные проводки

```
# a) Счёт продажи, клиент вне Испании B2B (art. 69 LIVA — no sujeto; 349 если ЕС)
D 430 Clientes (total)            / H 705 Prestaciones de servicios (base)
#    клиент в Испании:
D 430 (base+IVA)                  / H 705 (base), H 477 HP IVA repercutido (21 %)
#    оплата (разница курса при USD → 768/668):
D 572 Bancos                      / H 430

# b) Расход с испанской фактурой
D 6xx gasto (base), D 472 HP IVA soportado        / H 410 Acreedores (или 400)
#    услуга от поставщика ЕС/вне ЕС (inversión del sujeto pasivo):
D 6xx, D 472                                       / H 410, H 477
#    инвестиция (ноутбук):
D 217 Equipos para procesos de información, D 472 / H 572
#    амортизация (месяц или год):
D 681 Amortización inmovilizado material           / H 281 AA inmovilizado material

# c) Вознаграждение administrador (devengo месяца)
D 640 Sueldos y salarios (bruto)                   / H 4751 HP acreedora retenciones (35 %/19 %), H 465 Remuneraciones pendientes
D 465                                              / H 572            # выплата нетто
#    RETA, оплаченная SL (retribución en especie):
D 640 (cuota RETA)                                 / H 572            # платёж TGSS
D 640 (ingreso a cuenta) или D 465                 / H 4751           # ingreso a cuenta, если не repercutido
#    если socio выставляет профессиональный счёт (art. 27.1):
D 623 Servicios de profesionales independientes (base), D 472 (IVA) / H 4751 (15 %/7 %), H 410
#    уплата 111:
D 4751                                             / H 572

# d) Pago fraccionado (202) и провизия IS
D 473 HP retenciones y pagos a cuenta              / H 572            # каждый 202
D 630 Impuesto sobre beneficios (C00592)           / H 4752 HP acreedora por IS
D 4752                                             / H 473            # зачёт 202 и retenciones (473 ← банк. retenciones тоже)
D 4752                                             / H 572            # июль, уплата C00621 (>0); если <0: D 4709 HP deudora devolución / H 473
D 129 Resultado del ejercicio                      / H 630            # закрытие (регуляризация)

# e) Распределение результата (после решения socio único, ≤ 30 июня)
D 129                                              / H 112 Reserva legal, H 114x Reserva de capitalización/nivelación (indisponibles), H 113 Reservas voluntarias, H 526 Dividendo activo a pagar
D 526                                              / H 4751 (19 %), H 572
```

Книги, которые движок генерирует из этих проводок: Libro Diario (можно помесячные сводные записи), Libro de Inventarios y Cuentas Anuales (balance inicial, balances de comprobación ≥ квартальные, inventario, cuentas), Libro de actas (решения socio único), Libro registro de socios, Libro registro de contratos socio único.

### 9. Сравнение autónomo vs SL (2026, приближённо)

Допущения: расходы 6 000 €; RETA autónomo по мин. базе своего tramo (≈ 1 274,51 €/мес при 60 k, ≈ 1 732,03 при 120 k — базы 2025, тип 31,5 %); RETA societario 1 424,40 € × 31,5 % оплачена SL; IRPF общая шкала ≈ estatal × 2 (19/24/30/37/45/47), mínimo personal 5 550; gastos difícil justificación 5 % ≤ 2 000; работник: −2 000 € + reducción; IS micro 2026 (19/21) или ENC 15 %; вся прибыль после IS распределена дивидендами; фикс. расходы SL (RM, libros, depósito) 600 €/год.

| Сценарий | Autónomo IRPF, нетто | SL micro, нетто (зарплата 20k / 35k / 50k) | SL ENC 15 % |
|---|---|---|---|
| 60 000 € | 37 078 | 35 666 / 36 222 / 35 609 | 36 571 / 36 652 / 35 609 |
| 120 000 € | 70 152 | 73 030 / 74 059 / 74 485 | 76 354 / 76 691 / 76 473 |

| Сценарий (Beckham) | Autónomo Beckham 24 %, нетто | SL + Beckham (зарплата 20k / 50k), micro | ENC |
|---|---|---|---|
| 60 000 € | 37 379 | 31 739 / 34 724 | 32 643 / 34 724 |
| 120 000 € | 81 664 | 69 103 / 73 600 | 72 427 / 75 588 |

Правило большого пальца: обычный IRPF — SL ≈ паритет при 60 k€, +4–6 k€/год при 120 k€ с полной выплатой; при реинвестировании (прибыль остаётся в SL) выгода растёт на ≈ (ставка ahorro × нераспределённая прибыль). Под Beckham SL проигрывает на 3–12 k€/год, если прибыль выплачивается; имеет смысл только как «копилка» (отложенное налогообложение) или ради ограничения ответственности/контрактных требований клиентов.

## Сроки и модели

| Modelo | Что | Период | Срок | Когда не подаётся |
|---|---|---|---|---|
| 036 | Alta / NIF provisional → definitivo / изменения | событие | до начала операций; NIF definitivo — после регистрации в RM; опция 40.3 — февраль | — |
| 202 | Pago fraccionado IS | 1/P, 2/P, 3/P | 1–20 апреля, октября, декабря (domiciliación до 15) | результат ≤ 0 (INCN ≤ 6 M€); empresa emergente 2 периода |
| 200 | IS годовой | год | 1–25 июля (2026: до 27.07; domiciliación 1–22.07) | никогда (даже при убытке/без активности) |
| 111 | Retenciones trabajo/administradores/profesionales | квартал | 1–20 апреля, июля, октября, января | если в квартале не было выплат с retención (но при «alta» в 036 ожидают 111 — подать с нулём или снять обязанность) |
| 190 | Резюме 111 | год | 1–31 января | нет 111 за год |
| 123 | Retención дивиденды | квартал | 1–20 апреля, июля, октября, января | не было выплат капитала |
| 193 | Резюме 123 | год | 1–31 января (за 2025: до 02.02.2026) | нет 123 |
| 115 / 180 | Retención аренда | квартал / год | как 111 / январь | аренда ≤ 900 €/год, арендодатель IAE 861 с cuota, leasing, нет аренды |
| 303 / 390 | IVA | квартал / год | 1–20 апреля, июля, октября; 4T и 390 — 1–30 января | — (детали kb IVA) |
| 349 | Операции ЕС | квартал (месяц при >50 k€ товаров) | 1–20 след. месяца; 4T до 30 января | нет операций ЕС |
| 347 | Операции > 3 005,06 € | год | 1–28/29 февраля | все контрагенты уже в 349/190/180 |
| 232 | Operaciones vinculadas | год | 1–30 ноября | ни один порог не превышен |
| Legalización libros | RM | год | ≤ 30 апреля | — |
| Formulación / Aprobación / Depósito cuentas + titularidad real | RM | год | 31 марта / 30 июня / ≤ 1 мес. после утверждения | — |
| Titularidad real (обновление) | RM / RCTIR | событие | 10 дней с момента изменения | нет изменений |
| 840 | IAE alta | событие | 1 мес. после утраты освобождения (INCN ≥ 1 M€) | INCN < 1 M€ |
| 720 | Активы за рубежом | год | 1 января – 31 марта | SL с активами, отражёнными в учёте, освобождена |
| RETA alta administrador | TGSS | событие | до начала (alta previa, ≤ 60 дней) | — |

Первый год SL: 036 (NIF provisional) → escritura → RM → 036 (NIF definitivo, 120) → RETA alta → 303/111/123 по мере возникновения → 390/190/193/349-4T/347 в январе–феврале → libros до 30 апреля → cuentas → 200 в июле → depósito. 202 в первый год нет (кроме опции 40.3).

## Пограничные случаи

1. **Переход autónomo → SL с той же деятельностью**: 15 % ENC недоступен (29.1 párr. 2: деятельность велась физлицом, владеющим > 50 %). Движок: флаг `activity_previously_by_owner_gt50 = true` → только шкала micro.
2. **Socio-программист и art. 27.1**: если SL живёт с его кода, а он в RETA — его оплата = профессиональный счёт (15 %/7 %, IVA), а не nómina; за должность administrador — отдельная (может быть символическая) оплата с 35 %/19 %. Смешение в одну nómina — классическая ошибка при проверке.
3. **Beckham-holder и своя SL**: доход как профессионал через SL = actividad económica → допустим только при основании 93.1.b.3º (emprendedor; visa Ley 14/2013 покрывает требование ENISA). При входе по 93.1.b.1º/2º (трудовой/administrador) такой доход несовместим с режимом → брать только зарплату administrador (24 %) + дивиденды (ahorro). Детали — kb Beckham.
4. **Beckham и регион**: IS — государственный налог; шкала ahorro — только государственная; Beckham не использует региональную шкалу. Переезд между автономными сообществами влияет лишь на зарплату administrador под обычным IRPF (региональная шкала по резиденции на 31.12 / > 183 дней).
5. **Первый период < 12 месяцев**: порог 50 000 € micro-шкалы и лимит 1 M€ reserva de nivelación прорратируются по дням; base 202 за следующий год строится суммированием периодов до 365 дней.
6. **INCN = 0 в первом году** (не было продаж): для ставки следующего года INCN_prev = 0 < 1 M€ → micro-шкала; retención administrador — 19 %, если период закрыт и INCN < 100 k.
7. **Иностранные клиенты и retención**: SL не удерживают IRPF ни иностранные, ни испанские клиенты (в отличие от autónomo-профессионала) → в modelo 200 retenciones = только банк. проценты; весь IS платится через 202/200.
8. **Убыток в году N, прибыль в N+1**: 202 в N+1 не подаются (cuota N = 0); BIN компенсируется в 200 N+1 без практического лимита (< 1 M€); если применяли reserva de nivelación в N−1, в N её остаток уходит в C01033.
9. **Нераспределённая прибыль**: даёт ΔFP → reserva de capitalización в следующем году (20 % от прироста, лимит 25 % BI при INCN < 1 M€); требует indisponible-резерва 3 года — движок должен запретить её распределение до истечения срока.
10. **Оплата RETA с расчётного счёта SL** без оформления как retribución → риск переквалификации в liberalidad (не вычитаемо) и неучтённый доход socio; правильно — en especie через 640/4751 и в 190.
11. **Домашний офис socio, арендуемый SL**: vinculada-операция по рынку, retención 19 % (115/180), у socio — rendimiento de capital inmobiliario; IVA — аренда жилья физлицом освобождена, но помещение под офис — облагаемая операция (risky; см. kb IVA).
12. **Иностранный банк (Wise/Revolut) на SL**: 720 не нужен, если счёт отражён в учёте с идентификацией; но указать в 036 не требуется. Курсовые разницы — 768/668, облагаются IS.
13. **Capital 1 €**: 20 % прибыли в reserva legal до capital + RL ≥ 3 000 €; при ликвидации с долгами socio отвечает до 3 000 €. При капитале 3 000 € — обычные 10 % до 20 %.
14. **Modelo 232**: при выплатах socio-профессионалу > 50 % INCN (операции одного типа и метода) — обязателен в ноябре даже при малых суммах; штраф за неподачу — informativa (min 300 €, по 20 €/dato).
15. **Фиксированные 35 % в первый год**: INCN «последнего закрытого периода» не существует → условие < 100 k€ формально не выполнено → осторожно применять 35 % до первого закрытого года (см. Неясности).
16. **Empresa emergente**: без сертификата ENISA, записанного в RM, ни одна льгота Ley 28/2022 не применяется; движок должен требовать дату сертификата и регистрационную отметку.
17. **Выход из Beckham / окончание 6 лет**: дивиденды и зарплата из SL переходят на обычный IRPF (региональная шкала для зарплаты) — для SL ничего не меняется, кроме типа retención на зарплату (24 % → 35 %/19 % или общий алгоритм).

## Неясности

1. **Retención administrador в первый год SL**: нет закрытого периода для проверки INCN < 100 k€. UNVERIFIED (не найдена DGT по этому кейсу). Осторожно: 35 % до первого закрытого года; по итогам можно скорректировать только в IRPF получателя (переплата вернётся).
2. **IVA на счёт socio-профессионала своей SL**: art. 27.1 решает только IRPF; DGT ставит IVA в зависимость от «ordenación por cuenta propia» (риск, подчинённость). При 100 % контроле — обычно sujeto (21 %); для SL он вычитаем, так что ошибка в сторону «с IVA» нейтральна. Осторожно: выставлять с IVA.
3. **Beckham-получатель зарплаты/дивидендов: какой модели retención** — 111/190 и 123/193 (как для контрибуйентов IRPF) против 216/296 (IRNR). AEAT трактует impatriados как контрибуйентов IRPF с правилами IRNR; практика — 111/190 с типом 24 %. UNVERIFIED для дивидендов; осторожно: 123/193, 19 %.
4. **Прорратео tramo 50 000 € в 202-40.3**: инструкция описывает «tramos» по типам, но не оговаривает, прорратируется ли 50 k на 3/9/11 месяцев. Осторожно: применять полный tramo (как делает форма AEAT по введённой ставке) и пересчитать в 200; UNVERIFIED.
5. **Дата начала первого периода** (escritura vs inscripción): доктрина DGT — IS с даты escritura для sociedades en formación, которые затем регистрируются. Осторожно: period.start = fecha escritura; проверить при более чем 3 мес. между escritura и inscripción.
6. **Вычитаемость оплаты administrador без статутной оговорки**: ТС 2023–2024 смягчил, но AEAT по-прежнему проверяет art. 217 LSC. Осторожно: движок требует флаг `estatutos_cargo_retribuido` + acta socio único с суммой; иначе предупреждение «риск ajuste positivo».
7. **Ставки 2027–2029** взяты из текста DT 44ª Ley 7/2024; AEAT пока публикует до 2026. Возможны изменения в будущих PGE/реформах — хранить как таблицу по году.
8. **Verifactu**: юридически 01.01.2027 для SL; анонс переноса на 10.2028 от 05.10.2026 без BOE; Cortes распущены 06.10.2026 (выборы 29.11.2026). Осторожно: держать режим Verifactu готовым к 01.01.2027, флаг отключения при публикации нормы.
9. **RETA societario 2026**: 1 424,40 € — окончательная мин. база после регуляризации; в течение 2026 допускалась предварительная 1 000 €. Сумма доплаты придёт при регуляризации 2027. Детали — kb RETA.
10. **Шкала IRPF в сравнении autónomo vs SL** — приближение (estatal × 2); реальная Comunidad Valenciana/Asturias ±1–2 п.п.; базы RETA autónomo 2026 взяты по таблице 2025. Цифры сравнения — ориентир, не расчёт для подачи. Точные шкалы — kb IRPF autónomo.
11. **Reserva de nivelación для micro на двухступенчатой шкале**: AEAT подтверждает применимость (шкала — párr. 1 art. 29.1); для ENC на 15 % — нет. Если ENC-окно закончилось в середине «жизни» резерва — реверс продолжается по обычным правилам. Не найдено разъяснений по комбинации — UNVERIFIED.
12. **Hoja de titularidad real** — обязательна с депозитом по моделям Resolución DGSJFP 19.05.2026; отдельная ежегодная декларация в RCTIR в январе для SL **не** требуется (вид подачи через RM). Если RM отклонит депозит без hoja → cierre registral.
