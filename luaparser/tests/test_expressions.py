from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class ArithmeticOperatorsTestCase(tests.TestCase):
    """
    3.1 – Arithmetic Operators
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

    def test_division(self):
        ast = self.parser.srcToAST(r'a = 1 / 0.2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(FloatDivOpExpr([NumberExpr(1), NumberExpr(0.2)]))])))
        self.assertAstEqual(exp, ast)

    def test_negation(self):
        ast = self.parser.srcToAST(r'a = -1')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(UnOpNegExpr(NumberExpr(1)))])))
        self.assertAstEqual(exp, ast)

    def test_exponentiation(self):
        ast = self.parser.srcToAST(r'a = 1^2')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(ExpoOpExpr([NumberExpr(1), NumberExpr(2)]))])))
        self.assertAstEqual(exp, ast)


class ArithmeticOperatorsTestCase(tests.TestCase):
    """
    3.2 – Relational Operators
    """
    def setUp(self):
        self.parser = Parser()

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