from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *


class SimpleWidgetTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_global_var(self):
        ast = self.parser.srcToAST("foo = 42")
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr("42"))])))
        self.assertAstEqual(exp, ast)

    def test_local_var(self):
        ast = self.parser.srcToAST("local foo = 42")
        exp = Chunk(Block(LocalSetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr("42"))])))
        self.assertAstEqual(exp, ast)

    def test_multi_var(self):
        ast = self.parser.srcToAST("a,b,c = 1,2")
        exp = Chunk(Block(SetStat([VarsExpr([IdExpr("a"), IdExpr("b"), IdExpr("c")]), ExprsExpr([NumberExpr("1"), NumberExpr("2")])])))
        self.assertAstEqual(exp, ast)

    def test_local_multi_var(self):
        ast = self.parser.srcToAST("local foo, bar = 42")
        exp = Chunk(Block(LocalSetStat([VarsExpr([IdExpr("foo"), IdExpr("bar")]), ExprsExpr([NumberExpr("42")])])))
        self.assertAstEqual(exp, ast)