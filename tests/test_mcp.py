"""MCP server: what Claude Code / Codex read must equal the engine. Run: python3 -m unittest tests.test_mcp -v"""
import io
import json
import tempfile
import unittest
from pathlib import Path

from gestor import db, sede, tax
from gestor.mcp import Gestor, serve
from tests.test_tax import client, expense, invoice


def rpc(g, *msgs):
    out = io.StringIO()
    serve(g, io.StringIO("".join(json.dumps(m) + "\n" for m in msgs)), out)
    return [json.loads(line) for line in out.getvalue().splitlines()]


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


if __name__ == "__main__":
    unittest.main()
