from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


class AstTestCase(tests.TestCase):
    def test_walk_1(self):
        src = textwrap.dedent(
            """
            local a = 1
            """
        )
        tree = ast.parse(src)
        chunk, block, local, name, number = False, False, False, False, False
        for node in ast.walk(tree):
            if isinstance(node, Chunk):
                chunk = True
            if isinstance(node, Block):
                block = True
            if isinstance(node, LocalAssign):
                local = True
            if isinstance(node, Name):
                name = True
            if isinstance(node, Number):
                number = True
        self.assertTrue(chunk)
        self.assertTrue(block)
        self.assertTrue(local)
        self.assertTrue(name)
        self.assertTrue(number)

    def test_visitor_1(self):
        src = textwrap.dedent(
            """
            local a = 1
            """
        )

        called = False

        class NumberVisitor(ast.ASTVisitor):
            def visit_Number(self, node):
                nonlocal called
                called = True

        tree = ast.parse(src)
        NumberVisitor().visit(tree)
        self.assertTrue(called)

    def test_parse_error(self):
        src = textwrap.dedent(
            """
            local a = if
            """
        )

        self.assertRaises(Exception, ast.parse, src)

    # Cant walk the ast tree if lua file has semicolon(;) or repeat until loop and multiple args(...) #9
    def test_cont_int_1(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            function table.pack(...)
                repeat
                   print("value of a:", a)
                   a = a + 1;
                until( a > 15 )
            end
            """
            )
        )
        nodes = ast.walk(tree)
        expected_cls = [
            Chunk,
            Block,
            Function,
            Index,
            Name,
            Name,
            Varargs,
            Block,
            Repeat,
            Block,
            Call,
            Name,
            String,
            Name,
            Assign,
            Name,
            AddOp,
            Name,
            Number,
            SemiColon,
            GreaterThanOp,
            Name,
            Number,
        ]
        for node, exp in zip(nodes, expected_cls):
            self.assertIsInstance(node, exp)
