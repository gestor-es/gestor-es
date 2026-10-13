"""Every Russian string the app shows has an English and a Spanish translation that keeps its placeholders and citations."""
import ast
import re
import unittest
from pathlib import Path

from gestor import i18n, sources

PKG = Path(__file__).parent.parent / "gestor"
CYR = re.compile(r"[А-Яа-яЁё]")
PLACEHOLDER = re.compile(r"\{[^{}]*\}|\[\[[^\]]*\]\]")


def scan():
    """(msgids marked with _() or N_(), Russian literals outside them as 'file:line')."""
    msgids, loose = set(), []
    for path in sorted(PKG.glob("*.py")):
        if path.name == "i18n.py":
            continue
        text = path.read_text()
        lines = text.splitlines()
        tree = ast.parse(text)
        marked, docs = set(), set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("_", "N_") and node.args:
                arg = node.args[0]
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    msgids.add(arg.value)
                    marked.add(id(arg))
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                docs.add(id(node.value))
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and CYR.search(node.value) \
                    and id(node) not in marked | docs and "i18n: ignore" not in lines[node.lineno - 1]:
                loose.append(f"{path.name}:{node.lineno}: {node.value[:60]!r}")
    return msgids, loose


class Catalogs(unittest.TestCase):
    def test_no_untranslatable_russian_in_code(self):
        _, loose = scan()
        self.assertEqual(loose, [], "wrap these in _() or N_()")

    def test_every_string_translated_with_same_placeholders(self):
        msgids, _ = scan()
        for lang, cat in i18n.CATALOG.items():
            missing = sorted(m for m in msgids if CYR.search(m) and m not in cat)
            self.assertEqual(missing, [], f"{lang}: no translation")
            for m in msgids & cat.keys():
                self.assertEqual(sorted(PLACEHOLDER.findall(m)), sorted(PLACEHOLDER.findall(cat[m])), f"{lang}: {m[:60]!r}")
                self.assertFalse(CYR.search(cat[m]), f"{lang}: Russian left in {cat[m][:60]!r}")
            self.assertEqual(sorted(cat.keys() - msgids), [], f"{lang}: unused catalog entries")

    def test_sources_in_every_language(self):
        for sid, e in sources.SOURCES.items():
            for lang in ("en", "es"):
                need = ["title", "summary"] + (["status_note"] if e.get("status_note") else [])
                need += ["quote"] if lang == "en" and e.get("quote_ru") else []
                for key in need:
                    self.assertTrue(e.get(f"{key}_{lang}"), f"{sid}: no {key}_{lang}")
        for sid, e in sources.SOURCES.items():
            self.assertFalse(CYR.search(e.get("ref", "")), f"{sid}: ref is shown in every language, keep it Spanish")

    def test_docs_in_every_language(self):
        """Spanish originals in kb/ and docs/; English and Russian translations next to them."""
        root = PKG.parent
        originals = [*sorted((root / "kb").glob("*.md")), root / "docs/use-cases.md", root / "docs/onboarding.md", root / "docs/explainer.html"]
        for path in originals:
            for lang in ("en", "ru"):
                twin = path.parent / lang / path.name
                self.assertTrue(twin.exists(), f"no {twin.relative_to(root)}")
                if lang == "en":
                    self.assertFalse(CYR.search(twin.read_text()), f"Russian left in {twin.relative_to(root)}")
        for path in (root / "kb").glob("**/*.md"):
            self.assertTrue(path.parent.name in ("kb", "en", "ru"), f"unexpected {path.relative_to(root)}")

    def test_language_choice(self):
        self.assertEqual(i18n.pick("ru", "es-ES,es;q=0.9"), "ru")            # profile setting wins
        self.assertEqual(i18n.pick("", "de-DE,es;q=0.8,en;q=0.5"), "es")     # first supported browser language
        self.assertEqual(i18n.pick("", "de-DE"), "en")


if __name__ == "__main__":
    unittest.main()
