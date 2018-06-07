from luaparser.utils  import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:\t%(message)s')

class CommentsTestCase(tests.TestCase):
    def test_comment_before_local_assign(self):
        tree = ast.parse(textwrap.dedent("""
            -- rate limit
            -- an other comment
            --[==[ a long
            comment
            --]==]
            local rate_limit = 192
            """))
        exp = Chunk(Block([
            LocalAssign(
                [Name('rate_limit')],
                [Number(192)],
                [
                    Comment('-- rate limit'),
                    Comment('-- an other comment'),
                    Comment('--[==[ a long\ncomment\n--]==]', True)
                ]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_comment_before_global_assign(self):
        tree = ast.parse(textwrap.dedent("""
            -- rate limit
            rate_limit = 192
            """))
        print(ast.toPrettyStr(tree))
        exp = Chunk(Block([
            Assign(
                [Name('rate_limit')],
                [Number(192)],
                [Comment('-- rate limit')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_comment_before_method(self):
        tree = ast.parse(textwrap.dedent("""       
            --- description
            --- @tparam string arg a string
            function Class:print(arg)
            end
            """))
        print(ast.toPrettyStr(tree))
        exp = Chunk(Block([
            Method(
                source=Name('Class'),
                name=Name('print'),
                args=[Name('arg')],
                body=Block([]),
                comments=[Comment('--- description'), Comment('--- @tparam string arg a string')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_comment_in_table(self):
        tree = ast.parse(textwrap.dedent("""
            --- @table a table of constants
            local limits = {
              -- pre field 1
              HIGH = 127,    -- max rate limit
              -- pre field 2
              LOW  = 42,   -- min rate limit
              [true] = false, -- test
              "foo" -- just a value
              -- last
              ,toto -- toto value
              ,
              Model = true -- model
            }
            """))
        print(ast.toPrettyStr(tree))
        exp = Chunk(Block([
            LocalAssign(
                [Name('limits')],
                [Table([
                    Field(Name('HIGH'),  Number(127),   [Comment('-- pre field 1'), Comment('-- max rate limit')]),
                    Field(Name('LOW'),   Number(42),    [Comment('-- pre field 2'), Comment('-- min rate limit')]),
                    Field(TrueExpr(),    FalseExpr(),   [Comment('-- test')]),
                    Field(Number(1),     String('foo'), [Comment('-- just a value')]),
                    Field(Number(2),     Name('toto'), [Comment('-- last'), Comment('-- toto value')]),
                    Field(Name('Model'), TrueExpr(), [Comment('-- model')])
                ])],
                [Comment('--- @table a table of constants')]
            )
        ]))
        #print(ast.toPrettyStr(exp))
        self.assertEqual(exp, tree)


