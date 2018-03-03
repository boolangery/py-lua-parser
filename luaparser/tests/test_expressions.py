from luaparser.utils  import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


# https://www.lua.org/manual/5.3/manual.html#3.4

class ExpressionsTestCase(tests.TestCase):
    """
    3.4.1 – Arithmetic Operators
    """
    def test_addition(self):
        tree = ast.parse(r'a = 1 + 0.2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                AddOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[0], Chunk)
        self.assertEqual(nodes[0].tokens[0].value.text, 'a')
        self.assertEqual(nodes[0].tokens[1].value.text, ' ')
        self.assertEqual(nodes[0].tokens[2].value.text, '=')
        self.assertEqual(nodes[0].tokens[3].value.text, ' ')
        self.assertEqual(nodes[0].tokens[4].value.text, '1')
        self.assertEqual(nodes[0].tokens[5].value.text, ' ')
        self.assertEqual(nodes[0].tokens[6].value.text, '+')
        self.assertEqual(nodes[0].tokens[7].value.text, ' ')
        self.assertEqual(nodes[0].tokens[8].value.text, '0.2')

        self.assertIsInstance(nodes[1], Block)
        self.assertEqual(nodes[1].tokens[0].value.text, 'a')
        self.assertEqual(nodes[1].tokens[1].value.text, ' ')
        self.assertEqual(nodes[1].tokens[2].value.text, '=')
        self.assertEqual(nodes[1].tokens[3].value.text, ' ')
        self.assertEqual(nodes[1].tokens[4].value.text, '1')
        self.assertEqual(nodes[1].tokens[5].value.text, ' ')
        self.assertEqual(nodes[1].tokens[6].value.text, '+')
        self.assertEqual(nodes[1].tokens[7].value.text, ' ')
        self.assertEqual(nodes[1].tokens[8].value.text, '0.2')

        self.assertIsInstance(nodes[2], Assign)
        self.assertEqual(nodes[2].tokens[0].value.text, 'a')
        self.assertEqual(nodes[2].tokens[1].value.text, ' ')
        self.assertEqual(nodes[2].tokens[2].value.text, '=')
        self.assertEqual(nodes[2].tokens[3].value.text, ' ')
        self.assertEqual(nodes[2].tokens[4].value.text, '1')
        self.assertEqual(nodes[2].tokens[5].value.text, ' ')
        self.assertEqual(nodes[2].tokens[6].value.text, '+')
        self.assertEqual(nodes[2].tokens[7].value.text, ' ')
        self.assertEqual(nodes[2].tokens[8].value.text, '0.2')

        self.assertIsInstance(nodes[3], Name)
        self.assertEqual(nodes[3].tokens[0].value.text, 'a')

        self.assertIsInstance(nodes[4], AddOp)
        self.assertEqual(nodes[4].tokens[0].value.text, ' ')
        self.assertEqual(nodes[4].tokens[1].value.text, '1')
        self.assertEqual(nodes[4].tokens[2].value.text, ' ')
        self.assertEqual(nodes[4].tokens[3].value.text, '+')
        self.assertEqual(nodes[4].tokens[4].value.text, ' ')
        self.assertEqual(nodes[4].tokens[5].value.text, '0.2')

        self.assertIsInstance(nodes[5], Number)
        self.assertEqual(nodes[5].tokens[0].value.text, ' ')
        self.assertEqual(nodes[5].tokens[1].value.text, '1')

        self.assertIsInstance(nodes[6], Number)
        self.assertEqual(nodes[6].tokens[0].value.text, ' ')
        self.assertEqual(nodes[6].tokens[1].value.text, '0.2')


    def test_substraction(self):
        tree = ast.parse(r'a = 1 - 0.2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                SubOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_multiplication(self):
        tree = ast.parse(r'a = 1 * 0.2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                MultOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_float_division(self):
        tree = ast.parse(r'a = 1 / 0.2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                FloatDivOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_floor_division(self):
        tree = ast.parse(r'a = 1 // 0.2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                FloorDivOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_mod(self):
        tree = ast.parse(r'a = 1 % 0.2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                ModOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_unary_sub(self):
        tree = ast.parse(r'a = -1')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[
                UMinusOp(operand=Number(1))
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_exponentiation(self):
        tree = ast.parse(r'a = 1^2')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[ExpoOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    """
    3.4.2 – Bitwise Operators
    """
    def test_bitwise_and(self):
        tree = ast.parse(r'a = 3&5')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[BAndOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_or(self):
        tree = ast.parse(r'a = 3|5')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[BOrOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_exclusive_or(self):
        tree = ast.parse(r'a = 3 ~ 5')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[BXorOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_right_shift(self):
        tree = ast.parse(r'a = 3 >> 5')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[BShiftROp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_left_shirt(self):
        tree = ast.parse(r'a = 3 << 5')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[BShiftLOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_unary_not(self):
        tree = ast.parse(r'a = ~5')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[UBNotOp(operand=Number(5))]
        )]))
        self.assertEqual(exp, tree)

    """
    3.4.4 – Relational Operators
    """
    def test_less_than(self):
        tree = ast.parse(r'res = (1 < 2)')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[LessThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_greater_than(self):
        tree = ast.parse(r'res = (1 > 2)')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[GreaterThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_less_or_eq_than(self):
        tree = ast.parse(r'res = (1 <= 2)')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[LessOrEqThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_greater_or_eq_than(self):
        tree = ast.parse(r'res = (1 >= 2)')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[GreaterOrEqThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_equal_than(self):
        tree = ast.parse(r'res = 1 == 2')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[EqToOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_not_equal_than(self):
        tree = ast.parse(r'res = 1 ~= 2')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[NotEqToOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)


    """
    3.4.5 – Logical Operators
    """
    def test_logic_and(self):
        tree = ast.parse(r'res = 4 and 5')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[AndLoOp(
                left=Number(4),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_logic_or(self):
        tree = ast.parse(r'res = 4 or 5')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[OrLoOp(
                left=Number(4),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_logic_not(self):
        tree = ast.parse(r'res = not 5')
        exp = Chunk(Block([Assign(
            targets=[Name('res')],
            values=[ULNotOp(operand=Number(5))]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def test_concatenation(self):
        tree = ast.parse(r'str = "begin".."end"')
        exp = Chunk(Block([Assign(
            targets=[Name('str')],
            values=[Concat(
                left=String('begin'),
                right=String('end')
            )]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.7 – The Length Operator                                             '''
    ''' ----------------------------------------------------------------------- '''
    def test_length_op(self):
        tree = ast.parse(r'len = #t')
        exp = Chunk(Block([Assign(
            targets=[Name('len')],
            values=[ULengthOP(operand=Name('t'))]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))
        self.assertIsInstance(nodes[4], ULengthOP)
        self.assertEqual(nodes[4].tokens[0].value.text, ' ')
        self.assertEqual(nodes[4].tokens[1].value.text, '#')
        self.assertEqual(nodes[4].tokens[2].value.text, 't')


    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def test_dict(self):
        tree = ast.parse(r'a = {foo = "bar", bar = "foo"}')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[Table(
                keys=[
                    Name('foo'),
                    Name('bar')
                ],
                values=[
                    String('bar'),
                    String('foo')
                ]
            )]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[4], Table)
        self.assertEqual(nodes[4].tokens[0].value.text, ' ')
        self.assertEqual(nodes[4].tokens[1].value.text, '{')
        self.assertEqual(nodes[4].tokens[2].value.text, 'foo')
        self.assertEqual(nodes[4].tokens[3].value.text, ' ')
        self.assertEqual(nodes[4].tokens[4].value.text, '=')
        self.assertEqual(nodes[4].tokens[5].value.text, ' ')
        self.assertEqual(nodes[4].tokens[6].value.text, '"bar"')
        self.assertEqual(nodes[4].tokens[7].value.text, ',')
        self.assertEqual(nodes[4].tokens[8].value.text, ' ')
        self.assertEqual(nodes[4].tokens[9].value.text, 'bar')
        self.assertEqual(nodes[4].tokens[10].value.text, ' ')
        self.assertEqual(nodes[4].tokens[11].value.text, '=')
        self.assertEqual(nodes[4].tokens[12].value.text, ' ')
        self.assertEqual(nodes[4].tokens[13].value.text, '"foo"')
        self.assertEqual(nodes[4].tokens[14].value.text, '}')


    def test_nested_dict(self):
        tree = ast.parse(textwrap.dedent(r'''
            foo = {
              car = {
                name = 'bmw'
              },
              options = { radio = true }
            };;;
            '''))
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Table(
                keys=[
                    Name('car'),
                    Name('options')
                ],
                values=[
                    Table(keys=[Name('name')], values=[String('bmw')]),
                    Table(keys=[Name('radio')], values=[TrueExpr()]),
                ]
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_array(self):
        tree = ast.parse(textwrap.dedent(r'''
        foo = {
          1,    2,      4,
          8,    16,     32,
          64,   128,    256,
          512,  1024,   2048
        }
        '''))
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Table(
                keys=[
                    Number(1),  Number(2),  Number(3),
                    Number(4),  Number(5),  Number(6),
                    Number(7),  Number(8),  Number(9),
                    Number(10), Number(11), Number(12)
                ],
                values=[
                    Number(1),  Number(2),   Number(4),
                    Number(8),  Number(16),  Number(32),
                    Number(64), Number(128), Number(256),
                    Number(512),Number(1024),Number(2048)
                ]
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_mix_dict_array(self):
        tree = ast.parse(textwrap.dedent(r'''
        foo = {
          options = { radio = true },
          "enabled",
          157,
          [true] = false,
          ['true'] = true,
        };
        '''))
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Table(
                keys=[
                    Name('options'),  Number(1),  Number(2),
                    TrueExpr(), String('true')
                ],
                values=[
                    Table(keys=[Name('radio')], values=[TrueExpr()]),
                    String('enabled'), Number(157),
                    FalseExpr(), TrueExpr()
                ]
            )]
        )]))
        self.assertEqual(exp, tree)

        # test if all tokens included in '[true]' key
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[13], TrueExpr)
        self.assertEqual(nodes[13].tokens[0].value.text, '\n')
        self.assertEqual(nodes[13].tokens[1].value.text, '  ')
        self.assertEqual(nodes[13].tokens[2].value.text, '[')
        self.assertEqual(nodes[13].tokens[3].value.text, 'true')
        self.assertEqual(nodes[13].tokens[4].value.text, ']')

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.10 – Function Calls                                                 '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_call_simple(self):
        tree = ast.parse(r'print("hello")')
        exp = Chunk(Block([Call(
            func=Name('print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Call)
        self.assertEqual(nodes[2].tokens[0].value.text, 'print')
        self.assertEqual(nodes[2].tokens[1].value.text, '(')
        self.assertEqual(nodes[2].tokens[2].value.text, '"hello"')
        self.assertEqual(nodes[2].tokens[3].value.text, ')')

    def test_function_call_no_par_string(self):
        tree = ast.parse(r'print "hello"')
        exp = Chunk(Block([Call(
            func=Name('print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

    def test_function_call_no_par_table(self):
        tree = ast.parse(r'print {}')
        exp = Chunk(Block([Call(
            func=Name('print'),
            args=[Table([], [])]
        )]))
        self.assertEqual(exp, tree)

    def test_index_function_call(self):
        tree = ast.parse(r'foo.print {}')
        exp = Chunk(Block([Call(
            func=Index(Name('print'), Name('foo')),
            args=[Table([], [])]
        )]))
        self.assertEqual(exp, tree)

    def test_function_invoke(self):
        tree = ast.parse(r'foo:print("hello")')
        exp = Chunk(Block([Invoke(
            source=Name('foo'),
            func=Name('print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Invoke)
        self.assertEqual(nodes[2].tokens[0].value.text, 'foo')
        self.assertEqual(nodes[2].tokens[1].value.text, ':')
        self.assertEqual(nodes[2].tokens[2].value.text, 'print')
        self.assertEqual(nodes[2].tokens[3].value.text, '(')
        self.assertEqual(nodes[2].tokens[4].value.text, '"hello"')
        self.assertEqual(nodes[2].tokens[5].value.text, ')')

    def test_function_nested_invoke(self):
        tree = ast.parse(r'foo:bar():print("hello")')
        exp = Chunk(Block([Invoke(
            source=Invoke(
                source=Name('foo'),
                func=Name('bar'),
                args=[]
            ),
            func=Name('print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Invoke)
        self.assertEqual(nodes[2].tokens[0].value.text, 'foo')
        self.assertEqual(nodes[2].tokens[1].value.text, ':')
        self.assertEqual(nodes[2].tokens[2].value.text, 'bar')
        self.assertEqual(nodes[2].tokens[3].value.text, '(')
        self.assertEqual(nodes[2].tokens[4].value.text, ')')
        self.assertEqual(nodes[2].tokens[5].value.text, ':')
        self.assertEqual(nodes[2].tokens[6].value.text, 'print')
        self.assertEqual(nodes[2].tokens[7].value.text, '(')
        self.assertEqual(nodes[2].tokens[8].value.text, '"hello"')
        self.assertEqual(nodes[2].tokens[9].value.text, ')')

        self.assertIsInstance(nodes[3], Invoke)
        self.assertEqual(nodes[3].tokens[0].value.text, 'foo')
        self.assertEqual(nodes[3].tokens[1].value.text, ':')
        self.assertEqual(nodes[3].tokens[2].value.text, 'bar')
        self.assertEqual(nodes[3].tokens[3].value.text, '(')
        self.assertEqual(nodes[3].tokens[4].value.text, ')')


    def test_function_call_args(self):
        tree = ast.parse(r'print("hello",  42)')
        exp = Chunk(Block([Call(
            func=Name('print'),
            args=[String('hello'), Number(n=42)]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_def_anonymous(self):
        tree = ast.parse(r'f = function() local a end')
        exp = Chunk(Block([Assign(
            targets=[Name('f')],
            values=[AnonymousFunction(
                args=[],
                body=Block([LocalAssign(
                    targets=[Name('a')],
                    values=[]
                )])
            )]
        )]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[4], AnonymousFunction)
        self.assertEqual(nodes[4].tokens[0].value.text, ' ')
        self.assertEqual(nodes[4].tokens[1].value.text, 'function')
        self.assertEqual(nodes[4].tokens[2].value.text, '(')
        self.assertEqual(nodes[4].tokens[3].value.text, ')')
        self.assertEqual(nodes[4].tokens[4].value.text, ' ')
        self.assertEqual(nodes[4].tokens[5].value.text, 'local')
        self.assertEqual(nodes[4].tokens[6].value.text, ' ')
        self.assertEqual(nodes[4].tokens[7].value.text, 'a')
        self.assertEqual(nodes[4].tokens[8].value.text, ' ')
        self.assertEqual(nodes[4].tokens[9].value.text, 'end')

    def test_function_def_global(self):
        tree = ast.parse(r'function f() end')
        exp = Chunk(Block([Function(
            name=Name('f'),
            args=[],
            body=Block([])
        )]))
        self.assertEqual(exp, tree)

    def test_function_def_local(self):
        tree = ast.parse(r'local function _process() end')
        exp = Chunk(Block([LocalFunction(
            name=Name('_process'),
            args=[],
            body=Block([])
        )]))
        self.assertEqual(exp, tree)

    def test_function_def_indexed_name_global(self):
        tree = ast.parse(r'function t.a.b.c.f() end')
        exp = Chunk(Block([Function(
            name=Index(
                idx=Name('f'),
                value=Index(
                    idx=Name('c'),
                    value=Index(
                        idx=Name('b'),
                        value=Index(
                            idx=Name('a'),
                            value=Name('t')
                        )
                    )
                )),
            args=[],
            body=Block([])
        )]))
        self.assertEqual(exp, tree)

    def test_function_def_global_assign(self):
        tree = ast.parse(r't.a.b.c.f = function () end')
        exp = Chunk(Block([Assign(
            targets=[Index(
                idx=Name('f'),
                value=Index(
                    idx=Name('c'),
                    value=Index(
                        idx=Name('b'),
                        value=Index(
                            idx=Name('a'),
                            value=Name('t')
                        )
                    )
                ))],
            values=[AnonymousFunction(
                args=[],
                body=Block([])
            )]
        )]))
        self.assertEqual(exp, tree)
