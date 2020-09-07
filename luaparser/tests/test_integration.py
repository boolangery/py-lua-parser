from luaparser.utils  import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


class IntegrationTestCase(tests.TestCase):
    def test_cont_int_1(self):
        tree = ast.parse(textwrap.dedent(r'''
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
        '''))

        exp = Chunk(Block([
            Call(Name('describe'), [
                String('', StringDelimiter.DOUBLE_QUOTE),
                AnonymousFunction([], Block([
                    Call(Name('it'), [
                        AnonymousFunction([], Block([
                            Do(Block([
                                Function(Name('foo'), [], Block([]))
                            ]))
                        ]))
                    ]),
                    Do(Block([
                        Function(Name('bar'), [], Block([]))
                    ]))
                ]))
            ])
        ]))
        self.assertEqual(exp, tree)

    def test_cont_int_2(self):
        tree = ast.parse(textwrap.dedent(r'''
        if true then
          return true
        elseif isinstance() then
          return true
        end
        '''))

        exp = Chunk(Block([If(
            test=TrueExpr(),
            body=Block([Return([TrueExpr()])]),
            orelse=ElseIf(
                test=Call(Name('isinstance'), []),
                body=Block([Return([TrueExpr()])]),
                orelse=None
            )
        )]))
        self.assertEqual(exp, tree)

    # Unable to tell apart true indexing vs. syntactic sugar indexing #1
    def test_cont_int_3(self):
        tree = ast.parse(textwrap.dedent(r'x[a]'))
        exp = Chunk(Block([Index(idx=Name('a'), value=Name('x'), notation=IndexNotation.SQUARE)]))
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r'''x['a']'''))
        exp = Chunk(Block([Index(idx=String('a'), value=Name('x'), notation=IndexNotation.SQUARE)]))
        self.assertEqual(exp, tree)

        tree = ast.parse(textwrap.dedent(r'x.a'))
        exp = Chunk(Block([Index(idx=Name('a'), value=Name('x'))]))
        self.assertEqual(exp, tree)
