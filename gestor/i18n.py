"""Interface language. Source strings are Russian; gestor/locale/{en,es}/*.json map them to English and Spanish.

    _("Срок {d}").format(d=…)   translate now, in the request's language
    N_("Обзор")                 mark a module-level constant; translate it with _() where it is shown

Placeholders {name} and citations [[ids]] stay as they are in every translation (tests/test_i18n.py checks it).
A missing translation falls back to Russian, and the test fails, so it never ships."""
import json
from contextvars import ContextVar
from pathlib import Path

LANGS = {"en": "English", "ru": "Русский", "es": "Español"}
DEFAULT = "en"
DIR = Path(__file__).parent / "locale"
CATALOG = {lang: {k: v for p in sorted((DIR / lang).glob("*.json")) for k, v in json.loads(p.read_text()).items()}
           for lang in LANGS if lang != "ru"}
current = ContextVar("lang", default="ru")


def _(text: str) -> str:
    lang = current.get()
    return text if lang == "ru" else CATALOG[lang].get(text, text)


def N_(text: str) -> str:
    return text


def pick(saved: str, accept_language: str = "") -> str:
    """Profile setting first, then the browser's Accept-Language, then English."""
    if saved in LANGS:
        return saved
    for part in accept_language.split(","):
        code = part.split(";")[0].strip()[:2].lower()
        if code in LANGS:
            return code
    return DEFAULT


def src(entry: dict, key: str) -> str:
    """A legal source's text in the current language: title, summary, quote (translation of quote_es) or status_note.
    Spanish readers get no translated quote: quote_es is the original."""
    lang = current.get()
    if key == "quote" and lang == "es":
        return ""
    ru = entry.get("status_note" if key == "status_note" else f"{key}_ru", "")
    return ru if lang == "ru" else entry.get(f"{key}_{lang}") or ru
