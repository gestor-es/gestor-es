"""Rendering helpers whose mistakes would corrupt data. Run: python3 -m unittest tests.test_web -v"""
import unittest

from gestor.core import invoice_number, series_key
from gestor.web import ru_dates


class DatesTest(unittest.TestCase):
    def test_text_is_dmy_but_inputs_and_textareas_stay_iso(self):
        html = ('<p>до 2026-10-20</p><input type=date value="2026-10-20"><a href="/x?d=2026-10-20">2026-10-20</a>'
                '<textarea name=notes>оплата 2026-10-01</textarea><p>ref 12026-10-201</p>')
        self.assertEqual(ru_dates(html),
                         '<p>до 20.10.2026</p><input type=date value="2026-10-20"><a href="/x?d=2026-10-20">20.10.2026</a>'
                         '<textarea name=notes>оплата 2026-10-01</textarea><p>ref 12026-10-201</p>')


class NumberTest(unittest.TestCase):
    def test_template_and_legacy_prefix(self):
        key = series_key("FACT-{YYYY}-{NNNNN}", "2026")
        self.assertEqual(invoice_number({"series": key, "number": 8}), "FACT-2026-00008")
        self.assertEqual(invoice_number({"series": series_key("A", "2026"), "number": 12}), "A2026-0012")  # old profiles unchanged
        self.assertEqual(invoice_number({"series": key, "number": None}), "черновик")


if __name__ == "__main__":
    unittest.main()
