from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class TypesValuesTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_nil(self):
        ast = self.parser.srcToAST(r'foo = nil')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(NilExpr([]))])))
        self.assertAstEqual(exp, ast)

    def test_true(self):
        ast = self.parser.srcToAST(r'foo = true')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(TrueExpr([]))])))
        self.assertAstEqual(exp, ast)

    def test_false(self):
        ast = self.parser.srcToAST(r'foo = false')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(FalseExpr([]))])))
        self.assertAstEqual(exp, ast)

    def test_numbers(self):
        ast = self.parser.srcToAST(r'foo = 4')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(NumberExpr(4))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 0.4')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(NumberExpr(0.4))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 4.57e-3')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(NumberExpr(4.57e-3))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 0.3e12')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(NumberExpr(0.3e12))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 5e+20')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("foo")), ExprsExpr(NumberExpr(5e+20))])))
        self.assertAstEqual(exp, ast)

    def test_string_dbl_quote(self):
        ast = self.parser.srcToAST(r'a = "a line"')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("a")), ExprsExpr(StringExpr('a line'))])))
        self.assertAstEqual(exp, ast)

    def test_string_quote(self):
        ast = self.parser.srcToAST(r"b = 'another line'")
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("b")), ExprsExpr(StringExpr('another line'))])))
        self.assertAstEqual(exp, ast)

    def test_string_escape(self):
        ast = self.parser.srcToAST(r'''b = "one line\nnext line\n\"in quotes\", 'in quotes'"''')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("b")), ExprsExpr(StringExpr(r"one line\nnext line\n\"in quotes\", 'in quotes'"))])))
        self.assertAstEqual(exp, ast)

    def test_string_dbl_square(self):
        ast = self.parser.srcToAST(r'b = [[hello]]')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("b")), ExprsExpr(StringExpr(r"hello"))])))
        self.assertAstEqual(exp, ast)

        ast = self.parser.srcToAST(textwrap.dedent(r'''
            b = [[Multiple lines of text
            can be enclosed in double square
            brackets.]]
            '''))
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("b")), ExprsExpr(StringExpr("Multiple lines of text\ncan be enclosed in double square\nbrackets."))])))
        self.assertAstEqual(exp, ast)

    def test_string_dbl_square_equal(self):
        ast = self.parser.srcToAST(r'b = [=[one [[two]] one]=]')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("b")), ExprsExpr(StringExpr(r"one [[two]] one"))])))
        self.assertAstEqual(exp, ast)