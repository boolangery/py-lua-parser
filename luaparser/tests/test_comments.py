from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:\t%(message)s")


class CommentsTestCase(tests.TestCase):
    def test_comment_before_local_assign(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            -- rate limit
            -- an other comment
            --[==[ a long
            comment
            --]==]
            local rate_limit = 192
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    LocalAssign(
                        [Name("rate_limit")],
                        [Number(192)],
                        comments=[
                            Comment("-- rate limit"),
                            Comment("-- an other comment"),
                            Comment("--[==[ a long\ncomment\n--]==]", True),
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_comment_before_global_assign(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            -- rate limit
            rate_limit = 192
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        [Name("rate_limit")],
                        [Number(192)],
                        comments=[Comment("-- rate limit")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_comment_before_method(self):
        tree = ast.parse(
            textwrap.dedent(
                """       
            --- description
            --- @tparam string arg a string
            function Class:print(arg)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Method(
                        source=Name("Class"),
                        name=Name("print"),
                        args=[Name("arg")],
                        body=Block([]),
                        comments=[
                            Comment("--- description"),
                            Comment("--- @tparam string arg a string"),
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_comment_in_table(self):
        tree = ast.parse(
            textwrap.dedent(
                """
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
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    LocalAssign(
                        [Name("limits")],
                        [
                            Table(
                                [
                                    Field(
                                        Name("HIGH"),
                                        Number(127),
                                        comments=[
                                            Comment("-- pre field 1"),
                                            Comment("-- max rate limit"),
                                        ],
                                    ),
                                    Field(
                                        Name("LOW"),
                                        Number(42),
                                        comments=[
                                            Comment("-- pre field 2"),
                                            Comment("-- min rate limit"),
                                        ],
                                    ),
                                    Field(
                                        TrueExpr(),
                                        FalseExpr(),
                                        comments=[Comment("-- test")],
                                        between_brackets=True,
                                    ),
                                    Field(
                                        None,
                                        String(b"foo", "foo", StringDelimiter.DOUBLE_QUOTE),
                                        comments=[Comment("-- just a value")],
                                    ),
                                    Field(
                                        None,
                                        Name("toto"),
                                        comments=[
                                            Comment("-- last"),
                                            Comment("-- toto value"),
                                        ],
                                    ),
                                    Field(
                                        Name("Model"),
                                        TrueExpr(),
                                        comments=[Comment("-- model")],
                                    ),
                                ]
                            )
                        ],
                        comments=[Comment("--- @table a table of constants")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_comment_in_table_2(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            --- @module utils

            return {
                --- @export
                BAR = 4,
                --- test
                FOO = 5
            }
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Return(
                        values=[
                            Table(
                                [
                                    Field(
                                        Name("BAR"),
                                        Number(4),
                                        comments=[Comment("--- @export")],
                                    ),
                                    Field(
                                        Name("FOO"),
                                        Number(5),
                                        comments=[Comment("--- test")],
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            ),
            comments=[Comment("--- @module utils")],
        )
        self.assertEqual(exp, tree)

    def test_comment_chunk_tail(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            local x = 1
            -- comments should be visited
            """
            )
        )
        exp = Chunk(
            Block(
                [LocalAssign(targets=[Name("x")], values=[Number(n=1)])],
            ),
            comments=[Comment("-- comments should be visited")]
        )
        self.assertEqual(exp, tree)

    def test_comment_function_tail(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            function ok()
              -- comments should be visited
            end
            -- another comment
            """
            )
        )
        exp = Chunk(
            Block([
                Function(
                    name=Name("ok"),
                    args=[],
                    body=Block([], comments=[Comment("-- comments should be visited")])
                )
            ]),
            comments=[Comment("-- another comment")]
        )
        self.assertEqual(exp, tree)

    def test_comment_before_end_of_for_loop(self):
        # Regression test for https://github.com/boolangery/py-lua-parser/issues/81
        # Standalone comments right before the closing "end" of a for-loop body
        # used to be silently dropped.
        tree = ast.parse(
            textwrap.dedent(
                """
            for i=1,2 do
              p=i
              -- 4
              -- 5
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Fornum(
                        target=Name("i"),
                        start=Number(1),
                        stop=Number(2),
                        step=1,
                        body=Block(
                            [Assign([Name("p")], [Name("i")])],
                            comments=[Comment("-- 4"), Comment("-- 5")],
                        ),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_just_comment(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            -- just a comment
            """
            )
        )
        exp = Chunk(Block([], comments=[Comment("-- just a comment")]))
        self.assertEqual(exp, tree)
