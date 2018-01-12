from luaparser.utils  import tests
from luaparser import asttokens
from luaparser.astnodes import *
import textwrap

class AstTokensTestCase(tests.TestCase):
    def test_line_editor_line(self):
        src = textwrap.dedent("""
            local 
            a
            = 
            1""")

        atokens = asttokens.parse(src)
        tokens = atokens.lines()

        self.assertEqual(5, len(tokens))
        self.assertEqual(0, len(tokens[0]))
        self.assertEqual(1, len(tokens[1]))
        self.assertEqual(1, len(tokens[2]))
        self.assertEqual(1, len(tokens[3]))
        self.assertEqual(2, len(tokens[4]))

    def test_to_source(self):
        src = textwrap.dedent("""local a = 1""")
        atokens = asttokens.parse(src)
        self.assertEqual(src, atokens.toSource())

    def test_line_editor_stripl(self):
        src = """   local a = 1"""

        atokens = asttokens.parse(src)
        for tokens in atokens.lines():
            tokens.stripl()

        self.assertEqual(src.strip(), atokens.toSource())

    def test_editor_set_text(self):
        src = """local a = 1"""

        atokens = asttokens.parse(src)
        for token in atokens.types(asttokens.Tokens.NAME):
            print(token)
            token.text = 'foo'

        print(atokens.toSource())
        self.assertEqual(src.strip(), atokens.toSource())