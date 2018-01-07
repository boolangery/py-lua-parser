from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


# https://www.lua.org/manual/5.3/manual.html#3.4

class ExpressionsTestCase(tests.TestCase):
    """
    3.4.1 – Arithmetic Operators
    """
    def setUp(self):
        self.parser = Parser()

    def test_addition(self):
        ast = self.parser.srcToAST(r'a = 1 + 0.2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                AddOpExpr(
                    left=NumberExpr(1),
                    right=NumberExpr(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_substraction(self):
        ast = self.parser.srcToAST(r'a = 1 - 0.2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                SubOpExpr(
                    left=NumberExpr(1),
                    right=NumberExpr(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_multiplication(self):
        ast = self.parser.srcToAST(r'a = 1 * 0.2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                MultOpExpr(
                    left=NumberExpr(1),
                    right=NumberExpr(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_float_division(self):
        ast = self.parser.srcToAST(r'a = 1 / 0.2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                FloatDivOpExpr(
                    left=NumberExpr(1),
                    right=NumberExpr(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_floor_division(self):
        ast = self.parser.srcToAST(r'a = 1 // 0.2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                FloorDivOpExpr(
                    left=NumberExpr(1),
                    right=NumberExpr(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_mod(self):
        ast = self.parser.srcToAST(r'a = 1 % 0.2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                ModOpExpr(
                    left=NumberExpr(1),
                    right=NumberExpr(0.2)
                )
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_unary_sub(self):
        ast = self.parser.srcToAST(r'a = -1')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[
                USubOpExpr(operand=NumberExpr(1))
            ]
        )]))
        self.assertEqual(exp, ast)

    def test_exponentiation(self):
        ast = self.parser.srcToAST(r'a = 1^2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[ExpoOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)

    """
    3.4.2 – Bitwise Operators
    """
    def test_bitwise_and(self):
        ast = self.parser.srcToAST(r'a = 3&5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[BAndOpExpr(
                left=NumberExpr(3),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_bitwise_or(self):
        ast = self.parser.srcToAST(r'a = 3|5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[BOrOpExpr(
                left=NumberExpr(3),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_bitwise_exclusive_or(self):
        ast = self.parser.srcToAST(r'a = 3 ~ 5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[BXorOpExpr(
                left=NumberExpr(3),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_bitwise_right_shift(self):
        ast = self.parser.srcToAST(r'a = 3 >> 5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[BShiftROpExpr(
                left=NumberExpr(3),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_bitwise_left_shirt(self):
        ast = self.parser.srcToAST(r'a = 3 << 5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[BShiftLOpExpr(
                left=NumberExpr(3),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_bitwise_unary_not(self):
        ast = self.parser.srcToAST(r'a = ~5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[UBNotOpExpr(operand=NumberExpr(5))]
        )]))
        self.assertEqual(exp, ast)

    """
    3.4.4 – Relational Operators
    """
    def test_less_than(self):
        ast = self.parser.srcToAST(r'res = (1 < 2)')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[LessThanOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_greater_than(self):
        ast = self.parser.srcToAST(r'res = (1 > 2)')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[GreaterThanOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_less_or_eq_than(self):
        ast = self.parser.srcToAST(r'res = (1 <= 2)')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[LessOrEqThanOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_greater_or_eq_than(self):
        ast = self.parser.srcToAST(r'res = (1 >= 2)')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[GreaterOrEqThanOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_equal_than(self):
        ast = self.parser.srcToAST(r'res = 1 == 2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[EqToOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_not_equal_than(self):
        ast = self.parser.srcToAST(r'res = 1 ~= 2')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[NotEqToOpExpr(
                left=NumberExpr(1),
                right=NumberExpr(2)
            )]
        )]))
        self.assertEqual(exp, ast)


    """
    3.4.5 – Logical Operators
    """
    def test_logic_and(self):
        ast = self.parser.srcToAST(r'res = 4 and 5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[AndLoOpExpr(
                left=NumberExpr(4),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_logic_or(self):
        ast = self.parser.srcToAST(r'res = 4 or 5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[OrLoOpExpr(
                left=NumberExpr(4),
                right=NumberExpr(5)
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_logic_not(self):
        ast = self.parser.srcToAST(r'res = not 5')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='res')],
            values=[ULNotOpExpr(operand=NumberExpr(5))]
        )]))
        self.assertEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def test_concatenation(self):
        ast = self.parser.srcToAST(r'str = "begin".."end"')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='str')],
            values=[ConcatExpr(
                left=StringExpr('begin'),
                right=StringExpr('end')
            )]
        )]))
        self.assertEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.7 – The Length Operator                                             '''
    ''' ----------------------------------------------------------------------- '''
    def test_length_op(self):
        ast = self.parser.srcToAST(r'len = #t')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='len')],
            values=[ULengthOP(operand=NameExpr(id='t'))]
        )]))
        self.assertEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def test_dict(self):
        ast = self.parser.srcToAST(r'a = {foo = "bar", bar = "foo"}')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='a')],
            values=[TableExpr(
                keys=[
                    NameExpr(id='foo'),
                    NameExpr(id='bar')
                ],
                values=[
                    StringExpr(s='bar'),
                    StringExpr(s='foo')
                ]
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_nested_dict(self):
        ast = self.parser.srcToAST(textwrap.dedent(r'''
            foo = {
              car = {
                name = 'bmw'
              },
              options = { radio = true }
            };
            '''))
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[TableExpr(
                keys=[
                    NameExpr(id='car'),
                    NameExpr(id='options')
                ],
                values=[
                    TableExpr(keys=[NameExpr(id='name')], values=[StringExpr(s='bmw')]),
                    TableExpr(keys=[NameExpr(id='radio')], values=[TrueExpr()]),
                ]
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_array(self):
        ast = self.parser.srcToAST(textwrap.dedent(r'''
        foo = {
          1,    2,      4,
          8,    16,     32,
          64,   128,    256,
          512,  1024,   2048
        }
        '''))
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[TableExpr(
                keys=[
                    NumberExpr(1),  NumberExpr(2),  NumberExpr(3),
                    NumberExpr(4),  NumberExpr(5),  NumberExpr(6),
                    NumberExpr(7),  NumberExpr(8),  NumberExpr(9),
                    NumberExpr(10), NumberExpr(11), NumberExpr(12)
                ],
                values=[
                    NumberExpr(1),  NumberExpr(2),   NumberExpr(4),
                    NumberExpr(8),  NumberExpr(16),  NumberExpr(32),
                    NumberExpr(64), NumberExpr(128), NumberExpr(256),
                    NumberExpr(512),NumberExpr(1024),NumberExpr(2048)
                ]
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_mix_dict_array(self):
        ast = self.parser.srcToAST(textwrap.dedent(r'''
        foo = {
          options = { radio = true },
          "enabled",
          157
        };
        '''))
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='foo')],
            values=[TableExpr(
                keys=[
                    NameExpr('options'),  NumberExpr(1),  NumberExpr(2)
                ],
                values=[
                    TableExpr(keys=[NameExpr(id='radio')], values=[TrueExpr()]),
                    StringExpr('enabled'), NumberExpr(157)
                ]
            )]
        )]))
        self.assertEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.10 – Function Calls                                                 '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_call(self):
        ast = self.parser.srcToAST(r'print("hello")')
        exp = Chunk(body=Block(body=[CallStat(
            func=NameExpr(id='print'),
            args=[StringExpr('hello')]
        )]))
        self.assertEqual(exp, ast)

    def test_function_call_no_parent(self):
        ast = self.parser.srcToAST(r'print "hello"')
        exp = Chunk(body=Block(body=[CallStat(
            func=NameExpr(id='print'),
            args=[StringExpr('hello')]
        )]))
        self.assertEqual(exp, ast)

    def test_function_invoke(self):
        ast = self.parser.srcToAST(r'foo:print("hello")')
        exp = Chunk(body=Block(body=[InvokeStat(
            source=NameExpr('foo'),
            func=NameExpr(id='print'),
            args=[StringExpr('hello')]
        )]))
        self.assertEqual(exp, ast)

    def test_function_nested_invoke(self):
        ast = self.parser.srcToAST(r'foo:bar():print("hello")')
        exp = Chunk(body=Block(body=[InvokeStat(
            source=InvokeStat(
                source=NameExpr('foo'),
                func=NameExpr(id='bar'),
                args=[]
            ),
            func=NameExpr(id='print'),
            args=[StringExpr('hello')]
        )]))
        self.assertEqual(exp, ast)

    def test_function_call_args(self):
        ast = self.parser.srcToAST(r'print("hello",  42)')
        exp = Chunk(body=Block(body=[CallStat(
            func=NameExpr(id='print'),
            args=[StringExpr('hello'), NumberExpr(n=42)]
        )]))
        self.assertEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_definition(self):
        ast = self.parser.srcToAST(r'f = function() local a end')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[NameExpr(id='f')],
            values=[FunctionExpr(
                name='',
                args=[],
                body=[LocalAssignStat(
                    targets=[NameExpr(id='a')],
                    values=[]
                )]
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_function_definition_1(self):
        ast = self.parser.srcToAST(r'function f() end')
        exp = Chunk(body=Block(body=[FunctionExpr(
            name='f',
            args=[],
            body=[]
        )]))
        self.assertEqual(exp, ast)

    def test_function_definition_2(self):
        ast = self.parser.srcToAST(r'function t.a.b.c.f() end')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[IndexExpr(
                idx='f',
                value=IndexExpr(
                    idx='c',
                    value=IndexExpr(
                        idx='b',
                        value=IndexExpr(
                            idx='a',
                            value=NameExpr(id='t')
                        )
                    )
                ))],
            values=[FunctionExpr(
                name='',
                args=[],
                body=[]
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_function_definition_3(self):
        ast = self.parser.srcToAST(r't.a.b.c.f = function () end')
        exp = Chunk(body=Block(body=[AssignStat(
            targets=[IndexExpr(
                idx=NameExpr('f'),
                value=IndexExpr(
                    idx=NameExpr('c'),
                    value=IndexExpr(
                        idx=NameExpr('b'),
                        value=IndexExpr(
                            idx=NameExpr('a'),
                            value=NameExpr(id='t')
                        )
                    )
                ))],
            values=[FunctionExpr(
                name='',
                args=[],
                body=[]
            )]
        )]))
        self.assertEqual(exp, ast)

    def test_function_definition_4(self):
        ast = self.parser.srcToAST(r'local function f () end')
        exp = Chunk(body=Block(body=[LocalFunctionExpr(
            name='f',
            args=[],
            body=[]
        )]))
        self.assertEqual(exp, ast)
