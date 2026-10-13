*Переведено с испанского оригинала [kb/iva-facturacion.md](../iva-facturacion.md) 13.10.2026. Источник истины — испанский файл.*

# IVA и выставление фактур для autónomo / SL, оказывающих услуги

Состояние на 2026-10-08. Первичные источники: BOE, AEAT Sede, DGT. Всё, что не удалось подтвердить первичным источником, помечено как **UNVERIFIED** или `[INFERENCE]`.

## Краткое содержание

- IVA не зависит от régimen Beckham, от автономного сообщества (Valencia/Asturias) и от правовой формы (autónomo/SL). Правила одинаковые. Регион важен только на Канарских островах, в Сеуте и Мелилье. Там нет IVA, а действуют IGIC/IPSI.
- Услуги B2B клиенту-предпринимателю из другой страны ЕС: операция **не облагается (no sujeta)** в Испании (art. 69.Uno.1º LIVA). IVA платит клиент по механизму inversión del sujeto pasivo (reverse charge). Нужен alta в ROI (Modelo 036, casilla 582). NIF-IVA клиента проверяется в VIES. Modelo 303 → casilla **59**. Modelo 349 → clave **S**.
- Услуги B2B клиенту вне ЕС (США и т. д.): **no sujeta** (art. 69.Uno.1º), без упоминания inversión del sujeto pasivo. С 2023 года правило «фактического использования или эксплуатации» (art. 70.Dos) не применяется к услугам B2B, как наши. Modelo 303 → casilla **120**. В 349 не включается.
- Испанский клиент (B2B или B2C): IVA 21 %. Если клиент является предпринимателем/профессионалом, а исполнитель является физическим лицом с *профессиональной* деятельностью, фактура содержит retención IRPF. В общем режиме это 15 % (7 % в первые 3 года). В régimen Beckham это **24 %**. При *предпринимательской* деятельности и в SL retención нет.
- B2C клиенту из ЕС: испанский IVA 21 % (art. 69.Uno.2º). Исключение: электронные и телекоммуникационные услуги. До 10 000 €/год применяется испанский IVA. Выше этого порога (или по выбору) применяется IVA страны клиента через OSS (Modelo 369, casilla 123 в 303).
- B2C клиенту вне ЕС: консалтинг, разработка и обработка данных (список art. 69.Dos) и электронные услуги являются **no sujetas** (casilla 120). Остальное облагается по ставке 21 %.
- Право на вычет входящего IVA (IVA soportado) **сохраняется**, когда услуги оказываются иностранным клиентам (art. 94.Uno.2º LIVA). Prorrata не нужна, если нет освобождённых операций без права на вычет (art. 20). Типичный профиль (все клиенты за границей) ⇒ 303 почти всегда выходит «a compensar». Возврат (devolución) можно получить только в 4T (casilla 73) или через REDEME/SII.
- Услуги, полученные от поставщиков из ЕС (SaaS и т. д.): самоначисление (autorrepercusión), casillas 10/11 и 36/37, 349 clave **I**. От поставщиков вне ЕС: casillas 12/13 и 28/29. В 349 не включаются.
- Фактура (RD 1619/2012 art. 6): номер/серия, дата, стороны с NIF и адресом, описание, база, ставка, сумма налога (cuota), дата операции, если она отличается, обязательные пометки для освобождённых операций / no sujetas / ISP. Валюта может быть любой. Но **cuota IVA должна быть выражена в евро** по курсу на дату devengo. Factura simplificada допускается до 400 € с IVA. Но она запрещена в фактурах иностранным клиентам (art. 4.4.d).
- Modelo 390 **обязательна** для нашего профиля. Освобождены только módulos, аренда недвижимости и SII. Modelo 347: только контрагенты с суммой более 3 005,06 €/год. Исключаются операции, задекларированные в 349, и операции с retención.
- Verifactu (RD 1007/2023, Orden HAC/1177/2024): по RDL 15/2025 сроки такие. Плательщики IS с 01.01.2027. Остальные (autónomos в IRPF) с 01.07.2027. **05.10.2026 Hacienda объявила перенос до октября 2028 года.** Норма ещё не опубликована. Программа собственной разработки тоже должна соответствовать требованиям (цепочка хешей SHA-256, QR 30–40 мм, записи XML). Для неё нужна собственная declaración responsable.
- Электронная фактура B2B (Ley Crea y Crece, RD 238/2026, Orden HAC/1028/2026): обязательна, когда получатель является предпринимателем в Испании. Сроки: с **06.10.2027** (volumen de operaciones > 8 млн) и с **06.10.2028** (все остальные). К иностранным клиентам не применяется.
- Libros registro: выставленные фактуры, полученные фактуры и инвестиционные активы (bienes de inversión). Официальный формат AEAT — XLSX (LSI.xlsx) с листами EXPEDIDAS_INGRESOS / RECIBIDAS_GASTOS / BIENES-INVERSIÓN. Этот же файл импортируется в Pre303, Renta Web и Modelo 130.
- Хранение фактур: срок давности по LGT (4 года с окончания срока подачи соответствующей декларации). Для bienes de inversión срок больше (период регуляризации + 4 года). SL должна дополнительно хранить их 6 лет по Código de Comercio.

## Правила

1. **Общее правило места оказания услуг B2B**: услуга считается оказанной там, где находится клиент-предприниматель (головной офис / EP / адрес). Если клиент не находится в TAI (полуостров + Балеарские острова), операция является *no sujeta* в Испании. Действует с 01.01.2010 (Ley 2/2010). Источник: art. 69.Uno.1º LIVA — https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a69
2. **Общее правило B2C**: услуга считается оказанной там, где находится исполнитель (TAI) ⇒ испанский IVA 21 %. Исключение art. 69.Dos: перечисленные услуги являются no sujetas, если они оказаны клиенту-непредпринимателю **вне ЕС** (не Канарские острова / Сеута / Мелилья). В перечень входят: права интеллектуальной собственности, реклама, консультирование / консультанты / инжиниринг / юридические услуги, обработка данных и предоставление информации, перевод, предоставление персонала, аренда движимого имущества и т. д. Источник: art. 69.Dos LIVA (та же ссылка).
3. **Электронные услуги B2C** (хостинг, SaaS/подписки, скачиваемое ПО, онлайн-курсы без участия человека — art. 69.Tres.4º): если клиент находится в другой стране ЕС, применяется испанский IVA. Условия: сумма этих услуг плюс дистанционные продажи не превышает **10 000 €** (без IVA) в текущем и в предыдущем году, и не выбрано налогообложение в стране назначения (art. 70.Uno.8º, art. 73). Выше порога применяется IVA страны клиента (OSS/Modelo 369). Если клиент находится вне ЕС, операция является no sujeta (AEAT). Источники: art. 70.Uno.4º/8º, art. 73 LIVA; AEAT «IVA telecomunicaciones y servicios electrónicos» https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html
4. **Фактическое использование или эксплуатация (art. 70.Dos)**: после Ley 31/2022 и Ley 13/2023 правило применяется только к (1) услугам art. 69.Dos, оказанным клиентам-непредпринимателям, и (2) аренде транспортных средств, если они фактически используются в TAI. Оно не применяется к консалтингу и разработке B2B для клиента вне ЕС. Источник: art. 70.Dos LIVA (консолидированный текст).
5. **Налогоплательщик (sujeto pasivo) по услугам, полученным от нерезидента** (art. 84.Uno.2º.a): получатель-предприниматель в TAI сам начисляет IVA (inversión del sujeto pasivo). Документ, который даёт право на вычет, — фактура поставщика или бухгалтерский justificante (art. 97.Uno.4º). Отдельная «autofactura» не нужна. Источник: art. 84, 97 LIVA.
6. **Право на вычет** (art. 94.Uno): его дают, среди прочего, операции пункта 2º: «Операции, совершённые за пределами территории применения налога, которые давали бы право на вычет, если бы были совершены внутри неё». ⇒ Услуги иностранным клиентам (B2B ЕС / вне ЕС, no sujetas) **дают право на вычет**. Prorrata (art. 102–106) применяется, только если одновременно есть операции с правом и без права на вычет (освобождённые по art. 20). Источник: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a94
7. **Ограничения вычета**: art. 95: только расходы, прямо и исключительно связанные с деятельностью. Bienes de inversión частичного использования: пропорционально использованию. Легковые автомобили (turismos): презумпция **50 %** (и те же 50 % для топлива, парковки, ремонта и запчастей, art. 95.Cuatro). Art. 96: никогда не вычитаются ювелирные изделия, еда/напитки/табак, зрелищные мероприятия, представительские расходы на клиентов, поездки/отели/рестораны, кроме случая, когда расход вычитается в IRPF/IS. Источник: art. 95–96 LIVA.
8. **Формальные требования к вычету** (art. 97): оригинал фактуры на имя налогоплательщика со всеми данными art. 6 RD 1619/2012. «Tique» (factura simplificada без NIF получателя) не даёт права на вычет. Исключение: продавец добавил NIF и адрес получателя и cuota отдельной строкой (art. 7.2 RD 1619/2012). Срок для применения вычета: 4 года с devengo (art. 99.Tres, 100 LIVA).
9. **Devengo для услуг** (art. 75): в момент оказания услуги (75.Uno.2º). При предоплате: в момент получения оплаты (75.Dos). Длящиеся услуги (tracto sucesivo, 75.Uno.7º): когда становится подлежащей оплате каждая часть цены. Если срок оплаты не наступает в течение одного года: 31 декабря каждого года. Источник: art. 75 LIVA.
10. **Обязанность выставить фактуру** (RD 1619/2012 art. 2): во всех операциях, включая no sujetas и освобождённые, если клиент является предпринимателем/профессионалом или юридическим лицом. Также когда операция имеет место вне TAI, но исполнитель находится в TAI (art. 2.3.b.b’). Срок: B2B — до 16-го числа месяца, следующего за devengo (art. 11); B2C — в момент операции. Отправка клиенту выполняется в тот же срок (art. 18). Источник: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
11. **Содержание фактуры** (art. 6 RD 1619/2012): a) номер и серия (сквозная нумерация внутри серии; отдельные серии обязательны для rectificativas и для фактур, выставленных получателем или третьим лицом); b) дата выставления; c) полные имя и фамилии или наименование (razón social) сторон; d) NIF исполнителя; NIF клиента обязателен при ISP, в операциях в TAI и при EIB; e) адреса сторон; f) описание, цена за единицу без IVA, скидки; g) ставка; h) cuota отдельно; i) дата операции, если она отличается; j) при освобождении — ссылка на статью Directiva 2006/112/CE или LIVA, или «указание на то, что операция освобождена»; m) «inversión del sujeto pasivo», если налогоплательщиком является получатель; p) «специальный режим кассового метода (régimen especial del criterio de caja)». В операциях art. 2.3.b.b’.a’’ (B2B ЕС) можно не указывать f/g/h. Вместо этого указываются количество и характер услуги и налогооблагаемая сумма (art. 6.3). С 07.12.2023, art. 6.5: если используется SIF, на фактуру добавляется QR и (только в модальности VERI*FACTU) фраза «VERI*FACTU»/«Factura verificable en la sede electrónica de la AEAT» (фактура, проверяемая в электронной Sede AEAT).
12. **Factura simplificada** (art. 4, 7): до 400 € с IVA (до 3 000 € в перечисленных видах розничной деятельности) и для rectificativas. Её **нельзя** использовать при EIB и в операциях, место которых находится вне TAI (art. 4.4.d → art. 2.3.b.b’). То есть иностранным клиентам всегда выставляется полная фактура (factura completa).
13. **Factura rectificativa** (art. 15): обязательна при ошибке в данных, неверной cuota или изменении базы (art. 80 LIVA). Выставляется, как только становится известна причина, в течение 4 лет с devengo. Ведётся в отдельной серии. Содержит данные исправляемой фактуры и содержание исправления. Суммы указываются как разница (со знаком) или «в том виде, в каком они остаются после проведённого исправления», с указанием разницы. Отражение в 303: casillas 14/15 («Modificación bases y cuotas») в операциях с IVA. В no sujetas исправляется сумма casilla 59/120 периода.
14. **Валюта и язык** (art. 12 RD 1619/2012; art. 79.Once LIVA): суммы могут быть в любой валюте. Но cuota IVA указывается в евро по «курсу продавца, установленному Banco de España» на дату devengo. По DGT V2630-17, BdE такой курс не устанавливает: применяется референсный курс ЕЦБ (BCE), который публикует BdE. Допускается другой публичный источник, если он применяется последовательно и не отклоняется существенно. Язык: любой. AEAT может потребовать перевод на кастильский (castellano).
15. **Хранение** (art. 19–23 RD 1619/2012; art. 66–70 LGT): полученные фактуры, копии выставленных, бухгалтерские justificantes и DUA хранятся в течение срока давности (4 года). Нужно обеспечить подлинность, целостность, читаемость и онлайн-доступ AEAT. Хранение за пределами Испании допускается только в электронном виде, с удалённым доступом и с предварительным уведомлением AEAT. Bienes de inversión: до конца периода регуляризации (5 лет; недвижимость — 10) + срок давности. SL: 6 лет по art. 30 Código de Comercio.
16. **ROI / NIF-IVA**: до первой внутриевропейской операции подайте Modelo 036 с casilla **582** (alta в ROI) и датой первой операции в casilla **584**. Modelo 037 отменена 03.02.2025 (Orden HAC/1526/2024). Если AEAT не отвечает в течение 3 месяцев, заявление считается отклонённым. Источник: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html ; BOE-A-2025-410.
17. **Modelo 303**: ежеквартально (1–20 апреля/июля/октября; 4T: 1–30 января). Devolución (casilla 73): только в последней декларации года, если вы не в REDEME (art. 30 RIVA). В 1T–3T отрицательный результат может быть только «a compensar» (casilla 72). В инструкциях сказано: «Результат самостоятельного расчёта не может быть A COMPENSAR, если заполнена casilla (78), то есть если в подаваемом самостоятельном расчёте были применены суммы к зачёту, образовавшиеся в предыдущих периодах». Источник: Instrucciones 303 2026 — https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
18. **Modelo 390**: обязательна для всех, кто подаёт периодические 303, кроме (a) тех, кто ежеквартально декларирует только упрощённый режим (régimen simplificado) и/или аренду городской недвижимости, и (b) обязанных по SII. Срок: 1–30 января. Источник: Instrucciones 390-2025 — https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
19. **Modelo 349**: подаётся за каждый период, в котором есть операции с claves E/A/S/I/T/M/H/R/D/C. Периодичность ежеквартальная, если сумма EIB + услуг ЕС (claves E, S и другие) не превысила **50 000 €** без IVA ни в текущем квартале, ни в одном из 4 предыдущих кварталов. Иначе периодичность ежемесячная. Если порог превышен во 2-м месяце, подаётся месячная декларация за первые два месяца квартала и отмечается поле «INDICADOR CAMBIO PERIODICIDAD EN LA OBLIGACIÓN DE DECLARAR». Сроки: 1–20 следующего месяца; за последний период года — 1–30 января; за июль — до 20 сентября (ежемесячные). Источник: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
20. **Modelo 347**: ежегодно, в феврале (1–28/29). Включает контрагентов, с которыми за год превышено **3 005,06 €** (с IVA), с разбивкой по кварталам. Исключаются: операции без обязанности выставлять фактуру, импорт/экспорт товаров и операции, уже задекларированные в других периодических декларациях с тем же содержанием (349, retenciones 190/180). Не подают: обязанные по SII и лица, у которых есть только исключённые операции. Источник: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
21. **Retención IRPF в фактуре профессионала** испанскому плательщику-предпринимателю: 15 % (art. 101.5.a LIRPF). 7 % в год начала и в два следующих года, если в предыдущем году профессиональная деятельность не велась и клиенту передано письменное уведомление (art. 95.1 RIRPF). Régimen Beckham: retenciones по правилам IRNR. Профессиональная деятельность — **24 %**; предпринимательская деятельность — без retención (art. 114 RIRPF в редакции RD 1008/2023). Источники: https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
22. **Verifactu: сфера и сроки**: RRSIF (RD 1007/2023) применяется к плательщикам IS, IRPF с экономической деятельностью, IRNR с EP и к ERAR. Не применяется к обязанным по SII. Сроки по RDL 15/2025: IS — до 01.01.2027; остальные — до 01.07.2027. 05.10.2026 Министерство объявило о намерении перенести срок до **октября 2028 года** (чтобы согласовать его с электронной фактурой). Пока норма не опубликована, действуют даты 2027 года. Источники: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf ; https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
23. **Verifactu: требования к SIF** (RRSIF art. 8–16; Orden HAC/1177/2024 art. 10–21): на каждую фактуру — запись о регистрации фактуры (registro de facturación de alta, XML UTF-8). На каждую отмену — запись об отмене (registro de anulación). Цепочка отпечатков SHA-256 (поле Huella предыдущей записи). Кроме того, один из двух вариантов: отправка всех записей в AEAT (модальность VERI*FACTU, веб-сервис, контроль потока 60 с) или подпись XAdES квалифицированным сертификатом + журнал событий. QR размером 30×30–40×40 мм, ISO/IEC 18004, уровень M, с URL AEAT (NIF, серия+номер, дата, общая сумма). Фраза «VERI*FACTU» добавляется, только если записи отправляются. Источник: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
24. **Declaración responsable** (RRSIF art. 13; OM art. 15): обязательна для каждой версии любого SIF, включая **программу собственной разработки для собственного использования**. В этом случае её подписывает сам разработчик-пользователь. Внешней сертификации и реестра нет. Источник: FAQ AEAT — https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/certificacion-sistemas-informaticos-declaracion-responsable.html
25. **Электронная фактура B2B** (Ley 18/2022 art. 12; RD 238/2026; Orden HAC/1028/2026, действует с 06.10.2026): обязательна, когда получатель является предпринимателем/профессионалом с головным офисом / EP / адресом в Испании. Не применяется к simplificadas (кроме фактур art. 7.2). Сроки: 06.10.2027 — эмитенты с volumen de operaciones > 8 млн €; 06.10.2028 — остальные. Передача статусов (принята/оплачена): 06.10.2027 / 06.10.2028 (юридические лица) / 06.10.2029 (физические лица). Источник: https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html ; https://www.boe.es/eli/es/rd/2026/03/25/238/con
26. **Libros registro** (art. 62–70 RIVA; Orden HAC/773/2019 для IRPF): выставленные фактуры, полученные фактуры, bienes de inversión (+ некоторые внутриевропейские операции, которые нас не касаются). Записи в евро, в хронологическом порядке, с итогами по кварталам. Rectificativas — отдельно. Электронный формат AEAT: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; структура полей: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx
27. **Volumen de operaciones** (art. 121 LIVA) = сумма вознаграждений по всем операциям года (включая no sujetas по правилам места оказания и освобождённые), без IVA. Исключаются поставки bienes de inversión и нерегулярные финансовые операции / операции с недвижимостью. Используется в 303 (4T, casilla 88 «Total volumen de operaciones», для тех, кто освобождён от 390), в 390 (casilla 108 «Volumen de operaciones») и для порога 8 млн для электронной фактуры.

## Цифры

### Ставки и пороги (2025 и 2026, без изменений для нашего профиля)

| Параметр | 2025 | 2026 | Источник |
|---|---|---|---|
| Общая ставка IVA | 21 % | 21 % | art. 90 LIVA |
| Пониженная / сверхпониженная ставка | 10 % / 4 % (0 % и 5 %/7,5 % применялись только к продуктам питания до 2024 года) | 10 % / 4 % | art. 91 LIVA |
| Порог OSS (B2C электронные услуги + дистанционные продажи в ЕС) | 10 000 € без IVA | 10 000 € | art. 73 LIVA |
| Порог ежемесячной 349 | 50 000 € без IVA (квартал и 4 предыдущих) | 50 000 € | art. 81 RIVA |
| Порог 347 на контрагента | > 3 005,06 € с IVA | > 3 005,06 € | art. 33 RGAT |
| Bien de inversión (IVA) | ≥ 3 005,06 € и использование > 1 года | так же | art. 108 LIVA |
| Factura simplificada | ≤ 400 € с IVA (≤ 3 000 € в розничной торговле) | так же | art. 4 RD 1619/2012 |
| Презумпция использования автомобиля в деятельности | 50 % | 50 % | art. 95.Tres.2ª LIVA |
| Prorrata: округление | вверх, до целого % | так же | art. 104.Dos LIVA |
| Обязательная специальная prorrata | если общая даёт вычет на ≥ 10 % больше | так же | art. 103.Dos.2º |
| Крупное предприятие (ежемесячная 303, SII) | > 6 010 121,04 € volumen de operaciones за предыдущий год | так же | art. 71.3 RIVA |
| Retención профессионала (общий IRPF) | 15 % / 7 % (начало) | 15 % / 7 % | art. 101.5 LIRPF, 95.1 RIRPF |
| Retención профессионала (Beckham, IRNR) | 24 % | 24 % | art. 114 RIRPF |
| Срок вычета входящего IVA | 4 года с devengo | 4 года | art. 99–100 LIVA |
| Хранение фактур | 4 года (срок давности) | 4 года | art. 66 LGT, art. 19 RD 1619/2012 |
| Срок выставления фактуры B2B | до 16-го числа следующего месяца | так же | art. 11 RD 1619/2012 |

### Сроки (календарь)

| Modelo | Период | Срок | Domiciliación (−5 дней) |
|---|---|---|---|
| 303 | 1T/2T/3T | 1–20 апр / июл / окт | до 15-го числа |
| 303 | 4T | 1–30 января | до 25 января |
| 390 | год | 1–30 января | — |
| 349 ежеквартальная | 1T–3T | 1–20 апр / июл / окт | — |
| 349 | 4T (или декабрь) | 1–30 января | — |
| 347 | год | 1–28(29) февраля | — |
| 369 (OSS) | квартал | до последнего дня месяца, следующего за кварталом | — |
| 036 alta ROI | — | до первой операции в ЕС | — |
| 036 смена налогового адреса | — | 1 месяц со дня смены (art. 10 RGAT) | — |

Если последний день нерабочий (выходной или праздник), срок переносится на следующий рабочий день (календарь AEAT).

### Verifactu / электронная фактура: даты

| Обязанность | Дата | Статус |
|---|---|---|
| Адаптированный SIF: плательщики IS | 01.01.2027 | действует (RDL 15/2025) |
| Адаптированный SIF: autónomos в IRPF и остальные | 01.07.2027 | действует (RDL 15/2025) |
| Перенос всего RRSIF на октябрь 2028 года | ~10.2028 | объявлен 05.10.2026, **норма не опубликована** |
| Электронная фактура B2B, volumen de operaciones > 8 млн € | 06.10.2027 | действует (RD 238/2026 + OM HAC/1028/2026) |
| Электронная фактура B2B, остальные (наш профиль) | 06.10.2028 | действует |
| Передача статусов электронной фактуры, физические лица | 06.10.2029 | действует |

### Casillas Modelo 303 (форма 2025/2026): карта для нашего профиля

| Операция | Начисленный IVA (база/ставка/cuota) | IVA к вычету (база/cuota) | Дополнительная информация | 349 |
|---|---|---|---|---|
| Продажа испанскому клиенту по ставке 21 % | 07 / 08 / 09 | — | — | — |
| Продажа B2B клиенту из ЕС (услуга) | — | — | **59** | S |
| Продажа B2B клиенту вне ЕС, Канарские острова / Сеута / Мелилья | — | — | **120** | — |
| Продажа B2C вне ЕС услуг art. 69.Dos / электронных услуг | — | — | 120 | — |
| Продажа B2C в ЕС электронных услуг через OSS | — (в 369) | — | 123 | — |
| Экспорт товаров (art. 21) | — | — | 60 | — |
| Операции с ISP, в которых налогоплательщиком является испанский клиент (art. 84.Uno.2º c–g; не наш случай) | — | — | 122 | — |
| Покупка у испанского поставщика (текущие расходы) | — | 28 / 29 | — | — |
| Покупка bien de inversión в Испании | — | 30 / 31 | — | — |
| Импорт товаров (DUA) | — | 32 / 33 (34/35 инвестиции) | — | — |
| Услуга поставщика из ЕС (AIS) | **10 / 11** | **36 / 37** | — | I |
| Товар из ЕС (AIB) | 10 / 11 | 36 / 37 (38/39 инвестиции) | — | A |
| Услуга поставщика вне ЕС (ISP art. 84.Uno.2º.a) | **12 / 13** | **28 / 29** | — | — |
| Rectificativa с IVA (±) | 14 / 15 | 40 / 41 (полученные) | — | — |
| Итоги | 27 = 152+167+03+155+06+09+11+13+15+158+170+18+21+24+26 | 45 = 29+31+33+35+37+39+41+42+43+44 | 46 = 27 − 45 | |
| Результат | 64 = 46+58+76 (Suma de resultados); 65 = 100 %; 66 = 64; 110 (Cuotas a compensar pendientes de periodos anteriores); 78 (Cuotas a compensar de periodos anteriores aplicadas en este periodo); 87 = 110−78; 69 = 66+77−78+68+108 (Resultado de la autoliquidación); 71 = 69−70+109 | | 72 (Compensación) / 73 (Devolución, только 4T) | |

### Casillas Modelo 390 (2025): основные

| Содержание | Casillas |
|---|---|
| Régimen ordinario по ставкам, база/cuota | 0 %: 700/701; 2 %: 667/668; 4 %: 01/02; 5 %: 702/703; 7,5 %: 669/670; 10 %: 03/04; 21 %: 05/06 |
| Adquisiciones intracomunitarias de servicios, база/cuota по ставкам | 4 %: 545/546; 10 %: 547/548; 21 %: 551/552 (0, 2, 5 и 7,5 %: 720–723, 687–690) |
| Adquisiciones intracomunitarias de bienes, база/cuota по ставкам | 4 %: 21/22; 10 %: 23/24; 21 %: 25/26 (0, 2, 5 и 7,5 %: 716–719, 683–686) |
| IVA devengado en otros supuestos de inversión del sujeto pasivo (поставщик вне ЕС) | 27 / 28 |
| Modificación de bases y cuotas | 29 / 30 |
| Total bases y cuotas IVA / Total cuotas de IVA y recargo de equivalencia | 33 / 34; 47 |
| IVA deducible en operaciones interiores. Bienes y servicios corrientes | по ставкам 4 %: 190/191; 10 %: 603/604; 21 %: 605/606; итого 48 / 49 |
| IVA deducible en operaciones interiores. Bienes de inversión | по ставкам 4 %: 196/197; 10 %: 611/612; 21 %: 613/614; итого 50 / 51 |
| IVA deducible en adquisiciones intracomunitarias. Bienes de inversión / Servicios | по ставкам 4 %: 220/221 / 587/588; 10 %: 631/632 / 635/636; 21 %: 633/634 / 637/638; итого 58 / 59 и 597 / 598 |
| IVA deducible en importaciones. Bienes corrientes / Bienes de inversión | 52 / 53; 54 / 55 |
| Suma de resultados / Compensación de cuotas del ejercicio anterior / Resultado de la liquidación | 84, 85, 86 |
| Total resultados a ingresar en las autoliquidaciones de IVA del ejercicio / A compensar / A devolver | 95, 97, 98 |
| Volumen de operaciones: Operaciones en régimen general / Entregas intracomunitarias de bienes y servicios / Exportaciones y otras operaciones exentas con derecho a deducción / Operaciones exentas sin derecho a deducción / Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 126) / Operaciones sujetas con inversión del sujeto pasivo / Operaciones no sujetas por reglas de localización acogidas a los regímenes especiales de ventanilla única / Volumen de operaciones | 99, 103, 104, 105, 110, 125, 126, 108 |

### Claves для libros registro и записей Verifactu

| Поле | Значения |
|---|---|
| Calificación de la operación | S1 облагаемая, не освобождённая, без ISP; S2 облагаемая с ISP; N1 no sujeta art. 7/14; **N2 no sujeta по правилам места оказания (reglas de localización)** |
| Operación exenta | E1 art. 20; E2 art. 21; E3 art. 22; E4 art. 23–24; E5 art. 25 (EIB); E6 прочие |
| Clave de régimen | 01 общий; 02 экспорт; 07 кассовый метод (criterio de caja); 08 IGIC/IPSI; 17 OSS; 18 recargo de equivalencia … |
| Tipo de factura (Verifactu) | F1 полная; F2 simplificada; F3 заменяющая simplificadas; R1–R4 rectificativas (R1 ошибка в праве / art. 80.Uno-Dos-Seis, R2 art. 80.Tres, R3 art. 80.Cuatro, R4 прочие); R5 rectificativa для simplificada |
| Tipo NIF destinatario (libros) | 02 NIF-IVA ЕС; 03 паспорт; 04 официальный документ страны; 05 сертификат резидентства; 06 другой подтверждающий документ; 07 не зарегистрирован в censo |

## Формулы для движка

Во всех случаях: суммы в евро, 2 знака после запятой, округление `ROUND_HALF_UP` (как в формах AEAT). Cuota рассчитывается по каждой фактуре (по каждой ставке). В libros и в 303 суммируется уже округлённая cuota. Валидации AEAT (SII/Verifactu) допускают отклонение `|cuota − base×tipo| ≤ 10 €` на фактуру `[по документу валидаций AEAT; подтвердить версию]`.

### 1. Классификация продажи (место оказания + режим фактуры)

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
    withholding = compute_withholding(seller, customer)          # см. пункт 3
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
    if service.kind in {ART69DOS, ELECTRONIC}: regime = NO_SUJETA_LOCALIZACION   # art. 69.Dos / позиция AEAT
    else: regime = SUJETA_21                                     # общее правило art. 69.Uno.2º
    if effectively_used_in_TAI(service): regime = SUJETA_21     # art. 70.Dos (только B2C art. 69.Dos)
```

Канарские острова / Сеута / Мелилья: B2B → NO_SUJETA_LOCALIZACION (casilla 120, не 59; 349 не подаётся); B2C → SUJETA_21 (art. 69.Dos их исключает).

### 2. Строки фактуры в зависимости от режима

```
base      = Σ round(qty × unit_price × (1 − discount), 2)
case SUJETA_21:
    tipo = 21.00; cuota = round(base × 0.21, 2)
    retencion = round(base × withholding_rate, 2)            # только если withholding_rate > 0
    total_factura = base + cuota                              # «Total Factura» в libros НЕ уменьшается на retención
    total_a_pagar = base + cuota − retencion
    mentions: []  (с retención: строка «Retención IRPF x %: −N €» и база retención)
case NO_SUJETA_INTRACOM:
    tipo = none; cuota = 0; total = base
    required: NIF-IVA продавца (ES…) и клиента (с префиксом страны), оба действительны в VIES на дату фактуры
    mentions: «Operación no sujeta al IVA español por reglas de localización (art. 69.Uno.1º Ley 37/1992)»,
              «Inversión del sujeto pasivo / Reverse charge — art. 196 Directiva 2006/112/CE»
    forbidden: factura simplificada
case NO_SUJETA_LOCALIZACION:
    tipo = none; cuota = 0; total = base
    mentions: «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)»
              (для B2C art. 69.Dos: ссылка на art. 69.Dos)
    forbidden: factura simplificada
case OSS_DESTINO:
    tipo = rate(customer.country); cuota = round(base × tipo, 2); total = base + cuota
    mentions: «IVA … % (país de consumo …) — Régimen de la Unión OSS»; декларируется в 369; в 303 только casilla 123
```

Валюта, отличная от EUR: все суммы фактуры можно показать в этой валюте. Но нужно добавить строку «Cuota IVA: N EUR (tipo de cambio BCE dd/mm/aaaa: 1 EUR = X CUR)». В no sujetas IVA нет. Но эквивалент базы в EUR всё равно записывается в libro по курсу на дату devengo:

```
fx_date   = devengo_date (дата оказания услуги / получения аванса), не дата оплаты
rate      = ECB_reference_rate(fx_date)   # если день нерабочий, последний курс, опубликованный до этой даты [INFERENCE; DGT V2630-17 требует только последовательности]
base_eur  = round(base_cur / rate, 2)     # ЕЦБ котирует 1 EUR = X CUR
cuota_eur = round(base_eur × tipo, 2)
```

### 3. Retención IRPF в фактуре (только испанским клиентам-предпринимателям)

```
if not customer.spanish_withholder: rate = 0          # физическое лицо-потребитель, иностранный клиент без EP в Испании
elif seller.profile == SL: rate = 0                   # услуги SL не облагаются retención (кроме аренды и т. д.)
elif seller.activity_kind == EMPRESARIAL: rate = 0    # и в общем режиме, и в Beckham
elif seller.profile == AUTONOMO_BECKHAM: rate = 0.24  # art. 114 RIRPF → правила IRNR
elif start_year ≤ year ≤ start_year + 2 and no_professional_activity_prev_year and notice_given: rate = 0.07
else: rate = 0.15
retencion = round(base × rate, 2)    # база — налогооблагаемая база без IVA
```

Удержанная сумма засчитывается в IRPF (Modelo 100/151). Эти данные передаются в модуль IRPF/Beckham. В 303 они не отражаются.

### 4. Классификация расхода (входящий IVA)

```
input: supplier{country, vat_id}, invoice{base, tipo, cuota, currency}, item{kind: CURRENT | INVESTMENT | VEHICLE | FOOD_HOTEL_TRAVEL | GIFTS | PRIVATE_MIX}
deductible_share:
    kind == GIFTS or (FOOD_HOTEL_TRAVEL and not deductible_in_IRPF_IS) -> 0       # art. 96
    kind == VEHICLE (turismo) and related costs -> 0.50 (если не доказано иное)   # art. 95.Tres.2ª, Cuatro
    kind == PRIVATE_MIX (вода/свет/интернет жилья) -> 0                            # art. 95.Uno; позиция AEAT/TEAC
    в остальных случаях -> 1.00 × prorrata (prorrata = 1.00, если нет операций art. 20)
investment = (base ≥ 3005.06 and useful_life > 1y)                                # art. 108
if supplier.country == ES:
    casillas: (28,29) если not investment, иначе (30,31)
elif supplier.country in EU and supplier.vat_id valid and seller in ROI:          # AIS
    devengado (10,11) = (base_eur, round(base_eur×0.21,2)); deducible (36,37) = (base_eur, cuota×share) [(38,39) если investment]
    349: clave I, страна, NIF-IVA поставщика, base_eur
elif supplier.country not in EU (SaaS из США и т. д.):                            # ISP art. 84.Uno.2º.a
    devengado (12,13) = (base_eur, round(base_eur×0.21,2)); deducible (28,29) = (base_eur, cuota×share) [(30,31) если investment]
else (EU supplier charged foreign VAT because no ROI/VAT-id):
    иностранный VAT НЕ вычитается в 303; записать его как расход; возврат только через Modelo 360 (до 30.09 следующего года)
imports of goods (DUA): deducible (32,33) / (34,35), devengado: уплачен на таможне (или casilla 77, если выбрана отсрочка)
```

В AIS/ISP начисленная cuota = cuota к вычету (при share = 1) → нулевой эффект на результат. Но обе части обязательны (art. 97.Uno.4º: вычет возможен, только если операция «надлежащим образом отражена»).

### 5. Расчёт Modelo 303 за квартал Q

```
sales  = invoices issued with devengo in Q (включая rectificativas, со знаком)
purch  = received invoices registered in Q (также позже, в пределах срока 4 года)

c07 = Σ base(SUJETA_21);  c08 = 21;  c09 = Σ cuota(SUJETA_21)
c10 = Σ base(AIS + AIB);  c11 = Σ cuota(AIS + AIB)
c12 = Σ base(ISP non-EU); c13 = Σ cuota(ISP non-EU)
c14/c15 = Σ изменений base/cuota по rectificativas с IVA (если они не распределены в 07–09)   # знак ±
c27 = c03+c06+c09+c11+c13+c15 (+ другие ставки/RE = 0)
c28/c29 = Σ ES current + ISP non-EU current (base без пропорции; cuota × share)
c30/c31 = Σ ES investment (+ ISP non-EU investment)
c32/c33, c34/c35 = импорт
c36/c37 = Σ AIS + AIB current;  c38/c39 = AIB investment
c40/c41 = исправление вычетов (полученные rectificativas) ±
c43 = регуляризация bienes de inversión (только если изменилась prorrata/использование); c44 = только 4T с prorrata
c45 = c29+c31+c33+c35+c37+c39+c41+c42+c43+c44
c46 = c27 − c45
c59  = Σ base(NO_SUJETA_INTRACOM)        # услуги B2B ЕС (+ EIB)
c120 = Σ base(NO_SUJETA_LOCALIZACION)    # вне ЕС, Канарские острова / Сеута / Мелилья, B2C 69.Dos
c123 = Σ base(OSS_DESTINO)
c64 = c46 (+c58 +c76 = 0);  c65 = 100;  c66 = c64
c110 = остаток к зачёту на начало Q (из casilla 72 предыдущих периодов, за вычетом применённого)
c78  = min(c110, max(c66 + c77, 0))      # применяется максимально возможная сумма
c87  = c110 − c78
c69  = c66 + c77 − c78 + c68 + c108      # c68, c108 = 0 в нашем случае
c71  = c69 − c70 + c109                  # c70/c109 только в rectificativa
if c71 > 0: INGRESAR c71 (IBAN; domiciliación до −5 дней)
elif c71 < 0 and Q in {1T,2T,3T}: COMPENSAR  c72 = |c71|  (запрещено, если c78 > 0; в этом случае остаток переносится через c87)
elif c71 < 0 and Q == 4T: на выбор DEVOLVER c73 = |c71| (включая весь c110) или COMPENSAR c72
elif c71 == 0 and (c27>0 or c45>0): RESULTADO CERO
else: SIN ACTIVIDAD
новый остаток к зачёту = c87 + c72
```

Инварианты: `c08 = 21.00` только если c07 > 0; `c11 ≈ c10×0.21`, `c13 ≈ c12×0.21`; `c37 ≤ c11` (при вычете 100 % они равны); `c59 + c120 + c123 + c07 (+c04+c01) + c60` = доходы квартала по libro выставленных фактур.

### 6. Modelo 349 за период

```
for each (counterparty, clave) in period:
    clave S: Σ base_eur услуг NO_SUJETA_INTRACOM; clave I: Σ base_eur AIS; clave E/A: товары
    registro: код страны (DE, FR, …; XI для Северной Ирландии, только товары), NIF-IVA без префикса страны, имя, clave, сумма
periodicity: monthly if Σ(E+S+…) > 50000 in current quarter or any of previous 4 quarters, else quarterly
file only if ≥ 1 registro; исправления предыдущих периодов: отдельные registros «rectificación» с периодом и ранее задекларированной суммой
```

Сверка: `Σ clave S за год = casilla 59 (сумма 4 кварталов 303) − EIB = casilla 103 (390)`.

### 7. Modelo 347 за год

```
candidates = counterparties с Σ(total_factura с IVA) > 3005.06 за год
exclude: контрагенты/операции, задекларированные в 349 (клиенты ЕС B2B, поставщики ЕС);
         операции с retención, включённые в 190/180 (испанские клиенты B2B профессионала, арендодатель с retención);
         импорт/экспорт товаров; операции без обязанности выставлять фактуру
include: испанские поставщики без retención (> 3005.06), испанские клиенты без retención (юридические лица B2C, при предпринимательской деятельности / SL),
         клиенты и поставщики вне ЕС по услугам (no sujetas): AEAT их включает (исключения для услуг нет) [INFERENCE: подтвердить в INFORMA]
по каждому: годовая сумма (с IVA; для no sujetas — база) и разбивка по кварталам; clave A (покупки) / B (продажи)
```

### 8. Modelo 390

Агрегация 303 за год: начисленный IVA по ставкам → 01/02 (4 %), 03/04 (10 %), 05/06 (21 %); внутриевропейские приобретения по ставкам: текущие услуги (c36) → 545–552, основные средства (c38) → 21–26; ISP non-EU → 27/28; 33/34 и 47 = итоги начисленного; к вычету по ставкам с итогами 48/49 (c28/29), 50/51 (c30/31), 58/59 (c38/39) и 597/598 (c36/37); 64 = Σc45; 65 = 84 = Suma de resultados = Σc46; 85 = casilla 110 первой 303 года (остаток предыдущего года); 86 = 84 − 85; 95 = Σ положительных c71; 97/98 = результат последней 303 (compensar/devolver); volumen: 99 = Σc07(+04,01), 103 = Σc59, 104 = Σc60, 110 = Σc120, 126 = Σc123, 108 = сумма. Кроме того, статистические данные: эпиграф IAE, clave A05 («Resto de actividades profesionales») или A03 («Resto de actividades empresariales no incluidas en los dos subtipos anteriores»), индикатор «Operaciones económicas con terceras personas» (если есть 347).

### 9. Verifactu: записи при выставлении фактуры

```
on issue(invoice):
    rf = RegistroAlta{
        IDEmisorFactura = seller.NIF, NumSerieFactura = serie+numero, FechaExpedicionFactura = dd-mm-yyyy,
        TipoFactura = F1|F2|R1..R5, Descripcion, Destinatarios[{Nombre, NIF | IDOtro{CodigoPais, IDType, ID}}],
        Desglose[{ClaveRegimen=01, CalificacionOperacion=S1|S2|N1|N2 | OperacionExenta=E1..E6, TipoImpositivo, BaseImponible, CuotaRepercutida}],
        CuotaTotal, ImporteTotal, Encadenamiento{PrimerRegistro | RegistroAnterior{IDEmisor, NumSerie, Fecha, Huella}},
        SistemaInformatico{NombreRazon, NIF, NombreSistemaInformatico, IdSistemaInformatico(2 chars), Version, NumeroInstalacion, TipoUsoPosibleSoloVerifactu=S|N, TipoUsoPosibleMultiOT, IndicadorMultiplesOT},
        FechaHoraHusoGenRegistro = ISO-8601 с часовым поясом (2026-03-10T12:00:00+01:00), TipoHuella = 01 (SHA-256), Huella }
    cadena = "IDEmisorFactura=…&NumSerieFactura=…&FechaExpedicionFactura=…&TipoFactura=…&CuotaTotal=…&ImporteTotal=…&Huella=<prev or empty>&FechaHoraHusoGenRegistro=…"
    Huella = UPPER(HEX(SHA256(UTF8(cadena))))          # 64 символа; значения с trim; Huella= пусто в первой записи
    тестовый вектор AEAT: "IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00"
                     → 3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60
    mode VERIFACTU: POST XML в веб-сервис AEAT (сертификат), ждать t≥60 с между отправками или до лимита записей; повторы ≥ 1/час при сбое; CSV в ответе
    mode NO_VERIFACTU: подписать XAdES Enveloped квалифицированным сертификатом; вести журнал событий (запуск/остановка, экспорт, инциденты) с собственной цепочкой хешей
    в печатной версии / PDF: QR 30–40 мм, ISO 18004, уровень M, URL проверки AEAT с NIF, серия+номер, дата, общая сумма; текст «VERI*FACTU» только в режиме VERIFACTU
on cancel(invoice): RegistroAnulacion{IDFactura, Encadenamiento, Huella по полям NIF, NumSerie, Fecha, HuellaAnterior, FechaHoraHuso}
rectificativa: новый RegistroAlta TipoFactura=R1..R5, TipoRectificativa=S (замещением) | I (по разнице), FacturasRectificadas[...]
```

Записи (XML) и события хранятся до истечения срока давности и не могут изменяться. Любое исправление делается только новой записью. Declaración responsable (OM art. 15: название, Id (2 символа), версия, компоненты, SoloVerifactu S/N, MultiOT S/N, тип подписи, производитель с NIF и адресом, дата/место) встроена в меню программы и также доступна отдельно (PDF).

### 10. Libros registro: запись

Лист `EXPEDIDAS_INGRESOS` (LSI.xlsx): Ejercicio | Periodo (1T…4T) | Actividad: Código, Tipo, Grupo/Epígrafe IAE | Tipo de Factura (F1/F2/R1…) | Concepto de Ingreso (IRPF) | Ingreso Computable | Fecha Expedición | Fecha Operación | Identificación de la Factura: Serie, Número, Número-Final | NIF Destinatario: Tipo (02/03/04/05/06/07), Código País, Identificación | Nombre Destinatario | Clave de Operación (01…) | Calificación (S1/S2/N1/N2) | Operación Exenta (E1–E6) | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Repercutida | Tipo/Cuota Recargo Eq. | Cobro: Fecha, Importe, Medio, Identificación Medio | Tipo Retención IRPF | Importe Retenido IRPF | Registro Acuerdo Facturación | Inmueble: Situación, Ref. Catastral | Referencia Externa.

Лист `RECIBIDAS_GASTOS`: Ejercicio | Periodo | Actividad | Tipo de Factura | Concepto de Gasto | Gasto Deducible | Fecha Expedición | Fecha Operación | Identificación Factura del Expedidor (Serie-Número, Número-Final) | Fecha Recepción | Número Recepción / Final | NIF Expedidor: Tipo, Código País, Identificación | Nombre Expedidor | Clave de Operación | Bien de Inversión (S/N) | Inversión del Sujeto Pasivo (S/N) | Deducible en Periodo Posterior (S/N) | Periodo Deducción: Ejercicio, Periodo | Total Factura | Base Imponible | Tipo de IVA | Cuota IVA Soportado | Cuota Deducible | Tipo/Cuota Recargo Eq. | Pago: Fecha, Importe, Medio, Identificación | Tipo/Importe Retención IRPF | Registro Acuerdo Facturación | Inmueble | Referencia Externa.

Лист `BIENES-INVERSIÓN`: Ejercicio, Periodo, Actividad, Identificador, Descripción, Fecha Inicio Utilización, Valor Adquisición, Valor Amortizable, Método, % Amortización, Amortización (cuota, acumulada inicio/final, pendiente), Identificación factura, NIF/Nombre expedidor, Base, Tipo IVA, Prorrata definitiva, Cuota deducible, Regularización anual (prorrata, cuota deducible, cuota a regularizar), Baja (fecha, causa, factura de transmisión), Referencia externa.

Соответствие наших режимов полям libro: SUJETA_21 → S1, clave 01, ставка 21, cuota; NO_SUJETA_INTRACOM → N2, тип NIF 02 (VAT-id ЕС), ставка/cuota 0, total = base; NO_SUJETA_LOCALIZACION → N2, тип NIF 06 (или 04), ставка/cuota 0; AIS/ISP (полученные) → Inversión del Sujeto Pasivo = S, Cuota Soportado = Cuota Deducible = base×21 %. Соответствие в Pre303: N2 → casilla 59, если NIF типа 02 ЕС; иначе 120 `[INFERENCE: проверить по Traslado_Libros_a_Casillas_IVA 2026.xlsx]`. Файл: один на год, накопительный, с именем `{ejercicio}{NIF}T{nombre}.xlsx` (T = единый IVA+IRPF), ≤ 4 МБ.

### 11. Разобранные примеры (1T 2026, autónomo с профессиональной деятельностью, без Beckham, 2-й год деятельности → retención 7 %)

**A. B2B ЕС**: Beispiel GmbH, DE123456789 (VIES ok), услуга разработки на 3 000 €, 2026-01-20.
Фактура: база 3 000,00; IVA: no sujeto; итого 3 000,00. Пометки: «Operación no sujeta al IVA español (art. 69.Uno.1º LIVA). Inversión del sujeto pasivo — art. 196 Directiva 2006/112/CE». NIF-IVA ES… и DE…. 303: c59 += 3 000. 349 1T: DE | 123456789 | Beispiel GmbH | S | 3 000. Libro: N2, тип NIF 02.

**B. B2B США**: Acme Inc., EIN 12-3456789, 5 000 USD, devengo 2026-02-10, курс ЕЦБ 1 EUR = 1,0800 USD → 4 629,63 €.
Фактура: 5 000,00 USD (экв. 4 629,63 EUR, BCE 10/02/2026 1,0800); IVA: no sujeto; «Operación no sujeta al IVA español — art. 69.Uno.1º Ley 37/1992 (destinatario establecido fuera de la UE)». Без retención. 303: c120 += 4 629,63. 349: нет. 347: если за год превышено 3 005,06 € → включить (clave B) `[INFERENCE]`. Libro: N2, тип NIF 06, страна US.

**C. B2B Испания**: Cliente SL, B12345678, консалтинг на 2 000 €, 2026-03-05.
Фактура: база 2 000,00; IVA 21 % 420,00; retención IRPF 7 % −140,00; итого по фактуре 2 420,00; к оплате 2 280,00. 303: c07 += 2 000; c08 = 21; c09 += 420. Retención 140 → в IRPF (Modelo 130/100); клиент подаёт 111/190. 347: исключено (операция с retención). Libro: S1, clave 01, Tipo Retención 7, Importe 140, Total Factura 2 420.
Вариант профессионала в Beckham: retención 24 % = 480 → к оплате 1 940,00; предпринимательская деятельность / SL: retención 0 → к оплате 2 420,00.

**D. B2C Испания**: физическое лицо, NIF 12345678Z, 500 €, 2026-03-20.
Фактура (полная или simplificada в зависимости от лимита ≤ 400 €: 605 > 400 → полная): база 500,00; IVA 21 % 105,00; итого 605,00; без retención. 303: c07 += 500; c09 += 105.

**Расходы 1T**: коворкинг (ES) 300 + 63; ноутбук (ES) 1 500 + 315 (< 3 005,06 → не bien de inversión → 28/29); AWS (US) 100 € → ISP: c12 100 / c13 21; c28 100 / c29 21; SaaS из Ирландии (IE, VAT-id, мы в ROI) 200 € → AIS: c10 200 / c11 42; c36 200 / c37 42; 349 clave I: IE | … | 200.

**303 1T 2026**: c07 2 500; c09 525; c10 200; c11 42; c12 100; c13 21; c27 = 588,00; c28 1 900 (300+1 500+100); c29 399 (63+315+21); c36 200; c37 42; c45 = 441,00; c46 = 147,00; c59 3 000; c120 4 629,63; c66 147; c110 0; c78 0; c69 = c71 = 147,00 → **a ingresar 147,00**.
Если бы продаж C и D не было: c27 = 63; c45 = 441; c46 = −378 → 1T «a compensar» 378 (c72); во 2T c110 = 378 и т. д.; в 4T — c73 (devolver) на весь остаток.

## Сроки и modelos

| Modelo | Кто | Период | Срок | Когда не подаётся |
|---|---|---|---|---|
| 036 (alta, ROI casilla 582, смена адреса, baja) | все | по событию | до начала деятельности / до первой операции в ЕС; смена адреса: 1 месяц | — |
| 303 | все налогоплательщики (autónomo и SL) | квартал | 1–20 апр/июл/окт; 4T 1–30 янв | никогда (подаётся и «sin actividad») |
| 390 | все, кто подаёт 303, кроме módulos/аренды/SII | год | 1–30 января | SII; только módulos/аренда |
| 349 | тот, кто совершил операции с clave E/A/S/I… | квартал (месяц, если > 50 000 €) | 1–20 следующего месяца; последний период — 1–30 янв | нет операций в периоде |
| 347 | все, у кого есть контрагенты > 3 005,06 € (вне 349/190) | год | 1–28(29) февраля | SII; нет контрагентов выше порога |
| 369 (OSS) | зарегистрированные в Régimen de la Unión (alta Modelo 035) | квартал | до последнего дня следующего месяца (также при нуле) | не зарегистрирован |
| 360 | тот, кто уплатил иностранный IVA в ЕС без права вычесть его в 303 | год | до 30 сентября следующего года | по желанию |
| 111 / 190 | **клиент**, который удерживает retención (не мы) | квартал / год | 1–20 следующего месяца; 190: январь | — |
| Записи Verifactu | все, кто использует SIF (IS, IRPF, IRNR-EP) | непрерывно | с 01.01.2027 (IS) / 01.07.2027 (IRPF); объявлен перенос на 10.2028 | SII |
| Электронная фактура B2B | получатель-предприниматель в Испании | — | 06.10.2027 (> 8 млн) / 06.10.2028 (остальные) | клиент за границей; simplificadas |
| Libros registro | все | непрерывно, с итогами по кварталам | записи: до окончания срока подачи 303 за соответствующий период (art. 69 RIVA) | SII (ведутся в Sede) |

## Пограничные случаи

- **Клиент из ЕС без действительного VAT-id** (стартап до регистрации, частное лицо, которое представляется «предпринимателем»): считать его B2C (Reg. UE 282/2011 art. 18.2) → испанский IVA 21 %. Когда VAT-id будет получен, можно перевыставить фактуру без IVA через rectificativa (DGT это допускает, если можно доказать статус предпринимателя на дату операции).
- **У нас нет ROI, но клиент из ЕС B2B**: операция остаётся no sujeta (место оказания не зависит от ROI). Но 349 требует NIF-IVA, а клиент не найдёт нас в VIES → риск. Подайте 036, casilla 582, до первой фактуры.
- **Аванс от иностранного клиента**: devengo в момент получения оплаты (art. 75.Dos) → фактура на аванс в периоде получения, по курсу на дату получения. В no sujetas IVA нет, но сумма идёт в casilla 59/120 квартала аванса.
- **Длящийся договор (retainer) с иностранным клиентом** без ежемесячного срока оплаты: devengo 31 декабря (art. 75.Uno.7º). В no sujetas это влияет только на период 59/120 и 349.
- **Rectificativa по операции no sujeta** (скидка/возврат клиенту из США): отражается уменьшением casilla 120 в периоде выставления rectificativa. Если итог квартала отрицательный: формы AEAT не принимают отрицательные информационные casillas → поставить 0 и перенести остаток `[INFERENCE: проверить в Pre303]`.
- **Расходы при 100 % иностранных клиентов**: право на вычет полное (art. 94.Uno.2º), и результат 303 стабильно отрицательный. Devolución за 4T приходит в течение 6 месяцев (до ~конца июля), часто с requerimiento libros. Поэтому важно вести libros в формате AEAT. Альтернатива: REDEME (036, в ноябре на следующий год), с ежемесячной 303 и обязательным SII.
- **Beckham**: на IVA не влияет совсем. Он влияет только на retención в фактурах B2B испанским клиентам (24 %/0 %) и на то, что retención засчитывается в Modelo 151, а не в 100.
- **Переезд между автономными сообществами**: для IVA не важен. Обязательно подать 036 (смена налогового адреса) в течение одного месяца. Серия и нумерация фактур не меняются. Адрес в фактуре — новый с даты смены.
- **Канарские острова / Сеута / Мелилья**: клиент-предприниматель там → no sujeta, casilla 120 (не 59), в 349 не идёт. Клиент-потребитель → 21 %. Поставщик оттуда → ISP, как с третьей страной (12/13 + 28/29). Не путать с экспортом (casilla 60 только для товаров).
- **Северная Ирландия (XI)**: сохраняет статус ЕС только для товаров. Услуги B2B в UK/XI находятся вне ЕС → casilla 120.
- **Автомобиль**: 50 % cuota при покупке/лизинге/топливе/парковке. Консультанту почти невозможно доказать использование более 50 %. Пример: лизинг 400 + 84 → вычет 42 (база в libro 400 без пропорции, Cuota Deducible 42).
- **Офис дома**: IVA за коммунальные услуги жилья, частично используемого в деятельности, не вычитается (art. 95.Uno; позиция AEAT/TEAC), хотя в IRPF вычитается 30 % пропорциональной части. Аренда жилья освобождена: IVA в ней нет.
- **Ресторан/отель/поездки**: IVA вычитается, только если расход вычитается в IRPF/IS (рабочая поездка, подтверждённая документами) и есть полная фактура с NIF (не tique).
- **Ноутбук/оборудование < 3 005,06 €**: не bien de inversión для целей IVA → casilla 28/29, без регуляризации. Если ≥ 3 005,06 € → 30/31 и регуляризация в течение 5 лет при изменении prorrata или использования.
- **SaaS из США без фактуры с NIF** (только receipt): для ISP достаточно бухгалтерского justificante (art. 97.Uno.4º). Но justificante должен идентифицировать поставщика, услугу, дату и сумму. Его нужно хранить.
- **Электронные услуги B2C в ЕС**: продажа подписок/курсов европейским частным лицам → следите за порогом 10 000 € (включая предыдущий год). Если порог превышен: alta в OSS (Modelo 035) и Modelo 369; IVA по ставке страны клиента; нужны 2 доказательства местонахождения клиента (IP, адрес, банк).
- **Factura simplificada иностранному клиенту**: запрещена. В Verifactu тип F2 тоже не подходит: только F1.
- **SL и autónomo**: IVA идентичен. SL всегда подаёт декларации электронно с сертификатом. Как юридическое лицо она подпадает под электронную фактуру B2B (статусы с 06.10.2028) и под Verifactu как плательщик IS с 01.01.2027 (если перенос не будет оформлен).
- **Verifactu с программой, размещённой самим пользователем**: declaración responsable обязательна для каждой версии; NIF производителя = NIF пользователя. Удобнее модальность VERI*FACTU (не нужны подпись XAdES и журнал событий, и она вызывает больше доверия при devoluciones). Бесплатная альтернатива: приложение AEAT (но тогда фактуры ведутся только в нём).
- **Испанский клиент платит из-за границы / в другой валюте**: место оказания зависит от клиента (TAI) → 21 % независимо от валюты; cuota в евро по курсу на дату devengo.

## Невыясненные вопросы

1. **Verifactu: фактическая дата начала.** По норме (RDL 15/2025): 01.01.2027 / 01.07.2027. 05.10.2026 Hacienda объявила «перенос обязанностей Real Decreto 1007/2023 от 5 декабря, ещё не вступивших в применение, до октября 2028 года» (чтобы согласовать их с электронной фактурой для < 8 млн). Но RD ещё не опубликован. AEAT говорит о «прогнозе продления срока». Осторожная реализация: уже сейчас строить SIF по требованиям RRSIF/OM (цепочка, XML, QR) и включать обязательные отправку/подпись по фактически действующей дате; следить за BOE.
2. **Электронная фактура B2B: технический формат для нашего профиля.** RD 238/2026 ссылается на синтаксисы и на SPFE (государственное решение), с обязанностью отправлять копию при использовании частной платформы. Детали форматов (Facturae/UBL/CII) и API SPFE в Orden HAC/1028/2026 не проверены: **UNVERIFIED**. При одном-двух испанских клиентах проще использовать SPFE напрямую с 06.10.2028.
3. **Соответствие в Pre303 N2 → 59 или 120** в зависимости от типа NIF клиента: не подтверждено первичным источником (`Traslado_Libros_a_Casillas_IVA 2026.xlsx` не прочитан). Осторожно: не полагаться на автоматический импорт и рассчитывать 59/120 самим.
4. **347 для иностранных клиентов/поставщиков (вне ЕС) по услугам**: текст art. 33 RGAT исключает только импорт/экспорт *товаров*. Практика AEAT — включать их; **UNVERIFIED** в INFORMA. Осторожно: включать их (лишняя декларация вреда не причиняет; пропуск — нарушение art. 198/199 LGT).
5. **Курс для no sujetas и для IRPF**: art. 79.Once формально относится к IVA. Для суммы дохода в IRPF и в libros применяется тот же принцип (devengo) по доктрине DGT. Допускаются альтернативные источники (V2630-17). Осторожно: один источник (ЕЦБ, день devengo; в нерабочие дни — последний опубликованный курс). Курсовая разница при получении оплаты — финансовый результат вне IVA.
6. **Отрицательные информационные casillas 59/120** в rectificativas: поведение формы не проверено. Осторожно: ограничивать их нулём и переносить остаток исправления на следующий квартал, с примечанием в libro.
7. **Beckham + предпринимательская или профессиональная деятельность**: квалификация деятельности (IAE раздел 1ª или 2ª) определяет retención 24 % или 0 %. Это решает модуль Beckham/IRPF; здесь движок только получает индикатор. Статус «предпринимательской деятельности (actividad emprendedora)» (ENISA) на IVA не влияет.
8. **Допуск валидации ±10 €** между base×tipo и cuota в Verifactu/SII: данные по памяти из документа валидаций AEAT; версия 2026 года повторно не проверена: **UNVERIFIED**. Движок в любом случае считает точно; допуск нужен только при импорте сторонних фактур.
9. **Casillas 390 по ставкам**: сверены с diseño de registro DR390 2025 (https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/dr390e2025.xlsx) и с формой 390 из Manual práctico IVA 2025. Ограничение движка: все текущие внутриевропейские приобретения (c36) он считает услугами, а основные средства (c38, art. 108 LIVA) — товарами; внутриевропейские приобретения текущих товаров (casillas 21–26 и 56/57) не выделяются.
10. **Ставки IVA на 2027 год**: изменения не опубликованы; RETA/IRPF вне этого файла.
11. **Код XI / UK после Brexit для услуг**: UK — полноценная «третья страна» для услуг (casilla 120); XI считается ЕС только для товаров. Дополнительное подтверждение не искали.
12. **REDEME**: условия (отсутствие долгов, SII) и срок выбора (ноябрь) взяты из общих знаний art. 30 RIVA; повторно не перечитаны: **UNVERIFIED**.

### Основные источники

- LIVA (Ley 37/1992), консолидированная: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- RD 1619/2012 (Reglamento de facturación), консолидированный, с изменениями RD 1007/2023 и RD 238/2026: https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696
- Instrucciones Modelo 303 2026 (AEAT): https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html
- Formulario 303 (Manual IVA 2025, приложение): https://sede.agenciatributaria.gob.es/static_files/Sede/Biblioteca/Manual/Practicos/IVA/IVA_2025/Imagenes/Cap_9_303_eu_es.pdf
- Instrucciones 390-2025: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/G412/Instrucciones_modelo_390-2025.pdf
- Instrucciones 349: https://sede.agenciatributaria.gob.es/static_files/Sede/Procedimiento_ayuda/GI28/instr_mod_349.pdf
- 347, исключённые операции: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html
- RD 1007/2023 (RRSIF): https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 ; RDL 15/2025: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-24446 ; Orden HAC/1177/2024: https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138
- Записка Hacienda от 05.10.2026 (перенос на 10.2028): https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
- AEAT Verifactu FAQ (обновлено 21.07.2026): https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes.html ; спецификация отпечатка (huella): https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/Veri-Factu_especificaciones_huella_hash_registros.pdf
- Электронная фактура: RD 238/2026 https://www.boe.es/eli/es/rd/2026/03/25/238/con ; календарь AEAT https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html
- Формат libros registro: https://sede.agenciatributaria.gob.es/static_files/Sede/Tema/IVA/Fact_registro/Libros_registro/Formato_Electronico_Comun_Libros_Registro_IVA_IRPF.pdf ; LSI.xlsx: https://sede.agenciatributaria.gob.es/static_files/AEAT/LSI.xlsx ; Orden HAC/773/2019: https://www.boe.es/eli/es/o/2019/06/28/hac773
- Retenciones 2026 (с 10.09.2026): https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/CUADRO_TIPOS_RETENCION_IRPF_2026_10sept.pdf ; RD 1008/2023 (Beckham 24 %): https://sede.agenciatributaria.gob.es/Sede/irpf/novedades-impuesto/novedades-normativa-2023/principales-novedades-real-decreto-1008-diciembre.html
- Отмена Modelo 037 / ROI casilla 582: https://www.boe.es/buscar/doc.php?id=BOE-A-2025-410 ; https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/operaciones-intracomunitarias-consulta-operadores.html
- Электронные услуги B2C/OSS: https://sede.agenciatributaria.gob.es/Sede/no-residentes/iva-empresarios-profesionales-no-establecidos/iva-telecomunicaciones-servicios-electronicos.html ; Orden HAC/610/2021 (Modelo 369): https://www.boe.es/eli/es/o/2021/06/16/hac610
- Курс: DGT V2630-17 (через Iberley): https://www.iberley.es/resoluciones/resolucion-vinculante-dgt-v2630-17-16-10-2017-1473112 ; ECB reference rates: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.es.html
