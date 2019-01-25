import unittest
from luaparser.astnodes import *


class TestCase(unittest.TestCase):
    def assert_ast_equal(self, ast, other):
        if isinstance(ast, Node) and isinstance(other, Node):
            self.assertEqual(len(ast.childs), len(other.childs))
            self.assertIsInstance(ast, other.__class__)
            for i, child in enumerate(ast.childs):
                self.assert_ast_equal(child, other.childs[i])
        else:
            self.assertEqual(ast, other)
