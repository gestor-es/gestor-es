"""Tax engine: IVA (303/349/390/347), IRPF (130/100), Beckham (151), RETA, SL (202/111/115/200), calendar.

Sources and reasoning for every number: kb/*.md. Amounts are integer cents.
"""
import json
from datetime import date, timedelta
from decimal import Decimal as D

from . import core, rules, sources
from .core import cents, fmt, pct
from .i18n import N_, _

# ---------- tables (kb/irpf-autonomo.md, kb/beckham.md, kb/reta.md, kb/sociedad-limitada.md) ----------

# (lower bound €, rate % [, published cuota fija]) — without a published cuota fija it is accumulated from lower brackets.
STATE_SCALE = [(0, "9.5"), (12450, "12"), (20200, "15"), (35200, "18.5"), (60000, "22.5"), (300000, "24.5")]
REGION_SCALES = {
    "valencia": {
        2025: [(0, "9"), (12000, "12"), (22000, "15"), (32000, "17.5"), (42000, "20"), (52000, "22.5"),
               (62000, "25"), (72000, "26.5"), (100000, "27.5"), (150000, "28.5"), (200000, "29.5")],
        2026: [(0, "8.8"), (12000, "11.7"), (22000, "14.6"), (32000, "17"), (42000, "19.4"), (52000, "21.9"),
               (62000, "24.4"), (72000, "26.1"), (100000, "27.35"), (150000, "28.35"), (200000, "29.35")],
        2027: [(0, "8.7"), (12000, "11.6"), (22000, "14.5"), (32000, "16.9"), (42000, "19.3"), (52000, "21.8"),
               (62000, "24.3"), (72000, "26"), (100000, "27.25"), (150000, "28.25"), (200000, "29.25")],
    },
    "asturias": {
        2025: [(0, "9", 0), (12450, "12", "1120.50"), ("17707.20", "14", "1751.36"), ("33007.20", "19.2", "3893.36"),
               ("53407.20", "21.5", "7810.16"), (70000, "22.5", "11377.62"), (90000, "25", "15877.62"),
               (175000, "26", "37127.62")],
    },
    "madrid": {  # art. 1 DLeg 1/2010 (Ley 13/2023), from 2023
        2025: [(0, "8.5", 0), ("13362.22", "10.7", "1135.79"), ("19004.63", "12.8", "1739.53"),
               ("35425.68", "17.4", "3841.42"), ("57320.40", "20.5", "7651.10")],
    },
    "cataluna": {  # art. 611-1 DLeg 1/2024 (Decreto-ley 5/2025), from 2025
        2025: [(0, "9.5"), (12500, "12.5"), (22000, "16"), (33000, "19"), (53000, "21.5"), (90000, "23.5"),
               (120000, "24.5"), (175000, "25.5")],
    },
    "andalucia": {  # art. 23 Ley 5/2021 (Decreto-ley 7/2022), from 2022
        2025: [(0, "9.5"), (13000, "12"), (21100, "15"), (35200, "18.5"), (60000, "22.5")],
    },
}
for _r in ("asturias", "madrid", "cataluna", "andalucia"):  # unchanged in 2026
    REGION_SCALES[_r][2026] = REGION_SCALES[_r][2025]
MINIMO_PERSONAL = {"state": 5550, "valencia": 6105, "asturias": 6105, "madrid": D("5956.65"), "cataluna": 5550,
                   "andalucia": 5790}  # 2025/2026, under 65

BECKHAM_GENERAL = [(0, "24"), (600000, "47")]
GDJ_RATE, GDJ_CAP = D("0.05"), 2000_00  # gastos de difícil justificación, 2025/2026

# RETA: (upper bound of monthly R, base mín, base máx) — same bounds 2025/2026, kb/reta.md
RETA_TRAMOS = [
    ("R1", 670, "653.59", "718.94"), ("R2", 900, "718.95", "900"), ("R3", "1166.69", "849.67", "1166.70"),
    ("G1", 1300, "950.98", "1300"), ("G2", 1500, "960.78", "1500"), ("G3", 1700, "960.78", "1700"),
    ("G4", 1850, "1143.79", "1850"), ("G5", 2030, "1209.15", "2030"), ("G6", 2330, "1274.51", "2330"),
    ("G7", 2760, "1356.21", "2760"), ("G8", 3190, "1437.91", "3190"), ("G9", 3620, "1519.61", "3620"),
    ("G10", 4050, "1601.31", "4050"), ("G11", 6000, "1732.03", None), ("G12", None, "1928.10", None),
]
RETA_MAX_BASE = {2025: "4909.50", 2026: "5101.20"}
RETA_RATE = {2025: D("31.4"), 2026: D("31.5")}
RETA_MEI = {2025: D("0.8"), 2026: D("0.9")}
RETA_SOCIETARIO_MIN = {2025: "1000", 2026: "1424.40"}
TARIFA_PLANA = 80_00

# SL Impuesto sobre Sociedades (kb/sociedad-limitada.md)
IS_GENERAL = D("25")


def _known(table: dict, year: int):
    """Latest table not newer than `year` (falls back to the most recent known)."""
    ys = sorted(table)
    best = [y for y in ys if y <= year]
    return table[best[-1] if best else ys[0]], (year in table)


def scale(base_cents: int, brackets) -> int:
    """Progressive tax: cuota fija of the bracket + (base − lower) × rate, rounded once."""
    if base_cents <= 0:
        return 0
    b = D(base_cents) / 100
    fixed, prev = D(0), None
    for lo, rate, *published in brackets:
        lo = D(str(lo))
        if prev and b < lo:
            break
        if prev:
            fixed += (lo - prev[0]) * prev[1] / 100
        if published:
            fixed = D(str(published[0]))
        prev = (lo, D(rate))
    return cents((fixed + (b - prev[0]) * prev[1] / 100) * 100)


# ---------- profile ----------

def regime(s: dict, year: int) -> str:
    if s["kind"] == "sl":
        return "sl"
    first = str(s.get("beckham_first_year") or "")
    if first.isdigit() and int(first) <= year <= int(first) + 5:
        return "beckham"
    return "general"


def regime_label(s, year) -> str:
    return _({"sl": "Sociedad Limitada", "beckham": "autónomo, Beckham",
              "general": N_("autónomo, общий IRPF")}[regime(s, year)])


def region_for_year(s: dict, year: int) -> str | None:
    """Art. 72 LIRPF: the region where you spent most days of the year."""
    res = sorted(s.get("residence") or [], key=lambda r: r["from"])
    if not res:
        return None
    days = {}
    start, end = date(year, 1, 1), date(year, 12, 31)
    for i, r in enumerate(res):
        a = max(date.fromisoformat(r["from"]), start)
        b = min(date.fromisoformat(res[i + 1]["from"]) - timedelta(days=1) if i + 1 < len(res) else end, end)
        if b >= a:
            days[r["region"]] = days.get(r["region"], 0) + (b - a).days + 1
    if not days:
        return res[0]["region"] if date.fromisoformat(res[0]["from"]) > end else res[-1]["region"]
    return max(days, key=days.get)


def quarter_of(iso: str) -> int:
    return (int(iso[5:7]) - 1) // 3 + 1


def quarter_end(year, q) -> date:
    return date(year, 3 * q, 31 if q in (1, 4) else 30)


# ---------- ledger ----------

def sales(con, year: int) -> list[dict]:
    """Issued invoices of the year (by operation date), amounts in EUR, client as frozen on issue."""
    out = []
    for inv in con.execute("""SELECT i.*, c.name AS cname, c.tax_id AS ctax, c.country AS ccountry
                              FROM invoices i JOIN clients c ON c.id = i.client_id
                              WHERE i.number IS NOT NULL AND substr(coalesce(i.operation_date, i.issue_date), 1, 4) = ?""",
                           (str(year),)):
        a = core.invoice_amounts(con, inv)
        d = inv["operation_date"] or inv["issue_date"]
        c = json.loads(inv["parties"])["client"] if inv["parties"] else \
            {"name": inv["cname"], "tax_id": inv["ctax"], "country": inv["ccountry"]}
        out.append({"date": d, "q": quarter_of(d), "treatment": inv["treatment"], "vat_rate": inv["vat_rate"],
                    "base": a["base_eur"], "vat": a["vat_eur"], "irpf": a["irpf_eur"], "total": a["total_eur"] + a["irpf_eur"],
                    "rect": inv["rectifies_id"] is not None, "client": c["name"], "tax_id": c["tax_id"], "country": c["country"]})
    return out


def purchases(con, year: int) -> list:
    return con.execute("SELECT * FROM expenses WHERE substr(date, 1, 4) = ? ORDER BY date", (str(year),)).fetchall()


def is_asset(e) -> bool:
    """Equipment over 300 € per unit is amortized, not expensed at once."""
    return e["category"] == "equipment" and e["base_cents"] > 300_00


def is_vat_investment(e) -> bool:
    """Bien de inversión for IVA: equipment ≥ 3 005,06 € (art. 108 LIVA); services never."""
    return e["category"] == "equipment" and e["base_cents"] >= 3005_06


def amort_rate(s) -> D:
    """Computers: 26 % autónomo (tabla simplificada, group 5), 25 % SL (art. 12.1 LIS)."""
    return D("0.25") if s["kind"] == "sl" else D("0.26")


def _nondeductible_vat(e) -> int:
    if e["vat_kind"] == "none":
        return 0
    return e["vat_cents"] - pct(e["vat_cents"], e["vat_deductible_pct"])


def _cost(e) -> int:
    return pct(e["base_cents"] + _nondeductible_vat(e), e["deductible_pct"])


def expense_deductible(e, rate=D("0.26")) -> int:
    """Income-tax deductible amount of an expense in its own year; assets: that year's amortization."""
    if not is_asset(e):
        return _cost(e)
    return amortization(_cost(e), date.fromisoformat(e["date"]), int(e["date"][:4]), rate=rate)


def amortization(cost: int, start: date, year: int, upto: date | None = None, rate=D("0.26")) -> int:
    """Linear amortization accrued in `year` (until `upto`), never above remaining cost."""
    ys, ye = date(year, 1, 1), upto or date(year, 12, 31)
    days_year = (date(year, 12, 31) - ys).days + 1
    done = 0
    for y in range(start.year, year):
        a = max(start, date(y, 1, 1))
        dy = (date(y, 12, 31) - date(y, 1, 1)).days + 1
        done += cents(D(cost) * rate * ((date(y, 12, 31) - a).days + 1) / dy)
    a = max(start, ys)
    if ye < a:
        return 0
    this = cents(D(cost) * rate * ((ye - a).days + 1) / days_year)
    return max(0, min(this, cost - done))


def expense_vat_deductible(e) -> int:
    return 0 if e["vat_kind"] == "none" else pct(e["vat_cents"], e["vat_deductible_pct"])


HEALTH_CAP = 500_00  # seguro de enfermedad of the autónomo, per year (art. 30.2.5ª LIRPF)


def income_tax_expenses(con, year: int, upto: date, rate=D("0.26")) -> dict:
    """Deductible expenses for IRPF/IS from Jan 1 to `upto`, incl. amortization of assets bought earlier."""
    reta = other = amort = health = 0
    for e in con.execute("SELECT * FROM expenses WHERE date <= ? AND (substr(date, 1, 4) = ? OR category = 'equipment')",
                         (upto.isoformat(), str(year))):
        if is_asset(e):
            amort += amortization(_cost(e), date.fromisoformat(e["date"]), year, upto, rate)
        elif e["date"][:4] == str(year):
            v = _cost(e)
            if e["category"] == "reta":
                reta += v
            elif e["category"] == "health":
                health += v
            else:
                other += v
    other += min(health, HEALTH_CAP)
    return {"reta": reta, "other": other, "amort": amort, "total": reta + other + amort}


# ---------- IVA ----------

def form_303(con, year: int, q: int, carry_in: int, refund_4t=True) -> tuple[dict, int]:
    """Returns (form, carry_out). carry_in = cuotas a compensar from previous periods (casilla 110).
    4T with a negative result: refund (casilla 73) unless refund_4t is False (carry into next year)."""
    c = {k: 0 for k in ("01", "03", "04", "06", "07", "09", "10", "11", "12", "13", "14", "15", "28", "29", "30", "31",
                        "36", "37", "38", "39", "59", "120", "123")}
    for sl in (x for x in sales(con, year) if x["q"] == q):
        t = sl["treatment"]
        if t == "eu_b2b":
            c["59"] += sl["base"]
        elif t == "extra_eu":
            c["120"] += sl["base"]
        elif sl["rect"] and sl["vat"]:
            c["14"] += sl["base"]
            c["15"] += sl["vat"]
        else:
            key = {21: ("07", "09"), 10: ("04", "06"), 4: ("01", "03")}.get(int(sl["vat_rate"]))
            if key:
                c[key[0]] += sl["base"]
                c[key[1]] += sl["vat"]
    by_rate = {}  # (303 base casilla, IVA %) -> [base, cuota, cuota deducible]: the 390 splits these by rate
    for e in (x for x in purchases(con, year) if quarter_of(x["date"]) == q):
        ded = expense_vat_deductible(e)
        inv = is_vat_investment(e)
        base = e["base_cents"]  # full base; only the cuota is limited by the deductible share (kb/iva-facturacion.md §5)
        if e["vat_kind"] == "reverse_eu":
            c["10"] += base
            c["11"] += e["vat_cents"]
            k = "38" if inv else "36"
        elif e["vat_kind"] == "reverse_non_eu":
            c["12"] += base
            c["13"] += e["vat_cents"]
            k = "30" if inv else "28"
        elif e["vat_kind"] == "domestic" and ded:
            k = "30" if inv else "28"
        else:
            continue
        c[k] += base
        c[str(int(k) + 1)] += ded  # the cuota casilla follows its base: 28/29, 30/31, 36/37, 38/39
        r = by_rate.setdefault((k, e["vat_rate"]), [0, 0, 0])
        r[0] += base
        r[1] += e["vat_cents"]
        r[2] += ded
    c["27"] = c["03"] + c["06"] + c["09"] + c["11"] + c["13"] + c["15"]
    c["45"] = c["29"] + c["31"] + c["37"] + c["39"]
    c["46"] = c["27"] - c["45"]
    c["64"] = c["66"] = c["46"]
    c["110"] = carry_in
    c["78"] = carry_in if q == 4 and refund_4t else min(carry_in, max(c["66"], 0))
    c["87"] = carry_in - c["78"]
    c["69"] = c["71"] = c["66"] - c["78"]
    notes = []
    if c["71"] < 0 and q < 4:
        carry_out = c["87"] - c["71"]
        notes.append(_("A compensar: {amount} переносится в следующий квартал (casilla 72). [[liva-99]]").format(amount=fmt(-c['71'])))
    elif c["71"] < 0 and refund_4t:
        carry_out = 0
        notes.append(_("4T: возврат {amount} (casilla 73, придёт в течение ~6 месяцев). Если хотите перенести "
                       "a compensar на следующий год — укажите сумму в настройках («IVA a compensar на начало года»). [[liva-115]]")
                     .format(amount=fmt(-c['71'])))
    elif c["71"] < 0:
        carry_out = c["87"] - c["71"]
        notes.append(_("4T: {amount} переносится a compensar на следующий год (casilla 72). [[liva-99]]").format(amount=fmt(carry_out)))
    else:
        carry_out = c["87"]
    if c["59"]:
        notes.append(_("Есть услуги клиентам ЕС (casilla 59): нужен ROI (036, casilla 582) и Modelo 349, clave S. [[liva-69,riva-79]]"))
    if c["10"]:
        notes.append(_("Покупки услуг у поставщиков ЕС (autorrepercusión, casillas 10/11 и 36/37) — также в 349, clave I. [[liva-84,riva-79]]"))
    if not any(c[k] for k in c if k not in ("110", "78", "87")) and not carry_in:
        notes.append(_("Нет операций: подаётся «sin actividad». [[riva-71]]"))
    labels = [("01", "Régimen general 4 %: Base imponible"), ("03", "Régimen general 4 %: Cuota"),
              ("04", "Régimen general 10 %: Base imponible"), ("06", "Régimen general 10 %: Cuota"),
              ("07", "Régimen general 21 %: Base imponible"), ("09", "Régimen general 21 %: Cuota"),
              ("10", "Adquisiciones intracomunitarias de bienes y servicios: Base imponible"),
              ("11", "Adquisiciones intracomunitarias de bienes y servicios: Cuota"),
              ("12", _("Otras operaciones con inversión del sujeto pasivo (excepto adq. intracom.): Base imponible (поставщики вне ЕС)")),
              ("13", "Otras operaciones con inversión del sujeto pasivo (excepto adq. intracom.): Cuota"),
              ("14", "Modificación bases y cuotas: Base imponible"), ("15", "Modificación bases y cuotas: Cuota"),
              ("27", "Total cuota devengada"),
              ("28", "Por cuotas soportadas en operaciones interiores corrientes: Base"),
              ("29", "Por cuotas soportadas en operaciones interiores corrientes: Cuota"),
              ("30", "Por cuotas soportadas en operaciones interiores con bienes de inversión: Base"),
              ("31", "Por cuotas soportadas en operaciones interiores con bienes de inversión: Cuota"),
              ("36", "En adquisiciones intracomunitarias de bienes y servicios corrientes: Base"),
              ("37", "En adquisiciones intracomunitarias de bienes y servicios corrientes: Cuota"),
              ("38", "En adquisiciones intracomunitarias de bienes de inversión: Base"),
              ("39", "En adquisiciones intracomunitarias de bienes de inversión: Cuota"),
              ("45", "Total a deducir"), ("46", "Resultado régimen general"), ("59", "Entregas intracomunitarias de bienes y servicios"),
              ("120", "Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 123)"),
              ("66", "Atribuible a la Administración del Estado"),
              ("110", "Cuotas a compensar pendientes de periodos anteriores"),
              ("78", "Cuotas a compensar de periodos anteriores aplicadas en este periodo"),
              ("87", "Cuotas a compensar de periodos previos pendientes para periodos posteriores"), ("71", "Resultado")]
    boxes = [(k, l, c[k]) for k, l in labels if c[k] or k in ("27", "45", "46", "71")]
    return {"modelo": "303", "title": f"IVA {q}T", "boxes": boxes, "result": c["71"], "notes": notes, "c": c,
            "by_rate": by_rate, "carry_out": carry_out}, carry_out


def iva_year(con, s, year):
    forms, carry = [], int((s.get("iva_carry") or {}).get(str(year), 0))
    keep = bool((s.get("iva_carry") or {}).get(str(year + 1)))
    for q in range(1, 5):
        f, carry = form_303(con, year, q, carry, refund_4t=not keep)
        forms.append(f)
    return forms


def _eu_services_by_quarter(con, year) -> dict:
    out = {}
    for y in (year - 1, year):
        for sl in sales(con, y):
            if sl["treatment"] == "eu_b2b":
                out[(y, sl["q"])] = out.get((y, sl["q"]), 0) + sl["base"]
    return out


def form_349(con, year, q):
    rows, who, rect = {}, {}, False
    for sl in sales(con, year):
        if sl["q"] == q and sl["treatment"] == "eu_b2b":
            k = (sl["tax_id"] or sl["client"], "S")
            rows[k] = rows.get(k, 0) + sl["base"]
            who[k] = (sl["country"], sl["client"])
            rect |= sl["rect"]
    for e in purchases(con, year):
        if quarter_of(e["date"]) == q and e["vat_kind"] == "reverse_eu":
            k = (e["supplier_tax_id"] or e["supplier"], "I")
            rows[k] = rows.get(k, 0) + e["base_cents"]
            who[k] = ("", e["supplier"])  # suppliers have no country field: the VAT number's prefix gives it
    if not rows:
        return None
    boxes = [(clave, nif, v) for (nif, clave), v in sorted(rows.items(), key=lambda x: x[0][1])]
    notes = [_("NIF-IVA контрагента — без префикса страны.")]
    by_q = _eu_services_by_quarter(con, year)
    window = [(year, q)] + [((year * 4 + q - 1 - i - 1) // 4, (q - 1 - i - 1) % 4 + 1) for i in range(4)]
    if any(by_q.get(k, 0) > 50000_00 for k in window):
        notes.insert(0, _("Услуги клиентам ЕС > 50 000 € за квартал (текущий или один из 4 предыдущих): 349 подаётся ПОМЕСЯЧНО, "
                          "до 20 числа следующего месяца. Разбейте эти суммы по месяцам. [[riva-81]]"))
    if rect:
        notes.append(_("Есть rectificativa: если она исправляет счёт прошлого периода, в 349 это отдельная запись rectificación "
                       "с периодом и суммой исходной декларации, а не уменьшение текущего периода. [[riva-79]]"))
    return {"modelo": "349", "title": f"Operaciones intracomunitarias {q}T", "boxes": boxes,
            "result": sum(v for *_, v in boxes), "result_label": _("Сумма операций"), "notes": notes,
            "ops": [(clave, nif, *who[(nif, clave)], v) for clave, nif, v in boxes]}


def form_347(con, year):
    """Counterparties over 3 005,06 € (IVA included), excluding 349 operations and those with retención."""
    agg = {}
    for sl in sales(con, year):
        if sl["treatment"] == "eu_b2b" or sl["irpf"]:
            continue
        k = ("B ventas", sl["tax_id"] or sl["client"])
        agg[k] = agg.get(k, 0) + sl["total"]
    for e in purchases(con, year):
        if e["vat_kind"] == "reverse_eu" or e["withheld_cents"] or e["category"] in ("reta", "taxes", "personal", "admin_pay"):
            continue
        k = ("A compras", e["supplier_tax_id"] or e["supplier"])
        agg[k] = agg.get(k, 0) + e["base_cents"] + (e["vat_cents"] if e["vat_kind"] == "domestic" else 0)
    rows = [(k[0], k[1], v) for k, v in agg.items() if v > 3005_06]
    if not rows:
        return None
    return {"modelo": "347", "title": "Operaciones con terceros > 3 005,06 €", "boxes": rows, "result": sum(r[2] for r in rows),
            "result_label": _("Сумма"), "notes": [
                _("Клиенты и поставщики вне ЕС включены осторожно: art. 33 RGAT исключает только импорт и экспорт товаров. [[rgat-33]]"),
                _("Нужна разбивка по кварталам и NIF каждого контрагента — переносится из книг.")]}


# Modelo 390 casillas by IVA rate: AEAT diseño de registro DR390 2025 and the form in the IVA manual [[aeat-390-dr-2025]].
F390_SALES = ((4, "01", "02", "01", "03"), (10, "03", "04", "04", "06"), (21, "05", "06", "07", "09"))  # rate, 390 base/cuota, 303 base/cuota
F390_DEV = {  # 303 base casilla of an intra-EU purchase -> 390 IVA devengado: label, {rate: (base, cuota)}
    "38": ("Adquisiciones intracomunitarias de bienes", {4: ("21", "22"), 10: ("23", "24"), 21: ("25", "26")}),  # bien de inversión = goods
    "36": ("Adquisiciones intracomunitarias de servicios", {4: ("545", "546"), 10: ("547", "548"), 21: ("551", "552")}),
}
F390_DED = {  # 303 base casilla -> 390 IVA deducible: label, {rate: (base, cuota)}, total label, total (base, cuota)
    "28": ("IVA deducible en operaciones interiores de bienes y servicios corrientes", {4: ("190", "191"), 10: ("603", "604"), 21: ("605", "606")},
           "Total bases imponibles y cuotas deducibles en operaciones interiores de bienes y servicios corrientes", ("48", "49")),
    "30": ("IVA deducible en operaciones interiores de bienes de inversión", {4: ("196", "197"), 10: ("611", "612"), 21: ("613", "614")},
           "Total bases imponibles y cuotas deducibles en operaciones interiores de bienes de inversión", ("50", "51")),
    "38": ("IVA deducible en adquisiciones intracomunitarias de bienes de inversión", {4: ("220", "221"), 10: ("631", "632"), 21: ("633", "634")},
           "Total bases imponibles y cuotas deducibles en adquisiciones intracomunitarias de bienes de inversión", ("58", "59")),
    "36": ("IVA deducible en adquisiciones intracomunitarias de servicios", {4: ("587", "588"), 10: ("635", "636"), 21: ("637", "638")},
           "Total bases imponibles y cuotas deducibles en adquisiciones intracomunitarias de servicios", ("597", "598")),
}


def form_390(con, year, iva_forms):
    tot, by_rate = {}, {}
    for f in iva_forms:
        for k, v in f["c"].items():
            tot[k] = tot.get(k, 0) + v
        for k, v in f["by_rate"].items():
            by_rate[k] = [a + b for a, b in zip(by_rate.get(k, (0, 0, 0)), v)]
    first, last = iva_forms[0]["c"], iva_forms[-1]
    pos = sum(max(f["result"], 0) for f in iva_forms)
    applied_prev = min(first["110"], sum(f["c"]["78"] for f in iva_forms))
    neg = max(-last["result"], 0)
    refunded = neg and not last["carry_out"]
    domestic = tot["07"] + tot["04"] + tot["01"] + tot["14"]
    boxes = []
    for r, b, cu, b303, cu303 in F390_SALES:
        boxes += [(b, f"Régimen ordinario {r} %: Base imponible", tot[b303]), (cu, f"Régimen ordinario {r} %: Cuota devengada", tot[cu303])]
    for k, (label, by) in F390_DEV.items():
        for r, (b, cu) in by.items():
            v = by_rate.get((k, r), (0, 0, 0))
            boxes += [(b, f"{label} {r} %: Base imponible", v[0]), (cu, f"{label} {r} %: Cuota devengada", v[1])]
    boxes += [("27", _("IVA devengado en otros supuestos de inversión del sujeto pasivo: Base imponible (вне ЕС)"), tot["12"]),
              ("28", "IVA devengado en otros supuestos de inversión del sujeto pasivo: Cuota devengada", tot["13"]),
              ("29", "Modificación de bases y cuotas: Base imponible", tot["14"]), ("30", "Modificación de bases y cuotas: Cuota devengada", tot["15"]),
              ("33", "Total bases y cuotas IVA: Base imponible", tot["01"] + tot["04"] + tot["07"] + tot["10"] + tot["12"] + tot["14"]),
              ("34", "Total bases y cuotas IVA: Cuota devengada", tot["27"]),
              ("47", "Total cuotas IVA y recargo de equivalencia", tot["27"])]
    for k, (label, by, total, (tb, tc)) in F390_DED.items():
        for r, (b, cu) in by.items():
            v = by_rate.get((k, r), (0, 0, 0))
            boxes += [(b, f"{label} {r} %: Base imponible", v[0]), (cu, f"{label} {r} %: Cuota deducible", v[2])]
        boxes += [(tb, f"{total}: Base imponible", tot[k]), (tc, f"{total}: Cuota deducible", tot[str(int(k) + 1)])]
    boxes += [("64", "Suma de deducciones", tot["45"]), ("65", "Resultado régimen general", tot["46"]),
              ("84", "Suma de resultados", tot["46"]), ("85", "Compensación de cuotas del ejercicio anterior", applied_prev),
              ("86", "Resultado de la liquidación", tot["46"] - applied_prev),
              ("95", "Total resultados a ingresar en las autoliquidaciones de IVA del ejercicio", pos),
              ("97", "A compensar", 0 if refunded else neg), ("98", "A devolver", neg if refunded else 0),
              ("662", "Cuotas pendientes de compensación generadas en el ejercicio y distintas de las incluidas en la casilla 97", last["c"]["87"]),
              ("99", "Operaciones en régimen general", domestic),
              ("103", "Entregas intracomunitarias de bienes y servicios", tot["59"]),
              ("110", "Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 126)", tot["120"]),
              ("108", "Total volumen de operaciones (Art. 121 Ley IVA)", domestic + tot["59"] + tot["120"])]
    notes = []
    if any(r not in (4, 10, 21) and any(v) for (_k, r), v in by_rate.items()):
        notes.append(_("Есть покупки по ставке IVA не 4, 10 или 21 %: в итоговые casillas они вошли, а строки по их ставке "
                       "заполните в форме 390 сами. [[aeat-390-dr-2025]]"))
    return {"modelo": "390", "title": "Resumen anual IVA", "result": tot["46"], "result_label": _("IVA за год"), "notes": notes,
            "boxes": [b for b in boxes if b[2] or b[0] in ("34", "47", "64", "65", "84", "86", "108")]}


# ---------- IRPF general (130 / 100) ----------

def net_ytd(con, year, upto: date) -> dict:
    income = sum(x["base"] for x in sales(con, year) if x["date"] <= upto.isoformat())
    withheld = sum(x["irpf"] for x in sales(con, year) if x["date"] <= upto.isoformat())
    exp = income_tax_expenses(con, year, upto)
    p = income - exp["total"]
    gdj = min(GDJ_CAP, cents(GDJ_RATE * max(p, 0)))
    return {"income": income, "withheld": withheld, "exp": exp, "p": p, "gdj": gdj, "rn": p - gdj}


def low_income_reduction(con, s, year) -> int:
    """130 casilla 13: reduction per quarter by previous-year net (art. 110.3.c RIRPF).
    Unknown previous year (no data in the service) → 0: overpaying an advance is refunded in Modelo 100."""
    start = s.get("activity_start") or ""
    if start and int(start[:4]) >= year:
        return 100_00  # no previous-year activity
    if regime(s, year - 1) != "general" or not sales(con, year - 1):
        return 0
    rn = net_ytd(con, year - 1, date(year - 1, 12, 31))["rn"]
    for limit, red in ((9000_00, 100_00), (10000_00, 75_00), (11000_00, 50_00), (12000_00, 25_00)):
        if rn <= limit:
            return red
    return 0


def exempt_from_130(con, s, year) -> bool:
    """Profesional with ≥70 % of previous-year income subject to retención (art. 109.2 RIRPF).
    First year (no previous-year data): not exempt — check the quarter yourself."""
    if s.get("activity_kind") == "empresarial":
        return False
    prev = sales(con, year - 1)
    inc = sum(x["base"] for x in prev)
    return inc > 0 and sum(x["base"] for x in prev if x["irpf"]) * 10 >= inc * 7


def forms_130(con, s, year) -> list:
    out, prev7, neg19 = [], 0, 0
    red = low_income_reduction(con, s, year)
    for q in range(1, 5):
        n = net_ytd(con, year, quarter_end(year, q))
        c01, c02 = n["income"], n["exp"]["total"] + n["gdj"]
        c03 = c01 - c02
        c04 = cents(D(max(c03, 0)) * D("0.2"))
        c05 = prev7
        c06 = n["withheld"]
        c07 = c04 - c05 - c06
        c12 = max(c07, 0)
        c13 = red
        c14 = c12 - c13
        c15 = min(max(c14, 0), neg19)
        c17 = c19 = c14 - c15
        neg19 = neg19 - c15 + (-c19 if c19 < 0 and q < 4 else 0)
        prev7 += max(c07, 0)
        notes = []
        if c19 < 0:
            notes.append(_("Отрицательный результат: Q1–Q3 — a deducir в следующих кварталах; Q4 — negativa. Возврат — только через Modelo 100. [[rirpf-110]]"))
        out.append({"modelo": "130", "title": f"Pago fraccionado IRPF {q}T", "result": c19, "notes": notes, "boxes": [
            ("01", _("Ingresos computables correspondientes al conjunto de las actividades ejercidas (с 1 января)"), c01),
            ("02", _("Gastos fiscalmente deducibles correspondientes al conjunto de las actividades ejercidas (вкл. RETA, amortización, 5 % GDJ)"), c02),
            ("03", "Rendimiento neto", c03), ("04", "20 por 100 del importe de la casilla 03", c04),
            ("05", "A deducir: De los trimestres anteriores", c05),
            ("06", _("Retenciones e ingresos a cuenta soportados (с 1 января)"), c06), ("07", "Pago fraccionado previo del trimestre", c07),
            ("12", "Suma de pagos fraccionados previos del trimestre", c12),
            ("13", "Minoración por aplicación de la deducción a que se refiere el artículo 110.3 c) del Reglamento del Impuesto", c13),
            ("14", "Diferencia", c14), ("15", "Resultados negativos de trimestres anteriores", c15),
            ("19", "Resultado de la autoliquidación", c19)]})
    return out


def irpf_annual(con, s, year, paid_130: int, projected_130: int = 0) -> dict:
    """paid_130: advances actually filed (filings table); projected_130: computed but not yet filed."""
    n = net_ytd(con, year, date(year, 12, 31))
    region = region_for_year(s, year) or "valencia"
    notes = []
    first = str(s.get("inicio_first_year") or "")
    inicio = 0
    if first.isdigit() and year in (int(first), int(first) + 1) and n["rn"] > 0:
        inicio = cents(D(min(n["rn"], 100000_00)) * D("0.2"))
        notes.append(_("Reducción inicio 20 % (art. 32.3 LIRPF): первый год с положительным доходом и следующий за ним. [[lirpf-32]]"))
    elif not first and (s.get("activity_start") or "0")[:4] >= str(year - 1):
        notes.append(_("Новая деятельность: возможно, положена reducción 20 % (art. 32.3). Если в прошлом году не было другой "
                       "деятельности и > 50 % дохода не от бывшего работодателя — укажите первый прибыльный год в настройках. [[lirpf-32]]"))
    base = max(n["rn"] - inicio, 0)
    st_full, st_min = scale(base, STATE_SCALE), scale(min(base, MINIMO_PERSONAL["state"] * 100), STATE_SCALE)
    if region in REGION_SCALES:
        rscale, exact = _known(REGION_SCALES[region], year)
        rmin = MINIMO_PERSONAL[region]
        if not exact:
            notes.append(_("Шкала {region} за {year} не опубликована — взята последняя известная.")
                         .format(region=_(rules.REGIONS[region]), year=year))
    else:
        rscale, rmin = STATE_SCALE, MINIMO_PERSONAL["state"]
        notes.append(_("Регион без своей таблицы: региональная часть посчитана по государственной шкале (приблизительно)."))
    rg_full, rg_min = scale(base, rscale), scale(min(base, rmin * 100), rscale)
    cuota_st, cuota_rg = st_full - st_min, rg_full - rg_min
    total = cuota_st + cuota_rg
    result = total - n["withheld"] - paid_130
    if projected_130:
        notes.insert(0, _("Учтены только поданные 130 ({paid}). Ещё не поданы: {projected} — "
                          "после их уплаты доплата уменьшится на эту сумму.").format(paid=fmt(paid_130), projected=fmt(projected_130)))
    notes += [_("Регион за {year}: {region} (art. 72 LIRPF — где больше дней). [[lirpf-72]]")
              .format(year=year, region=_(rules.REGIONS.get(region, region))),
              _("Расчёт для одиночки до 65 лет без детей и без иных доходов. Дети, ипотека, сбережения, региональные вычеты "
                "(аренда жилья в Valencia/Asturias и т.п.) — добавить в Renta WEB."),
              _("Подача: Renta WEB (Modelo 100), апрель — 30 июня следующего года.")]
    return {"modelo": "100", "title": _("Renta {year} (оценка)").format(year=year), "result": result, "notes": notes, "boxes": [
        ("0180", "Total ingresos computables", n["income"]), ("0186", "Seguridad Social del titular de la actividad", n["exp"]["reta"]),
        ("0208", "Dotaciones del ejercicio para amortización de inmovilizado material", n["exp"]["amort"]),
        ("0218", _("Gastos fiscalmente deducibles: Suma (вкл. RETA)"), n["exp"]["total"]),
        ("0222", "Conjunto de provisiones deducibles y gastos de difícil justificación: 5 % (≤ 2 000 €)", n["gdj"]),
        ("0224", "Rendimiento neto", n["rn"]),
        ("0234", "Reducción por inicio de una actividad económica", inicio), ("0435", "Base imponible general", base),
        ("0545", _("Cuota íntegra estatal (после mínimo personal)"), cuota_st), ("0546", "Cuota íntegra autonómica", cuota_rg),
        ("0587", "Cuota líquida incrementada total", total),
        ("0599", "Retenciones y demás pagos a cuenta: Por rendimientos de actividades económicas", n["withheld"]),
        ("0604", "Pagos fraccionados ingresados (actividades económicas)", paid_130),
        ("0610", _("Cuota diferencial: + к доплате / − к возврату"), result)]}


# ---------- Beckham (151) ----------

def beckham_annual(con, s, year) -> dict:
    sl = sales(con, year)
    income = sum(x["base"] for x in sl)
    withheld = sum(x["irpf"] for x in sl)
    supplies = sum(_cost(e) for e in purchases(con, year) if e["category"] == "home")
    cuota = scale(income, BECKHAM_GENERAL)
    paid_210 = sum(irnr_paid(s, year))
    result = cuota - withheld - paid_210
    return {"modelo": "151", "title": _("Declaración régimen especial {year} (оценка)").format(year=year), "result": result, "boxes": [
        ("B.02", _("Ingresos íntegros (все клиенты, в т.ч. иностранные)"), income),
        ("B.03/B.04", _("Gastos de personal; Gastos de aprovisionamiento de materiales y de suministros (только они)"), 0),
        ("B.05 = F.17", "Rendimiento neto: positivo = Base liquidable general", income),
        ("G.19", _("Cuota correspondiente a la base liquidable general: 24 % до 600 000 €, 47 % сверх"), cuota),
        ("G.33", "Retenciones e ingresos a cuenta", withheld),
        ("G.34", "Cuotas del Impuesto sobre la Renta de no Residentes pagadas respecto de rentas incluidas en la declaración (Modelo 210)", paid_210),
        ("G.43", "Resultado de la declaración: + a ingresar / − a devolver", result)], "notes": [
        _("Режим Beckham: расходы (софт, коворкинг, техника, gestoría) и собственная RETA НЕ уменьшают базу. [[trlirnr-24,dgt-v1112-25]]"),
        _("Строгий расчёт: suministros не вычтены. Ваши коммунальные расходы в «доле для работы»: {amount} — "
          "их вычет по art. 24.2 спорный, решать с консультантом. [[trlirnr-24]]").format(amount=fmt(supplies)),
        _("Квартальных деклараций по налогу нет: авансы в режиме — только удержания клиента, а 210 — форма нерезидентов. "
          "Применяется ли общий 130 к деятельности в режиме, закон прямо не говорит. Квартально откладывайте ~24 % от выручки. "
          "[[rirpf-114,orden-eha-3316-2010-210,lirpf-99-7-pagos-fraccionados]]"),
        *([_("Уплаченные добровольно 210 ({amount}) вычитаются из налога. Куда их писать после года переезда — в [34]/[37] "
             "или в [06] Epígrafe B — AEAT прямо не говорит; gestor пишет в [34]/[37]. [[rirpf-114-2b-cuotas-irnr,aeat-151-instr-c34]]")
           .format(amount=fmt(paid_210))] if paid_210 else []),
        _("Иностранный налог у источника → deducción doble imposición (G.27, лимит 30 % cuota) — добавить вручную. "
          "[[rirpf-114,aeat-novedades-rd1008-2023]]"),
        _("Подача: отдельная форма 151 в Sede (Cl@ve), до 30 июня следующего года (domiciliación до 25 июня). [[orden-hfp-1338-2023]]")]}


# ---------- RETA ----------

def reta_tramo(year, r_monthly_cents: int):
    for name, hi, lo, top in RETA_TRAMOS:
        if hi is None or D(r_monthly_cents) / 100 <= D(str(hi)):
            mx = top or _known(RETA_MAX_BASE, year)[0]
            return name, cents(D(lo) * 100), cents(D(mx) * 100)


def reta_days(s, year) -> tuple[int, int]:
    """(days in RETA during `year`, of them regularizable). Tarifa plana covers the alta month and the next 12 full
    calendar months and is not regularized (kb/reta.md rule 6)."""
    ys, ye = date(year, 1, 1), date(year, 12, 31)
    start = date.fromisoformat(s["reta_start"]) if s.get("reta_start") else None
    first = max(start, ys) if start else ys
    if first > ye:
        return 0, 0
    ordinary = first
    if s.get("tarifa_plana") and start:
        m = start.month + 13
        ordinary = max(first, date(start.year + (m - 1) // 12, (m - 1) % 12 + 1, 1))
    return (ye - first).days + 1, max(0, (ye - ordinary).days + 1)


def reg_months(s, year) -> D:
    """Regularizable liquidation months in `year`; a partial month counts by its days."""
    total_d, reg_d = reta_days(s, year)
    if not reg_d:
        return D(0)
    start = date(year, 12, 31) - timedelta(days=reg_d - 1)
    full = 12 - start.month
    dim = (add_months(date(year, start.month, 1), 1) - timedelta(days=1)).day
    return full + D(dim - start.day + 1) / dim


def reta_estimate(con, s, year, net_annual: int, paid_reta: int) -> dict:
    """Art. 308 LGSS: N = (IRPF net + own cuotas) × 0.93 (0.97 societario); R = N / regularizable days × 30 (kb/reta.md)."""
    a = net_annual + paid_reta
    societario = s["kind"] == "sl"
    n = cents(D(a) * (D("0.97") if societario else D("0.93")))
    total_d, reg_d = reta_days(s, year)
    r = D(n) * 30 / (reg_d or total_d or 365)  # unrounded until the tramo is chosen
    name, lo, hi = reta_tramo(year, r)
    if societario:
        floor = cents(D(_known(RETA_SOCIETARIO_MIN, year)[0]) * 100)
        lo, hi = max(lo, floor), max(hi, floor)
    rate, exact = _known(RETA_RATE, year)
    cuota = pct(lo, rate)
    chosen = s.get("reta_base") or 0
    notes = [_("Доход для RETA: {amount} за год (чистый доход + RETA), минус {pct} % → {monthly} в месяц "
               "(дней в RETA: {days}, из них регуляризуемых: {reg_days}) → tramo {tramo}.")
             .format(amount=fmt(a), pct='3' if societario else '7', monthly=fmt(cents(r)), days=total_d, reg_days=reg_d, tramo=name),
             _("Базу меняют в Import@ss до 6 раз в год (с 1 марта, мая, июля, сентября, ноября, января).")]
    if not exact:
        notes.append(_("Таблиц RETA за {year} в gestor нет (не опубликованы или не внесены) — расчёт по таблицам {used} года: "
                       "tramos, базы, ставка.").format(year=year, used=max((y for y in RETA_RATE if y <= year), default=min(RETA_RATE))))
    delta = 0
    if total_d > reg_d:
        notes.append(_("Tarifa plana: {days} дн. фиксированная cuota 80 € + MEI, за них регуляризации нет. "
                       "80 € закон прямо называет для 2023–2025 годов; на 2026 год сумму сверьте с TGSS. [[leta-38ter]]")
                     .format(days=total_d - reg_d))
    if reg_d and chosen:
        if chosen < lo:
            delta = cents(D(pct(lo - chosen, rate)) * reg_months(s, year))
            notes.append(_("Ваша база {base} ниже минимума tramo {minimum} → ожидаемая доплата при регуляризации ≈ {amount}. [[rd2064-1995-46]]")
                         .format(base=fmt(chosen), minimum=fmt(lo), amount=fmt(delta)))
        elif chosen > hi:
            delta = -cents(D(pct(chosen - hi, rate)) * reg_months(s, year))
            notes.append(_("Ваша база выше максимума tramo → ожидаемый возврат ≈ {amount}. [[rd2064-1995-46]]").format(amount=fmt(-delta)))
        else:
            notes.append(_("Ваша база внутри tramo — регуляризации не будет. [[rd2064-1995-46]]"))
    elif reg_d:
        notes.append(_("Укажите в настройках текущую базу RETA, чтобы посчитать регуляризацию."))
    if regime(s, year) == "beckham":
        notes.insert(0, _("Beckham: TGSS не получает данные из Modelo 151; критерий регуляризации не установлен. "
                          "Ниже — симуляция по обычным правилам art. 308 LGSS, не окончательный расчёт. [[lgss-308]]"))
    return {"modelo": "RETA", "title": _("Seguridad Social {year} (оценка)").format(year=year), "result": delta,
            "result_label": _("Регуляризация"), "notes": notes, "boxes": [
                ("R", "Rendimiento mensual para SS", cents(r)), ("tramo", f"Tramo {name}: base mínima", lo), ("", "base máxima", hi),
                ("", _("Cuota mínima в месяц ({rate} %)").format(rate=rate), cuota), ("", _("Ваша текущая база"), chosen)]}


# ---------- SL (202 / 111 / 200) ----------

IS_MICRO = {2024: [(0, "23")], 2025: [(0, "21"), (50000, "22")], 2026: [(0, "19"), (50000, "21")],
            2027: [(0, "17"), (50000, "20")]}


def sl_days(s, year) -> int:
    """Length of the company tax period in `year` (first period starts at the escritura / activity start)."""
    start = s.get("activity_start") or ""
    first = date.fromisoformat(start) if start[:4] == str(year) else date(year, 1, 1)
    return (date(year, 12, 31) - first).days + 1


def is_rate(s, year, base: int) -> int:
    """IS cuota íntegra: micro (INCN prev. < 1 M€) scale with the 50 000 € band prorated for a short first period;
    15 % empresa emergente in its first profitable period and the next three (year must be set); else 25 %."""
    fp = str(s.get("sl_first_profit_year") or "")
    if s.get("sl_emergente") and fp.isdigit() and int(fp) <= year <= int(fp) + 3:
        return pct(base, 15)
    if s.get("sl_small_incn"):
        days = min(sl_days(s, year), 365)
        brackets = [(lo if not i else D(lo) * days / 365, rate) for i, (lo, rate) in enumerate(_known(IS_MICRO, year)[0])]
        return scale(base, brackets)
    return pct(base, IS_GENERAL)


def sl_profit(con, s, year, upto: date) -> dict:
    income = sum(x["base"] for x in sales(con, year) if x["date"] <= upto.isoformat())
    exp = income_tax_expenses(con, year, upto, amort_rate(s))
    return {"income": income, "exp": exp["total"], "profit": income - exp["total"]}


def forms_202(con, s, year) -> list:
    """Modalidad 40.2 LIS: 18 % of the last 200 whose deadline has passed (April → year-2, Oct/Dec → year-1).
    Base = cuota íntegra − deducciones − retenciones of that 200; entered in settings, else estimated from the ledger."""
    out = []
    started = int((s.get("activity_start") or "0000")[:4] or 0)
    for p, ref in ((1, year - 2), (2, year - 1), (3, year - 1)):
        entered = (s.get("sl_200_cuotas") or {}).get(str(ref))
        has_data = sales(con, ref)
        if entered is not None:
            base, note = int(entered), _("База — из поданного Modelo 200 за {ref} (настройки).").format(ref=ref)
        elif started > ref:
            base, note = 0, _("Компании в {ref} не было — 202 не подаётся.").format(ref=ref)
        elif has_data:
            base = is_rate(s, ref, max(sl_profit(con, s, ref, date(ref, 12, 31))["profit"], 0))
            note = _("Оценка по счетам {ref}. Точнее — внесите базу из поданного Modelo 200 в настройках.").format(ref=ref)
        else:
            base, note = None, _("Нет данных за {ref}: внесите базу из Modelo 200 за {ref} в настройках.").format(ref=ref)
        res = pct(base or 0, 18)
        notes = [note, _("Modalidad 40.2. Если текущий год заметно хуже прошлого — опция 40.3 (от текущей прибыли) через 036 в феврале.")]
        fp = str(s.get("sl_first_profit_year") or "")
        if s.get("sl_emergente") and fp.isdigit() and year in (int(fp) + 1, int(fp) + 2):
            base, res = 0, 0
            notes = [_("Empresa emergente: в 2 периода после первого прибыльного 202 не платится. [[sl-ley28-2022-8]]")]
        out.append({"modelo": "202", "title": f"Pago fraccionado IS {p}P", "result": res, "applies": base is None or res > 0,
                    "boxes": [("01", f"Base del pago fraccionado: cuota IS {ref} − deducciones − retenciones", base or 0), ("03", "A ingresar (18 %)", res)],
                    "notes": notes})
    return out


def forms_withholding(con, s, year) -> tuple[list, list]:
    """Retenciones WE withheld, per quarter: 111 (administrador of an SL, profesionales) and 115 (rent).
    Administrador: 19 % if last-year turnover is known and < 100 000 €, else 35 % (art. 80.1.3º RIRPF)."""
    prev = sales(con, year - 1)
    admin_rate = 19 if prev and sum(x["base"] for x in prev) < 100000_00 else 35
    f111, f115 = [], []
    for q in range(1, 5):
        rows = [e for e in purchases(con, year) if quarter_of(e["date"]) == q]
        money = sum(e["base_cents"] for e in rows if e["category"] == "admin_pay") if s["kind"] == "sl" else 0
        kind = sum(e["base_cents"] for e in rows if e["category"] == "reta") if s["kind"] == "sl" and money else 0
        prof = [e for e in rows if e["withheld_cents"] and e["category"] not in ("rent", "admin_pay")]
        rent = [e for e in rows if e["withheld_cents"] and e["category"] == "rent"]
        boxes, total = [], 0
        if money or kind:
            boxes += [("02", "Rendimientos del trabajo. Rendimientos dinerarios: Importe de las percepciones", money),
                      ("03", f"Rendimientos del trabajo. Rendimientos dinerarios: Importe de las retenciones ({admin_rate} %)", pct(money, admin_rate)),
                      ("05", _("Rendimientos del trabajo. Rendimientos en especie: Valor percepciones en especie (RETA, оплаченная SL)"), kind),
                      ("06", "Rendimientos del trabajo. Rendimientos en especie: Importe de los ingresos a cuenta", pct(kind, admin_rate))]
            total += pct(money + kind, admin_rate)
        if prof:
            w = sum(e["withheld_cents"] for e in prof)
            boxes += [("07–09", "Rendimientos de actividades económicas. Rendimientos dinerarios: Importe de las percepciones",
                       sum(e["base_cents"] for e in prof)),
                      ("07–09", "Rendimientos de actividades económicas. Rendimientos dinerarios: Importe de las retenciones", w)]
            total += w
        n_prof = len({e["supplier_tax_id"] or e["supplier"] for e in prof})
        f111.append({"modelo": "111", "title": f"Retenciones {q}T", "result": total, "boxes": boxes,
                     "notes": [_("Получателей-профессионалов: {n}.").format(n=n_prof) if prof else "",
                               _("190 в январе: сводка по получателям (administrador — clave E, профессионалы — clave G).")
                               + ("" if prev or not money else _(" Оборот прошлого года неизвестен — взята ставка 35 %.")) + " [[rirpf-80]]"]}
                    if boxes else None)
        f115.append({"modelo": "115", "title": f"Retenciones alquiler {q}T", "result": sum(e["withheld_cents"] for e in rent),
                     "boxes": [("", "Base retenciones e ingresos a cuenta", sum(e["base_cents"] for e in rent)),
                               ("", "Retenciones e ingresos a cuenta (19 %)", sum(e["withheld_cents"] for e in rent))],
                     "notes": [_("180 в январе: сводка по арендодателям. [[rirpf-100]]")]} if rent else None)
    return f111, f115


def is_annual(con, s, year, paid_202: int, projected_202: int = 0) -> dict:
    r = sl_profit(con, s, year, date(year, 12, 31))
    base = max(r["profit"], 0)
    cuota = is_rate(s, year, base)
    notes = [_("Без reserva de capitalización/nivelación, BIN прошлых лет, ENC 15 % и вычетов — добавить в Sociedades WEB."),
             _("Подача всегда, даже при убытке: 1–25 июля следующего года (сертификат компании)."),
             _("Registro Mercantil: legalización libros до 30 апреля, formulación до 31 марта, aprobación до 30 июня, depósito ≈ до 30 июля.")]
    if projected_202:
        notes.insert(0, _("Учтены только поданные 202 ({paid}); ещё не поданы: {projected}.")
                     .format(paid=fmt(paid_202), projected=fmt(projected_202)))
    if s.get("sl_emergente") and not str(s.get("sl_first_profit_year") or "").isdigit():
        notes.append(_("Empresa emergente: укажите в настройках первый прибыльный год — без него расчёт идёт по обычной ставке, "
                       "15 % действует в этом году и трёх следующих. [[ley28-2022-7]]"))
    return {"modelo": "200", "title": _("Impuesto sobre Sociedades {year} (оценка)").format(year=year), "result": cuota - paid_202, "boxes": [
        ("", "Ingresos", r["income"]), ("", _("Gastos (вкл. amortización, retribución administrador)"), r["exp"]),
        ("00552", "Base imponible", base), ("00562", "Cuota íntegra", cuota),
        ("00601–00605", "Pagos fraccionados (1er, 2º y 3er pago fraccionado)", paid_202),
        ("00621", "Resultado", cuota - paid_202)], "notes": notes}


# ---------- legal basis (ids in gestor/sources/*.json) ----------

FORM_SOURCES = {
    "303": ["riva-71", "aeat-303-instr-2026", "liva-115"],
    "130": ["rirpf-109", "rirpf-110", "lirpf-99"],
    "349": ["riva-79", "riva-81"],
    "347": ["rgat-33"],
    "390": ["riva-71", "aeat-390-instr", "aeat-390-dr-2025", "liva-108"],
    "100": ["lirpf-63", "lirpf-57", "lirpf-72", "cv-escala", "ast-escala", "mad-escala", "cat-escala", "and-escala",
            "aeat-manual-renta-gastos"],
    "151": ["lirpf-93", "rirpf-114", "trlirnr-24", "trlirnr-25", "aeat-novedades-rd1008-2023", "orden-hfp-1338-2023",
            "aeat-manual-beckham"],
    "RETA": ["lgss-308", "orden-pjc-178-2025", "orden-pjc-297-2026", "rd2064-1995-46", "rd2064-1995-45", "tgss-importass-base"],
    "202": ["lis-40", "sl-aeat-202-cuota-cero"],
    "200": ["lis-29", "lis-dt44", "lis-124", "lis-15", "lis-12"],
    "111": ["rirpf-80", "lirpf-99"],
    "115": ["rirpf-100", "rirpf-75"],
}
BOX_SOURCES = {
    ("303", "07"): ["liva-90"], ("303", "09"): ["liva-90"],
    ("303", "10"): ["liva-84"], ("303", "11"): ["liva-84"], ("303", "12"): ["liva-84"], ("303", "13"): ["liva-84"],
    ("303", "28"): ["liva-94", "liva-97"], ("303", "29"): ["liva-94", "liva-95", "liva-97"],
    ("303", "30"): ["liva-108"], ("303", "31"): ["liva-108"],
    ("303", "36"): ["liva-84", "liva-94"], ("303", "37"): ["liva-84", "liva-94"],
    ("303", "59"): ["liva-69", "aeat-303-instr-2026"], ("303", "120"): ["liva-69", "aeat-303-instr-2026"],
    ("303", "110"): ["liva-99"], ("303", "78"): ["liva-99"], ("303", "87"): ["liva-99"], ("303", "71"): ["liva-115"],
    ("130", "01"): ["lirpf-28"], ("130", "02"): ["lirpf-28", "rirpf-30", "lirpf-30-reta", "amort-simplificada"],
    ("130", "04"): ["rirpf-110"], ("130", "06"): ["lirpf-101"], ("130", "13"): ["rirpf-110", "aeat-130-instr"],
    ("130", "19"): ["rirpf-110"],
    ("100", "0186"): ["lirpf-30-reta"], ("100", "0208"): ["amort-simplificada"], ("100", "0222"): ["rirpf-30"],
    ("100", "0234"): ["lirpf-32"], ("100", "0545"): ["lirpf-63", "lirpf-57"],
    ("100", "0546"): ["cv-escala", "ast-escala", "mad-escala", "cat-escala", "and-escala"],
    ("100", "0599"): ["lirpf-101"],
    ("151", "B.03/B.04"): ["trlirnr-24", "dgt-v1112-25"], ("151", "G.19"): ["lirpf-93", "trlirnr-25"], ("151", "G.33"): ["rirpf-114"],
    ("RETA", "tramo"): ["orden-pjc-178-2025", "orden-pjc-297-2026", "lgss-308"],
    ("202", "03"): ["lis-40"], ("200", "00562"): ["lis-29", "lis-dt44"],
}


# ---------- assembly ----------

def filed_amounts(con, year, modelo) -> dict:
    return {r["period"]: r["amount_cents"] for r in
            con.execute("SELECT period, amount_cents FROM filings WHERE year = ? AND modelo = ?", (year, modelo))}


def _paid_and_projected(con, year, modelo, computed: list) -> tuple[int, int]:
    """Advances credited in the annual return: only filed ones; the rest is shown as projected."""
    filed = filed_amounts(con, year, modelo)
    paid = sum(max(v, 0) for v in filed.values())
    projected = sum(max(f["result"], 0) for f in computed if f["period"] not in filed)
    return paid, projected


def forms(con, s, year) -> list:
    reg = regime(s, year)
    iva = iva_year(con, s, year)
    groups = []
    f130 = forms_130(con, s, year) if reg == "general" and not exempt_from_130(con, s, year) else []
    f202 = forms_202(con, s, year) if reg == "sl" else []
    f111, f115 = forms_withholding(con, s, year)
    for q in range(1, 5):
        fs = [dict(iva[q - 1])]
        if f130:
            fs.append(f130[q - 1])
        f349 = form_349(con, year, q)
        if f349:
            fs.append(f349)
        fs += [f for f in (f111[q - 1], f115[q - 1]) if f]
        if reg == "sl" and q < 4 and f202[q - 1]["applies"]:
            fs.append(f202[q - 1])
        for f in fs:
            f.update(year=year, period=f"{q}T" if f["modelo"] != "202" else f"{q}P",
                     deadline=deadline(f["modelo"], year, q), opens=opens(f["modelo"], year, q))
        groups.append((_("{q} квартал").format(q=q), fs))
    annual = [form_390(con, year, iva)]
    f347 = form_347(con, year)
    if f347:
        annual.append(f347)
    if reg == "general":
        annual.append(irpf_annual(con, s, year, *_paid_and_projected(con, year, "130", f130)))
        if exempt_from_130(con, s, year):
            annual[-1]["notes"].append(_("130 не подаётся: в прошлом году ≥ 70 % дохода было с retención."))
    elif reg == "beckham":
        annual.append(beckham_annual(con, s, year))
    else:
        annual.append(is_annual(con, s, year, *_paid_and_projected(con, year, "202", [f for f in f202 if f["applies"]])))
    if reg == "sl":
        pay = sum(e["base_cents"] for e in purchases(con, year) if e["category"] == "admin_pay")
        reta = sum(e["base_cents"] for e in purchases(con, year) if e["category"] == "reta")
        if pay or reta or s.get("reta_start"):
            annual.append(reta_estimate(con, s, year, pay, reta))
    else:
        n = net_ytd(con, year, date(year, 12, 31))
        annual.append(reta_estimate(con, s, year, n["rn"], n["exp"]["reta"]))
    for f in annual:
        f.update(year=year, period="0A", deadline=deadline(f["modelo"], year, 0), opens=opens(f["modelo"], year, 0))
    for _name, fs in groups + [("", annual)]:
        for f in fs:
            f["sources"] = applicable(FORM_SOURCES.get(f["modelo"], []), s, year)
    groups.append((_("Годовые"), annual))
    return groups


REGION_SOURCES = {"valencia": "cv-escala", "asturias": "ast-escala", "madrid": "mad-escala", "cataluna": "cat-escala",
                  "andalucia": "and-escala"}


def applicable(ids, s, year) -> list:
    """Sources that apply to this profile in `year`: valid that year, and only the regional scale of that year's region."""
    other = {sid for r, sid in REGION_SOURCES.items() if r != region_for_year(s, year)}
    return [i for i in sources.for_year(ids, year) if i not in other]


# ---------- calendar ----------

# Fiestas nacionales of art. 45 RD 2001/1983 (6 Jan is substitutable, but no region substituted it in the
# 2023–2026 BOE calendars). Regional/local holidays (art. 30.6 Ley 39/2015) and Sunday→Monday moves are not modelled.
NATIONAL_HOLIDAYS = ((1, 1), (1, 6), (5, 1), (8, 15), (10, 12), (11, 1), (12, 6), (12, 8), (12, 25))


def good_friday(year: int) -> date:
    """Viernes Santo: two days before Gregorian Easter Sunday (anonymous Gregorian algorithm)."""
    a, b, c = year % 19, year // 100, year % 100
    h = (19 * a + b - b // 4 - (b - (b + 8) // 25 + 1) // 3 + 15) % 30
    wd = (32 + 2 * (b % 4) + 2 * (c // 4) - h - c % 4) % 7
    month, day = divmod(h + wd - 7 * ((a + 11 * h + 22 * wd) // 451) + 114, 31)
    return date(year, month, day + 1) - timedelta(days=2)


def business_day(d: date) -> date:
    """Art. 30.2 and 30.5 Ley 39/2015: a deadline on a Saturday, Sunday or national holiday moves to the next working day."""
    while d.weekday() >= 5 or (d.month, d.day) in NATIONAL_HOLIDAYS or d == good_friday(d.year):
        d += timedelta(days=1)
    return d


def deadline(modelo: str, year: int, q: int) -> str:
    """Filing deadline for the tax period, moved past weekends and national holidays (business_day)."""
    if modelo in ("303", "130", "349", "111", "115"):
        if q == 4:
            d = date(year + 1, 1, 20 if modelo in ("111", "115") else 30)
        else:
            d = date(year, 3 * q + 1, 20)
    elif modelo == "202":
        d = date(year, (4, 10, 12)[q - 1], 20)
    elif modelo == "390":
        d = date(year + 1, 1, 30)
    elif modelo == "347":
        d = date(year + 1, 3, 1) - timedelta(days=1)
    elif modelo in ("190", "180"):
        d = date(year + 1, 1, 31)
    elif modelo in ("100", "151", "714"):
        d = date(year + 1, 6, 30)
    elif modelo == "200":
        d = date(year + 1, 7, 25)
    elif modelo in ("720", "721"):
        d = date(year + 1, 3, 31)
    elif modelo == "RETA":
        d = date(year + 1, 12, 31)
    else:
        d = date(year + 1, 1, 30)
    return business_day(d).isoformat()


def opens(modelo: str, year: int, q: int) -> str:
    """First day of the filing window (AEAT calendar): quarterly — day after the quarter; 202 — 1 Apr/Oct/Dec;
    annual — 1 Jan, 347 — 1 Feb, Renta/151 — 1 Apr (campaign start approximated), 200 — 1 Jul of the next year."""
    if modelo in ("303", "130", "349", "111", "115") and q:
        d = quarter_end(year, q) + timedelta(days=1)
    elif modelo == "202":
        d = date(year, (4, 10, 12)[q - 1], 1)
    elif modelo == "347":
        d = date(year + 1, 2, 1)
    elif modelo in ("100", "151", "714"):
        d = date(year + 1, 4, 1)
    elif modelo == "200":
        d = date(year + 1, 7, 1)
    else:
        d = date(year + 1, 1, 1)
    return d.isoformat()


def calendar(con, s, year) -> list:
    """All filing deadlines for tax year `year`: computed forms plus reminders without a computed form."""
    fs = [f for _, group in forms(con, s, year) for f in group if f["modelo"] != "RETA"]
    out = [{"modelo": f["modelo"], "period": f["period"], "year": year, "title": f["title"], "deadline": f["deadline"],
            "opens": f["opens"]} for f in fs]
    present = {f["modelo"] for f in fs}
    extra = []
    if "111" in present:
        extra.append(("190", deadline("190", year, 0), "Resumen anual retenciones (111)"))
    if "115" in present:
        extra.append(("180", deadline("180", year, 0), "Resumen anual retenciones alquiler (115)"))
    if regime(s, year) == "general":
        extra.append(("720", deadline("720", year, 0), _("Bienes en el extranjero (если > 50 000 € в блоке)")))
    if regime(s, year) == "sl":
        extra += [("Libros", business_day(date(year + 1, 4, 30)).isoformat(), _("Legalización de libros в Registro Mercantil")),
                  ("Cuentas", business_day(date(year + 1, 7, 30)).isoformat(), _("Депозит cuentas anuales + titularidad real"))]
    out += [{"modelo": m, "period": "0A", "year": year, "title": t, "deadline": d, "opens": opens(m, year, 0)} for m, d, t in extra]
    return sorted(out, key=lambda d: d["deadline"])


# ---------- duties: what gestor thinks you must file, and why ----------

MODELO_ABOUT = {  # one sentence: what this return is about, for someone who has never seen it
    "303": N_("IVA, начисленный клиентам, минус IVA из ваших расходов. Плюс — платите, минус — переносите на следующий квартал (после 4T можно вернуть)."),
    "130": N_("Аванс IRPF: 20 % прибыли с 1 января минус авансы прошлых кварталов и удержания клиентов. Итог года считается в Renta."),
    "349": N_("Сведения, не налог: кому в ЕС вы оказали услуги без IVA и у кого из ЕС купили. Платить ничего не нужно."),
    "111": N_("IRPF, который вы удержали из чужих счетов (специалисты, администратор SL), — вы перечисляете его в AEAT."),
    "115": N_("19 %, которые вы удержали из аренды помещения, — вы перечисляете их в AEAT за арендодателя."),
    "202": N_("Аванс налога на прибыль SL, считается от последней декларации 200."),
    "390": N_("Годовая сводка всех 303. Платить ничего не нужно, цифры должны сойтись с кварталами."),
    "347": N_("Сведения о контрагентах с оборотом за год больше 3 005,06 €. Платить ничего не нужно."),
    "100": N_("Годовая декларация IRPF: налог за год по шкале минус авансы 130 и удержания клиентов."),
    "151": N_("Годовая декларация режима Beckham: 24 % (47 % сверх 600 000 €) минус удержания клиентов."),
    "200": N_("Годовой налог на прибыль SL минус авансы 202."),
    "RETA": N_("Не декларация: оценка, сколько TGSS доначислит или вернёт по взносам после конца года."),
}

DUTY_INFO = {  # modelo → (what it is, how often, rules that create the duty)
    "303": (N_("IVA за квартал"), N_("каждый квартал"), ["riva-71"]),
    "130": (N_("Аванс IRPF: 20 % прибыли с 1 января"), N_("каждый квартал"), ["lirpf-99", "rirpf-109"]),
    "349": (N_("Сведения об операциях с бизнесом из ЕС"), N_("в квартал, когда они были"), ["riva-79", "riva-81"]),
    "111": (N_("Удержания IRPF, которые сделали вы"), N_("каждый квартал"), ["lirpf-101", "rirpf-95", "rirpf-80"]),
    "115": (N_("Удержание 19 % с аренды помещения"), N_("каждый квартал"), ["rirpf-100", "rirpf-75"]),
    "202": (N_("Аванс налога на прибыль SL"), N_("апрель, октябрь, декабрь"), ["lis-40", "sl-aeat-202-cuota-cero"]),
    "390": (N_("Годовая сводка IVA"), N_("январь"), ["riva-71", "aeat-390-instr"]),
    "347": (N_("Контрагенты с оборотом за год больше 3 005,06 € (бизнес из ЕС идёт в 349)"), N_("февраль"), ["rgat-33"]),
    "100": (N_("Годовая декларация IRPF (Renta)"), N_("апрель — июнь"), ["lirpf-63", "lirpf-72"]),
    "151": (N_("Годовая декларация режима Beckham"), N_("апрель — июнь"), ["lirpf-93", "orden-hfp-1338-2023"]),
    "200": (N_("Годовой налог на прибыль SL"), N_("июль"), ["lis-124", "lis-29"]),
    "190": (N_("Годовая сводка удержаний из 111"), N_("январь"), []),
    "180": (N_("Годовая сводка удержаний с аренды из 115"), N_("январь"), []),
    "720": (N_("Имущество за рубежом"), N_("январь — март"), ["lgt-da18", "irpf-rgat-42bis"]),
    "Libros": (N_("Легализация бухгалтерских книг SL"), N_("до 30 апреля"), ["ley14-2013-18"]),
    "Cuentas": (N_("Депозит годовой отчётности SL"), N_("до 30 июля"), ["lsc-253", "lsc-279"]),
    "RETA": (N_("Взнос в Seguridad Social autónomo"), N_("каждый месяц, списание"), ["lgss-305", "lgss-308"]),
    "210": (N_("Декларация IRNR нерезидента без постоянного представительства"), N_("поквартально"), ["orden-eha-3316-2010-210"]),
}


def duties(con, s, year) -> tuple[list, list]:
    """(what you file in `year` with the reason from your data, what you don't file and why). Rows: modelo, what, when, why, ids."""
    reg = regime(s, year)
    have = list(dict.fromkeys(d["modelo"] for d in calendar(con, s, year)))
    if s.get("reta_start") and s["reta_start"] <= f"{year}-12-31":
        have.append("RETA")
    why = {
        "303": _("У вас деятельность в Испании. 303 подаётся каждый квартал, даже если IVA нет."),
        "130": _("Общий IRPF. Освобождение (не меньше 70 % дохода за прошлый год с удержанием клиента) к вам не применяется."),
        "349": _("В {year} есть счета бизнесу из ЕС или услуги поставщиков из ЕС.").format(year=year),
        "111": _("Вы платили вознаграждение, с которого удерживаете IRPF."),
        "115": _("Вы арендуете помещение, с аренды удерживается 19 %."),
        "202": _("У SL есть налог на прибыль, авансы считаются от прошлой декларации 200."),
        "390": _("Её подаёт каждый, кто подаёт 303 (кроме участников SII и режимов, освобождённых приказом)."),
        "347": _("Есть контрагент с оборотом за год больше 3 005,06 €, в том числе вне ЕС: исключены только импорт и экспорт товаров и операции из 349."),
        "100": _("В {year} у вас общий режим IRPF.").format(year=year),
        "151": _("{year} — год режима Beckham (первый год {first}).").format(year=year, first=s.get("beckham_first_year")),
        "200": _("Налог на прибыль SL за год."),
        "190": _("Вы подаёте 111 — по ней раз в год нужна сводка."),
        "180": _("Вы подаёте 115 — по ней раз в год нужна сводка."),
        "720": _("Только если за рубежом больше 50 000 € в одном блоке: счета, ценные бумаги или недвижимость. Этого gestor не видит."),
        "Libros": _("SL обязана легализовать книги учёта."),
        "Cuentas": _("SL обязана сдать годовую отчётность."),
        "RETA": _("Вы в RETA с {date}.").format(date=s.get("reta_start")),
    }
    out = [dict(modelo=m, what=_(DUTY_INFO[m][0]), when=_(DUTY_INFO[m][1]), why=why[m],
                ids=for_year_ids(m, year)) for m in have if m in DUTY_INFO]
    no = []
    if "130" not in have:
        if reg == "beckham":
            no.append(("130", _("В режиме Beckham авансы — только удержания клиентов по правилам IRNR. "
                                "Применяется ли общий 130 к деятельности в режиме, закон прямо не говорит."),
                       ["rirpf-114", "aeat-novedades-rd1008-2023", "lirpf-99-7-pagos-fraccionados"]))
        elif reg == "sl":
            no.append(("130", _("У SL нет IRPF. Вместо 130 — авансы 202 и годовая 200."), ["lis-40"]))
        else:
            no.append(("130", _("В прошлом году не меньше 70 % дохода пришло с удержанием клиента."), ["rirpf-109"]))
    if reg == "beckham":
        no.append(("100", _("Вместо обычной Renta — Modelo 151."), ["lirpf-93", "orden-hfp-1338-2023"]))
        no.append(("210", _("Вы налогоплательщик IRPF, а 210 подают нерезиденты. Клиент без представительства в Испании "
                            "не удерживает налог, поэтому квартального платежа закон не требует. Уплаченные добровольно 210 "
                            "впишите в анкете — gestor вычтет их в 151."), ["orden-eha-3316-2010-210", "trlirnr-31-1", "rirpf-114-2b-cuotas-irnr"]))
    if "349" not in have:
        no.append(("349", _("В {year} нет операций с бизнесом из ЕС.").format(year=year), ["riva-79"]))
    if "347" not in have:
        no.append(("347", _("Ни с одним контрагентом — в Испании или вне ЕС — оборот не больше 3 005,06 €. Операции из 349 и с удержанием не считаются."),
                   ["rgat-33"]))
    if "111" not in have:
        no.append(("111", _("Вы не платили вознаграждений, с которых надо удерживать IRPF."), []))
    if "115" not in have:
        no.append(("115", _("В {year} нет расходов на аренду, с которых вы удержали 19 %.").format(year=year), ["rirpf-100"]))
    return out, [dict(modelo=m, what=_(DUTY_INFO[m][0]), why=w, ids=i) for m, w, i in no]


def for_year_ids(modelo, year) -> list:
    return sources.for_year(DUTY_INFO[modelo][2], year)


def add_months(d: date, n: int) -> date:
    m = d.month - 1 + n
    y, m = d.year + m // 12, m % 12 + 1
    last = (date(y + m // 12, m % 12 + 1, 1) - timedelta(days=1)).day
    return date(y, m, min(d.day, last))


# ---------- dashboard ----------

def irnr_paid(s, year) -> list:
    """Voluntary Modelo 210 paid under Beckham, cents per quarter (settings key 'YYYY-qT')."""
    return [s.get("irnr_paid", {}).get(f"{year}-{q}T", 0) for q in range(1, 5)]


PAY_ORDER = ["210", "130", "303", "111", "115", "202", "RETA", "151", "100", "200"]


def payments(con, s, year) -> dict:
    """Money for `year` to AEAT and TGSS, put in the quarter it covers. Each cell is [paid, due] in cents: paid = filed
    amount or recorded payment, due = computed but not filed yet (negative only for a 303 4T refund). Annual returns sit
    in `annual`. For Beckham `high` adds the average quarter of the last year for each quarter still ahead.
    `why[(modelo, quarter 0–3 | "year", "paid" | "due")]` says what a part is made of — the chart shows it on hover."""
    today = date.today()
    filed = {(r["modelo"], r["period"]): (r["amount_cents"] or 0, r["filed_on"]) for r in
             con.execute("SELECT modelo, period, amount_cents, filed_on FROM filings WHERE year = ?", (year,))}
    rows, annual, why, all_forms = {}, {}, {}, [f for _, fs in forms(con, s, year) for f in fs]
    for f in all_forms:
        m, p = f["modelo"], f["period"]
        if m not in PAY_ORDER or m == "RETA":
            continue
        key = "year" if p == "0A" else int(p[0]) - 1
        refund = m == "303" and p == "4T" and f["result"] < 0 and not f.get("carry_out")
        if (m, p) in filed:
            cell = [max(filed[(m, p)][0], 0), 0]
            why[(m, key, "paid")] = _("подано {date}").format(date=filed[(m, p)][1])
        else:
            cell = [0, f["result"] if refund else max(f["result"], 0)]
            why[(m, key, "due")] = (_("возврат, подать до {date}") if refund else _("расчёт по вашим книгам, подать до {date}")).format(date=f["deadline"])
        if p == "0A":
            annual[m] = cell
        else:
            rows.setdefault(m, [[0, 0] for _ in range(4)])[key] = cell
    if any(irnr_paid(s, year)):
        rows["210"] = [[c, 0] for c in irnr_paid(s, year)]
        why.update({("210", q, "paid"): _("уплачено по анкете; вычтется из налога в 151") for q in range(4)})
    reta = con.execute("SELECT date, base_cents FROM expenses WHERE category = 'reta' AND substr(date, 1, 4) = ? ORDER BY date",
                       (str(year),)).fetchall()
    if reta:
        cells, months = [[0, 0] for _ in range(4)], [[] for _ in range(4)]
        for r in reta:
            cells[(int(r["date"][5:7]) - 1) // 3][0] += r["base_cents"]
            months[(int(r["date"][5:7]) - 1) // 3].append(f"{_(MONTHS[int(r['date'][5:7]) - 1])} {fmt(r['base_cents'])}")
        for q in range(4):
            if months[q]:
                why[("RETA", q, "paid")] = _("взносы: {months}").format(months=", ".join(months[q]))
        if year == today.year:  # the months after the last cuota, at that cuota
            ahead = list(range(int(reta[-1]["date"][5:7]) + 1, 13))
            for month in ahead:
                cells[(month - 1) // 3][1] += reta[-1]["base_cents"]
            for q in {(m - 1) // 3 for m in ahead}:
                ms = [_(MONTHS[m - 1]) for m in ahead if (m - 1) // 3 == q]
                why[("RETA", q, "due")] = _("{first}–{last}: по {amount}, как последний взнос").format(
                    first=ms[0], last=ms[-1], amount=fmt(reta[-1]['base_cents']))
        rows["RETA"] = cells
    if "151" in annual:
        box = {k: v for k, _, v in next(f for f in all_forms if f["modelo"] == "151")["boxes"]}
        if annual["151"][1]:
            why[("151", "year", "due")] = (_("24 % от выручки {income} = {cuota}").format(income=fmt(box['B.02']), cuota=fmt(box['G.19']))
                                           + (_(" минус удержания {amount}").format(amount=fmt(box['G.33'])) if box["G.33"] else "")
                                           + (_(" минус 210 {amount}").format(amount=fmt(box['G.34'])) if box["G.34"] else "")
                                           + _("; подать до 30.06.{year}").format(year=year + 1))
    high = {}
    if regime(s, year) == "beckham" and "151" in annual and year == today.year:
        inc = [0] * 8
        for i, y in enumerate((year - 1, year)):
            for x in sales(con, y):
                inc[i * 4 + (int(x["date"][5:7]) - 1) // 3] += x["base"]
        done = (today.month - 1) // 3  # quarters finished this year
        run = sum(inc[done: done + 4]) // 4  # the last four finished quarters
        # ponytail: flat run-rate of the last year; seasonality or a known contract needs its own forecast input
        hi = scale(box["B.02"] + run * (4 - done), BECKHAM_GENERAL) - box["G.33"] - box["G.34"]
        if annual["151"][0] == 0 and hi > annual["151"][1]:
            high["151"] = hi
            why["high"] = _("если в оставшихся кварталах ({n}) доход будет как средний квартал за год, {avg}, "
                            "налог 151 вырастет на {amount}").format(n=4 - done, avg=fmt(run), amount=fmt(hi - annual['151'][1]))
    every = list(rows.values()) + [[c] for c in annual.values()]
    paid = sum(c[0] for cells in every for c in cells)
    due = sum(max(c[1], 0) for cells in every for c in cells)
    return {"rows": {m: rows[m] for m in PAY_ORDER if m in rows}, "annual": {m: annual[m] for m in PAY_ORDER if m in annual},
            "high": high, "why": why, "paid": paid, "due": due,
            "due_high": due + sum(high[m] - max(annual[m][1], 0) for m in high)}


MONTHS = [N_("январь"), N_("февраль"), N_("март"), N_("апрель"), N_("май"), N_("июнь"),
          N_("июль"), N_("август"), N_("сентябрь"), N_("октябрь"), N_("ноябрь"), N_("декабрь")]


def warnings(con, s, year) -> list:
    w = []
    today = date.today()
    visa = s.get("visa")
    first = str(s.get("beckham_first_year") or "")
    if first.isdigit() and s["kind"] == "autonomo" and visa in ("nomada_digital", "cuenta_propia"):
        w.append(_("Beckham с этим статусом: обычная самозанятость = establecimiento permanente → исключение из режима. "
                   "Beckham для autónomo возможен только через actividad emprendedora (ENISA). [[dgt-v2248-24,dgt-v1274-25,rirpf-113]]"))
    if first.isdigit() and int(first) + 5 == year:
        w.append(_("{year} — последний год Beckham. С {next}: Modelo 100 и 130, Modelo 720, налог на имущество по всему миру. [[lirpf-93]]")
                 .format(year=year, next=year + 1))
    if first.isdigit() and s.get("reta_start"):
        limit = add_months(date.fromisoformat(s["reta_start"]), 6)
        if today <= limit:
            w.append(_("Modelo 149 (опция Beckham) — подать до {date} (6 месяцев от alta в RETA). [[rirpf-116]]").format(date=limit.isoformat()))
    if visa == "nomada_digital":
        frm = (today - timedelta(days=365)).isoformat()
        rows = [x for y in (today.year - 1, today.year) for x in sales(con, y) if x["date"] >= frm]
        tot = sum(x["base"] for x in rows)
        es = sum(x["base"] for x in rows if x["country"] == "ES")
        if tot:
            share = D(es) * 100 / D(tot)
            if share > 18:
                w.append(_("Испанские клиенты: {share:.1f} % выручки за 12 месяцев. Лимит визы цифрового кочевника — 20 % "
                           "[[ley14-2013-74bis]]").format(share=share))
    if visa == "cuenta_propia" and len(s.get("residence") or []) > 1:
        w.append(_("ВНЖ cuenta propia: первое разрешение привязано к региону и сектору (art. 83 RD 1155/2024). "
                   "Переезд деятельности до первого продления — проверить modificación. [[rd1155-2024-83]]"))
    if s.get("permit_until"):
        left = (date.fromisoformat(s["permit_until"]) - today).days
        if left <= 120:
            w.append(_("ВНЖ истекает {date} (через {days} дн.). Готовьте продление: справки AEAT/TGSS "
                       "«al corriente», vida laboral, декларации. [[rd1155-2024-86]]").format(date=s['permit_until'], days=left))
    # DF 4.ª RRSIF (RDL 15/2025): IS taxpayers (art. 3.1.a) before 01.01.2027, the rest before 01.07.2027
    start, who = (date(2027, 1, 1), _("SL (плательщиков Impuesto sobre Sociedades)")) if s["kind"] == "sl" \
        else (date(2027, 7, 1), "autónomos")
    msg = _("Verifactu для {who} — с {date}. Hacienda объявила перенос на 10.2028, но это ещё не норма. "
            "Этот сервис пока не формирует записи Verifactu. [[verifactu-rd1007-2023,verifactu-rdl15-2025,verifactu-nota-2026]]") \
        if today < start else \
        _("Verifactu для {who} обязателен с {date}. Объявленный Hacienda перенос на 10.2028 — проверьте, вышел ли он в BOE; "
          "если нет, срок уже наступил. Этот сервис не формирует записи Verifactu. "
          "[[verifactu-rd1007-2023,verifactu-rdl15-2025,verifactu-nota-2026]]")
    w.append(msg.format(who=who, date=f"{start:%d.%m.%Y}"))
    return w
