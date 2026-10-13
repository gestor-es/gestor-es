"""Legal-source registry: every § shown in the UI must resolve to a complete, checkable entry.
Run: python3 -m unittest tests.test_sources -v"""
import io
import re
import tempfile
import unittest
from pathlib import Path

from gestor import db, rules, sources, tax
from gestor.web import make_app

REQUIRED = ("kind", "ref", "title_ru", "url", "summary_ru", "status", "checked", "quote_es", "quote_ru")
CODE = Path(__file__).parent.parent / "gestor"


def get(app, path, entity):
    env = {"REQUEST_METHOD": "GET", "PATH_INFO": path.split("?")[0], "QUERY_STRING": path.partition("?")[2],
           "HTTP_COOKIE": f"entity={entity}", "wsgi.input": io.BytesIO()}
    status = []
    body = b"".join(app(env, lambda s, h: status.append(s)))
    return status[0], body.decode()


class Registry(unittest.TestCase):
    def test_entries_are_complete(self):
        self.assertGreater(len(sources.SOURCES), 50)
        for sid, e in sources.SOURCES.items():
            with self.subTest(sid):
                for k in REQUIRED:
                    self.assertTrue(e.get(k), f"{sid}: no {k}")
                self.assertIn(e["status"], sources.STATUS)
                self.assertTrue(e["url"].startswith("https://"))
                if e["status"] != "verified":
                    self.assertTrue(e.get("status_note"), f"{sid}: uncertain entry must say why")
                self.assertIn(e["kind"], sources.KINDS)
                for pid in e.get("practice", []):
                    self.assertIn(pid, sources.SOURCES, f"{sid}: practice {pid} missing")

    def test_every_configured_and_literal_reference_exists(self):
        """Covers ids on branches no fixture renders (e.g. rectificativa invoices)."""
        ids = [i for m in (tax.FORM_SOURCES, tax.BOX_SOURCES, rules.VISA_SOURCES, rules.VAT_KIND_SOURCES) for v in m.values() for i in v]
        ids += [i for m in (rules.TREATMENTS, rules.EXPENSE_CATEGORIES) for v in m.values() for i in v.get("sources", [])]
        for name in ("tax.py", "web.py"):  # source ids always contain "-"; skips doc examples like [[ids]]
            ids += [i for i in sources.split_cites((CODE / name).read_text())[1] if "-" in i]
        ids += [i for lst in re.findall(r"\[('[a-z0-9]+-[a-z0-9-]+'(?:, '[a-z0-9]+-[a-z0-9-]+')*)\]", (CODE / "web.py").read_text())
                for i in re.findall(r"'([a-z0-9-]+)'", lst)]
        self.assertGreater(len(ids), 100)
        self.assertEqual([i for i in ids if i not in sources.SOURCES], [])

    def test_loader_rejects_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "a.json").write_text('{"x": {}, "x": {}}')
            with self.assertRaisesRegex(ValueError, "a.json.*x"):
                sources.load(d)
            (d / "a.json").write_text('{"x": {}}')
            (d / "b.json").write_text('{"x": {}}')
            with self.assertRaisesRegex(ValueError, "b.json.*x.*a.json"):
                sources.load(d)

    def test_for_year_keeps_only_applicable_annual_sources(self):
        ids = ["orden-pjc-178-2025", "orden-pjc-297-2026", "lgss-308"]
        self.assertEqual(sources.for_year(ids, 2026), ["orden-pjc-297-2026", "lgss-308"])
        self.assertEqual(sources.for_year(ids, 2025), ["orden-pjc-178-2025", "lgss-308"])

    def test_auto_translate_keeps_page_and_anchor(self):
        self.assertEqual(sources.auto_tr("https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a93"),
                         "https://www-boe-es.translate.goog/buscar/act.php?id=BOE-A-2006-20764"
                         "&_x_tr_sl=es&_x_tr_tl=ru&_x_tr_hl=ru#a93")
        self.assertTrue(sources.auto_tr("https://sede.agenciatributaria.gob.es/Sede/x.html")
                        .startswith("https://sede-agenciatributaria-gob-es.translate.goog/Sede/x.html?"))

    def test_split_cites(self):
        self.assertEqual(sources.split_cites("Текст. [[liva-69, liva-84]]"), ("Текст.", ["liva-69", "liva-84"]))


class EveryCitationResolves(unittest.TestCase):
    """Render the pages of every profile type; no § may point to a missing source."""

    def test_pages(self):
        with tempfile.TemporaryDirectory() as tmp:
            data = Path(tmp)
            for entity, settings in (("general", {}), ("beckham", {"beckham_first_year": "2025", "visa": "nomada_digital"}),
                                     ("sl", {"kind": "sl", "sl_emergente": True}), ("cuenta", {"visa": "cuenta_propia"})):
                con = db.connect(data / f"{entity}.db")
                db.save_settings(con, dict(settings, name="T", tax_id="X1", address="A", reta_start="2026-01-01",
                                           tarifa_plana=True, residence=[{"from": "2024-01-01", "region": "valencia"},
                                                                         {"from": "2026-06-01", "region": "asturias"}]))
                con.execute("INSERT INTO clients(name, tax_id, country, is_business, address) VALUES ('C', 'DE1', 'DE', 1, 'x')")
                con.execute("INSERT INTO invoices(series, number, issue_date, client_id, treatment, parties) "
                            "VALUES ('A2026', 1, '2026-02-01', 1, 'eu_b2b', '')")
                con.execute("INSERT INTO invoice_lines(invoice_id, description, unit_price_cents) VALUES (1, 'x', 100000)")
                for cat, kind in (("software", "reverse_eu"), ("rent", "domestic"), ("admin_pay", "none"), ("reta", "none")):
                    con.execute("INSERT INTO expenses(date, supplier, category, vat_kind, base_cents, vat_cents, withheld_cents) "
                                "VALUES ('2026-03-01', 'S', ?, ?, 10000, 2100, 1900)", (cat, kind))
                con.close()
            app = make_app(data)
            for entity in ("general", "beckham", "sl", "cuenta"):
                for path in ("/", "/taxes?year=2026", "/settings", "/expenses/new", "/invoices/1", "/sources", "/guide"):
                    with self.subTest(entity=entity, path=path):
                        status, html = get(app, path, entity)
                        self.assertEqual(status, "200 OK")
                        self.assertNotIn("источник не найден", html)
                        self.assertRegex(html, r'class=src |class="cite |<div class=explain>.*?href="/sources#')
            taxes = get(app, "/taxes?year=2026", "general")[1]  # annual orders: only the 2026 one applies
            self.assertIn("Orden PJC/297/2026", taxes)
            self.assertNotIn("Orden PJC/178/2025", taxes)


if __name__ == "__main__":
    unittest.main()
