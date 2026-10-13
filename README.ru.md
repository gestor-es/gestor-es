[English](README.md) | Русский | [Español](README.es.md)

# gestor

Локальный gestor для autónomo и SL в Испании: счета, расходы, IVA/IRPF/Beckham/SL, RETA и календарь подач. Один пользователь, локально, без зависимостей (Python 3.12+, stdlib). Считает декларации и объясняет каждую сумму законом; подаёте вы сами.

Всё на английском, русском и испанском: интерфейс, карточки источников права, база знаний и документация. Язык интерфейса переключается в меню профиля или в «Анкете» и хранится в профиле. MCP-сервер отвечает на том же языке.

```bash
python3 -m gestor                      # http://127.0.0.1:8765, данные в ~/.gestor
python3 -m gestor --data ~/gestor-data --port 8800
python3 -m unittest tests.test_tax -v  # движок против примеров из kb/
```

- `gestor/tax.py` — движок: 303, 349, 347, 390, 130, 100, 151, 202, 111, 115, 200, RETA, календарь, предупреждения.
- `gestor/web.py` — интерфейс (серверный HTML, без фреймворков и сборки), `gestor/db.py` — SQLite, по файлу на профиль.
- `kb/` — база знаний с источниками (BOE, AEAT, TGSS), проверена на 08.10.2026: [IVA и счета](kb/iva-facturacion.md), [IRPF autónomo](kb/irpf-autonomo.md), [режим Beckham](kb/beckham.md), [RETA](kb/reta.md), [Sociedad Limitada](kb/sociedad-limitada.md), [визы и резидентство](kb/visados.md), [календарь подач](kb/calendario-presentacion.md). Переводы: [`kb/en/`](kb/en/), [`kb/es/`](kb/es/). Русский оригинал — источник истины.
- `gestor/sources/*.json` — источники права: цитата из BOE/AEAT/DGT на испанском, перевод на русский и английский, что это значит, статус (прямо в тексте / толкование / спорно), практика. В интерфейсе — значок § у каждой суммы, объяснение с законом под каждым полем ввода, «Профиль» с выводами gestor о вашей ситуации и страница «Справочник». `python3 -m unittest tests.test_sources` проверяет, что каждый § ведёт к полной записи.
- [`docs/use-cases.md`](docs/use-cases.md) — что сервис делает и чего не делает.
- [`docs/onboarding.md`](docs/onboarding.md) — канонический порядок онбординга: какие документы загрузить, что спросить, что уточнить.
- [`docs/explainer.html`](docs/explainer.html) — как устроен gestor на вымышленном профиле: части, путь одного счёта, разобранный квартал. Откройте в браузере после клонирования.

Бэкап — скопировать папку данных (`*.db` и `receipts/`). Счёт в PDF — «Печать / PDF» в браузере.
Цифры — расчёт по введённым данным; подаёте вы сами в Sede AEAT.

## Помощь в Sede из Claude Code или Codex

`gestor/mcp.py` — MCP-сервер по stdio, только чтение. Инструменты: `declarations` (декларации года со сроком и статусом) и `declaration` (casillas одной декларации в формате Sede, заметки с §, ссылка на Sede и файл для «Importar» в `<data>/sede/<профиль>/`). Подписка — ваша, в вашей программе; gestor ключей не хранит.

```bash
claude mcp add -s user gestor -e PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
codex mcp add gestor --env PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
claude --chrome   # Claude in Chrome: агент работает в вашем Chrome, где вы вошли в Sede
```

Агент открывает форму, загружает файл или вписывает casillas, жмёт «Validar» и сверяет экран с gestor. «Presentar» и «Firmar y enviar» он не нажимает: это правило в `INSTRUCTIONS`, подписываете вы.
