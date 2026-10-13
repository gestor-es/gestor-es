[English](README.md) | [Русский](README.ru.md) | Español

# gestor

Un gestor local para autónomos y SL en España: facturas, gastos, IVA/IRPF/Beckham/SL, RETA y calendario de presentaciones. Un solo usuario, en local, sin dependencias (Python 3.12+, stdlib). Calcula sus declaraciones y explica cada importe con la norma; la presentación la hace usted.

Todo está en inglés, ruso y español: la interfaz, las fichas de fuentes jurídicas, la base de conocimiento y la documentación. Puede cambiar el idioma de la interfaz en el menú del perfil o en «Cuestionario». El idioma se guarda en cada perfil. El servidor MCP responde en el mismo idioma.

```bash
python3 -m gestor                      # http://127.0.0.1:8765, datos en ~/.gestor
python3 -m gestor --data ~/gestor-data --port 8800
python3 -m unittest tests.test_tax -v  # el motor frente a los ejemplos de kb/
```

- `gestor/tax.py` — motor: 303, 349, 347, 390, 130, 100, 151, 202, 111, 115, 200, RETA, calendario, avisos.
- `gestor/web.py` — interfaz (HTML generado en el servidor, sin frameworks ni compilación), `gestor/db.py` — SQLite, un archivo por perfil.
- [`kb/es/`](kb/es/) — base de conocimiento con fuentes (BOE, AEAT, TGSS), revisada a 08.10.2026: [IVA y facturación](kb/es/iva-facturacion.md), [IRPF de autónomos](kb/es/irpf-autonomo.md), [régimen Beckham](kb/es/beckham.md), [RETA](kb/es/reta.md), [Sociedad Limitada](kb/es/sociedad-limitada.md), [visados y residencia](kb/es/visados.md), [calendario de presentaciones](kb/es/calendario-presentacion.md). En inglés: [`kb/en/`](kb/en/). Los originales rusos de `kb/` son la fuente de verdad.
- `gestor/sources/*.json` — fuentes jurídicas: cita original del BOE/AEAT/DGT en español, traducción, qué significa, estado (literal en el texto / interpretación / discutido), práctica. En la interfaz: el signo § en cada importe, una explicación con la norma bajo cada campo, «Perfil» con las conclusiones de gestor sobre su situación y la página «Fuentes». `python3 -m unittest tests.test_sources` comprueba que cada § lleva a una entrada completa.
- [`docs/es/use-cases.md`](docs/es/use-cases.md) — qué hace el servicio y qué no hace.
- [`docs/es/onboarding.md`](docs/es/onboarding.md) — el orden canónico de alta en gestor: qué documentos subir, qué preguntar, qué aclarar.
- [`docs/es/explainer.html`](docs/es/explainer.html) — cómo funciona gestor, con un perfil ficticio: sus partes, el recorrido de una factura y un trimestre calculado. Ábralo en el navegador después de clonar.

Copia de seguridad: copie la carpeta de datos (`*.db` y `receipts/`). Factura en PDF: «Imprimir / PDF» en el navegador.
Las cifras son un cálculo con los datos que usted introduce. La presentación la hace usted en la Sede de la AEAT.

## Ayuda en la Sede desde Claude Code o Codex

`gestor/mcp.py` es un servidor MCP por stdio, solo de lectura. Herramientas: `declarations` (declaraciones del año con plazo y estado) y `declaration` (casillas de una declaración en formato Sede, notas con §, enlace a la Sede y archivo para «Importar» en `<data>/sede/<perfil>/`). La suscripción es suya, en su propio programa. gestor no guarda claves.

```bash
claude mcp add -s user gestor -e PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
codex mcp add gestor --env PYTHONPATH=$PWD -- python3 -m gestor.mcp --entity main
claude --chrome   # Claude in Chrome: el agente trabaja en su Chrome, donde usted ha iniciado sesión en la Sede
```

El agente abre el formulario, carga el archivo o escribe las casillas, pulsa «Validar» y compara la pantalla con gestor. No pulsa «Presentar» ni «Firmar y enviar»: esta regla está en `INSTRUCTIONS`. Firma usted.
