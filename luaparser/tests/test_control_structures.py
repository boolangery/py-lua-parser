from luaparser import tests
from luaparser import Parser, Printer
from luaparser.astNodes import *
import textwrap


''' ----------------------------------------------------------------------- '''
''' 3.3.4 – Control Structures                                              '''
''' ----------------------------------------------------------------------- '''
class ControlStructureTestCase(tests.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_while(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            while true do
              print('hello world')
            end"""))
        exp = Chunk(body=Block(body=[
            WhileStat(test=TrueExpr(), body=[
                CallStat(func=NameExpr('print'), args=[StringExpr('hello world')])
            ])
        ]))
        self.assertEqual(exp, ast)

    def test_repeat_until(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            repeat        
            until true
            """))
        exp = Chunk(body=Block(body=[
            RepeatStat(body=[], test=TrueExpr())
        ]))
        self.assertEqual(exp, ast)

    def test_if(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
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
        self.assertEqual(exp, ast)

    def test_if_exp(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
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
        Printer.pprint(ast, Printer.Style.PYTHON, True)
        self.assertEqual(exp, ast)

    def test_if_elseif(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            if true then 
            elseif false then     
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
        self.assertEqual(exp, ast)

    def test_if_elseif_else(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
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
        self.assertEqual(exp, ast)

    def test_if_elseif_elseif_else(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
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
        self.assertEqual(exp, ast)

    def test_label(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
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
        self.assertEqual(exp, ast)

    def test_label(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            goto foo
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
        Printer.pprint(ast, Printer.Style.PYTHON, True)
        self.assertEqual(exp, ast)
