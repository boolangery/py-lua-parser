from luaparser.utils import tests
from luaparser import ast
from luaparser.astnodes import *
from luaparser.builder import SyntaxException
import textwrap


class StatementsTestCase(tests.TestCase):
    """
    3.3.1 – Blocks
    """

    def test_empty_block(self):
        tree = ast.parse(";;;;")
        exp = Chunk(Block([SemiColon(), SemiColon(), SemiColon(), SemiColon()]))
        self.assertEqual(exp, tree)

    def test_2_block(self):
        tree = ast.parse("local a;local b;")
        exp = Chunk(
            Block(
                [
                    LocalAssign(targets=[Name("a")], values=[]),
                    SemiColon(),
                    LocalAssign(targets=[Name("b")], values=[]),
                    SemiColon(),
                ]
            )
        )
        self.assertEqual(exp, tree)

        """
    3.3.3 – Assignment
    """

    def test_set_number(self):
        tree = ast.parse("i=3")
        exp = Chunk(Block([Assign(targets=[Name("i")], values=[Number(3)])]))
        self.assertEqual(exp, tree)

    def test_set_string(self):
        tree = ast.parse('i="foo bar"')
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("i")],
                        values=[String("foo bar", StringDelimiter.DOUBLE_QUOTE)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_set_array_index(self):
        tree = ast.parse("a[i] = 42")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[
                            Index(
                                idx=Name("i"),
                                value=Name("a"),
                                notation=IndexNotation.SQUARE,
                            )
                        ],
                        values=[Number(42)],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_set_table_index(self):
        tree = ast.parse("_ENV.x = val")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Index(idx=Name("x"), value=Name("_ENV"))],
                        values=[Name("val")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_set_multi(self):
        tree = ast.parse("x, y = y, x")

        exp = Chunk(
            Block(
                [Assign(targets=[Name("x"), Name("y")], values=[Name("y"), Name("x")])]
            )
        )
        self.assertEqual(exp, tree)

    """
    3.3.4 – Control Structures
    """

    def test_for_in_1(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for k, v in pairs({}) do
              print(k, v)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Forin(
                        Block([Call(func=Name("print"), args=[Name("k"), Name("v")])]),
                        iter=[Call(func=Name("pairs"), args=[Table([])])],
                        targets=[Name("k"), Name("v")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_for_in_2(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for k, v in foo.pairs({}) do
              print(k, v)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Forin(
                        Block([Call(func=Name("print"), args=[Name("k"), Name("v")])]),
                        iter=[
                            Call(
                                func=Index(Name("pairs"), Name("foo")), args=[Table([])]
                            )
                        ],
                        targets=[Name("k"), Name("v")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_for_in_3(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for k, v in foo:pairs({}) do
              print(k, v)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Forin(
                        Block([Call(func=Name("print"), args=[Name("k"), Name("v")])]),
                        iter=[
                            Invoke(
                                source=Name("foo"), func=Name("pairs"), args=[Table([])]
                            )
                        ],
                        targets=[Name("k"), Name("v")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_for_in_4(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for k, v in bar.foo:pairs({}) do
              print(k, v)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Forin(
                        body=Block(
                            [Call(func=Name("print"), args=[Name("k"), Name("v")])]
                        ),
                        iter=[
                            Invoke(
                                source=Index(Name("foo"), Name("bar")),
                                func=Name("pairs"),
                                args=[Table([])],
                            )
                        ],
                        targets=[Name("k"), Name("v")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_for_in_5(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for k, v in bar:foo(42):pairs({}) do
              print(k, v)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Forin(
                        body=Block(
                            [Call(func=Name("print"), args=[Name("k"), Name("v")])]
                        ),
                        iter=[
                            Invoke(
                                source=Invoke(
                                    source=Name("bar"),
                                    func=Name("foo"),
                                    args=[Number(42)],
                                ),
                                func=Name("pairs"),
                                args=[Table([])],
                            )
                        ],
                        targets=[Name("k"), Name("v")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_for_in_6(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for k, v in bar:foo(42).pairs({}) do
              print(k, v)
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Forin(
                        body=Block(
                            [Call(func=Name("print"), args=[Name("k"), Name("v")])]
                        ),
                        iter=[
                            Call(
                                func=Index(
                                    idx=Name("pairs"),
                                    value=Invoke(
                                        source=Name("bar"),
                                        func=Name("foo"),
                                        args=[Number(42)],
                                    ),
                                ),
                                args=[Table([])],
                            )
                        ],
                        targets=[Name("k"), Name("v")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_numeric_for(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            for i=1,10,2 do print(i) end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Fornum(
                        target=Name("i"),
                        start=Number(1),
                        stop=Number(10),
                        step=Number(2),
                        body=Block([Call(func=Name("print"), args=[Name("i")])]),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_do_end(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            do
              local foo = 'bar'
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Do(
                        body=Block(
                            [LocalAssign(targets=[Name("foo")], values=[String("bar")])]
                        )
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_while(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            while true do
              print('hello world')
            end"""
            )
        )
        exp = Chunk(
            Block(
                [
                    While(
                        test=TrueExpr(),
                        body=Block(
                            [Call(func=Name("print"), args=[String("hello world")])]
                        ),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_repeat_until(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            repeat        
            until true
            """
            )
        )
        exp = Chunk(Block([Repeat(body=Block([]), test=TrueExpr())]))
        self.assertEqual(exp, tree)

    def test_if(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            if true then    
            end
            """
            )
        )

        exp = Chunk(Block([If(test=TrueExpr(), body=Block([]), orelse=None)]))
        self.assertEqual(exp, tree)

    def test_if_exp(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            if (a<2) then    
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    If(
                        test=LessThanOp(left=Name("a"), right=Number(2)),
                        body=Block([]),
                        orelse=None,
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_if_elseif(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            if true then 
            elseif false then     
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    If(
                        test=TrueExpr(),
                        body=Block([]),
                        orelse=ElseIf(test=FalseExpr(), body=Block([]), orelse=None),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_if_elseif_else(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            if true then 
            elseif false then  
            else   
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    If(
                        test=TrueExpr(),
                        body=Block([]),
                        orelse=ElseIf(
                            test=FalseExpr(), body=Block([]), orelse=Block([])
                        ),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_if_elseif_elseif_else(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            if true then
            elseif false then
            elseif 42 then
            else
              return true
            end
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    If(
                        test=TrueExpr(),
                        body=Block([]),
                        orelse=ElseIf(
                            test=FalseExpr(),
                            body=Block([]),
                            orelse=ElseIf(
                                test=Number(42),
                                body=Block([]),
                                orelse=Block([Return([TrueExpr()])]),
                            ),
                        ),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_label(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            ::foo::
            """
            )
        )
        exp = Chunk(Block([Label(Name("foo"))]))
        self.assertEqual(exp, tree)

    def test_goto(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            goto foo
            ::foo::
            """
            )
        )
        exp = Chunk(Block([Goto(label=Name("foo")), Label(Name("foo"))]))
        self.assertEqual(exp, tree)

    def test_break(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            break
            """
            )
        )
        exp = Chunk(Block([Break()]))
        self.assertEqual(exp, tree)

    def test_return(self):
        tree = ast.parse(r"return nil")
        exp = Chunk(Block([Return([Nil()])]))
        self.assertEqual(exp, tree)

    def test_return_multiple(self):
        tree = ast.parse(r'return nil, "error", 42; ')
        exp = Chunk(
            Block(
                [
                    Return(
                        [
                            Nil(),
                            String("error", StringDelimiter.DOUBLE_QUOTE),
                            Number(42),
                        ]
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_ambiguous_syntax(self):
        src = textwrap.dedent(
            """
            local a = b
            (print)('foo')
            """
        )
        self.assertRaises(SyntaxException, ast.parse, src)

    def test_index(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            foo.bar = 'bar'
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Index(idx=Name("bar"), value=Name("foo"))],
                        values=[String("bar")],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)
