"""WSGI app: invoices, expenses, clients, taxes, settings. Server-rendered HTML, no frameworks."""
import csv
import io
import json
import re
import mimetypes
import secrets
import urllib.request
from datetime import date
from email.parser import BytesParser
from email.policy import default as email_policy
from html import escape
from http.cookies import SimpleCookie
from pathlib import Path
from urllib.parse import parse_qs, quote

from . import core, db, i18n, rules, sources, tax
from . import sede as sede_file
from .core import fmt, fmt_num, invoice_number, parse_money
from .i18n import _, N_

STATIC = Path(__file__).parent / "static"
MAX_BODY = 20 * 2**20  # bytes per request: receipts are photos and PDFs
LOOPBACK = {"", "127.0.0.1", "localhost", "[::1]"}  # Host header values gestor answers to ("" = no header, e.g. tests)
INLINE_TYPES = {"application/pdf", "image/png", "image/jpeg", "image/gif", "image/webp"}  # receipts that cannot run scripts
VAT_RATES = {0, 4, 10, 21}


class Redirect(Exception):
    def __init__(self, to, entity=None):
        self.to, self.entity = to, entity


class NotFound(Exception):
    pass


def h(x) -> str:
    return escape("" if x is None else str(x))


class Request:
    def __init__(self, environ, data_dir: Path):
        self.method = environ["REQUEST_METHOD"]
        self.path = environ.get("PATH_INFO") or "/"
        self.query = {k: v[0] for k, v in parse_qs(environ.get("QUERY_STRING", "")).items()}
        self.form, self.files = {}, {}
        if self.method == "POST":
            size = int(environ.get("CONTENT_LENGTH") or 0)
            if size > MAX_BODY:
                raise ValueError(_("запрос больше {mb} МБ: загрузите файл поменьше").format(mb=MAX_BODY // 2**20))
            body = environ["wsgi.input"].read(size)
            ctype = environ.get("CONTENT_TYPE", "")
            if ctype.startswith("multipart/form-data"):
                msg = BytesParser(policy=email_policy).parsebytes(b"Content-Type: " + ctype.encode() + b"\r\n\r\n" + body)
                for part in msg.iter_parts():
                    name = part.get_param("name", header="content-disposition")
                    if part.get_filename():
                        self.files[name] = (part.get_filename(), part.get_payload(decode=True))
                    else:
                        self.form[name] = part.get_payload(decode=True).decode().strip()
            else:
                self.form = {k: v[0].strip() for k, v in parse_qs(body.decode(), keep_blank_values=True).items()}
        cookie = SimpleCookie(environ.get("HTTP_COOKIE", ""))
        entities = sorted(p.stem for p in data_dir.glob("*.db"))
        wanted = cookie["entity"].value if "entity" in cookie else ""
        self.entity = wanted if wanted in entities else ("main" if "main" in entities else entities[0] if entities else "main")
        self.entities = entities or ["main"]
        self.data_dir = data_dir
        self.con = db.connect(data_dir / f"{self.entity}.db")
        self.s = db.get_settings(self.con)
        self.lang = i18n.pick(self.s["lang"], environ.get("HTTP_ACCEPT_LANGUAGE", ""))

    def year(self) -> int:
        return int(self.query.get("year") or date.today().year)


# ---------- layout ----------

NAV = [("/", N_("Обзор")), ("/taxes", N_("Налоги")), ("/invoices", N_("Счета")), ("/expenses", N_("Расходы")), ("/clients", N_("Клиенты"))]


def profile_line(s: dict, entity: str) -> tuple[str, str]:
    """(who, what) for the profile menu: the person's name and their regime and region; the db name if the form is empty."""
    y = date.today().year
    if not s["name"] and not s["tax_id"]:
        return entity, _("анкета не заполнена")
    region = _(rules.REGIONS.get(tax.region_for_year(s, y) or "", ""))
    return s["name"] or entity, ", ".join(x for x in (_(tax.regime_label(s, y)), region) if x)


# ---------- legal sources ----------

def badge(e: dict) -> str:
    status = e.get("status", "")
    return f'<span class="stamp {h(status)}">{h(_(sources.STATUS.get(status, status)))}</span>'


SENTENCE_END = re.compile(r"[.!?]\s+(?=[А-ЯЁA-Z«])")  # i18n: ignore
ABBREV = {"см", "ст", "art", "arts", "п", "т", "ч", "напр", "г", "гг", "e", "ss", "núm", "apdo"}  # i18n: ignore


def first_sentence(text: str) -> str:
    """First sentence of a summary, not fooled by «см. DT», «ст. 93», «art. 5»."""
    for m in SENTENCE_END.finditer(text):
        word = re.findall(r"[\wáéíóúñ]+$", text[:m.start()])
        if not (word and word[0].lower() in ABBREV):
            return text[:m.start() + 1]
    return text


def explain(text: str, ids=()) -> str:
    """Next to an input: what it means for you, then every rule it rests on — gist, Справочник entry, original text."""
    items = []
    for sid in dict.fromkeys(ids):
        e = sources.get(sid)
        if not e:
            items.append(f'<li class="cite missing">§ {h(sid)}: {_("источник не найден")}</li>')
            continue
        flag = badge(e) if e.get("status") != "verified" else ""
        items.append(f'<li><a href="/sources#{h(sid)}">§ {h(e.get("ref", sid))}</a>{flag} — {h(first_sentence(i18n.src(e, "summary")))} '
                     f'<a href="{h(e.get("url", ""))}" target=_blank rel=noopener>{_("оригинал")}</a></li>')
    body = f"<p>{text}</p>" if text else ""
    return f'<div class=explain>{body}{"<ul>" + "".join(items) + "</ul>" if items else ""}</div>'


def switch_explain(name: str, value: str, current: str, text: str, ids) -> str:
    """explain() for one option of a <select name=…>; only the chosen option's block is visible (page script toggles it)."""
    return explain(h(text), ids).replace("<div class=explain>", f'<div class=explain data-for="{h(name)}" data-value="{h(value)}"'
                                         f'{"" if str(value) == str(current) else " hidden"}>', 1)


VAT_KIND_TEXT = {
    "domestic": N_("IVA из чека испанского поставщика вычитается в 303, если factura выписана на ваш NIF."),
    "reverse_eu": N_("Поставщик из ЕС без IVA: вы сами начисляете 21 % и тут же вычитаете (303, casillas 10/11 и 36/37). Покупка попадает в 349."),
    "reverse_non_eu": N_("Поставщик вне ЕС без IVA: то же самоначисление в 303 (casillas 12/13 и 28/29), в 349 не попадает."),
    "none": N_("Без IVA: банк, страховка, налоги, RETA. В 303 не попадает."),
}


def source_body(e: dict) -> str:
    """Full card: meaning → status and why → reference → Spanish original → translation → practice → links."""
    url = e.get("url", "")
    links = [f'<a href="{h(url)}" target=_blank rel=noopener>{_("Оригинал")}</a>' if url else "",
             f'<a href="{h(sources.auto_tr(url))}" target=_blank rel=noopener>{_("Автоперевод страницы")}</a>' if url and sources.auto_tr(url) else "",
             f'<a href="{h(e["mirror_url"])}" target=_blank rel=noopener>{_("Полный текст (зеркало)")}</a>' if e.get("mirror_url") else ""]
    practice = "".join(  # each item keeps its own status: a verified card must not lend certainty to an interpretation
        f'<li><a href="/sources#{h(p["id"])}">{h(p["ref"])}</a> {badge(p)} — {h(i18n.src(p, "summary"))}'
        f'{f" <i>{h(i18n.src(p, "status_note"))}</i>" if p.get("status") != "verified" and p.get("status_note") else ""}</li>'
        for p in (sources.get(pid) for pid in e.get("practice", [])) if p)
    valid = (_("Применяется с {start} по {end}.").format(start=h(e.get("valid_from", "…")), end=h(e.get("valid_to", _("сейчас")))) + " "
             if e.get("valid_from") or e.get("valid_to") else "")
    summary, quote_tr = i18n.src(e, "summary"), i18n.src(e, "quote")
    return f"""{f'<p class=meaning>{h(summary)}</p>' if summary else ''}
<p class=status-note>{badge(e)} {h(i18n.src(e, 'status_note'))}</p>
<p class=src-head><b>{h(e.get('ref', e['id']))}</b>, {h(_(sources.KINDS.get(e.get('kind'), e.get('kind', ''))))}: {h(i18n.src(e, 'title'))}</p>
{f'<blockquote lang=es>{h(e["quote_es"])}</blockquote>' if e.get('quote_es') else ''}
{f'<blockquote lang={i18n.current.get()} class=tr>{h(quote_tr)}<small>{_("Перевод gestor, не официальный.")}</small></blockquote>' if quote_tr else ''}
{f'<p class=small>{_("Практика и разъяснения:")}</p><ul class=practice>{practice}</ul>' if practice else ''}
<p class="small links">{' '.join(l for l in links if l)}</p>
<p class=small>{valid}{_("Текст проверен {d}.").format(d=h(e.get('checked', '—')))}</p>"""


def and_list(xs: list[str]) -> str:
    return _("{a} и {b}").format(a=", ".join(xs[:-1]), b=xs[-1]) if len(xs) > 1 else "".join(xs)


def cite(ids) -> str:
    """Inline § chips. A chip opens the source card in a side panel (native popover), so tables keep their row height.
    Cards themselves are appended once per page by page(). Uncertainty is spelled out on the chip."""
    out = []
    for sid in dict.fromkeys(ids or []):
        e = sources.get(sid)
        if not e:
            out.append(f'<span class="cite missing">§ {h(sid)}: {_("источник не найден")}</span>')
            continue
        status = e.get("status", "")
        flag = f" — {_(sources.STATUS[status])}" if status in ("interpretation", "disputed") else ""
        out.append(f'<button type=button class="cite {h(status)}" popovertarget="src-{h(sid)}">§ {h(e.get("ref", sid))}{h(flag)}</button>')
    return f'<div class=cites>{"".join(out)}</div>' if out else ""


def source_panels(body: str) -> str:
    """One side-panel card per source cited on the page."""
    return "".join(
        f"""<aside popover id="src-{h(sid)}" class=src-panel aria-label="{_("Источник")}">
<button type=button class=close popovertarget="src-{h(sid)}" popovertargetaction=hide>{_("Закрыть")}</button>
{source_body(sources.get(sid))}<p class=small><a href="/sources#{h(sid)}">{_("Открыть в справочнике")}</a></p></aside>"""
        for sid in dict.fromkeys(re.findall(r'popovertarget="src-([a-z0-9-]+)"', body)) if sources.get(sid))


def cited(text: str) -> str:
    """Engine text with trailing [[ids]] → escaped text + chips."""
    plain, ids = sources.split_cites(text)
    return h(plain) + " " + cite(ids)


def page(req, title, body, index=None) -> str:
    here = lambda u: (u == "/" and req.path == "/") or (u != "/" and req.path.startswith(u))
    nav = "".join(f'<a href="{u}"{" aria-current=page" if here(u) else ""}>{_(t)}</a>' for u, t in NAV)
    others = []
    for e in req.entities:
        if e == req.entity:
            who, what = profile_line(req.s, e)
            others.append(f'<span class=on>{h(who)}<small>{h(what)}</small></span>')
        else:
            con = db.connect(req.data_dir / f"{e}.db")
            who, what = profile_line(db.get_settings(con), e)
            con.close()
            others.append(f'<button name=entity value="{h(e)}">{h(who)}<small>{h(what)}</small></button>')
    me = h(req.s["name"] or req.entity) + (f' <small>{h(req.s["tax_id"])}</small>' if req.s["tax_id"] else "")
    header = f"""<header class=appbar><a class=brand href="/">gestor</a><nav aria-label="{_("Разделы")}">{nav}</nav>
<a class=ref href="/sources"{" aria-current=page" if here("/sources") else ""}>{_("Справочник")}</a>
<details class=me><summary>{me}</summary><div class=menu>
<a href="/settings">{_("Анкета и «как gestor вас понял»")}</a><div class=label>{_("Профили")}</div>
<form method=post action="/entities/use">{"".join(others)}</form><a class=add href="/entities">+ {_("Новый профиль")}</a>
<form method=post action="/lang" class=langs><input type=hidden name=back value="{h(req.path)}">{"".join(
    f'<button name=lang value={k}{" aria-current=true" if k == req.lang else ""}>{k.upper()}</button>' for k in i18n.LANGS)}</form>
</div></details></header>"""
    return ru_dates(f"""<!doctype html><html lang={req.lang}><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>{h(title)} · gestor</title>
<link rel=stylesheet href="/static/fonts.css">
<link rel=stylesheet href="/static/style.css">
<div class=layout>{header}<aside class=toc-col>{toc(req, body, index)}</aside><main>{body}</main></div>{source_panels(body)}
<footer class=colophon aria-hidden=true><div class=giant>gestor</div><img src="/static/papel-sellado.jpg" alt=""></footer>
<script>document.addEventListener('change', e => document.querySelectorAll(`[data-for="${{e.target.name}}"]`)
  .forEach(d => d.hidden = d.dataset.value !== e.target.value));
const tocLinks = [...document.querySelectorAll('.toc a[href^="#"]')];
const tocSeen = new IntersectionObserver(es => es.forEach(e => e.isIntersecting &&
  tocLinks.forEach(a => a.classList.toggle('on', a.hash === '#' + e.target.id))), {{ rootMargin: '0px 0px -70% 0px' }});
tocLinks.forEach(a => {{ const t = document.getElementById(a.hash.slice(1)); if (t) tocSeen.observe(t); }});
document.addEventListener('click', e => document.querySelectorAll('details.me[open]')
  .forEach(d => d.contains(e.target) || d.removeAttribute('open')));</script></html>""")


ISO_DATE = re.compile(r"(?<![\d-])(\d{4})-(\d{2})-(\d{2})(?![\d-])")
TEXTAREA = re.compile(r"(<textarea.*?</textarea>)", re.S)


def ru_dates(html: str) -> str:
    """Every date a person reads is dd.mm.yyyy. Data stays ISO: attributes (date inputs, links) and <textarea> are untouched."""
    return "".join(part if part.startswith("<textarea") else
                   re.sub(r">[^<]+<", lambda m: ISO_DATE.sub(r"\3.\2.\1", m.group()), part)
                   for part in TEXTAREA.split(html))


def dm(iso: str) -> str:
    return f"{iso[8:10]}.{iso[5:7]}"


HEADING_RE = re.compile(r'<h2 id="?([\w-]+)"?>(.*?)</h2>|<div class=band id="?([\w-]+)"?>(.*?)</div>', re.S)
YEARLY = ("/", "/taxes", "/invoices", "/expenses")


def toc(req, body: str, index=None) -> str:
    """Left index like the contents of a book: section, dot leader, its deadline as the «page number»,
    modelos underneath (overdue in red). Pages may pass `index`; otherwise the page's own headings are used.
    index item: (anchor, title, due 'dd.mm' or '', [(anchor, modelo, overdue), …])."""
    if index is None:
        index = [((m.group(1) or m.group(3)), re.sub(r"<[^>]+>", "", m.group(2) or m.group(4)), "", [])
                 for m in HEADING_RE.finditer(body)]  # heading text is already escaped HTML
    else:
        index = [(a, h(t), due, forms) for a, t, due, forms in index]
    years = ""
    if req.path in YEARLY:
        y = req.year()
        years = (f'<div class=toc-year><a href="{req.path}?year={y - 1}" aria-label="{y - 1}">‹</a><b>{y}</b>'
                 f'<a href="{req.path}?year={y + 1}" aria-label="{y + 1}">›</a></div>')
    if not index and not years:
        return ""
    lis = "".join(
        f'<li><a class=entry href="#{h(a)}">{t}<span>{h(due)}</span></a>'
        + (f'<div class=toc-forms>{" ".join(f"<a href=#{h(fa)}{" class=late" if late else ""}>{h(fm)}</a>" for fa, fm, late in forms)}</div>'
           if forms else "") + "</li>" for a, t, due, forms in index)
    return f'<nav class=toc aria-label="{_("Содержание страницы")}">{years}<ol>{lis}</ol></nav>'


def junction(word: str) -> str:
    """Oversized display word at the seam between two blocks; decoration only, the real heading stays in the markup."""
    return f'<div class=junction aria-hidden=true><span>{h(word)}</span></div>'


def table(head, rows, cls="list") -> str:
    th = "".join(f"<th>{c}</th>" for c in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr or f"<tr><td colspan=99 class=muted>{_("пусто")}</td></tr>"}</tbody></table>'


def field(label, name, value="", type="text", **kw) -> str:
    attrs = " ".join(f'{k.rstrip("_")}="{h(v)}"' for k, v in kw.items())
    return f'<label>{label}<input type={type} name={name} value="{h(value)}" {attrs}></label>'


def select(label, name, options: dict, value) -> str:
    opts = "".join(f'<option value="{h(k)}"{" selected" if str(k) == str(value) else ""}>{h(v)}</option>' for k, v in options.items())
    return f"<label>{label}<select name={name}>{opts}</select></label>"


def year_switch(req, path) -> str:
    y = req.year()
    return f'<p class=years><a href="{path}?year={y - 1}">← {y - 1}</a> <b>{y}</b> <a href="{path}?year={y + 1}">{y + 1} →</a></p>'


def onboarding_hint(req) -> str:
    if req.s["name"] and req.s["tax_id"]:
        return ""
    return '<div class=warn>' + _('Заполните <a href="/settings">профиль</a>: имя, NIE/NIF, режим и регион. Без него расчёты неполные.') + '</div>'


# ---------- dashboard ----------

PAYS = {"303", "130", "111", "115", "202", "100", "151", "200"}  # returns that can end in a payment; 349/390/347 only inform
QUARTERLY = ["303", "130", "349", "111", "115"]
MATRIX_NAMES = {"303": "IVA", "130": "IRPF", "349": N_("ЕС"), "111": N_("удержания"), "115": N_("аренда")}


def has_books(req, y) -> bool:
    return bool(tax.sales(req.con, y) or tax.purchases(req.con, y))


def stamp(f, filed, today, books=True, brief=False) -> str:
    """Office stamp for one return: PRESENTADO / FUERA DE PLAZO / PENDIENTE (window open), or just the deadline.
    Without any invoices or expenses that year gestor cannot know you missed it, so no red stamp.
    brief: stamp only — the overview matrix shows the quarter's deadline once, in the row head."""
    done = filed.get((f["modelo"], f["period"]))
    note = (lambda text: "") if brief else (lambda text: f"<small>{text}</small>")
    if done:
        return f'<span class="stamp ok">PRESENTADO</span>{note(h(done["filed_on"]))}'
    if f["deadline"] < today:
        if not books:
            return f'<small>{_("счетов за этот год в gestor нет")}</small>' if brief else \
                f'<small>{_("срок был {d}; счетов за этот год в gestor нет").format(d=h(f["deadline"]))}</small>'
        return f'<span class="stamp late">FUERA DE PLAZO</span>{note(_("срок был {d}").format(d=h(f["deadline"])))}'
    if f["opens"] <= today:
        return f'<span class="stamp wait">PENDIENTE</span>{note(_("до {d}").format(d=h(f["deadline"])))}'
    return (f'<small>{_("до {d}").format(d=h(f["deadline"]))}</small>' if brief else
            f'<small>{_("с {opens} до {d}").format(opens=h(f["opens"]), d=h(f["deadline"]))}</small>')


def mismatch(f, done) -> bool:
    """Filed amount differs from what gestor computes now (e.g. invoices added after filing)."""
    return bool(done) and f["modelo"] in PAYS and done["amount_cents"] is not None and done["amount_cents"] != f["result"]


def filings(req, y) -> dict:
    return {(r["modelo"], r["period"]): r for r in req.con.execute("SELECT * FROM filings WHERE year = ?", (y,))}


def profile_ready(s) -> bool:
    return bool(s["name"] and s["tax_id"] and (s["kind"] == "sl" or s["activity_start"] or s["reta_start"]))


def payment_slip(req, today) -> str:
    """Open filing windows (this year's or last year's 4T/annual) as a payment slip; overdue returns above it."""
    if not profile_ready(req.s):
        return (f'<div class=slip><div><span class=label>{_("Недостаточно данных, чтобы сказать, что подавать.")}</span></div>'
                f'<a class="btn primary" href="/settings">{_("Заполнить профиль")}</a></div>')
    cy = int(today[:4])
    pending, late, reminders = [], [], []
    for fy in (cy - 1, cy):
        if not has_books(req, fy):  # no books that year in gestor → nothing to claim
            continue
        done = filings(req, fy)
        for q, (_title, g) in enumerate(tax.forms(req.con, req.s, fy), 1):
            for f in g:
                if f["modelo"] == "RETA" or (f["modelo"], f["period"]) in done or today < f["opens"]:
                    continue
                (pending if today <= f["deadline"] else late).append((f, q))
        reminders += [d for d in tax.calendar(req.con, req.s, fy)
                      if d["modelo"] in ("190", "180", "720", "Libros", "Cuentas") and d["opens"] <= today <= d["deadline"]]
    overdue = (f"""<div class=warn><b>{_("Просрочено:")}</b> {', '.join(f'<a href="/taxes?year={f["year"]}#q{q}">{_("{modelo} за {period} {year}").format(modelo=h(f["modelo"]), period=h(f["period"]), year=f["year"])}</a>'
                                                         for f, q in late)}. {_("Подайте как можно скорее: пока AEAT не прислала требование,\nдоплата меньше.")} {cite(['lgt-27', 'lgt-198'])}</div>""" if late else "")
    remind = "".join("<li>" + _("Напоминание: {modelo} — {title}, до {d}. gestor её не считает.").format(
        modelo=h(d['modelo']), title=h(d['title']), d=h(d['deadline'])) + "</li>" for d in reminders)
    if not pending:
        return overdue + (f'<div class=slip><div><span class=label>{_("Открытых сроков сейчас нет.")}</span><span class=amount>{fmt(0)}</span></div>'
                          f'{"<ul class=rest>" + remind + "</ul>" if remind else ""}</div>')
    pending.sort(key=lambda p: p[0]["deadline"])
    due = [p for p in pending if p[0]["deadline"] == pending[0][0]["deadline"]]
    d0, fy, q = due[0][0]["deadline"], due[0][0]["year"], due[0][1]
    pay = sum(max(f["result"], 0) for f, _q in due if f["modelo"] in PAYS)
    days = (date.fromisoformat(d0) - date.fromisoformat(today)).days
    rest = "".join(f"<li>{_('{modelo} за {period} {year}').format(modelo=h(f['modelo']), period=h(f['period']), year=f['year'])}: "
                   f"{h(f.get('result_label', _('результат'))).lower()} {fmt(f['result'])}"
                   f"{'' if f['modelo'] in PAYS else ' ' + _('(сведения, без оплаты)')}</li>" for f, _q in due)
    by_period = {}
    for f, _q in due:
        by_period.setdefault(f["period"], []).append(f["modelo"])
    ref = "; ".join(_("{modelos} за {period}").format(modelos=and_list(ms), period=p) for p, ms in by_period.items())
    label = (_("К уплате до {d}, через {days} дн.") if pay else _("Подать, платить не нужно до {d}, через {days} дн.")).format(d=h(d0), days=days)
    return overdue + f"""<div class=slip><div><span class=label>{label}</span>
<span class=amount>{fmt(pay)}</span><div class=ref>{h(ref)} {fy}</div></div>
<a class="btn primary" href="/taxes?year={fy}#q{q}">{_("Открыть расчёт")}</a><ul class=rest>{rest}{remind}</ul></div>"""


PAY_NAMES = {"210": "Modelo 210 (IRNR)", "130": "Modelo 130 (IRPF)", "303": "Modelo 303 (IVA)", "111": N_("Modelo 111 (удержания)"),
             "115": N_("Modelo 115 (аренда)"), "202": "Modelo 202 (IS)", "RETA": "RETA (TGSS)", "151": N_("Modelo 151 (за год)"),
             "100": N_("Renta, 100 (за год)"), "200": N_("Modelo 200 (IS за год)")}
PAY_INK = {"210": "ink-pen", "130": "ink-pen", "202": "ink-pen", "303": "ink-print", "111": "ink-print", "115": "ink-print",
           "RETA": "ink-stamp", "151": "ink-light", "100": "ink-light", "200": "ink-light"}  # advances / RETA / annual: one ink each


def eur0(c) -> str:
    return f"{round(c / 100):,}".replace(",", ".")


def money_cell(paid, due) -> str:
    if due < 0:
        return f'<td class="num due">{_("≈ {amount} возврат").format(amount=fmt(due).replace(" €", ""))}</td>'
    parts = ([fmt(paid).replace(" €", "")] if paid else []) + ([f"<i>≈ {fmt(due).replace(' €', '')}</i>"] if due else [])
    return f'<td class=num>{" + ".join(parts) or "—"}</td>'


def wrap_words(text: str, width: int) -> list:
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    return lines + [cur] if cur else lines


def money_svg(cols, top, year_total) -> str:
    """cols: (label, [(cents, ink, dashed, title, detail)], caption) stacked from the baseline; dashed = not paid yet.
    Hovering a block shows what it is: modelo and period, amount, its share of the quarter and of the year, and what it is
    made of. Each block k is followed (after every column, so tips paint on top) by <g class="tip t{k}">, revealed by an
    inline rule `.s{k}:hover ~ .t{k}` — no JS."""
    W, B, gap = 880, 240, 150
    yv = lambda v: (B - 30) * v / top
    out = [f'<line class=base x1=0 x2={W} y1={B} y2={B} />',
           f'<line class=sep x1="{30 + 4 * gap + 10}" x2="{30 + 4 * gap + 10}" y1="16" y2="{B + 28}" />']
    tips, rules, k = [], [], 0
    for i, (label, segs, cap) in enumerate(cols):
        x, w, y = 30 + i * gap + (40 if i == 4 else 0), 110 if i == 4 else 70, B
        col_total = sum(v for v, *_ in segs if v > 0)
        for v, ink, dashed, title, detail in segs:
            if v <= 0:
                continue
            hgt = yv(v)
            out.append(f'<rect class="seg s{k} {ink}{" fore" if dashed else ""}" tabindex=0 x="{x}" y="{y - hgt:.1f}" '
                       f'width="{w}" height="{hgt:.1f}" />')
            year_share = f"{100 * v / year_total:.0f}"
            share = (_("{q} % квартала, {y} % года").format(q=f"{100 * v / col_total:.0f}", y=year_share) if i < 4 else
                     _("{y} % года").format(y=year_share))
            lines = [(f"{'≈ ' if dashed else ''}{fmt(v)}{' — ' + _('ещё не оплачено') if dashed else ''}", "tip-v"), (share, "tip-l")]
            lines += [(t, "tip-l") for t in wrap_words(detail, 44)] if detail else []
            tw, th = 24 + 7.3 * max(len(title), *(len(t) for t, _ in lines)), 34 + 18 * len(lines)
            tx = x + w + 10 if i < len(cols) - 1 else x - tw - 10
            ty = min(max(y - hgt / 2 - th / 2, 4), B - th)
            tips.append(f'<g class="tip t{k}"><rect class=tip-bg x="{tx}" y="{ty:.1f}" width="{tw:.0f}" height="{th}" />'
                        f'<rect class="{ink}{" fore" if dashed else ""} tip-key" x="{tx + 12}" y="{ty + 11:.1f}" width="10" height="10" />'
                        f'<text class=tip-h x="{tx + 28}" y="{ty + 20:.1f}">{h(title)}</text>'
                        + "".join(f'<text class={c} x="{tx + 12}" y="{ty + 40 + 18 * n:.1f}">{h(t)}</text>' for n, (t, c) in enumerate(lines))
                        + "</g>")
            rules.append(f".s{k}:hover~.t{k},.s{k}:focus~.t{k}{{display:inline}}")
            y -= hgt
            k += 1
        out.append(f'<text class=cap x="{x + w / 2}" y="{y - 8:.1f}">{h(cap)}</text><text class=axis x="{x + w / 2}" y="{B + 22}">{h(label)}</text>')
    return (f'<svg class=money-chart viewBox="0 0 {W} {B + 34}" role=img aria-label="{_("Налоги и RETA по кварталам и за год")}">'
            f'<style>{"".join(rules)}</style>{"".join(out + tips)}</svg>')


def money_block(req, y) -> str:
    """Taxes and RETA for the year by the quarter they cover, plus the year: paid, still due, and for Beckham a range."""
    p = tax.payments(req.con, req.s, y)
    if not p["rows"] and not p["annual"]:
        return ""
    why = p["why"]
    qs = []
    for q in range(4):
        segs = ([(c[q][0], PAY_INK[m], False, f"{_(PAY_NAMES[m])}, {q + 1}T", why.get((m, q, "paid"), "")) for m, c in p["rows"].items()]
                + [(c[q][1], PAY_INK[m], True, f"{_(PAY_NAMES[m])}, {q + 1}T", why.get((m, q, "due"), "")) for m, c in p["rows"].items()])
        paid, due = sum(s[0] for s in segs if not s[2]), sum(s[0] for s in segs if s[2] and s[0] > 0)
        qs.append((f"{q + 1}T", segs, (eur0(paid) if paid else "") + (" + " if paid and due else "") + (f"≈ {eur0(due)}" if due else "")))
    lo, hi = p["paid"] + p["due"], p["paid"] + p["due_high"]
    by_q = lambda c, i: ", ".join(f"{q + 1}T {fmt(c[q][i])}" for q in range(4) if c[q][i] > 0)
    year_segs = ([(sum(x[0] for x in c), PAY_INK[m], False, _("{name}, оплачено").format(name=_(PAY_NAMES[m])), by_q(c, 0)) for m, c in p["rows"].items()]
                 + [(c[0], PAY_INK[m], False, _(PAY_NAMES[m]), why.get((m, "year", "paid"), "")) for m, c in p["annual"].items()]
                 + [(sum(max(x[1], 0) for x in c), PAY_INK[m], True, _("{name}, ещё").format(name=_(PAY_NAMES[m])), by_q(c, 1)) for m, c in p["rows"].items()]
                 + [(c[1], PAY_INK[m], True, _(PAY_NAMES[m]), why.get((m, "year", "due"), "")) for m, c in p["annual"].items()]
                 + [(hi - lo, "ink-light", True, _("Верх вилки прогноза"), why.get("high", ""))])
    total = f"{eur0(lo)} — {eur0(hi)}" if hi > lo else eur0(lo)
    chart = money_svg(qs + [(_("Год {y}").format(y=y), year_segs, total)], max(hi, 1) * 1.08, max(lo, 1))
    body = ""
    for m, cells in list(p["rows"].items()) + [(m, None) for m in p["annual"]]:
        if cells:
            yp, yd = sum(c[0] for c in cells), sum(max(c[1], 0) for c in cells)
            row = "".join(money_cell(*c) for c in cells) + money_cell(yp, yd)
        else:
            paid, due = p["annual"][m]
            span = (f'<td class=num><i>≈ {fmt(due).replace(" €", "")} — {fmt(p["high"][m]).replace(" €", "")}</i></td>'
                    if m in p["high"] else money_cell(paid, due))
            row = '<td class=num>—</td>' * 4 + span
        body += f'<tr><th><i class="chip {PAY_INK[m]}"></i>{_(PAY_NAMES[m])}</th>{row}</tr>'
    totals = "".join(f'<td class=num>{cap or "—"}</td>' for _label, _segs, cap in qs) + f'<td class=num>{total}</td>'
    rest = fmt(p["due"]) if hi == lo else f"{eur0(p['due'])}–{eur0(p['due_high'])} €"
    return f"""<div class=band id=money>{_("Налоги и RETA за {y}").format(y=y)}</div>
<p class=money-total>{total} €</p>
<p class=sub>{_("Уже заплачено {paid}, осталось {rest}. Платёж стоит в квартале, за который он сделан; ≈ и пунктир — ещё не оплачено.").format(paid=fmt(p['paid']), rest=rest)}
{_("Верх вилки — если до конца года доход пойдёт, как в среднем квартале за последний год.") if hi > lo else ""}</p>
{chart}
<table class=money><thead><tr><th></th><th class=num>1T</th><th class=num>2T</th><th class=num>3T</th><th class=num>4T</th><th class=num>{_("Год")}</th></tr></thead>
<tbody>{body}</tbody><tfoot><tr><th>{_("Итого")}</th>{totals}</tr></tfoot></table>"""


def dashboard(req):
    y, today = req.year(), date.today().isoformat()
    filed, books = filings(req, y), has_books(req, y)
    groups = tax.forms(req.con, req.s, y)
    slip = payment_slip(req, today)
    by = {(f["modelo"], int(f["period"][0])): f for _g, fl in groups[:4] for f in fl if f["modelo"] in QUARTERLY}
    mods = [m for m in QUARTERLY if any(k[0] == m for k in by)]
    rows = ""
    for q in range(1, 5):
        fs = [by[(m, q)] for m in mods if (m, q) in by]
        if not fs:
            rows += f"<tr><th scope=row>{q}T</th><td colspan={len(mods) or 1} class=later>{_('нет обязательств')}</td></tr>"
            continue
        opens, due = min(f["opens"] for f in fs), min(f["deadline"] for f in fs)
        when = f"{dm(opens)}–{dm(due)}" if today < opens else _("до {d}").format(d=dm(due)) if today <= due else _("срок {d}").format(d=dm(due))
        cells = (f"<td colspan={len(mods)} class=later>{_('окно откроется {d}').format(d=opens)}</td>" if today < opens else
                 "".join(f"<td>{stamp(by[(m, q)], filed, today, books, brief=True) if (m, q) in by else '<small>—</small>'}</td>" for m in mods))
        rows += f"<tr><th scope=row>{q}T<small>{when}</small></th>{cells}</tr>"
    other = [f for _g, fl in groups for f in fl if f["modelo"] not in QUARTERLY and f["modelo"] != "RETA"]  # 202 and annual
    extra = [d for d in tax.calendar(req.con, req.s, y) if d["period"] == "0A" and d["modelo"] not in {f["modelo"] for f in other}]
    ann = "".join(f"<tr><td>{h(f['modelo'])}</td><td>{h(f['title'])}</td><td>{stamp(f, filed, today, books, brief=True)}</td></tr>" for f in other)
    ann += "".join(f"<tr><td>{h(d['modelo'])}</td><td>{h(d['title'])}</td><td><small>{_('до {d}, напоминание').format(d=h(d['deadline']))}</small></td></tr>"
                   for d in extra)
    ann_title = _("Авансы IS и годовые") if any(f["modelo"] == "202" for f in other) else _("Годовые")
    region = _(rules.REGIONS.get(tax.region_for_year(req.s, y) or "", ""))
    regime = h(_(tax.regime_label(req.s, y))) + (", " + h(region) if region else "")
    body = f"""<h1>{_("Сводка {y}").format(y=y)}</h1><p class=sub>{_("На {date}: {regime}.").format(date=date.fromisoformat(today).strftime('%d.%m.%Y'), regime=regime)}
<a href="/settings">{_("Как gestor вас понял")}</a></p>
{onboarding_hint(req)}{year_switch(req, '/')}
{slip}
{''.join(f'<div class=warn>{cited(w)}</div>' for w in tax.warnings(req.con, req.s, y))}
{junction(str(y))}
<div class=cols><div><div class=band id=quarters>{_("Квартальные декларации {y}").format(y=y)}</div>
<table class=matrix><thead><tr><th>{_("Квартал")}</th>{''.join(f'<th>{m} <small>{_(MATRIX_NAMES[m])}</small></th>' for m in mods)}</tr></thead><tbody>{rows}</tbody></table></div>
<div><div class=band id=annual>{ann_title}</div><table class=dates><tbody>{ann}</tbody></table>
<div class=basis>{_("Сроки и что будет при опоздании:")} {cite(['aeat-calendario-2026', 'lpac-30', 'dias-inhabiles-2026', 'orden-domiciliacion', 'lgt-27', 'lgt-198'])}</div>
<p class=actions><a class="btn primary" href="/invoices/new">{_("Новый счёт")}</a> <a class=btn href="/expenses/new">{_("Новый расход")}</a></p></div></div>
{money_block(req, y)}
<footer class=foot><span>{_("gestor считает, подаёте вы сами в Sede AEAT. Все суммы — оценка по вашим книгам на сегодня.")}</span>
<span>{_("Каждая цифра ведёт к закону: значок §.")}</span></footer>"""
    return page(req, _("Обзор"), body)


# ---------- clients ----------

def client_form(c=None) -> str:
    c = c or {"name": "", "tax_id": "", "country": "ES", "is_business": 1, "address": "", "email": ""}
    return f"""{field(_('Название / имя'), 'name', c['name'], required=1)}
{field('NIF / VAT ID / Tax ID', 'tax_id', c['tax_id'])}
{explain(_('Бизнесу в Испании и в ЕС номер NIF / VAT ID обязателен на счёте. VAT ID клиента из ЕС проверьте в VIES.'), ['rd1619-6'])}
{field(_('Страна (ISO, 2 буквы)'), 'country', c['country'], maxlength=2, required=1)}
{select(_('Тип'), 'is_business', {1: _('Компания / предприниматель'), 0: _('Частное лицо')}, c['is_business'])}
{explain(_('По стране и типу клиента gestor выбирает режим IVA для счёта: Испания — 21 %, бизнес в ЕС — без IVA (reverse charge), вне ЕС — без испанского IVA.'),
         ['liva-69', 'dir2006-196', 'liva-90'])}
<label>{_('Адрес')}<textarea name=address rows=3>{h(c['address'])}</textarea></label>
{field('Email', 'email', c['email'], type='email')}"""


def client_values(f) -> tuple:
    if not f.get("name"):
        raise ValueError(_("нужно название клиента"))
    return (f["name"], f.get("tax_id", ""), (f.get("country") or "ES").upper()[:2], int(f.get("is_business", 1)),
            f.get("address", ""), f.get("email", ""))


def save_client(con, f, cid=None) -> int:
    if cid:
        con.execute("UPDATE clients SET name=?, tax_id=?, country=?, is_business=?, address=?, email=? WHERE id=?", client_values(f) + (cid,))
        return cid
    return con.execute("INSERT INTO clients(name, tax_id, country, is_business, address, email) VALUES (?,?,?,?,?,?)",
                       client_values(f)).lastrowid


def clients(req):
    if req.method == "POST":
        save_client(req.con, req.form)
        nxt = req.form.get("next") or ""
        raise Redirect(nxt if nxt.startswith("/") and not nxt.startswith("//") else "/clients")
    rows = [(f'<a href="/clients/{c["id"]}">{h(c["name"])}</a>', h(c["tax_id"]), h(c["country"]),
             _("компания") if c["is_business"] else _("частное лицо"))
            for c in req.con.execute("SELECT * FROM clients ORDER BY name")]
    body = f"""<h1>{_("Клиенты")}</h1>{table([_('Клиент'), 'ID', _('Страна'), _('Тип')], rows)}
<h2>{_("Новый клиент")}</h2><form method=post class=grid>{client_form()}<input type=hidden name=next value="{h(req.query.get('next', ''))}"><button>{_("Добавить")}</button></form>"""
    return page(req, _("Клиенты"), body)


def client_edit(req, cid):
    c = req.con.execute("SELECT * FROM clients WHERE id = ?", (cid,)).fetchone() or _404()
    if req.method == "POST":
        save_client(req.con, req.form, cid)
        raise Redirect("/clients")
    return page(req, c["name"], f"<h1>{h(c['name'])}</h1><form method=post class=grid>{client_form(c)}<button>{_('Сохранить')}</button></form>")


def _404():
    raise NotFound()


# ---------- invoices ----------

def fetch_ecb_rate(currency: str, on: str) -> float:
    """Last ECB reference rate (currency per 1 EUR) published on or before `on` (art. 79.Once LIVA allows BCE rate)."""
    url = (f"https://data-api.ecb.europa.eu/service/data/EXR/D.{quote(currency)}.EUR.SP00.A"
           f"?endPeriod={on}&lastNObservations=1&format=csvdata")
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            rows = list(csv.DictReader(io.StringIO(r.read().decode())))
        return float(rows[-1]["OBS_VALUE"])
    except (OSError, IndexError, KeyError, ValueError) as e:
        raise ValueError(_("курс ЕЦБ для {currency} недоступен ({error}) — введите курс вручную").format(currency=currency, error=e))


def invoices(req):
    y = req.year()
    rows = []
    tot = 0
    for inv in req.con.execute("""SELECT i.*, c.name AS client FROM invoices i JOIN clients c ON c.id = i.client_id
                                  WHERE substr(i.issue_date, 1, 4) = ? ORDER BY i.issue_date DESC, i.id DESC""", (str(y),)):
        a = core.invoice_amounts(req.con, inv)
        tot += a["base_eur"] if inv["number"] else 0
        status = _("черновик") if not inv["number"] else (_("оплачен {d}").format(d=inv["paid_date"]) if inv["paid_date"] else _("выставлен"))
        rows.append((inv["issue_date"], f'<a href="/invoices/{inv["id"]}">{h(invoice_number(inv))}</a>', h(inv["client"]),
                     money_in(a["total"], inv["currency"]), fmt(a["base_eur"]), status))
    body = f"""<h1>{_("Счета")}</h1>{year_switch(req, '/invoices')}
<p><a class=btn href="/invoices/new">{_("Новый счёт")}</a></p>
{table([_('Дата'), _('Номер'), _('Клиент'), _('Итого'), _('База, €'), _('Статус')], rows)}
<p class=muted>{_("База за {y} по выставленным:").format(y=y)} <b>{fmt(tot)}</b></p>"""
    return page(req, _("Счета"), body)


def invoice_form(req, inv=None, lines=()):
    cl = req.con.execute("SELECT * FROM clients ORDER BY name").fetchall()
    if not cl:
        raise Redirect("/clients?next=/invoices/new")
    inv = inv or {"client_id": cl[0]["id"], "issue_date": date.today().isoformat(), "operation_date": "",
                  "currency": "EUR", "fx_rate": "", "treatment": "", "vat_rate": "", "irpf_rate": "", "notes": ""}
    lines = list(lines) + [None] * (5 - len(lines))
    line_rows = "".join(
        f"""<div class=line><label>{_("Описание")}<input name=desc{i} value="{h(l['description'] if l else '')}"></label>
<label>{_("Кол-во")}<input name=qty{i} value="{h(l['quantity'] if l else '1')}" size=4></label>
<label>{_("Цена, {currency}").format(currency=h(inv['currency']))}<input name=price{i} value="{h(fmt_num(l['unit_price_cents']) if l else '')}" size=10></label></div>"""
        for i, l in enumerate(lines))
    treatments = {"": _("авто (по стране клиента)")} | {k: _(v["label"]) for k, v in rules.TREATMENTS.items()}
    return f"""<form method=post class=grid>
{select(_('Клиент'), 'client_id', {c['id']: f"{c['name']} ({c['country']})" for c in cl}, inv['client_id'])}
<p class=muted><a href="/clients?next={quote(req.path)}">+ {_('новый клиент')}</a></p>
{field(_('Дата счёта'), 'issue_date', inv['issue_date'], type='date', required=1)}
{field(_('Дата операции (если другая)'), 'operation_date', inv['operation_date'] or '', type='date')}
{explain(_('Счёт бизнесу выставляется не позже 15-го числа следующего месяца. Дата операции влияет на квартал IVA и курс валюты.'), ['rd1619-11', 'rd1619-6'])}
{select(_('Валюта'), 'currency', {k: f"{k} — {_(v)}" for k, v in rules.CURRENCIES.items()}, inv['currency'])}
{field(_('Курс: единиц валюты за 1 € (пусто — курс ЕЦБ)'), 'fx_rate', inv['fx_rate'] if inv['currency'] != 'EUR' else '')}
{explain(_('Счёт в валюте: база и IVA пересчитываются в евро по курсу на дату операции. gestor берёт справочный курс ЕЦБ, поэтому в списке только валюты, у которых он есть.'), ['liva-79', 'dgt-v2630-17'])}
{select(_('Режим IVA'), 'treatment', treatments, inv['treatment'])}
{field(_('IVA %, пусто — по режиму'), 'vat_rate', inv['vat_rate'])}
{explain(_('«Авто» берёт режим из карточки клиента: Испания — IVA 21 %; бизнес в ЕС — без IVA, клиент платит сам (reverse charge), счёт идёт в 349; '
           'вне ЕС — испанский IVA не начисляется. Счёт нужен в любом случае.'), ['liva-69', 'dir2006-196', 'liva-90', 'rd1619-2'])}
{field(_('Retención IRPF %, пусто — авто'), 'irpf_rate', inv['irpf_rate'])}
{explain(_('«Авто»: удержание есть, только если клиент — бизнес в Испании, а вы profesional. В общем IRPF — 15 % (7 % в первые годы), '
           'в режиме Beckham — 24 %. Иностранный клиент без представительства в Испании не удерживает.'),
         ['lirpf-101', 'rirpf-95', 'aeat-novedades-rd1008-2023', 'irpf-dgt-v2541-20'])}
<fieldset><legend>{_('Строки')}</legend>{line_rows}</fieldset>
<label>{_('Примечание на счёте')}<textarea name=notes rows=2>{h(inv['notes'])}</textarea></label>
<button>{_('Сохранить черновик')}</button></form>"""


def save_invoice(req, inv_id=None, rectifies=None):
    f = req.form
    if inv_id:  # every caller: an issued invoice keeps its lines; only a rectificativa changes it
        old = req.con.execute("SELECT number, rectifies_id FROM invoices WHERE id = ?", (inv_id,)).fetchone() or _404()
        if old["number"]:
            raise ValueError(_("выставленный счёт менять нельзя — сделайте factura rectificativa"))
        rectifies = rectifies or old["rectifies_id"]
    client = req.con.execute("SELECT * FROM clients WHERE id = ?", (int(f["client_id"]),)).fetchone() or _404()
    issue_date = core.iso_date(f["issue_date"])
    op_date = core.iso_date(f["operation_date"]) if f.get("operation_date") else None
    treatment = f.get("treatment") or rules.suggest_treatment(client)
    vat = float(core.num(f["vat_rate"])) if f.get("vat_rate") else rules.TREATMENTS[treatment]["vat"]
    irpf = (float(core.num(f["irpf_rate"])) if f.get("irpf_rate") else
            rules.suggest_irpf_rate(treatment, req.s, tax.regime(req.s, int(issue_date[:4])), int(issue_date[:4])))
    if vat not in VAT_RATES:  # tax.form_303 has buckets only for these; any other rate would vanish from the 303
        raise ValueError(_("ставка IVA — 0, 4, 10 или 21 %"))
    if not 0 <= irpf <= 47:
        raise ValueError(_("retención IRPF — от 0 до 47 %"))
    currency = f.get("currency") or "EUR"
    if currency not in rules.CURRENCIES:
        raise ValueError(_("валюта — из списка: по ней ЕЦБ публикует курс"))
    if currency == "EUR":
        fx = 1.0
    elif f.get("fx_rate"):
        fx = float(core.num(f["fx_rate"]))
    else:
        fx = fetch_ecb_rate(currency, op_date or issue_date)
    if fx <= 0:
        raise ValueError(_("курс должен быть больше нуля"))
    lines = [(f[f"desc{i}"], float(core.num(f.get(f"qty{i}"), "1")), parse_money(f.get(f"price{i}", "")))
             for i in range(5) if f.get(f"desc{i}")]
    if not lines:
        raise ValueError(_("нужна хотя бы одна строка"))
    series = "R" + issue_date[:4] if rectifies else core.series_key(req.s["series"], issue_date[:4])
    vals = (client["id"], issue_date, op_date, currency, fx, treatment, vat, irpf, f.get("notes", ""), series)
    if inv_id:
        req.con.execute("""UPDATE invoices SET client_id=?, issue_date=?, operation_date=?, currency=?, fx_rate=?, treatment=?,
                           vat_rate=?, irpf_rate=?, notes=?, series=? WHERE id=? AND number IS NULL""", vals + (inv_id,))
        req.con.execute("DELETE FROM invoice_lines WHERE invoice_id = ?", (inv_id,))
    else:
        inv_id = req.con.execute("""INSERT INTO invoices(client_id, issue_date, operation_date, currency, fx_rate, treatment,
                                    vat_rate, irpf_rate, notes, series) VALUES (?,?,?,?,?,?,?,?,?,?)""", vals).lastrowid
    req.con.executemany("INSERT INTO invoice_lines(invoice_id, description, quantity, unit_price_cents) VALUES (?,?,?,?)",
                        [(inv_id,) + l for l in lines])
    return inv_id


def invoice_new(req):
    if req.method == "POST":
        raise Redirect(f"/invoices/{save_invoice(req)}")
    return page(req, _("Новый счёт"), f"<h1>{_('Новый счёт')}</h1>{invoice_form(req)}")


def get_invoice(req, iid):
    return req.con.execute("SELECT * FROM invoices WHERE id = ?", (iid,)).fetchone() or _404()


def invoice_edit(req, iid):
    inv = get_invoice(req, iid)
    if inv["number"]:
        raise ValueError(_("выставленный счёт менять нельзя — сделайте factura rectificativa"))
    if req.method == "POST":
        save_invoice(req, iid)
        raise Redirect(f"/invoices/{iid}")
    return page(req, _("Черновик"), f"<h1>{_('Черновик счёта')}</h1>{invoice_form(req, inv, db.invoice_lines(req.con, iid))}")


def invoice_issue(req, iid):
    inv = get_invoice(req, iid)
    if inv["number"]:
        raise Redirect(f"/invoices/{iid}")
    s = req.s
    if not (s["name"] and s["tax_id"] and s["address"]):
        raise ValueError(_("перед выставлением заполните имя, NIF/NIE и адрес в настройках"))
    c = req.con.execute("SELECT * FROM clients WHERE id = ?", (inv["client_id"],)).fetchone()
    if not c["address"] or (inv["treatment"] in ("es_b2b", "eu_b2b") and not c["tax_id"]):
        raise ValueError(_("у клиента нужны адрес и NIF / VAT ID (art. 6 RD 1619/2012)"))
    last = req.con.execute("SELECT max(number) AS n, max(issue_date) AS d FROM invoices WHERE series = ? AND number IS NOT NULL",
                           (inv["series"],)).fetchone()
    if last["d"] and inv["issue_date"] < last["d"]:
        raise ValueError(_("дата счёта раньше последнего выставленного в серии {series} ({d}) — нумерация должна идти по датам").format(
            series=core.NUMBER_TOKEN.sub('', inv['series']), d=last['d']))
    parties = {"issuer": {k: s[k] for k in ("name", "tax_id", "address", "email", "iban")},
               "client": {k: c[k] for k in ("name", "tax_id", "address", "country", "is_business")}}
    req.con.execute("UPDATE invoices SET number = ?, parties = ? WHERE id = ?",
                    ((last["n"] or 0) + 1, json.dumps(parties, ensure_ascii=False), iid))
    raise Redirect(f"/invoices/{iid}")


def invoice_paid(req, iid):
    req.con.execute("UPDATE invoices SET paid_date = ? WHERE id = ? AND number IS NOT NULL",
                    (core.iso_date(req.form.get("paid_date") or date.today().isoformat()), iid))
    raise Redirect(f"/invoices/{iid}")


def invoice_delete(req, iid):
    req.con.execute("DELETE FROM invoices WHERE id = ? AND number IS NULL", (iid,))
    raise Redirect("/invoices")


def invoice_rectify(req, iid):
    inv = get_invoice(req, iid)
    if not inv["number"]:
        raise ValueError(_("черновик можно просто исправить"))
    reason = req.form.get("reason", "").strip()
    if not reason:
        raise ValueError(_("укажите причину исправления (art. 15 RD 1619/2012)"))
    today = date.today().isoformat()
    new = req.con.execute("""INSERT INTO invoices(series, issue_date, client_id, currency, fx_rate, treatment, vat_rate, irpf_rate,
                             notes, rectifies_id, rectify_reason) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                          (f"R{today[:4]}", today, inv["client_id"], inv["currency"], inv["fx_rate"], inv["treatment"],
                           inv["vat_rate"], inv["irpf_rate"], "", iid, reason)).lastrowid
    req.con.executemany("INSERT INTO invoice_lines(invoice_id, description, quantity, unit_price_cents) VALUES (?,?,?,?)",
                        [(new, l["description"], -l["quantity"], l["unit_price_cents"]) for l in db.invoice_lines(req.con, iid)])
    raise Redirect(f"/invoices/{new}/edit")


def money_in(c, cur):
    return fmt(c) if cur == "EUR" else fmt(c).replace("€", cur)


def invoice_parties(req, inv) -> tuple[dict, dict]:
    """Issuer and client as printed: frozen snapshot for issued invoices, live data for drafts."""
    if inv["parties"]:
        p = json.loads(inv["parties"])
        return p["issuer"], p["client"]
    c = req.con.execute("SELECT * FROM clients WHERE id = ?", (inv["client_id"],)).fetchone()
    return req.s, dict(c)


def invoice_view(req, iid):
    inv = get_invoice(req, iid)
    s, c = invoice_parties(req, inv)
    a = core.invoice_amounts(req.con, inv)
    cur = inv["currency"]
    lines = "".join(
        f"<tr><td>{h(l['description'])}</td><td class=num>{l['quantity']:g}</td><td class=num>{money_in(l['unit_price_cents'], cur)}</td>"
        f"<td class=num>{money_in(core.line_total(l), cur)}</td></tr>"
        for l in db.invoice_lines(req.con, iid))
    t = rules.TREATMENTS[inv["treatment"]]
    orig = get_invoice(req, inv["rectifies_id"]) if inv["rectifies_id"] else None
    title = "Factura rectificativa" if orig else "Factura / Invoice"
    rect = (f"<p>Rectifica la factura {h(invoice_number(orig))} de {orig['issue_date']}. Motivo: {h(inv['rectify_reason'])} "
            f"(art. 15 RD 1619/2012)</p>") if orig else ""
    eur = "" if cur == "EUR" else (f"<p class=small>Tipo de cambio BCE: 1 EUR = {inv['fx_rate']:g} {h(cur)}. Base imponible {fmt(a['base_eur'])}"
                                   f"{', cuota IVA ' + fmt(a['vat_eur']) if a['vat'] else ''}.</p>")
    irpf_row = (f"<tr><td colspan=3>Retención IRPF {inv['irpf_rate']:g}%</td><td class=num>{money_in(-a['irpf'], cur)}</td></tr>"
                if a["irpf"] else "")
    doc = f"""<article class=invoice>
<div class=inv-head><div><h1>{title}</h1><p>Nº <b>{h(invoice_number(inv))}</b><br>Fecha: {inv['issue_date']}
{'<br>Fecha de operación: ' + inv['operation_date'] if inv['operation_date'] else ''}</p></div>
<div class=right><b>{h(s['name'])}</b><br>NIF: {h(s['tax_id'])}<br>{h(s['address']).replace(chr(10), '<br>')}<br>{h(s['email'])}</div></div>
<div class=bill><small>Cliente / Bill to</small><br><b>{h(c['name'])}</b><br>{'VAT/Tax ID: ' + h(c['tax_id']) + '<br>' if c['tax_id'] else ''}
{h(c['address']).replace(chr(10), '<br>')}<br>{h(c['country'])}</div>
{rect}
<table><thead><tr><th>Concepto / Description</th><th class=num>Cant.</th><th class=num>Precio</th><th class=num>Importe</th></tr></thead>
<tbody>{lines}</tbody><tfoot>
<tr><td colspan=3>Base imponible</td><td class=num>{money_in(a['base'], cur)}</td></tr>
<tr><td colspan=3>{f"IVA {inv['vat_rate']:g}%" if inv['vat_rate'] else 'IVA: no sujeto / not subject'}</td><td class=num>{money_in(a['vat'], cur)}</td></tr>{irpf_row}
<tr class=total><td colspan=3>Total</td><td class=num>{money_in(a['total'], cur)}</td></tr></tfoot></table>
{eur}<p class=small>{h(t['mention'])}</p><div class=noprint>{cite(t.get('sources', []) + ['rd1619-6'] + (['rd1619-15'] if orig else []))}</div>
{'<p class=small>' + h(inv['notes']) + '</p>' if inv['notes'] else ''}
{'<p class=small>IBAN: ' + h(s['iban']) + '</p>' if s['iban'] else ''}</article>"""
    if inv["number"]:
        actions = f"""<button onclick="print()">{_('Печать / PDF')}</button>
<form method=post action="/invoices/{iid}/paid" class=inline><input type=date name=paid_date value="{inv['paid_date'] or date.today().isoformat()}"><button>{_('Оплачен')}</button></form>
<form method=post action="/invoices/{iid}/rectify" class=inline><input name=reason placeholder="{_('Причина исправления')}" required><button>Rectificativa</button></form>"""
    else:
        actions = f"""<a class=btn href="/invoices/{iid}/edit">{_('Изменить')}</a>
<form method=post action="/invoices/{iid}/issue" class=inline><button class=primary>{_('Выставить (присвоить номер)')}</button></form>
<form method=post action="/invoices/{iid}/delete" class=inline onsubmit="return confirm({h(json.dumps(_('Удалить безвозвратно?')))})"><button>{_('Удалить')}</button></form>"""
    return page(req, invoice_number(inv), f"<div class='actions noprint'>{actions}</div>{doc}")


# ---------- expenses ----------

def expense_form(req, e=None):
    e = e or {"date": date.today().isoformat(), "supplier": "", "supplier_tax_id": "", "invoice_ref": "", "description": "",
              "category": "software", "vat_kind": "domestic", "base_cents": None, "vat_rate": 21, "vat_cents": None,
              "deductible_pct": "", "vat_deductible_pct": "", "withheld_cents": 0, "receipt": ""}
    cats = {k: _(v["label"]) for k, v in rules.EXPENSE_CATEGORIES.items()}
    reg = tax.regime(req.s, int(str(e["date"])[:4]))

    def cat_text(k, c):
        pct = str(c["irpf"]) + " %" if c["irpf"] or k == "personal" else _("процент укажите ниже")
        income = (_("В режиме Beckham налог эта покупка не уменьшает: art. 24 TRLIRNR разрешает только персонал, материалы и suministros, "
                    "и gestor считает строго") if reg == "beckham" else
                  (_("В расходы налога на прибыль SL — {pct}") if reg == "sl" else _("В расходы IRPF — {pct}")).format(pct=pct))
        return _("{label}. {income}; IVA к вычету — {vat} %.").format(label=_(c["label"]), income=income, vat=c["vat"])
    receipt = f'<p><a href="/receipts/{quote(e["receipt"])}">{_("чек: {name}").format(name=h(e["receipt"]))}</a></p>' if e["receipt"] else ""
    return f"""<form method=post enctype=multipart/form-data class=grid>
{field(_('Дата'), 'date', e['date'], type='date', required=1)}
{field(_('Поставщик'), 'supplier', e['supplier'], required=1)}
{field(_('NIF/VAT поставщика'), 'supplier_tax_id', e['supplier_tax_id'])}
{field(_('Номер его счёта'), 'invoice_ref', e['invoice_ref'])}
{field(_('Что это'), 'description', e['description'])}
{select(_('Категория'), 'category', cats, e['category'])}
{''.join(switch_explain('category', k, e['category'], cat_text(k, c),
                        ['trlirnr-24'] + [i for i in c['sources'] if i.startswith('liva')] if reg == 'beckham' else c['sources'])
         for k, c in rules.EXPENSE_CATEGORIES.items())}
{select('IVA', 'vat_kind', {k: _(v) for k, v in rules.VAT_KINDS.items()}, e['vat_kind'])}
{''.join(switch_explain('vat_kind', k, e['vat_kind'], _(VAT_KIND_TEXT[k]), rules.VAT_KIND_SOURCES[k]) for k in rules.VAT_KINDS)}
{field(_('База без IVA, €'), 'base', fmt_num(e['base_cents']) if e['base_cents'] is not None else '', required=1)}
{field(_('Ставка IVA %'), 'vat_rate', e['vat_rate'])}
{field(_('Сумма IVA, € (пусто — по ставке)'), 'vat', fmt_num(e['vat_cents']) if e['vat_cents'] is not None else '')}
{field(_('% в налоговую базу (пусто — по категории)'), 'deductible_pct', e['deductible_pct'])}
{field(_('% IVA к вычету (пусто — по категории)'), 'vat_deductible_pct', e['vat_deductible_pct'])}
{explain(_('Пусто — процент категории. Долю IVA можно ставить только для bienes de inversión (дороже 3 005,06 €; у автомобиля — презумпция 50 %). '
           'Остальное при смешанном использовании — 0 % IVA.'), ['liva-95', 'liva-108', 'lirpf-28'])}
{field(_('Retención, которую ВЫ удержали, €'), 'withheld', fmt_num(e['withheld_cents']) if e['withheld_cents'] else '')}
{explain(_('Платите испанскому профессионалу — удерживаете 15 % и сдаёте по 111. Аренда помещения — 19 % по 115.'), ['lirpf-101', 'rirpf-100', 'rirpf-75'])}
<label>{_('Чек / factura (PDF, фото)')}<input type=file name=receipt></label>{receipt}
{explain(_('Без factura на ваше имя расход не вычитается: выписки банка мало. Храните документы не меньше 4 лет после срока подачи декларации, '
           'где расход учтён; по амортизируемым вещам и переносимым остаткам — дольше.'), ['aeat-manual-renta-gastos', 'liva-97', 'lgt-66'])}
<button>{_('Сохранить')}</button></form>"""


def save_expense(req, eid=None):
    f = req.form
    day = core.iso_date(f["date"])
    if f["category"] not in rules.EXPENSE_CATEGORIES or f.get("vat_kind", "domestic") not in rules.VAT_KINDS:
        raise ValueError(_("неизвестная категория или вид IVA"))
    if not f.get("supplier"):
        raise ValueError(_("нужен поставщик"))
    cat = rules.EXPENSE_CATEGORIES[f["category"]]
    base = parse_money(f["base"])
    rate = float(core.num(f.get("vat_rate")))
    vat_kind = f.get("vat_kind", "domestic")
    vat = parse_money(f["vat"]) if f.get("vat") else (core.pct(base, rate) if vat_kind != "none" else 0)
    ded = float(core.num(f["deductible_pct"])) if f.get("deductible_pct") else cat["irpf"]
    vded = float(core.num(f["vat_deductible_pct"])) if f.get("vat_deductible_pct") else cat["vat"]
    if not all(0 <= x <= 100 for x in (rate, ded, vded)):
        raise ValueError(_("ставка IVA и доли вычета — от 0 до 100 %"))
    vals = (day, f["supplier"], f.get("supplier_tax_id", ""), f.get("invoice_ref", ""), f.get("description", ""),
            f["category"], vat_kind, base, rate, vat, ded, vded, parse_money(f.get("withheld", "")))
    cols = ("date, supplier, supplier_tax_id, invoice_ref, description, category, vat_kind, base_cents, vat_rate, vat_cents, "
            "deductible_pct, vat_deductible_pct, withheld_cents")
    if eid:
        req.con.execute(f"UPDATE expenses SET ({cols}) = ({','.join('?' * len(vals))}) WHERE id = ?", vals + (eid,))
    else:
        eid = req.con.execute(f"INSERT INTO expenses ({cols}) VALUES ({','.join('?' * len(vals))})", vals).lastrowid
    if req.files.get("receipt") and req.files["receipt"][1]:
        name, data = req.files["receipt"]
        receipt = f"{day}-{secrets.token_hex(3)}-{re.sub(r'[^A-Za-z0-9._-]', '_', name)[-60:]}"
        (req.data_dir / "receipts").mkdir(exist_ok=True)
        (req.data_dir / "receipts" / receipt).write_bytes(data)
        old = req.con.execute("SELECT receipt FROM expenses WHERE id = ?", (eid,)).fetchone()["receipt"]
        req.con.execute("UPDATE expenses SET receipt = ? WHERE id = ?", (receipt, eid))
        if old:  # the old file goes only once the row points at the new one
            (req.data_dir / "receipts" / old).unlink(missing_ok=True)
    return eid


def delete_expense(con, data_dir: Path, eid: int) -> None:
    """Row first, then its receipt file: a failed delete never leaves a row pointing at a missing file."""
    old = con.execute("SELECT receipt FROM expenses WHERE id = ?", (eid,)).fetchone()
    con.execute("DELETE FROM expenses WHERE id = ?", (eid,))
    if old and old["receipt"]:
        (data_dir / "receipts" / old["receipt"]).unlink(missing_ok=True)


def expenses(req):
    y = req.year()
    rows, tot_base, tot_ded, tot_vat = [], 0, 0, 0
    for e in req.con.execute("SELECT * FROM expenses WHERE substr(date, 1, 4) = ? ORDER BY date DESC, id DESC", (str(y),)):
        ded = tax.expense_deductible(e, tax.amort_rate(req.s))
        vded = tax.expense_vat_deductible(e)
        tot_base += e["base_cents"]
        tot_ded += ded
        tot_vat += vded
        rows.append((e["date"], f'<a href="/expenses/{e["id"]}">{h(e["supplier"])}</a>', h(e["description"]),
                     h(_(rules.EXPENSE_CATEGORIES[e["category"]]["label"])), fmt(e["base_cents"]), fmt(ded), fmt(vded),
                     _("чек") if e["receipt"] else ""))
    body = f"""<h1>{_('Расходы')}</h1>{year_switch(req, '/expenses')}<p><a class=btn href="/expenses/new">{_('Новый расход')}</a></p>
{table([_('Дата'), _('Поставщик'), _('Что'), _('Категория'), _('База'), _('В налоговую базу'), _('IVA к вычету'), ''], rows)}
<p class=muted>{_('Итого {y}: база {base}, уменьшает базу {ded}, IVA к вычету {vat}.').format(y=y, base=fmt(tot_base), ded=fmt(tot_ded), vat=fmt(tot_vat))}</p>
<p class=muted>{_('Подсказка: расход вычитается только с factura completa на ваш NIE/NIF и только если он связан с деятельностью.')}</p>"""
    return page(req, _("Расходы"), body)


def expense_new(req):
    if req.method == "POST":
        save_expense(req)
        raise Redirect("/expenses?year=" + req.form["date"][:4])
    return page(req, _("Новый расход"), f"<h1>{_('Новый расход')}</h1>{expense_form(req)}")


def expense_edit(req, eid):
    e = req.con.execute("SELECT * FROM expenses WHERE id = ?", (eid,)).fetchone() or _404()
    if req.method == "POST":
        save_expense(req, eid)
        raise Redirect("/expenses?year=" + req.form["date"][:4])
    return page(req, _("Расход"), f"""<h1>{_('Расход')}</h1>{expense_form(req, e)}
<form method=post action="/expenses/{eid}/delete" onsubmit="return confirm({h(json.dumps(_('Удалить безвозвратно?')))})"><button>{_('Удалить')}</button></form>""")


def expense_delete(req, eid):
    delete_expense(req.con, req.data_dir, eid)
    raise Redirect("/expenses")


def receipt_file(req, name):
    p = (req.data_dir / "receipts" / name).resolve()
    if p.parent != (req.data_dir / "receipts").resolve() or not p.is_file():
        raise NotFound()
    return p


# ---------- taxes ----------

SEDE = {  # official AEAT procedure page per modelo (checked 08.10.2026)
    "303": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G414.shtml",
    "130": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G601.shtml",
    "349": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI28.shtml",
    "390": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G412.shtml",
    "347": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI27.shtml",
    "100": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G229.shtml",
    "151": "https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-151.html",
    "111": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GH01.shtml",
    "115": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GH02.shtml",
    "202": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GE00.shtml",
    "200": "https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GE04.shtml",
    "RETA": "https://portal.seg-social.gob.es/wps/portal/importass/importass",
}

BOX_RU = {  # plain words under the Spanish label (Russian or English; none in Spanish); the Spanish stays because that is what the Sede form says
    # 303
    "Régimen general 21 %: Base imponible": N_("IVA 21 % с ваших продаж: база"), "Régimen general 21 %: Cuota": N_("…сумма IVA"),
    "Adquisiciones intracomunitarias de bienes y servicios: Base imponible": N_("покупки у бизнеса из ЕС: база"),
    "Adquisiciones intracomunitarias de bienes y servicios: Cuota": N_("…IVA, который вы начисляете сами"),
    "Otras operaciones con inversión del sujeto pasivo (excepto adq. intracom.): Cuota": N_("…IVA, который вы начисляете сами"),
    "Modificación bases y cuotas: Base imponible": N_("исправления по счетам: база"), "Modificación bases y cuotas: Cuota": N_("…исправление IVA"),
    "Total cuota devengada": N_("итого IVA начислено"),
    "Por cuotas soportadas en operaciones interiores corrientes: Base": N_("испанские расходы с IVA: база"),
    "Por cuotas soportadas en operaciones interiores corrientes: Cuota": N_("…IVA к вычету"),
    "En adquisiciones intracomunitarias de bienes y servicios corrientes: Base": N_("расходы у бизнеса из ЕС: база"),
    "En adquisiciones intracomunitarias de bienes y servicios corrientes: Cuota": N_("…IVA к вычету"),
    "Total a deducir": N_("итого IVA к вычету"), "Resultado régimen general": N_("разница: начислено минус к вычету"),
    "Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 123)": N_("услуги клиентам вне ЕС, без испанского IVA"),
    "Cuotas a compensar pendientes de periodos anteriores": N_("остаток к зачёту из прошлых кварталов"),
    "Cuotas a compensar de periodos anteriores aplicadas en este periodo": N_("зачтено в этом квартале"),
    "Cuotas a compensar de periodos previos pendientes para periodos posteriores": N_("остаток на следующие кварталы"),
    "Resultado": N_("итог"),
    # 390
    "Régimen ordinario 21 %: Base imponible": N_("IVA 21 % с ваших продаж: база"), "Régimen ordinario 21 %: Cuota devengada": N_("…сумма IVA"),
    "Régimen ordinario 10 %: Base imponible": N_("IVA 10 % с ваших продаж: база"), "Régimen ordinario 10 %: Cuota devengada": N_("…сумма IVA"),
    "Régimen ordinario 4 %: Base imponible": N_("IVA 4 % с ваших продаж: база"), "Régimen ordinario 4 %: Cuota devengada": N_("…сумма IVA"),
    "Adquisiciones intracomunitarias de servicios 21 %: Base imponible": N_("услуги от бизнеса из ЕС: база"),
    "Adquisiciones intracomunitarias de servicios 21 %: Cuota devengada": N_("…IVA, который вы начисляете сами"),
    "Total bases y cuotas IVA: Cuota devengada": N_("итого IVA начислено"),
    "Modificación de bases y cuotas: Base imponible": N_("исправления по счетам: база"),
    "Modificación de bases y cuotas: Cuota devengada": N_("…исправление IVA"),
    "Total bases imponibles y cuotas deducibles en operaciones interiores de bienes y servicios corrientes: Cuota deducible": N_("…IVA к вычету"),
    "Total bases imponibles y cuotas deducibles en operaciones interiores de bienes de inversión: Cuota deducible":
        N_("IVA к вычету по основным средствам"),
    "Total bases imponibles y cuotas deducibles en adquisiciones intracomunitarias de servicios: Cuota deducible": N_("…IVA к вычету"),
    "Suma de deducciones": N_("итого IVA к вычету"),
    "Suma de resultados": N_("разница: начислено минус к вычету"), "Resultado de la liquidación": N_("итог"),
    "Total resultados a ingresar en las autoliquidaciones de IVA del ejercicio": N_("сумма положительных 303"),
    "Compensación de cuotas del ejercicio anterior": N_("зачтён остаток прошлого года"),
    "A compensar": N_("IV квартал: оставить к зачёту"), "A devolver": N_("IV квартал: вернуть"),
    "Cuotas pendientes de compensación generadas en el ejercicio y distintas de las incluidas en la casilla 97":
        N_("остаток к зачёту на конец года"),
    "Operaciones en régimen general": N_("оборот с IVA"), "Entregas intracomunitarias de bienes y servicios": N_("оборот: услуги бизнесу в ЕС"),
    "Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 126)": N_("оборот: клиенты вне ЕС"),
    "Total volumen de operaciones (Art. 121 Ley IVA)": N_("оборот за год"),
    # 130
    "Rendimiento neto": N_("чистый доход"), "20 por 100 del importe de la casilla 03": N_("20 % от чистого дохода"),
    "A deducir: De los trimestres anteriores": N_("авансы, уплаченные в прошлых кварталах"),
    N_("Retenciones e ingresos a cuenta soportados (с 1 января)"): N_("удержания клиентов с 1 января"),
    "Pago fraccionado previo del trimestre": N_("аванс до вычетов"),
    "Minoración por aplicación de la deducción a que se refiere el artículo 110.3 c) del Reglamento del Impuesto":
        N_("скидка при низком доходе прошлого года"),
    "Resultados negativos de trimestres anteriores": N_("отрицательные результаты прошлых кварталов"),
    "Resultado de la autoliquidación": N_("итог"),
    # 100 / 151
    "Total ingresos computables": N_("доходы"), "Base imponible general": N_("налоговая база"),
    "Cuota líquida incrementada total": N_("налог после вычетов"), "Cuota íntegra autonómica": N_("региональная часть налога"),
    "Retenciones y demás pagos a cuenta: Por rendimientos de actividades económicas": N_("удержания клиентов"),
    "Retenciones e ingresos a cuenta": N_("удержания клиентов"),
    "Pagos fraccionados ingresados (actividades económicas)": N_("авансы по 130"),
    "Reducción por inicio de una actividad económica": N_("снижение 20 % для новых"),
    "Dotaciones del ejercicio para amortización de inmovilizado material": N_("амортизация"),
    "Seguridad Social del titular de la actividad": N_("взносы RETA"),
    # RETA
    "Rendimiento mensual para SS": N_("месячный доход для RETA"), "base máxima": N_("максимальная база"),
}


def next_step(f, done, today) -> str:
    """«Дальше»: the one thing to do now for this return, with the place to do it. Every state has a step, waiting included."""
    m, guide = f["modelo"], f'<a class=go href="/guide#{h(f["modelo"])}">{_("Как подать →")}</a>'
    sede = f'<a class=go href="{h(SEDE[m])}" target=_blank rel=noopener>{_("Открыть в Sede ↗")}</a>' if m in SEDE else ""
    if sede_file.available(f):
        sede += f'<a class=go href="/sede/{f["year"]}/{h(f["period"])}/{h(m)}">{_("Скачать файл для Sede ↓")}</a>'
    if m == "RETA":
        raise_base = (_("Чтобы доплата была меньше, поднимите базу в Import@ss: новая база действует с 1 марта, мая, июля, сентября, "
                        "ноября или января — после двухмесячного окна заявления.") + " " if f["result"] > 0 else "")
        return (f'<div class=next><b>{_("Дальше")}</b>{_("Подавать ничего не нужно: TGSS пересчитает взносы сама, когда AEAT передаст ей ваш доход за год.")} '
                f'{_("Ждите уведомления в Import@ss или NOTESS; доплату вносят до конца месяца после уведомления.")} {raise_base}'
                f'{cite(["rd2064-1995-46", "rd2064-1995-45"])}<br>'
                f'<a class=go href="{h(SEDE["RETA"])}" target=_blank rel=noopener>{_("Открыть Import@ss ↗")}</a></div>')
    if done:
        if mismatch(f, done):
            return ""  # the mismatch warning already says what to do
        pay = m in PAYS and (done["amount_cents"] or 0) > 0
        return (f'<div class="next done"><b>{_("Подано {d}").format(d=h(done["filed_on"]))}</b>'
                f'{_("Сохраните PDF-justificante с CSV: только он подтверждает подачу.")} '
                + (_("Проверьте в банке, что сумма списана или оплачена по NRC.") if pay else _("Больше ничего делать не нужно.")) + "</div>")
    if today < f["opens"]:
        return (f'<div class=next><b>{_("Дальше")}</b>'
                f'{_("Окно подачи откроется {d}. До тех пор вносите счета и расходы периода — gestor пересчитает цифры.").format(d=h(f["opens"]))} {guide}</div>')
    if f["deadline"] < today:
        return (f'<div class="next late"><b>{_("Срок прошёл {d}").format(d=h(f["deadline"]))}</b>'
                f'{_("Подайте как можно скорее: пока AEAT не прислала требование, доплата и штраф меньше.")} '
                f'{cite(["lgt-27", "lgt-198"])}<br>{guide}{sede}</div>')
    what = (_("Подайте и оплатите: списанием со счёта (domiciliación — заканчивается на несколько дней раньше срока) или по NRC.")
            if m in PAYS and f["result"] > 0 else
            _("Подайте; платить не нужно — сумма уменьшит IVA следующего квартала.") if m == "303" and f["result"] < 0 else
            _("Подайте; это сведения, платить не нужно.") if m not in PAYS else _("Подайте с нулевым результатом."))
    return f'<div class=next><b>{_("Дальше, до {d}").format(d=h(f["deadline"]))}</b>{what} {guide}{sede}</div>'


def action(f, done) -> str:
    if f["modelo"] == "RETA":
        return _("Ждать перерасчёта TGSS")
    if done:
        return _("Сумма в Sede отличается от расчёта — проверьте") if mismatch(f, done) else _("Подано")
    if f["modelo"] not in PAYS:
        return _("Подать, это сведения")
    return _("Подать и заплатить") if f["result"] > 0 else (_("Подать, платить не нужно") if f["result"] < 0 else _("Подать с нулём"))


def render_form(req, f, filed) -> str:
    done = filed.get((f["modelo"], f["period"]))
    plain = {} if i18n.current.get() == "es" else {_(k): v for k, v in BOX_RU.items()}  # Spanish readers need only the form's own label
    ru = lambda label: f'<span class=ru>{h(_(plain[label]))}</span>' if plain.get(label) else ""
    rows = [(f'<span class=box>{f"<sup>{h(b[0])}</sup>" if b[0] else ""}{fmt(b[2]).replace(" €", "")}</span>', h(b[1]) + ru(b[1]),
             cite(tax.applicable(tax.BOX_SOURCES.get((f["modelo"], b[0]), []), req.s, f["year"]))) for b in f["boxes"]]
    boxes = (f"<table class=boxes><thead><tr><th>Casilla, €</th><th>{_('Как в форме и по-русски')}</th><th>{_('Основание')}</th></tr></thead><tbody>"
             + "".join(f"<tr><td class=v>{v}</td><td>{label}</td><td class=basis>{c}</td></tr>" for v, label, c in rows) + "</tbody></table>")
    notes = "".join(f"<li>{cited(n)}</li>" for n in f.get("notes", []) if n)
    basis = f'<div class=basis>{_("Основание:")} {cite(f.get("sources", []))}</div>' if f.get("sources") else ""
    hidden = (f'<input type=hidden name=modelo value="{h(f["modelo"])}"><input type=hidden name=year value="{f["year"]}">'
              f'<input type=hidden name=period value="{h(f["period"])}">')
    differs = mismatch(f, done)
    if done:
        check = (f'<div class=warn>{_("В Sede вы указали {filed}, gestor сейчас считает {now}: разница {diff}. Возможно, после подачи добавились счета или расходы — тогда нужна autoliquidación rectificativa.").format(filed=fmt(done["amount_cents"]), now=fmt(f["result"]), diff=fmt(done["amount_cents"] - f["result"]))} '
                 f'{cite(["lgt-120"] + (["riva-74bis"] if f["modelo"] == "303" else []))}</div>') if differs else ""
        status = f"""{check}<span class="stamp ok">PRESENTADO</span> {h(done['filed_on'])}{', CSV ' + h(done['reference']) if done['reference'] else ''}
<form method=post action="/filings/unmark" class=inline>{hidden}<button>{_('Отменить отметку')}</button></form>"""
    elif f["modelo"] == "RETA":
        status = ""
    else:
        status = f"""<form method=post action="/filings" class=inline>{hidden}
<label>{_('Сумма из Sede')}<input name=amount value="{fmt_num(f['result'])}" size=10></label>
<label>{_('Дата подачи')}<input type=date name=filed_on value="{date.today().isoformat()}"></label>
<label>{_('CSV из justificante')}<input name=reference size=16></label><button class=primary>{_('Отметить поданным')}</button></form>"""
    nxt = next_step(f, done, date.today().isoformat())
    return f"""<details class=form id="f-{h(f['modelo'])}-{h(f['period'])}"{' open' if not done or differs else ''}><summary><b>{h(f['modelo'])}</b> {h(f['title'])}
{'' if f['modelo'] == 'RETA' else f"<span class=due>{_('до {d}').format(d=f['deadline'])}</span>"}{' <span class="stamp late">' + _('СУММА ОТЛИЧАЕТСЯ') + '</span>' if differs else ''}
<span class=res>{h(f.get('result_label') or _('Результат'))}: {fmt(f['result'])}</span>
<small class=about>{h(_(tax.MODELO_ABOUT.get(f['modelo'], '')))}</small></summary>
{boxes}{'<ul class=notes>' + notes + '</ul>' if notes else ''}{basis}<div class=mark>{nxt}{status}</div></details>"""


def taxes(req):
    y, today = req.year(), date.today().isoformat()
    filed, books = filings(req, y), has_books(req, y)
    groups = tax.forms(req.con, req.s, y)
    body, index = "", []
    for n, (g, fs) in enumerate(groups, 1):
        unfiled = [f for f in fs if f["modelo"] != "RETA" and (f["modelo"], f["period"]) not in filed]
        due = min((f["deadline"] for f in unfiled or fs if f["modelo"] != "RETA"), default="")
        index.append((f"q{n}", g, f"{due[8:10]}.{due[5:7]}" if due else "",
                      [(f"f-{f['modelo']}-{f['period']}", f["modelo"], books and f in unfiled and f["deadline"] < today) for f in fs]))
        summary = "".join(f'<tr><td><a href="#f-{h(f["modelo"])}-{h(f["period"])}">{h(f["modelo"])}</a> {h(f["title"])}'
                          f'<small>{h(_(tax.MODELO_ABOUT.get(f["modelo"], "")))}</small></td>'
                          f'<td class=num>{fmt(f["result"])}</td><td>{action(f, filed.get((f["modelo"], f["period"])))}</td>'
                          f'<td>{stamp(f, filed, today, books) if f["modelo"] != "RETA" else ""}</td></tr>' for f in fs)
        body += (junction(f"{n}T" if n <= 4 else _("год")) + f'<h2 id=q{n}>{h(g)}</h2>' + (f'<table class=quarter><thead><tr><th>Modelo</th><th class=num>{_("Результат")}</th><th>{_("Что сделать")}</th>'
                                               f'<th>{_("Статус")}</th></tr></thead><tbody>{summary}</tbody></table>'
                                               + "".join(render_form(req, f, filed) for f in fs) if fs else f"<p class=muted>{_('нет обязательств')}</p>"))
    return page(req, _("Налоги"), f"""<h1>{_('Налоги')} {y} <small>{h(tax.regime_label(req.s, y))}</small></h1>
<p class=sub>{_('Перенесите casillas в Sede AEAT один в один и отметьте подачу здесь. У каждой casilla — закон, по которому она посчитана.')} <a href="/guide">{_('Как подать в Sede, по шагам →')}</a></p>
{onboarding_hint(req)}{year_switch(req, '/taxes')}{body}
<div class=band id=export>{_('Экспорт')}</div><p><a href="/export/{y}/emitidas.csv">Libro de facturas emitidas (CSV)</a><br>
<a href="/export/{y}/recibidas.csv">Libro de facturas recibidas / gastos (CSV)</a></p>
<p class=muted>{_('При отметке «подан» укажите сумму из поданной декларации: годовые 100 и 200 учитывают только поданные авансы, а gestor сравнит её со своим расчётом.')}</p>
<div class=basis>{_('Опоздание и исправление декларации:')} {cite(['lgt-27', 'lgt-198', 'lgt-120', 'riva-74bis', 'lgt-66'])}</div>""",
                index + [("export", _("Экспорт"), "", [])])


def save_filing(con, f):
    con.execute("INSERT OR REPLACE INTO filings(modelo, year, period, filed_on, amount_cents, reference) VALUES (?,?,?,?,?,?)",
                (f["modelo"], int(f["year"]), f["period"], core.iso_date(f.get("filed_on") or date.today().isoformat()),
                 parse_money(f.get("amount", "")), f.get("reference", "")))


def delete_filing(con, f):
    con.execute("DELETE FROM filings WHERE modelo = ? AND year = ? AND period = ?", (f["modelo"], int(f["year"]), f["period"]))


def filing_mark(req):
    save_filing(req.con, req.form)
    raise Redirect(f"/taxes?year={int(req.form['year'])}")


def filing_unmark(req):
    delete_filing(req.con, req.form)
    raise Redirect(f"/taxes?year={int(req.form['year'])}")


def safe_cell(v):
    """Spreadsheet formula injection guard for text cells."""
    return "'" + v if isinstance(v, str) and v[:1] in ("=", "+", "-", "@") else v


def export_csv(req, year, kind):
    out = io.StringIO()
    w = csv.writer(out, delimiter=";")
    if kind == "emitidas":
        w.writerow(["Fecha expedición", "Fecha operación", "Serie-Número", "Destinatario", "NIF destinatario", "País",
                    "Tipo operación", "Base imponible EUR", "Tipo IVA", "Cuota IVA EUR", "Retención IRPF EUR", "Total EUR"])
        for inv in req.con.execute("SELECT * FROM invoices WHERE number IS NOT NULL AND substr(issue_date, 1, 4) = ? ORDER BY series, number",
                                   (str(year),)):
            a = core.invoice_amounts(req.con, inv)
            _, c = invoice_parties(req, inv)
            w.writerow([inv["issue_date"], inv["operation_date"] or "", invoice_number(inv), safe_cell(c["name"]), safe_cell(c["tax_id"]),
                        c["country"], inv["treatment"], fmt_num(a["base_eur"]), inv["vat_rate"], fmt_num(a["vat_eur"]),
                        fmt_num(a["irpf_eur"]), fmt_num(a["total_eur"])])
    else:
        w.writerow(["Fecha", "Proveedor", "NIF proveedor", "Nº factura", "Concepto", "Categoría", "Tipo IVA", "Base EUR",
                    "Cuota IVA EUR", "IVA deducible EUR", "Gasto deducible EUR", "Retención practicada EUR"])
        for e in req.con.execute("SELECT * FROM expenses WHERE substr(date, 1, 4) = ? ORDER BY date, id", (str(year),)):
            w.writerow([e["date"], safe_cell(e["supplier"]), safe_cell(e["supplier_tax_id"]), safe_cell(e["invoice_ref"]),
                        safe_cell(e["description"]), e["category"], e["vat_kind"], fmt_num(e["base_cents"]), fmt_num(e["vat_cents"]),
                        fmt_num(tax.expense_vat_deductible(e)), fmt_num(tax.expense_deductible(e, tax.amort_rate(req.s))),
                        fmt_num(e["withheld_cents"])])
    return ("text/csv; charset=utf-8", "\ufeff" + out.getvalue(), f"{kind}-{year}.csv")


# ---------- settings / entities ----------

def year_amounts(text: str, quarterly=False) -> dict:
    """'2025 1234,56' per line → {'2025': cents}; quarterly: '2026 1T 2400,00' → {'2026-1T': cents}."""
    out, shape = {}, _("«год квартал сумма»") if quarterly else _("«год сумма»")
    for line in text.splitlines():
        parts = line.split()
        if len(parts) == 2 + quarterly and re.fullmatch(r"\d{4}", parts[0]) and (not quarterly or parts[1].upper() in ("1T", "2T", "3T", "4T")):
            key = f"{parts[0]}-{parts[1].upper()}" if quarterly else parts[0]
            out[key] = parse_money(parts[-1])
            if out[key] < 0:
                raise ValueError(_("строка {line}: сумма не может быть отрицательной").format(line=repr(line)))
        elif parts:
            raise ValueError(_("строка {line}: нужно {shape}").format(line=repr(line), shape=shape))
    return out


def year_amounts_text(d: dict) -> str:
    return "\n".join(f"{y.replace('-', ' ')} {fmt_num(v)}" for y, v in sorted(d.items()))


CENSO = {"303": "IVA trimestral (303)", "130": "IRPF pago fraccionado (130)", "111": "Retenciones e ingresos a cuenta (111)",
         "115": "Retenciones de arrendamientos (115)", "roi": "Registro de operadores intracomunitarios (ROI)"}


def residence_lines(text: str) -> list:
    """'2024-01-01 valencia' per line → [{'from', 'region'}] sorted by date; lines of another shape are ignored."""
    out = []
    for line in text.splitlines():
        parts = line.split()
        if len(parts) == 2:
            if parts[1] not in rules.REGIONS:
                raise ValueError(_("неизвестный регион {region}; варианты: {options}").format(region=repr(parts[1]), options=", ".join(rules.REGIONS)))
            out.append({"from": core.iso_date(parts[0]), "region": parts[1]})
    return sorted(out, key=lambda r: r["from"])


def series_format(text: str) -> str:
    series = text.strip().upper() or "A"
    if not (re.fullmatch(r"[A-Z0-9]+", series) or (len(core.NUMBER_TOKEN.findall(series)) == 1 and
                                                     re.fullmatch(r"[A-Z0-9/._-]*", re.sub(r"\{YYYY\}|\{N+\}", "", series)))):
        raise ValueError(_("формат номера: буквы, цифры, - / . _ , {YYYY} и один {NNNN}; например FACT-{YYYY}-{NNNNN}"))
    return series


def one_of(options, error):
    def check(v):
        if v not in options:
            raise ValueError(_(error))
        return v
    return check


def year4(v: str) -> str:
    if v and not re.fullmatch(r"\d{4}", v):
        raise ValueError(_("год — 4 цифры"))
    return v


opt_date = lambda v: core.iso_date(v) if v else ""
flag = lambda v: v == "1"

# Questionnaire field → parser of the form's text value. The web form posts all of them; the MCP server posts only the changed ones.
SETTINGS_FIELDS = {
    "name": str, "tax_id": str.upper, "address": str, "email": str, "iban": str,
    "phone": lambda v: re.sub(r"\D", "", v)[-9:], "lang": one_of(("", *i18n.LANGS), N_("неизвестный язык")),
    "sex": lambda v: v if v in ("", "H", "M") else "", "iae": lambda v: re.sub(r"[^0-9.]", "", v)[:4],
    "censo": lambda v: [k for k in CENSO if k in v.split()],  # space-separated keys of CENSO
    "kind": one_of(("autonomo", "sl"), N_("неизвестная форма или статус")),
    "visa": one_of(rules.VISAS, N_("неизвестная форма или статус")),
    "beckham_first_year": year4, "inicio_first_year": year4, "sl_first_profit_year": year4,
    "activity_start": opt_date, "reta_start": opt_date, "permit_until": opt_date, "censo_date": opt_date, "birth_date": opt_date,
    "residence": residence_lines, "series": series_format,
    "activity_kind": lambda v: one_of(("profesional", "empresarial"), N_("неизвестный вид деятельности"))(v or "profesional"),
    "new_activity_irpf_7": flag, "tarifa_plana": flag, "sl_small_incn": flag, "sl_emergente": flag,
    "reta_base": parse_money, "iva_carry": year_amounts, "sl_200_cuotas": year_amounts,
    "irnr_paid": lambda v: year_amounts(v, quarterly=True),
}


def settings_values(f: dict) -> dict:
    """Form text values → validated settings; only the keys present in f."""
    return {k: SETTINGS_FIELDS[k](v) for k, v in f.items()}


def settings(req):
    s = req.s
    if req.method == "POST":
        f = req.form
        form = {k: f.get(k, "") for k in SETTINGS_FIELDS} | {"censo": " ".join(k for k in CENSO if f.get(f"censo_{k}") == "1")}
        db.save_settings(req.con, settings_values(form))
        raise Redirect("/settings?saved=1")
    res = "\n".join(f"{r['from']} {r['region']}" for r in s["residence"])
    chk = lambda name, label: (f'<label class=check><input type=checkbox id=f-{name} name={name} value=1'
                               f'{" checked" if s.get(name) else ""}> {label}</label>')
    rate = tax._known(tax.RETA_RATE, date.today().year)
    sl = s["kind"] == "sl"
    sl_band = f"""<div class=band>{_('Только для SL')}</div>
{chk('sl_small_incn', _('Оборот SL за прошлый год меньше 1 млн €'))}
{explain(_('Микропредприятие платит налог на прибыль по пониженной шкале (в 2026 году 19 % и 21 %) вместо 25 %.'), ['lis-29', 'lis-dt44'])}
{chk('sl_emergente', _('SL — сертифицированная empresa emergente (Ley 28/2022)'))}
{field(_('Первый прибыльный год SL'), 'sl_first_profit_year', s['sl_first_profit_year'], placeholder='2025', id='f-sl_first_profit_year')}
{explain(_('Empresa emergente платит 15 % в первый прибыльный год и 3 следующих. Авансы 202 в первые 2 года не платятся.'), ['ley28-2022-7', 'sl-ley28-2022-8'])}
<label>{_('База 202 из поданных Modelo 200 (cuota − deducciones − retenciones): «год сумма»')}<textarea name=sl_200_cuotas rows=2 placeholder="2025 12700,00">{h(year_amounts_text(s['sl_200_cuotas']))}</textarea></label>
{explain(_('Авансы 202 — 18 % от этой суммы из последней поданной 200. Без неё gestor оценивает по книгам.'), ['lis-40'])}""" if sl else ""
    body = f"""<h1>{_('Профиль «{name}»').format(name=h(req.entity))}</h1>
<p class=sub>{_('Сверху — как gestor понял вашу ситуацию и что из неё следует. Ниже — <a href="#form">анкета</a>: у каждого вопроса написано, на что он влияет и на каком законе это основано.')}</p>
{'<p class=ok>' + _('Сохранено. Проверьте выводы ниже.') + '</p>' if req.query.get('saved') else ''}
{understood(req)}
{junction(_('анкета'))}
<h2 id=form>{_('Анкета')}</h2>
<form method=post class=grid>
<div class=band>{_('Кто вы — печатается на каждом счёте')}</div>
{field(_('Имя / razón social'), 'name', s['name'], id='f-name')}{field('NIE / NIF', 'tax_id', s['tax_id'], id='f-tax_id')}
<label>{_('Адрес')}<textarea name=address rows=3>{h(s['address'])}</textarea></label>
{field('Email', 'email', s['email'])}{field(_('Телефон'), 'phone', s['phone'], placeholder='600123456')}{field(_('IBAN для оплаты'), 'iban', s['iban'])}
{select(_('Язык интерфейса'), 'lang', {'': _('как в браузере'), **i18n.LANGS}, s['lang'])}
{explain(_('Без имени, NIF и адреса счёт неполный: gestor не даст его выставить.'), ['rd1619-6'])}
{select(_('Пол (как в certificado censal)'), 'sex', {'': '—', 'H': 'Hombre', 'M': 'Mujer'}, s['sex'])}{field(_('Дата рождения'), 'birth_date', s['birth_date'], type='date')}
{explain(_('Телефон, пол и дату рождения gestor вписывает в файлы 349 и 151 для Sede.'), [])}
<div class=band>{_('Форма и статус')}</div>
{select(_('Форма'), 'kind', {'autonomo': 'Autónomo (persona física)', 'sl': 'Sociedad Limitada'}, s['kind'])}
{select(_('Статус пребывания'), 'visa', {k: _(v) for k, v in rules.VISAS.items()}, s['visa'])}
{switch_explain('kind', 'autonomo', s['kind'], _('Autónomo платит IRPF с прибыли: доходы минус расходы деятельности.'), ['lirpf-28'])}
{switch_explain('kind', 'sl', s['kind'], _('SL платит налог на прибыль, а вы как администратор — IRPF со своего вознаграждения.'), ['lis-29', 'rirpf-80'])}
{''.join(switch_explain('visa', k, s['visa'], _('{label}: от статуса зависят ограничения деятельности и условия продления.').format(label=_(label)),
                        rules.VISA_SOURCES.get(k, []))
         for k, label in rules.VISAS.items())}
{field(_('Первый год режима Beckham (пусто — общий IRPF)'), 'beckham_first_year', s['beckham_first_year'], placeholder='2025', id='f-beckham_first_year')}
{explain(_('Первый год, в котором вы стали налоговым резидентом Испании: режим считается с него, а не с даты Modelo 149. Режим длится 6 лет: этот год и 5 следующих. '
           'Для autónomo режим возможен только как actividad emprendedora (отчёт ENISA) или как высококвалифицированный профессионал для стартапов и I+D+i.'),
         ['lirpf-93', 'rirpf-116', 'rirpf-113', 'dgt-v1274-25'])}
<label>{_('Beckham: уплачено по Modelo 210, «год квартал сумма»')}<textarea name=irnr_paid rows=3 placeholder="2026 1T 2400,00&#10;2026 2T 2400,00">{h(year_amounts_text(s['irnr_paid']))}</textarea></label>
{explain(_('Квартальный 210 в режиме закон не требует, но если вы его платили, эти суммы вычитаются из налога в 151.'),
         ['orden-eha-3316-2010-210', 'rirpf-114-2b-cuotas-irnr', 'aeat-151-instr-c34'])}
<div class=band>{_('Где вы живёте')}</div>
<label>{_('По строке «дата регион» ({regions})').format(regions=', '.join(rules.REGIONS))}<textarea id=f-residence name=residence rows=3 placeholder="2024-03-01 madrid&#10;2027-01-15 andalucia">{h(res)}</textarea></label>
{explain(_('Регион задаёт региональную часть IRPF. Регион года — тот, где вы прожили больше дней. Прописка сама по себе не доказательство.'),
         ['lirpf-72', 'lirpf-9', 'irpf-dgt-v1886-18'])}
<div class=band>{_('Деятельность')}</div>
{field(_('Alta в Hacienda (Modelo 036/037)'), 'activity_start', s['activity_start'], type='date', id='f-activity_start')}
{select(_('Вид деятельности (IAE)'), 'activity_kind', {'profesional': _('Profesional (раздел 2: разработка, консалтинг)'), 'empresarial': _('Empresarial (раздел 1)')}, s['activity_kind'])}
{field(_('Эпиграф IAE (из certificado censal, например 763)'), 'iae', s['iae'], placeholder='763')}
{explain(_('Профессионалу испанский клиент-бизнес удерживает 15 % IRPF из счёта, в первые годы — 7 %. С empresarial не удерживают.'),
         ['lirpf-101', 'rirpf-95'])}
{chk('new_activity_irpf_7', _('Удержание 7 % вместо 15 % (год начала и 2 следующих)'))}
{explain(_('Клиенту нужно письменно сообщить, что вы начинаете деятельность. Срок считается календарными годами.'),
         ['rirpf-95', 'irpf-dgt-v3658-16'])}
{field(_('Первый прибыльный год для снижения 20 %'), 'inicio_first_year', s['inicio_first_year'], placeholder='2025', id='f-inicio_first_year')}
{explain(_('Снижение 20 % — в первый прибыльный год и следующий, база до 100 000 €. Не положено за год, в котором больше половины выручки — от компании, '
           'где вы были наёмным в год перед стартом, и если в год перед стартом у вас уже была деятельность.'),
         ['lirpf-32', 'irpf-dgt-v0175-18', 'irpf-dgt-v1425-18'])}
{field(_('ВНЖ / виза действует до'), 'permit_until', s['permit_until'], type='date')}
{explain(_('gestor предупредит за 120 дней до конца срока.'), rules.VISA_SOURCES.get(s['visa'], [])[-1:])}
<div class=band>{_('RETA — соцстрах autónomo')}</div>
{field(_('Alta в RETA'), 'reta_start', s['reta_start'], type='date', id='f-reta_start')}
{field(_('Текущая база RETA, €/мес (пусто — минимальная)'), 'reta_base', fmt_num(s['reta_base']) if s.get('reta_base') else '', id='f-reta_base')}
{explain(_('Базу вы выбираете в Import@ss. Взнос = база × {rate} % (сумма ставок приказа о взносах). После года TGSS сверит базу с вашим реальным доходом '
           'и доначислит или вернёт разницу.').format(rate=rate[0]), sources.for_year(['orden-pjc-178-2025', 'orden-pjc-297-2026'], date.today().year)
         + ['rd2064-1995-46', 'rd2064-1995-45', 'tgss-importass-base'])}
{chk('tarifa_plana', _('Льготный взнос RETA (tarifa plana, cuota reducida)'))}
{explain(_('80 €/мес закон прямо устанавливает для 2023–2025 годов. Сумму на 2026 год закон не называет: gestor считает 80 €, сверьте с TGSS.'),
         ['leta-38ter', 'reta-rdl13-2022-dt5'])}
<div class=band>Certificado censal AEAT</div>
{field(_('Дата certificado (Sede → Mis datos censales → Mis obligaciones)'), 'censo_date', s['censo_date'], type='date')}
{''.join(f'<label class=check><input type=checkbox name=censo_{k} value=1{" checked" if k in s["censo"] else ""}> {h(v)}</label>' for k, v in CENSO.items())}
{explain(_('Отметьте обязанности со статусом ALTA. gestor сравнит их со своим списком «Что вы подаёте» и покажет расхождения. '
           'Изменения в censo подаются через Modelo 036 в течение месяца.'), ['rgat-10'])}
<div class=band>{_('IVA и счета')}</div>
<label>{_('IVA a compensar на начало года: «год сумма»')}<textarea name=iva_carry rows=2 placeholder="2027 420,00">{h(year_amounts_text(s['iva_carry']))}</textarea></label>
{explain(_('Если в 303 за 4T вы не просили возврат, остаток переходит в следующий год (casilla 110).'), ['liva-99', 'liva-115'])}
{field(_('Формат номера счёта'), 'series', s['series'], placeholder='FACT-{YYYY}-{NNNNN}')}
{explain(_('{YYYY} — год, {NNNNN} — номер с нулями: FACT-{YYYY}-{NNNNN} даёт FACT-2026-00001. Просто буквы, например A, дают A2026-0001. '
           'Счета нумеруются по порядку, без пропусков и по датам. Исправительные — отдельная серия R.'), ['rd1619-6', 'rd1619-15'])}
{sl_band}
<button class=primary>{_('Сохранить и проверить выводы')}</button></form>"""
    return page(req, _("Профиль"), body)


def understood(req) -> str:
    """How gestor reads your answers: facts, duties with reasons, duties you don't have, and where gestor may be wrong."""
    s, y = req.s, date.today().year
    if not s["name"] or not (s["activity_start"] or s["reta_start"]):
        return f'<div class=band>{_("Как gestor вас понял")}</div><p>{_("Пока не понял: заполните анкету ниже и сохраните.")}</p>'
    reg = tax.regime(s, y)
    region = tax.region_for_year(s, y)
    first = str(s.get("beckham_first_year") or "")
    if reg == "beckham":
        regime_text = _("В {y} — режим Beckham: с {first} по {last} год включительно.").format(y=y, first=first, last=int(first) + 5)
    elif reg == "sl":
        regime_text = _("В {y} — налог на прибыль SL.").format(y=y)
    elif first.isdigit() and int(first) + 5 < y:
        regime_text = _("В {y} — общий IRPF, прибыль считается по estimación directa (режим Beckham закончился в {last}).").format(y=y, last=int(first) + 5)
    else:
        regime_text = _("В {y} — общий IRPF, прибыль считается по estimación directa.").format(y=y)
    activity = _("Деятельность профессиональная") if s["activity_kind"] == "profesional" else _("Деятельность предпринимательская")
    reta_base = _("{amount} в месяц").format(amount=fmt(s["reta_base"])) if s.get("reta_base") else _("минимальная")
    facts = [
        (_("Вы — {kind}, статус: {visa}.").format(kind="Sociedad Limitada" if s["kind"] == "sl" else "autónomo",
                                                 visa=_(rules.VISAS.get(s["visa"], s["visa"]))), "f-name"),
        (regime_text, "f-beckham_first_year"),
        (_("Налоговый регион {y}: {region} — там вы проводите больше дней.").format(y=y, region=_(rules.REGIONS[region])) if region else
         _("Регион не указан: региональная часть IRPF не посчитана."), "f-residence"),
        (activity + (_(", alta {d}").format(d=s["activity_start"]) if s["activity_start"] else "") + ".", "f-activity_start"),
        (_("RETA с {d}, база {base}").format(d=s["reta_start"], base=reta_base) + (_(", льготный взнос") if s.get("tarifa_plana") else "") + "."
         if s.get("reta_start") else _("В RETA не зарегистрированы."), "f-reta_start"),
    ]
    have, no = tax.duties(req.con, s, y)
    censo = []
    if s.get("censo_date"):
        mine = {d["modelo"] for d in have}
        for m in ("303", "130", "111", "115"):
            if m in mine and m not in s["censo"]:
                censo.append(_("gestor считает, что вы подаёте {m}, а в certificado censal от {d} этой обязанности нет: "
                               "сделайте alta через Modelo 036 или проверьте анкету.").format(m=m, d=s["censo_date"]))
            elif m in s["censo"] and m not in mine:
                censo.append(_("В certificado censal от {d} {m} в статусе ALTA, а gestor её не ждёт: "
                               "подавайте её или сделайте baja через Modelo 036.").format(m=m, d=s["censo_date"]))
        if "349" in mine and "roi" not in s["censo"]:
            censo.append(_("У вас операции с бизнесом из ЕС (349), а ROI в certificado censal не отмечен: проверьте alta в ROI через Modelo 036."))
    rows = "".join(f"<tr><td>{h(d['modelo'])}</td><td><b>{h(d['what'])}</b><small>{h(d['when'])}</small>"
                   f"<small>{h(_(tax.MODELO_ABOUT.get(d['modelo'], '')))}</small></td>"
                   f"<td>{explain(h(d['why']), d['ids'])}</td></tr>" for d in have)
    nots = "".join(f"<li><b>{h(d['modelo'])}</b>: {h(d['what'])}. {explain(h(d['why']), d['ids'])}</li>" for d in no)
    used = [i for d in have + no for i in d["ids"]]
    for __, fs in tax.forms(req.con, s, y):  # every rule behind your own numbers this year
        for f in fs:
            used += f["sources"] + [i for n in f.get("notes", []) if n for i in sources.split_cites(n)[1]]
            used += [i for b in f["boxes"] for i in tax.applicable(tax.BOX_SOURCES.get((f["modelo"], b[0]), []), s, y)]
    used += [i for w in tax.warnings(req.con, s, y) for i in sources.split_cites(w)[1]]
    doubts = [e for e in (sources.get(i) for i in dict.fromkeys(used)) if e and e.get("status") != "verified"]
    risky = "".join(f'<li><a href="/sources#{h(e["id"])}">§ {h(e["ref"])}</a> {badge(e)} — {h(i18n.src(e, "status_note"))}</li>'
                    for e in doubts)
    return f"""<div class=band id=understood>{_('Как gestor вас понял')}</div>
<ul class=understood>{''.join(f'<li>{h(t)} <a href="#{a}">{_("изменить")}</a></li>' for t, a in facts)}</ul>
{junction(str(y))}
<h2 id=duties>{_('Что вы подаёте в {y}').format(y=y)}</h2>
<p class=sub>{_('Каждая строка — вывод из анкеты и ваших счетов. Под причиной — закон, на котором держится вывод.')}</p>
<table class=duties><thead><tr><th>Modelo</th><th>{_('Что и когда')}</th><th>{_('Почему у вас')}</th></tr></thead><tbody>{rows}</tbody></table>
{''.join(f'<div class=warn>{explain(h(t), ["rgat-10"])}</div>' for t in censo)}
{f'<h2 id=not-filed>{_("Что вы не подаёте и почему")}</h2><ul class=why-not>{nots}</ul>' if nots else ''}
{f'<h2 id=doubts>{_("Где gestor может ошибаться в вашем случае")}</h2><p class=sub>{_("Здесь закон не говорит прямо. gestor выбрал осторожный вариант; при сомнении спросите asesor.")}</p><ul class=risky>{risky}</ul>' if risky else ''}"""


def create_entity(data_dir: Path, raw: str) -> str:
    """New profile = new database file; the name keeps only a-z 0-9 - _. Creating an existing one changes nothing."""
    name = re.sub(r"[^a-z0-9_-]", "", raw.lower())
    if not name:
        raise ValueError(_("имя профиля: латиница, цифры, - и _"))
    data_dir.mkdir(parents=True, exist_ok=True)
    db.connect(data_dir / f"{name}.db").close()
    return name


def entities(req):
    if req.method == "POST":
        raise Redirect("/settings", entity=create_entity(req.data_dir, req.form.get("name", "")))
    body = f"""<h1>{_('Профили')}</h1><p>{_('Каждый профиль — отдельная база: например, личный autónomo и SL.')}</p>
<ul>{''.join(f'<li>{h(e)}</li>' for e in req.entities)}</ul>
<form method=post class=grid>{field(_('Новый профиль (латиницей)'), 'name', placeholder='sl')}<button>{_('Создать')}</button></form>"""
    return page(req, _("Профили"), body)


def entity_use(req):
    name = req.form.get("entity", "")
    if name not in req.entities:
        raise ValueError(_("нет такого профиля"))
    raise Redirect("/", entity=name)


def lang_use(req):
    """Interface language for this profile: saved in its settings, so the MCP server answers in it too."""
    lang, back = req.form.get("lang", ""), req.form.get("back", "/")
    if lang not in i18n.LANGS:
        raise NotFound()
    db.save_settings(req.con, {"lang": lang})
    raise Redirect(back if back.startswith("/") and not back.startswith("//") else "/")


GUIDE_NAMES = {"303": N_("IVA за квартал"), "130": N_("Аванс IRPF"), "349": N_("Операции с ЕС"), "390": N_("Годовая сводка IVA"),
               "347": N_("Контрагенты > 3 005,06 €"), "100": N_("Renta (общий IRPF)"), "151": N_("Декларация режима Beckham"),
               "111": N_("Удержания IRPF"), "115": N_("Удержания с аренды"), "202": N_("Аванс налога SL"), "200": N_("Налог на прибыль SL")}


def guide(req):
    """How to file in the Sede, step by step — from the AEAT's own help for the web form (303 help, checked 08.10.2026)."""
    links = "".join(f'<tr id="{m}"><td>{m}</td><td>{h(_(n))}</td><td><a href="{h(SEDE[m])}" target=_blank rel=noopener>{_("Открыть в Sede ↗")}</a></td></tr>'
                    for m, n in GUIDE_NAMES.items())
    original = (f'<a href="https://sede.agenciatributaria.gob.es/Sede/ayuda/consultas-informaticas/presentacion-declaraciones-ayuda-tecnica/modelo-303.html"'
                f' target=_blank rel=noopener>{_("оригинал для 303")}</a>')
    body = f"""<h1>{_('Как подать декларацию')}</h1>
<p class=sub>{_('gestor считает цифры, а подаёте вы сами в Sede AEAT. Это занимает 10–15 минут. Шаги — по справке AEAT к веб-форме ({link}); у 130, 349, 111, 115, 390 и 347 форма устроена так же.').format(link=original)}</p>

<h2 id=access>{_('1. Вход')}</h2>
<p>{_('Войдите с Cl@ve или с электронным сертификатом. Сертификат FNMT выдают по NIE после личного визита с паспортом и TIE. Cl@ve подходит для всех деклараций autónomo; SL подаёт только с сертификатом представителя.')}</p>

<h2 id=open>{_('2. Откройте форму декларации')}</h2>
<p>{_('В Sede каждая декларация называется «Modelo» и номером: Modelo 303, Modelo 130. Ссылки ведут прямо на её страницу.')}</p>
<table class=list><thead><tr><th>Modelo</th><th>{_('Что это')}</th><th></th></tr></thead><tbody>{links}</tbody></table>

<h2 id=fill>{_('3. Заполните casillas')}</h2>
<ol>
<li>{_('Выберите «Nueva declaración», укажите год и период.')}</li>
<li>{_('Переносите числа из gestor один в один: номер в рамке gestor = номер casilla в форме. Для 303 часть полей заполнит сервис Pre303 — сверьте их с gestor. Для 130, 303, 349 и 151 вручную вводить не обязательно: скачайте в gestor «Файл для Sede» и загрузите его в форме кнопкой «Importar». Файл собран по официальному diseño de registro AEAT, но на настоящей Sede ещё не проверялся — сверьте casillas после загрузки.')}</li>
<li>{_('Нажмите «Validar declaración». Ошибки исправьте, предупреждения прочитайте: подать с ними можно.')}</li>
</ol>

<h2 id=pay>{_('4. Если есть сумма к уплате')}</h2>
<ul>
<li>{_('<b>Domiciliación</b> — AEAT спишет со счёта в последний день срока. Укажите IBAN. Выбрать её можно только до даты на несколько дней раньше срока подачи.')} {cite(['orden-domiciliacion', 'aeat-calendario-2026'])}</li>
<li>{_('<b>A ingresar</b> — заплатите сразу: кнопка «Realizar pago (NRC)», картой, Bizum или со счёта. NRC — 22 символа, это квитанция об оплате.')}</li>
</ul>

<h2 id=send>{_('5. Отправьте и сохраните justificante')}</h2>
<p>{_('«Presentar declaración» → «Firmar y enviar». Скачайте PDF-justificante: на нём CSV, дата и время приёма. <b>Подачу подтверждает только он.</b> NRC подтверждает лишь оплату; «Guardar», «Vista previa» и «Exportar» — не подача.')}</p>

<h2 id=mark>{_('6. Отметьте в gestor')}</h2>
<p>{_('На странице «Налоги» нажмите «Отметить поданным» и впишите сумму из justificante, дату и CSV. gestor сверит сумму со своим расчётом и учтёт поданный аванс в годовой декларации.')}</p>

<h2 id=fix>{_('Если ошиблись после подачи')}</h2>
<p>{_('Подаётся autoliquidación rectificativa — та же форма с отметкой об исправлении. Если доплата больше — подайте её сами до требования AEAT.')}
{cite(['lgt-120', 'riva-74bis', 'lgt-27'])}</p>

<h2 id=annual>{_('Годовые: Renta и 151')}</h2>
<p>{_('Обычная Renta (100) подаётся в Renta WEB в кампанию с апреля по 30 июня. Декларация режима Beckham (151) — отдельный сервис, не Renta WEB: Cl@ve или сертификат, «Firmar y enviar», justificante. В файле 151 из gestor нет пола, даты рождения, адреса и эпиграфа IAE: их форма попросит после «Importar».')} {cite(['orden-hfp-1338-2023'])}</p>

<h2 id=RETA>RETA</h2>
<p>{_('Взносы списываются каждый месяц сами. Базу меняют в <a href="{url}" target=_blank rel=noopener>Import@ss ↗</a>; уведомление о перерасчёте приходит туда же и в NOTESS.').format(url=h(SEDE['RETA']))} {cite(['rd2064-1995-45', 'rd2064-1995-46'])}</p>"""
    return page(req, _("Как подать"), body)


def sede_download(req, year, period, modelo):
    """Fixed-width file for «Importar» in the Sede web form (gestor/sede.py)."""
    if not req.s.get("tax_id"):
        raise ValueError(_("Укажите NIE/NIF в настройках: без него Sede не примет файл"))
    f = next((f for __, fs in tax.forms(req.con, req.s, year) for f in fs
              if f["modelo"] == str(modelo) and f["period"] == period and sede_file.available(f)), None) or _404()
    return ("application/octet-stream", sede_file.BUILDERS[f["modelo"]](req.s, f), sede_file.filename(req.s, f))


# ---------- routing ----------

def sources_page(req):
    """Справочник: every legal source gestor relies on, uncertain ones first."""
    allsrc = sorted(sources.SOURCES.values(), key=lambda e: (e["domain"], e.get("kind") == "practice", e["id"]))
    counts = {k: sum(1 for e in allsrc if e.get("status") == k) for k in sources.STATUS}
    doubtful = [e for e in allsrc if e.get("status") in ("disputed", "interpretation")]
    toc = " ".join(f'<a href="#d-{d}">{h(_(t))}</a>' for d, t in sources.DOMAINS.items() if any(e["domain"] == d for e in allsrc))
    card = lambda e: f'<article class=src id="{h(e["id"])}">{source_body(e)}</article>'
    body = "".join(
        f'<h2 id="d-{d}">{h(_(t))}</h2>' + "".join(card(e) for e in allsrc if e["domain"] == d)
        for d, t in sources.DOMAINS.items())
    risky = "".join(f'<li><a href="#{h(e["id"])}">{h(e.get("ref", e["id"]))}</a> — {h(i18n.src(e, "status_note") or i18n.src(e, "title"))}</li>'
                    for e in doubtful if e.get("status") == "disputed")
    stamp_text = lambda k: f'<span class="stamp {k}">{h(_(sources.STATUS[k]))}</span>'
    return page(req, _("Справочник"), f"""<h1>{_('Справочник')}</h1>
<p class=lead>{_('Каждая сумма и каждое правило в gestor ссылаются сюда (значок §). У каждого источника есть оригинал, перевод на русский, что это значит для вас и практика DGT и судов, если она есть. Это расчёт, а не консультация: спорные места помечены, и gestor в них выбирает осторожный вариант.')}</p>
<table class=trust><tbody>
<tr><td class=num>{len(allsrc)}</td><td>{_('<b>источников</b> — законы, регламенты, разъяснения AEAT и TGSS, ответы DGT и решения судов, на которых держатся расчёты gestor.')}</td></tr>
<tr><td class=num>{counts['verified']}</td><td>{stamp_text('verified')} {_('правило написано в тексте источника дословно — его можно проверить по испанской цитате в карточке.')}</td></tr>
<tr><td class=num>{counts['interpretation']}</td><td>{stamp_text('interpretation')} {_('одной фразы нет: gestor сложил вывод из нескольких норм (например, ставку RETA 31,5 % — из пяти ставок приказа). В карточке написано, как именно.')}</td></tr>
<tr><td class=num>{counts['disputed']}</td><td>{stamp_text('disputed')} {_('закон молчит или его применение к вам неоднозначно. gestor выбрал осторожный вариант; эти места собраны ниже, в «Где закон неясен».')}</td></tr>
</tbody></table>
<p class="small gaps">{toc}</p>
{f'<h2 id=unclear>{_("Где закон неясен")}</h2><ul class=risky>{risky}</ul>' if risky else ''}
{body}""")


ROUTES = [
    (r"/", dashboard),
    (r"/clients", clients), (r"/clients/(\d+)", client_edit),
    (r"/invoices", invoices), (r"/invoices/new", invoice_new), (r"/invoices/(\d+)", invoice_view),
    (r"/invoices/(\d+)/edit", invoice_edit), (r"/invoices/(\d+)/issue", invoice_issue), (r"/invoices/(\d+)/paid", invoice_paid),
    (r"/invoices/(\d+)/delete", invoice_delete), (r"/invoices/(\d+)/rectify", invoice_rectify),
    (r"/expenses", expenses), (r"/expenses/new", expense_new), (r"/expenses/(\d+)", expense_edit),
    (r"/expenses/(\d+)/delete", expense_delete), (r"/receipts/([^/]+)", receipt_file),
    (r"/taxes", taxes), (r"/filings", filing_mark), (r"/filings/unmark", filing_unmark),
    (r"/export/(\d{4})/(emitidas|recibidas)\.csv", export_csv),
    (r"/settings", settings), (r"/entities", entities), (r"/entities/use", entity_use), (r"/lang", lang_use), (r"/sources", sources_page),
    (r"/guide", guide), (r"/sede/(\d{4})/([1-4]T|0A)/(130|303|349|151)", sede_download),
]
POST_ONLY = {invoice_issue, invoice_paid, invoice_delete, invoice_rectify, expense_delete, filing_mark, filing_unmark, entity_use, lang_use}


def make_app(data_dir: Path):
    data_dir.mkdir(parents=True, exist_ok=True)

    def app(environ, start):
        path = environ.get("PATH_INFO") or "/"
        host = re.sub(r":\d+$", "", environ.get("HTTP_HOST", ""))
        if host not in LOOPBACK:  # DNS rebinding: a foreign name resolving to 127.0.0.1 must not read the books
            start("403 Forbidden", [("Content-Type", "text/plain; charset=utf-8")])
            return [b"gestor answers only on 127.0.0.1 / localhost"]
        if path.startswith("/static/"):
            p = STATIC / path.removeprefix("/static/")
            if p.resolve().parent == STATIC.resolve() and p.is_file():
                start("200 OK", [("Content-Type", mimetypes.guess_type(p.name)[0] or "application/octet-stream"),
                                 ("X-Content-Type-Options", "nosniff")])
                return [p.read_bytes()]
        req, token, ok = None, None, False
        try:
            origin = environ.get("HTTP_ORIGIN")
            if environ["REQUEST_METHOD"] == "POST" and origin is not None and origin != f"http://{environ.get('HTTP_HOST')}":
                raise NotFound()  # cross-site form post
            req = Request(environ, data_dir)
            req.con.execute("BEGIN")  # one transaction per request: a failure halfway leaves the books as they were
            token = i18n.current.set(req.lang)
            for pattern, fn in ROUTES:
                m = re.fullmatch(pattern, req.path)
                if m:
                    if fn in POST_ONLY and req.method != "POST":
                        raise NotFound()
                    args = [int(a) if a.isdigit() else a for a in m.groups()]
                    out = fn(req, *args)
                    break
            else:
                raise NotFound()
            ok = True
            if isinstance(out, Path):  # receipts: only inert types open in the browser; anything else is downloaded
                ctype = mimetypes.guess_type(out.name)[0] or "application/octet-stream"
                inline = ctype in INLINE_TYPES
                start("200 OK", [("Content-Type", ctype if inline else "application/octet-stream"),
                                 ("Content-Disposition", f'{"inline" if inline else "attachment"}; filename="{out.name}"'),
                                 ("X-Content-Type-Options", "nosniff")])
                return [out.read_bytes()]
            if isinstance(out, tuple):
                ctype, text, fname = out
                start("200 OK", [("Content-Type", ctype), ("Content-Disposition", f'attachment; filename="{fname}"')])
                return [text if isinstance(text, bytes) else text.encode()]
            start("200 OK", [("Content-Type", "text/html; charset=utf-8")])
            return [out.encode()]
        except Redirect as r:
            ok = True
            headers = [("Location", r.to)]
            if r.entity:
                headers.append(("Set-Cookie", f"entity={r.entity}; Path=/; SameSite=Lax"))
            start("303 See Other", headers)
            return [b""]
        except NotFound:
            start("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
            return [_("не найдено").encode()]
        except (ValueError, KeyError) as e:
            text = _("не заполнено поле {field}").format(field=e) if isinstance(e, KeyError) else str(e)
            msg = f"<h1>{_('Ошибка')}</h1><p class=warn>{h(text)}</p><p><a href='javascript:history.back()'>{_('← назад')}</a></p>"
            start("400 Bad Request", [("Content-Type", "text/html; charset=utf-8")])
            return [(page(req, _("Ошибка"), msg) if req else msg).encode()]
        finally:
            if req:
                if req.con.in_transaction:
                    req.con.execute("COMMIT" if ok else "ROLLBACK")
                req.con.close()
            if token:
                i18n.current.reset(token)

    return app
