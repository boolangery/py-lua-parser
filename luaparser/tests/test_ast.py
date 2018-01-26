from luaparser.utils  import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap

class TokensTestCase(tests.TestCase):

    def test_ast_tokens_1(self):
        src = textwrap.dedent("""
            local a = 42
            """)
        tree = ast.parse(src)
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[0], Chunk)
        self.assertEqual(nodes[0].tokens[0].text, 'local')
        self.assertEqual(nodes[0].tokens[1].text, ' ')
        self.assertEqual(nodes[0].tokens[2].text, 'a')
        self.assertEqual(nodes[0].tokens[3].text, ' ')
        self.assertEqual(nodes[0].tokens[4].text, '=')
        self.assertEqual(nodes[0].tokens[5].text, ' ')
        self.assertEqual(nodes[0].tokens[6].text, '42')

        self.assertIsInstance(nodes[1], Block)
        self.assertEqual(nodes[1].tokens[0].text, 'local')
        self.assertEqual(nodes[1].tokens[1].text, ' ')
        self.assertEqual(nodes[1].tokens[2].text, 'a')
        self.assertEqual(nodes[1].tokens[3].text, ' ')
        self.assertEqual(nodes[1].tokens[4].text, '=')
        self.assertEqual(nodes[1].tokens[5].text, ' ')
        self.assertEqual(nodes[1].tokens[6].text, '42')

        self.assertIsInstance(nodes[2], LocalAssign)
        self.assertEqual(nodes[2].tokens[0].text, 'local')
        self.assertEqual(nodes[2].tokens[1].text, ' ')
        self.assertEqual(nodes[2].tokens[2].text, 'a')
        self.assertEqual(nodes[2].tokens[3].text, ' ')
        self.assertEqual(nodes[2].tokens[4].text, '=')
        self.assertEqual(nodes[2].tokens[5].text, ' ')
        self.assertEqual(nodes[2].tokens[6].text, '42')

        self.assertIsInstance(nodes[3], Number)
        self.assertEqual(nodes[3].tokens[0].text, '42')

        self.assertIsInstance(nodes[4], Name)
        self.assertEqual(nodes[4].tokens[0].text, 'a')

    def test_walk_1(self):
        src = textwrap.dedent("""
            local a = 1
            """)
        tree = ast.parse(src)
        chunk, block, local, name, number = False, False, False, False, False
        for node in ast.walk(tree):
            if isinstance(node, Chunk): chunk = True
            if isinstance(node, Block): block = True
            if isinstance(node, LocalAssign): local = True
            if isinstance(node, Name): name = True
            if isinstance(node, Number): number = True
        self.assertTrue(chunk)
        self.assertTrue(block)
        self.assertTrue(local)
        self.assertTrue(name)
        self.assertTrue(number)

    def test_visitor_1(self):
        src = textwrap.dedent("""
            local a = 1
            """)

        called = False
        class NumberVisitor(ast.ASTVisitor):
            def visit_Number(self, node):
                nonlocal called
                called = True

        tree = ast.parse(src)
        NumberVisitor().visit(tree)
        self.assertTrue(called)

    def test_parse_error(self):
        src = textwrap.dedent("""
            local a = if
            """)

        self.assertRaises(ast.SyntaxException, ast.parse, src)


