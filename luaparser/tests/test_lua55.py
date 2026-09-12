import textwrap

from luaparser import ast
from luaparser.ast import SyntaxException
from luaparser.astnodes import (
    Assign,
    Attribute,
    GlobalAssign,
    GlobalFunction,
    LocalAssign,
    Name,
    Number,
    StringDelimiter,
    Varargs,
)
from luaparser.utils import tests


class Lua55TestCase(tests.TestCase):
    def test_global_declarations(self):
        tree = ast.parse(textwrap.dedent("""
            global x, y <const> = 1, 2
            global <const> z
            global<close> *
        """))

        first, second, third = tree.body.body
        self.assertEqual(
            GlobalAssign(
                targets=[Name("x"), Name("y", Attribute(Name("const")))],
                values=[Number(1), Number(2)],
            ),
            first,
        )
        self.assertEqual(
            GlobalAssign(
                targets=[Name("z")],
                values=[],
                attribute=Attribute(Name("const")),
            ),
            second,
        )
        self.assertEqual(
            GlobalAssign(attribute=Attribute(Name("close")), wildcard=True),
            third,
        )

    def test_global_function(self):
        statement = ast.parse("global function f(a) return a end").body.body[0]
        self.assertIsInstance(statement, GlobalFunction)
        self.assertEqual(Name("f"), statement.name)
        self.assertEqual([Name("a")], statement.args)

    def test_global_remains_usable_as_an_identifier(self):
        tree = ast.parse("global = global + 1; global()")
        statement = tree.body.body[0]
        self.assertIsInstance(statement, Assign)
        self.assertEqual([Name("global")], statement.targets)

    def test_prefixed_local_attribute(self):
        statement = ast.parse("local <const> x, y <close>").body.body[0]
        self.assertEqual(
            LocalAssign(
                targets=[Name("x"), Name("y", Attribute(Name("close")))],
                values=[],
                attribute=Attribute(Name("const")),
            ),
            statement,
        )

    def test_named_varargs(self):
        tree = ast.parse("function f(a, ... args) return args.n end")
        statement = tree.body.body[0]
        self.assertEqual(Varargs(Name("args")), statement.args[-1])
        self.assertEqual("function f(a, ... args)\n    return args.n\nend", ast.to_lua_source(tree))

    def test_unlimited_long_bracket_level_and_round_trip(self):
        source = "x = [==========[a ]] b]==========]"
        tree = ast.parse(source)
        value = tree.body.body[0].values[0]
        self.assertEqual(10, value.long_bracket_level)
        self.assertEqual(b"a ]] b", value.s)
        self.assertEqual(source, ast.to_lua_source(tree))

    def test_long_string_value_normalizes_line_endings(self):
        value = ast.parse("x=[=[\r\na\r\nb\n\rc\rd]=]").body.body[0].values[0]
        self.assertEqual(b"a\nb\nc\nd", value.s)
        self.assertEqual(StringDelimiter.DOUBLE_SQUARE, value.delimiter)

    def test_short_string_byte_escapes(self):
        values = ast.parse(r'x="\255"; y="\xFF"; z="\1234"').body.body
        self.assertEqual(b"\xff", values[0].values[0].s)
        self.assertEqual(b"\xff", values[2].values[0].s)
        self.assertEqual(b"{4", values[4].values[0].s)

    def test_escaped_line_endings(self):
        for newline in ("\n", "\r", "\r\n", "\n\r"):
            value = ast.parse('x="a\\' + newline + 'b"').body.body[0].values[0]
            self.assertEqual(b"a\nb", value.s)

    def test_z_escape_consumes_ascii_whitespace(self):
        value = ast.parse('x="a\\z \t\v\f\r\n b"').body.body[0].values[0]
        self.assertEqual(b"ab", value.s)

    def test_vertical_tab_is_whitespace(self):
        self.assertEqual(
            LocalAssign(targets=[Name("x")], values=[Number(1)]),
            ast.parse("local\vx=1").body.body[0],
        )

    def test_hexadecimal_floats_build_an_ast(self):
        for source, expected in (("0xF0.0", 240.0), ("0xABCp-3", 343.5), ("0X0.41", 0.25390625)):
            value = ast.parse("x=" + source).body.body[0].values[0]
            self.assertEqual(expected, value.n)

    def test_invalid_short_strings_are_rejected(self):
        for source in ('x="a\nb"', "x='a\rb'", r'x="\256"', r'x="\999"', r'x="\|"', r'x="\$"', r'x="\#"'):
            with self.assertRaises(SyntaxException, msg=repr(source)):
                ast.parse(source)

    def test_unlimited_long_comment_level(self):
        source = "--[==========[ignored]==========]\nx=1"
        statement = ast.parse(source).body.body[0]
        self.assertEqual([Name("x")], statement.targets)
        self.assertEqual([Number(1)], statement.values)

    def test_lua55_forms_round_trip(self):
        sources = (
            "global x = 1",
            "global function f()\n\nend",
            "global<const> *",
            "local <const> x, y <close> = 1, 2",
        )
        for source in sources:
            self.assertEqual(source, ast.to_lua_source(ast.parse(source)))
