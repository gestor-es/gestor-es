"""Rendering helpers whose mistakes would corrupt data, and the HTTP guards. Run: python3 -m unittest tests.test_web -v"""
import io
import tempfile
import unittest
from pathlib import Path

from gestor import db
from gestor.core import invoice_number, series_key
from gestor.web import make_app, ru_dates


def call(app, method, path, host="127.0.0.1:8765", body=b"", ctype="application/x-www-form-urlencoded"):
    seen = {}
    env = {"REQUEST_METHOD": method, "PATH_INFO": path, "QUERY_STRING": "", "HTTP_HOST": host, "CONTENT_TYPE": ctype,
           "CONTENT_LENGTH": str(len(body)), "wsgi.input": io.BytesIO(body)}
    out = b"".join(app(env, lambda status, headers: seen.update(status=status, headers=dict(headers))))
    return seen["status"], seen["headers"], out


class HttpGuards(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.data = Path(self.tmp.name)
        con = db.connect(self.data / "main.db")
        con.execute("INSERT INTO clients(name, tax_id, country, address) VALUES ('C', 'ESB1', 'ES', 'x')")
        con.execute("INSERT INTO expenses(date, supplier, category, base_cents) VALUES ('2026-03-01', 'S', 'software', 1000)")
        con.close()
        self.app = make_app(self.data)

    def tearDown(self):
        self.tmp.cleanup()

    def rows(self, sql):
        con = db.connect(self.data / "main.db")
        try:
            return con.execute(sql).fetchall()
        finally:
            con.close()

    def test_only_loopback_host(self):
        """DNS rebinding: a page on evil.example resolving to 127.0.0.1 must not read the books."""
        self.assertEqual(call(self.app, "GET", "/", host="evil.example:8765")[0], "403 Forbidden")
        self.assertEqual(call(self.app, "GET", "/", host="localhost:8765")[0], "200 OK")

    def test_active_receipts_are_downloaded_not_rendered(self):
        (self.data / "receipts").mkdir()
        (self.data / "receipts" / "a.html").write_text("<script>alert(1)</script>")
        (self.data / "receipts" / "b.pdf").write_bytes(b"%PDF-1.4")
        _, html_h, _ = call(self.app, "GET", "/receipts/a.html")
        _, pdf_h, _ = call(self.app, "GET", "/receipts/b.pdf")
        self.assertEqual((html_h["Content-Type"], html_h["Content-Disposition"][:10]), ("application/octet-stream", "attachment"))
        self.assertEqual((pdf_h["Content-Type"], pdf_h["Content-Disposition"][:6]), ("application/pdf", "inline"))
        self.assertEqual(html_h["X-Content-Type-Options"], "nosniff")

    def test_unsupported_vat_rate_is_refused(self):
        """A 22 % invoice would print IVA but vanish from every 303 bucket."""
        body = b"client_id=1&issue_date=2026-03-01&treatment=es_b2b&vat_rate=22&irpf_rate=15&desc0=x&qty0=1&price0=100"
        self.assertEqual(call(self.app, "POST", "/invoices/new", body=body)[0], "400 Bad Request")
        self.assertEqual(self.rows("SELECT count(*) FROM invoices")[0][0], 0)

    def test_failed_request_leaves_books_unchanged(self):
        """The expense row is updated before the receipt file is written; if the write fails, the update is rolled back."""
        (self.data / "receipts").write_text("not a folder")  # writing the receipt will fail
        sep = b"--b"
        fields = {"date": "2026-03-01", "supplier": "Changed", "category": "software", "vat_kind": "domestic",
                  "base": "10", "vat_rate": "21"}
        body = b"".join(sep + f'\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode() for k, v in fields.items())
        body += sep + b'\r\nContent-Disposition: form-data; name="receipt"; filename="r.pdf"\r\n\r\n%PDF\r\n' + sep + b"--\r\n"
        with self.assertRaises(OSError):
            call(self.app, "POST", "/expenses/1", body=body, ctype="multipart/form-data; boundary=b")
        self.assertEqual(self.rows("SELECT supplier FROM expenses WHERE id = 1")[0][0], "S")


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
