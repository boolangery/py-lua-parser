from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *


class VariablesTestCase(tests.TestCase):
    def test_global_var(self):
        tree = ast.parse("foo = 42")
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='foo')],
            values=[Number(n=42)]
        )]))
        self.assertEqual(exp, tree)

    def test_local_var(self):
        tree = ast.parse("local foo = 42")
        exp = Chunk(body=Block(body=[LocalAssign(
            targets=[Name(id='foo')],
            values=[Number(n=42)]
        )]))
        self.assertEqual(exp, tree)

    def test_empty_local_var(self):
        tree = ast.parse("local foo, bar")
        exp = Chunk(body=Block(body=[LocalAssign(
            targets=[Name(id='foo'), Name(id='bar')],
            values=[]
        )]))
        self.assertEqual(exp, tree)

    def test_multi_var(self):
        tree = ast.parse("a,b,c = 1,2")
        exp = Chunk(body=Block(body=[Assign(
            targets=[
                Name(id='a'),
                Name(id='b'),
                Name(id='c')
            ],
            values=[
                Number(n=1),
                Number(n=2)
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_local_multi_var(self):
        tree = ast.parse("local foo, bar = 42")
        exp = Chunk(body=Block(body=[LocalAssign(
            targets=[
                Name(id='foo'),
                Name(id='bar')
            ],
            values=[
                Number(n=42)
            ]
        )]))
        self.assertEqual(exp, tree)