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
        #print(Printer.toStr(ast))
        self.assertAstEqual(exp, ast)