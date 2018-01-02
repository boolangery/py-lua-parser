from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class LuaVisitorTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_assign(self):
        src = """i  = 3"""
        ast = self.parser.srcToAST(textwrap.dedent(src))
        self.assertEqual(src, Printer.toStr(ast, Printer.Style.LUA))

    def test_assign(self):
        src = """x,  y,z =  a,b,c"""
        ast = self.parser.srcToAST(textwrap.dedent(src))
        self.assertEqual(src, Printer.toStr(ast, Printer.Style.LUA))