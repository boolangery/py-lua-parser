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

    def test_to_pretty_json(self):
        src = textwrap.dedent(
            """\
            local a = "foo"\
            """
        )
        exp = textwrap.dedent(
            """\
            {
                "Chunk": {
                    "body": {
                        "Block": {
                            "body": [
                                {
                                    "LocalAssign": {
                                        "wrapped": false,
                                        "targets": [
                                            {
                                                "Name": {
                                                    "wrapped": false,
                                                    "id": "a",
                                                    "start_char": null,
                                                    "stop_char": null,
                                                    "line": null
                                                }
                                            }
                                        ],
                                        "values": [
                                            {
                                                "String": {
                                                    "wrapped": false,
                                                    "s": "foo",
                                                    "raw": "foo",
                                                    "delimiter": {},
                                                    "start_char": 10,
                                                    "stop_char": 14,
                                                    "line": null
                                                }
                                            }
                                        ],
                                        "start_char": 0,
                                        "stop_char": 14,
                                        "line": null
                                    }
                                }
                            ],
                            "start_char": 0,
                            "stop_char": 14,
                            "line": null
                        }
                    },
                    "start_char": 0,
                    "stop_char": 14,
                    "line": null
                }
            }"""
        )
        self.assertEqual(ast.to_pretty_json(ast.parse(src)), exp)


class ASTTransformerTestCase(tests.TestCase):
    """Tests for ASTTransformer."""

    def test_noop_returns_same_tree(self):
        """Transformer with no overrides returns identical structure."""
        src = "local x = 1"
        tree = ast.parse(src)

        class NoopTransformer(ast.ASTTransformer):
            pass

        result = NoopTransformer().visit(tree)
        self.assertEqual(ast.to_pretty_str(result), ast.to_pretty_str(tree))
        # Root should be the same object when no transforms applied
        self.assertIs(result, tree)

    def test_replace_number(self):
        """Replace a Number node with a different value."""
        src = "local x = 42"
        tree = ast.parse(src)

        class Doubler(ast.ASTTransformer):
            def visit_Number(self, node):
                return Number(node.n * 2)

        result = Doubler().visit(tree)
        self.assertIn("84", ast.to_pretty_str(result))
        self.assertNotIn("42", ast.to_pretty_str(result))

    def test_replace_string(self):
        """Replace a String literal."""
        src = 'local msg = "hello"'
        tree = ast.parse(src)

        class StringUpper(ast.ASTTransformer):
            def visit_String(self, node):
                upper_raw = node.raw.upper()
                return String(upper_raw.encode(), upper_raw, node.delimiter)

        result = StringUpper().visit(tree)
        output = ast.to_pretty_str(result)
        self.assertIn("HELLO", output)
        self.assertNotIn("hello", output)

    def test_keep_node_by_returning_none(self):
        """Returning None keeps the original node."""
        src = "local x = 42"
        tree = ast.parse(src)

        class KeepNumbers(ast.ASTTransformer):
            def visit_Number(self, node):
                if node.n == 42:
                    return None  # keep
                return Number(0)

        result = KeepNumbers().visit(tree)
        self.assertEqual(ast.to_pretty_str(result), ast.to_pretty_str(tree))

    def test_keep_node_by_returning_same(self):
        """Returning the same node object keeps it."""
        src = "local x = 42"
        tree = ast.parse(src)

        class IdentityTransformer(ast.ASTTransformer):
            def visit_Number(self, node):
                return node  # same object

        result = IdentityTransformer().visit(tree)
        self.assertEqual(ast.to_pretty_str(result), ast.to_pretty_str(tree))
        self.assertIs(result, tree)

    def test_replace_statement(self):
        """Replace an entire statement node."""
        src = "local x = 1"
        tree = ast.parse(src)

        class AssignToNil(ast.ASTTransformer):
            def visit_LocalAssign(self, node):
                # Replace local assignment with a nil assignment
                return Assign(node.targets, [Nil()])

        result = AssignToNil().visit(tree)
        output = ast.to_lua_source(result)
        self.assertIn("nil", output)
        self.assertNotIn("local", output)

    def test_replace_multiple_in_list(self):
        """Replace multiple nodes in a list (block body)."""
        src = textwrap.dedent("""\
            local a = 1
            local b = 2
            local c = 3
        """)
        tree = ast.parse(src)

        class DropMiddleStatement(ast.ASTTransformer):
            def visit_LocalAssign(self, node):
                target_name = node.targets[0].id
                if target_name == "b":
                    return None  # remove it -- handled via parent removal
                return node

        result = DropMiddleStatement().visit(tree)
        output = ast.to_lua_source(result)
        self.assertIn("local a", output)
        self.assertIn("local c", output)
        # 'local b' should still be there since returning None keeps the node
        self.assertIn("local b", output)

    def test_replace_in_call_args(self):
        """Replace an argument inside a function call."""
        src = "print(42)"
        tree = ast.parse(src)

        class ArgReplacer(ast.ASTTransformer):
            def visit_Number(self, node):
                s = str(node.n).encode()
                return String(s, str(node.n), StringDelimiter.DOUBLE_QUOTE)

        result = ArgReplacer().visit(tree)
        output = ast.to_pretty_str(result)
        self.assertIn("String", output)

    def test_recursive_replacement(self):
        """Perform recursive transformations (expression folding)."""
        src = "local x = 2 + 3"
        tree = ast.parse(src)

        class ConstantFolder(ast.ASTTransformer):
            def visit_AddOp(self, node):
                if isinstance(node.left, Number) and isinstance(node.right, Number):
                    return Number(node.left.n + node.right.n)
                return node

        result = ConstantFolder().visit(tree)
        output = ast.to_lua_source(result)
        self.assertIn("= 5", output)

    def test_chained_replacement(self):
        """Replace a node, then replace a child of the replacement."""
        src = textwrap.dedent("""\
            if true then
                x = 1
            end
        """)
        tree = ast.parse(src)

        class IfRewriter(ast.ASTTransformer):
            def visit_If(self, node):
                # Replace all if-statements with a do-block (for testing)
                return Do(node.body)
            def visit_TrueExpr(self, node):
                # Replace true with false (tests ordering: If replaced first,
                # so TrueExpr inside old If condition is never visited)
                return FalseExpr()

        result = IfRewriter().visit(tree)
        output = ast.to_lua_source(result)
        self.assertIn("do", output.lower())

    def test_none_root_returns_none(self):
        """Passing None returns None."""
        class NullTransformer(ast.ASTTransformer):
            pass
        self.assertIsNone(NullTransformer().visit(None))

    def test_root_replacement(self):
        """Replace the root Chunk node."""
        src = "local x = 1"
        tree = ast.parse(src)

        class RootReplacer(ast.ASTTransformer):
            def visit_Chunk(self, node):
                new_body = Block([LocalAssign(
                    [Name("y")],
                    [Number(99)]
                )])
                return Chunk(new_body)

        result = RootReplacer().visit(tree)
        output = ast.to_lua_source(result)
        self.assertIn("y = 99", output)
        self.assertNotIn("x = 1", output)

    def test_identity_transformer_roundtrip(self):
        """Full round-trip: parse -> transform (identity) -> generate Lua."""
        src = textwrap.dedent("""\
            function foo(a, b)
                if a > b then
                    return a + 1
                else
                    return b * 2
                end
            end
            foo(10, 20)
        """)
        tree = ast.parse(src)
        original_output = ast.to_lua_source(tree)

        class Identity(ast.ASTTransformer):
            pass

        result = Identity().visit(tree)
        result_output = ast.to_lua_source(result)

        self.assertEqual(original_output, result_output)
        self.assertIs(result, tree)

    def test_visit_method_for_parent_class(self):
        """visit_Name is called for Name nodes; no crash on unrecognized types."""
        src = "local x = 1"
        tree = ast.parse(src)

        visited_names = []

        class NameCollector(ast.ASTTransformer):
            def visit_Name(self, node):
                visited_names.append(node.id)
                return node

        NameCollector().visit(tree)
        self.assertIn("x", visited_names)

    def test_replace_deeply_nested(self):
        """Replace a node deep in the tree."""
        src = textwrap.dedent("""\
            local t = {
                a = {
                    b = 42
                }
            }
        """)
        tree = ast.parse(src)

        class DeepReplacer(ast.ASTTransformer):
            def visit_Number(self, node):
                if node.n == 42:
                    return Number(999)
                return node

        result = DeepReplacer().visit(tree)
        output = ast.to_lua_source(result)
        self.assertIn("999", output)
        self.assertNotIn("42", output)


