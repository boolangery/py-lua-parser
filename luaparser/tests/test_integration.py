import textwrap

from luaparser import ast
from luaparser.astnodes import *
from luaparser.utils import tests


class IntegrationTestCase(tests.TestCase):
    maxDiff = None

    def test_cont_int_1(self):
        tree = ast.parse(
            textwrap.dedent(
                r"""
        describe("", function()
          it(function()
            do
              function foo()
              end
            end
          end)
          do
            function bar()
            end
          end
        end)
        """
            )
        )

        exp = Chunk(
            Block(
                [
                    Call(
                        Name("describe"),
                        [
                            String("", StringDelimiter.DOUBLE_QUOTE),
                            AnonymousFunction(
                                [],
                                Block(
                                    [
                                        Call(
                                            Name("it"),
                                            [
                                                AnonymousFunction(
                                                    [],
                                                    Block(
                                                        [
                                                            Do(
                                                                Block(
                                                                    [
                                                                        Function(
                                                                            Name("foo"),
                                                                            [],
                                                                            Block([]),
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                )
                                            ],
                                        ),
                                        Do(
                                            Block(
                                                [Function(Name("bar"), [], Block([]))]
                                            )
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    def test_cont_int_2(self):
        tree = ast.parse(
            textwrap.dedent(
                r"""
        if true then
          return true
        elseif isinstance() then
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
                        body=Block([Return([TrueExpr()])]),
                        orelse=ElseIf(
                            test=Call(Name("isinstance"), []),
                            body=Block([Return([TrueExpr()])]),
                            orelse=None,
                        ),
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    # Unable to tell apart true indexing vs. syntactic sugar indexing #1
    def test_cont_int_3(self):
        tree = ast.parse(textwrap.dedent(r"print(x[a])"))
        exp = Chunk(Block([Call(
            func=Name("print"),
            args=[Index(idx=Name("a"), value=Name("x"), notation=IndexNotation.SQUARE)],
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r"""print(x['a'])"""))
        exp = Chunk(Block([Call(
            func=Name("print"),
            args=[Index(idx=String("a"), value=Name("x"), notation=IndexNotation.SQUARE)],
        )]))
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r"print(x.a)"))
        exp = Chunk(Block([Call(
            func=Name("print"),
            args=[Index(idx=Name("a"), value=Name("x"))],
        )]))
        self.assertEqual(exp, tree)

    # luaparser.utils.visitor.VisitorException: No visitor found for class <enum 'StringDelimiter'>
    # #11
    # #14
    def test_cont_int_4(self):
        tree = ast.parse(
            textwrap.dedent(
                r"""
        local function sayHello()
            print('hello world !')
        end
        sayHello()
        """
            )
        )
        pretty_str = ast.to_pretty_str(tree)
        exp = textwrap.dedent(
            r"""
                Chunk: {} 2 keys
                  body: {} 2 keys
                    Block: {} 2 keys
                      body: [] 2 items
                        0: {} 1 key          
                          LocalFunction: {} 5 keys
                            wrapped: False
                            name: {} 4 keys
                              Name: {} 4 keys
                                wrapped: False
                                id: 'sayHello'
                            args: [] 0 item
                            body: {} 2 keys
                              Block: {} 2 keys
                                body: [] 1 item
                                  0: {} 1 key                    
                                    Call: {} 5 keys
                                      wrapped: False
                                      func: {} 4 keys
                                        Name: {} 4 keys
                                          wrapped: False
                                          id: 'print'
                                      args: [] 1 item
                                        0: {} 1 key                          
                                          String: {} 4 keys
                                            wrapped: False
                                            s: 'hello world !'
                                            delimiter: SINGLE_QUOTE
                                      style: DEFAULT
                        1: {} 1 key          
                          Call: {} 5 keys
                            wrapped: False
                            func: {} 4 keys
                              Name: {} 4 keys
                                wrapped: False
                                id: 'sayHello'
                            args: [] 0 item
                            style: DEFAULT"""
        )
        self.assertEqual(exp, pretty_str)
        ast.to_xml_str(tree)

    # Cant walk the ast tree if lua file has semicolon(;) or repeat until loop and multiple args(...) #9
    def test_cont_int_5(self):
        tree = ast.parse(
            textwrap.dedent(
                """
                    function table.pack(...)
                        repeat
                           print("value of a:", a)
                           a = a + 1;
                        until( a > 15 )
                    end
                """
            )
        )
        nodes = ast.walk(tree)
        expected_cls = [
            Chunk,
            Block,
            Function,
            Index,
            Name,
            Name,
            Varargs,
            Block,
            Repeat,
            Block,
            Call,
            Name,
            String,
            Name,
            Assign,
            Name,
            AddOp,
            Name,
            Number,
            SemiColon,
            GreaterThanOp,
            Name,
            Number,
        ]
        for node, exp in zip(nodes, expected_cls):
            self.assertIsInstance(node, exp)

    # Comments are ignored if they are written after the last line of a table ending with a comma #15
    def test_cont_int_6(self):
        tree = ast.parse(
            textwrap.dedent(
                """
            foo = {
                mykey = "myvalue",
                -- this comment is ignored if previous line ends with a comma
            }
            """
            )
        )
        exp = Chunk(
            Block(
                [
                    Assign(
                        [Name("foo")],
                        [
                            Table(
                                [
                                    Field(
                                        Name("mykey"),
                                        String(
                                            "myvalue",
                                            delimiter=StringDelimiter.DOUBLE_QUOTE,
                                        ),
                                        comments=[
                                            Comment(
                                                "-- this comment is ignored if previous line ends with a comma"
                                            )
                                        ],
                                    ),
                                ]
                            )
                        ],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    # Bitwise precedence is wrong #33
    def test_cont_int_7(self):
        tree = ast.parse(r"a = 1&2+3")
        exp = Chunk(
            Block(
                [
                    Assign(
                        targets=[Name("a")],
                        values=[BAndOp(left=Number(1), right=AddOp(left=Number(2), right=Number(3)))],
                    )
                ]
            )
        )
        self.assertEqual(exp, tree)

    # Brackets are absent in output of AST->source_code conversion #57
    def test_cont_int_8(self):
        source = r"result = (a + b) / (c + d)"
        self.assertEqual(source, ast.to_lua_source(ast.parse(source)))

    # Failure to parse chained comparisons #56
    def test_cont_int_9(self):
        tree = ast.parse(textwrap.dedent("""
            if false == false == false then 
                x = 2
            end
        """))
        exp = Chunk(
            Block([
                If(
                    test=EqToOp(left=EqToOp(left=FalseExpr(), right=FalseExpr()), right=FalseExpr()),
                    body=Block([
                        Assign([Name("x")], [Number(2)])
                    ]),
                    orelse=None,
                )
            ])
        )
        self.assertEqual(exp, tree)

    # ULengthOp not correctly parsed #54
    def test_cont_int_10(self):
        tree = ast.parse(textwrap.dedent("""
            if #setting >10 and setting_name == "user" then return 100 end
        """))
        exp = Chunk(
            Block([
                If(
                    test=AndLoOp(left=GreaterThanOp(left=ULengthOP(Name("setting")), right=Number(10)),
                                 right=EqToOp(left=Name("setting_name"),
                                              right=String("user", StringDelimiter.DOUBLE_QUOTE))),
                    body=Block([
                        Return([Number(100)])
                    ]),
                    orelse=None,
                )
            ])
        )
        self.assertEqual(exp, tree)

    # Strings are not being parsed #43
    def test_cont_int_12(self):
        tree = ast.parse(textwrap.dedent("""
            a='\\0\\n\\ta'
        """))
        exp = Chunk(
            Block([
                Assign([Name("a")], [String("\x00\n\ta", StringDelimiter.SINGLE_QUOTE)])
            ])
        )
        self.assertEqual(exp, tree)

    # Comments with Chinese characters are discarded #39
    def test_cont_int_13(self):
        tree = ast.parse(textwrap.dedent("""
               function setupRichText()
                    richText.fitArea = false	    -- 是否根据内容自适应高度
                    richText.fitPerHeight = nil     -- 自适应的单行高度
                    return richText
                end
        """))
        exp = Chunk(
            Block([
                Function(
                    name=Name("setupRichText"),
                    args=[],
                    body=Block([
                        Assign([Index(Name("fitArea"), Name("richText"))], [FalseExpr()], comments=[
                            Comment('-- 是否根据内容自适应高度')
                        ]),
                        Assign([Index(Name("fitPerHeight"), Name("richText"))], [Nil()], comments=[
                            Comment('-- 自适应的单行高度')
                        ]),
                        Return([Name("richText")])
                    ])
                )
            ])
        )
        self.assertEqual(exp, tree)
