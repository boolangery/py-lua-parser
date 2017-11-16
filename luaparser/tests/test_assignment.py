from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *


class AssignmentTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_set_number(self):
        ast = self.parser.srcToAST("i=3")
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("i")), ExprsExpr(NumberExpr("3"))])))
        self.assertAstEqual(exp, ast)

    def test_set_string(self):
        ast = self.parser.srcToAST('i="foo bar"')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("i")), ExprsExpr(StringExpr('"foo bar"'))])))
        self.assertAstEqual(exp, ast)

    def test_set_array_index(self):
        ast = self.parser.srcToAST('a[i] = 42')
        exp = Chunk(Block(SetStat([VarsExpr(IndexExpr([IdExpr("a"), IdExpr("i")])), ExprsExpr(NumberExpr('42'))])))
        self.assertAstEqual(exp, ast)

    def test_set_table_index(self):
        ast = self.parser.srcToAST('_ENV.x = val')
        exp = Chunk(Block(SetStat([VarsExpr(IndexExpr([IdExpr("_ENV"), IdExpr("x")])), ExprsExpr(IdExpr('val'))])))
        self.assertAstEqual(exp, ast)

    def test_set_multi(self):
        ast = self.parser.srcToAST('x, y = y, x')
        exp = Chunk(Block(SetStat([VarsExpr([IdExpr("x"), IdExpr("y")]), ExprsExpr([IdExpr('y'), IdExpr('x')])])))
        self.assertAstEqual(exp, ast)