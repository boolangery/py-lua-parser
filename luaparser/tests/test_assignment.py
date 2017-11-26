from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *


class AssignmentTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_set_number(self):
        ast = self.parser.srcToAST("i=3")
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("i")), ExprsExpr(NumberExpr(3))])))
        self.assertAstEqual(exp, ast)

    def test_set_string(self):
        ast = self.parser.srcToAST('i="foo bar"')
        exp = Chunk(Block(AssignStat([VarsExpr(NameExpr("i")), ExprsExpr(StringExpr('foo bar'))])))
        self.assertAstEqual(exp, ast)

    def test_set_array_index(self):
        ast = self.parser.srcToAST('a[i] = 42')
        exp = Chunk(Block(AssignStat([VarsExpr(IndexExpr([NameExpr("a"), NameExpr("i")])), ExprsExpr(NumberExpr(42))])))
        self.assertAstEqual(exp, ast)

    def test_set_table_index(self):
        ast = self.parser.srcToAST('_ENV.x = val')
        exp = Chunk(Block(AssignStat([VarsExpr(IndexExpr([NameExpr("_ENV"), NameExpr("x")])), ExprsExpr(NameExpr('val'))])))
        self.assertAstEqual(exp, ast)

    def test_set_multi(self):
        ast = self.parser.srcToAST('x, y = y, x')
        exp = Chunk(Block(AssignStat([VarsExpr([NameExpr("x"), NameExpr("y")]), ExprsExpr([NameExpr('y'), NameExpr('x')])])))
        self.assertAstEqual(exp, ast)