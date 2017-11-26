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
            while a[i] do
              i = i + 1
            end"""))
        exp = Chunk(Block(
            WhileStat([
                IndexExpr([NameExpr("a"), NameExpr("i")]),
                Block(AssignStat([
                    VarsExpr(NameExpr("i")),
                    ExprsExpr(AddOpExpr([NameExpr("i"), NumberExpr(1)]))
                ]))
            ])
        ))
        self.assertAstEqual(exp, ast)

    def test_while_break(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            while a[i] do
              break
            end"""))
        exp = Chunk(Block(
            WhileStat([
                IndexExpr([NameExpr("a"), NameExpr("i")]),
                Block(BreakStat(None))
            ])
        ))
        self.assertAstEqual(exp, ast)


    def test_repeat_until(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            repeat        
            until true
            """))
        exp = Chunk(Block(RepeatStat([Block(None), TrueExpr()])))
        self.assertAstEqual(exp, ast)

    def test_if(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            if true then    
            end
            """))
        exp = Chunk(Block(IfStat([TrueExpr(), Block(None)])))
        self.assertAstEqual(exp, ast)

    def test_if_exp(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            if (a<2) then    
            end
            """))
        exp = Chunk(Block(IfStat([LessThanOpExpr([NameExpr('a'), NumberExpr(2)]), Block(None)])))
        self.assertAstEqual(exp, ast)

    def test_if_elseif(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            if true then 
            elseif false then     
            end
            """))
        exp = Chunk(Block(
            IfStat([
                TrueExpr(), Block(None), ElseIfStat([FalseExpr(), Block(None)])
            ])
        ))
        self.assertAstEqual(exp, ast)

    def test_if_elseif_else(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            if true then 
            elseif false then  
            else   
            end
            """))
        exp = Chunk(Block(
            IfStat([
                TrueExpr(), Block(None),
                ElseIfStat([FalseExpr(), Block(None)]),
                ElseStat(Block(None))
            ])
        ))
        self.assertAstEqual(exp, ast)

    def test_if_elseif_elseif_else(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            if true then 
            elseif false then  
            elseif 42 then 
            else   
            end
            """))
        exp = Chunk(Block(
            IfStat([
                TrueExpr(), Block(None),
                ElseIfStat([FalseExpr(), Block(None)]),
                ElseIfStat([NumberExpr(42), Block(None)]),
                ElseStat(Block(None))
            ])
        ))
        self.assertAstEqual(exp, ast)

    def test_label(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            ::foo::
            """))
        exp = Chunk(Block(LabelStat(NameExpr('foo'))))
        self.assertAstEqual(exp, ast)

    def test_label(self):
        ast = self.parser.srcToAST(textwrap.dedent("""
            goto foo
            ::foo::
            """))
        exp = Chunk(Block([GotoStat(NameExpr('foo')), LabelStat(NameExpr('foo'))]))
        self.assertAstEqual(exp, ast)