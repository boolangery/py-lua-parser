from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *


class BlockTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_empty_block(self):
        ast = self.parser.srcToAST(";;;;")
        exp = Chunk(Block(None))
        self.assertAstEqual(exp, ast)

    def test_2_block(self):
        ast = self.parser.srcToAST("local a;local b;")
        exp = Chunk(Block([LocalSetStat(VarsExpr(IdExpr("a"))), LocalSetStat(VarsExpr(IdExpr("b")))]))
        self.assertAstEqual(exp, ast)