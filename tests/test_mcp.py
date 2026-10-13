"""MCP server: what Claude Code / Codex read and write must equal the engine and the web form. Run: python3 -m unittest tests.test_mcp -v"""
import io
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from gestor import db, sede, tax
from gestor.mcp import Gestor, serve
from tests.test_tax import client, expense, invoice


def rpc(g, *msgs):
    out = io.StringIO()
    serve(g, io.StringIO("".join(json.dumps(m) + "\n" for m in msgs)), out)
    return [json.loads(line) for line in out.getvalue().splitlines()]


def call(g, tool, **arguments):
    """One tool call → (data, error text or None)."""
    (r,) = rpc(g, {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool, "arguments": arguments}})
    r = r["result"]
    return r.get("structuredContent"), (r["content"][0]["text"] if r.get("isError") else None)


class McpTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        data = Path(self.dir.name)
        con = db.connect(data / "t.db")
        db.save_settings(con, dict(db.DEFAULT_SETTINGS, kind="autonomo", name="Test", tax_id="X0000000T", activity_start="2020-01-01"))
        us = client(con, "US")
        invoice(con, us, "2026-08-15", "6000", "extra_eu")
        expense(con, "2026-08-10", "1000", vat_kind="domestic", vat="210")
        self.s, self.con, self.g = db.get_settings(con), con, Gestor(data, "t")

    def tearDown(self):
        self.con.close()
        self.dir.cleanup()

    def test_casillas_and_file_equal_engine(self):
        init, call, unknown = rpc(self.g,
                                  {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18"}},
                                  {"jsonrpc": "2.0", "method": "notifications/initialized"},
                                  {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                                   "params": {"name": "declaration", "arguments": {"modelo": "303", "year": 2026, "period": "3T"}}},
                                  {"jsonrpc": "2.0", "id": 3, "method": "server/discover"})
        self.assertEqual(init["result"]["protocolVersion"], "2025-06-18")
        self.assertEqual(unknown["error"]["code"], -32601)  # 2026-07-28 clients fall back to initialize on this
        d = call["result"]["structuredContent"]
        f = next(f for _, fs in tax.forms(self.con, self.s, 2026) for f in fs if f["modelo"] == "303" and f["period"] == "3T")
        self.assertEqual([(c["casilla"], c["cents"]) for c in d["casillas"]], [(b[0], b[2]) for b in f["boxes"]])
        self.assertEqual(d["result"], "-210,00")  # Sede format: comma decimals, no thousands separator
        self.assertEqual(Path(d["sede_file"]).read_bytes(), sede.file_303(self.s, f))

    def test_unknown_return_is_a_tool_error(self):
        (r,) = rpc(self.g, {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                            "params": {"name": "declaration", "arguments": {"modelo": "200", "year": 2026, "period": "0A"}}})
        self.assertTrue(r["result"]["isError"])

    def test_no_profile_is_a_tool_error_and_creates_nothing(self):
        data = Path(self.dir.name) / "missing"
        (r,) = rpc(Gestor(data, "main"), {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                          "params": {"name": "declarations", "arguments": {"year": 2026}}})
        self.assertTrue(r["result"]["isError"])
        self.assertFalse(data.exists())

    def test_empty_profile_gets_no_amounts_and_no_late(self):
        db.connect(Path(self.dir.name) / "new.db").close()  # what the web interface leaves after the first visit
        g, y = Gestor(Path(self.dir.name), "new"), date.today().year  # this year always has a 4T still ahead and past deadlines
        (lst, one) = rpc(g, {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "declarations", "arguments": {"year": y}}},
                         {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                          "params": {"name": "declaration", "arguments": {"modelo": "303", "year": y, "period": "4T"}}})
        d = lst["result"]["structuredContent"]
        self.assertEqual(d["profile_incomplete"], ["name", "tax_id", "activity_start"])
        self.assertTrue(d["declarations"])
        for r in d["declarations"]:
            self.assertNotIn("status", r)
            self.assertNotIn("result", r)
            self.assertGreaterEqual(r["deadline"], date.today().isoformat())
        self.assertTrue(one["result"]["isError"])

    def test_without_books_a_passed_deadline_is_not_late(self):  # same rule as web.stamp
        call(self.g, "profile_create", name="fresh")
        call(self.g, "profile_update", profile="fresh", fields={"name": "N", "tax_id": "X1", "activity_start": "2020-01-01"})
        y = date.today().year - 1
        statuses = {d["status"] for d in call(self.g, "declarations", profile="fresh", year=y)[0]["declarations"]}
        self.assertNotIn("late", statuses)
        self.assertIn("no books", statuses)

    def test_second_profile_is_created_filled_and_kept_apart(self):
        self.assertEqual(call(self.g, "profile_create", name="SL")[0], {"profile": "sl"})
        _, err = call(self.g, "profile_update", profile="sl", fields={"kind": "sl", "name": "Acme SL", "activity_start": "2026-13-01"})
        self.assertIn("2026-13-01", err)
        self.assertEqual(call(self.g, "profile", profile="sl")[0]["fields"]["name"], "")  # a rejected update writes nothing
        d, _ = call(self.g, "profile_update", profile="sl",
                    fields={"kind": "sl", "name": "Acme SL", "tax_id": "b12345678", "censo": ["303", "111"], "sl_emergente": True})
        self.assertEqual(d["incomplete"], ["activity_start"])  # an SL needs its start date too: first period, 202
        d, err = call(self.g, "profile_update", profile="sl", fields={"activity_start": "2026-02-01"})
        self.assertIsNone(err)
        self.assertEqual(d["incomplete"], [])
        s = call(self.g, "profile", profile="sl")[0]["fields"]
        self.assertEqual((s["tax_id"], s["censo"], s["sl_emergente"]), ("B12345678", ["303", "111"], True))
        self.assertEqual(call(self.g, "profile")[0]["fields"]["name"], "Test")  # the default profile is untouched
        self.assertEqual([p["profile"] for p in call(self.g, "profiles")[0]["profiles"]], ["sl", "t"])
        self.assertIn("unknown fields", call(self.g, "profile_update", fields={"nombre": "x"})[1])
        self.assertIn("no gestor profile", call(self.g, "books", profile="../t", year=2026)[1])

    def test_issued_invoice_is_never_changed_or_deleted(self):
        cid = call(self.g, "client_save", name="Beta GmbH", country="DE", tax_id="DE123456789", address="Berlin")[0]["id"]
        inv, err = call(self.g, "invoice_draft_save", client_id=cid, issue_date="2026-09-01",
                        lines=[{"description": "Consulting", "quantity": 2, "price": "1000,00"}])
        self.assertIsNone(err)
        self.assertEqual((inv["number"], inv["treatment"], inv["total_eur"]), (None, "eu_b2b", "2000,00"))
        self.con.execute("UPDATE invoices SET number = 1 WHERE id = ?", (inv["id"],))  # issued in the web interface
        _, err = call(self.g, "invoice_draft_save", id=inv["id"], client_id=cid, issue_date="2026-09-01",
                      lines=[{"description": "Other", "price": 1}])
        self.assertIsNotNone(err)
        self.assertIsNotNone(call(self.g, "invoice_draft_delete", id=inv["id"])[1])
        self.assertEqual([l["description"] for l in db.invoice_lines(self.con, inv["id"])], ["Consulting"])


if __name__ == "__main__":
    unittest.main()
