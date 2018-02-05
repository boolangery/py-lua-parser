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
    def test_token_editor_next_no_ignore(self):
        editor = asttokens.parse(r"""local a = 1""")
        first = editor.first()

        self.assertEqual('local', first.text)
        self.assertEqual(' ', first.next([]).text)
        self.assertEqual('a', first.next([]).next([]).text)
        self.assertEqual(' ', first.next([]).next([]).next([]).text)
        self.assertEqual('=', first.next([]).next([]).next([]).next([]).text)
        self.assertEqual(' ', first.next([]).next([]).next([]).next([]).next([]).text)
        self.assertEqual('1', first.next([]).next([]).next([]).next([]).next([]).next([]).text)

    def test_token_editor_next_ignore(self):
        editor = asttokens.parse(r"""local a = 1""")
        first = editor.first()

        self.assertEqual('local', first.text)
        self.assertEqual('a', first.next().text)
        self.assertEqual('=', first.next().next().text)
        self.assertEqual('1', first.next().next().next().text)

        self.assertEqual('local', first.text)
        self.assertEqual('=', first.next([asttokens.Tokens.SPACE, asttokens.Tokens.NAME]).text)

    def test_token_editor_prev_no_ignore(self):
        editor = asttokens.parse(r"""local a = 1""")
        last = editor.last()

        self.assertEqual('<EOF>', last.text)
        self.assertEqual('1',     last.prev([]).text)
        self.assertEqual(' ',     last.prev([]).prev([]).text)
        self.assertEqual('=',     last.prev([]).prev([]).prev([]).text)
        self.assertEqual(' ',     last.prev([]).prev([]).prev([]).prev([]).text)
        self.assertEqual('a',     last.prev([]).prev([]).prev([]).prev([]).prev([]).text)
        self.assertEqual(' ',     last.prev([]).prev([]).prev([]).prev([]).prev([]).prev([]).text)
        self.assertEqual('local', last.prev([]).prev([]).prev([]).prev([]).prev([]).prev([]).prev([]).text)

    def test_token_editor_prev_ignore(self):
        editor = asttokens.parse(r"""local a = 1""")
        last = editor.last()

        self.assertEqual('<EOF>', last.text)
        self.assertEqual('1',     last.prev().text)
        self.assertEqual('=',     last.prev().prev().text)
        self.assertEqual('a',     last.prev().prev().prev().text)
        self.assertEqual('local', last.prev().prev().prev().prev().text)
        self.assertEqual(None,    last.prev().prev().prev().prev().prev())

    def test_group_editor_line_count(self):
        src = textwrap.dedent(r"""local 
            a
            = 
            1""")

        atokens = asttokens.parse(src)
        self.assertEqual(4, atokens.lineCount())

    def test_group_editor_lines(self):
        src = textwrap.dedent(r"""
            local foo = "s"
            local bar = "a"
            local res = foo .. bar""")
        atokens = asttokens.parse(src)

        # test yield
        count = 0
        for line in atokens.lines():
            count += 1
        self.assertEqual(4, count)

        # test content
        lines = list(atokens.lines()) # lines yield

        self.assertEqual('local foo = "s"\n', lines[1].toSource())
        self.assertEqual('local bar = "a"\n', lines[2].toSource())
        self.assertEqual('local res = foo .. bar', lines[3].toSource())

    def test_group_editor_types(self):
        src = textwrap.dedent(r"""
            -- comment 1
            local foo = "s"
            -- comment 2
            local bar = "a"
            """)
        atokens = asttokens.parse(src)

        count = 0
        for token in atokens.types(asttokens.Tokens.LOCAL):
            count += 1
        self.assertEqual(2, count)

        count = 0
        for token in atokens.types([asttokens.Tokens.LOCAL, asttokens.Tokens.LINE_COMMENT]):
            count += 1
        self.assertEqual(4, count)

    def test_group_editor_first(self):
        atokens = asttokens.parse(r"""local foo = 42""")
        self.assertEqual(atokens[0], atokens.first())
        self.assertEqual('local', atokens.first().text)

        # empty
        atokens = asttokens.parse(r"""""")
        self.assertEqual(atokens[0], atokens.first())

    def test_group_editor_last(self):
        atokens = asttokens.parse(r"""local foo = 42""")
        self.assertEqual(atokens[7], atokens.last())
        self.assertEqual('<EOF>', atokens.last().text)

        # empty
        atokens = asttokens.parse(r"""""")
        self.assertEqual(atokens[0], atokens.last())

    def test_program_edior_range(self):
        src = textwrap.dedent(r"""
            local foo = "s"
            local bar = "a"
            local res = foo .. bar""")
        atokens = asttokens.parse(src)

        rangetok = atokens.range(0, 2)
        self.assertEqual(3, len(rangetok))

        self.assertEqual('\n', rangetok[0].text)
        self.assertEqual('local', rangetok[1].text)
        self.assertEqual(' ', rangetok[2].text)


    def test_line_editor_lstrip(self):
        atokens = asttokens.parse(r"""   local foo = "s"; """)
        lines = list(atokens.lines())

        self.assertEqual('   local foo = "s"; ', lines[0].toSource())
        self.assertEqual('local foo = "s"; ', lines[0].lstrip().toSource())

        self.assertEqual('foo = "s"; ', lines[0].lstrip([
            asttokens.Tokens.SPACE,
            asttokens.Tokens.LOCAL]).toSource())

    def test_line_editor_rstrip(self):
        atokens = asttokens.parse(r"""local foo = "s";   
        """)
        lines = list(atokens.lines())

        self.assertEqual('local foo = "s";\n', lines[0].rstrip().toSource())


    def test_line_editor_indent(self):
        atokens = asttokens.parse(r"""local foo = "s"; """)
        lines = list(atokens.lines())

        lines[0].indent(2)

        self.assertEqual(r"""  local foo = "s"; """, atokens.allToSource())
        self.assertEqual(r"""  local foo = "s"; """, lines[0].toSource())

    def test_line_editor_indent_2(self):
        atokens = asttokens.parse(r"""  local foo = "s"; """)
        lines = list(atokens.lines())

        lines[0].indent(2)

        self.assertEqual(r"""  local foo = "s"; """, atokens.allToSource())
        self.assertEqual(r"""  local foo = "s"; """, lines[0].toSource())
