*Переведено с испанского оригинала [kb/calendario-presentacion.md](../calendario-presentacion.md) 13.10.2026. Источник истины — испанский файл.*

## Резюме

- Проверено по доступным первичным источникам на **08.10.2026**. Год доходов (`ejercicio`) и год подачи — разные поля. Годовые декларации за ejercicio 2025 подаются в 2026 году. Декларации за ejercicio 2026 подаются в основном в 2027 году.
- Для малого бизнеса на общей территории (territorio común) квартальные modelos 303/130/111/115 обычно подаются до 20 апреля, 20 июля и 20 октября. **Для 4T сроки другие:** 111/115 — до 20 января; 303/130/349 и 390 — до 30 января, с переносом, если день нерабочий; 180/190 — до 31 января, с переносом.
- В 2026 году срок domiciliación для modelos 303/130 за 4T 2025 года — **27 января**, а не автоматически 25 января. Для обычных кварталов это 15 апреля, 15 июля или 15 октября. Календарь нельзя реализовать по формуле «дата подачи минус пять дней».
- Renta 2025 через интернет: **08.04–30.06.2026**. Domiciliación — до **25.06.2026**. Modelo 151 — отдельный сервис, а не обычный Renta WEB. **Cl@ve допускается**. Сертификат — не единственный способ входа.
- Для modelo 303 за 4T 2026 года AEAT уже прямо публикует дату **01.02.2027**. Остальные даты 2027 года ниже, которые не подтверждены собственным календарём AEAT, помечены как расчётные. Точная дата начала Renta 2026 в 2027 году — **UNVERIFIED**.
- Modelos 303/130 можно сформировать как текстовый файл по diseño de registro и импортировать в форму Sede. **Это не CSV, не PDF и не произвольный XML**, хотя файл содержит закрывающие теги `<T...>`.
- Проверенные действующие файлы: **DR303e26v101.xlsx** для 2026 года; **DR303e25.xlsx** для 2025 года; **DR130e15v12.xls** для 2019 года и последующих ejercicios. Год в названии спецификации 130 не означает, что она устарела.
- Pre303 — подтверждённый сервис предварительного заполнения формы. Публичный документированный API Pre303, который позволял бы сторонней программе рассчитать или подать декларацию без формы, **не подтверждён**. API SII или VERI*FACTU не заменяет подачу 303.
- NIE достаточно, чтобы получить испанский сертификат FNMT и зарегистрироваться в Cl@ve. Для этого нужно надлежащим образом подтвердить личность. Российский паспорт и TIE **не являются DNIe**. SL подаёт декларации с электронным сертификатом своего представителя или через уполномоченного представителя. Личный Cl@ve не заменяет сертификат SL.
- Статусы «файл создан», «форма проверена», «NRC получен», «декларация принята» и «налог уплачен» независимы друг от друга. Подачу подтверждают **justificante + CSV + дата и время AEAT**. При domiciliación нужно потом проверить списание со счёта.
- Подача после срока без предварительного requerimiento, если есть сумма к уплате: recargo за несвоевременную декларацию по ст. 27 LGT, **«1 процент плюс ещё 1 дополнительный процент за каждый полный месяц просрочки»**. По истечении 12 месяцев — **15% и проценты**. Декларация с нулевым результатом или информационная декларация не освобождена от санкций: к ним применяются собственные санкции.
- Autoliquidación rectificativa введена не одновременно для всех modelos. Для 303 — с 09/3T 2024 года. Для 100 — с ejercicio 2024. Для 200 — для периодов, начатых с 01.01.2024. Для 130 сохраняется complementaria. Неподанная первоначальная декларация не является complementaria.

## Правила

1. **Сроки и их переносы зависят от конкретной modelo и от календаря AEAT.** По данным AEAT, «если окончание срока подачи приходится на нерабочий день, срок заканчивается в первый следующий рабочий день». Для электронного обслуживания ориентиром служит официальный календарь Sede, а не любой список праздников по месту жительства. Для банковской domiciliación AEAT устанавливает: «между окончанием срока подачи autoliquidación с domiciliación платежа и окончанием общего срока подачи и добровольной уплаты этой же autoliquidación **должно быть не менее трёх рабочих дней или пяти календарных дней**. Для этих целей нерабочими днями считаются субботы, воскресенья, национальные праздники, а также автономные или местные праздники, которые затрагивают муниципалитет, где находится Departamento de Informática de la Agencia Tributaria». Правило применяется к рассмотренным здесь подачам 2025–2026 годов. Таблица 2026 года имеет приоритет над приблизительным правилом. Источник: [Сроки подачи autoliquidaciones с банковской domiciliación, 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html).

2. **Квартальная периодичность 349 не следует из квартальной периодичности 303.** Базовая периодичность сводной декларации (declaración recapitulativa, 349) — месячная. Квартальная периодичность допускается, «когда ни в отчётном квартале, ни в каждом из четырёх предыдущих календарных кварталов общая сумма поставок товаров и оказания услуг, которые должны быть отражены в сводной декларации, не превышает 50.000 евро без учёта налога на добавленную стоимость». Если порог превышен внутри квартала, «должна быть подана сводная декларация за месяц или месяцы, прошедшие с начала этого календарного квартала». Годовой 349 использовать нельзя. Если операций для отражения нет, «349 с нулями» не нужен. Для июля есть продлённый срок до 20 сентября. Для декабря или 4T срок — до 30 января. Применяется в 2025–2026 годах. Источники: [AEAT, внутрисоюзные операции](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/5-impuesto-sobre-valor-anadido/5_9-operaciones-intracomunitarias.html), [сроки 349, руководство по IVA 2026](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2026/capitulo-09-declaraciones-informativas-iva-379/declaracion-recapitulativa-operac-intracomunitarias-modelo-349/plazo-presentacion.html).

3. **Modelo 036 — обязанность, связанная с конкретными событиями, а не квартальная.** Declaración de alta: «до начала соответствующей деятельности или до возникновения обязанности удерживать налог или вносить платежи на счёт». Declaración de modificación: «1 месяц со дня, следующего за днём изменения». Declaración de baja: «1 месяц с момента прекращения деятельности или фактического погашения записей в Registro Mercantil». Для domicilio fiscal autónomo используется declaración censal de modificación (036), casilla 122. Смену адреса не нужно откладывать до Renta. Заявление о включении в Registro de Operadores Intracomunitarios (ROI) нужно подать до соответствующих внутрисоюзных операций. Для опций по IVA и IS есть специальные сроки. Например, «опция уплаты авансового платежа с части налоговой базы за период первых 3, 9 или 11 месяцев каждого календарного года» (ст. 40.3 LIS) осуществляется в «феврале года, в котором она должна вступить в силу, только для налоговых периодов, совпадающих с календарным годом». В 2026 году срок — до 02.03.2026. Modelo 037 упразднена с **03.02.2025**. Источники: [036 в календаре 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/modelo-036.html), [срок для изменения](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/plazos-presentacion/declaracion-modificacion-modelo-036.html), [casilla 122](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/guia-practica-cumplimentacion-modelo-censal-036/capitulo-01-cuestiones-generales/causas-presentacion-obligados-declarar/modificacion-modelo-036/casilla-122-domicilio-fiscal-modelo-036.html), [02.03.2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html).

4. **Идентификация зависит от декларанта, а не только от modelo.** Физические лица могут использовать Cl@ve для modelos 036, 100, 111, 115, 130, 149, 151, 180, 190, 303, 347, 349, 390, 714, 720 и 721. Сертификат или DNIe подходят для большего числа процедур. SL обязана подавать декларации электронно с сертификатом. Полномочия администратора или представителя должны быть признаны. Número de referencia подходит только для разрешённых процедур по IRPF. Это не универсальный способ входа. Применяется в 2025–2026 годах. Список сверен с календарём 2026 года. Источник: [AEAT, идентификация](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/recuerde/identificacion-presentar-autoliquidaciones.html).

5. **Для иностранца без DNIe есть полностью рабочий путь FNMT с NIE.** «Solicitud vía internet de su Certificado» (запрос сертификата через интернет) для физического лица → «Código de Solicitud» (код запроса) → «Acreditación de la identidad en una Oficina de Acreditación de Identidad» (подтверждение личности в офисе подтверждения личности) лично, с действующими оригиналами TIE или официального документа NIE и паспорта → «Descarga de su Certificado de Usuario» (загрузка сертификата пользователя) по инструкциям FNMT. Обычно нужна cita previa. Рекомендуется экспортировать защищённую резервную копию закрытого ключа. Для Cl@ve доступны три пути. Первый — «Registro por Internet en el sistema Cl@ve con certificado o DNI electrónico» (регистрация в системе Cl@ve через интернет с сертификатом или электронным DNI). Второй — очная регистрация. Третий — «Registro en Cl@ve por internet con carta de invitación y CSV» (регистрация в Cl@ve через интернет с письмом-приглашением и CSV). Письмо отправляется на domicilio fiscal. При NIE указывается номер носителя документа (número de soporte). Письмо даёт базовый уровень регистрации. Не все процедуры продвинутого уровня доступны. Нельзя предполагать, что для российского паспорта доступен конкретный вид видеоидентификации. Это действующая процедура, а не ежегодная налоговая ставка. Источники: [FNMT: документы](https://www.sede.fnmt.gob.es/registro-inicio/preguntas-frecuentes/-/asset_publisher/DKnDigPrgk4U/content/4-3-2-3-acreditacion-de-la-identidad-de-una-persona-fisica), [Cl@ve с письмом](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/registrarse-clave-pin/registro-internet-csv.html), [número de soporte](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/firma-digital-sistema-clave-pin-tecnica/incidencias-tecnicas-clave-pin/introduzca-soporte-valido.html).

6. **Renta WEB и modelo 151 — разные рабочие процессы.** Обычный IRPF подаётся через Renta WEB / modelo 100. Régimen Beckham использует собственную форму 151: Cl@ve или сертификат/DNIe, `Importar` и `Exportar` файла в формате BOE `.151`, `Validar declaración` и `Firmar y enviar`. Нельзя автоматически заменять 151 декларацией 100. Нельзя заявлять, что 151 — «только вручную, без файла». Для 151 опубликован DR для ejercicio 2023 и последующих. Он применим к рассмотренным здесь годам. Источники: [техническая помощь по 151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html), [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), [инструкции по 151](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html).

7. **Импортировать декларацию — не значит подать её.** После `Importar` нужно выбрать тип декларации (к уплате, domiciliación, reconocimiento de deuda и т. д.). Затем нужно исправить ошибки, которые покажет `Validar declaración`, выполнить `Firmar y enviar` и получить justificante. `Guardar`, `Vista previa`, `Exportar` и NRC сами по себе подачу не подтверждают. NRC — это «полный номер ссылки из 22 символов, который служит подтверждением платежа». Он подтверждает платёж, а не подачу декларации. Его данные должны совпадать с NIF/modelo/ejercicio/периодом/суммой. При `Reconocimiento de deuda` заявление об отсрочке или зачёте оформляется отдельно, по ссылке `Tramitar deuda` в квитанции о подаче, если его не заполнили прямо в этом процессе. Применяется к действующим формам 2025–2026 годов. Источники: [130](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-130.html), [151](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html).

8. **Pre303 не освобождает от проверки исходных данных.** Сервис предлагает Ventana Censal IVA, Identificación, Resultado и Cartera de cuotas a compensar. Расширенный расчёт возможен с SII или Libros Agregados. Для обязанных лиц вне SII, которые отвечают требованиям, он возможен с импортом libros registro. Представителю нужны соответствующие полномочия (apoderamientos) для всех функций, в частности для PRE303. На 08.10.2026 в изученной публичной документации не найден контракт API Pre303 для автоматической самостоятельной подачи. Подтверждён путь «форма + официальный файл или книги». Источники: [Pre303](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303.html), [функции](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/que-servicios-funcionalidades-tiene-nuevo-pre303.html), [доступ](https://sede.agenciatributaria.gob.es/Sede/iva/pre-303/acceder-pre303.html), [техническая помощь по 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303.html).

9. **RETA ведётся отдельно от AEAT, в Import@ss.** В `Base de cotización y rendimientos` сообщается или изменяется прогноз среднемесячного чистого дохода и base в пределах допустимого диапазона (tramo). В год есть до шести дат вступления изменений в силу. Немедленного ретроактивного изменения всех прошлых месяцев нет. В `Consulta de recibos de trabajo autónomo` доступны выставленные взносы (cuotas). Выставление взноса нужно сверять с банковским списанием. Правила системы действуют с 2023 года и применимы в 2025–2026 годах. Источники: [изменение base](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos), [руководство для autónomo](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo+Autonomo/guia), [квитанции](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Consulta%2Bde%2Bpagos%2By%2Bdeudas/ConsultaRecibos).

10. **Подача после срока без предварительного requerimiento и неуплата уже задекларированного долга — разные случаи.** Ст. 27 LGT применяется к autoliquidación, поданной добровольно после срока за правильно указанный период. Нельзя смешивать пропущенные операции с текущим кварталом. Recargo снижается на 25% только при выполнении условий уплаты долга и recargo по ст. 27.5. Нельзя обещать снижение при любом reconocimiento de deuda. Если долг не уплачен, могут добавиться recargos del período ejecutivo по ст. 28. Текущая шкала ст. 27 действует с **11.07.2021** и, следовательно, в 2025–2026 годах. Источник: [LGT, ст. 27–28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27).

11. **Отсутствие суммы к уплате не отменяет обязанность подать декларацию и не исключает санкции.** Ст. 198 LGT, за неподачу в срок без экономического ущерба: «фиксированный денежный штраф 200 евро или, если речь идёт о declaraciones censales […], 400 евро». Для информационных деклараций: «фиксированный денежный штраф 20 евро за каждое данное или совокупность данных, относящихся к одному и тому же лицу или организации, которые должны были быть включены в декларацию, минимум 300 евро и максимум 20.000 евро». Если декларации поданы «после срока без предварительного requerimiento налоговой администрации, санкция и минимальный и максимальный пределы составляют половину предусмотренных в предыдущем пункте». Это возможная санкция в отдельной процедуре. Это не сумма, которая автоматически добавляется в casilla налога. Если после requerimiento есть ущерб для Hacienda, может применяться ст. 191: от 50 до 150% неуплаченной cuota, в зависимости от нарушения. Применяется в 2025–2026 годах. Источник: [LGT, ст. 191, 198, 199](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a198).

12. **Способ исправления зависит от modelo и налогового периода.** Для 303 с 09/3T 2024 года autoliquidación rectificativa — общий путь. Это верно и при увеличении, и при уменьшении результата. Есть специальные исключения, в частности некоторые споры об IVA repercutido и о нарушении нормы более высокого ранга. Для 100 с ejercicio 2024 rectificativa используется в предусмотренных случаях. Для отдельных случаев регуляризации сохраняются специальные complementarias. Для 200 в периодах, начатых с 01.01.2024, используется rectificativa. Для 130, действующей формы 151 и обычных удержаний сохраняются собственные механизмы complementaria или заявления об исправлении (solicitud de rectificación). Новшество 100 нельзя автоматически применять к ним. Источники: [303, исправления](https://sede.agenciatributaria.gob.es/Sede/iva/presentar-declaracion-iva-modelo-303/errores-declaracion.html), [FAQ 303](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/autoliquidacion-rectificativa.html), [100 ejercicio 2024](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2024/c18-cuota-liquida-resultante-autoliquidacion/regularizacion-situaciones-tributarias/general.html), [200](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/manual-sociedades-2024/capitulo-02-identificac-autoliq-compl-incn/autoliquidacion-rectificativa.html), [130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

## Цифры

### Фиксированные значения для календаря и рисков

| Параметр | 2025 | 2026 | Уточнение |
|---|---:|---:|---|
| Лимит квартального 349 | 50 000 € | 50 000 € | Текущий квартал и каждый из четырёх предыдущих; без IVA, по соответствующим исходящим операциям |
| Порог обычных операций на одного контрагента для 347 | >3 005,06 € | >3 005,06 € | Годовая сумма с IVA; исключения важнее самого порога |
| Формальная обязанность 714 независимо от cuota | Активы или права >2 000 000 € | Так же | Дополнительно к обязанности при cuota к уплате; учитывать активы соответствующей сферы налогообложения, до вычета долгов и с учётом освобождённых активов |
| Начальный порог 720 | >50 000 € по соответствующему блоку | Так же | Это не единый порог для всего имущества за рубежом; есть бухгалтерские и личные исключения |
| Повторная 720 | Рост соответствующего блока >20 000 € относительно последней обязательной подачи | Так же | Учитывать также прекращение владения или полномочий, а не только рост |
| Начальный порог 721 | В совокупности >50 000 € | Так же | Криптовалюты на хранении у кастодиана за рубежом; самостоятельное хранение не включается |
| Повторная 721 | Рост >20 000 € и некоторые случаи утраты статуса | Так же | Проверять правила ст. 42 quater; не копировать буквально все правила 720 |
| Ст. 27, до 12 месяцев | 1% + 1 п.п./полный месяц | Так же | Без requerimiento; дни не делятся на 30 |
| Ст. 27, после 12 месяцев | 15% + проценты | Так же | Проценты только со дня, следующего за окончанием этих 12 месяцев |
| Снижение recargo по ст. 27.5 | 25% от recargo | 25% | Условное; долг и проценты этой скидкой не уменьшаются |
| Налоговые проценты за просрочку (interés de demora) | 4,0625% годовых | 4,0625% по проверенной таблице или её продлению | Не замораживать ставку на будущие годы |
| Ст. 28: ejecutivo / apremio reducido / ordinario | 5% / 10% / 20% | Так же | Взаимоисключающие; 20% совместимы с процентами |
| Ст. 198: обычная декларация без ущерба | 200 € / 100 € добровольно | Так же | До других применимых снижений санкции |
| Ст. 198: declaración censal | 400 € / 200 € добровольно | Так же | Для 036 autónomo; не путать со 100 € по ст.198.5 для физического лица без деятельности |
| Ст. 198: информационная декларация | 20 €/данное, мин. 300 €, макс. 20 000 € | Так же | Добровольно: 10 €/данное, мин. 150 €, макс. 10 000 € |
| Лимит веб-форм 349/190/347 | 40 000 записей | 40 000 записей в действующих инструкциях | При превышении — файл/TGVI; небольшой файл тоже допускается |

Источники таблицы: [LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186), [проценты, Banco de España](https://clientebancario.bde.es/pcb/es/menu-horizontal/productosservici/relacionados/tiposinteres/guia-textual/tiposinteresrefe/tabla_tipos_interes_demora.html), [AEAT, проценты 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/irpf-2025/c18-cuota-liquida-resultante-autoliquidacion/incremento-cuotas-liquidas-estatal-autonomica/calculo-intereses-demora/reglas-calculo.html), [714](https://sede.agenciatributaria.gob.es/Sede/no-residentes/impuesto-sobre-patrimonio/declaracion-impuesto-patrimonio-no-residentes.html), [исключения 347](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes.html), [721 FAQ](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html).

### Подачи в 2026 году и закрытие ejercicio 2026 в начале 2027 года

Все даты включительные. `—` означает, что domiciliación не применяется к информационной декларации. Это не означает, что обязанности подачи нет.

| Modelo / период | Срок подачи | Последний день domiciliación | Статус |
|---|---|---|---|
| 111, 115: 4T 2025 | 01–20.01.2026 | 15.01.2026 | AEAT |
| 303, 130: 4T 2025 | 01–30.01.2026 | **27.01.2026** | AEAT |
| 349: 4T/12M 2025; 390: год 2025 | 01–30.01.2026 | — | AEAT |
| 190, 180: год 2025 | 01.01–02.02.2026 | — | AEAT |
| 347: год 2025 | 01.02–02.03.2026 | — | AEAT |
| 720, 721: год 2025 | 01.01–31.03.2026 | — | AEAT |
| 303, 130, 111, 115: 1T 2026 | 01–20.04.2026 | 15.04.2026 | AEAT |
| 349: 1T 2026 | 01–20.04.2026 | — | AEAT |
| 202: 1P 2026 | 01–20.04.2026 | 15.04.2026 | AEAT; по умолчанию это не «квартальная прибыль за 1T» |
| 100, 151, 714: год 2025 | Кампания через интернет 08.04–30.06.2026 | 25.06.2026 | Общий конец срока и domiciliación подтверждены для всех трёх; 151 — отдельный сервис |
| 303, 130, 111, 115: 2T 2026 | 01–20.07.2026 | 15.07.2026 | AEAT |
| 349: 2T 2026 | 01–20.07.2026 | — | AEAT |
| 200: календарный год 2025 | 01–27.07.2026 | **22.07.2026** | AEAT; 25 июля — суббота |
| 718: год 2025, если возникает ITSGF | 01–31.07.2026 | 28.07.2026 | AEAT; не заменяет 714 |
| 303, 130, 111, 115: 3T 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 349: 3T 2026 | 01–20.10.2026 | — | AEAT |
| 202: 2P 2026 | 01–20.10.2026 | 15.10.2026 | AEAT |
| 102: второй платёж обычной Renta 2025 при допустимой рассрочке (fraccionamiento) | До 05.11.2026 | Собственные сроки управления domiciliación, см. ниже | AEAT; не переносить этот режим автоматически на 151 |
| 202: 3P 2026 | 01–21.12.2026 | **16.12.2026** | AEAT; 20 декабря — воскресенье |
| 111, 115: 4T 2026 | 01–20.01.2027 | 15.01.2027 | Расчёт по действующему правилу; полный календарь 2027 года UNVERIFIED |
| 303: 4T 2026 | 01.01–**01.02.2027** | Ожидается 27.01.2027 | AEAT уже опубликовала конец срока подачи; domiciliación 2027 года — расчётная |
| 130: 4T 2026; 349: 4T/12M 2026; 390: год 2026 | 01.01–01.02.2027 | Для 130 ожидается 27.01.2027; для остальных — | Расчёт: 30 января — суббота |
| 190, 180: год 2026 | 01.01–01.02.2027 | — | Расчёт: 31 января — воскресенье |
| 347: год 2026 | 01.02–01.03.2027 | — | Расчёт: 28 февраля — воскресенье |
| 720, 721: год 2026 | 01.01–31.03.2027 | — | Действующее годовое правило; календарь 2027 года ещё не подтверждён |
| 100, 151, 714: год 2026 | Ожидается апрель–30.06.2027 | Ожидается 25.06.2027 | Начало и окончательный календарь кампании **UNVERIFIED** |
| 200: календарный год 2026 | Ожидается 01–26.07.2027 | Ожидается 21.07.2027 | Расчёт: 25 июля — воскресенье; проверить утверждённый календарь и праздники |

Источники: [годовой календарь 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual.html), [domiciliación](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [30 января](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/enero/hasta-30-enero.html), [2 февраля](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/febrero/hasta-2-febrero.html), [2 марта](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-2-marzo.html), [31 марта](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/marzo/hasta-31-marzo.html), [303 до 1 февраля 2027 года](https://sede.agenciatributaria.gob.es/Sede/en_gb/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/calendario-anual/febrero-2027/hasta-1-febrero-2027.html).

Для кампании Renta 2025: телефонная помощь AEAT **06.05–30.06.2026**, запись (cita) **29.04–29.06**; очная помощь **01.06–30.06**, запись (cita) **29.05–29.06**. Это не гарантирует, что AEAT примет к рассмотрению предпринимательский случай или случай régimen Beckham. Для помощи действуют критерии допуска. [Даты кампании](https://sede.agenciatributaria.gob.es/Sede/ayuda/contenidos-lectura-facil/calendario-contribuyente-2026-simplificado-personas-fisicas/fechas-campana-renta-patrimonio.html).

Управление вторым платежом 102: **действующая таблица AEAT** на момент проверки указывает для **02.11.2026** «До 2 ноября (для налогоплательщиков, которые оформили domiciliación первого платежа, — отозвать/восстановить или оформить domiciliación)» и для **20.10.2026** «До 20 октября для изменения IBAN». В поисковом фрагменте той же страницы появлялась старая дата 30 сентября. Нужно использовать действующую страницу или актуальные инструкции. Эти сроки нельзя смешивать с первой domiciliación Renta.

### Месячные режимы: все сроки календарного 2026 года

Небольшой объём не отменяет месячный 303, если есть REDEME/SII по соответствующему основанию. Месячные 111/115 возникают, в частности, у крупных компаний. `M` — месяц операций. Даты без года ниже относятся к 2026 году.

| Период | 303: подача / domiciliación | 111/115: подача / domiciliación | 349: подача |
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

Источник: [официальная таблица 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/plazos-presentacion-autoliquidaciones-domiciliacion-bancaria.html), [349 в сентябре](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/calendario-anual/septiembre/hasta-21-septiembre.html). Временные продления из-за чрезвычайных обстоятельств имеют приоритет над базовым календарём.

### Import@ss: сроки изменения base в 2025 и 2026 годах

| Дата заявления | Дата вступления в силу новой base |
|---|---|
| 01.01–28.02 | 01.03 того же года |
| 01.03–30.04 | 01.05 |
| 01.05–30.06 | 01.07 |
| 01.07–31.08 | 01.09 |
| 01.09–31.10 | 01.11 |
| 01.11–31.12 | 01.01 следующего года |

Ни один из двух рассмотренных годов не является високосным. Это сроки изменения в RETA, а не сроки подачи modelos AEAT. Также не гарантируется, что срок переносится на следующий рабочий день по правилам налоговой domiciliación. Источник: [TGSS, Base de cotización y rendimientos](https://portal.seg-social.gob.es/wps/portal/importass/importass/Categorias/Altas,+bajas+y+modificaciones/Bajas+y+modificaciones/BCRendimientos).

## Формулы для движка

### 1. Выбор обязанности и календарь

Вход: профиль и интервалы его действия; NIF налогоплательщика; ejercicio/период; обязанности по censo; тип операции или удержания; REDEME/SII; история 349; дата закрытия финансового года SL; история ранее принятых деклараций; requerimiento AEAT; способ оплаты. Выход: список обязанностей с доказательством их применимости, срок подачи, собственный срок domiciliación и статус источника.

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

Нельзя переносить 111/115 на 30 января вслед за 303. Для 202 нужно создавать `1P`, `2P`, `3P` в апреле, октябре и декабре, а не `1T–4T`. Для 200 законный срок — 25 календарных дней после шести месяцев, следующих за окончанием налогового периода, с предусмотренным переносом. Июльская дата относится только к финансовому году, который совпадает с календарным. Напоминания можно отправлять заранее по внутренней настройке. Но внутреннюю дату нельзя показывать как законный срок.

При смене адреса нужно хранить отдельно фактическую дату смены адреса и дату сообщения в 036. Для общего IRPF автономное сообщество (comunidad) определяется по правилам обычного места жительства за год. Налог не делится по месяцам между двумя сообществами. В régimen Beckham нет автономной шкалы обычного IRPF. Но адрес и Comunidad в 151 всё равно нужно обновить.

### 2. Форматы: реестр по modelo и году

**Ссылки на спецификации — обязательная часть контракта генератора.** Их выбирают по `ejercicio`, а не по календарной дате экспорта.

| Modelo | Официальная спецификация | Способ подачи и тип структуры |
|---|---|---|
| 303 за 2025 | [DR303e25.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/DR303e25.xlsx), обновлена 04.12.2025 | Pre303/веб-форма с Importar; фиксированная ширина по страницам с `<T...>` |
| 303 за 2026 | [DR303e26v101.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_26/DR303e26v101.xlsx), обновлена 28.01.2026 | Так же; внутри книги версия указана как `10.01`; номер схемы нельзя выводить из имени файла |
| 130 за 2025/2026 | [DR130e15v12.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/DR130e15v12.xls), март 2019 года, версия 1.2 | Форма, Importar/Exportar `.130`; одна страница и обёртка |
| 111 | [dr111e16v18.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos/dr111e16v18.xls), май 2021 года, для 2019+ | [Электронная форма с Importar](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-111/presentacion-electronica-modelo-111.html); фиксированная ширина с обёрткой |
| 349 | [DR_Anexo_349.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_20/DR_Anexo_349.pdf), Orden HAC/174/2020, 2020+ | [Форма ≤40 000 записей или подача файлом](https://sede.agenciatributaria.gob.es/Sede/iva/iva-operaciones-comercio-exterior/identificacion-realizar-operaciones-otros-empresarios-ue/modelo-349.html); тип 1 — декларант + тип 2 — операции/исправления |
| 390 за 2025 | [dr390e2025.xlsx](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos_25/dr390e2025.xlsx), обновлена 05.12.2025 | [Форма](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390.html) и [отдельная подача файлом](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-390/modelo-390-presentacion-mediante-fichero.html); структура фиксированной ширины по страницам |
| 190 за 2025 | [DISENOS_LOGICOS_190_2025.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/archivos_25/DISENOS_LOGICOS_190_2025.pdf), Orden HAC/1431/2025 | Форма ≤40 000 записей или [TGVI online](https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/declaraciones-informativas-ayuda-tecnica/modelos-190-198/modelo-190-fichero.html); тип 1 + тип 2 — получатели |
| 347 за 2025+ | [347.pdf](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_300_399/archivos/347.pdf), Orden HAC/1431/2025 | [Форма ≤40 000 записей или TGVI](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/forma-presentacion.html); тип 1 + тип 2 — декларируемые лица/недвижимость |
| 151 за 2025/2026 | [DR151E2023.xls](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/DR151E2023.xls), 2023+ | Собственная веб-форма, Importar/Exportar; имя файла экспорта `NIF_Ejercicio_0A.151` |
| 100 за 2025 | [Renta2025.xsd](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/Renta2025.xsd), [словарь](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/DR_100_199/diccionarioXSD_2025.properties) | Renta WEB; опубликованный XML/XSD — другой формат, а не контейнер 303/130 |

Для 390 за ejercicio 2026 на дату проверки не найден подтверждённый собственный DR. Нельзя подавать файл 2025 года с изменённым годом так, будто он гарантированно допустим. Modelo 190 обновляется каждый год. Для 190 за 2026 год тоже нужно заново проверить публикацию перед кампанией. Каталоги: [100–199](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-100-199.html), [300–399](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/modelos-300-399.html), [архив 303](https://sede.agenciatributaria.gob.es/Sede/ayuda/disenos-registro/ejercicios-anteriores-modelos-300-399.html).

В информационных modelos 349/190/347 записи фиксированной длины определены в их PDF, а не структурой `<T303...>`. Запись типа 1 идентифицирует декларанта, период и контрольные итоги. Записи типа 2 содержат контрагентов или получателей и специальные записи. Их нельзя заменить бухгалтерским CSV. Сочетания ключей и подключей (claves и subclaves) и счётчики берутся из **конкретного DR**, а не из названий колонок экранной формы. Для 190 AEAT прямо предупреждает: первый выбранный способ подачи (форма или файл) определяет допустимый путь последующих подач. Канал исходной декларации нужно сохранять. TGVI может позволить подать корректные записи и исправить остальные позже. Нельзя считать поданным весь исходный набор, пока принятые и отклонённые записи не сверены.

### 3. Общая сериализация 303/130

Ниже приведены **проверенные позиции, отсчитанные от единицы**, длины и знаки. Для массива в программе индекс равен `position - 1`. Длина измеряется в байтах выбранной однобайтовой кодировки, а не в code points UTF-8.

```text
format_amount(value_eur, width, signed):
    # Входное значение уже рассчитано налоговым модулем с точностью до евроцента.
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
# Без разделителей CSV, без BOM UTF-8, без отступов XML и без переводов строки внутри записи.
```

Источник по кодировке, выравниванию и `N` для отрицательных значений: [AEAT, Diseños de registro — краткое руководство, с. 4–6, 10–12](https://sede.agenciatributaria.gob.es/static_files/Sede/Disenyo_registro/Ayudas/Disenyos_registro_Manual_uso.pdf). Это позиционный текст, а не XML-документ для XML-сериализатора. Пробелы значимы, `trim` недопустим. Денежные расчёты ведутся в Decimal или в целых центах. Итоговое округление до 0,01 € следует правилам каждой casilla. Если конкретная инструкция не указывает иное, техническая конвенция — decimal ROUND_HALF_UP со сверкой по форме AEAT. Нельзя округлять каждое промежуточное выражение. Нельзя использовать двоичный float.

**Обёртка имеет одинаковые позиции в обоих проверенных DR:**

| Абсолютная позиция | Длина | Содержимое |
|---:|---:|---|
| 1 | 2 | `<T` |
| 3 | 3 | `303` или `130` |
| 6 | 1 | `0` |
| 7 | 4 | Ejercicio, например `2026` |
| 11 | 2 | Период, например `3T`; в месячном 303 — `01`…`12` |
| 13 | 5 | `0000>` |
| 18 | 5 | `<AUX>` |
| 23 | 70 | Пробелы, резерв AEAT |
| 93 | 4 | Версия программы разработчика |
| 97 | 4 | Пробелы |
| 101 | 9 | NIF разработчика по инструкции DR |
| 110 | 213 | Пробелы |
| 323 | 6 | `</AUX>` |
| 329 | Переменная | Страницы modelo |
| После последней страницы | 18 | `</T3030EEEEPP0000>` или `</T1300EEEEPP0000>` |

Пример начала для 303 за 3T 2026 года: `<T303020263T0000><AUX>`. Для 130: `<T130020263T0000><AUX>`. `EEEE`/`PP` здесь — метасимволы пояснения, а не буквальные значения файла. В DR130 описание закрывающего тега содержит опечатку `T1230`. Но колонка **Contenido** (содержимое) однозначно указывает `</T1300AAAAPP0000>`: использовать 130.

### 4. Modelo 130: единственная полностью определённая страница

После обёртки идёт страница `DR 13001` размером **600 байт**. Указанные позиции — **локальные позиции страницы**. Поэтому её позиция 1 находится на позиции 329 полного файла.

| Позиция | Длина | Поле |
|---:|---:|---|
| 1 | 11 | `<T13001000>` |
| 12 | 1 | Пробел, индикатор дополнительной страницы; он не означает, что декларация является complementaria |
| 13 | 1 | Тип: `I` ingreso, `U` domiciliación, `G` CCT, `N` negativa, `B` a deducir |
| 14 | 9 | NIF |
| 23 | 60 | Фамилии (Apellidos) |
| 83 | 20 | Имя (Nombre) |
| 103 | 4 | Ejercicio |
| 107 | 2 | `1T`…`4T` |
| 109 + 17×(k−1), k=1…19 | 17 на поле | Casillas `[01]`…`[19]` подряд |
| 432 | 1 | `X` для complementaria; иначе пробел |
| 433 | 13 | Номер justificante предыдущей декларации, если это complementaria |
| 446 | 34 | IBAN для domiciliación, выравнивание влево, далее пробелы |
| 480 | 96 | Резерв AEAT, пробелы |
| 576 | 13 | Зарезервированная электронная печать (sello electrónico), пробелы |
| 589 | 12 | `</T13001000>` |

Casillas со знаком `N`: **03, 07, 11, 14, 17, 19**. Остальные денежные поля — `Num`, без отрицательных значений. В поле из 17 символов два неявных десятичных знака, без запятой и без точки. Общая длина простой декларации: **328 + 600 + 18 = 946 байт**.

Налоговый модуль передаёт рассчитанные значения casillas. Сериализатор их не пересчитывает. В complementaria пересчитывается весь период. `[18]` — это сумма результатов **к уплате** предыдущих 130 за тот же ejercicio/период, а не налог всех предыдущих кварталов; `[19] = [17] − [18]`. Неподанная первоначальная 130 имеет `[18]=0`, без `X` и без фиктивного предыдущего justificante. Нулевой или отрицательный результат нельзя превращать в `I` только ради возможности заплатить. Источники: указанный выше DR130 и [официальные инструкции по 130](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html).

### 5. Modelo 303 за 2026 год: страницы и casillas

Рабочая книга содержит `DP30300`, `DP30301`, `DP30302`, `DP30303`, `DP30304`, `DP30305` и `DP303DID`. Для обычной деятельности в régimen general нужны данные страницы 01, результат страницы 03 и раздел оплаты DID. Страница 02 относится к régimen simplificado. Страница 04 содержит годовую информацию для освобождённых от 390. Страница 05 содержит соответствующую информацию о prorrata или sectores diferenciados. **Пустые страницы 04/05 не включаются**, согласно примечаниям DR. Для применимой страницы 02 и для повторяемых страниц нужно соблюдать их собственные условия повторения. Страницу 02 нельзя создавать для консультанта, который не находится в régimen simplificado.

| Страница | Начало / конец | Общая длина | Важно |
|---|---|---:|---|
| DP30301 | `<T30301000>` / `</T30301000>` | 1 581 | NIF, период, индикаторы и régimen general |
| DP30303 | `<T30303000>` / `</T30303000>` | 1 017 | Дополнительная информация, результат, rectificativa |
| DP30304 | `<T30304000>` / `</T30304000>` | 998 | Последний период для освобождённых от 390; не добавлять без данных |
| DP30305 | `<T30305000>` / `</T30305000>` | 1 528 | Prorratas/sectores; не добавлять без данных |
| DP303DID | `<T303DID00>` / `</T303DID00>` | 823 | IBAN/BIC/иностранный банк |

Для комбинации 01 + 03 + DID длина вместе с обёрткой составляет **3 767 байт**. Это структурная проверка этой комбинации. Это не доказательство того, что любое нулевое значение пройдёт бизнес-валидацию AEAT.

**DP30301: позиции локальные для страницы.** Начало: позиция 12 — пробел; 13 — тип декларации; 14/9 — NIF; 23/80 — имя или наименование (razón social); 103/4 — ejercicio; 107/2 — период. Индикаторы 109–130 берутся из DR. Нельзя заполнять их все нулями. Например, для того, кто платит налоги только в обычном régimen general, позиция 111 = `3`. Добровольный SII — позиция 127. Освобождение от 390 — позиция 128 (`0` вне последнего периода; в последнем — `1`/`2`). Годовой объём — позиция 129 по условию DR. Позиция 130 — новое специальное поле для топлива. Для кварталов и для 01 оно равно `0`. Наличие этого поля меняет смещения относительно некоторых старых схем.

| Casilla | Позиция/длина DP30301 | Тип |
|---|---|---|
| 01 / 02 / 03 | 209/17; 226/5; 231/17 | Num; ставка `00400` |
| 04 / 05 / 06 | 287/17; 304/5; 309/17 | Num; ставка `01000` |
| 07 / 08 / 09 | 326/17; 343/5; 348/17 | Num; ставка `02100` |
| 10 / 11 | 365/17; 382/17 | Num; внутрисоюзные приобретения |
| 12 / 13 | 399/17; 416/17 | Num; другие случаи inversión del sujeto pasivo |
| 14 / 15 | 433/17; 450/17 | N; изменения (modificaciones) |
| 27 | 696/17 | N; итого cuota devengada |
| 28 / 29 | 713/17; 730/17 | Num; внутренние текущие |
| 30 / 31 | 747/17; 764/17 | Num; внутренние инвестиционные товары |
| 32 / 33 | 781/17; 798/17 | Num; импорт текущий |
| 34 / 35 | 815/17; 832/17 | Num; импорт инвестиционный |
| 36 / 37 | 849/17; 866/17 | Num; внутрисоюзные текущие |
| 38 / 39 | 883/17; 900/17 | Num; внутрисоюзные инвестиционные |
| 40 / 41 | 917/17; 934/17 | N; исправление вычетов |
| 42 / 43 / 44 | 951/17; 968/17; 985/17 | N |
| 45 / 46 | 1002/17; 1019/17 | N |
| Резерв + печать | 1036/521; 1557/13 | Пробелы |
| Конец | 1570/12 | `</T30301000>` |

Остальные поля, включая поля нулевой ставки и recargo de equivalencia, физически остаются в записи. Они заполняются **константами и нулями из DR**. Их не удаляют. Для итога IVA используются все предписанные слагаемые, а не только привычные casillas:

```text
303[27] = [152]+[167]+[03]+[155]+[06]+[09]+[11]+[13]+[15]
          +[158]+[170]+[18]+[21]+[24]+[26]
303[45] = [29]+[31]+[33]+[35]+[37]+[39]+[41]+[42]+[43]+[44]
303[46] = [27] - [45]
```

**DP30303: ключевые поля результата.**

| Casilla/поле | Позиция/длина | Тип/значение |
|---|---|---|
| 59 | 12/17 | N; внутрисоюзные поставки и услуги |
| 60 | 29/17 | N; экспорт и приравненные операции; не включает автоматически любую услугу за пределами ЕС |
| 64 | 199/17 | N; `[46]+[58]+[76]` |
| 65 | 216/5 | Num; % Estado, 100% = `10000` |
| 66 | 221/17 | N; относимое на Estado |
| 77 | 238/17 | Num; отложенный IVA при импорте |
| 110 / 78 / 87 | 255/17; 272/17; 289/17 | Num; остаток, применённая часть, остаток прошлых периодов |
| 68 | 306/17 | N; регуляризация Estado/forales |
| 108 | 323/17 | N; специальная корректировка из-за расхождения; это не универсальная «ручная корректировка» |
| 69 | 340/17 | N |
| 70 | 357/17 | Num; предыдущие результаты к уплате за тот же период |
| 109 | 374/17 | Num; возвраты, назначенные AEAT за тот же период |
| 112 | 391/17 | Num; специальные авансовые платежи по modelo 319 за топливо, обычно 0 |
| 71 | 408/17 | N; итоговый результат |
| Нет деятельности (Sin actividad) | 425/1 | `X` или пробел; нулевой IVA не означает автоматически, что деятельности не было |
| Rectificativa | 426/1 | `X` или пробел |
| Предыдущий justificante | 427/13 | Обязателен по условиям rectificativa |
| Изменить или отменить предыдущую domiciliación | 440/1 | `X` или пробел |
| 111 — сумма исправления | 441/17 | Num; по правилам rectificativa, а не полная сумма переплаты |
| Причина исправлений / расхождение | 458/1; 459/1 | `X` или пробел |
| Резерв / закрытие | 460/546; 1006/12 | Пробелы / `</T30303000>` |

```text
303[87] = [110] - [78]
303[69] = [66] + [77] - [78] + [68] + [108]
303[71] = [69] - [70] + [109] - [112]
# Обычная первоначальная декларация: [70]=[109]=0; [108]=0, если нет специальной причины.
# Применение [78] и возврат или зачёт отрицательного результата решает модуль IVA.
# [87] нельзя считать новым полным остатком: это остаток прошлых периодов.
```

В DID: SWIFT-BIC — позиция 12/11; IBAN — 23/34; банк — 57/70; адрес — 127/35; город — 162/30; код страны — 192/2; отметка SEPA — 194/1 (`0` пусто, `1` Испания, `2` ЕС-SEPA, `3` остальные); резерв — 195/617; конец — 812/12. Испанский IBAN — это первые 24 символа с `ES`. Остаток поля заполняется пробелами. В rectificativa с casilla 111>0 банковские данные требуются и в некоторых вариантах, которые не являются возвратом. Исключение — предусмотренный в DR случай изменения исходной domiciliación.

Тип 303: `I` ingreso, `U` domiciliación, `C` compensación, `D` devolución, `N` нет деятельности/нулевой результат, `G`/`V` CCT, `X` возврат переводом за границу. Для rectificativa с `[71]<0` и `[111]>0` DR требует определять тип по той части `[71]`, которая не относится к `[111]`. Тип нельзя выбирать только по знаку `[71]`.

Эти смещения относятся **только к DR303e26v101**. Для 2025 года используются соответствующие листы DR303e25. Здесь реальный тестовый файл не создавался и не импортировался в Sede. Указанная структура извлечена из официальных книг, а не из образца, принятого сервером.

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

Для 100 в Renta WEB используется встроенная опция `Modificar declaración presentada`. Для предусмотренной rectificativa указываются исходная декларация и casillas **103/104** по руководству 2024 года. Но **словарь конкретного ejercicio нужно проверить перед генерацией**. Для 200 используется Sociedades WEB или его действующий DR и блок rectificativa. Номера casillas из 303 для него не используются. Для информационных 190/180/347/349 нужны собственные операции alta, modificación или baja, complementaria или sustitutiva, или исправления записей. Выбор зависит от modelo и выбранного канала. Нельзя подать второй «обычный» файл и считать первый аннулированным.

### 7. Recargo и оценка просрочки

Вход: исходный законный срок `D`, фактическая дата подачи `F`, неуплаченная сумма по поздней autoliquidación `B`, наличие requerimiento до подачи, история платежей и применимые годовые процентные ставки. Выход: **оценка** recargo и процентов и путь обработки. Это не новая casilla исходной декларации.

```text
if F <= D:
    late_filing_recargo = 0
elif previous_requerimiento:
    do not apply voluntary_art27_estimate
    route = review assessment/sanction procedure
elif B <= 0:
    recargo_art27 = 0
    route = evaluate formal_penalty_art198  # не означает «санкции нет»
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

`legally_completed_calendar_months` — это календарные месяцы, **а не** `floor(days/30)`. Начало и конец месячного интервала, месяцы без соответствующего числа и точную границу 12 месяцев нужно проверять по официальному расчёту или уведомлению AEAT. Найденная публичная формулировка повторяет закон и не даёт собственного примера для точной границы. До такой проверки движок должен показывать диапазон или предупреждение на сомнительной граничной дате. Он не должен придумывать гарантированную ставку. Это не влияет на ясные случаи. Долг 1 000 € и подача через десять дней → recargo 10 €. С применимым снижением → 7,50 €. Если прошло более 12 месяцев → 150 € плюс проценты с указанной даты, а не проценты за весь первый год.

Обычно AEAT начисляет recargo отдельно. **Его нельзя добавлять к результату casilla 19 Modelo130 или casilla71 Modelo303**. Если декларация уже принята в срок, но банк не списал сумму, нужно проверить ст.28 и обстоятельства платежа. Подавать дубликат и рассчитывать ст.27 в этом случае не нужно. Удержания и некоторые другие долги не допускают обычной отсрочки (aplazamiento). Наличие опции reconocimiento de deuda не даёт автоматического права на отсрочку.

## Сроки и modelos

### Кто что подаёт

Здесь «Beckham» означает действительную и принятую опцию по ст.93 с выполнением её условий. Визы предпринимателя для этого недостаточно. Если modelo нет в списке, который ведёт gestoría, это не доказывает освобождение.

| Modelo | Кто/когда | Когда не возникает / важное ограничение | Срок |
|---|---|---|---|
| 303 | Autónomo любого из двух профилей IRPF и SL с соответствующей деятельностью, облагаемой IVA | Régimen Beckham не освобождает от IVA. Исключительно освобождённая деятельность может не иметь периодической обязанности. Inversión del sujeto pasivo и другие факты анализируются отдельно. Если периодическая обязанность есть, период с нулевым результатом тоже подаётся | Квартал/месяц по таблицам |
| 130 | Autónomo в estimación directa; применение к деятельности, допущенной по ст.93, решается специальными нормами, а не меткой профиля | В профессиональной деятельности при обычном IRPF — освобождение, если ≥70% доходов предыдущего года были с удержанием; в год начала — применимый период. SL его не подаёт. В régimen Beckham его нельзя автоматически включать или исключать без правил по типу дохода | 1T–3T до 20-го числа; 4T до 30 января, с переносом |
| 349 | Любой из профилей с соответствующими внутрисоюзными поставками или приобретениями товаров или услуг | Операции вне ЕС сами по себе не порождают 349. Без операций для отражения он не подаётся с нулями. Покупка SaaS из ЕС тоже может породить обязанность | Месяц/квартал по собственной проверке |
| 111 | Лицо или SL, которые выплачивают зарплаты, профессиональные доходы или другие включённые доходы с обязанностью удерживать налог | Это удержания **плательщика**, а не удержания из собственных выставленных счетов. Если включённый доход выплачен без фактического удержания из-за нулевой ставки, может потребоваться отрицательная (negativa) декларация. Если выплат не было вообще, это другой случай | До 20-го числа после квартала; ежемесячно для соответствующих крупных плательщиков |
| 115 | Плательщик по предпринимательской аренде городской недвижимости, облагаемой удержанием | Нужно проверять исключения и сертификат арендодателя. Не любая аренда жилья у частного лица порождает 115 | Как для 111 |
| 202 | SL и другие плательщики IS, обязанные вносить авансовые платежи | Малой обычной SL без суммы к уплате обычно не нужно его подавать. У крупных налогоплательщиков есть специальные правила подачи с нулями. Нельзя создавать 202 для участника — физического лица | Апрель/октябрь/декабрь, не июль |
| 390 | Годовая сводная декларация по IVA для обязанных подавать периодические декларации по IVA | Освобождены SII и квартальные плательщики, которые платят налог только в régimen simplificado или по аренде городской недвижимости на общей территории; годовые данные переходят в последний 303. Обычный консультант в régimen general не освобождается только потому, что у него 12 счетов | До 30 января |
| 190 | Включённые годовые выплаты и удержания, связанные со 111 | Это не отчёт об удержаниях, которые сделали сами клиенты. Нужно включать соответствующие нулевые или освобождённые выплаты по правилам modelo | До 31 января |
| 180 | Годовая сводка соответствующих арендных платежей и удержаний по 115 | Не возникает только из-за наличия собственного жилья или из-за получения арендной платы | До 31 января |
| 347 | Autónomo/SL с включаемыми операциями с третьими лицами выше порога | Исключаются операции, уже охваченные другой специальной информацией с требуемым совпадением содержания: например, 349 и соответствующие удержания; SII и другие личные исключения. **Услуга вне ЕС не равна экспортированному товару**. Исключение для экспорта не переносится автоматически | Февраль следующего года |
| 100 | Обычный IRPF autónomo; администратор SL как физическое лицо — по собственной обязанности | С 2023 года тот, кто был в RETA в какой-либо момент года, обязан подать декларацию IRPF. Но при действующем régimen Beckham применяется 151 вместо обычного 100 | Кампания Renta следующего года |
| 151 | Действующий специальный режим по ст.93, включая соответствующего администратора или предпринимателя | Не заменяет 303, удержания и декларации самой SL. Не предоставляется автоматически из-за наличия NIE или визы | Срок годовой кампании IRPF; в 2026 году — до 30 июня |
| 200 | SL за свой налоговый период | Не освобождается из-за «отсутствия деятельности» или нулевой прибыли. Пока существуют субъект и обязанность по IS, обычная SL подаёт декларацию | 25 дней после шести месяцев, следующих за концом периода |
| 714 | Физическое лицо с положительной cuota по Patrimonio или с активами и правами более 2 миллионов € в применимой сфере | В régimen Beckham — обязанность по реальному принципу (obligación real) по соответствующим испанским активам, а не автоматически по мировому имуществу. Автономные минимумы и льготы рассчитываются отдельно | Вместе с Renta; в 2026 году — до 30 июня |
| 720 | Обычный резидент или SL с активами, позициями и порогами за рубежом, без исключения | AEAT прямо освобождает физическое лицо, которое применяет ст.93. Для SL или физического лица с надлежащим бухгалтерским учётом могут быть собственные бухгалтерские исключения. Личные активы администратора и активы SL проверяются отдельно | 1 января–31 марта |
| 721 | Криптовалюты за рубежом у кастодиана, соответствующие позиции и порог | Самостоятельное хранение не включается. Нельзя выводить собственное освобождение для régimen Beckham только из текста FAQ720; см. «Открытые вопросы» | 1 января–31 марта |
| 036 | Alta, modificación или baja, адрес, IAE и обязанности, ROI, предусмотренные налоговые опции | Не подаётся каждый год, чтобы подтвердить, что ничего не изменилось. 037 больше не используется | По факту события, обычно месяц; alta/ROI — до операций; собственные сроки для опций |
| 102 | Второй платёж допустимой рассрочки 60/40 обычной Renta | Это не универсальная отсрочка для всех modelos. Первоначальная autoliquidación после срока и 151 требуют собственных правил | 05.11.2026 для Renta2025 |
| 718 | Физическое лицо, если возникает Impuesto Temporal de Solidaridad de las Grandes Fortunas | Не создавать автоматически для каждого, кто подаёт 714. Нужна собственная проверка cuota и сферы налогообложения | Июль следующего года; в 2026 году — до 31 июля |

Первичные источники условий: [130, инструкции](https://sede.agenciatributaria.gob.es/Sede/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-130-irpf______esionales-estimacion-directa-fraccionado_/instrucciones.html), [202, когда подавать](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-practicos/folleto-actividades-economicas/4-impuesto-sobre-sociedades/4_8-pagos-fraccionados/4_8_2-modelos-pagos-fraccionados.html), [390, обязанные лица](https://sede.agenciatributaria.gob.es/Sede/eu_es/ayuda/manuales-videos-folletos/manuales-practicos/manual-iva-2025/capitulo-09-declaraciones-informativas-iva-379/declaracion-resumen-anual-modelo-390/obligados-presentar-declaracion.html), [347, исключения](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-347-decla_____racion-anual-operaciones-personas_/operaciones-excluidas-modelo-347.html), [720 и ст.93](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-720-decla_____sobre-bienes-derechos-extranjero_/preguntas-frecuentes/contribuyentes-obligados-declarar.html), [721](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/declaraciones-informativas/modelo-721-decla-sobre-monedas-extranjero/preguntas-frecuentes-sobre-modelo-721.html). Юридические расчёты по каждому налогу и условия régimen Beckham нужно брать из соответствующего налогового модуля. Календарь их не дублирует.

Дополнительные обязанности включаются по факту события. 149 — при выборе, отказе или исключении из régimen Beckham. 123/193 — при соответствующих выплатах доходов от капитала, например дивидендов SL. 216/296 — при определённых выплатах нерезидентам. Это не обязанности каждого независимого профессионала. Они не заменяют modelos из списка. Чтобы сам владелец подавал декларации через self-hosted приложение, статус colaborador social не нужен. Чтобы подавать от имени другого юридического лица, нужны надлежащие apoderamientos.

Для **149** в 2025–2026 годах. Основная опция — не позднее **6 месяцев** с начала деятельности по alta в Seguridad Social или по допустимому документу. Для связанного лица (asociado) действует срок, который заканчивается позже: конец его шести месяцев с момента въезда или срок основного лица. Отказ (renuncia): **ноябрь–декабрь года, предшествующего году вступления в силу**. Например, чтобы отказаться с действием в 2027 году, срок — 01.11–31.12.2026. Исключение (exclusión): **один месяц с момента невыполнения условий**. Окончание командировки (desplazamiento) с сохранением налогового резидентства за год: **один месяц с окончания командировки**. Подача 149 и его приложений — отдельная процедура, а не необязательное приложение к годовому 151. Источники: [календарь непериодических modelos IRPF 2026](https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026/informacion-sobre-presentacion-modelos-no-periodicos/impuesto-sobre-renta-personas-fisicas.html), [инструкции по 149](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-149-irpf-comunicacion-opcion-exclusion_/instrucciones-cumplimentar-comunicacion.html).

### Практический маршрут пользователя

1. Получить сертификат FNMT или Cl@ve. Сверить NIE/NIF и адрес в AEAT. Для SL — сертификат или apoderamientos представителя. Не хранить закрытый ключ без защиты на сервере. Не передавать его маркетплейсу без осознанного оформления представительства.
2. Выбрать точные modelo, ejercicio, период и способ подачи. Экспортировать файл соответствующей версии или использовать libros registro в установленном формате.
3. В Sede выбрать `Presentación`/`Importar` или собственную `Presentación mediante fichero`, где она есть. Встроенный веб-импорт файла не равен собственному API. Modelos 349/190/347 допускают TGVI. Modelo 390 допускает собственную подачу файлом. Для отдельных modelos 303/130/111 подтверждён обычный путь через форму с Importar.
4. Сверить casillas с книгами, историей зачётов и уже принятыми декларациями. Исправить ошибки и прочитать предупреждения. Данные, автоматически предзаполненные в Pre303, могут охватывать не всю деятельность.
5. Если результат положительный, выбрать доступный способ оплаты. После срока domiciliación декларацию ещё можно подать в пределах общего срока с допустимым способом оплаты. Ждать следующего квартала не нужно. Иностранный банк/SEPA и `Reconocimiento de deuda y pago por transferencia` имеют собственные условия и сроки зачисления.
6. `Formalizar ingreso / devolución` → `Firmar y enviar` → отдельно сохранить PDF, CSV, justificante и подтверждение платежа. Для перевода или reconocimiento de deuda выполнить оставшиеся шаги. Для domiciliación проверить фактическое списание, отказ банка и остаток.
7. В Import@ss отдельно сверить alta в RETA, доходы (rendimientos) и base, уведомление о регуляризации и квитанции. Войти можно с сертификатом, Cl@ve или SMS, если они доступны и номер зарегистрирован в TGSS. Наличие NIE в AEAT не гарантирует, что телефон привязан в TGSS.

## Пограничные случаи

### Налоги, сроки и подача

- **Один клиент из ЕС, 60 000 € за квартал:** 303 может остаться квартальным, а 349 может перейти на месячную периодичность. Порог 349 не проверяется только по количеству счетов. Если порог превышен во втором месяце, нельзя ждать конца квартала и потом отправлять обычный квартальный 349.
- **Клиент из США и услуга из Ирландии:** продажа не порождает 349, а покупка может его породить. Отсутствие испанского IVA в обоих счетах не означает, что режим одинаковый. Операции с услугами вне ЕС проверяются для 347 отдельно от экспорта товаров.
- **Испанский клиент удержал IRPF из нашего счёта:** его удержание входит в наши расчёты IRPF, но не порождает наш 111. Если мы платим испанскому профессионалу по счёту с удержанием, могут возникнуть 111/190.
- **Нулевой IVA к уплате из-за иностранных клиентов, но деятельность была:** не отмечать `Sin actividad` автоматически. Если расходы были больше, нужно выбрать правильный зачёт или возврат, а не просто нулевой результат. Отрицательный 303 всё равно является декларацией.
- **Baja autónomo в середине года:** уже возникшие квартальные и годовые обязанности сохраняются. В некоторых случаях освобождение от 390 теряется, если последний 303 года уже не требуется. Дата baja в RETA не доказывает одновременную baja всех обязанностей перед AEAT.
- **Переезд между автономными сообществами:** государственные ставки ст.93 не меняются. Но нужны правильный адрес и правильные данные 151. Для обычного IRPF и Patrimonio нужно отдельно определить сообщество. Нельзя считать полгода по одной автономной шкале и полгода по другой.
- **Régimen Beckham и семья:** FAQ720 содержит старое общее замечание о том, что режим не распространяется на семью. После расширения ст.93 в 2023 году члены семьи, которые отвечают требованиям, могут осуществить собственную опцию. Положение каждого проверяется отдельно. Жену нельзя освободить только из-за режима мужа. Ей также нельзя отказать в собственной опции из-за устаревшей фразы FAQ.
- **SL и администратор:** NIF, декларации, сертификат и платежи SL отделены от собственных modelos 100/151/714 администратора. Подавать 200 с данными физического лица нельзя. Личный Cl@ve не заменяет сертификат общества.
- **Последний день domiciliación прошёл, а общий срок — нет:** это не подача после срока. Нужно предложить NRC или другую допустимую оплату. Не нужно рассчитывать recargo заранее.
- **Налог уплачен, но связь оборвалась при подписании:** найти принятую декларацию и NRC. Не платить повторно вслепую. **Подпись завершена, но списания не было:** найти долг или статус domiciliación. Не отправлять дубликат декларации.
- **Исправление принятого 303 с предыдущей domiciliación:** новая rectificativa не гарантирует автоматическую отмену предыдущего списания. Нужно проверить специальный индикатор, допустимый срок изменения и подтверждение AEAT. Иначе возможно двойное списание или неверная разница.
- **Срок пропущен, есть requerimiento:** безопасный добровольный расчёт по ст.27 может уже не применяться. Requerimiento — это не только бумажное письмо: учитываются официально врученные электронные уведомления. Не обещать «только 1%».
- **Ошибка предыдущего квартала обнаружена после подачи годовой декларации:** требуется согласованное исправление соответствующего квартала и годовой информации. Увеличение текущего 303/130 без правильной привязки к прошлому периоду не всегда является законной регуляризацией.
- **Информационная декларация приняла часть записей:** нужно сохранить идентификаторы и счётчики принятого набора. «Файл отправлен» не означает «все операции 190/349 приняты». Отклонённые записи исправляются способом, который допускает использованный канал.

## Открытые вопросы

1. **2027: календарь опубликован не полностью.** Найдено прямое подтверждение даты 01.02.2027 для 303 за 4T 2026 года. Остальные будущие даты получены из действующих сроков и переносов календаря. Они явно помечены. Начало Renta2026, её годовой приказ (orden) и окончательные сроки domiciliación нужно загрузить после публикации. Ожидаемую дату 7/8 апреля 2027 года нельзя показывать как установленную. Автономный праздник 25/26 июля 2027 года может повлиять на конкретный официальный календарь для 200. Расчётная дата 26 июля не окончательная.

2. **API Pre303: UNVERIFIED.** Изучены страницы Pre303, процедуры (gestiones), описание функций и техническая помощь по 303. Опубликованный WSDL/OpenAPI именно для Pre303 не найден. Это не доказывает, что закрытого канала интеграции нет. Подтверждённый для проекта путь — официальный импорт файла или книг в форму и подпись пользователя. Нельзя объявлять допустимой заменой подачи ни недокументированные HTTP-вызовы, ни API SII или VERI*FACTU.

3. **Файлы описаны, но импорт на сервере не проверен.** Байтовые позиции 303/130 извлечены из официальных файлов Excel. Тестовые декларации, реальные платежи и подачи не выполнялись. Перед запуском в работу главный агент должен проверить экспорт→импорт в официальном симуляторе или в форме без отправки: 2025/2026, ingreso/negativa/compensación, отрицательные `N`, NIE, Ñ, IBAN, rectificativa. Это обязательная проверка совместимости, а не заявленный результат этого исследования.

4. **Версии DR и условные индикаторы меняются.** В 303 за 2026 год обнаружены дополнительные поля для топлива/modelo 319. Использовать смещения 2025 года опасно даже для пользователя, который не торгует топливом. DR для 390 за 2026 год не подтверждён. Экспорт нужно блокировать, если ejercicio не поддерживается. Нельзя без предупреждения использовать «последний известный формат».

5. **NIF Empresa Desarrollo для self-hosted разработчика.** DR требует NIFED и версию SW. Но изученная инструкция не объясняет собственную регистрацию разработчика для отдельного личного импорта. Нельзя ставить выдуманный NIF поставщика. Нельзя утверждать, что достаточно оставить поле пустым. Для собственного испанского разработчика нужно использовать действительный NIF и проверить его валидатором. Неизвестные требования конкретного канала нужно уточнять у AEAT.

6. **721 в régimen Beckham — собственная непроверенная квалификация.** FAQ720 прямо освобождает лиц по ст.93. Прочитанная FAQ721 перечисляет резидентов и критерии хранения. Но она не содержит прямого равнозначного пояснения для ст.93. Нельзя автоматически предоставлять освобождение от 721 только по аналогии. Если у пользователя есть криптовалюты на хранении у кастодиана за рубежом выше порога, возможная обязанность сохраняется. Нужна ручная проверка или предварительный запрос (consulta) в DGT. Ненужная декларация не подаётся автоматически «на всякий случай».

7. **Граница полного месяца и 12 месяцев для recargo.** Источники подтверждают формулу. Но официальный пример ровно на границе не найден. Точная оценка в эти даты помечается как UNVERIFIED и сверяется с расчётом или уведомлением AEAT. Месяцы не заменяются блоками по тридцать дней. Таблица процентов 2026 года подтверждает 4,0625%. Но для будущих лет нужна собственная версия, а не экстраполяция.

8. **Конфликт сроков domiciliación в источниках AEAT.** Для **151** таблица календаря 2026 года прямо указывает **25 июня**. Но [инструкции по 151 для ejercicio 2023 и последующих](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-sobre-renta-personas-fisicas/modelo-151-decla_____los-trabajadores-desplazados-espanol_/instrucciones-cumplimentacion-ejercicio-2023-siguientes.html) дважды указывают **26 июня**. Дополнительная проверка первичной нормы решает противоречие в пользу **25.06.2026**. [Orden HFP/1338/2023, ст. 4.2, с. 5 PDF](https://www.boe.es/boe/dias/2023/12/15/pdfs/BOE-A-2023-25416.pdf) устанавливает, что domiciliación «может быть оформлена с начала срока и, как общее правило, до дня, который наступает за пять дней до окончания срока подачи». Это 25 июня, если срок заканчивается 30 июня. Это совпадает с календарём. Дату 26 июня из инструкций нельзя использовать, чтобы допустить новую domiciliación для 151 за 2025 год. Для **102** поиск показывал 30 сентября. Прочитанная действующая таблица 2026 года указывает **02 ноября** и собственный срок **20 октября** для IBAN. Документ воспроизводит действующую таблицу. Перед каждой операцией нужно брать действующий нормативный срок и конкретную доступность действия в Sede. Нельзя смешивать первоначальную подачу с изменением уже назначенного платежа.

9. **Этот документ не заменяет модули расчёта налогов.** Он полностью перечисляет запрошенные modelos, их сроки и каналы. Но право на régimen Beckham, необходимость 130 для конкретного дохода по ст.93, расчёт 714/718, автономные вычеты и допустимость отсрочки определяются соответствующими нормами. Их не определяет наличие кнопки или подписки. Нельзя отключать modelo из-за неопределённости. Нужно показать, какие входные факты необходимы для решения.
