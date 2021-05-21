from luaparser.tests.comparators import node_compare_without_char
from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


# https://www.lua.org/manual/5.3/manual.html#3.4

class ExpressionsTestCase(tests.TestCase):
    """ Test node start_char, stop_char and start_line
    """

    def test_char_1(self):
        tree = ast.parse(r'a = 1 + 0.2')
        exp = Chunk(
            Block([Assign(
                targets=[Name('a', start_char=0, stop_char=0, start_line=1)],
                values=[
                    AddOp(
                        left=Number(1, start_char=4, stop_char=4, start_line=1),
                        right=Number(0.2, start_char=8, stop_char=10, start_line=1),
                        start_char=4, stop_char=10, start_line=1
                    )
                ],
                start_char=0, stop_char=10, start_line=1
            )], start_char=0, stop_char=10, start_line=1),
            start_char=0, stop_char=10, start_line=1
        )
        self.assertEqual(exp, tree)
