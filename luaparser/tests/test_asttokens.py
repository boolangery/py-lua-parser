from luaparser.utils  import tests
from luaparser import ast
from luaparser import asttokens
from luaparser.astnodes import *
import textwrap

src_1 = """
Account = {}
Account.__index = Account

function Account:create(balance)
   local acnt = {}             -- our new object
   setmetatable(acnt,Account)  -- make Account handle lookup
   acnt.balance = balance      -- initialize our object
   return acnt
end

function Account:withdraw(amount)
   self.balance = self.balance - amount
end

-- create and use an Account
acc = Account:create(1000)
acc:withdraw(100)
"""

class AstTokensTestCase(tests.TestCase):
    def test_line_editor_line(self):
        src = textwrap.dedent("""
            local 
            a
            = 
            1""")

        atokens = asttokens.parse(src)
        tokens = atokens.lines()

        self.assertEqual(4, len(tokens))
        self.assertEqual(1, len(tokens[0]))
        self.assertEqual(1, len(tokens[1]))
        self.assertEqual(1, len(tokens[2]))
        self.assertEqual(2, len(tokens[3]))

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
        exp = """local foo = 1"""

        atokens = asttokens.parse(src)
        for token in atokens.types(asttokens.Tokens.NAME):
            token.text = 'foo'

        self.assertEqual(exp, atokens.toSource())

    def test_editor_indent(self):
        src = """local a = 1"""
        exp = """  local a = 1"""

        atokens = asttokens.parse(src)
        for tokens in atokens.lines():
            tokens.indent(2)

        self.assertEqual(exp, atokens.toSource())

    def test_editor_from_ast(self):
        src = textwrap.dedent("""
            local a = 1
            local b, c = '11'""")
        exp= textwrap.dedent("""
            local _a = 1
            local _b, _c = '11'""")

        tree = ast.parse(src)
        atokens = asttokens.parse(src)

        for node in ast.walk(tree):
            if isinstance(node, LocalAssign):
                tokens = atokens.fromAST(node)
                for name in tokens.types(asttokens.Tokens.NAME):
                    name.text = '_' + name.text

        self.assertEqual(exp, atokens.toSource())

    def test_editor_render_source(self):
        atokens = asttokens.parse(src_1)

        self.assertEqual(src_1, atokens.toSource())