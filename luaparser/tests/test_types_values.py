from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class TypesValuesTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_nil(self):
        ast = self.parser.srcToAST(r'foo = nil')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='foo')
            ],
            values=[
                NilExpr()
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_true(self):
        ast = self.parser.srcToAST(r'foo = true')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='foo')
            ],
            values=[
                TrueExpr()
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_false(self):
        ast = self.parser.srcToAST(r'foo = false')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='foo')
            ],
            values=[
                FalseExpr()
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_numbers(self):
        ast = self.parser.srcToAST(r'foo = 4')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=4)]
        )]))
        self.assertEqual(exp, ast)

        ast = self.parser.srcToAST(r'foo = 0.4')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=0.4)]
        )]))
        self.assertEqual(exp, ast)

        ast = self.parser.srcToAST(r'foo = 4.57e-3')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=4.57e-3)]
        )]))
        self.assertEqual(exp, ast)

        ast = self.parser.srcToAST(r'foo = 0.3e12')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=0.3e12)]
        )]))
        self.assertEqual(exp, ast)

        ast = self.parser.srcToAST(r'foo = 5e+20')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=5e+20)]
        )]))
        self.assertEqual(exp, ast)

    def test_string_dbl_quote(self):
        ast = self.parser.srcToAST(r'a = "a line"')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[StringExpr(s='a line')]
        )]))
        self.assertEqual(exp, ast)

    def test_string_quote(self):
        ast = self.parser.srcToAST(r"b = 'another line'")
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='another line')]
        )]))
        self.assertEqual(exp, ast)

    def test_string_escape(self):
        ast = self.parser.srcToAST(r'''b = "one line\nnext line\n\"in quotes\", 'in quotes'"''')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s=r"one line\nnext line\n\"in quotes\", 'in quotes'")]
        )]))
        self.assertEqual(exp, ast)

    def test_string_dbl_square(self):
        ast = self.parser.srcToAST(r'b = [[hello]]')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='hello')]
        )]))
        self.assertEqual(exp, ast)

        ast = self.parser.srcToAST(textwrap.dedent(r'''
            b = [[Multiple lines of text
            can be enclosed in double square
            brackets.]]
            '''))
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='Multiple lines of text\ncan be enclosed in double square\nbrackets.')]
        )]))
        self.assertEqual(exp, ast)

    def test_string_dbl_square_equal(self):
        ast = self.parser.srcToAST(r'b = [=[one [[two]] one]=]')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='b')],
            values=[StringExpr(s='one [[two]] one')]
        )]))
        self.assertEqual(exp, ast)