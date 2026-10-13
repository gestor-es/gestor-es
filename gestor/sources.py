"""Legal sources registry: gestor/sources/*.json (id → entry). Every rule shown in the UI cites ids from here."""
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from . import i18n
from .i18n import N_

DIR = Path(__file__).parent / "sources"
DOMAINS = {"iva": N_("IVA и счета"), "irpf": "IRPF autónomo", "beckham": N_("Режим Beckham"), "reta": "RETA",
           "sl": "Sociedad Limitada", "proc": N_("Сроки, штрафы, Verifactu"), "visas": N_("Виза и резидентство")}
STATUS = {"verified": N_("прямо в источнике"), "interpretation": N_("толкование gestor"), "disputed": N_("спорно")}
KINDS = {"law": N_("закон"), "regulation": N_("регламент или приказ"), "eu": N_("право ЕС"), "aeat": N_("разъяснение AEAT"),
         "tgss": N_("разъяснение TGSS"), "practice": N_("практика")}


def _no_dup_keys(pairs):
    keys = [k for k, _ in pairs]
    dup = {k for k in keys if keys.count(k) > 1}
    if dup:
        raise ValueError(f"duplicate keys {sorted(dup)}")
    return dict(pairs)


def load(folder: Path = DIR) -> dict:
    out = {}
    for path in sorted(folder.glob("*.json")):
        try:
            entries = json.loads(path.read_text(), object_pairs_hook=_no_dup_keys)
        except ValueError as err:
            raise ValueError(f"{path.name}: {err}") from err
        for sid, entry in entries.items():
            if sid in out:
                raise ValueError(f"{path.name}: id {sid} already defined in {out[sid]['domain']}.json")
            out[sid] = dict(entry, id=sid, domain=path.stem)
    return out


SOURCES = load()


def for_year(ids, year: int) -> list:
    """Drop sources whose valid_from/valid_to do not overlap `year` (e.g. the 2025 RETA order in a 2026 form)."""
    def ok(e):
        return not e or (e.get("valid_from", "0000") <= f"{year}-12-31" and e.get("valid_to", "9999") >= f"{year}-01-01")
    return [i for i in ids if ok(SOURCES.get(i))]


SOURCES = load()


def auto_tr(url: str) -> str:
    """Google's translate proxy for the same page (es → interface language), keeping the article anchor; none for Spanish."""
    lang = i18n.current.get()
    if not url or lang == "es":
        return ""
    u = urlsplit(url)
    host = u.netloc.replace("-", "--").replace(".", "-") + ".translate.goog"
    query = (u.query + "&" if u.query else "") + f"_x_tr_sl=es&_x_tr_tl={lang}&_x_tr_hl={lang}"
    return urlunsplit(("https", host, u.path, query, u.fragment))


CITE_RE = re.compile(r"\s*\[\[([a-z0-9,\- ]+)\]\]")


def split_cites(text: str) -> tuple[str, list]:
    """'Текст [[liva-69,liva-84]]' → ('Текст', ['liva-69', 'liva-84'])."""
    ids = [i.strip() for m in CITE_RE.finditer(text) for i in m.group(1).split(",") if i.strip()]
    return CITE_RE.sub("", text), ids


def get(sid: str) -> dict | None:
    return SOURCES.get(sid)
