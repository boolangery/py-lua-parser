from luaparser import tests
from luaparser import ast
from luaparser.astNodes import *
import textwrap


class StatementsTestCase(tests.TestCase):
    """
    3.3.1 – Blocks
    """
    def test_empty_block(self):
        tree = ast.parse(";;;;")
        exp = Chunk(body=Block(body=[]))
        self.assertEqual(exp, tree)

    def test_2_block(self):
        tree = ast.parse("local a;local b;")
        exp = Chunk(body=Block(body=[
            LocalAssignStat(targets=[NameExpr('a')],values=[]),
            LocalAssignStat(targets=[NameExpr('b')],values=[])
        ]))
        self.assertEqual(exp, tree)

        """
    3.3.3 – Assignment
    """
    def test_set_number(self):
        tree = ast.parse("i=3")
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('i')],values=[NumberExpr(3)])
        ]))
        self.assertEqual(exp, tree)

    def test_set_string(self):
        tree = ast.parse('i="foo bar"')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('i')],values=[StringExpr('foo bar')])
        ]))
        self.assertEqual(exp, tree)

    def test_set_array_index(self):
        tree = ast.parse('a[i] = 42')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[IndexExpr(idx=NameExpr('i'), value=NameExpr('a'))], values=[NumberExpr(42)])
        ]))
        self.assertEqual(exp, tree)

    def test_set_table_index(self):
        tree = ast.parse('_ENV.x = val')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[IndexExpr(idx=NameExpr('x'), value=NameExpr('_ENV'))], values=[NameExpr('val')])
        ]))
        self.assertEqual(exp, tree)

    def test_set_multi(self):
        tree = ast.parse('x, y = y, x')
        exp = Chunk(body=Block(body=[
            AssignStat(targets=[NameExpr('x'), NameExpr('y')],values=[NameExpr('y'), NameExpr('x')])
        ]))
        self.assertEqual(exp, tree)

    '''
    3.3.4 – Control Structures
    '''
    def test_for_in(self):
        tree = ast.parse(textwrap.dedent("""
            for k, v in pairs({}) do
              print(k, v)
            end
            """))
        exp = Chunk(body=Block(body=[
            ForinStat(
                body=[CallStat(func=NameExpr('print'), args=[NameExpr('k'), NameExpr('v')])],
                iter=CallStat(func=NameExpr('pairs'), args=[TableExpr(keys=[], values=[])]),
                targets=[NameExpr('k'), NameExpr('v')]
            )
        ]))
        self.assertEqual(exp, tree)

    def test_numeric_for(self):
        tree = ast.parse(textwrap.dedent("""
            for i=1,10,2 do print(i) end
            """))
        exp = Chunk(body=Block(body=[
            FornumStat(
                start=NumberExpr(1),
                stop=NumberExpr(10),
                step=NumberExpr(2)
            )
        ]))
        self.assertEqual(exp, tree)

    def test_while(self):
        tree = ast.parse(textwrap.dedent("""
            while true do
              print('hello world')
            end"""))
        exp = Chunk(body=Block(body=[
            WhileStat(test=TrueExpr(), body=[
                CallStat(func=NameExpr('print'), args=[StringExpr('hello world')])
            ])
        ]))
        self.assertEqual(exp, tree)

    def test_repeat_until(self):
        tree = ast.parse(textwrap.dedent("""
            repeat        
            until true
            """))
        exp = Chunk(body=Block(body=[
            RepeatStat(body=[], test=TrueExpr())
        ]))
        self.assertEqual(exp, tree)

    def test_if(self):
        tree = ast.parse(textwrap.dedent("""
            if true then    
            end
            """))
        exp = Chunk(body=Block(body=[
            IfStat(
                test=TrueExpr(),
                body=[],
                orelse=None
            )
        ]))
        self.assertEqual(exp, tree)

    def test_if_exp(self):
        tree = ast.parse(textwrap.dedent("""
            if (a<2) then    
            end
            """))
        exp = Chunk(body=Block(body=[
            IfStat(
                test=LessThanOpExpr(
                    left=NameExpr('a'),
                    right=NumberExpr(2)
                ),
                body=[],
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
        exp = Chunk(body=Block(body=[
            IfStat(
                test=TrueExpr(),
                body=[],
                orelse=None
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
        exp = Chunk(body=Block(body=[
            IfStat(
                test=TrueExpr(),
                body=[],
                orelse=IfStat(
                    test=FalseExpr(),
                    body=[],
                    orelse=[]
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
            end
            """))
        exp = Chunk(body=Block(body=[
            IfStat(
                test=TrueExpr(),
                body=[],
                orelse=IfStat(
                    test=FalseExpr(),
                    body=[],
                    orelse=IfStat(
                        test=NumberExpr(42),
                        body=[],
                        orelse=[]
                    )
                )
            )
        ]))
        self.assertEqual(exp, tree)

    def test_label(self):
        tree = ast.parse(textwrap.dedent("""
            ::foo::
            """))
        exp = Chunk(body=Block(body=[
            IfStat(
                test=TrueExpr(),
                body=[],
                orelse=IfStat(
                    test=FalseExpr(),
                    body=[],
                    orelse=IfStat(
                        test=NumberExpr(42),
                        body=[],
                        orelse=[]
                    )
                )
            )
        ]))
        self.assertEqual(exp, tree)

    def test_label(self):
        tree = ast.parse(textwrap.dedent("""
            goto foo
            ::foo::
            """))
        exp = Chunk(body=Block(body=[
            GotoStat(label='foo'),
            LabelStat(id='foo')
        ]))
        self.assertEqual(exp, tree)


    def test_comment_line(self):
        tree = ast.parse(textwrap.dedent("""
            -- a basic comment
            """))
        exp = Chunk(body=Block(body=[
            CommentStat('a basic comment')
        ]))
        self.assertEqual(exp, tree)

    # def test_comment_enable_code(self):
    #     tree = ast.parse(textwrap.dedent("""
    #         ---[[The long handled doubleshovel means that this code will run
    #         print "This will print because it is not a comment!"
    #         -- We can still include comments by prefixing them with a doubledash
    #         -- print "This will not print because it is commented out"
    #         ]]
    #         """))
    #     exp = Chunk(body=Block(body=[
    #         GotoStat(label='foo'),
    #         LabelStat(id='foo')
    #     ]))
    #     Printer.pprint(tree, Printer.Style.PYTHON, True)
    #     self.assertEqual(exp, tree)