from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


class TypesValuesTestCase(tests.TestCase):
    def test_nil(self):
        tree = ast.parse(r'foo = nil')
        exp = Chunk(Block([Assign(
            targets=[
                Name('foo')
            ],
            values=[
                Nil()
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_true(self):
        tree = ast.parse(r'foo = true')
        exp = Chunk(Block([Assign(
            targets=[
                Name('foo')
            ],
            values=[
                TrueExpr()
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_false(self):
        tree = ast.parse(r'foo = false')
        exp = Chunk(Block([Assign(
            targets=[
                Name('foo')
            ],
            values=[
                FalseExpr()
            ]
        )]))
        self.assertEqual(exp, tree)

    def test_numbers(self):
        tree = ast.parse(r'foo = 04')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=4)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 0.4')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=0.4)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 4.57e-3')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=4.57e-3)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 0.3e12')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=0.3e12)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 5e+20')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=5e+20)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 0.31416E1')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=0.31416E1)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(r'foo = 0xff')
        exp = Chunk(Block([Assign(
            targets=[Name('foo')],
            values=[Number(n=0xff)]
        )]))
        self.assertEqual(exp, tree)

    def test_string_dbl_quote(self):
        tree = ast.parse(r'a = "a line"')
        exp = Chunk(Block([Assign(
            targets=[Name('a')],
            values=[String('a line', StringDelimiter.DOUBLE_QUOTE)]
        )]))
        self.assertEqual(exp, tree)

    def test_string_quote(self):
        tree = ast.parse(r"b = 'another line'")
        exp = Chunk(Block([Assign(
            targets=[Name('b')],
            values=[String('another line')]
        )]))
        self.assertEqual(exp, tree)

    def test_string_escape(self):
        tree = ast.parse(r'''b = "one line\nnext line\n\"in quotes\", 'in quotes'"''')
        exp = Chunk(Block([Assign(
            targets=[Name('b')],
            values=[String(r"one line\nnext line\n\"in quotes\", 'in quotes'", StringDelimiter.DOUBLE_QUOTE)]
        )]))
        self.assertEqual(exp, tree)

    def test_string_dbl_square(self):
        tree = ast.parse(r'b = [[hello]]')
        exp = Chunk(Block([Assign(
            targets=[Name('b')],
            values=[String('hello', StringDelimiter.DOUBLE_SQUARE)]
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r'''
            b = [[Multiple lines of text
            can be enclosed in double square
            brackets.]]
            '''))
        exp = Chunk(Block([Assign(
            targets=[Name('b')],
            values=[String('Multiple lines of text\ncan be enclosed in double square\nbrackets.', StringDelimiter.DOUBLE_SQUARE)]
        )]))
        self.assertEqual(exp, tree)

    def test_string_dbl_square_equal(self):
        tree = ast.parse(r'b = [=[one [[two]] one]=]')
        exp = Chunk(Block([Assign(
            targets=[Name('b')],
            values=[String('one [[two]] one')]
        )]))
        self.assertEqual(exp, tree)
