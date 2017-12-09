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

        """
    3.3.3 – Assignment
    """
    def test_set_number(self):
        ast = self.parser.srcToAST("i=3")
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('i')],values=[NumberExpr(3)])
        ]))
        self.assertEqual(exp, ast)

    def test_set_string(self):
        ast = self.parser.srcToAST('i="foo bar"')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('i')],values=[StringExpr('foo bar')])
        ]))
        self.assertEqual(exp, ast)

    def test_set_array_index(self):
        ast = self.parser.srcToAST('a[i] = 42')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[IndexExpr(idx=NameExpr('i'), value=NameExpr('a'))], values=[NumberExpr(42)])
        ]))
        self.assertEqual(exp, ast)

    def test_set_table_index(self):
        ast = self.parser.srcToAST('_ENV.x = val')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[IndexExpr(idx=NameExpr('x'), value=NameExpr('_ENV'))], values=[NameExpr('val')])
        ]))
        self.assertEqual(exp, ast)

    def test_set_multi(self):
        ast = self.parser.srcToAST('x, y = y, x')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('x'), NameExpr('y')],values=[NameExpr('y'), NameExpr('x')])
        ]))
        self.assertEqual(exp, ast)