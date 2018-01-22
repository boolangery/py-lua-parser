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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[
                AddOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        print(ast.toPrettyStr(tree))
        self.assertEqual(exp, tree)

    def test_substraction(self):
        tree = ast.parse(r'a = 1 - 0.2')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[
                MultOp(
                    left=Number(1),
                    right=Number(0.2)
                )
            ]
        )]))
        print(ast.toPrettyStr(tree))
        self.assertEqual(exp, tree)

    def test_float_division(self):
        tree = ast.parse(r'a = 1 / 0.2')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[
                USubOp(operand=Number(1))
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_exponentiation(self):
        tree = ast.parse(r'a = 1^2')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[BAndOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_or(self):
        tree = ast.parse(r'a = 3|5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[BOrOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_exclusive_or(self):
        tree = ast.parse(r'a = 3 ~ 5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[BXorOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_right_shift(self):
        tree = ast.parse(r'a = 3 >> 5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[BShiftROp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_left_shirt(self):
        tree = ast.parse(r'a = 3 << 5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[BShiftLOp(
                left=Number(3),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_bitwise_unary_not(self):
        tree = ast.parse(r'a = ~5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[UBNotOp(operand=Number(5))]
        )]))
        self.assertEqual(exp, tree)

    """
    3.4.4 – Relational Operators
    """
    def test_less_than(self):
        tree = ast.parse(r'res = (1 < 2)')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[LessThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_greater_than(self):
        tree = ast.parse(r'res = (1 > 2)')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[GreaterThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_less_or_eq_than(self):
        tree = ast.parse(r'res = (1 <= 2)')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[LessOrEqThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_greater_or_eq_than(self):
        tree = ast.parse(r'res = (1 >= 2)')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[GreaterOrEqThanOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_equal_than(self):
        tree = ast.parse(r'res = 1 == 2')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[EqToOp(
                left=Number(1),
                right=Number(2)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_not_equal_than(self):
        tree = ast.parse(r'res = 1 ~= 2')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[AndLoOp(
                left=Number(4),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_logic_or(self):
        tree = ast.parse(r'res = 4 or 5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[OrLoOp(
                left=Number(4),
                right=Number(5)
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_logic_not(self):
        tree = ast.parse(r'res = not 5')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='res')],
            values=[ULNotOp(operand=Number(5))]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def test_concatenation(self):
        tree = ast.parse(r'str = "begin".."end"')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='str')],
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='len')],
            values=[ULengthOP(operand=Name(id='t'))]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def test_dict(self):
        tree = ast.parse(r'a = {foo = "bar", bar = "foo"}')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='a')],
            values=[Table(
                keys=[
                    Name(id='foo'),
                    Name(id='bar')
                ],
                values=[
                    String(s='bar'),
                    String(s='foo')
                ]
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_nested_dict(self):
        tree = ast.parse(textwrap.dedent(r'''
            foo = {
              car = {
                name = 'bmw'
              },
              options = { radio = true }
            };;;
            '''))
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='foo')],
            values=[Table(
                keys=[
                    Name(id='car'),
                    Name(id='options')
                ],
                values=[
                    Table(keys=[Name(id='name')], values=[String(s='bmw')]),
                    Table(keys=[Name(id='radio')], values=[TrueExpr()]),
                ]
            )]
        )]))
        print(ast.toPrettyStr(tree))
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
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='foo')],
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
          157
        };
        '''))
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='foo')],
            values=[Table(
                keys=[
                    Name('options'),  Number(1),  Number(2)
                ],
                values=[
                    Table(keys=[Name(id='radio')], values=[TrueExpr()]),
                    String('enabled'), Number(157)
                ]
            )]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.10 – Function Calls                                                 '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_call_simple(self):
        tree = ast.parse(r'print("hello")')
        exp = Chunk(body=Block(body=[Call(
            func=Name(id='print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

    def test_function_call_no_par_string(self):
        tree = ast.parse(r'print "hello"')
        exp = Chunk(body=Block(body=[Call(
            func=Name(id='print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

    def test_function_call_no_par_table(self):
        tree = ast.parse(r'print {}')
        exp = Chunk(body=Block(body=[Call(
            func=Name(id='print'),
            args=[Table([], [])]
        )]))
        self.assertEqual(exp, tree)

    def test_index_function_call(self):
        tree = ast.parse(r'foo.print {}')
        exp = Chunk(body=Block(body=[Call(
            func=Index(Name(id='print'), Name(id='foo')),
            args=[Table([], [])]
        )]))
        self.assertEqual(exp, tree)

    def test_function_invoke(self):
        tree = ast.parse(r'foo:print("hello")')
        exp = Chunk(body=Block(body=[Invoke(
            source=Name('foo'),
            func=Name(id='print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

    def test_function_nested_invoke(self):
        tree = ast.parse(r'foo:bar():print("hello")')
        exp = Chunk(body=Block(body=[Invoke(
            source=Invoke(
                source=Name('foo'),
                func=Name(id='bar'),
                args=[]
            ),
            func=Name(id='print'),
            args=[String('hello')]
        )]))
        self.assertEqual(exp, tree)

    def test_function_call_args(self):
        tree = ast.parse(r'print("hello",  42)')
        exp = Chunk(body=Block(body=[Call(
            func=Name(id='print'),
            args=[String('hello'), Number(n=42)]
        )]))
        self.assertEqual(exp, tree)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_definition(self):
        tree = ast.parse(r'f = function() local a end')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Name(id='f')],
            values=[Function(
                name='',
                args=[],
                body=[LocalAssign(
                    targets=[Name(id='a')],
                    values=[]
                )]
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_function_definition_1(self):
        tree = ast.parse(r'function f() end')
        exp = Chunk(body=Block(body=[Function(
            name='f',
            args=[],
            body=[]
        )]))
        self.assertEqual(exp, tree)

    def test_function_definition_2(self):
        tree = ast.parse(r'function t.a.b.c.f() end')
        exp = Chunk(body=Block(body=[Function(
            name=Index(
                idx='f',
                value=Index(
                    idx='c',
                    value=Index(
                        idx='b',
                        value=Index(
                            idx='a',
                            value=Name(id='t')
                        )
                    )
                )),
            args=[],
            body=[]
        )]))
        self.assertEqual(exp, tree)

    def test_function_definition_3(self):
        tree = ast.parse(r't.a.b.c.f = function () end')
        exp = Chunk(body=Block(body=[Assign(
            targets=[Index(
                idx=Name('f'),
                value=Index(
                    idx=Name('c'),
                    value=Index(
                        idx=Name('b'),
                        value=Index(
                            idx=Name('a'),
                            value=Name(id='t')
                        )
                    )
                ))],
            values=[Function(
                name='',
                args=[],
                body=[]
            )]
        )]))
        self.assertEqual(exp, tree)

    def test_function_definition_4(self):
        tree = ast.parse(r'local function f () end')
        exp = Chunk(body=Block(body=[LocalFunction(
            name='f',
            args=[],
            body=[]
        )]))
        self.assertEqual(exp, tree)

    def test_function_definition_5(self):
        tree = ast.parse(textwrap.dedent("""
            function MetaTable.__call (func)
            end
            """))
        exp = Chunk(body=Block(body=[Function(
            name=Index(idx='__call', value=Name('MetaTable')),
            args=[Name('func')],
            body=[]
        )]))
        self.assertEqual(exp, tree)