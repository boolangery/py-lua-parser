from luaparser import tests
from luaparser import ast
from luaparser.astNodes import *
import textwrap


# https://www.lua.org/manual/5.3/manual.html#3.4

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
        # editor = self.parser.srcToProgramEditor(src)
        # print(editor.toStr())

