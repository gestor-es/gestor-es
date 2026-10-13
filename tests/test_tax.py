"""Engine checks against the worked examples in kb/*.md. Run: python3 -m unittest tests.test_tax -v"""
import unittest
from datetime import date
from decimal import Decimal as D
from unittest import mock

from gestor import db, tax
from gestor.core import parse_money


def setup(kind="autonomo", **settings):
    con = db.connect(":memory:")
    s = dict(db.DEFAULT_SETTINGS, kind=kind, name="Test", tax_id="X0000000T", activity_start="2020-01-01")
    s.update(settings)
    return con, s


def client(con, country, business=1):
    return con.execute("INSERT INTO clients(name, tax_id, country, is_business) VALUES (?,?,?,?)",
                       (f"C-{country}-{business}", f"ID{country}{business}", country, business)).lastrowid


def invoice(con, cid, day, amount, treatment, vat=0, irpf=0, number=None):
    n = number or (con.execute("SELECT count(*) FROM invoices").fetchone()[0] + 1)
    iid = con.execute("""INSERT INTO invoices(series, number, issue_date, client_id, treatment, vat_rate, irpf_rate)
                         VALUES ('A', ?, ?, ?, ?, ?, ?)""", (n, day, cid, treatment, vat, irpf)).lastrowid
    con.execute("INSERT INTO invoice_lines(invoice_id, description, quantity, unit_price_cents) VALUES (?, 'x', 1, ?)",
                (iid, parse_money(amount)))


def expense(con, day, amount, category="other", vat_kind="none", vat="0", irpf_pct=100, vat_pct=100):
    con.execute("""INSERT INTO expenses(date, supplier, category, vat_kind, base_cents, vat_cents, deductible_pct, vat_deductible_pct)
                   VALUES (?, 'S', ?, ?, ?, ?, ?, ?)""", (day, category, vat_kind, parse_money(amount), parse_money(vat), irpf_pct, vat_pct))


def year_2025_example(con):
    """kb/irpf-autonomo.md: 60 000 € foreign income, 6 000 € expenses, 3 600 € RETA, even by quarter."""
    us = client(con, "US")
    for m in (2, 5, 8, 11):
        invoice(con, us, f"2025-{m:02d}-15", "15000", "extra_eu")
        expense(con, f"2025-{m:02d}-10", "1500")
        expense(con, f"2025-{m:02d}-28", "900", category="reta")


class IrpfGeneral(unittest.TestCase):
    def test_130_quarters_and_annual_valencia_asturias(self):
        con, s = setup(residence=[{"from": "2020-01-01", "region": "valencia"}])
        year_2025_example(con)
        # previous year with RN > 12 000 → no minoración (as in the KB example)
        invoice(con, client(con, "US"), "2024-06-01", "40000", "extra_eu", number=99)
        self.assertEqual([f["result"] for f in tax.forms_130(con, s, 2025)], [239400, 239400, 239400, 249800])
        f100 = tax.irpf_annual(con, s, 2025, 968000)
        box = {b[0]: b[2] for b in f100["boxes"]}
        self.assertEqual(box["0224"], 4840000)
        self.assertEqual(box["0587"], 1253805)
        self.assertEqual(f100["result"], 285805)
        s["residence"] = [{"from": "2020-01-01", "region": "asturias"}]
        self.assertEqual({b[0]: b[2] for b in tax.irpf_annual(con, s, 2025, 968000)["boxes"]}["0587"], 1257683)

    def test_annual_credits_only_filed_130(self):
        con, s = setup(residence=[{"from": "2020-01-01", "region": "valencia"}])
        year_2025_example(con)
        invoice(con, client(con, "US"), "2024-06-01", "40000", "extra_eu", number=99)
        f100 = [f for f in tax.forms(con, s, 2025)[-1][1] if f["modelo"] == "100"][0]
        self.assertEqual(f100["result"], 1253805)  # nothing filed → nothing credited
        con.execute("INSERT INTO filings(modelo, year, period, filed_on, amount_cents) VALUES ('130', 2025, '1T', '2025-04-15', 239400)")
        f100 = [f for f in tax.forms(con, s, 2025)[-1][1] if f["modelo"] == "100"][0]
        self.assertEqual(f100["result"], 1253805 - 239400)

    def test_asturias_published_fixed_quota(self):
        """kb/irpf-autonomo.md: use published cuota fija (1 751,36 € at 17 707,20 €)."""
        self.assertEqual(tax.scale(1770723, tax.REGION_SCALES["asturias"][2025]), 175136)

    def test_first_year_minoracion_and_unknown_previous_year(self):
        con, s = setup(activity_start="2025-01-01")
        year_2025_example(con)
        self.assertEqual(tax.low_income_reduction(con, s, 2025), 10000)
        s["activity_start"] = "2020-01-01"
        self.assertEqual(tax.low_income_reduction(con, s, 2025), 0)  # no 2024 data → conservative

    def test_region_by_days(self):
        s = dict(db.DEFAULT_SETTINGS, residence=[{"from": "2024-01-01", "region": "valencia"},
                                                 {"from": "2027-03-01", "region": "asturias"}])
        self.assertEqual(tax.region_for_year(s, 2027), "asturias")
        s["residence"][1]["from"] = "2027-10-01"
        self.assertEqual(tax.region_for_year(s, 2027), "valencia")
        self.assertEqual(tax.region_for_year(s, 2028), "asturias")


class Beckham(unittest.TestCase):
    def test_151_strict(self):
        """kb/beckham.md: 60 000 € (10 000 € Spanish client with 24 % retención) → 12 000 € a ingresar (strict)."""
        con, s = setup(beckham_first_year="2025")
        invoice(con, client(con, "ES"), "2025-03-01", "10000", "es_b2b", vat=21, irpf=24)
        invoice(con, client(con, "US"), "2025-06-01", "50000", "extra_eu")
        expense(con, "2025-02-01", "6000")
        self.assertEqual(tax.regime(s, 2030), "beckham")
        self.assertEqual(tax.regime(s, 2031), "general")
        f = tax.beckham_annual(con, s, 2025)
        self.assertEqual(f["result"], 1200000)
        self.assertNotIn("130", [f["modelo"] for _, fs in tax.forms(con, s, 2025) for f in fs])

    def test_payments_by_quarter(self):
        """What the Overview shows: 210 in the quarter it covers, RETA by month, 151 still due = cuota − 210, nothing twice."""
        con, s = setup(beckham_first_year="2025", irnr_paid={"2025-1T": 100000, "2025-3T": 200000})
        year_2025_example(con)  # 60 000 € income, 4 × 900 € RETA
        p = tax.payments(con, s, 2025)
        self.assertEqual([c[0] for c in p["rows"]["210"]], [100000, 0, 200000, 0])
        self.assertEqual([c[0] for c in p["rows"]["RETA"]], [90000] * 4)
        self.assertEqual(p["annual"]["151"], [0, 1440000 - 300000])  # 24 % of 60 000 € minus the 210 already paid
        self.assertEqual((p["paid"], p["due"]), (300000 + 360000, 1140000))


class Iva(unittest.TestCase):
    def test_303_1t_2026_example(self):
        """kb/iva-facturacion.md example 11: result 147,00 €."""
        con, s = setup()
        invoice(con, client(con, "DE"), "2026-01-20", "3000", "eu_b2b")
        invoice(con, client(con, "ES"), "2026-03-05", "2000", "es_b2b", vat=21, irpf=7)
        invoice(con, client(con, "ES", 0), "2026-03-20", "500", "es_b2c", vat=21)
        con.execute("INSERT INTO invoices(series, number, issue_date, client_id, currency, fx_rate, treatment) "
                    "VALUES ('A', 50, '2026-02-10', ?, 'USD', 1.08, 'extra_eu')", (client(con, "US"),))
        con.execute("INSERT INTO invoice_lines(invoice_id, description, unit_price_cents) VALUES (last_insert_rowid(), 'x', 500000)")
        expense(con, "2026-01-05", "300", "rent", "domestic", "63")
        expense(con, "2026-01-06", "1500", "equipment", "domestic", "315")
        expense(con, "2026-02-01", "100", "software", "reverse_non_eu", "21")
        expense(con, "2026-02-02", "200", "software", "reverse_eu", "42")
        f, carry = tax.form_303(con, 2026, 1, 0)
        c = f["c"]
        self.assertEqual((c["27"], c["45"], c["59"], c["120"], c["71"]), (58800, 44100, 300000, 462963, 14700))
        self.assertEqual(carry, 0)

    def test_partial_deduction_keeps_full_base(self):
        """kb/iva-facturacion.md: vehicle lease 400 + 84, 50 % → base 400, cuota deducible 42."""
        con, s = setup()
        expense(con, "2026-01-05", "400", "travel", "domestic", "84", vat_pct=50)
        c = tax.form_303(con, 2026, 1, 0)[0]["c"]
        self.assertEqual((c["28"], c["29"]), (40000, 4200))

    def test_compensation_carry_4t_refund_or_keep(self):
        con, s = setup()
        expense(con, "2026-02-01", "1000", "software", "domestic", "210")
        expense(con, "2026-11-01", "1000", "software", "domestic", "210")
        forms = tax.iva_year(con, s, 2026)
        self.assertEqual([f["result"] for f in forms], [-21000, 0, 0, -42000])
        self.assertEqual(forms[1]["c"]["110"], 21000)
        s["iva_carry"] = {"2027": 42000}  # user keeps the balance instead of a refund
        last = tax.iva_year(con, s, 2026)[3]
        self.assertEqual((last["c"]["78"], last["c"]["71"]), (0, -21000))
        self.assertEqual(tax.iva_year(con, s, 2027)[0]["c"]["110"], 42000)


class Reta(unittest.TestCase):
    def test_tramo_and_regularization(self):
        """kb/reta.md: 48 000 € → G10, base 1 601,31 €, cuota 502,81 €; from G1 minimum → ≈ 2 450,40 € extra."""
        con, s = setup(reta_base=95098, reta_start="2020-01-01")
        f = tax.reta_estimate(con, s, 2025, 4800000 - 360000, 360000)
        box = {b[1]: b[2] for b in f["boxes"]}
        self.assertEqual(box["Tramo G10: base mínima"], 160131)
        self.assertEqual(f["result"], 245040)

    def test_tarifa_plana_window_and_part_year(self):
        # alta 2025-07-10 with tarifa plana: covered July 2025 + 12 full months → ordinary from 2026-08-01
        con, s = setup(reta_start="2025-07-10", tarifa_plana=True, reta_base=95098)
        self.assertEqual(tax.reta_days(s, 2025), (175, 0))
        self.assertEqual(tax.reta_days(s, 2026), (365, 153))
        f = tax.reta_estimate(con, s, 2026, 4800000 - 360000, 360000)
        # N = 44 640 € / 153 days × 30 → R ≈ 8 753 €/month → G12, base mín 1 928,10 €; 5 regularizable months
        self.assertEqual(f["result"], tax.pct(192810 - 95098, "31.5") * 5)

    def test_partial_alta_month_counts_by_days(self):
        con, s = setup(reta_start="2026-07-31", reta_base=95098)
        self.assertEqual(tax.reta_days(s, 2026), (154, 154))
        f = tax.reta_estimate(con, s, 2026, 2400000, 0)  # R = 22 320 / 154 × 30 ≈ 4 348 € → G11
        self.assertIn("Tramo G11: base mínima", {b[1] for b in f["boxes"]})


class Sociedad(unittest.TestCase):
    def test_is_micro_rates_and_202(self):
        con, s = setup("sl")
        self.assertEqual(tax.is_rate(s, 2026, 6000000), 1160000)  # 50 000 × 19 % + 10 000 × 21 %
        self.assertEqual(tax.is_rate(s, 2025, 6000000), 1270000)
        invoice(con, client(con, "US"), "2025-05-01", "60000", "extra_eu")
        f202 = tax.forms_202(con, s, 2026)
        self.assertEqual([f["result"] for f in f202], [0, 228600, 228600])  # 18 % of 12 700
        self.assertEqual(tax.is_rate(s, 2024, 6000000), 1380000)  # 2024 micro: 23 % flat

    def test_202_needs_prior_200_and_short_first_period(self):
        con, s = setup("sl", activity_start="2020-01-01")
        f = tax.forms_202(con, s, 2026)
        self.assertTrue(all(x["applies"] for x in f))  # history unknown → must not be silently skipped
        s["sl_200_cuotas"] = {"2025": 1000000}
        self.assertEqual(tax.forms_202(con, s, 2026)[1]["result"], 180000)
        s["activity_start"] = "2026-07-01"  # 184-day first period: 50 000 € band prorated
        self.assertEqual(tax.is_rate(s, 2026, 4000000), tax.scale(4000000, [(0, "19"), (D(50000) * 184 / 365, "21")]))
        self.assertFalse(any(x["applies"] for x in tax.forms_202(con, dict(s, sl_200_cuotas={}), 2026)))

    def test_admin_withholding_defaults_to_35_without_history(self):
        con, s = setup("sl")
        expense(con, "2026-02-01", "10000", "admin_pay")
        f111, _ = tax.forms_withholding(con, s, 2026)
        self.assertEqual(f111[0]["result"], 350000)
        con.execute("UPDATE expenses SET withheld_cents = 350000")  # user also typed the retención → counted once
        self.assertEqual(tax.forms_withholding(con, s, 2026)[0][0]["result"], 350000)

    def test_emergente_windows(self):
        con, s = setup("sl", sl_emergente=True, sl_200_cuotas={"2025": 1000000})
        self.assertEqual(tax.is_rate(s, 2026, 4000000), tax.scale(4000000, tax.IS_MICRO[2026]))  # no year → no 15 %
        s["sl_first_profit_year"] = "2025"
        self.assertEqual(tax.is_rate(s, 2028, 4000000), 600000)
        self.assertNotEqual(tax.is_rate(s, 2029, 4000000), 600000)
        self.assertFalse(any(f["applies"] for f in tax.forms_202(con, s, 2026)))


class Money(unittest.TestCase):
    def test_parse_money(self):
        self.assertEqual([parse_money(x) for x in ("1.000", "1,000", "1.234,56", "1234.5", "10,5", "")],
                         [100000, 100000, 123456, 123450, 1050, 0])
        with self.assertRaises(ValueError):
            parse_money("nan")
        with self.assertRaises(ValueError):
            parse_money("1e309")

    def test_scale_exact_boundary_uses_published_quota(self):
        self.assertEqual(tax.scale(7000000, tax.REGION_SCALES["asturias"][2025]), 1137762)


class Duties(unittest.TestCase):
    def test_regime_and_data_decide_what_is_filed(self):
        con, s = setup(reta_start="2025-01-01")
        invoice(con, client(con, "US"), "2026-02-10", "3000", "extra_eu")
        have, no = tax.duties(con, s, 2026)
        filed = [d["modelo"] for d in have]
        self.assertEqual(filed[:2], ["303", "130"])
        self.assertIn("100", filed)
        self.assertIn("RETA", filed)
        self.assertEqual({d["modelo"] for d in no}, {"349", "347", "111", "115"})
        invoice(con, client(con, "DE"), "2026-05-10", "3000", "eu_b2b")
        self.assertIn("349", [d["modelo"] for d in tax.duties(con, s, 2026)[0]])
        _, no = tax.duties(con, dict(s, beckham_first_year="2025"), 2026)
        reasons = {d["modelo"]: d["ids"] for d in no}
        self.assertIn("aeat-novedades-rd1008-2023", reasons["130"])
        self.assertIn("100", reasons)

    def test_filing_window_opens(self):
        """PENDIENTE starts when AEAT opens the window, not on the last day of the period (202 is filed in Apr/Oct/Dec)."""
        self.assertEqual(tax.opens("303", 2026, 3), "2026-10-01")
        self.assertEqual(tax.opens("130", 2026, 4), "2027-01-01")
        self.assertEqual([tax.opens("202", 2026, q) for q in (1, 2, 3)], ["2026-04-01", "2026-10-01", "2026-12-01"])
        self.assertEqual(tax.opens("100", 2026, 0), "2027-04-01")


class WarningsYears(unittest.TestCase):
    @staticmethod
    def verifactu(kind, on):
        class Fixed(date):
            @classmethod
            def today(cls):
                return on
        con, s = setup(kind)
        with mock.patch.object(tax, "date", Fixed):
            return [w for w in tax.warnings(con, s, on.year) if w.startswith("Verifactu")]

    def test_sl_gets_verifactu_with_is_date(self):
        w = self.verifactu("sl", date(2026, 10, 13))
        self.assertEqual(len(w), 1)
        self.assertTrue(w[0].startswith("Verifactu для SL (плательщиков Impuesto sobre Sociedades) — с 01.01.2027."), w[0])
        self.assertIn("перенос на 10.2028", w[0])

    def test_warning_stays_after_the_date(self):
        w = self.verifactu("autonomo", date(2027, 7, 2))
        self.assertEqual(len(w), 1)
        self.assertTrue(w[0].startswith("Verifactu для autónomos обязателен с 01.07.2027."), w[0])
        self.assertIn("перенос на 10.2028", w[0])
        self.assertTrue(self.verifactu("sl", date(2027, 1, 1))[0].startswith("Verifactu для SL (плательщиков Impuesto sobre Sociedades) обязателен с 01.01.2027."))

    def test_reta_year_without_tables_says_which_year_was_used(self):
        con, s = setup(reta_base=95098, reta_start="2020-01-01")
        note = "Таблиц RETA за 2027 в gestor нет (не опубликованы или не внесены) — расчёт по таблицам 2026 года: tramos, базы, ставка."
        self.assertIn(note, tax.reta_estimate(con, s, 2027, 4800000 - 360000, 360000)["notes"])
        self.assertFalse(any("Таблиц RETA" in n for n in tax.reta_estimate(con, s, 2026, 4800000 - 360000, 360000)["notes"]))


class Holidays(unittest.TestCase):
    def test_deadline_on_national_holiday_moves_to_next_working_day(self):
        """Art. 30.5 Ley 39/2015: 31.12.2028 is a Sunday and 01.01.2029 a national holiday → Tuesday 02.01.2029."""
        self.assertEqual(tax.deadline("RETA", 2027, 0), "2029-01-02")
        self.assertEqual(tax.business_day(date(2028, 4, 30)), date(2028, 5, 2))  # SL libros: Sunday, then 1 May
        self.assertEqual(tax.business_day(date(2026, 4, 3)), date(2026, 4, 6))   # Viernes Santo 2026 (BOE-A-2025-23702)
        self.assertEqual(tax.business_day(date(2026, 10, 12)), date(2026, 10, 13))

    def test_working_days_and_aeat_calendar_dates_stay(self):
        """AEAT calendars 2025/2026; Easter Monday is only regional, so 20.04.2025 (Sunday) ends on 21.04.2025."""
        self.assertEqual([tax.deadline("303", 2026, q) for q in (1, 2, 3)], ["2026-04-20", "2026-07-20", "2026-10-20"])
        self.assertEqual(tax.deadline("130", 2025, 4), "2026-01-30")
        self.assertEqual(tax.deadline("303", 2025, 1), "2025-04-21")
        self.assertEqual(tax.business_day(date(2026, 4, 2)), date(2026, 4, 2))  # Jueves Santo is not national



class RegionScales(unittest.TestCase):
    def cuota_0546(self, region, year=2025):
        """42 000 € income, no expenses → GDJ 2 000 (cap) → base 40 000 €."""
        con, s = setup(residence=[{"from": "2020-01-01", "region": region}])
        invoice(con, client(con, "US"), f"{year}-06-01", "42000", "extra_eu")
        f100 = tax.irpf_annual(con, s, year, 0)
        box = {b[0]: b[2] for b in f100["boxes"]}
        self.assertEqual(box["0435"], 4000000)
        return box["0546"], f100["notes"]

    def test_cuota_autonomica_on_40000_base_2025(self):
        # Madrid, art. 1/2 DLeg 1/2010: 3 841,42 + (40 000 − 35 425,68) × 17,4 % = 4 637,35;
        #   mínimo 5 956,65 × 8,5 % = 506,32; 4 637,35 − 506,32 = 4 131,03
        # Cataluña, art. 611-1/611-2: 4 135 + (40 000 − 33 000) × 19 % = 5 465; 5 550 × 9,5 % = 527,25 → 4 937,75
        # Andalucía, art. 23/23 bis Ley 5/2021: 4 322 + (40 000 − 35 200) × 18,5 % = 5 210; 5 790 × 9,5 % = 550,05 → 4 659,95
        # (old code: state scale 5 250,75 − 527,25 = 4 723,50 for all three)
        for region, expected in (("madrid", 413103), ("cataluna", 493775), ("andalucia", 465995)):
            with self.subTest(region):
                self.assertEqual(self.cuota_0546(region)[0], expected)

    def test_2026_reuses_unchanged_scale_without_fallback_note(self):
        for region in ("madrid", "cataluna", "andalucia"):
            with self.subTest(region):
                cuota, notes = self.cuota_0546(region, 2026)
                self.assertEqual(cuota, self.cuota_0546(region)[0])
                self.assertFalse([n for n in notes if "не опубликована" in n or "без своей таблицы" in n])


class Form390Rates(unittest.TestCase):
    def test_mixed_rate_year_one_box_per_casilla(self):
        """DR390 2025: 4/10/21 % → 01/02, 03/04, 05/06; per-rate deducible lines; totals = sum of the four 303."""
        con, s = setup()
        es = client(con, "ES", 0)
        invoice(con, es, "2026-02-10", "1000", "es_b2c", vat=21)
        invoice(con, es, "2026-05-10", "500", "es_b2c", vat=10)
        invoice(con, es, "2026-08-10", "200", "es_b2c", vat=4)
        invoice(con, es, "2026-11-10", "300", "es_b2c", vat=21)
        invoice(con, es, "2026-11-11", "100", "es_b2c", vat=10)
        for day, amount, category, kind, vat, rate in (("2026-01-05", "200", "software", "domestic", "42", 21),
                                                       ("2026-04-05", "100", "software", "domestic", "10", 10),
                                                       ("2026-04-06", "5000", "equipment", "reverse_eu", "1050", 21),
                                                       ("2026-07-05", "300", "software", "reverse_eu", "63", 21),
                                                       ("2026-10-05", "4000", "equipment", "domestic", "840", 21)):
            expense(con, day, amount, category, kind, vat)
            con.execute("UPDATE expenses SET vat_rate = ? WHERE id = last_insert_rowid()", (rate,))
        iva = tax.iva_year(con, s, 2026)
        f = tax.form_390(con, 2026, iva)
        box = {b[0]: b[2] for b in f["boxes"]}
        self.assertEqual(len(box), len(f["boxes"]))  # one box per casilla, no shared range labels like «01–06»
        self.assertEqual(box, {
            "01": 20000, "02": 800, "03": 60000, "04": 6000, "05": 130000, "06": 27300,
            "25": 500000, "26": 105000, "551": 30000, "552": 6300, "33": 740000, "34": 145400, "47": 145400,
            "605": 20000, "606": 4200, "603": 10000, "604": 1000, "48": 30000, "49": 5200,
            "613": 400000, "614": 84000, "50": 400000, "51": 84000,
            "633": 500000, "634": 105000, "58": 500000, "59": 105000,
            "637": 30000, "638": 6300, "597": 30000, "598": 6300,
            "64": 200500, "65": -55100, "84": -55100, "86": -55100, "95": 21600, "98": 76700, "99": 210000, "108": 210000})
        total = lambda k: sum(q["c"][k] for q in iva)
        for b390, b303 in (("02", "03"), ("04", "06"), ("06", "09"), ("34", "27"), ("49", "29"), ("51", "31"), ("59", "39"),
                           ("598", "37"), ("64", "45"), ("65", "46")):
            self.assertEqual(box[b390], total(b303), b390)
        self.assertEqual(f["result"], sum(q["result"] for q in iva))
        self.assertEqual(f["notes"], [])


if __name__ == "__main__":
    unittest.main()
