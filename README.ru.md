[English](README.md) | Русский | [Español](README.es.md)

# gestor

Локальный gestor для autónomo и SL в Испании: счета, расходы, IVA/IRPF/Beckham/SL, RETA и календарь подач. Один пользователь, локально, без зависимостей (Python 3.12+, stdlib). Считает декларации и объясняет каждую сумму законом; подаёте вы сами.

Всё на английском, русском и испанском: интерфейс, карточки источников права, база знаний и документация. Язык интерфейса переключается в меню профиля или в «Анкете» и хранится в профиле. MCP-сервер отвечает на том же языке.

## Начать с агентом

Вставьте это в Claude Code или Codex. Агент установит gestor и проведёт первую сессию, по одному вопросу за раз.

```text
Установи gestor из https://github.com/gestor-es/gestor-es и проведи мою первую сессию. Говори со мной по-русски.
1. Склонируй в ~/gestor-es. gestor нужен Python 3.12+: если python3 старее, помоги поставить новый и используй его ниже.
2. В ~/gestor-es запусти интерфейс так, чтобы он работал и после твоего выхода:
   nohup python3 -m gestor > gestor.log 2>&1 &
   Потом дай мне ссылку http://127.0.0.1:8765.
3. Подключи MCP-сервер gestor для своей программы командой из раздела README
   «Помощь в Sede из Claude Code или Codex», запуская из ~/gestor-es.
4. Скажи мне перезапустить тебя в ~/gestor-es, чтобы сервер загрузился (`claude --continue` или `codex resume --last`),
   и написать «продолжай». Потом следуй инструкциям First session от сервера gestor.
Ничего не подавай, не подписывай и не оплачивай. Не спрашивай PIN Cl@ve, пароли и пароль сертификата.
```

Следующие сессии: в Claude Code — `/mcp__gestor__start`, в Codex — «начни с gestor». Агент назовёт ближайший срок и что для него нужно.

## Запустить самому

```bash
python3 -m gestor                      # http://127.0.0.1:8765, данные в ~/.gestor
python3 -m gestor --data ~/gestor-data --port 8800
python3 -m unittest tests.test_tax -v  # движок против примеров из kb/
```

- `gestor/tax.py` — движок: 303, 349, 347, 390, 130, 100, 151, 202, 111, 115, 200, RETA, календарь, предупреждения.
- `gestor/web.py` — интерфейс (серверный HTML, без фреймворков и сборки), `gestor/db.py` — SQLite, по файлу на профиль.
- [`kb/ru/`](kb/ru/) — база знаний с источниками (BOE, AEAT, TGSS), проверена на 08.10.2026: [IVA и счета](kb/ru/iva-facturacion.md), [IRPF autónomo](kb/ru/irpf-autonomo.md), [режим Beckham](kb/ru/beckham.md), [RETA](kb/ru/reta.md), [Sociedad Limitada](kb/ru/sociedad-limitada.md), [визы и резидентство](kb/ru/visados.md), [календарь подач](kb/ru/calendario-presentacion.md). Оригиналы — на испанском в [`kb/`](kb/), с дословными цитатами закона; источник истины — они. Английский: [`kb/en/`](kb/en/).
- `gestor/sources/*.json` — источники права: цитата из BOE/AEAT/DGT на испанском, перевод на русский и английский, что это значит, статус (прямо в тексте / толкование / спорно), практика. В интерфейсе — значок § у каждой суммы, объяснение с законом под каждым полем ввода, «Профиль» с выводами gestor о вашей ситуации и страница «Справочник». `python3 -m unittest tests.test_sources` проверяет, что каждый § ведёт к полной записи.
- [`docs/ru/use-cases.md`](docs/ru/use-cases.md) — что сервис делает и чего не делает.
- [`docs/ru/onboarding.md`](docs/ru/onboarding.md) — канонический порядок онбординга: какие документы загрузить, что спросить, что уточнить.
- [`docs/ru/explainer.html`](docs/ru/explainer.html) — как устроен gestor на вымышленном профиле: части, путь одного счёта, разобранный квартал. Откройте в браузере после клонирования.
- [`docs/glosario-aeat.md`](docs/glosario-aeat.md) — термины AEAT, которые использует gestor, со ссылкой на страницу AEAT (на испанском).

Бэкап — скопировать папку данных (`*.db` и `receipts/`). Счёт в PDF — «Печать / PDF» в браузере.
Цифры — расчёт по введённым данным; подаёте вы сами в Sede AEAT.

## Помощь в Sede из Claude Code или Codex

`gestor/mcp.py` — MCP-сервер по stdio для всех профилей в папке данных (`profiles`, `profile_create`, аргумент `profile` у каждого инструмента). Читает: анкету (`profile`), клиентов, счета и расходы (`books`), декларации года со сроком и статусом (`declarations`), одну декларацию в формате Sede с заметками § и файлом для «Importar» в `<data>/sede/<профиль>/` (`declaration`). Пишет после вашего явного «да»: анкету (`profile_update`), клиентов (`client_save`), расходы (`expense_save`, `expense_delete`), черновики счетов (`invoice_draft_save`, `invoice_draft_delete`) и отметки о подаче (`filing_mark`, `filing_unmark`). Счёт не выставляет: номер присваивается в интерфейсе. Промпт `start`: первая сессия или ближайший срок. Пока в анкете нет имени, NIE/NIF и даты начала деятельности, `declarations` отдаёт только будущие сроки, без сумм, а агент ведёт вас по [онбордингу](docs/onboarding.md). Подписка — ваша, в вашей программе; gestor ключей не хранит.

```bash
claude mcp add -s user gestor -e PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
codex mcp add gestor --env PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
claude --chrome   # Claude in Chrome: агент работает в вашем Chrome, где вы вошли в Sede
```

Агент открывает форму, загружает файл или вписывает casillas, жмёт «Validar» и сверяет экран с gestor. «Presentar» и «Firmar y enviar» он не нажимает: это правило в `INSTRUCTIONS`, подписываете вы.
