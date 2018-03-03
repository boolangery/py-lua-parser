from luaparser.utils  import tests
from luaparser import ast
from luaparser.astnodes import *
import textwrap


class StatementsTestCase(tests.TestCase):
    """
    3.3.1 – Blocks
    """
    def test_empty_block(self):
        tree = ast.parse(";;;;")
        exp = Chunk(Block([]))
        self.assertEqual(exp, tree)

    def test_2_block(self):
        tree = ast.parse("local a;local b;")
        exp = Chunk(Block([
            LocalAssign(targets=[Name('a')],values=[]),
            LocalAssign(targets=[Name('b')],values=[])
        ]))
        self.assertEqual(exp, tree)

        """
    3.3.3 – Assignment
    """
    def test_set_number(self):
        tree = ast.parse("i=3")
        exp = Chunk(Block([
            Assign(targets=[Name('i')],values=[Number(3)])
        ]))
        self.assertEqual(exp, tree)

    def test_set_string(self):
        tree = ast.parse('i="foo bar"')
        exp = Chunk(Block([
            Assign(targets=[Name('i')],values=[String('foo bar')])
        ]))
        self.assertEqual(exp, tree)

    def test_set_array_index(self):
        tree = ast.parse('a[i] = 42')
        exp = Chunk(Block([
            Assign(targets=[Index(idx=Name('i'), value=Name('a'))], values=[Number(42)])
        ]))
        self.assertEqual(exp, tree)

    def test_set_table_index(self):
        tree = ast.parse('_ENV.x = val')
        exp = Chunk(Block([
            Assign(targets=[Index(idx=Name('x'), value=Name('_ENV'))], values=[Name('val')])
        ]))
        self.assertEqual(exp, tree)

    def test_set_multi(self):
        tree = ast.parse('x, y = y, x')
        exp = Chunk(Block([
            Assign(targets=[Name('x'), Name('y')],values=[Name('y'), Name('x')])
        ]))
        self.assertEqual(exp, tree)

    '''
    3.3.4 – Control Structures
    '''
    def test_for_in_1(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(Block([
            Forin(
                Block([Call(func=Name('print'), args=[Name('k'), Name('v')])]),
                iter=Call(func=Name('pairs'), args=[Table(keys=[], values=[])]),
                targets=[Name('k'), Name('v')]
            )
        ]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Forin)
        self.assertEqual(nodes[2].tokens[0].value.text, '\n')
        self.assertEqual(nodes[2].tokens[1].value.text, 'for')
        self.assertEqual(nodes[2].tokens[2].value.text, ' ')
        self.assertEqual(nodes[2].tokens[3].value.text, 'k')
        self.assertEqual(nodes[2].tokens[4].value.text, ',')
        self.assertEqual(nodes[2].tokens[5].value.text, ' ')
        self.assertEqual(nodes[2].tokens[6].value.text, 'v')
        self.assertEqual(nodes[2].tokens[7].value.text, ' ')
        self.assertEqual(nodes[2].tokens[8].value.text, 'in')
        self.assertEqual(nodes[2].tokens[9].value.text, ' ')
        self.assertEqual(nodes[2].tokens[10].value.text, 'pairs')
        self.assertEqual(nodes[2].tokens[11].value.text, '(')
        self.assertEqual(nodes[2].tokens[12].value.text, '{')
        self.assertEqual(nodes[2].tokens[13].value.text, '}')
        self.assertEqual(nodes[2].tokens[14].value.text, ')')
        self.assertEqual(nodes[2].tokens[15].value.text, ' ')
        self.assertEqual(nodes[2].tokens[16].value.text, 'do')
        self.assertEqual(nodes[2].tokens[17].value.text, '\n')
        self.assertEqual(nodes[2].tokens[18].value.text, '  ')
        self.assertEqual(nodes[2].tokens[19].value.text, 'print')
        self.assertEqual(nodes[2].tokens[20].value.text, '(')
        self.assertEqual(nodes[2].tokens[21].value.text, 'k')
        self.assertEqual(nodes[2].tokens[22].value.text, ',')
        self.assertEqual(nodes[2].tokens[23].value.text, ' ')
        self.assertEqual(nodes[2].tokens[24].value.text, 'v')
        self.assertEqual(nodes[2].tokens[25].value.text, ')')
        self.assertEqual(nodes[2].tokens[26].value.text, '\n')
        self.assertEqual(nodes[2].tokens[27].value.text, 'end')

        self.assertIsInstance(nodes[5], Call)
        self.assertEqual(nodes[5].tokens[0].value.text, ' ')
        self.assertEqual(nodes[5].tokens[1].value.text, 'pairs')
        self.assertEqual(nodes[5].tokens[2].value.text, '(')
        self.assertEqual(nodes[5].tokens[3].value.text, '{')
        self.assertEqual(nodes[5].tokens[4].value.text, '}')
        self.assertEqual(nodes[5].tokens[5].value.text, ')')

        self.assertIsInstance(nodes[7], Table)
        self.assertEqual(nodes[7].tokens[0].value.text, '{')
        self.assertEqual(nodes[7].tokens[1].value.text, '}')

        self.assertIsInstance(nodes[8], Block)
        self.assertEqual(nodes[8].tokens[0].value.text, '\n')
        self.assertEqual(nodes[8].tokens[1].value.text, '  ')
        self.assertEqual(nodes[8].tokens[2].value.text, 'print')
        self.assertEqual(nodes[8].tokens[3].value.text, '(')
        self.assertEqual(nodes[8].tokens[4].value.text, 'k')
        self.assertEqual(nodes[8].tokens[5].value.text, ',')
        self.assertEqual(nodes[8].tokens[6].value.text, ' ')
        self.assertEqual(nodes[8].tokens[7].value.text, 'v')
        self.assertEqual(nodes[8].tokens[8].value.text, ')')

    def test_for_in_2(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in foo.pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(Block([
            Forin(
                Block([Call(func=Name('print'), args=[Name('k'), Name('v')])]),
                iter=Call(func=Index(Name('pairs'), Name('foo')), args=[Table(keys=[], values=[])]),
                targets=[Name('k'), Name('v')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_for_in_3(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in foo:pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(Block([
            Forin(
                Block([Call(func=Name('print'), args=[Name('k'), Name('v')])]),
                iter=Invoke(source=Name('foo'), func=Name('pairs'), args=[Table(keys=[], values=[])]),
                targets=[Name('k'), Name('v')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_for_in_4(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in bar.foo:pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(Block([
            Forin(
                body=Block([Call(func=Name('print'), args=[Name('k'), Name('v')])]),
                iter=Invoke(source=Index(Name('foo'), Name('bar')), func=Name('pairs'), args=[Table(keys=[], values=[])]),
                targets=[Name('k'), Name('v')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_for_in_5(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in bar:foo(42):pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(Block([
            Forin(
                body=Block([Call(func=Name('print'), args=[Name('k'), Name('v')])]),
                iter=Invoke(
                    source=Invoke(source=Name('bar'), func=Name('foo'), args=[Number(42)]),
                    func=Name('pairs'),
                    args=[Table(keys=[], values=[])]),
                targets=[Name('k'), Name('v')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_for_in_6(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in bar:foo(42).pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(Block([
            Forin(
                body=Block([Call(func=Name('print'), args=[Name('k'), Name('v')])]),
                iter=Call(
                    func=Index(idx=Name('pairs'), value=Invoke(source=Name('bar'), func=Name('foo'), args=[Number(42)])),
                    args=[Table(keys=[], values=[])]),
                targets=[Name('k'), Name('v')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_numeric_for(self):
        tree = ast.parse(textwrap.dedent("""
            for i=1,10,2 do print(i) end
            """))
        exp = Chunk(Block([
            Fornum(
                target=Name('i'),
                start=Number(1),
                stop=Number(10),
                step=Number(2),
                body=Block([Call(func=Name('print'), args=[Name('i')])])
            )
        ]))
        self.assertEqual(exp, tree)

    def test_do_end(self):
        tree = ast.parse(textwrap.dedent("""
            do
              local foo = 'bar'
            end
            """))
        exp = Chunk(Block([
            Do(
                body=Block([LocalAssign(targets=[Name('foo')],values=[String('bar')])])
            )
        ]))
        self.assertEqual(exp, tree)

    def test_while(self):
        tree = ast.parse(textwrap.dedent("""
            while true do
              print('hello world')
            end"""))
        exp = Chunk(Block([
            While(test=TrueExpr(), body=Block([
                Call(func=Name('print'), args=[String('hello world')])
            ]))
        ]))
        self.assertEqual(exp, tree)

    def test_repeat_until(self):
        tree = ast.parse(textwrap.dedent("""
            repeat        
            until true
            """))
        exp = Chunk(Block([
            Repeat(body=Block([]), test=TrueExpr())
        ]))
        self.assertEqual(exp, tree)

    def test_if(self):
        tree = ast.parse(textwrap.dedent("""
            if true then    
            end
            """))
        exp = Chunk(Block([
            If(
                test=TrueExpr(),
                body=Block([]),
                orelse=None
            )
        ]))
        self.assertEqual(exp, tree)

    def test_if_exp(self):
        tree = ast.parse(textwrap.dedent("""
            if (a<2) then    
            end
            """))
        exp = Chunk(Block([
            If(
                test=LessThanOp(
                    left=Name('a'),
                    right=Number(2)
                ),
                body=Block([]),
                orelse=None
            )
        ]))
        self.assertEqual(exp, tree)

    def test_if_elseif(self):
        tree = ast.parse(textwrap.dedent("""
            if true then 
            elseif false then     
            end
            """))
        exp = Chunk(Block([
            If(
                test=TrueExpr(),
                body=Block([]),
                orelse=ElseIf(test=FalseExpr(), body=Block([]), orelse=None)
            )
        ]))
        self.assertEqual(exp, tree)

    def test_if_elseif_else(self):
        tree = ast.parse(textwrap.dedent("""
            if true then 
            elseif false then  
            else   
            end
            """))
        exp = Chunk(Block([
            If(
                test=TrueExpr(),
                body=Block([]),
                orelse=ElseIf(
                    test=FalseExpr(),
                    body=Block([]),
                    orelse=Block([])
                )
            )
        ]))
        self.assertEqual(exp, tree)

    def test_if_elseif_elseif_else(self):
        tree = ast.parse(textwrap.dedent("""
            if true then
            elseif false then
            elseif 42 then
            else
              return true
            end
            """))
        exp = Chunk(Block([
            If(
                test=TrueExpr(),
                body=Block([]),
                orelse=ElseIf(
                    test=FalseExpr(),
                    body=Block([]),
                    orelse=ElseIf(
                        test=Number(42),
                        body=Block([]),
                        orelse=Block([Return([TrueExpr()])])
                    )
                )
            )
        ]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], If)
        self.assertEqual(nodes[2].tokens[0].value.text, '\n')
        self.assertEqual(nodes[2].tokens[1].value.text, 'if')
        self.assertEqual(nodes[2].tokens[2].value.text, ' ')
        self.assertEqual(nodes[2].tokens[3].value.text, 'true')
        self.assertEqual(nodes[2].tokens[4].value.text, ' ')
        self.assertEqual(nodes[2].tokens[5].value.text, 'then')
        self.assertEqual(nodes[2].tokens[6].value.text, '\n')
        self.assertEqual(nodes[2].tokens[7].value.text, 'elseif')
        self.assertEqual(nodes[2].tokens[8].value.text, ' ')
        self.assertEqual(nodes[2].tokens[9].value.text, 'false')
        self.assertEqual(nodes[2].tokens[10].value.text, ' ')
        self.assertEqual(nodes[2].tokens[11].value.text, 'then')
        self.assertEqual(nodes[2].tokens[12].value.text, '\n')
        self.assertEqual(nodes[2].tokens[13].value.text, 'elseif')
        self.assertEqual(nodes[2].tokens[14].value.text, ' ')
        self.assertEqual(nodes[2].tokens[15].value.text, '42')
        self.assertEqual(nodes[2].tokens[16].value.text, ' ')
        self.assertEqual(nodes[2].tokens[17].value.text, 'then')
        self.assertEqual(nodes[2].tokens[18].value.text, '\n')
        self.assertEqual(nodes[2].tokens[19].value.text, 'else')
        self.assertEqual(nodes[2].tokens[20].value.text, '\n')
        self.assertEqual(nodes[2].tokens[21].value.text, '  ')
        self.assertEqual(nodes[2].tokens[22].value.text, 'return')
        self.assertEqual(nodes[2].tokens[23].value.text, ' ')
        self.assertEqual(nodes[2].tokens[24].value.text, 'true')
        self.assertEqual(nodes[2].tokens[25].value.text, '\n')
        self.assertEqual(nodes[2].tokens[26].value.text, 'end')

        self.assertIsInstance(nodes[5], ElseIf)
        self.assertEqual(nodes[5].tokens[0].value.text, '\n')
        self.assertEqual(nodes[5].tokens[1].value.text, 'elseif')
        self.assertEqual(nodes[5].tokens[2].value.text, ' ')
        self.assertEqual(nodes[5].tokens[3].value.text, 'false')
        self.assertEqual(nodes[5].tokens[4].value.text, ' ')
        self.assertEqual(nodes[5].tokens[5].value.text, 'then')

        self.assertIsInstance(nodes[8], ElseIf)
        self.assertEqual(nodes[8].tokens[0].value.text, '\n')
        self.assertEqual(nodes[8].tokens[1].value.text, 'elseif')
        self.assertEqual(nodes[8].tokens[2].value.text, ' ')
        self.assertEqual(nodes[8].tokens[3].value.text, '42')
        self.assertEqual(nodes[8].tokens[4].value.text, ' ')
        self.assertEqual(nodes[8].tokens[5].value.text, 'then')

    def test_label(self):
        tree = ast.parse(textwrap.dedent("""
            ::foo::
            """))
        exp = Chunk(Block([
            Label(Name('foo'))
        ]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Label)
        self.assertEqual(nodes[2].tokens[0].value.text, '\n')
        self.assertEqual(nodes[2].tokens[1].value.text, '::')
        self.assertEqual(nodes[2].tokens[2].value.text, 'foo')
        self.assertEqual(nodes[2].tokens[3].value.text, '::')

    def test_goto(self):
        tree = ast.parse(textwrap.dedent("""
            goto foo
            ::foo::
            """))
        exp = Chunk(Block([
            Goto(label=Name('foo')),
            Label(Name('foo'))
        ]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Goto)
        self.assertEqual(nodes[2].tokens[0].value.text, '\n')
        self.assertEqual(nodes[2].tokens[1].value.text, 'goto')
        self.assertEqual(nodes[2].tokens[2].value.text, ' ')
        self.assertEqual(nodes[2].tokens[3].value.text, 'foo')

    def test_break(self):
        tree = ast.parse(textwrap.dedent("""
            break
            """))
        exp = Chunk(Block([
            Break()
        ]))
        self.assertEqual(exp, tree)

    def test_return(self):
        tree = ast.parse(r'return nil')
        exp = Chunk(Block([Return([
            Nil()
        ])]))
        self.assertEqual(exp, tree)

    def test_return_multiple(self):
        tree = ast.parse(r'return nil, "error", 42; ')
        exp = Chunk(Block([Return([
            Nil(), String('error'), Number(42)
        ])]))
        self.assertEqual(exp, tree)

        # test tokens
        nodes = list(ast.walk(tree))

        self.assertIsInstance(nodes[2], Return)
        self.assertEqual(nodes[2].tokens[0].value.text, 'return')
        self.assertEqual(nodes[2].tokens[1].value.text, ' ')
        self.assertEqual(nodes[2].tokens[2].value.text, 'nil')
        self.assertEqual(nodes[2].tokens[3].value.text, ',')
        self.assertEqual(nodes[2].tokens[4].value.text, ' ')
        self.assertEqual(nodes[2].tokens[5].value.text, '"error"')
        self.assertEqual(nodes[2].tokens[6].value.text, ',')
        self.assertEqual(nodes[2].tokens[7].value.text, ' ')
        self.assertEqual(nodes[2].tokens[8].value.text, '42')
        self.assertEqual(nodes[2].tokens[9].value.text, ';')
