from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *


class VariablesTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_global_var(self):
        ast = self.parser.srcToAST("foo = 42")
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=42)]
        )]))
        self.assertEqual(exp, ast)

    def test_local_var(self):
        ast = self.parser.srcToAST("local foo = 42")
        exp = Chunk(body=Block(body=[LocalAssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=42)]
        )]))
        self.assertEqual(exp, ast)

    def test_multi_var(self):
        ast = self.parser.srcToAST("a,b,c = 1,2")
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[
                NameExpr(id='a'),
                NameExpr(id='b'),
                NameExpr(id='c')
            ],
            values=[
                NumberExpr(n=1),
                NumberExpr(n=2)
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_local_multi_var(self):
        ast = self.parser.srcToAST("local foo, bar = 42")
        exp = Chunk(body=Block(body=[LocalAssignStat(
            targets=[
                NameExpr(id='foo'),
                NameExpr(id='bar')
            ],
            values=[
                NumberExpr(n=42)
            ]
        )]))
        self.assertEqual(exp, ast)