from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class ControlStructureTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_set_number(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            while a[i] do
              i = i + 1
            end"""))
        exp = Chunk(Block(
            WhileStat([
                IndexExpr([IdExpr("a"), IdExpr("i")]),
                Block(SetStat([
                    VarsExpr(IdExpr("i")),
                    ExprsExpr(AddOpExpr([IdExpr("i"), NumberExpr(1)]))
                ]))
            ])
        ))

        self.assertAstEqual(exp, ast)
