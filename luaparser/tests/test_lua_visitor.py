from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class LuaVisitorTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_addition(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            i   = 3
            """))

        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('i')],values=[NumberExpr(3)])
        ]))
        Printer.pprint(ast, Printer.Style.PYTHON)
        Printer.pprint(ast, Printer.Style.LUA)
        self.assertEqual(exp, ast)
