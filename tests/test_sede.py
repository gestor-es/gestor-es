"""Sede import files: positions and encodings from the AEAT «diseños de registro». Run: python3 -m unittest tests.test_sede -v"""
import unittest

from gestor import sede, tax
from tests.test_tax import client, expense, invoice, setup


def at(rec: str, pos: int, length: int = 17) -> str:
    return rec[pos - 1:pos - 1 + length]


def forms(con, s, modelo):
    return {f["period"]: f for _, fs in tax.forms(con, s, 2026) for f in fs if f["modelo"] == modelo}


class SpecTest(unittest.TestCase):
    def test_pages_are_contiguous_and_match_declared_length(self):
        for name in ("130", "303-2026", "151-2023"):
            for page, p in sede.spec(name)["pages"].items():
                pos = 1
                for f in sorted(p["fields"], key=lambda x: x["pos"]):
                    self.assertEqual(f["pos"], pos, f"{name} {page}: hueco antes de {f['pos']}")
                    pos += f["len"]
                if p["declared_length"]:
                    self.assertEqual(pos - 1, p["declared_length"], f"{name} {page}")


class FieldTest(unittest.TestCase):
    num = {"len": 17, "type": "N", "const": None, "desc": "x"}

    def test_signed_amount_and_errors(self):
        self.assertEqual(sede.field(self.num, -11025), "N0000000000011025")
        self.assertEqual(sede.field(self.num, 945), "00000000000000945")
        with self.assertRaises(ValueError):
            sede.field(dict(self.num, type="Num"), -1)
        with self.assertRaises(ValueError):
            sede.field(dict(self.num, len=3), 12345)

    def test_latin(self):
        self.assertEqual(sede.latin("Núñez-García, José"), "NUÑEZ GARCIA JOSE")
        self.assertEqual(sede.latin("O’Brien (Pty) Ltd."), "O BRIEN PTY LTD")
        self.assertEqual(sede.latin("Иван"), "")


class FilesTest(unittest.TestCase):
    def setUp(self):
        self.con, self.s = setup(name="Petrov, Ivan", iban="ES91 2100 0418 4502 0005 1332")
        us, de = client(self.con, "US"), client(self.con, "DE")
        for m in (2, 5, 8, 11):
            invoice(self.con, us, f"2026-{m:02d}-15", "6000", "extra_eu")
            invoice(self.con, de, f"2026-{m:02d}-16", "1000", "eu_b2b")
            expense(self.con, f"2026-{m:02d}-10", "1000", vat_kind="domestic", vat="210")

    def test_303_compensar(self):
        f = forms(self.con, self.s, "303")["3T"]
        t = sede.file_303(self.s, f).decode("iso-8859-1")
        self.assertEqual(len(t), 328 + 1581 + 1017 + 823 + 18)
        self.assertTrue(t.startswith("<T303020263T0000><AUX>") and t.endswith("</T303020263T0000>"))
        p1, p3 = t[328:328 + 1581], t[328 + 1581:328 + 1581 + 1017]
        self.assertEqual(at(p1, 13, 1), "C")                     # negative before 4T: a compensar
        self.assertEqual(at(p1, 730), "00000000000021000")       # [29] cuota deducible interior, 210.00 €
        self.assertEqual(at(p1, 1019), "N0000000000021000")      # [46]
        self.assertEqual(at(p3, 12), "00000000000100000")        # [59] servicios UE
        self.assertEqual(at(p3, 216, 5), "10000")                # [65] 100 %
        self.assertEqual(at(p3, 408), "N0000000000021000")       # [71]
        self.assertEqual((at(p1, 109, 9), at(p1, 127, 4)), ("223222  2", "2000"))  # flags outside 4T: no prorrata, 390, volumen
        self.assertEqual(at(p3, 425, 1), " ")                    # there is activity
        self.assertEqual(t[328 + 1581 + 1017 + 22:328 + 1581 + 1017 + 56].strip(), "")  # no IBAN unless refund

    def test_303_4t_refund_carries_iban(self):
        f = forms(self.con, self.s, "303")["4T"]
        t = sede.file_303(self.s, f).decode("iso-8859-1")
        did = t[328 + 1581 + 1017:328 + 1581 + 1017 + 823]
        self.assertEqual(at(t[328:], 13, 1), "D")
        self.assertEqual((at(t[328:], 115, 2), at(t[328:], 128, 1)), ("22", "2"))  # 4T: prorrata especial no, 390 not exonerated
        self.assertEqual(at(did, 23, 34).strip(), "ES9121000418450200051332")
        self.assertEqual(at(did, 194, 1), "1")
        lt = sede.file_303(dict(self.s, iban="LT12 1000 0111 0100 1000"), f).decode("iso-8859-1")
        self.assertEqual(lt[328 + 1581 + 1017 + 193], "2")       # SEPA outside Spain

    def test_130_casillas(self):
        f = forms(self.con, self.s, "130")["3T"]
        box = {b[0]: b[2] for b in f["boxes"]}
        t = sede.file_130(self.s, f).decode("iso-8859-1")
        self.assertEqual(len(t), 946)
        r = t[328:928]
        self.assertEqual(at(r, 13, 1), "I")
        self.assertEqual((at(r, 23, 60).strip(), at(r, 83, 20).strip()), ("PETROV", "IVAN"))
        self.assertEqual(int(at(r, 143)), box["03"])             # [03] rendimiento neto
        self.assertEqual(at(r, 381), at(r, 415))                 # [17] = [19] without a complementaria
        self.assertEqual(int(at(r, 415)), f["result"])           # [19]

    def test_349_records(self):
        self.con.execute("UPDATE clients SET tax_id = '123456789' WHERE country = 'DE'")  # number without prefix: country from client
        self.con.execute("""INSERT INTO expenses(date, supplier, supplier_tax_id, category, vat_kind, base_cents, vat_cents)
                            VALUES ('2026-08-03', 'Example Supplier Ltd', 'IE 1234567AB', 'software', 'reverse_eu', 1500, 315)""")
        f = forms(self.con, self.s, "349")["3T"]
        head, *ops = sede.file_349(self.s, f).decode("iso-8859-1").split("\r\n")
        self.assertEqual([len(r) for r in [head] + ops], [500, 500, 500])
        self.assertEqual((head[:17], head[17:57].strip(), head[135:137]), ("13492026X0000000T", "PETROV IVAN", "3T"))
        self.assertEqual((head[137:146], head[146:161]), ("000000002", "000000000101500"))  # 2 operators, 1015.00 €
        s_op = next(r for r in ops if r[132] == "S")
        i_op = next(r for r in ops if r[132] == "I")
        self.assertEqual((s_op[75:77], s_op[77:92].strip(), s_op[133:146]), ("DE", "123456789", "0000000100000"))
        self.assertEqual((i_op[75:77], i_op[77:92].strip(), i_op[92:132].strip()), ("IE", "1234567AB", "EXAMPLE SUPPLIER LTD"))

    def test_349_needs_eu_vat_id(self):
        self.con.execute("""INSERT INTO expenses(date, supplier, supplier_tax_id, category, vat_kind, base_cents, vat_cents)
                            VALUES ('2026-08-03', 'Somebody', '1234567', 'software', 'reverse_eu', 1500, 315)""")
        with self.assertRaises(ValueError):
            sede.file_349(self.s, forms(self.con, self.s, "349")["3T"])

    def test_151_beckham(self):
        s = dict(self.s, beckham_first_year="2026", residence=[{"from": "2025-01-01", "region": "valencia"}])
        f = next(f for _, fs in tax.forms(self.con, s, 2026) for f in fs if f["modelo"] == "151")
        t = sede.file_151(s, f).decode("iso-8859-1")
        self.assertEqual(len(t), 328 + 1150 + 800 + 800 + 1350 + 500 + 18)
        self.assertTrue(t.startswith("<T15102026" + "0A0000><AUX>"))
        p1, p5 = t[328:1478], t[1478:2278]
        p6, p10 = t[2278:3078], t[3078:4428]
        self.assertEqual((at(p1, 13, 1), at(p1, 983, 2), at(p5, 13, 2), at(p5, 117, 1)), ("I", "17", "12", "1"))
        self.assertEqual(int(at(p5, 15)), 28000_00)               # [02] ingresos: 4 × (6 000 + 1 000)
        self.assertEqual(int(at(p6, 648)), 28000_00)              # [08] total rendimientos netos
        self.assertEqual(int(at(p10, 825)), 6720_00)              # [19] 24 %
        self.assertEqual(int(at(p10, 876)) + int(at(p10, 893)), 6720_00)  # [22] + [23]
        self.assertEqual(int(at(p10, 1233)), f["result"])         # [43]

    def test_151_credits_voluntary_210(self):
        s = dict(self.s, beckham_first_year="2026", residence=[{"from": "2025-01-01", "region": "valencia"}],
                 irnr_paid={"2026-1T": 3000_00, "2026-2T": 4000_00})
        f = next(f for _, fs in tax.forms(self.con, s, 2026) for f in fs if f["modelo"] == "151")
        self.assertEqual(f["result"], 6720_00 - 7000_00)          # refund, not 6 720 € to pay
        p10 = sede.file_151(s, f).decode("iso-8859-1")[3078:4428]
        self.assertEqual((int(at(p10, 1080)), int(at(p10, 1131))), (7000_00, 7000_00))  # [34] and Epígrafe B [37]
        self.assertEqual(at(p10, 1233), "N0000000000028000")      # [43] −280,00 €


if __name__ == "__main__":
    unittest.main()
