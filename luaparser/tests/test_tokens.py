from luaparser import tests
from luaparser import ast
from luaparser import asttokens
from luaparser.astNodes import *
import textwrap


class TokensTestCase(tests.TestCase):
    def test_tokenEditor(self):
        src = textwrap.dedent("""
            local a = 1; local b = 2;
            if true then 
              local str = 'hello world'
            elseif false then     
              local str = 'error'
            end
            """)
        tree = ast.parse(src)
        tokens = asttokens.parse(src)
        # editor = self.parser.srcToProgramEditor(src)
        # print(editor.toStr())

