from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *


class VariablesTestCase(tests.TestCase):
    def test_global_var(self):
        tree = ast.parse("foo = 42")
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=42)]
        )]))
        self.assertEqual(exp, tree)

    def test_local_var(self):
        tree = ast.parse("local foo = 42")
        exp = Chunk(Block([LocalAssign(
            targets=[Name('foo')],
            values=[Number(n=42)]
        )]))
        self.assertEqual(exp, tree)

    def test_empty_local_var(self):
        tree = ast.parse("local foo, bar")
        exp = Chunk(Block([LocalAssign(
            targets=[Name('foo'), Name('bar')],
            values=[]
        )]))
        self.assertEqual(exp, tree)

    def test_multi_var(self):
        tree = ast.parse("a,b,c = 1,2")
        exp = Chunk(Block([Assign(
            targets=[
                Name('a'),
                Name('b'),
                Name('c')
            ],
            values=[
                Number(n=1),
                Number(n=2)
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_local_multi_var(self):
        tree = ast.parse("local foo, bar = 42")
        exp = Chunk(Block([LocalAssign(
            targets=[
                Name('foo'),
                Name('bar')
            ],
            values=[
                Number(n=42)
            ]
        )]))
        self.assertEqual(exp, tree)