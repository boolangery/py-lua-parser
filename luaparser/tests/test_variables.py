from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *


class VariablesTestCase(tests.TestCase):
    def test_global_var(self):
        tree = ast.parse("foo = 42")
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=42)]
        )]))
        self.assertEqual(exp, tree)

    def test_local_var(self):
        tree = ast.parse("local foo = 42")
        exp = Chunk(body=Block(body=[LocalAssignStat(
            targets=[NameExpr(id='foo')],
            values=[NumberExpr(n=42)]
        )]))
        self.assertEqual(exp, tree)

    def test_multi_var(self):
        tree = ast.parse("a,b,c = 1,2")
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
        self.assertEqual(exp, tree)

    def test_local_multi_var(self):
        tree = ast.parse("local foo, bar = 42")
        exp = Chunk(body=Block(body=[LocalAssignStat(
            targets=[
                NameExpr(id='foo'),
                NameExpr(id='bar')
            ],
            values=[
                NumberExpr(n=42)
            ]
        )]))
        self.assertEqual(exp, tree)