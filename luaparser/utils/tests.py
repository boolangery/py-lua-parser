import unittest
from luaparser.astnodes import *

class TestCase(unittest.TestCase):
    def assertAstEqual(self, ast, other):
        if isinstance(ast, Node) and isinstance(other, Node):
            self.assertEqual(len(ast.childs), len(other.childs))
            self.assertIsInstance(ast, other.__class__)
            for i, child in enumerate(ast.childs):
                self.assertAstEqual(child, other.childs[i])
        else:
            self.assertEqual(ast, other)