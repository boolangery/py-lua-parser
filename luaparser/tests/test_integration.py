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
                String(''),
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
