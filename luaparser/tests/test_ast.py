from luaparser.utils import tests
from luaparser import astutils
from luaparser.astnodes import *
import textwrap

class TokensTestCase(tests.TestCase):

    def test_walk_1(self):
        src = textwrap.dedent("""
            local a = 1
            """)
        tree = astutils.parse(src)
        chunk, block, local, name, number = False, False, False, False, False
        for node in astutils.walk(tree):
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
        class NumberVisitor(astutils.ASTVisitor):
            def visit_Number(self, node):
                nonlocal called
                called = True

        tree = astutils.parse(src)
        NumberVisitor().visit(tree)
        self.assertTrue(called)

    def test_parse_error(self):
        src = textwrap.dedent("""
            local a = if
            """)

        self.assertRaises(Exception, astutils.parse, src)


