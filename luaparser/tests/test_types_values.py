from luaparser import tests
from luaparser import ast
from luaparser.astNodes import *
import textwrap


class TypesValuesTestCase(tests.TestCase):
    def test_nil(self):
        tree = ast.parse(r'foo = nil')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='foo')
            ],
            values=[
                NilExpr()
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_true(self):
        tree = ast.parse(r'foo = true')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='foo')
            ],
            values=[
                TrueExpr()
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_false(self):
        tree = ast.parse(r'foo = false')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='foo')
            ],
            values=[
                FalseExpr()
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_numbers(self):
        tree = ast.parse(r'foo = 4')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=4)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 0.4')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=0.4)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 4.57e-3')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=4.57e-3)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 0.3e12')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=0.3e12)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 5e+20')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=5e+20)]
        )]))
        self.assertEqual(exp, tree)

    def test_string_dbl_quote(self):
        tree = ast.parse(r'a = "a line"')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[StringExpr(s='a line')]
        )]))
        self.assertEqual(exp, tree)

    def test_string_quote(self):
        tree = ast.parse(r"b = 'another line'")
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='another line')]
        )]))
        self.assertEqual(exp, tree)

    def test_string_escape(self):
        tree = ast.parse(r'''b = "one line\nnext line\n\"in quotes\", 'in quotes'"''')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s=r"one line\nnext line\n\"in quotes\", 'in quotes'")]
        )]))
        self.assertEqual(exp, tree)

    def test_string_dbl_square(self):
        tree = ast.parse(r'b = [[hello]]')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='hello')]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r'''
            b = [[Multiple lines of text
            can be enclosed in double square
            brackets.]]
            '''))
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='Multiple lines of text\ncan be enclosed in double square\nbrackets.')]
        )]))
        self.assertEqual(exp, tree)

    def test_string_dbl_square_equal(self):
        tree = ast.parse(r'b = [=[one [[two]] one]=]')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='one [[two]] one')]
        )]))
        self.assertEqual(exp, tree)