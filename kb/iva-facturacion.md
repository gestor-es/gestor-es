# IVA и выставление счетов (facturación) для автономо / SL, оказывающих услуги

Статус на 2026-10-08. Источники — первичные (BOE, AEAT Sede, DGT). Всё, что не удалось подтвердить первичным источником, помечено **UNVERIFIED** или `[INFERENCE]`.

## Кратко

- IVA не зависит от режима Beckham, от региона (Valencia/Asturias) и от формы (autónomo/SL): правила одинаковы. Регион важен только для Canarias/Ceuta/Melilla (там нет IVA — IGIC/IPSI).
- Услуги B2B клиенту-предпринимателю в другой стране ЕС: **no sujeta** в Испании (art. 69.Uno.1º LIVA), IVA платит клиент по reverse charge. Нужна регистрация в ROI (Modelo 036, casilla 582), NIF-IVA клиента проверяется в VIES. Modelo 303 → casilla **59**; Modelo 349 → clave **S**.
- Услуги B2B клиенту вне ЕС (США и т.п.): **no sujeta** (art. 69.Uno.1º), без reverse-charge-оговорки; с 2023 правило «uso efectivo» (art. 70.Dos) к B2B-услугам нашего типа не применяется. Modelo 303 → casilla **120**; в 349 не попадает.
- Испанский клиент (B2B или B2C): IVA 21 %. Если клиент — empresario/profesional и исполнитель — физлицо с *профессиональной* деятельностью, в счёте указывается retención IRPF: 15 % (7 % первые 3 года) в обычном режиме; **24 %** в режиме Beckham; при *empresarial* деятельности и у SL — retención нет.
- B2C клиенту в ЕС: испанский IVA 21 % (art. 69.Uno.2º). Исключение — электронные/телеком-услуги: до 10 000 €/год — испанский IVA, выше (или по опции) — IVA страны клиента через OSS (Modelo 369, casilla 123 в 303).
- B2C клиенту вне ЕС: консалтинг/разработка/обработка данных (список art. 69.Dos) и электронные услуги — **no sujeta** (casilla 120), остальное — 21 %.
- Право на вычет входного IVA **сохраняется** при оказании услуг иностранным клиентам (art. 94.Uno.2º LIVA): prorrata не нужна, если нет exentas sin derecho (art. 20). Типичный профиль (все клиенты за рубежом) ⇒ 303 почти всегда «a compensar», возврат — только в 4T (casilla 73) или через REDEME/SII.
- Полученные услуги от поставщиков ЕС (SaaS и т.п.): autorrepercusión — casillas 10/11 и 36/37, 349 clave **I**. От поставщиков вне ЕС: casillas 12/13 и 28/29, в 349 не идёт.
- Счёт (RD 1619/2012 art. 6): номер/серия, дата, стороны с NIF и адресами, описание, base, tipo, cuota, дата операции если отличается, обязательные оговорки для exentas/no sujetas/ISP. Валюта любая, но **cuota IVA — в евро** по курсу на дату devengo. Simplificada ≤ 400 € с IVA, но запрещена для счетов иностранным клиентам (art. 4.4.d).
- Modelo 390 для нашего профиля **обязателен** (освобождены только módulos/аренда недвижимости/SII). Modelo 347 — только контрагенты > 3 005,06 €/год, исключая операции из 349 и операции с retención.
- Verifactu (RD 1007/2023, Orden HAC/1177/2024): по RDL 15/2025 сроки — IS с 01.01.2027, остальные (IRPF-автономо) с 01.07.2027. **05.10.2026 Hacienda объявила перенос на октябрь 2028**, нормативный акт ещё не опубликован. Самописный софт обязан соответствовать (hash-цепочка SHA-256, QR 30–40 мм, XML-реестры) и иметь собственную declaración responsable.
- Электронный счёт B2B (Ley Crea y Crece, RD 238/2026, Orden HAC/1028/2026): обязателен для получателей-предпринимателей в Испании с **06.10.2027** (оборот > 8 млн) и **06.10.2028** (все остальные). К иностранным клиентам не относится.
- Книги (libros registro): facturas expedidas, recibidas, bienes de inversión. Официальный формат AEAT — XLSX (LSI.xlsx) с листами EXPEDIDAS_INGRESOS / RECIBIDAS_GASTOS / BIENES-INVERSIÓN; он же импортируется в Pre303, Renta Web и Modelo 130.
- Хранение счетов — срок prescripción LGT (4 года с конца срока подачи соответствующей декларации); для bienes de inversión — дольше (период регуляризации + 4 года); для SL дополнительно 6 лет по Código de Comercio.

## Правила

1. **Общее правило места оказания услуг B2B** — услуга локализуется там, где находится клиент-предприниматель (sede/EP/domicilio). Если клиент не в TAI (Península+Baleares) — операция *no sujeta* в Испании. В силе с 01.01.2010 (Ley 2/2010). Источник: art. 69.Uno.1º LIVA — https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a69
2. **Общее правило B2C** — услуга локализуется по месту исполнителя (TAI) ⇒ испанский IVA 21 %. Исключение art. 69.Dos: перечисленные услуги (права ИС, реклама, asesoramiento/consultores/ingeniería/abogacía, tratamiento de datos y suministro de informaciones, traducción, cesión de personal, аренда движимого имущества и др.) клиенту-непредпринимателю **вне ЕС** (не Canarias/Ceuta/Melilla) — no sujetas. Источник: art. 69.Dos LIVA (та же ссылка).
3. **Электронные услуги B2C** (hosting, SaaS/подписки, скачиваемый софт, онлайн-курсы без участия человека — art. 69.Tres.4º): клиент в другой стране ЕС — испанский IVA пока сумма таких услуг + ventas a distancia не превышает **10 000 €** (без IVA) в текущем и прошлом году и нет опции налогообложения в destino (art. 70.Uno.8º, art. 73); выше — IVA страны клиента (OSS/Modelo 369). Клиент вне ЕС — no sujeta (AEAT). Источники: art. 70.Uno.4º/8º, art. 73 LIVA; AEAT «IVA telecomunicaciones y servicios electrónicos» https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html
4. **Uso efectivo (art. 70.Dos)** после Ley 31/2022 и Ley 13/2023 применяется только к (1) услугам art. 69.Dos клиентам-непредпринимателям и (2) аренде транспортных средств, если фактически используются в TAI. К B2B-консалтингу/разработке для клиента вне ЕС не применяется. Источник: art. 70.Dos LIVA (консолидированный текст).
5. **Sujeto pasivo при получении услуг от нерезидента** (art. 84.Uno.2º.a) — получатель-предприниматель в TAI сам начисляет IVA (inversión del sujeto pasivo). Документ для вычета — счёт поставщика или justificante contable (art. 97.Uno.4º), отдельная «autofactura» не нужна. Источник: art. 84, 97 LIVA.
6. **Право на вычет** (art. 94.Uno): даёт в т.ч. п. 2º — операции вне TAI, которые давали бы право на вычет внутри. ⇒ услуги иностранным клиентам (B2B ЕС/вне ЕС, no sujetas) **дают право на вычет**. Prorrata (art. 102–106) — только при наличии одновременно операций с правом и без права (exentas art. 20). Источник: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a94
7. **Ограничения вычета**: art. 95 — только расходы, прямо и исключительно связанные с деятельностью; bienes de inversión частичного использования — пропорционально, автомобили (turismos) — презумпция **50 %** (и те же 50 % на топливо, парковку, ремонт, запчасти — art. 95.Cuatro). art. 96 — никогда: ювелирка, еда/напитки/табак, зрелища, atenciones a clientes, поездки/гостиницы/рестораны, кроме случаев, когда расход вычитаем в IRPF/IS. Источник: art. 95–96 LIVA.
8. **Формальные требования вычета** (art. 97): оригинал счёта на имя налогоплательщика со всеми реквизитами art. 6 RD 1619/2012; «тикет» (factura simplificada без NIF получателя) вычет не даёт, если продавец не добавил NIF и адрес получателя и cuota отдельной строкой (art. 7.2 RD 1619/2012). Срок реализации вычета — 4 года с devengo (art. 99.Tres, 100 LIVA).
9. **Devengo услуг** (art. 75): при оказании услуги (75.Uno.2º); при предоплате — в момент получения оплаты (75.Dos); длящиеся услуги (tracto sucesivo, 75.Uno.7º) — когда exigible каждая часть цены; если exigibilidad не наступает в течение года — 31 декабря каждого года. Источник: art. 75 LIVA.
10. **Обязанность выставить счёт** (RD 1619/2012 art. 2): по всем операциям, включая no sujetas и exentas, если клиент — empresario/profesional или persona jurídica, и когда операция локализована за пределами TAI, но исполнитель — в TAI (art. 2.3.b.b’). Срок: B2B — до 16-го числа месяца, следующего за devengo (art. 11); B2C — в момент операции. Отправить клиенту — в тот же срок (art. 18). Источник: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
11. **Содержание счёта** (art. 6 RD 1619/2012): a) номер и серия (сквозная нумерация в серии; отдельные серии обязательны для rectificativas и для счетов, выставляемых получателем/третьим лицом); b) дата выставления; c) полные имена/наименования сторон; d) NIF исполнителя; NIF клиента обязателен при ISP, при операциях в TAI и при EIB; e) адреса сторон; f) описание, цена за единицу без IVA, скидки; g) tipo; h) cuota отдельно; i) дата операции, если отличается; j) при exención — ссылка на статью Directiva 2006/112/CE или LIVA либо слово «exenta»; m) «inversión del sujeto pasivo», если плательщик — получатель; p) «régimen especial del criterio de caja». Для операций art. 2.3.b.b’.a’’ (ЕС B2B) можно опустить f/g/h, указав объём и характер услуги и облагаемую сумму (art. 6.3). С 07.12.2023 art. 6.5: при использовании SIF — QR и (только в режиме VERI*FACTU) фраза «VERI*FACTU»/«Factura verificable en la sede electrónica de la AEAT».
12. **Factura simplificada** (art. 4, 7): до 400 € с IVA (до 3 000 € для перечисленных розничных активностей) и для rectificativas; **нельзя** для EIB и для операций, локализованных вне TAI (art. 4.4.d → art. 2.3.b.b’), т.е. для иностранных клиентов — всегда полный счёт.
13. **Factura rectificativa** (art. 15): обязательна при ошибке в реквизитах, неверной cuota или изменении base (art. 80 LIVA); выставляется, как только обнаружена причина, в пределах 4 лет от devengo; в отдельной серии; содержит реквизиты исправляемого счёта и суть исправления; суммы — либо как разница (со знаком), либо «как должно быть» с указанием разницы. Отражение в 303: casillas 14/15 (изменение base/cuota) — для операций с IVA; для no sujetas — корректируется сумма casilla 59/120 периода.
14. **Валюта и язык** (art. 12 RD 1619/2012; art. 79.Once LIVA): суммы — в любой валюте, но cuota IVA — в евро по «tipo de cambio vendedor fijado por el Banco de España» на дату devengo. По DGT V2630-17 BdE курс не фиксирует — применяется курс-референс ЕЦБ (публикуемый BdE), допустим иной общедоступный источник, если применяется последовательно и не отклоняется существенно. Язык любой; AEAT может потребовать перевод на castellano.
15. **Хранение** (art. 19–23 RD 1619/2012; art. 66–70 LGT): полученные счета, копии выставленных, justificantes contables, DUA — в течение срока prescripción (4 года), с гарантией подлинности, целостности, читаемости и онлайн-доступа для AEAT; хранение вне Испании — только электронно с удалённым доступом и предварительным уведомлением AEAT. Для bienes de inversión — до конца срока регуляризации (5 лет; недвижимость 10) + prescripción. Для SL: 6 лет по art. 30 Código de Comercio.
16. **ROI / NIF-IVA**: до первой интракоммунитарной операции подать Modelo 036 с casilla **582** (alta ROI) и датой первой операции в casilla **584**. Modelo 037 упразднён с 03.02.2025 (Orden HAC/1526/2024). Отсутствие ответа AEAT 3 месяца = отказ. Источник: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html ; BOE-A-2025-410.
17. **Modelo 303**: ежеквартально (1–20 апреля/июля/октября; 4T — 1–30 января). Возврат (casilla 73) — только в последней декларации года, если нет REDEME (art. 30 RIVA); в 1T–3T отрицательный результат — только «a compensar» (casilla 72). Нельзя получить результат «a compensar», если в этом же периоде применены cuotas прошлых периодов (casilla 78 заполнена). Источник: Instrucciones 303 2026 — https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
18. **Modelo 390**: обязателен для всех, кто подаёт периодические 303, кроме (а) квартальных плательщиков только в régimen simplificado и/или аренде городской недвижимости и (б) SII. Срок 1–30 января. Источник: Instrucciones 390-2025 — https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
19. **Modelo 349**: подаётся за каждый период, в котором были операции с клавами E/A/S/I/T/M/H/R/D/C. Периодичность квартальная, если сумма EIB+услуг ЕС (claves E, S и др.) не превысила **50 000 €** без IVA ни в текущем, ни в каждом из 4 предыдущих кварталов; иначе — месячная (при превышении во 2-м месяце — «trimestre truncado»). Сроки: 1–20 следующего месяца; за последний период года — 1–30 января; июль — до 20 сентября (месячные). Источник: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
20. **Modelo 347**: ежегодно в феврале (1–28/29), контрагенты, с которыми за год > **3 005,06 €** (с IVA), с разбивкой по кварталам. Исключаются: операции без обязанности счёта, импорт/экспорт товаров, операции, уже поданные в других периодических декларациях с совпадающим содержанием (349, retenciones 190/180). Не подают: SII-плательщики, лица только с исключёнными операциями. Источник: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
21. **Retención IRPF в счёте профессионала** испанскому плательщику-предпринимателю: 15 % (art. 101.5.a LIRPF); 7 % в год начала и два следующих, если в предыдущем году профессиональная деятельность не велась и клиенту вручено письменное уведомление (art. 95.1 RIRPF). Режим Beckham: удержания по нормам IRNR — профессиональная деятельность **24 %**, empresarial — без удержания (art. 114 RIRPF в ред. RD 1008/2023). Источники: https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
22. **Verifactu — сфера и сроки**: RRSIF (RD 1007/2023) применяется к плательщикам IS, IRPF с actividades económicas, IRNR с EP и ERAR; не применяется к SII. Сроки по RDL 15/2025: IS — до 01.01.2027; остальные — до 01.07.2027. 05.10.2026 Министерство объявило намерение перенести на **октябрь 2028** (совмещение с e-factura); до публикации нормы действуют даты 2027. Источники: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf ; https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
23. **Verifactu — требования к SIF** (RRSIF art. 8–16; Orden HAC/1177/2024 art. 10–21): на каждый счёт — registro de facturación de alta (XML UTF-8), на аннулирование — registro de anulación; huella SHA-256 с цепочкой (поле Huella предыдущей записи); либо отправка всех записей в AEAT (режим VERI*FACTU, web-service, контроль потока 60 с), либо подпись XAdES квалифицированным сертификатом + registro de eventos; QR 30×30–40×40 мм, ISO/IEC 18004, уровень M, с URL AEAT (NIF, serie+número, fecha, importe total); фраза «VERI*FACTU» только при отправке. Источник: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
24. **Declaración responsable** (RRSIF art. 13; OM art. 15): обязательна для каждой версии любого SIF, включая **самописный софт для собственного использования** — его сертифицирует сам разработчик-пользователь; внешней сертификации и регистрации нет. Источник: FAQ AEAT — https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
25. **Factura electrónica B2B** (Ley 18/2022 art. 12; RD 238/2026; Orden HAC/1028/2026, в силе 06.10.2026): обязательна, когда получатель — empresario/profesional с sede/EP/domicilio в Испании; не для simplificadas (кроме art. 7.2). Сроки: 06.10.2027 — выставляющие с оборотом > 8 млн €; 06.10.2028 — остальные. Сообщение статусов (принята/оплачена): 06.10.2027 / 06.10.2028 (юрлица) / 06.10.2029 (физлица). Источник: https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html ; https://www.boe.es/eli/es/rd/2026/03/25/238/con
26. **Libros registro** (art. 62–70 RIVA; Orden HAC/773/2019 для IRPF): facturas expedidas, recibidas, bienes de inversión (+ determinadas operaciones intracomunitarias — для нас неактуально). Записи в евро, хронологически, с итогами по кварталам; rectificativas — отдельно. Электронный формат AEAT: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; дизайн полей: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx
27. **Volumen de operaciones** (art. 121 LIVA) = сумма contraprestaciones всех операций года (включая no sujetas по локализации и exentas), без IVA; исключаются продажи bienes de inversión и нерегулярные финансовые/недвижимые операции. Используется в 303 (4T, casilla 88 у освобождённых от 390), 390 (casilla 108) и для порога e-factura 8 млн.

## Цифры

### Ставки и пороги (2025 и 2026 — без изменений для нашего профиля)

| Параметр | 2025 | 2026 | Источник |
|---|---|---|---|
| Tipo general IVA | 21 % | 21 % | art. 90 LIVA |
| Tipo reducido / superreducido | 10 % / 4 % (0 % и 5 %/7,5 % были только на продукты до 2024) | 10 % / 4 % | art. 91 LIVA |
| Порог OSS (B2C электронные + ventas a distancia ЕС) | 10 000 € без IVA | 10 000 € | art. 73 LIVA |
| Порог месячного 349 | 50 000 € без IVA (квартал и 4 предыдущих) | 50 000 € | art. 81 RIVA |
| Порог 347 на контрагента | > 3 005,06 € с IVA | > 3 005,06 € | art. 33 RGAT |
| Bien de inversión (IVA) | ≥ 3 005,06 € и использование > 1 года | то же | art. 108 LIVA |
| Factura simplificada | ≤ 400 € с IVA (≤ 3 000 € для розницы) | то же | art. 4 RD 1619/2012 |
| Презумпция affectación автомобиля | 50 % | 50 % | art. 95.Tres.2ª LIVA |
| Prorrata — округление | вверх до целого % | то же | art. 104.Dos LIVA |
| Prorrata especial обязательна | если general даёт на ≥ 10 % больше вычета | то же | art. 103.Dos.2º |
| Gran empresa (303 месячный, SII) | > 6 010 121,04 € оборота пред. года | то же | art. 71.3 RIVA |
| Retención profesional (обычный IRPF) | 15 % / 7 % (старт) | 15 % / 7 % | art. 101.5 LIRPF, 95.1 RIRPF |
| Retención profesional (Beckham, IRNR) | 24 % | 24 % | art. 114 RIRPF |
| Срок вычета входного IVA | 4 года от devengo | 4 года | art. 99–100 LIVA |
| Хранение счетов | 4 года (prescripción) | 4 года | art. 66 LGT, art. 19 RD 1619/2012 |
| Срок выставления счёта B2B | до 16-го числа след. месяца | то же | art. 11 RD 1619/2012 |

### Сроки (календарь)

| Modelo | Период | Срок | Домициляция (−5 дней) |
|---|---|---|---|
| 303 | 1T/2T/3T | 1–20 апр / июл / окт | до 15-го |
| 303 | 4T | 1–30 января | до 25 января |
| 390 | год | 1–30 января | — |
| 349 квартальный | 1T–3T | 1–20 апр / июл / окт | — |
| 349 | 4T (или декабрь) | 1–30 января | — |
| 347 | год | 1–28(29) февраля | — |
| 369 (OSS) | квартал | до конца месяца, следующего за кварталом | — |
| 036 alta ROI | — | до первой операции ЕС | — |
| 036 смена domicilio fiscal | — | 1 месяц с изменения (art. 10 RGAT) | — |

Если последний день — выходной/праздник, срок переносится на следующий рабочий день (AEAT calendario).

### Verifactu / e-factura — даты

| Обязанность | Дата | Статус |
|---|---|---|
| SIF адаптирован — плательщики IS | 01.01.2027 | в силе (RDL 15/2025) |
| SIF адаптирован — IRPF-автономо и прочие | 01.07.2027 | в силе (RDL 15/2025) |
| Перенос всего RRSIF на октябрь 2028 | ~10.2028 | объявлено 05.10.2026, **норма не опубликована** |
| e-factura B2B, оборот > 8 млн € | 06.10.2027 | в силе (RD 238/2026 + OM HAC/1028/2026) |
| e-factura B2B, остальные (наш профиль) | 06.10.2028 | в силе |
| Сообщение статусов e-factura, физлица | 06.10.2029 | в силе |

### Casillas Modelo 303 (форма 2025/2026) — карта для нашего профиля

| Операция | Devengado (base/tipo/cuota) | Deducible (base/cuota) | Informativas | 349 |
|---|---|---|---|---|
| Продажа испанскому клиенту 21 % | 07 / 08 / 09 | — | — | — |
| Продажа B2B клиенту ЕС (услуга) | — | — | **59** | S |
| Продажа B2B клиенту вне ЕС, Canarias/Ceuta/Melilla | — | — | **120** | — |
| Продажа B2C вне ЕС услуг art. 69.Dos / электронных | — | — | 120 | — |
| Продажа B2C ЕС электронных услуг через OSS | — (в 369) | — | 123 | — |
| Экспорт товаров (art. 21) | — | — | 60 | — |
| Операции с ISP, где плательщик — испанский клиент (art. 84.Uno.2º c–g; не наш случай) | — | — | 122 | — |
| Покупка у испанского поставщика (текущие) | — | 28 / 29 | — | — |
| Покупка bien de inversión в Испании | — | 30 / 31 | — | — |
| Импорт товаров (DUA) | — | 32 / 33 (34/35 инвест.) | — | — |
| Услуга от поставщика ЕС (AIS) | **10 / 11** | **36 / 37** | — | I |
| Товар из ЕС (AIB) | 10 / 11 | 36 / 37 (38/39 инвест.) | — | A |
| Услуга от поставщика вне ЕС (ISP art. 84.Uno.2º.a) | **12 / 13** | **28 / 29** | — | — |
| Rectificativa с IVA (±) | 14 / 15 | 40 / 41 (входящие) | — | — |
| Итоги | 27 = 152+167+03+155+06+09+11+13+15+158+170+18+21+24+26 | 45 = 29+31+33+35+37+39+41+42+43+44 | 46 = 27 − 45 | |
| Результат | 64 = 46+58+76; 65 = 100 %; 66 = 64; 110 (пред. остаток); 78 (применено); 87 = 110−78; 69 = 66+77−78+68+108; 71 = 69−70+109 | | 72 (compensar) / 73 (devolver, только 4T) | |

### Casillas Modelo 390 (2025) — ключевые

| Содержание | Casillas |
|---|---|
| Régimen ordinario по ставкам (0/4/10/21 %) base/cuota | 01–06, 700–703, 667–670 (21 % — пара 05/06 `[INFERENCE: проверить по формуляру]`) |
| Adquisiciones intracomunitarias de servicios base/cuota по ставкам | 545–548, 551–552, 720–723, 687–690 |
| Adquisiciones intracomunitarias de bienes | 21–26, 716–719, 683–686 |
| Otros supuestos de ISP (поставщик вне ЕС) | 27 / 28 |
| Modificación bases y cuotas | 29 / 30 |
| Total bases / cuotas devengadas | 33 / 34; 47 (cuotas IVA + RE) |
| Deducible interior corrientes (сумма) | 48 / 49 (по ставкам 695–698, 190–191 …) |
| Deducible interior bienes de inversión | 50 / 51 |
| Deducible importaciones corrientes / inversión | 52 / 53; 54 / 55 |
| Resultado régimen general / suma / compensación año anterior / resultado liquidación | 84, 85, 86 |
| Итоги autoliquidaciones: a ingresar / a compensar / a devolver | 95, 97, 98 |
| Volumen de operaciones: régimen general / EIB+servicios ЕС / exportaciones / exentas sin derecho / no sujetas localización / ISP / OSS / total | 99, 103, 104, 105, 110, 125, 126, 108 |

### Claves для libros registro и registros Verifactu

| Поле | Значения |
|---|---|
| Calificación de la operación | S1 sujeta no exenta sin ISP; S2 sujeta con ISP; N1 no sujeta art. 7/14; **N2 no sujeta por reglas de localización** |
| Operación exenta | E1 art. 20; E2 art. 21; E3 art. 22; E4 art. 23–24; E5 art. 25 (EIB); E6 otras |
| Clave de régimen | 01 general; 02 exportación; 07 criterio de caja; 08 IGIC/IPSI; 17 OSS; 18 recargo equivalencia … |
| Tipo de factura (Verifactu) | F1 completa; F2 simplificada; F3 sustitutiva de simplificadas; R1–R4 rectificativas (R1 error de derecho/art. 80.Uno-Dos-Seis, R2 art. 80.Tres, R3 art. 80.Cuatro, R4 resto); R5 rectificativa de simplificada |
| Tipo NIF destinatario (libros) | 02 NIF-IVA ЕС; 03 pasaporte; 04 doc. oficial país; 05 certificado residencia; 06 otro documento probatorio; 07 no censado |

## Формулы для движка

Везде: суммы в евро, 2 знака, округление `ROUND_HALF_UP` (как в формах AEAT). Cuota считается на каждый счёт (по каждой ставке) и уже округлённой суммируется в книги и в 303; валидации AEAT (SII/Verifactu) допускают отклонение `|cuota − base×tipo| ≤ 10 €` на счёт `[по документу validaciones AEAT; подтвердить версию]`.

### 1. Классификация продажи (place of supply + режим счёта)

```
input: seller{profile: AUTONOMO_IRPF | AUTONOMO_BECKHAM | SL, activity_kind: PROFESIONAL | EMPRESARIAL, years_since_start, oss_registered}
       customer{country, is_business, vat_id (optional, validated in VIES), spanish_withholder: bool}
       service{kind: GENERAL | ELECTRONIC | ART69DOS (consulting, data processing, IP, advertising, translation...) | IMMOVABLE | OTHER_SPECIAL}
       ytd_b2c_eu_electronic_sales (current year and previous year, without IVA)

TAI  = country == ES and region not in {Canarias, Ceuta, Melilla}
EU   = country in EU27 (excluding ES-TAI; Canarias/Ceuta/Melilla treated as NON_EU for IVA)

if service.kind == IMMOVABLE: locate by property (art. 70.Uno.1º) — вне нашего профиля, STOP

# B2B status: vat_id valid in VIES, or (non-EU) other proof of business (Reg. UE 282/2011 art. 18)
b2b = customer.is_business and (customer.country not in EU or vat_id_valid)

case TAI:
    regime = SUJETA_21
    withholding = compute_withholding(seller, customer)          # см. п.3
case EU and b2b:
    regime = NO_SUJETA_INTRACOM                                  # art. 69.Uno.1º; casilla 59; 349 clave S
    require seller in ROI (ES-VAT in VIES) else -> WARN_ROI
case EU and not b2b:
    if service.kind == ELECTRONIC and (ytd_prev > 10000 or ytd_cur + amount > 10000 or seller.oss_registered):
        regime = OSS_DESTINO                                     # IVA страны клиента, Modelo 369, casilla 123
    else:
        regime = SUJETA_21                                       # art. 69.Uno.2º / 70.Uno.8º
case NON_EU and b2b:
    regime = NO_SUJETA_LOCALIZACION                              # art. 69.Uno.1º; casilla 120
case NON_EU and not b2b:
    if service.kind in {ART69DOS, ELECTRONIC}: regime = NO_SUJETA_LOCALIZACION   # art. 69.Dos / criterio AEAT
    else: regime = SUJETA_21                                     # regla general art. 69.Uno.2º
    if effectively_used_in_TAI(service): regime = SUJETA_21     # art. 70.Dos (только B2C art. 69.Dos)
```

Для Canarias/Ceuta/Melilla: B2B → NO_SUJETA_LOCALIZACION (casilla 120, не 59, 349 не подаётся); B2C → SUJETA_21 (art. 69.Dos их исключает).

### 2. Строки счёта по режиму

```
base      = Σ round(qty × unit_price × (1 − discount), 2)
case SUJETA_21:
    tipo = 21.00; cuota = round(base × 0.21, 2)
    retencion = round(base × withholding_rate, 2)            # только если withholding_rate > 0
    total_factura = base + cuota                              # «Total factura» в libros НЕ уменьшается на retención
    total_a_pagar = base + cuota − retencion
    mentions: []  (при retención — строка «Retención IRPF x %: −N €» и база удержания)
case NO_SUJETA_INTRACOM:
    tipo = none; cuota = 0; total = base
    required: NIF-IVA продавца (ES…) и клиента (с префиксом страны), оба валидны в VIES на дату счёта
    mentions: «Operación no sujeta al IVA español por reglas de localización (art. 69.Uno.1º Ley 37/1992)»,
              «Inversión del sujeto pasivo / Reverse charge — art. 196 Directiva 2006/112/CE»
    forbidden: factura simplificada
case NO_SUJETA_LOCALIZACION:
    tipo = none; cuota = 0; total = base
    mentions: «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)»
              (для B2C art. 69.Dos — ссылка на art. 69.Dos)
    forbidden: factura simplificada
case OSS_DESTINO:
    tipo = rate(customer.country); cuota = round(base × tipo, 2); total = base + cuota
    mentions: «IVA … % (país de consumo …) — Régimen de la Unión OSS»; декларируется в 369, в 303 только casilla 123
```

Валюта ≠ EUR: все суммы счёта можно показывать в валюте, но добавить строку «Cuota IVA: N EUR (tipo de cambio BCE dd/mm/aaaa: 1 EUR = X CUR)». Для no sujetas IVA нет, но EUR-эквивалент базы всё равно фиксируется в книге по курсу на дату devengo:

```
fx_date   = devengo_date (дата оказания услуги / получения предоплаты), не дата оплаты
rate      = ECB_reference_rate(fx_date)   # если выходной — последний опубликованный до даты [INFERENCE; DGT V2630-17 требует лишь последовательности]
base_eur  = round(base_cur / rate, 2)     # ECB котирует 1 EUR = X CUR
cuota_eur = round(base_eur × tipo, 2)
```

### 3. Удержание IRPF в счёте (только испанским клиентам-предпринимателям)

```
if not customer.spanish_withholder: rate = 0          # физлицо-потребитель, иностранный клиент без EP в Испании
elif seller.profile == SL: rate = 0                   # услуги SL не подлежат retención (кроме аренды и т.п.)
elif seller.activity_kind == EMPRESARIAL: rate = 0    # и в обычном режиме, и в Beckham
elif seller.profile == AUTONOMO_BECKHAM: rate = 0.24  # art. 114 RIRPF → normas IRNR
elif start_year ≤ year ≤ start_year + 2 and no_professional_activity_prev_year and notice_given: rate = 0.07
else: rate = 0.15
retencion = round(base × rate, 2)    # база — base imponible без IVA
```

Удержанное идёт в счёт IRPF (Modelo 100/151) — передаётся модулю IRPF/Beckham; в 303 не отражается.

### 4. Классификация расхода (входной IVA)

```
input: supplier{country, vat_id}, invoice{base, tipo, cuota, currency}, item{kind: CURRENT | INVESTMENT | VEHICLE | FOOD_HOTEL_TRAVEL | GIFTS | PRIVATE_MIX}
deductible_share:
    kind == GIFTS or (FOOD_HOTEL_TRAVEL and not deductible_in_IRPF_IS) -> 0       # art. 96
    kind == VEHICLE (turismo) and related costs -> 0.50 (если не доказано иное)    # art. 95.Tres.2ª, Cuatro
    kind == PRIVATE_MIX (вода/свет/интернет жилья) -> 0                            # art. 95.Uno; criterio AEAT/TEAC
    иначе -> 1.00 × prorrata (prorrata = 1.00, если нет операций art. 20)
investment = (base ≥ 3005.06 and useful_life > 1y)                                # art. 108
if supplier.country == ES:
    casillas: (28,29) если not investment else (30,31)
elif supplier.country in EU and supplier.vat_id valid and seller in ROI:          # AIS
    devengado (10,11) = (base_eur, round(base_eur×0.21,2)); deducible (36,37) = (base_eur, cuota×share) [(38,39) если investment]
    349: clave I, país, NIF-IVA поставщика, base_eur
elif supplier.country not in EU (US SaaS и т.п.):                                 # ISP art. 84.Uno.2º.a
    devengado (12,13) = (base_eur, round(base_eur×0.21,2)); deducible (28,29) = (base_eur, cuota×share) [(30,31) если investment]
else (EU supplier charged foreign VAT because no ROI/VAT-id):
    foreign VAT NOT deductible in 303; записать как расход; возврат только через Modelo 360 (до 30.09 след. года)
imports of goods (DUA): deducible (32,33) / (34,35), devengado — уплачен на таможне (или casilla 77 при опции diferimiento)
```

Для AIS/ISP cuota devengada = cuota deducible (при share = 1) → нулевой эффект на результат, но обе стороны обязательны (art. 97.Uno.4º: вычет только если операция «debidamente consignada»).

### 5. Сборка Modelo 303 за квартал Q

```
sales  = invoices issued with devengo in Q (включая rectificativas, со знаком)
purch  = received invoices registered in Q (можно и позже, в пределах 4 лет)

c07 = Σ base(SUJETA_21);  c08 = 21;  c09 = Σ cuota(SUJETA_21)
c10 = Σ base(AIS + AIB);  c11 = Σ cuota(AIS + AIB)
c12 = Σ base(ISP non-EU); c13 = Σ cuota(ISP non-EU)
c14/c15 = Σ изменений base/cuota по rectificativas с IVA (если не разнесены по 07–09)   # знак ±
c27 = c03+c06+c09+c11+c13+c15 (+ прочие ставки/RE = 0)
c28/c29 = Σ ES current + ISP non-EU current (base без prorrateo; cuota × share)
c30/c31 = Σ ES investment (+ ISP non-EU investment)
c32/c33, c34/c35 = импорты
c36/c37 = Σ AIS + AIB current;  c38/c39 = AIB investment
c40/c41 = корректировки вычетов (rectificativas полученные) ±
c43 = регуляризация bienes de inversión (только если изменилась prorrata/использование); c44 = только 4T при prorrata
c45 = c29+c31+c33+c35+c37+c39+c41+c42+c43+c44
c46 = c27 − c45
c59  = Σ base(NO_SUJETA_INTRACOM)        # услуги B2B ЕС (+ EIB)
c120 = Σ base(NO_SUJETA_LOCALIZACION)    # вне ЕС, Canarias/Ceuta/Melilla, B2C 69.Dos
c123 = Σ base(OSS_DESTINO)
c64 = c46 (+c58 +c76 = 0);  c65 = 100;  c66 = c64
c110 = остаток к компенсации на начало Q (из casilla 72 предыдущих периодов минус применённое)
c78  = min(c110, max(c66 + c77, 0))      # применяем максимум возможного
c87  = c110 − c78
c69  = c66 + c77 − c78 + c68 + c108      # c68, c108 = 0 для нас
c71  = c69 − c70 + c109                  # c70/c109 только в rectificativa
if c71 > 0: INGRESAR c71 (IBAN; домициляция до −5 дней)
elif c71 < 0 and Q in {1T,2T,3T}: COMPENSAR  c72 = |c71|  (запрещено, если c78 > 0 — тогда остаток переносится через c87)
elif c71 < 0 and Q == 4T: выбор DEVOLVER c73 = |c71| (включая весь c110) или COMPENSAR c72
elif c71 == 0 and (c27>0 or c45>0): RESULTADO CERO
else: SIN ACTIVIDAD
новый остаток к компенсации = c87 + c72
```

Инварианты: `c08 = 21.00` только если c07 > 0; `c11 ≈ c10×0.21`, `c13 ≈ c12×0.21`; `c37 ≤ c11` (при 100 % вычете равны); `c59 + c120 + c123 + c07 (+c04+c01) + c60` = выручка квартала по книге выставленных.

### 6. Modelo 349 за период

```
for each (counterparty, clave) in period:
    clave S: Σ base_eur услуг NO_SUJETA_INTRACOM; clave I: Σ base_eur AIS; clave E/A: товары
    registro: código país (DE, FR, …; XI для Сев. Ирландии только для товаров), NIF-IVA без префикса страны, nombre, clave, importe
periodicity: monthly if Σ(E+S+…) > 50000 in current quarter or any of previous 4 quarters, else quarterly
file only if ≥ 1 registro; rectificaciones прошлых периодов — отдельные записи «rectificación» с периодом и ранее заявленной суммой
```

Сверка: `Σ clave S за год = casilla 59 (сумма 4 кварталов 303) − EIB = casilla 103 (390)`.

### 7. Modelo 347 за год

```
candidates = counterparties с Σ(total_factura с IVA) > 3005.06 за год
exclude: контрагенты/операции, заявленные в 349 (клиенты ЕС B2B, поставщики ЕС);
         операции с retención, попавшие в 190/180 (испанские B2B-клиенты профессионала, арендодатель с retención);
         импорт/экспорт товаров; операции без обязанности счёта
include: испанские поставщики без retención (> 3005.06), испанские клиенты без retención (B2C-юрлица, при empresarial/SL),
         клиенты и поставщики вне ЕС по услугам (no sujetas) — AEAT включает их (нет исключения для услуг) [INFERENCE: подтвердить в INFORMA]
по каждому: importe anual (с IVA; для no sujetas — base) и разбивка по кварталам; clave A (compras) / B (ventas)
```

### 8. Modelo 390

Агрегация годовых 303: devengado по ставкам → 01–06; AIS → 545–552 группа; ISP non-EU → 27/28; deducible → 48/49, 50/51, 52/53, 54/55 + интраком. блок; 84 = результат; 85 = casilla 110 первого 303 года (остаток прошлого года); 95 = Σ положительных c71; 97/98 = результат последнего 303 (compensar/devolver); volumen: 99 = Σc07(+04,01), 103 = Σc59, 104 = Σc60, 110 = Σc120, 126 = Σc123, 108 = сумма. Плюс datos estadísticos: IAE epígrafe, clave A05 (otras actividades profesionales) или A03 (empresariales), флаг «operaciones con terceras personas» (есть ли 347).

### 9. Verifactu — записи при выставлении счёта

```
on issue(invoice):
    rf = RegistroAlta{
        IDEmisorFactura = seller.NIF, NumSerieFactura = serie+numero, FechaExpedicionFactura = dd-mm-yyyy,
        TipoFactura = F1|F2|R1..R5, Descripcion, Destinatarios[{Nombre, NIF | IDOtro{CodigoPais, IDType, ID}}],
        Desglose[{ClaveRegimen=01, CalificacionOperacion=S1|S2|N1|N2 | OperacionExenta=E1..E6, TipoImpositivo, BaseImponible, CuotaRepercutida}],
        CuotaTotal, ImporteTotal, Encadenamiento{PrimerRegistro | RegistroAnterior{IDEmisor, NumSerie, Fecha, Huella}},
        SistemaInformatico{NombreRazon, NIF, NombreSistemaInformatico, IdSistemaInformatico(2 chars), Version, NumeroInstalacion, TipoUsoPosibleSoloVerifactu=S|N, TipoUsoPosibleMultiOT, IndicadorMultiplesOT},
        FechaHoraHusoGenRegistro = ISO-8601 с зоной (2026-03-10T12:00:00+01:00), TipoHuella = 01 (SHA-256), Huella }
    cadena = "IDEmisorFactura=…&NumSerieFactura=…&FechaExpedicionFactura=…&TipoFactura=…&CuotaTotal=…&ImporteTotal=…&Huella=<prev or empty>&FechaHoraHusoGenRegistro=…"
    Huella = UPPER(HEX(SHA256(UTF8(cadena))))          # 64 символа; значения trim; Huella= пусто для первой записи
    тест-вектор AEAT: "IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00"
                     → 3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60
    mode VERIFACTU: POST XML в web-service AEAT (сертификат), ждать t≥60 с между отправками или до лимита записей; ретраи ≥ 1/час при сбое; CSV в ответе
    mode NO_VERIFACTU: подписать XAdES Enveloped квалифицированным сертификатом; вести registro de eventos (запуск/останов, экспорт, инциденты) с собственной hash-цепочкой
    на печатной/PDF-форме: QR 30–40 мм, ISO 18004, уровень M, URL cotejo AEAT с NIF, serie+numero, fecha, importe total; текст «VERI*FACTU» только в режиме VERIFACTU
on cancel(invoice): RegistroAnulacion{IDFactura, Encadenamiento, Huella по полям NIF, NumSerie, Fecha, HuellaAnterior, FechaHoraHuso}
rectificativa: новый RegistroAlta TipoFactura=R1..R5, TipoRectificativa=S (por sustitución) | I (por diferencias), FacturasRectificadas[...]
```

Записи (XML) и события хранятся до prescripción, неизменяемы; любая правка — только новой записью. Декларация responsable (OM art. 15: название, Id (2 символа), версия, компоненты, SoloVerifactu S/N, MultiOT S/N, тип подписи, продюсер — NIF и адрес, дата/место) встроена в меню софта и доступна отдельно (PDF).

### 10. Libros registro — запись

Лист `EXPEDIDAS_INGRESOS` (LSI.xlsx): Ejercicio | Periodo (1T…4T) | Actividad: Código, Tipo, Grupo/Epígrafe IAE | Tipo de Factura (F1/F2/R1…) | Concepto de Ingreso (IRPF) | Ingreso Computable | Fecha Expedición | Fecha Operación | Identificación de la Factura: Serie, Número, Número-Final | NIF Destinatario: Tipo (02/03/04/05/06/07), Código País, Identificación | Nombre Destinatario | Clave de Operación (01…) | Calificación (S1/S2/N1/N2) | Operación Exenta (E1–E6) | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Repercutida | Tipo/Cuota Recargo Eq. | Cobro: Fecha, Importe, Medio, Identificación Medio | Tipo Retención IRPF | Importe Retenido IRPF | Registro Acuerdo Facturación | Inmueble: Situación, Ref. Catastral | Referencia Externa.

Лист `RECIBIDAS_GASTOS`: Ejercicio | Periodo | Actividad | Tipo de Factura | Concepto de Gasto | Gasto Deducible | Fecha Expedición | Fecha Operación | Identificación Factura del Expedidor (Serie-Número, Número-Final) | Fecha Recepción | Número Recepción / Final | NIF Expedidor: Tipo, Código País, Identificación | Nombre Expedidor | Clave de Operación | Bien de Inversión (S/N) | Inversión del Sujeto Pasivo (S/N) | Deducible en Periodo Posterior (S/N) | Periodo Deducción: Ejercicio, Periodo | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Soportado | Cuota Deducible | Tipo/Cuota Recargo Eq. | Pago: Fecha, Importe, Medio, Identificación | Tipo/Importe Retención IRPF | Registro Acuerdo Facturación | Inmueble | Referencia Externa.

Лист `BIENES-INVERSIÓN`: Ejercicio, Periodo, Actividad, Identificador, Descripción, Fecha Inicio Utilización, Valor Adquisición, Valor Amortizable, Método, % Amortización, Amortización (cuota, acumulada inicio/final, pendiente), Identificación factura, NIF/Nombre expedidor, Base, Tipo IVA, Prorrata definitiva, Cuota deducible, Regularización anual (prorrata, cuota deducible, cuota a regularizar), Baja (fecha, causa, factura de transmisión), Referencia externa.

Маппинг наших режимов в книгу: SUJETA_21 → S1, clave 01, tipo 21, cuota; NO_SUJETA_INTRACOM → N2, NIF tipo 02 (VAT-id ЕС), tipo/cuota 0, total = base; NO_SUJETA_LOCALIZACION → N2, NIF tipo 06 (или 04), tipo/cuota 0; AIS/ISP (recibidas) → Inversión del Sujeto Pasivo = S, Cuota Soportado = Cuota Deducible = base×21 %. Pre303 маппинг N2 → casilla 59 при NIF tipo 02 ЕС, иначе 120 `[INFERENCE: проверить по Traslado_Libros_a_Casillas_IVA 2026.xlsx]`. Файл: один на год, нарастающим итогом, имя `{ejercicio}{NIF}T{nombre}.xlsx` (T = unificado IVA+IRPF), ≤ 4 МБ.

### 11. Разобранные примеры (1T 2026, автономо-профессионал, не Beckham, 2-й год деятельности → 7 % retención)

**A. EU B2B** — Beispiel GmbH, DE123456789 (VIES ok), услуга разработки 3 000 € 2026-01-20.
Счёт: base 3 000,00; IVA — no sujeto; total 3 000,00. Оговорки: «Operación no sujeta al IVA español (art. 69.Uno.1º LIVA). Inversión del sujeto pasivo — art. 196 Directiva 2006/112/CE». NIF-IVA ES… и DE… 303: c59 += 3 000. 349 1T: DE | 123456789 | Beispiel GmbH | S | 3 000. Книга: N2, NIF tipo 02.

**B. US B2B** — Acme Inc., EIN 12-3456789, 5 000 USD, devengo 2026-02-10, курс ЕЦБ 1 EUR = 1,0800 USD → 4 629,63 €.
Счёт: 5 000,00 USD (equiv. 4 629,63 EUR, BCE 10/02/2026 1,0800); IVA — no sujeto; «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)». Без retención. 303: c120 += 4 629,63. 349 — нет. 347 — если за год > 3 005,06 € → включить (clave B) `[INFERENCE]`. Книга: N2, NIF tipo 06, país US.

**C. Spanish B2B** — Cliente SL, B12345678, консалтинг 2 000 €, 2026-03-05.
Счёт: base 2 000,00; IVA 21 % 420,00; retención IRPF 7 % −140,00; total factura 2 420,00; a pagar 2 280,00. 303: c07 += 2 000; c08 = 21; c09 += 420. Retención 140 → в IRPF (Modelo 130/100), клиент подаёт 111/190. 347: исключён (операция с retención). Книга: S1, clave 01, Tipo Retención 7, Importe 140, Total Factura 2 420.
Вариант Beckham-профессионал: retención 24 % = 480 → a pagar 1 940,00; empresarial/SL: retención 0 → a pagar 2 420,00.

**D. Spanish B2C** — физлицо, NIF 12345678Z, 500 €, 2026-03-20.
Счёт (полный или simplificada, т.к. ≤ 400 € нет — 605 > 400 → полный): base 500,00; IVA 21 % 105,00; total 605,00; без retención. 303: c07 += 500; c09 += 105.

**Расходы 1T**: coworking (ES) 300 + 63; ноутбук (ES) 1 500 + 315 (< 3 005,06 → не bien de inversión → 28/29); AWS (US) 100 € → ISP: c12 100 / c13 21; c28 100 / c29 21; SaaS из Ирландии (IE, VAT-id, мы в ROI) 200 € → AIS: c10 200 / c11 42; c36 200 / c37 42; 349 clave I: IE | … | 200.

**303 1T 2026**: c07 2 500; c09 525; c10 200; c11 42; c12 100; c13 21; c27 = 588,00; c28 1 900 (300+1 500+100); c29 399 (63+315+21); c36 200; c37 42; c45 = 441,00; c46 = 147,00; c59 3 000; c120 4 629,63; c66 147; c110 0; c78 0; c69 = c71 = 147,00 → **a ingresar 147,00**.
Если бы продаж C и D не было: c27 = 63; c45 = 441; c46 = −378 → 1T «a compensar» 378 (c72); во 2T c110 = 378 и т.д.; в 4T — c73 (devolver) всем остатком.

## Сроки и модели

| Modelo | Кто | Период | Срок | Когда не подаётся |
|---|---|---|---|---|
| 036 (alta, ROI casilla 582, cambio domicilio, baja) | все | событие | до начала деятельности / первой операции ЕС; смена domicilio — 1 месяц | — |
| 303 | все sujetos pasivos (autónomo и SL) | квартал | 1–20 апр/июл/окт; 4T 1–30 янв | никогда (даже «sin actividad» подаётся) |
| 390 | все, кто подаёт 303, кроме módulos/аренды/SII | год | 1–30 января | SII; только módulos/аренда |
| 349 | кто выполнял операции clave E/A/S/I… | квартал (месяц при > 50 000 €) | 1–20 след. месяца; последний период 1–30 янв | в периоде нет операций |
| 347 | все с контрагентами > 3 005,06 € (вне 349/190) | год | 1–28(29) февраля | SII; нет контрагентов выше порога |
| 369 (OSS) | зарегистрированные в Régimen de la Unión (alta Modelo 035) | квартал | до последнего дня след. месяца (даже нулевая) | не зарегистрирован |
| 360 | кто уплатил иностранный VAT в ЕС без права вычета в 303 | год | до 30 сентября след. года | опция |
| 111 / 190 | **клиент**, удерживающий retención (не мы) | квартал / год | 1–20 след. месяца; 190 — январь | — |
| Verifactu registros | все с SIF (IS, IRPF, IRNR-EP) | непрерывно | с 01.01.2027 (IS) / 01.07.2027 (IRPF); анонс переноса на 10.2028 | SII |
| e-factura B2B | получатель — предприниматель в Испании | — | 06.10.2027 (> 8 млн) / 06.10.2028 (остальные) | клиент за рубежом; simplificadas |
| Libros registro | все | непрерывно, итоги по кварталам | записи — до срока подачи 303 соответствующего периода (art. 69 RIVA) | SII (ведутся в Sede) |

## Пограничные случаи

- **Клиент ЕС без валидного VAT-id** (стартап до регистрации, частное лицо-«предприниматель»): трактовать как B2C (Reg. UE 282/2011 art. 18.2) → испанский 21 %; перевыставить без IVA можно rectificativa после получения VAT-id (DGT допускает, если статус предпринимателя на дату операции доказуем).
- **Мы без ROI, но клиент ЕС B2B**: операция всё равно no sujeta (локализация не зависит от ROI), но 349 требует NIF-IVA; клиент не найдёт нас в VIES → риск. Подать 036 casilla 582 до первого счёта.
- **Предоплата от иностранного клиента**: devengo в момент оплаты (art. 75.Dos) → счёт на аванс в периоде получения, курс — на дату оплаты; при no sujetas IVA нет, но в 59/120 попадает в квартале аванса.
- **Длящийся контракт (retainer) с иностранным клиентом** без ежемесячной exigibilidad: devengo 31 декабря (art. 75.Uno.7º) — для no sujetas влияет только на период 59/120 и 349.
- **Rectificativa по no sujeta** (скидка/возврат клиенту США): отражается уменьшением casilla 120 в периоде выставления rectificativa; если итог за квартал отрицательный — AEAT формы не принимают отрицательные информативные casillas → ставить 0 и переносить `[INFERENCE: проверить в Pre303]`.
- **Расходы при 100 % иностранных клиентах**: право на вычет полное (art. 94.Uno.2º), результат 303 стабильно отрицательный; возврат в 4T приходит в течение 6 месяцев (до ~конца июля), часто с requerimiento книг — поэтому книги в формате AEAT критичны. Альтернатива — REDEME (036, ноябрь на следующий год) с месячным 303 и обязательным SII.
- **Beckham**: на IVA не влияет никак; влияет только на retención в испанских B2B-счетах (24 %/0 %) и на то, что retención учитывается в Modelo 151, а не 100.
- **Переезд между автономными сообществами**: для IVA безразлично; обязательна 036 (cambio de domicilio fiscal) в течение месяца; серия счетов и нумерация не меняются; адрес в счёте — новый с даты смены.
- **Canarias/Ceuta/Melilla**: клиент-предприниматель там → no sujeta, casilla 120 (не 59), не 349; клиент-потребитель → 21 %. Поставщик оттуда — ISP как с третьей страной (12/13 + 28/29). Не путать с экспортом (casilla 60 — только товары).
- **Северная Ирландия (XI)**: только для товаров сохраняет статус ЕС; услуги B2B в UK/XI — вне ЕС → casilla 120.
- **Автомобиль**: 50 % cuota на покупку/лизинг/топливо/парковку; доказать > 50 % почти невозможно для консультанта; пример: лизинг 400 + 84 → вычет 42 (base в книге 400 без prorrateo, Cuota Deducible 42).
- **Домашний офис**: IVA с коммунальных услуг жилья, используемого частично, не вычитается (art. 95.Uno; критерий AEAT/TEAC), хотя в IRPF 30 % доли вычитаемы; аренда жилья — exenta, IVA нет.
- **Ресторан/гостиница/поездки**: IVA вычитаем только если расход вычитаем в IRPF/IS (командировка с документальным подтверждением) и есть полный счёт с NIF (не тикет).
- **Ноутбук/оборудование < 3 005,06 €**: не bien de inversión для IVA → casilla 28/29, без регуляризации; ≥ 3 005,06 € → 30/31 и 5-летняя регуляризация, если изменится prorrata/использование.
- **SaaS из США без счёта с NIF** (только receipt): для ISP достаточно justificante contable (art. 97.Uno.4º), но он должен идентифицировать поставщика, услугу, дату и сумму; хранить.
- **Электронные услуги B2C в ЕС**: продажа подписок/курсов европейским частным лицам → следить за порогом 10 000 € (включая прошлый год); при превышении — alta OSS (Modelo 035) и Modelo 369; IVA по ставке страны клиента; нужны 2 доказательства местоположения клиента (IP, адрес, банк).
- **Factura simplificada иностранному клиенту** — запрещена; и в Verifactu тип F2 не подойдёт — только F1.
- **SL vs autónomo**: IVA идентичен; SL — всегда электронная подача с сертификатом, подпадает под e-factura B2B как юрлицо (статусы с 06.10.2028), Verifactu как IS-плательщик с 01.01.2027 (если перенос не оформят).
- **Verifactu при self-hosted софте**: обязательна declaración responsable на каждую версию, NIF продюсера = NIF пользователя; удобнее режим VERI*FACTU (не нужна XAdES-подпись и registro de eventos, выше доверие при возвратах). Бесплатная альтернатива — приложение AEAT (но тогда счета ведутся только в нём).
- **Клиент испанский, но платит из-за рубежа / в валюте**: локализация по клиенту (TAI) → 21 % независимо от валюты; cuota в евро по курсу на devengo.

## Неясности

1. **Verifactu — реальная дата старта.** Нормативно (RDL 15/2025) — 01.01.2027 / 01.07.2027; Hacienda 05.10.2026 объявила перенос «обязанностей, ещё не вступивших в силу» на октябрь 2028 (совместить с e-factura для < 8 млн), но RD ещё не опубликован; AEAT пишет «previsión». Осторожная реализация: собрать SIF по требованиям RRSIF/OM уже сейчас (цепочка, XML, QR), включать обязательную отправку/подпись по фактически действующей дате; следить за BOE.
2. **E-factura B2B — технический формат для нашего профиля.** RD 238/2026 ссылается на синтаксисы и SPFE (solución pública) с обязанностью отправки копии при использовании частной платформы; детали форматов (Facturae/UBL/CII) и API SPFE в Orden HAC/1028/2026 не проверены — **UNVERIFIED**. Для одного-двух испанских клиентов проще использовать SPFE напрямую с 06.10.2028.
3. **Pre303 маппинг N2 → 59 vs 120** по типу NIF клиента — не подтверждён первичкой (`Traslado_Libros_a_Casillas_IVA 2026.xlsx` не читался). Осторожно: не полагаться на автоимпорт, считать 59/120 самим.
4. **347 для иностранных (вне ЕС) клиентов/поставщиков по услугам**: текст art. 33 RGAT исключает только импорт/экспорт *товаров*; практика AEAT — включать; **UNVERIFIED** по INFORMA. Осторожно: включать (избыточная подача безвредна; пропуск — infracción art. 198/199 LGT).
5. **Курс для no sujetas и для IRPF**: art. 79.Once формально про IVA; для суммы дохода в IRPF/книгах применяется тот же принцип (devengo) по доктрине DGT, альтернативные источники допустимы (V2630-17). Осторожно: один источник (ЕЦБ, день devengo; выходные — последний опубликованный), курсовая разница при оплате — финансовый результат вне IVA.
6. **Отрицательные информативные casillas 59/120** при rectificativas: поведение формы не проверено. Осторожно: ограничивать нулём и переносить остаток корректировки на следующий квартал с пометкой в книге.
7. **Beckham + empresarial vs profesional**: квалификация деятельности (IAE sección 1ª vs 2ª) определяет 24 % или 0 % retención — решает модуль Beckham/IRPF; здесь движок только принимает флаг. Статус «actividad emprendedora» (ENISA) не влияет на IVA.
8. **Валидационный допуск ±10 €** между base×tipo и cuota в Verifactu/SII — по памяти из документа валидаций AEAT, версия 2026 не перепроверена — **UNVERIFIED**; движок всё равно считает точно, допуск нужен лишь при импорте чужих счетов.
9. **390 casillas по ставкам** (05/06 для 21 %) — выведены из диапазона инструкции «01–06», не сверены с формуляром — `[INFERENCE]`. Остальные номера 390 (27/28, 545–552, 48–55, 84–86, 95–98, 99–110, 125–126, 108) взяты из Instrucciones 390-2025.
10. **Ставки IVA 2027** — изменений не опубликовано; RETA/IRPF вне этого файла.
11. **Код XI / UK после Brexit для услуг** — UK полностью «третья страна» для услуг (casilla 120), XI только для товаров; доп. подтверждения не искали.
12. **REDEME**: условия (отсутствие долгов, SII) и срок опции (ноябрь) — по общему знанию art. 30 RIVA, не перечитывались — **UNVERIFIED**.

### Основные источники

- LIVA (Ley 37/1992) консолидированная: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- RD 1619/2012 (Reglamento de facturación) консолидированный, с изменениями RD 1007/2023 и RD 238/2026: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Instrucciones Modelo 303 2026 (AEAT): https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
- Формуляр 303 (Manual IVA 2025, anexo): https://sede.agenciatributaria.gob.es/static_files/Sede/Biblioteca/Manual/Practicos/IVA/IVA_2025/Imagenes/Cap_9_303_eu_es.pdf
- Instrucciones 390-2025: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
- Instrucciones 349: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
- 347 excluidas: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
- RD 1007/2023 (RRSIF): https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; RDL 15/2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Hacienda nota 05.10.2026 (перенос на 10.2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- AEAT Verifactu FAQ (обновл. 21.07.2026): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html ; spec huella: https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/Veri-Factu_especificaciones_huella_hash_registros.pdf
- E-factura: RD 238/2026 https://www.boe.es/eli/es/rd/2026/03/25/238/con ; календарь AEAT https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html
- Libros registro формат: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; LSI.xlsx: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx ; Orden HAC/773/2019: https://www.boe.es/eli/es/o/2019/06/28/hac773
- Retenciones 2026 (с 10.09.2026): https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; RD 1008/2023 (Beckham 24 %): https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
- Modelo 037 упразднён / ROI casilla 582: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 ; https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html
- Электронные услуги B2C/OSS: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html ; Orden HAC/610/2021 (Modelo 369): https://www.boe.es/eli/es/o/2021/06/16/hac610
- Курс валют: DGT V2630-17 (через Iberley): https://www.iberley.es/resoluciones/resolucion-vinculante-dgt-v2630-17-16-10-2017-1473112 ; ECB reference rates: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.es.html
