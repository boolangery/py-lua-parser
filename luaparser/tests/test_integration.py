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
        tree = ast.parse(textwrap.dedent(r"x[a]"))
        exp = Chunk(
            Block(
                [Index(idx=Name("a"), value=Name("x"), notation=IndexNotation.SQUARE)]
            )
        )
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r"""x['a']"""))
        exp = Chunk(
            Block(
                [Index(idx=String("a"), value=Name("x"), notation=IndexNotation.SQUARE)]
            )
        )
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r"x.a"))
        exp = Chunk(Block([Index(idx=Name("a"), value=Name("x"))]))
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
                          LocalFunction: {} 4 keys
                            name: {} 2 keys
                              Name: {} 2 keys
                                id: 'sayHello'
                            args: [] 0 item
                            body: {} 2 keys
                              Block: {} 2 keys
                                body: [] 1 item
                                  0: {} 1 key                    
                                    Call: {} 3 keys
                                      func: {} 2 keys
                                        Name: {} 2 keys
                                          id: 'print'
                                      args: [] 1 item
                                        0: {} 1 key                          
                                          String: {} 3 keys
                                            s: 'hello world !'
                                            delimiter: SINGLE_QUOTE
                        1: {} 1 key          
                          Call: {} 3 keys
                            func: {} 2 keys
                              Name: {} 2 keys
                                id: 'sayHello'
                            args: [] 0 item"""
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
