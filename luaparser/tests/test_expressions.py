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
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(AddOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_subtraction(self):
        ast = self.parser.srcToAST(r'a = 1 - 0.2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(SubOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_multiplication(self):
        ast = self.parser.srcToAST(r'a = 1 * 0.2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(MultOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_float_division(self):
        ast = self.parser.srcToAST(r'a = 1 / 0.2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(FloatDivOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_floor_division(self):
        ast = self.parser.srcToAST(r'a = 1 // 0.2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(FloorDivOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_mod_division(self):
        ast = self.parser.srcToAST(r'a = 1 % 0.2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(ModOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_negation(self):
        ast = self.parser.srcToAST(r'a = -1')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(UnOpNegExpr(NumberExpr(1)))])))
        self.assertAstEqual(exp, ast)

    def test_exponentiation(self):
        ast = self.parser.srcToAST(r'a = 1^2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(ExpoOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)

    """
    3.4.2 – Bitwise Operators
    """
    def test_bitwise_and(self):
        ast = self.parser.srcToAST(r'a = 3&5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(AndOpExpr([NumberExpr(3), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_bitwise_or(self):
        ast = self.parser.srcToAST(r'a = 3|5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(OrOpExpr([NumberExpr(3), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_bitwise_exclusive_or(self):
        ast = self.parser.srcToAST(r'a = 3 ~ 5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(XorOpExpr([NumberExpr(3), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_bitwise_right_shift(self):
        ast = self.parser.srcToAST(r'a = 3 >> 5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(ShiftROpExpr([NumberExpr(3), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_bitwise_right_left(self):
        ast = self.parser.srcToAST(r'a = 3 << 5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(ShiftLOpExpr([NumberExpr(3), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_bitwise_unary_not(self):
        ast = self.parser.srcToAST(r'a = ~5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(UnOpNotExpr(NumberExpr(5)))])))
        self.assertAstEqual(exp, ast)

    """
    3.4.4 – Relational Operators
    """
    def test_less_than(self):
        ast = self.parser.srcToAST(r'res = (1 < 2)')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(LessThanOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)

    def test_greater_than(self):
        ast = self.parser.srcToAST(r'res = (1 > 2)')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(GreaterThanOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)

    def test_less_or_eq_than(self):
        ast = self.parser.srcToAST(r'res = (1 <= 2)')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(LessOrEqThanOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)

    def test_greater_or_eq_than(self):
        ast = self.parser.srcToAST(r'res = (1 >= 2)')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(GreaterOrEqThanOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)

    def test_equal_than(self):
        ast = self.parser.srcToAST(r'res = 1 == 2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(EqToOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)

    def test_not_equal_than(self):
        ast = self.parser.srcToAST(r'res = 1 ~= 2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(NotEqToOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)


    """
    3.4.5 – Logical Operators
    """
    def test_logic_and(self):
        ast = self.parser.srcToAST(r'res = 4 and 5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(AndLoOpExpr([NumberExpr(4), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_logic_or(self):
        ast = self.parser.srcToAST(r'res = 4 or 5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(OrLoOpExpr([NumberExpr(4), NumberExpr(5)]))])))
        self.assertAstEqual(exp, ast)

    def test_logic_not(self):
        ast = self.parser.srcToAST(r'res = not 5')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("res")), ExprsExpr(NotLoOpExpr(NumberExpr(5)))])))
        self.assertAstEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def test_concatenation(self):
        ast = self.parser.srcToAST(r'str = "begin".."end"')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("str")), ExprsExpr(ConcatExpr([StringExpr('begin'), StringExpr('end')]))])))
        self.assertAstEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.7 – The Length Operator                                             '''
    ''' ----------------------------------------------------------------------- '''
    def test_length_op(self):
        ast = self.parser.srcToAST(r'len = #t')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("len")), ExprsExpr(LengthExpr(IdExpr('t')))])))
        self.assertAstEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def test_dict(self):
        ast = self.parser.srcToAST(r'a = {foo = "bar", bar = "foo"}')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(TableExpr([
            KeysExpr([IdExpr("foo"), IdExpr("bar")]),
            ValuesExpr([StringExpr("bar"), StringExpr("foo")])
        ]))])))
        self.assertAstEqual(exp, ast)

    def test_nested_dict(self):
        ast = self.parser.srcToAST(textwrap.dedent(r'''
            foo = {
              car = {
                name = 'bmw'
              },
              options = { radio = true }
            };
            '''))
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(TableExpr([
            KeysExpr([IdExpr("car"),
                      IdExpr("options")]),
            ValuesExpr([
                TableExpr([KeysExpr(IdExpr('name')), ValuesExpr(StringExpr('bmw'))]),
                TableExpr([KeysExpr(IdExpr('radio')), ValuesExpr(TrueExpr())])
            ])
        ]))])))
        self.assertAstEqual(exp, ast)

    def test_array(self):
        ast = self.parser.srcToAST(textwrap.dedent(r'''
        foo = {
          1,    2,      4,
          8,    16,     32,
          64,   128,    256,
          512,  1024,   2048
        }
        '''))

        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(TableExpr([
            KeysExpr([
                NumberExpr(1),    NumberExpr(2),    NumberExpr(3),
                NumberExpr(4),    NumberExpr(5),    NumberExpr(6),
                NumberExpr(7),    NumberExpr(8),    NumberExpr(9),
                NumberExpr(10),   NumberExpr(11),   NumberExpr(12)
            ]),
            ValuesExpr([
                NumberExpr(1),    NumberExpr(2),    NumberExpr(4),
                NumberExpr(8),    NumberExpr(16),   NumberExpr(32),
                NumberExpr(64),   NumberExpr(128),  NumberExpr(256),
                NumberExpr(512),  NumberExpr(1024), NumberExpr(2048)
            ])
        ]))])))
        self.assertAstEqual(exp, ast)

    def test_mix_dict_array(self):
        ast = self.parser.srcToAST(textwrap.dedent(r'''
        foo = {
          options = { radio = true },
          "enabled",
          157
        };
        '''))

        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(TableExpr([
            KeysExpr([
                IdExpr('options'), NumberExpr(1), NumberExpr(2)
            ]),
            ValuesExpr([
                TableExpr([KeysExpr(IdExpr('radio')), ValuesExpr(TrueExpr())]),
                StringExpr('enabled'),
                NumberExpr(157)
            ])
        ]))])))
        self.assertAstEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.10 – Function Calls                                                 '''
    ''' ----------------------------------------------------------------------- '''
    ''' todo: maybe remove ExprsExpr'''
    def test_function_call(self):
        ast = self.parser.srcToAST(r'print("hello")')
        exp = Chunk(Block(CallStat([IdExpr("print"), ArgsExpr(ExprsExpr(StringExpr('hello')))])))
        self.assertAstEqual(exp, ast)

    def test_function_call_no_parent(self):
        ast = self.parser.srcToAST(r'print "hello"')
        exp = Chunk(Block(CallStat([IdExpr("print"), ArgsExpr(StringExpr('hello'))])))
        self.assertAstEqual(exp, ast)

    def test_function_call_sugar_syntax(self):
        ast = self.parser.srcToAST(r'foo:print("hello")')
        exp = Chunk(Block(InvokeStat([IdExpr("foo"), IdExpr("print"), ArgsExpr(ExprsExpr(StringExpr('hello')))])))
        self.assertAstEqual(exp, ast)

    def test_function_call_args(self):
        ast = self.parser.srcToAST(r'print("hello",  42)')
        exp = Chunk(Block(CallStat([IdExpr("print"), ArgsExpr(ExprsExpr([StringExpr('hello'), NumberExpr(42)]))])))
        self.assertAstEqual(exp, ast)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def test_function_definition(self):
        ast = self.parser.srcToAST(r'f = function() print("hello") end')
        exp = Chunk(Block(SetStat([
            VarsExpr(IdExpr('f')),
            ExprsExpr(FunctionExpr(Block(CallStat([IdExpr('print'), ArgsExpr(ExprsExpr(StringExpr('hello')))]))))
        ])))
        self.assertAstEqual(exp, ast)

    def test_function_definition_1(self):
        ast = self.parser.srcToAST(r'function f() end')
        exp = Chunk(Block(SetStat([IdExpr('f'),FunctionExpr(Block(None))])))
        self.assertAstEqual(exp, ast)

    def test_function_definition_2(self):
        ast = self.parser.srcToAST(r'function t.a.b.c.f() end')
        exp = Chunk(Block(SetStat([
            IndexExpr([
                IndexExpr([
                    IndexExpr([
                        IndexExpr([
                            IdExpr('t'), IdExpr('a')
                        ]), IdExpr('b')
                    ]), IdExpr('c')
                ]), IdExpr('f')
            ])
            ,FunctionExpr(Block(None))])))
        self.assertAstEqual(exp, ast)

    def test_function_definition_3(self):
        ast = self.parser.srcToAST(r't.a.b.c.f = function () end')
        exp = Chunk(Block(SetStat([
            VarsExpr(
                IndexExpr([
                    IndexExpr([
                        IndexExpr([
                            IndexExpr([
                                IdExpr('t'), IdExpr('a')
                            ]), IdExpr('b')
                        ]), IdExpr('c')
                    ]), IdExpr('f')
                ])
            )
            ,ExprsExpr(FunctionExpr(Block(None)))])))
        self.assertAstEqual(exp, ast)

    def test_function_definition_4(self):
        ast = self.parser.srcToAST(r'local function f () end')
        exp = Chunk(Block(LocalRecStat([IdExpr('f'), FunctionExpr(Block(None))])))
        self.assertAstEqual(exp, ast)
