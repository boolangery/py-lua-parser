from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


# https://www.lua.org/manual/5.3/manual.html#3.4


class ExpressionsTestCase(tests.TestCase):
    maxDiff = None

    """
    3.4.1 – Arithmetic Operators
    """

    def test_addition(self):
        tree = ast.parse(r"a = 1 + 0.2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[AddOp(left=Number(1), right=Number(0.2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_substraction(self):
        tree = ast.parse(r"a = 1 - 0.2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[SubOp(left=Number(1), right=Number(0.2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_multiplication(self):
        tree = ast.parse(r"a = 1 * 0.2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[MultOp(left=Number(1), right=Number(0.2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_float_division(self):
        tree = ast.parse(r"a = 1 / 0.2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[FloatDivOp(left=Number(1), right=Number(0.2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_floor_division(self):
        tree = ast.parse(r"a = 1 // 0.2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[FloorDivOp(left=Number(1), right=Number(0.2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_mod(self):
        tree = ast.parse(r"a = 1 % 0.2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[ModOp(left=Number(1), right=Number(0.2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_unary_sub(self):
        tree = ast.parse(r"a = -1")
        exp = Chunk(
            Block([Assign(targets=[Name("a")], values=[UMinusOp(operand=Number(1))])])
        )
        self.assertEqual(exp, tree)

    def test_exponentiation(self):
        tree = ast.parse(r"a = 1^2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[ExpoOp(left=Number(1), right=Number(2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_exponentiation_minus(self):
        tree = ast.parse(r"a = 1^-2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[ExpoOp(left=Number(1), right=UMinusOp(Number(2)))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_exponentiation_3(self):
        tree = ast.parse(r"a = 10^-foo()")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[ExpoOp(left=Number(10), right=UMinusOp(Call(Name("foo"), [])))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    """
    3.4.2 – Bitwise Operators
    """

    def test_bitwise_and(self):
        tree = ast.parse(r"a = 3&5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[BAndOp(left=Number(3), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_bitwise_or(self):
        tree = ast.parse(r"a = 3|5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[BOrOp(left=Number(3), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_bitwise_exclusive_or(self):
        tree = ast.parse(r"a = 3 ~ 5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[BXorOp(left=Number(3), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_bitwise_right_shift(self):
        tree = ast.parse(r"a = 3 >> 5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[BShiftROp(left=Number(3), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_bitwise_left_shirt(self):
        tree = ast.parse(r"a = 3 << 5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[BShiftLOp(left=Number(3), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_bitwise_unary_not(self):
        tree = ast.parse(r"a = ~5")
        exp = Chunk(
            Block([Assign(targets=[Name("a")], values=[UBNotOp(operand=Number(5))])])
        )
        self.assertEqual(exp, tree)

    """
    3.4.4 – Relational Operators
    """

    def test_less_than(self):
        tree = ast.parse(r"res = (1 < 2)")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[LessThanOp(left=Number(1), right=Number(2), wrapped=True)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_greater_than(self):
        tree = ast.parse(r"res = (1 > 2)")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[GreaterThanOp(left=Number(1), right=Number(2), wrapped=True)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_less_or_eq_than(self):
        tree = ast.parse(r"res = (1 <= 2)")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[LessOrEqThanOp(left=Number(1), right=Number(2), wrapped=True)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_greater_or_eq_than(self):
        tree = ast.parse(r"res = (1 >= 2)")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[GreaterOrEqThanOp(left=Number(1), right=Number(2), wrapped=True)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_equal_than(self):
        tree = ast.parse(r"res = 1 == 2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[EqToOp(left=Number(1), right=Number(2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_not_equal_than(self):
        tree = ast.parse(r"res = 1 ~= 2")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[NotEqToOp(left=Number(1), right=Number(2))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    """
    3.4.5 – Logical Operators
    """

    def test_logic_and(self):
        tree = ast.parse(r"res = 4 and 5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[AndLoOp(left=Number(4), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_logic_or(self):
        tree = ast.parse(r"res = 4 or 5")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("res")],
                        values=[OrLoOp(left=Number(4), right=Number(5))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_logic_not(self):
        tree = ast.parse(r"res = not 5")
        exp = Chunk(
            Block([Assign(targets=[Name("res")], values=[ULNotOp(operand=Number(5))])])
        )
        self.assertEqual(exp, tree)

    """ ----------------------------------------------------------------------- """
    """ 3.4.6 – Concatenation                                                   """
    """ ----------------------------------------------------------------------- """

    def test_concatenation(self):
        tree = ast.parse(r'str = "begin".."end"')
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("str")],
                        values=[
                            Concat(
                                left=String("begin", StringDelimiter.DOUBLE_QUOTE),
                                right=String("end", StringDelimiter.DOUBLE_QUOTE),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    """ ----------------------------------------------------------------------- """
    """ 3.4.7 – The Length Operator                                             """
    """ ----------------------------------------------------------------------- """

    def test_length_op(self):
        tree = ast.parse(r"len = #t")
        exp = Chunk(
            Block(
                [Assign(targets=[Name("len")], values=[ULengthOP(operand=Name("t"))])]
            )
        )
        self.assertEqual(exp, tree)

    def test_length_op_2(self):
        ast.parse(r"""len = #{"a","b","c"}""")

    """ ----------------------------------------------------------------------- """
    """ 3.4.9 – Table Constructors                                              """
    """ ----------------------------------------------------------------------- """

    def test_dict(self):
        tree = ast.parse(r'a = {foo = "bar", bar = "foo"}')
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[
                            Table(
                                [
                                    Field(
                                        Name("foo"),
                                        String("bar", StringDelimiter.DOUBLE_QUOTE),
                                    ),
                                    Field(
                                        Name("bar"),
                                        String("foo", StringDelimiter.DOUBLE_QUOTE),
                                    ),
                                ]
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_nested_dict(self):
        tree = ast.parse(
            textwrap.dedent(
                r"""
            foo = {
              car = {
                name = 'bmw'
              },
              options = { radio = true }
            };;;
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("foo")],
                        values=[
                            Table(
                                [
                                    Field(
                                        Name("car"),
                                        Table([Field(Name("name"), String("bmw"))]),
                                    ),
                                    Field(
                                        Name("options"),
                                        Table([Field(Name("radio"), TrueExpr())]),
                                    ),
                                ]
                            )
                        ],
                    ),
                    SemiColon(),
                    SemiColon(),
                    SemiColon(),
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_array(self):
        tree = ast.parse(
            textwrap.dedent(
                r"""
        foo = {
          1,    2,      4,
          8,    16,     32,
          64,   128,    256,
          512,  1024,   2048
        }
        """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("foo")],
                        values=[
                            Table(
                                [
                                    Field(Number(1), Number(1), between_brackets=True),
                                    Field(Number(2), Number(2), between_brackets=True),
                                    Field(Number(3), Number(4), between_brackets=True),
                                    Field(Number(4), Number(8), between_brackets=True),
                                    Field(Number(5), Number(16), between_brackets=True),
                                    Field(Number(6), Number(32), between_brackets=True),
                                    Field(Number(7), Number(64), between_brackets=True),
                                    Field(Number(8), Number(128), between_brackets=True),
                                    Field(Number(9), Number(256), between_brackets=True),
                                    Field(Number(10), Number(512), between_brackets=True),
                                    Field(Number(11), Number(1024), between_brackets=True),
                                    Field(Number(12), Number(2048), between_brackets=True),
                                ]
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_mix_dict_array(self):
        tree = ast.parse(
            textwrap.dedent(
                r"""
        foo = {
          options = { radio = true },
          "enabled",
          157,
          [true] = false,
          ['true'] = true,
        };
        """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("foo")],
                        values=[
                            Table(
                                [
                                    Field(
                                        Name("options"),
                                        Table([Field(Name("radio"), TrueExpr())]),
                                    ),
                                    Field(
                                        Number(1),
                                        String("enabled", StringDelimiter.DOUBLE_QUOTE),
                                        between_brackets=True,
                                    ),
                                    Field(Number(2), Number(157), between_brackets=True),
                                    Field(
                                        TrueExpr(), FalseExpr(), between_brackets=True
                                    ),
                                    Field(
                                        String("true"),
                                        TrueExpr(),
                                        between_brackets=True,
                                    ),
                                ]
                            )
                        ],
                    ),
                    SemiColon(),
                ]
            )
        )
        self.assertEqual(exp, tree)

    """ ----------------------------------------------------------------------- """
    """ 3.4.10 – Function Calls                                                 """
    """ ----------------------------------------------------------------------- """

    def test_function_call_simple(self):
        tree = ast.parse(r'print("hello")')
        exp = Chunk(
            Block(
                [
                    Call(
                        func=Name("print"),
                        args=[String("hello", StringDelimiter.DOUBLE_QUOTE)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_call_no_par_string(self):
        tree = ast.parse(r'print "hello"')
        exp = Chunk(
            Block(
                [
                    Call(
                        func=Name("print"),
                        args=[String("hello", StringDelimiter.DOUBLE_QUOTE)],
                        style=CallStyle.NO_PARENTHESIS,
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_call_no_par_table(self):
        tree = ast.parse(r"print {}")
        exp = Chunk(Block([Call(func=Name("print"), args=[Table([])], style=CallStyle.NO_PARENTHESIS)]))
        self.assertEqual(exp, tree)

    def test_index_function_call(self):
        tree = ast.parse(r"foo.print {}")
        exp = Chunk(
            Block([Call(func=Index(Name("print"), Name("foo")), args=[Table([])], style=CallStyle.NO_PARENTHESIS)])
        )
        self.assertEqual(exp, tree)

    def test_function_invoke(self):
        tree = ast.parse(r'foo:print("hello")')
        exp = Chunk(
            Block(
                [
                    Invoke(
                        source=Name("foo"),
                        func=Name("print"),
                        args=[String("hello", StringDelimiter.DOUBLE_QUOTE)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_nested_invoke(self):
        tree = ast.parse(r'foo:bar():print("hello")')
        exp = Chunk(
            Block(
                [
                    Invoke(
                        source=Invoke(source=Name("foo"), func=Name("bar"), args=[]),
                        func=Name("print"),
                        args=[String("hello", StringDelimiter.DOUBLE_QUOTE)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_call_args(self):
        tree = ast.parse(r'print("hello",  42)')
        exp = Chunk(
            Block(
                [
                    Call(
                        func=Name("print"),
                        args=[
                            String("hello", StringDelimiter.DOUBLE_QUOTE),
                            Number(n=42),
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_exp(self):
        tree = ast.parse(r'a = (foo + bar)[42][43](1, 2)')
        exp = Chunk(
            Block([
                Assign(
                    targets=[Name("a")],
                    values=[
                        Call(
                            func=Index(
                                idx=Number(43),
                                value=Index(
                                    idx=Number(42),
                                    value=AddOp(Name("foo"), Name("bar"), wrapped=True),
                                    notation=IndexNotation.SQUARE
                                ),
                                notation=IndexNotation.SQUARE
                            ),
                            args=[Number(1), Number(2)]
                        )
                    ]
                )
            ])
        )
        self.assertEqual(exp, tree)

    def test_function_exp_invoke(self):
        tree = ast.parse(r'a = (foo + bar)[42]:hello "ok"')
        exp = Chunk(
            Block([
                Assign(
                    targets=[Name("a")],
                    values=[
                        Invoke(
                            source=Index(
                                idx=Number(42),
                                value=AddOp(Name("foo"), Name("bar"), wrapped=True),
                                notation=IndexNotation.SQUARE
                            ),
                            func=Name("hello"),
                            args=[String("ok", delimiter=StringDelimiter.DOUBLE_QUOTE)],
                            style=CallStyle.NO_PARENTHESIS,
                        )
                    ]
                )
            ])
        )
        self.assertEqual(exp, tree)

    """ ----------------------------------------------------------------------- """
    """ 3.4.11 – Function Definitions                                           """
    """ ----------------------------------------------------------------------- """

    def test_function_def_anonymous(self):
        tree = ast.parse(r"f = function() local a <const> end")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("f")],
                        values=[
                            AnonymousFunction(
                                args=[],
                                body=Block(
                                    [LocalAssign(targets=[Name("a", attribute=Attribute(Name("const")))], values=[])]
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_def_global(self):
        tree = ast.parse(r"function f() end")
        exp = Chunk(Block([Function(name=Name("f"), args=[], body=Block([]))]))
        self.assertEqual(exp, tree)

    def test_function_def_local(self):
        tree = ast.parse(r"local function _process() end")
        exp = Chunk(
            Block([LocalFunction(name=Name("_process"), args=[], body=Block([]))])
        )
        self.assertEqual(exp, tree)

    def test_function_def_indexed_name_global(self):
        tree = ast.parse(r"function t.a.b.c.f() end")
        exp = Chunk(
            Block(
                [
                    Function(
                        name=Index(
                            idx=Name("f"),
                            value=Index(
                                idx=Name("c"),
                                value=Index(
                                    idx=Name("b"),
                                    value=Index(idx=Name("a"), value=Name("t")),
                                ),
                            ),
                        ),
                        args=[],
                        body=Block([]),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_function_def_global_assign(self):
        tree = ast.parse(r"t.a.b.c.f = function () end")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[
                            Index(
                                idx=Name("f"),
                                value=Index(
                                    idx=Name("c"),
                                    value=Index(
                                        idx=Name("b"),
                                        value=Index(idx=Name("a"), value=Name("t")),
                                    ),
                                ),
                            )
                        ],
                        values=[AnonymousFunction(args=[], body=Block([]))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)
