## Кратко

- Проверено по доступным первичным источникам на **08.10.2026**. Год дохода (`ejercicio`) и год подачи — разные поля: годовые декларации за 2025 подаются в 2026; за 2026 — преимущественно в 2027.
- Для небольшого бизнеса в territorio común квартальные 303/130/111/115 обычно подаются до 20 апреля, июля и октября. **За IV квартал сроки различаются:** 111/115 — 20 января, 303/130/349 и 390 — 30 января с переносом нерабочих дней; 180/190 — 31 января с переносом.
- В 2026 срок domiciliación для 303/130 за IV квартал 2025 — **27 января**, а не автоматически 25 января. Для обычных кварталов — 15 апреля/июля/октября. Календарь нельзя реализовать формулой «дата подачи минус пять дней».
- Renta 2025 через Интернет: **08.04–30.06.2026**, domiciliación — до **25.06.2026**. Modelo 151 — отдельный сервис, не обычный Renta WEB; **Cl@ve допускается**, сертификат не является единственным способом входа.
- Для 303 за IV квартал 2026 AEAT уже прямо публикует **01.02.2027**. Остальные приведённые ниже даты 2027, не подтверждённые отдельным календарём AEAT, помечены как расчётные; точный старт Renta 2026 в 2027 — **UNVERIFIED**.
- 303/130 можно генерировать как текстовый файл по diseño de registro и импортировать в форму Sede. Это **не CSV, не PDF и не произвольный XML**, несмотря на обрамляющие теги `<T...>`.
- Проверены актуальные файлы: **DR303e26v101.xlsx** для 2026; **DR303e25.xlsx** для 2025; **DR130e15v12.xls** для 2019 и последующих лет. Номер года в имени спецификации 130 не означает, что она устарела.
- Pre303 — подтверждённый сервис предварительного заполнения формы. Публичный документированный API именно Pre303, позволяющий сторонней программе рассчитать/подать декларацию без формы, **не подтверждён**. API SII или VERI*FACTU не заменяет подачу 303.
- NIE достаточно для получения испанского certificado FNMT и регистрации Cl@ve при надлежащем подтверждении личности. Российский паспорт и TIE **не являются DNIe**. SL подаёт с certificado electrónico представителя либо через уполномоченного представителя, не с личным Cl@ve как заменой сертификата SL.
- Состояния «файл создан», «форма проверена», «NRC получен», «декларация принята» и «налог оплачен» независимы. Завершение подачи подтверждается **justificante + CSV + датой/временем AEAT**; domiciliación требует последующей сверки списания.
- Добровольная просрочка с суммой к уплате: art. 27 LGT — **1% + 1 процентный пункт за каждый полный месяц**, после 12 месяцев — **15% и проценты**. Нулевая/информационная декларация не становится безнаказанной: действуют отдельные санкции.
- Autoliquidación rectificativa не введена одновременно для всех моделей: для 303 — начиная с 09/3T 2024, для 100 — с ejercicio 2024, для 200 — с периодов, начинающихся 01.01.2024; 130 сохраняет complementaria. Первичная пропущенная декларация не является complementaria.

## Правила

1. **Сроки и переносы определяются конкретной моделью и календарём AEAT.** Если последний день нерабочий, срок заканчивается в следующий рабочий день. Для электронного обслуживания ориентир — официальный календарь Sede, не произвольный список праздников по месту проживания. Для domiciliación AEAT требует интервал не менее **трёх рабочих либо пяти календарных дней** между её окончанием и общим сроком; при расчёте рабочих дней учитывает субботы, воскресенья, общенациональные праздники и региональные/местные праздники муниципалитета Departamento de Informática AEAT. Действует для рассматриваемых подач 2025–2026; таблица на 2026 имеет приоритет над эвристикой. Источник: [официальные сроки и domiciliación 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html).

2. **Квартальная периодичность 349 не следует из квартальной периодичности 303.** Базовая периодичность 349 — месяц; квартал допускается, если сумма соответствующих intracomunitarias entregas de bienes/prestaciones de servicios без IVA не превышала 50 000 € ни в текущем квартале, ни в четырёх предыдущих. При превышении внутри квартала возникает специальная подача за уже истёкшие месяцы; годовой 349 не использовать. Без операций, подлежащих включению, «нулевой 349» не нужен. Для июля есть продлённое окно до 20 сентября, для декабря/IV квартала — до 30 января. Действует в 2025–2026. Источники: [AEAT, operaciones intracomunitarias](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/5-impuesto-sobre-valor-anadido/5_9-operaciones-intracomunitarias.html), [сроки 349, manual IVA 2026](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2026/capitulo-09-declaraciones-informativas-iva-379/declaracion-recapitulativa-operac-intracomunitarias-modelo-349/plazo-presentacion.html).

3. **Modelo 036 — событийная, а не квартальная обязанность.** Alta — до начала деятельности/соответствующих операций; обычная modificación — в течение месяца со дня, следующего за изменением; baja — обычно месяц после прекращения. Для domicilio fiscal autónomo применяется modificación 036, casilla 122; переезд не следует откладывать до Renta. ROI нужно запросить до соответствующих intracomunitarias операций. Для опций IVA/IS действуют специальные окна: например, выбор art. 40.3 LIS для календарного периода — в феврале, в 2026 до 02.03.2026. Modelo 037 отменена с **03.02.2025**. Источники: [036 в календаре 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/modelo-036.html), [срок modificación](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/plazos-presentacion/declaracion-modificacion-modelo-036.html), [casilla 122](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/modificacion-modelo-036/casilla-122-domicilio-fiscal-modelo-036.html), [02.03.2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html).

4. **Аутентификация зависит от заявителя, а не только от модели.** Физлица могут использовать Cl@ve для 036, 100, 111, 115, 130, 149, 151, 180, 190, 303, 347, 349, 390, 714, 720, 721. Сертификат/DNIe применим шире. SL обязана подавать электронно с certificado; полномочия администратора/представителя должны быть признаны. Número de referencia годится только для разрешённых IRPF-процедур, не как универсальный доступ. Действует в 2025–2026; список проверен по календарю 2026. Источник: [AEAT, identificación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/recuerde/identificacion-presentar-autoliquidaciones.html).

5. **Для иностранца без DNIe есть полностью рабочий путь FNMT с NIE.** Запрос certificado de persona física → código de solicitud → личное подтверждение в oficina de acreditación с действующими оригиналами TIE/официального документа NIE и паспорта → загрузка сертификата согласно инструкции FNMT. Обычно нужна cita previa; экспортировать защищённую резервную копию закрытого ключа. Для Cl@ve доступны регистрация с сертификатом, очная регистрация, либо carta de invitación на domicilio fiscal с CSV; при NIE указывается número de soporte документа. Carta даёт nivel básico, не все процедуры высокого уровня доступны. Возможность конкретного вида vídeoidentificación для российского паспорта не предполагать. Это актуальная процедура, а не ежегодная налоговая ставка. Источники: [FNMT: документы](https://www.sede.fnmt.gob.es/registro-inicio/preguntas-frecuentes/-/asset_publisher/DKnDigPrgk4U/content/4-3-2-3-acreditacion-de-la-identidad-de-una-persona-fisica), [Cl@ve с carta](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/registrarse-clave-pin/registro-internet-csv.html), [número de soporte](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/incidencias-tecnicas-clave-pin/introduzca-soporte-valido.html).

6. **Renta WEB и 151 — разные workflows.** Обычный IRPF — Renta WEB / modelo 100; Beckham — отдельная форма 151, с Cl@ve или certificado/DNIe, импортом/экспортом BOE-файла `.151`, проверкой и `Firmar y enviar`. Нельзя автоматически заменить 151 декларацией 100 или объявить 151 «только вручную, без файла». Для 151 опубликован DR для ejercicio 2023 и следующих, применимый в рассматриваемые годы. Источники: [техническая инструкция 151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html), [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), [инструкции 151](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html).

7. **Импорт декларации не является подачей.** После импорта выбрать способ погашения, исправить ошибки валидатора, подписать и получить justificante. `Guardar`, `Vista previa`, `Exportar` и NRC по отдельности этого не подтверждают. NRC — 22 символа и подтверждает платёж, не сдачу декларации; его данные должны совпасть с NIF/modelo/ejercicio/periodo/importe. При `Reconocimiento de deuda` запрос aplazamiento/compensación оформляется отдельно, если не завершён непосредственно в workflow. Действует в актуальных формах 2025–2026. Источники: [130](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-130.html), [151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html).

8. **Pre303 не освобождает от проверки исходных данных.** Сервис даёт Ventana Censal IVA, Identificación, результат/остатки cuotas a compensar; расширенный расчёт возможен по SII/Libros Agregados или импорту libros registro у подходящих не-SII-плательщиков. Представителю для всех функций нужны соответствующие полномочия, в частности PRE303. На 08.10.2026 в проверенной публичной документации не найден контракт API Pre303 для независимой автоматической подачи; подтверждён путь формы + официальный файл/книги. Источники: [Pre303](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303.html), [функции](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/que-servicios-funcionalidades-tiene-nuevo-pre303.html), [доступ](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/acceder-pre303.html), [техническая инструкция 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303.html).

9. **RETA обслуживается отдельно от AEAT, в Import@ss.** Через `Base de cotización y rendimientos` сообщаются/меняются прогноз среднемесячного rendimiento neto и base в разрешённом tramo. До шести дат вступления изменений в силу в год, без немедленного ретроактивного изменения всех предыдущих месяцев. В `Consulta de recibos de trabajo autónomo` доступны выставленные cuotas; факт выставления сверять с банковским списанием. Правила системы действуют с 2023, применимы в 2025–2026. Источники: [изменение base](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos), [guía autónomo](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo+Autonomo/guia), [recibos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta%2Bde%2Bpagos%2By%2Bdeudas/ConsultaRecibos).

10. **Добровольная просрочка до requerimiento и неуплата уже заявленного долга — разные основания.** Art. 27 LGT применяется к добровольно поданному опоздавшему расчёту за правильно указанный период; не смешивать пропущенные обороты с текущим кварталом. Recargo уменьшится на 25% только при выполнении условий уплаты долга и recargo, установленных art. 27.5; не обещать скидку при любом признании долга. При неоплате возможны дополнительно recargos del período ejecutivo по art. 28. Текущая шкала art. 27 действует с **11.07.2021**, следовательно в 2025–2026. Источник: [LGT, arts. 27–28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27).

11. **Отсутствие суммы к уплате не отменяет декларационную обязанность и санкции.** Art. 198 LGT: обычная просрочка без ущерба — 200 €, censal — 400 €, обязательные информационные данные — 20 € за dato/conjunto de datos по одному лицу, минимум 300 €, максимум 20 000 €; добровольная поздняя подача без requerimiento уменьшает эти величины вдвое. Это потенциальная санкция в отдельном производстве, не сумма, автоматически добавляемая в casilla налога. При ущербе Hacienda после requerimiento возможен art. 191: 50–150% недоимки в зависимости от состава. Действует в 2025–2026. Источник: [LGT, arts. 191, 198, 199](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198).

12. **Исправление выбирается по модели и налоговому периоду.** 303 с 09/3T 2024 — autoliquidación rectificativa как общий путь и при увеличении, и при уменьшении результата; существуют специальные исключения, в частности отдельные споры об IVA repercutido и нарушении нормы более высокого уровня. 100 с ejercicio 2024 — rectificativa в предусмотренных случаях, с сохранением специальных complementarias для отдельных оснований регуляризации. 200 с периодов, начинающихся 01.01.2024, — rectificativa. 130, актуальная форма 151 и обычные удержания сохраняют собственные механизмы complementaria/solicitud de rectificación; не распространять на них автоматом нововведение 100. Источники: [303, исправления](https://sede.agenciatributaria.gob.es/Sede/iva/presentar-declaracion-iva-modelo-303/errores-declaracion.html), [FAQ 303](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/autoliquidacion-rectificativa.html), [100 ejercicio 2024](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2024/c18-cuota-liquida-resultante-autoliquidacion/regularizacion-situaciones-tributarias/general.html), [200](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2024/capitulo-02-identificac-autoliq-compl-incn/autoliquidacion-rectificativa.html), [130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

## Цифры

### Постоянные для календаря и рисков

| Параметр | 2025 | 2026 | Уточнение |
|---|---:|---:|---|
| Лимит квартального 349 | 50 000 € | 50 000 € | Текущий и каждый из четырёх предыдущих кварталов; без IVA, по соответствующим исходящим операциям |
| Порог обычных операций на контрагента для 347 | >3 005,06 € | >3 005,06 € | Годовая сумма с IVA; исключения важнее самого порога |
| Формальная обязанность 714 независимо от cuota | Активы/права >2 000 000 € | То же | Кроме обязанности при cuota a ingresar; считать активы соответствующей налоговой сферы, до долгов и с учётом освобождённых активов |
| Первичный порог 720 | >50 000 € на соответствующий блок | То же | Не единый порог на всё зарубежное имущество; есть бухгалтерские и персональные исключения |
| Повторный 720 | Рост соответствующего блока >20 000 € относительно последней обязательной подачи | То же | Отдельно учитывать прекращение владения/полномочий, не только рост |
| Первичный порог 721 | Совокупно >50 000 € | То же | Зарубежная кастодиальная криптовалюта; self-custody не входит |
| Повторный 721 | Рост >20 000 € и отдельные случаи прекращения статуса | То же | Проверять правила art. 42 quater, не копировать буквально все правила 720 |
| Art. 27, до истечения 12 месяцев | 1% + 1 п.п./полный месяц | То же | Без requerimiento; не деление дней на 30 |
| Art. 27, после 12 месяцев | 15% + intereses | То же | Проценты только с дня после окончания этих 12 месяцев |
| Уменьшение recargo art. 27.5 | 25% от recargo | 25% | Условное; долг и проценты не уменьшаются этой скидкой |
| Interés de demora tributario | 4,0625% годовых | 4,0625% по проверенной таблице/продлению | Не замораживать ставку на будущие годы |
| Art. 28: ejecutivo / apremio reducido / ordinario | 5% / 10% / 20% | То же | Взаимоисключающие между собой; 20% совместим с intereses |
| Art. 198: обычная декларация без ущерба | 200 € / 100 € добровольно | То же | До иных применимых уменьшений санкции |
| Art. 198: declaración censal | 400 € / 200 € добровольно | То же | Для autónomo 036; не путать с 100 € по art.198.5 для физлица без деятельности |
| Art. 198: информационная декларация | 20 €/dato, min 300 €, max 20 000 € | То же | Добровольно: 10 €/dato, min 150 €, max 10 000 € |
| Лимит web-форм 349/190/347 | 40 000 записей | 40 000 записей в актуальных инструкциях | При превышении — fichero/TGVI; небольшой файл тоже допустим |

Источники к таблице: [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), [проценты, Banco de España](https://clientebancario.bde.es/pcb/es/menu-horizontal/productosservici/relacionados/tiposinteres/guia-textual/tiposinteresrefe/tabla_tipos_interes_demora.html), [AEAT, проценты 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html), [714](https://sede.agenciatributaria.gob.es/Sede/no-residentes/impuesto-sobre-patrimonio/declaracion-impuesto-patrimonio-no-residentes.html), [исключения 347](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes.html), [721 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html).

### Подача в 2026 и закрытие ejercicio 2026 в начале 2027

Все даты включительно. `—` означает, что domiciliación неприменима к информационной декларации, а не отсутствие обязанности подать.

| Модель / период | Окно подачи | Последний день domiciliación | Статус |
|---|---|---|---|
| 111, 115: 4T 2025 | 01–20.01.2026 | 15.01.2026 | AEAT |
| 303, 130: 4T 2025 | 01–30.01.2026 | **27.01.2026** | AEAT |
| 349: 4T/12M 2025; 390: год 2025 | 01–30.01.2026 | — | AEAT |
| 190, 180: год 2025 | 01.01–02.02.2026 | — | AEAT |
| 347: год 2025 | 01.02–02.03.2026 | — | AEAT |
| 720, 721: год 2025 | 01.01–31.03.2026 | — | AEAT |
| 303, 130, 111, 115: 1T 2026 | 01–20.04.2026 | 15.04.2026 | AEAT |
| 349: 1T 2026 | 01–20.04.2026 | — | AEAT |
| 202: 1P 2026 | 01–20.04.2026 | 15.04.2026 | AEAT; не «квартальная прибыль Q1» по умолчанию |
| 100, 151, 714: год 2025 | Кампания Интернет 08.04–30.06.2026 | 25.06.2026 | Общий конец и domiciliación подтверждены для всех трёх; 151 — отдельный сервис |
| 303, 130, 111, 115: 2T 2026 | 01–20.07.2026 | 15.07.2026 | AEAT |
| 349: 2T 2026 | 01–20.07.2026 | — | AEAT |
| 200: календарный год 2025 | 01–27.07.2026 | **22.07.2026** | AEAT; 25 июля — суббота |
| 718: год 2025, если возникает ITSGF | 01–31.07.2026 | 28.07.2026 | AEAT; не замена 714 |
| 303, 130, 111, 115: 3T 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 349: 3T 2026 | 01–20.10.2026 | — | AEAT |
| 202: 2P 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 102: второй платёж обычной Renta 2025 при допустимом fraccionamiento | До 05.11.2026 | Отдельные сроки управления domiciliación, см. ниже | AEAT; не переносить этот режим автоматически на 151 |
| 202: 3P 2026 | 01–21.12.2026 | **16.12.2026** | AEAT; 20 декабря — воскресенье |
| 111, 115: 4T 2026 | 01–20.01.2027 | 15.01.2027 | Расчёт по действующему правилу; полный календарь 2027 UNVERIFIED |
| 303: 4T 2026 | 01.01–**01.02.2027** | Ожидается 27.01.2027 | Конец подачи уже опубликован AEAT; domiciliación 2027 расчётная |
| 130: 4T 2026; 349: 4T/12M 2026; 390: год 2026 | 01.01–01.02.2027 | Для 130 ожидается 27.01.2027; прочие — | Расчёт: 30 января — суббота |
| 190, 180: год 2026 | 01.01–01.02.2027 | — | Расчёт: 31 января — воскресенье |
| 347: год 2026 | 01.02–01.03.2027 | — | Расчёт: 28 февраля — воскресенье |
| 720, 721: год 2026 | 01.01–31.03.2027 | — | Действующее ежегодное правило; календарь 2027 ещё не подтверждён |
| 100, 151, 714: год 2026 | Ожидается апрель–30.06.2027 | Ожидается 25.06.2027 | Начало/окончательный календарь кампании **UNVERIFIED** |
| 200: календарный год 2026 | Ожидается 01–26.07.2027 | Ожидается 21.07.2027 | Расчёт: 25 июля — воскресенье; проверить утверждённый календарь и праздники |

Источники: [годовой календарь 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual.html), [domiciliación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [30 января](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/enero/hasta-30-enero.html), [2 февраля](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/febrero/hasta-2-febrero.html), [2 марта](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html), [31 марта](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-31-marzo.html), [303 до 1 февраля 2027](https://sede.agenciatributaria.gob.es/Sede/en_gb/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/calendario-anual/febrero-2027/hasta-1-febrero-2027.html).

Для campaña Renta 2025: телефонная помощь AEAT **06.05–30.06.2026**, запись **29.04–29.06**; очная **01.06–30.06**, запись **29.05–29.06**. Это не гарантия обслуживания предпринимательского/Beckham-кейса: действуют критерии допуска к помощи. [Даты кампании](https://sede.agenciatributaria.gob.es/Sede/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/fechas-campana-renta-patrimonio.html).

Управление вторым платежом 102: **живая таблица AEAT** на момент чтения указывает до **02.11.2026** для revocar/rehabilitar/domiciliar у плательщиков с domiciliación первого платежа и до **20.10.2026** для изменения IBAN. В поисковой выдержке той же страницы встречалась старая дата 30 сентября; использовать живую страницу/актуальную инструкцию и не смешивать эти сроки с первой domiciliación Renta.

### Месячные режимы: все сроки в календарном 2026

Малый объём не отменяет месячный 303 при REDEME/SII по соответствующему основанию; месячные 111/115 возникают, в частности, у grandes empresas. `M` — месяц операций; даты без года ниже относятся к 2026.

| Период | 303: подать / domiciliación | 111/115: подать / domiciliación | 349: подать |
|---|---|---|---|
| 12M 2025 | 30.01 / 27.01 | 20.01 / 15.01 | 30.01 |
| 01M 2026 | 02.03 / 25.02 | 20.02 / 17.02 | 20.02 |
| 02M 2026 | 30.03 / 25.03 | 20.03 / 16.03 | 20.03 |
| 03M 2026 | 30.04 / 27.04 | 20.04 / 15.04 | 20.04 |
| 04M 2026 | 01.06 / 27.05 | 20.05 / 15.05 | 20.05 |
| 05M 2026 | 30.06 / 25.06 | 22.06 / 17.06 | 22.06 |
| 06M 2026 | 30.07 / 27.07 | 20.07 / 15.07 | 20.07 |
| 07M 2026 | 31.08 / 26.08 | 20.08 / 17.08 | **21.09** |
| 08M 2026 | 30.09 / 25.09 | 21.09 / 16.09 | **21.09**, отдельно от июля |
| 09M 2026 | 30.10 / 27.10 | 20.10 / 15.10 | 20.10 |
| 10M 2026 | 30.11 / 25.11 | 20.11 / 17.11 | 20.11 |
| 11M 2026 | 30.12 / **24.12** | 21.12 / 16.12 | 21.12 |
| 12M 2026 | Ожидается 01.02.2027 / 27.01.2027 | Ожидается 20.01.2027 / 15.01.2027 | Ожидается 01.02.2027 |

Источник: [официальная таблица 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [349 в сентябре](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/septiembre/hasta-21-septiembre.html). Временные продления вследствие чрезвычайных обстоятельств имеют приоритет над базовым календарём.

### Import@ss: окна изменения base в 2025 и 2026

| Дата заявления | Дата начала новой base |
|---|---|
| 01.01–28.02 | 01.03 того же года |
| 01.03–30.04 | 01.05 |
| 01.05–30.06 | 01.07 |
| 01.07–31.08 | 01.09 |
| 01.09–31.10 | 01.11 |
| 01.11–31.12 | 01.01 следующего года |

Оба рассматриваемых года невисокосные. Это окна изменения RETA, не сроки подачи modelos AEAT и не обещание переноса окна на рабочий день по правилам налоговой domiciliación. Источник: [TGSS, Base de cotización y rendimientos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos).

## Формулы для движка

### 1. Выбор обязанности и календарь

Вход: профиль и его интервалы действия; NIF налогоплательщика; ejercicio/periodo; censal-обязанности; вид операции/удержания; REDEME/SII; historia 349; дата конца финансового года SL; история ранее принятых деклараций; требование AEAT; способ оплаты. Выход: перечень обязанностей с доказательством применимости, сроком подачи, отдельным сроком domiciliación и статусом источника.

```text
for each model, tax_period:
    applicable = obligation_rule(model, profile_at_period, activity, transactions, census)
    # Отсутствие платежа само по себе не означает applicable = false.
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

Не переносить 111/115 на 30 января вслед за 303. Для 202 создавать `1P`, `2P`, `3P` в апреле/октябре/декабре, не `1T–4T`. Для 200 нормативный срок — 25 календарных дней после шести месяцев с окончания налогового периода, с предусмотренным переносом; июльская дата подходит только календарному финансовому году. Напоминания допустимо отправлять заранее по внутренней настройке, но не называть внутреннюю дату законным дедлайном.

При переезде хранить дату фактического изменения domicilio и дату уведомления 036 отдельно. Для общего IRPF регион определяется правилами residencia habitual за год, а не разбиением налога по месяцам двух регионов; для Beckham нет региональной шкалы обычного IRPF, но адрес/Comunidad в 151 всё равно актуализируются.

### 2. Форматы: реестр по модели и году

**Ссылки на спецификации — обязательная часть контракта генератора.** Выбирать их по `ejercicio`, а не по календарной дате экспорта.

| Модель | Официальная спецификация | Способ подачи и вид структуры |
|---|---|---|
| 303 за 2025 | [DR303e25.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/DR303e25.xlsx), обновлена 04.12.2025 | Pre303/web-форма с Importar; страничный fixed-width с `<T...>` |
| 303 за 2026 | [DR303e26v101.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_26/DR303e26v101.xlsx), обновлена 28.01.2026 | То же; внутри книги версия обозначена `10.01`; не выводить номер схемы из имени файла |
| 130 за 2025/2026 | [DR130e15v12.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/DR130e15v12.xls), март 2019, версия 1.2 | Форма, Importar/Exportar `.130`; одна страница и обёртка |
| 111 | [dr111e16v18.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/dr111e16v18.xls), май 2021, для 2019+ | [Электронная форма с Importar](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-111/presentacion-electronica-modelo-111.html); fixed-width с обёрткой |
| 349 | [DR_Anexo_349.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_20/DR_Anexo_349.pdf), Orden HAC/174/2020, 2020+ | [Форма ≤40 000 записей или presentación mediante fichero](https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/identificacion-realizar-operaciones-otros-empresarios-ue/modelo-349.html); tipo 1 declarante + tipo 2 operaciones/rectificaciones |
| 390 за 2025 | [dr390e2025.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/dr390e2025.xlsx), обновлена 05.12.2025 | [Форма](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390.html) и [отдельная presentación con fichero](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390/modelo-390-presentacion-mediante-fichero.html); страничная fixed-width структура |
| 190 за 2025 | [DISENOS_LOGICOS_190_2025.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos_25/DISENOS_LOGICOS_190_2025.pdf), Orden HAC/1431/2025 | Форма ≤40 000 записей или [TGVI online](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/declaraciones-informativas-ayuda-tecnica/modelos-190-198/modelo-190-fichero.html); tipo 1 + tipo 2 perceptores |
| 347 за 2025+ | [347.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos/347.pdf), Orden HAC/1431/2025 | [Форма ≤40 000 записей или TGVI](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/forma-presentacion.html); tipo 1 + tipo 2 declarados/inmuebles |
| 151 за 2025/2026 | [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), 2023+ | Отдельная web-форма, Importar/Exportar; имя экспорта `NIF_Ejercicio_0A.151` |
| 100 за 2025 | [Renta2025.xsd](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/Renta2025.xsd), [diccionario](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/diccionarioXSD_2025.properties) | Renta WEB; опубликованный XML/XSD — иной формат, не контейнер 303/130 |

Для 390 ejercicio 2026 отдельный подтверждённый DR на дату проверки не найден: не выдавать файл 2025 с заменённым годом за гарантированно допустимый. Для ежегодно обновляемого 190 за 2026 также перепроверять публикацию к кампании. Каталоги: [100–199](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-100-199.html), [300–399](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-300-399.html), [архив 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/ejercicios-anteriores-modelos-300-399.html).

У информационных моделей 349/190/347 записи фиксированной длины определяются их PDF, а не конструкцией `<T303...>`: один registro tipo 1 идентифицирует заявителя, период и контрольные итоги; registros tipo 2 содержат контрагентов/получателей и специальные записи. Нельзя заменить их бухгалтерским CSV. Привязки claves/subclaves и счётчики брать из **конкретного DR**, не из названий колонок экранной формы. Для 190 AEAT отдельно предупреждает, что первый выбранный способ подачи (форма или fichero) определяет допустимый путь последующих подач; хранить канал исходной декларации. TGVI может разрешать подачу корректных записей с последующим исправлением остальных: не считать весь исходный набор сданным, пока не сверены принятые/отклонённые записи.

### 3. Общая сериализация 303/130

Ниже приведены проверенные **позиции с единицы**, длины и знаки. Для программного массива индекс равен `position - 1`; длина измеряется в байтах выбранной однобайтовой кодировки, а не в UTF-8 code points.

```text
format_amount(value_eur, width, signed):
    # Вход уже рассчитан налоговым модулем до евроцента.
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
# Никаких CSV-разделителей, UTF-8 BOM, XML indentation или переносов строк внутри записи.
```

Источник кодировки, выравнивания и `N` для отрицательных значений: [AEAT, Diseños de registro — breve manual, стр. 4–6, 10–12](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/Ayudas/Disenyos_registro_Manual_uso.pdf). Это позиционный текст, а не XML-документ для XML serializer: пробелы значимы, `trim` недопустим. Денежные расчёты — Decimal/целые центы; окончательное округление до 0,01 € по правилам конкретной casilla. Если конкретная инструкция не задаёт другое, техническая конвенция — decimal ROUND_HALF_UP, сверяемая с формой AEAT; не округлять каждое промежуточное выражение и не использовать двоичный float.

**Обёртка одинакова по позициям для двух проверенных DR:**

| Абсолютная позиция | Длина | Содержимое |
|---:|---:|---|
| 1 | 2 | `<T` |
| 3 | 3 | `303` либо `130` |
| 6 | 1 | `0` |
| 7 | 4 | Ejercicio, например `2026` |
| 11 | 2 | Periodo, например `3T`; у месячного 303 — `01`…`12` |
| 13 | 5 | `0000>` |
| 18 | 5 | `<AUX>` |
| 23 | 70 | Пробелы, reservado AEAT |
| 93 | 4 | Версия программы разработчика |
| 97 | 4 | Пробелы |
| 101 | 9 | NIF разработчика по инструкции DR |
| 110 | 213 | Пробелы |
| 323 | 6 | `</AUX>` |
| 329 | Переменная | Страницы модели |
| После последней страницы | 18 | `</T3030EEEEPP0000>` либо `</T1300EEEEPP0000>` |

Пример начала для 303 за 3T 2026: `<T303020263T0000><AUX>`; для 130: `<T130020263T0000><AUX>`. `EEEE`/`PP` здесь метасимволы объяснения, не буквальные значения в файле. В DR130 описание закрытия содержит опечатку `T1230`, но колонка **Contenido** однозначно указывает `</T1300AAAAPP0000>`: использовать 130.

### 4. Modelo 130: полностью определяемая единственная страница

После обёртки идёт **600-байтовая** страница `DR 13001`; приведённые позиции **локальны странице**, поэтому её позиция 1 находится в позиции 329 всего файла.

| Позиция | Длина | Поле |
|---:|---:|---|
| 1 | 11 | `<T13001000>` |
| 12 | 1 | Пробел, indicador de página complementaria; это не признак complementaria декларации |
| 13 | 1 | Tipo: `I` ingreso, `U` domiciliación, `G` CCT, `N` negativa, `B` a deducir |
| 14 | 9 | NIF |
| 23 | 60 | Apellidos |
| 83 | 20 | Nombre |
| 103 | 4 | Ejercicio |
| 107 | 2 | `1T`…`4T` |
| 109 + 17×(k−1), k=1…19 | 17 на поле | Casillas `[01]`…`[19]` последовательно |
| 432 | 1 | `X` для declaración complementaria, иначе пробел |
| 433 | 13 | Número justificante предыдущей декларации, если complementaria |
| 446 | 34 | IBAN для domiciliación, слева, далее пробелы |
| 480 | 96 | Reservado AEAT, пробелы |
| 576 | 13 | Sello electrónico reservado, пробелы |
| 589 | 12 | `</T13001000>` |

Casillas со знаком `N`: **03, 07, 11, 14, 17, 19**. Остальные денежные поля — `Num`, без отрицательных значений. В поле 17 символов — подразумеваемые две десятичные цифры, без запятой/точки. Полная длина простой декларации: **328 + 600 + 18 = 946 байт**.

Налоговый модуль передаёт рассчитанные значения casillas без повторного расчёта сериализатором. Для complementaria весь период рассчитывается заново; `[18]` — сумма результатов **a ingresar** предыдущих 130 того же ejercicio/periodo, не налог за все предыдущие кварталы; `[19] = [17] − [18]`. Пропущенная первичная 130 имеет `[18]=0`, без `X` и без фиктивного предыдущего justificante. Нулевой/отрицательный результат не превращать в `I` только ради платежа. Источники: DR130 выше и [официальные инструкции 130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

### 5. Modelo 303 за 2026: страницы и casillas

Рабочая книга содержит `DP30300`, `DP30301`, `DP30302`, `DP30303`, `DP30304`, `DP30305`, `DP303DID`. Для обычной деятельности régimen general нужны данные страницы 01, результата 03 и платёжного раздела DID; 02 — régimen simplificado; 04 — годовые сведения освобождённых от 390; 05 — соответствующие сведения prorrata/sectores diferenciados. **Пустые страницы 04/05 не включаются** согласно примечаниям DR. У применимой 02/повторяющихся страниц соблюдать её собственные условия повторения; не создавать её для консультанта без régimen simplificado.

| Страница | Начало / конец | Полная длина | Важное |
|---|---|---:|---|
| DP30301 | `<T30301000>` / `</T30301000>` | 1 581 | NIF, период, флаги и régimen general |
| DP30303 | `<T30303000>` / `</T30303000>` | 1 017 | Допинформация, результат, rectificativa |
| DP30304 | `<T30304000>` / `</T30304000>` | 998 | Последний период у освобождённых от 390; не добавлять без данных |
| DP30305 | `<T30305000>` / `</T30305000>` | 1 528 | Prorratas/sectores; не добавлять без данных |
| DP303DID | `<T303DID00>` / `</T303DID00>` | 823 | IBAN/BIC/зарубежный банк |

Для комбинации 01 + 03 + DID длина **3 767 байт** вместе с обёрткой. Это структурная проверка такой комбинации, не доказательство, что произвольные нулевые значения пройдут бизнес-валидацию AEAT.

**DP30301: позиции локальны странице.** Начало: позиция 12 пробел, 13 tipo declaración; 14/9 NIF; 23/80 nombre o razón social; 103/4 ejercicio; 107/2 periodo. Флаги 109–130 брать по DR, не заполнять все нулями: например, для обычного только régimen general позиция 111 = `3`; SII voluntario — 127; exoneración 390 — 128 (`0` вне последнего периода, в последнем `1`/`2`); volumen anual — 129 по условию DR. Позиция 130 — новое специальное поле combustible, для кварталов и 01 имеет `0`; его наличие меняет смещения относительно некоторых старых схем.

| Casilla | Позиция/длина DP30301 | Тип |
|---|---|---|
| 01 / 02 / 03 | 209/17; 226/5; 231/17 | Num; ставка `00400` |
| 04 / 05 / 06 | 287/17; 304/5; 309/17 | Num; ставка `01000` |
| 07 / 08 / 09 | 326/17; 343/5; 348/17 | Num; ставка `02100` |
| 10 / 11 | 365/17; 382/17 | Num; adquisiciones intracomunitarias |
| 12 / 13 | 399/17; 416/17 | Num; прочая inversión del sujeto pasivo |
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
| Reservado + sello | 1036/521; 1557/13 | Пробелы |
| Конец | 1570/12 | `</T30301000>` |

Оставшиеся поля, включая zero-rate/recargo equivalencia, всё равно физически присутствуют; заполнять **константами и нулями по DR**, не вырезать их. Для суммы IVA использовать все предписанные слагаемые, а не только популярные casillas:

```text
303[27] = [152]+[167]+[03]+[155]+[06]+[09]+[11]+[13]+[15]
          +[158]+[170]+[18]+[21]+[24]+[26]
303[45] = [29]+[31]+[33]+[35]+[37]+[39]+[41]+[42]+[43]+[44]
303[46] = [27] - [45]
```

**DP30303: ключевые поля результата.**

| Casilla/поле | Позиция/длина | Тип/смысл |
|---|---|---|
| 59 | 12/17 | N; intracomunitarias entregas y servicios |
| 60 | 29/17 | N; exportaciones y asimiladas; не автоматически любые услуги non-EU |
| 64 | 199/17 | N; `[46]+[58]+[76]` |
| 65 | 216/5 | Num; % Estado, 100% = `10000` |
| 66 | 221/17 | N; atribuible al Estado |
| 77 | 238/17 | Num; IVA importación pendiente |
| 110 / 78 / 87 | 255/17; 272/17; 289/17 | Num; остаток, применённая часть, остаток старых периодов |
| 68 | 306/17 | N; regularización Estado/forales |
| 108 | 323/17 | N; специальный ajuste por discrepancia, не универсальная «ручная поправка» |
| 69 | 340/17 | N |
| 70 | 357/17 | Num; предыдущие результаты a ingresar того же периода |
| 109 | 374/17 | Num; devoluciones acordadas AEAT того же периода |
| 112 | 391/17 | Num; особые pagos a cuenta modelo 319 по combustible, обычно 0 |
| 71 | 408/17 | N; окончательный resultado |
| Sin actividad | 425/1 | `X` либо пробел; нулевой IVA не означает автоматически отсутствие деятельности |
| Rectificativa | 426/1 | `X` либо пробел |
| Предыдущий justificante | 427/13 | Обязательно по условиям rectificativa |
| Изменить/отменить прежнюю domiciliación | 440/1 | `X` либо пробел |
| 111 — importe rectificación | 441/17 | Num; по правилам rectificativa, не общий размер переплаты |
| Motivo rectificaciones / discrepancia | 458/1; 459/1 | `X` либо пробел |
| Reservado / закрытие | 460/546; 1006/12 | Пробелы / `</T30303000>` |

```text
303[87] = [110] - [78]
303[69] = [66] + [77] - [78] + [68] + [108]
303[71] = [69] - [70] + [109] - [112]
# Первичная обычная declaración: [70]=[109]=0; [108]=0 без специального основания.
# Применение [78] и возврат/перенос отрицательного результата решает IVA-модуль.
# Нельзя считать [87] полным новым остатком: это остаток именно старых периодов.
```

В DID: SWIFT-BIC позиция 12/11, IBAN 23/34, banco 57/70, dirección 127/35, ciudad 162/30, código país 192/2, marca SEPA 194/1 (`0` пусто, `1` España, `2` UE-SEPA, `3` остальные), reservado 195/617, конец 812/12. Испанский IBAN — первые 24 символа с `ES`, остаток поля пробелы. При rectificativa с casilla 111>0 банковские реквизиты требуются и в некоторых вариантах не-devolución, кроме предусмотренного DR случая изменения исходной domiciliación.

Tipo 303: `I` ingreso, `U` domiciliación, `C` compensación, `D` devolución, `N` sin actividad/resultado cero, `G`/`V` CCT, `X` devolución transferencia extranjero. Для rectificativa с `[71]<0` и `[111]>0` DR требует определять тип по части `[71]`, не относящейся к `[111]`; не выбирать тип просто по знаку `[71]`.

Эти смещения относятся **только к DR303e26v101**. Для 2025 использовать соответствующие листы DR303e25. Генерация и импорт реального тестового файла в Sede здесь не выполнялись; приведённая структура извлечена из официальных книг, не из принятого сервером образца.

### 6. Принятие, исправление и платежи

```text
if no accepted_return_for_same_model_year_period:
    mode = ORIGINAL  # даже после срока
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

Для 100 в Renta WEB использовать встроенное `Modificar declaración presentada`; для предусмотренной rectificativa идентификация исходной декларации и casillas **103/104** по manual 2024, но **проверять словарь конкретного ejercicio перед генерацией**. Для 200 использовать Sociedades WEB/его актуальный DR и блок rectificativa, не заимствовать номера 303. Для информационных 190/180/347/349 нужны собственные операции alta/modificación/baja, complementaria/sustitutiva или rectificaciones записей согласно модели и выбранному каналу. Нельзя подать второй «обычный» файл и считать первый отменённым.

### 7. Recargo и оценка просрочки

Вход: первоначальный законный срок `D`, дата фактической подачи `F`, неуплаченная сумма, которая следует из позднего расчёта `B`, наличие requerimiento до подачи, история платежей и применимые годовые процентные ставки. Выход: **оценка** recargo/intereses и маршрут обработки, не новая casilla исходной декларации.

```text
if F <= D:
    late_filing_recargo = 0
elif previous_requerimiento:
    do not apply voluntary_art27_estimate
    route = review assessment/sanction procedure
elif B <= 0:
    recargo_art27 = 0
    route = evaluate formal_penalty_art198  # не «штрафа нет»
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

`legally_completed_calendar_months` — календарные месяцы, **не** `floor(days/30)`. Начало/окончание месячного интервала, месяцы без соответствующего числа и точная граница 12 месяцев требуют проверки по официальному расчёту/уведомлению AEAT: публичная найденная формулировка повторяет закон без отдельного примера на самой границе. До такой проверки движок должен показывать диапазон/предупреждение на спорной граничной дате, а не выдумывать гарантированный тариф. Это не мешает безусловным случаям: долг 1 000 € и подача спустя десять дней → 10 € recargo; при применимой скидке → 7,50 €. Через более 12 месяцев → 150 € плюс проценты с указанной даты, а не проценты за весь первый год.

Recargo обычно ликвидирует AEAT отдельно; **не добавлять его в resultado casilla 19 Modelo130 или casilla71 Modelo303**. Если налоговая декларация уже принята вовремя, но банк не списал деньги, проверять art.28 и обстоятельства оплаты, а не подавать дубликат и начислять art.27. Удержания и некоторые другие долги не допускают обычного aplazamiento: наличие кнопки признания долга не означает автоматического права на отсрочку.

## Сроки и модели

### Кому что подавать

Здесь «Beckham» означает действительную принятую opción art.93 с соблюдением условий, а не только наличие предпринимательской визы. Отсутствие модели в списке, который ведёт gestoría, не доказывает освобождение.

| Modelo | Кто/когда | Когда не возникает / важное ограничение | Срок |
|---|---|---|---|
| 303 | Autónomo любого из двух IRPF-профилей и SL при соответствующей IVA-деятельности | Beckham не освобождает от IVA. Чисто освобождённая деятельность может не иметь периодической обязанности; обратное начисление/иные события анализировать отдельно. При действующей периодической обязанности сдавать и нулевой период | Квартал/месяц по таблицам |
| 130 | Autónomo в estimación directa; применимость к разрешённой деятельности art.93 решать по специальным нормам, не по ярлыку профиля | Для профессиональной деятельности обычного IRPF освобождение при ≥70% дохода с retención за предыдущий год; в год начала — применимый период. SL не подаёт. Beckham нельзя автоматически включать/исключать без правил по виду дохода | Q1–Q3 до 20-го; Q4 до 30 января с переносом |
| 349 | Любой из профилей при соответствующих intra-EU поставках/приобретениях товаров или услуг | Non-EU операции сами по себе не создают 349; без включаемых операций не подавать нулевую. Покупка EU SaaS тоже может создавать обязанность | Месяц/квартал по самостоятельному тесту |
| 111 | Лицо/SL, выплачивающее заработную плату, профессиональные и иные включаемые доходы с обязанностью удержания | Это удержания **плательщика**, не retención из собственных выставленных счетов. Если выплачивался включаемый доход без фактического удержания из-за нулевой ставки, может требоваться отрицательная декларация; если выплат вовсе не было — иной случай | До 20-го после квартала; у соответствующих крупных плательщиков ежемесячно |
| 115 | Плательщик предпринимательской аренды городского объекта, подлежащей удержанию | Проверять исключения и сертификат арендодателя; не вся аренда жилья частным лицом создаёт 115 | Как 111 |
| 202 | SL и иные IS-плательщики с обязанностью pagos fraccionados | Для обычной небольшой SL при отсутствии суммы к уплате подача обычно не требуется; у больших плательщиков — особые правила нулевой подачи. Не создавать 202 владельцу-физлицу | Апрель/октябрь/декабрь, не июль |
| 390 | IVA resumen anual у обязанных к периодическим IVA-декларациям | Освобождение SII и установленных квартальных плательщиков только régimen simplificado/arrendamiento urbano в territorio común; годовые данные переходят в последний 303. Обычный консультант с régimen general не освобождён только потому, что у него 12 счетов | До 30 января |
| 190 | Годовые включаемые выплаты/удержания, связанные с 111 | Не отчёт о retenciones, которые удержали собственные клиенты. Включать соответствующие нулевые/освобождённые выплаты по правилам модели | До 31 января |
| 180 | Годовое резюме соответствующих arrendamientos/retenciones 115 | Не возникает только из-за собственного жилья или роли получателя арендной платы | До 31 января |
| 347 | Autónomo/SL с включаемыми операциями с третьими лицами сверх порога | Исключаются операции, уже охваченные специальной информацией с требуемым совпадением содержания: например, 349 и соответствующие удержания; SII и иные персональные исключения. **Non-EU услуга не равна экспортируемому товару**, исключение экспортов не переносить автоматически | Февраль следующего года |
| 100 | Обычный IRPF autónomo; администратор SL как физлицо — по его собственной обязанности | С 2023 для находившихся в RETA в какой-либо момент года действует обязанность IRPF-декларации, но у действующего Beckham применяется 151 вместо обычного100 | Кампания Renta следующего года |
| 151 | Действующий специальный режим art.93, включая соответствующего administrador/предпринимателя | Не заменяет 303/retenciones/декларации самой SL. Не предоставляется автоматически из-за NIE/visa | Срок ежегодной IRPF-кампании; в 2026 до 30 июня |
| 200 | SL за её собственный налоговый период | Не освобождать из-за «нет деятельности» или нулевой прибыли; пока есть субъект и обязанность IS, обычная SL подаёт | 25 дней после шести месяцев от конца периода |
| 714 | Физлицо с положительной cuota Patrimonio либо активами/правами выше 2 млн € по применимой сфере | Для Beckham — obligación real по соответствующим испанским активам, не автоматически мировое имущество. Минимумы/льготы региона рассчитываются отдельно | Вместе с Renta, в 2026 до 30 июня |
| 720 | Обычный резидент/SL при зарубежных активах, ролях и порогах, без исключения | AEAT прямо освобождает физлицо с art.93. Для SL/физлица с надлежащим учётом возможны отдельные бухгалтерские исключения. Личные активы администратора и активы SL проверяются отдельно | 1 января–31 марта |
| 721 | Зарубежная криптовалюта у custodio, соответствующие роли/порог | Self-custody не включается. Отдельное освобождение Beckham не выводить лишь из текста FAQ720 — см. «Неясности» | 1 января–31 марта |
| 036 | Alta/modificación/baja, domicilio, IAE/обязанности, ROI, предусмотренные налоговые опции | Не ежегодная подача ради подтверждения неизменности. 037 больше не использовать | Событийно, обычно месяц; alta/ROI до операций; отдельные окна опций |
| 102 | Второй платёж по допустимому 60/40 fraccionamiento обычной Renta | Не универсальная рассрочка всех моделей; просроченный первичный расчёт и 151 требуют отдельных правил | 05.11.2026 для Renta2025 |
| 718 | Физлицо при возникновении Impuesto Temporal de Solidaridad de las Grandes Fortunas | Не создавать автоматически всем, кто подаёт714; отдельный тест cuota/сферы обложения | Июль следующего года, в 2026 до31 июля |

Первичные источники для условий: [130, инструкции](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html), [202, когда подавать](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/4-impuesto-sobre-sociedades/4_8-pagos-fraccionados/4_8_2-modelos-pagos-fraccionados.html), [390, обязанные](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-09-declaraciones-informativas-iva-379/declaracion-resumen-anual-modelo-390/obligados-presentar-declaracion.html), [347, исключения](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 и art.93](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes/contribuyentes-obligados-declarar.html), [721](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html). Юридические расчёты каждого налога и условия Beckham должны подключаться из соответствующего налогового модуля, не дублироваться календарём.

Дополнительные обязательства включать по событию: 149 при opción/renuncia/exclusión Beckham; 123/193 при соответствующих выплатах капитала, например дивидендах SL; 216/296 при определённых выплатах нерезидентам. Это не обязанности каждого фрилансера и не замена перечисленных моделей. Для подачи самим владельцем self-hosted приложения статус colaborador social не нужен; для подачи за иное юридическое лицо необходимы надлежащие полномочия.

Для **149** в 2025–2026: opción principal — максимум **6 месяцев** от начала деятельности по alta Seguridad Social/допустимому документу; asociado — более позднее из окончания его шестимесячного срока от въезда и срока principal. Renuncia — **ноябрь–декабрь предшествующего году эффекта года**; например, для отказа с 2027 — 01.11–31.12.2026. Exclusión — **месяц с нарушения условий**; fin del desplazamiento при сохранении residencia fiscal за год — **месяц с окончания desplazamiento**. Передача 149 и приложений — самостоятельная процедура, не приложение по желанию к годовой 151. Источники: [календарь непериодических IRPF-моделей 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/impuesto-sobre-renta-personas-fisicas.html), [инструкция 149](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-149-irpf-comunicacion-opcion-exclusion_/instrucciones-cumplimentar-comunicacion.html).

### Практический путь пользователя

1. Получить FNMT/Cl@ve, сверить NIE/NIF и domicilio в AEAT; SL — сертификат/полномочия представителя. Закрытый ключ не хранить в открытом виде на сервере и не передавать маркетплейсу без осознанного оформления представительства.
2. Выбрать точные модель, ejercicio, periodo и режим подачи; экспортировать файл соответствующей версии либо использовать libros registro в установленном формате.
3. В Sede выбрать `Presentación`/`Importar` либо отдельную `Presentación mediante fichero`, где она существует. Встроенный веб-импорт файла не равен отдельному API. 349/190/347 поддерживают TGVI, 390 — отдельную подачу con fichero; для одиночных303/130/111 подтверждён обычный путь через форму с Importar.
4. Сверить casillas с libros, историю compensaciones и уже принятые декларации, устранить errores, прочитать avisos. Автоматически предзаполненные данные Pre303 могут не покрывать всю деятельность.
5. При положительном результате выбрать доступную оплату. После срока domiciliación ещё можно подать в общий срок с допустимым способом платежа; не ждать следующего квартала. Зарубежный банк/SEPA и `pago por transferencia` имеют собственные условия и время зачисления.
6. `Firmar y enviar` → сохранить PDF/CSV/justificante и подтверждение платежа отдельно. Для transferencia/признания долга отслеживать незавершённые шаги; для domiciliación — фактическое исполнение, отказ банка и saldo.
7. В Import@ss отдельно сверить alta RETA, rendimientos/base, уведомление regularización и recibos. Вход возможен через доступные certificado/Cl@ve/SMS, если номер зарегистрирован у TGSS; NIE в AEAT не гарантирует привязку телефона в TGSS.

## Пограничные случаи

### Налоги, сроки и подача

- **Один EU-клиент, 60 000 € за квартал:** 303 может остаться квартальным, а349 перейти на месяц. Порог349 проверяется не только по количеству счетов; при превышении во втором месяце нельзя ждать окончания квартала и затем отправить обычный квартальный349.
- **Клиент из США и сервис из Ирландии:** продажа не создаёт349, но покупка может; отсутствие испанского IVA на обоих счетах не означает одинаковый режим. Обороты non-EU услуг проверять для347 отдельно от экспортов товаров.
- **Испанский клиент удержал IRPF из нашего счёта:** его удержание попадает в наши расчёты IRPF, но не создаёт нашу111. Если мы сами оплатили испанскому профессионалу счёт с retención,111/190 могут возникнуть.
- **IVA к уплате ноль из-за зарубежных клиентов, но деятельность была:** не ставить `Sin actividad` автоматически. Если расходов было больше, выбрать корректный перенос/возврат, а не просто нулевой результат; отрицательная303 остаётся декларацией.
- **Закрытие autónomo в середине года:** сохраняются уже возникшие квартальные и годовые обязательства. В некоторых случаях освобождение390 теряется, если последний303 года уже не требуется. Одна дата baja в RETA не доказывает одновременную baja всех obligaciones AEAT.
- **Переезд между автономными сообществами:** не меняет общегосударственные ставки art.93, но требует корректного domicilio/сведений151 и отдельного определения региона для обычного IRPF и Patrimonio. Не рассчитывать полгода по одной региональной шкале и полгода по другой.
- **Beckham и семья:** FAQ720 содержит старое общее замечание, что режим не распространяется на семью; после расширения art.93 в2023 возможна собственная opción у квалифицирующихся членов семьи. Проверять персональный статус каждого, не освобождать супругу просто из-за режима мужа и не отрицать её отдельную opción на основании устаревшей фразы FAQ.
- **SL и administrador:** NIF, декларации, certificado и платежи SL отделены от собственных100/151/714 администратора. Подать200 с данными физлица недопустимо; личный Cl@ve не заменяет корпоративный certificado.
- **Последний день domiciliación прошёл, но общий срок ещё нет:** это не extemporánea. Предложить NRC/другой допустимый платёж, не начислять recargo заранее.
- **Налог оплачен, сеть оборвалась на подписи:** искать принятую декларацию и NRC; не платить повторно вслепую. **Подпись прошла, списание не прошло:** искать долг/состояние domiciliación, не отправлять дубликат декларации.
- **Исправление принятой303 с прежней domiciliación:** новая rectificativa не гарантирует автоматическую отмену старого списания. Проверить специальный флаг, допустимое окно изменения и подтверждение AEAT; иначе возможно двойное списание/неверная разница.
- **Пропущен срок с requerimiento:** добровольный безопасный расчёт art27 уже может быть неприменим. Требование — не только бумажное письмо: учитывать официально вручённые электронные уведомления. Не обещать «всего1%».
- **Выявлена ошибка прошлого квартала после подачи годовой:** требуется согласованное исправление соответствующего квартала и годовой информации; увеличение текущего303/130 без правильной привязки к прошлому периоду не всегда является законной regularización.
- **Информационная декларация приняла часть записей:** хранить идентификаторы и счётчики принятого набора; «файл отправлен» не значит «все190/349 операции приняты». Исправлять отказанные записи тем способом, который допускает используемый канал.

## Неясности

1. **2027: опубликован не весь календарь.** Прямое подтверждение01.02.2027 найдено для303 за4T2026. Другие будущие даты получены из действующих сроков и календарных переносов и явно помечены; начало Renta2026, её ежегодный приказ и окончательные окна domiciliación должны быть подгружены после публикации. Нельзя выдавать ожидаемое7/8апреля2027 за установленную дату. Региональный праздник25/26июля2027 может повлиять на конкретный официальный календарь200: расчёт26июля не является окончательным.

2. **Pre303 API — UNVERIFIED.** Проверены страницы Pre303, gestiones, описание функций и техническая помощь303; опубликованный WSDL/OpenAPI именно для Pre303 не найден. Это не доказательство отсутствия любого закрытого интеграционного канала. Подтверждённый проектный путь — официальный импорт файла/книг в форме и пользовательская подпись. Ни undocumented HTTP-вызовы, ни API SII/VERI*FACTU не объявлять поддерживаемой заменой подачи.

3. **Файлы описаны, но серверный импорт не испытан.** Байтовые позиции303/130 извлечены из официальных Excel; пробные декларации, реальные платежи и подача не выполнялись. До эксплуатации основной агент должен проверить экспорт→импорт на официальном симуляторе/форме без отправки:2025/2026, ingreso/negativa/compensación, отрицательные `N`, NIE, Ñ, IBAN, rectificativa. Это обязательная проверка совместимости, не заявленный результат текущего исследования.

4. **ВерсииDR и условные флаги меняются.** Для3032026 обнаружены дополнительные поля combustible/modelo319; использование смещений2025 опасно даже для пользователя, который топливом не торгует. DR3902026 не подтверждён. Выгрузки должны блокироваться при неподдерживаемом ejercicio, а не использовать «последний известный» формат без предупреждения.

5. **NIF Empresa Desarrollo у self-hosted разработчика.** DR требует NIFED и версиюSW, но проверенная инструкция не объясняет отдельную регистрацию разработчика для личного единичного импорта. Не подставлять вымышленный NIF поставщика и не утверждать, что достаточно пустого поля. Для собственного испанского разработчика использовать действительный NIF с проверкой валидатором; неизвестные требования конкретного канала уточнять у AEAT.

6. **721 для Beckham — отдельная непроверенная квалификация.** FAQ720 прямо освобождает art93; прочитанныйFAQ721 перечисляет резидентов и критерии custodia, но не содержит аналогичного прямого разъяснения дляart93. Не выдавать автоматическое освобождение721 только по аналогии. Если у пользователя есть зарубежная custodial-криптовалюта сверх порога, сохранить потенциальную обязанность с ручным разбором/первичной consulta DGT; не подавать автоматически лишнюю декларацию «на всякий случай».

7. **Граница полного месяца/12 месяцев в recargo.** Источники подтверждают формулу, но найденного официального примера на самом дне границы нет. Точная оценка на таких датах помечается UNVERIFIED и сверяется с расчётомAEAT/уведомлением; не заменять месяцы тридцатидневными блоками. Процентная таблица2026 подтверждает4,0625%, но для будущих годов нужна отдельная версия, а не экстраполяция.

8. **Конфликт сроков domiciliación в источниках AEAT.** Для **151** таблица calendario 2026 прямо указывает **25 июня**, но [инструкция 151 для ejercicio 2023+](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html) дважды указывает **26 июня**. Дополнительная проверка первичного акта разрешает противоречие в пользу **25.06.2026**: [Orden HFP/1338/2023, art. 4.2, стр. 5 PDF](https://www.boe.es/boe/dias/2023/12/15/pdfs/BOE-A-2023-25416.pdf) устанавливает «hasta, con carácter general, cinco días antes» окончания подачи, то есть 25 июня при окончании 30 июня; это совпадает с календарём. Дату 26 июня из инструкции не использовать для разрешения новой domiciliación 151 за 2025. Для **102** поиск показывал 30 сентября, прочитанная живая таблица 2026 — **02 ноября** с отдельным **20 октября** для IBAN. В документе воспроизведена живая таблица. Перед операцией брать актуальный нормативный срок и конкретную доступность действия в Sede; не смешивать первичную подачу с изменением ранее порученного платежа.

9. **Документ не заменяет расчётные модули налогов.** Он полностью перечисляет запрошенные modelos и сроки/каналы, но право на Beckham, необходимость130 для конкретного доходаart93, расчёт714/718, региональные вычеты и допустимость aplazamiento определяются соответствующими нормами, а не наличием кнопки или подписки. Не отключать модель на основании неопределённости: показывать, какие входные факты нужны для решения.
