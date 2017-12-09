from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *


class StatementsTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    """
    3.3.1 – Blocks
    """
    def test_empty_block(self):
        ast = self.parser.srcToAST(";;;;")
        exp = Chunk(body=Block(body=[]))
        self.assertEqual(exp, ast)

    def test_2_block(self):
        ast = self.parser.srcToAST("local a;local b;")
        exp = Chunk(body=Block(body=[
            LocalAssignStat(targets=[NameExpr('a')],values=[]),
            LocalAssignStat(targets=[NameExpr('b')],values=[])
        ]))
        self.assertEqual(exp, ast)