from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


class TypesValuesTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_nil(self):
        ast = self.parser.srcToAST(r'foo = nil')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NilExpr([]))])))
        self.assertAstEqual(exp, ast)

    def test_true(self):
        ast = self.parser.srcToAST(r'foo = true')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(TrueExpr([]))])))
        self.assertAstEqual(exp, ast)

    def test_false(self):
        ast = self.parser.srcToAST(r'foo = false')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(FalseExpr([]))])))
        self.assertAstEqual(exp, ast)

    def test_numbers(self):
        ast = self.parser.srcToAST(r'foo = 4')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr(4))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 0.4')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr(0.4))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 4.57e-3')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr(4.57e-3))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 0.3e12')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr(0.3e12))])))
        self.assertAstEqual(exp, ast)
        ast = self.parser.srcToAST(r'foo = 5e+20')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("foo")), ExprsExpr(NumberExpr(5e+20))])))
        self.assertAstEqual(exp, ast)

    def test_string_dbl_quote(self):
        ast = self.parser.srcToAST(r'a = "a line"')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("a")), ExprsExpr(StringExpr('a line'))])))
        self.assertAstEqual(exp, ast)

    def test_string_quote(self):
        ast = self.parser.srcToAST(r"b = 'another line'")
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("b")), ExprsExpr(StringExpr('another line'))])))
        self.assertAstEqual(exp, ast)

    def test_string_escape(self):
        ast = self.parser.srcToAST(r'''b = "one line\nnext line\n\"in quotes\", 'in quotes'"''')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("b")), ExprsExpr(StringExpr(r"one line\nnext line\n\"in quotes\", 'in quotes'"))])))
        self.assertAstEqual(exp, ast)

    def test_string_dbl_square(self):
        ast = self.parser.srcToAST(r'b = [[hello]]')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("b")), ExprsExpr(StringExpr(r"hello"))])))
        self.assertAstEqual(exp, ast)

        ast = self.parser.srcToAST(textwrap.dedent(r'''
            b = [[Multiple lines of text
            can be enclosed in double square
            brackets.]]
            '''))
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("b")), ExprsExpr(StringExpr("Multiple lines of text\ncan be enclosed in double square\nbrackets."))])))
        self.assertAstEqual(exp, ast)

    def test_string_dbl_square_equal(self):
        ast = self.parser.srcToAST(r'b = [=[one [[two]] one]=]')
        exp = Chunk(Block(SetStat([VarsExpr(IdExpr("b")), ExprsExpr(StringExpr(r"one [[two]] one"))])))
        self.assertAstEqual(exp, ast)

    def test_dict(self):
        # https://www.lua.org/pil/2.5.html
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