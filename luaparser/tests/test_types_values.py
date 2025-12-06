from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


class TypesValuesTestCase(tests.TestCase):
    def test_nil(self):
        tree = ast.parse(r"foo = nil")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Nil()])]))
        self.assertEqual(exp, tree)

    def test_true(self):
        tree = ast.parse(r"foo = true")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[TrueExpr()])]))
        self.assertEqual(exp, tree)

    def test_false(self):
        tree = ast.parse(r"foo = false")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[FalseExpr()])]))
        self.assertEqual(exp, tree)

    def test_numbers(self):
        tree = ast.parse(r"foo = 04")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Number(n=4)])]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r"foo = 0.4")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Number(n=0.4)])]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r"foo = 4.57e-3")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Number(n=4.57e-3)])]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r"foo = 0.3e12")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Number(n=0.3e12)])]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r"foo = 5e+20")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Number(n=5e20)])]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r"foo = 0.31416E1")
        exp = Chunk(
            Block([Assign(targets=[Name("foo")], values=[Number(n=0.31416e1)])])
        )
        self.assertEqual(exp, tree)

        tree = ast.parse(r"foo = 0xff")
        exp = Chunk(Block([Assign(targets=[Name("foo")], values=[Number(n=0xFF)])]))
        self.assertEqual(exp, tree)

    def test_string_dbl_quote(self):
        tree = ast.parse(r'a = "a line"')
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[String(b"a line", "a line", StringDelimiter.DOUBLE_QUOTE)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_string_quote(self):
        tree = ast.parse(r"b = 'another line'")
        exp = Chunk(
            Block([Assign(targets=[Name("b")], values=[String(b"another line", "another line")])])
        )
        self.assertEqual(exp, tree)

    def test_string_escape(self):
        tree = ast.parse(r'''b = "one line\nnext line\n\"in quotes\", 'in quotes'"''')
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("b")],
                        values=[
                            String(
                                b"one line\nnext line\n\"in quotes\", 'in quotes'",
                                "one line\\nnext line\\n\\\"in quotes\\\", 'in quotes'",
                                StringDelimiter.DOUBLE_QUOTE,
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_string_dbl_square(self):
        tree = ast.parse(r"b = [[hello]]")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("b")],
                        values=[String(b"hello", "hello", StringDelimiter.DOUBLE_SQUARE)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

        tree = ast.parse(
            textwrap.dedent(
                r"""
            b = [[Multiple lines of text
            can be enclosed in double square
            brackets.]]
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("b")],
                        values=[
                            String(
                                b"Multiple lines of text\ncan be enclosed in double square\nbrackets.",
                                "Multiple lines of text\ncan be enclosed in double square\nbrackets.",
                                StringDelimiter.DOUBLE_SQUARE,
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_string_dbl_square_equal(self):
        tree = ast.parse(r"b = [=[one [[two]] one]=]")
        exp = Chunk(
            Block([Assign(targets=[Name("b")], values=[String(b"one [[two]] one", "one [[two]] one", delimiter=StringDelimiter.DOUBLE_SQUARE)])])
        )
        self.assertEqual(exp, tree)

    def test_string_dbl_square_equal_newlines(self):
        tree = ast.parse(
            textwrap.dedent(
            r"""
                a = [=[
                four
                ]=]
                b = [===[
                five
                ]===]
            """
            )
        )
        exp = Chunk(
            Block([
                Assign(targets=[Name("a")], values=[String(b"\nfour\n", "\nfour\n", delimiter=StringDelimiter.DOUBLE_SQUARE)]),
                Assign(targets=[Name("b")], values=[String(b"\nfive\n", "\nfive\n", delimiter=StringDelimiter.DOUBLE_SQUARE)]),
            ])
        )
        self.assertEqual(exp, tree)

    def test_string_literal(self):
        tree = ast.parse(r'a="\u{9}"')
        exp = Chunk(
            Block([Assign(targets=[Name("a")], values=[String(b"\x09", r"\u{9}", StringDelimiter.DOUBLE_QUOTE)])])
        )
        self.assertEqual(exp, tree)
