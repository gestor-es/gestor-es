"""Money parsing/formatting, input validation and invoice amounts. All amounts are integer cents."""
import re
from datetime import date
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

from . import db
from .i18n import _


def parse_money(text: str) -> int:
    """'1.234,56' | '1234.56' | '1234,5' | '1.000' (mil) | '-10' -> cents. Last separator is the decimal one,
    except groups of exactly three digits, which are thousands (money never has 3 decimals)."""
    s = (text or "").strip().replace(" ", "").replace("€", "")
    if not s:
        return 0
    if re.fullmatch(r"-?\d{1,3}([.,]\d{3})+", s):
        s = re.sub(r"[.,]", "", s)
    elif "," in s and "." in s:
        dec = "," if s.rfind(",") > s.rfind(".") else "."
        s = s.replace("." if dec == "," else ",", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    return cents(num(s) * 100)


def num(text, default="0") -> Decimal:
    """Finite decimal from user input ('1,5' ok); rejects nan/inf/garbage."""
    try:
        d = Decimal((text or default).strip().replace(",", "."))
    except InvalidOperation:
        raise ValueError(_("не число: {text}").format(text=repr(text)))
    if not d.is_finite() or abs(d) >= 10 ** 12:
        raise ValueError(_("не число: {text}").format(text=repr(text)))
    return d


def iso_date(text: str) -> str:
    try:
        return date.fromisoformat(text).isoformat()
    except (TypeError, ValueError):
        raise ValueError(_("неверная дата: {text}").format(text=repr(text)))


def cents(x) -> int:
    """Round half up to integer cents (Spanish tax practice)."""
    return int(Decimal(str(x)).quantize(Decimal(1), rounding=ROUND_HALF_UP))


def pct(base: int, rate) -> int:
    return cents(Decimal(base) * Decimal(str(rate)) / 100)


def fmt(c: int | None) -> str:
    if c is None:
        return "—"
    whole, frac = divmod(abs(c), 100)
    return ("−" if c < 0 else "") + f"{whole:,}".replace(",", ".") + f",{frac:02d} €"


def fmt_num(c: int) -> str:
    """Plain decimal for form inputs: 1234.56"""
    return f"{c / 100:.2f}"


def line_total(l) -> int:
    return cents(Decimal(str(l["quantity"])) * l["unit_price_cents"])


def invoice_amounts(con, inv) -> dict:
    """Totals in invoice currency and in EUR. Cuota IVA in EUR is computed on the EUR base (art. 79.Once LIVA)."""
    base = sum(line_total(l) for l in db.invoice_lines(con, inv["id"]))
    vat = pct(base, inv["vat_rate"])
    irpf = pct(base, inv["irpf_rate"])
    fx = Decimal(str(inv["fx_rate"] or 1))
    base_eur = cents(Decimal(base) / fx)
    vat_eur = pct(base_eur, inv["vat_rate"])
    irpf_eur = pct(base_eur, inv["irpf_rate"])
    return {
        "base": base, "vat": vat, "irpf": irpf, "total": base + vat - irpf,
        "base_eur": base_eur, "vat_eur": vat_eur, "irpf_eur": irpf_eur,
        "total_eur": base_eur + vat_eur - irpf_eur,
    }


NUMBER_TOKEN = re.compile(r"\{(N{1,8})\}")


def series_key(template: str, year: str) -> str:
    """Settings template → per-invoice series key. 'FACT-{YYYY}-{NNNNN}' → 'FACT-2026-{NNNNN}'; a bare prefix 'A' keeps
    the old 'A2026' key (number printed as A2026-0001)."""
    return template.replace("{YYYY}", year) if NUMBER_TOKEN.search(template) else template + year


def invoice_number(inv) -> str:
    if not inv["number"]:
        return _("черновик")
    m = NUMBER_TOKEN.search(inv["series"])
    return (inv["series"][:m.start()] + f"{inv['number']:0{len(m.group(1))}d}" + inv["series"][m.end():] if m
            else f"{inv['series']}-{inv['number']:04d}")
