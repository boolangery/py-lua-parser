# Generated from luaparser/parser/LuaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LuaParser import LuaParser
else:
    from LuaParser import LuaParser

# This class defines a complete generic visitor for a parse tree produced by LuaParser.

class LuaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LuaParser#start_.
    def visitStart_(self, ctx:LuaParser.Start_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx:LuaParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx:LuaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat.
    def visitStat(self, ctx:LuaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#assign.
    def visitAssign(self, ctx:LuaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#goto.
    def visitGoto(self, ctx:LuaParser.GotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#do.
    def visitDo(self, ctx:LuaParser.DoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#while.
    def visitWhile(self, ctx:LuaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#repeat.
    def visitRepeat(self, ctx:LuaParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#if.
    def visitIf(self, ctx:LuaParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#for.
    def visitFor(self, ctx:LuaParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#forin.
    def visitForin(self, ctx:LuaParser.ForinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#localfunction.
    def visitLocalfunction(self, ctx:LuaParser.LocalfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#localassign.
    def visitLocalassign(self, ctx:LuaParser.LocalassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#attnamelist.
    def visitAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#attrib.
    def visitAttrib(self, ctx:LuaParser.AttribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx:LuaParser.RetstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx:LuaParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#funcname.
    def visitFuncname(self, ctx:LuaParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varlist.
    def visitVarlist(self, ctx:LuaParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#namelist.
    def visitNamelist(self, ctx:LuaParser.NamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#explist.
    def visitExplist(self, ctx:LuaParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#exp.
    def visitExp(self, ctx:LuaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx:LuaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall.
    def visitFunctioncall(self, ctx:LuaParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail.
    def visitTail(self, ctx:LuaParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#nestedtail.
    def visitNestedtail(self, ctx:LuaParser.NestedtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx:LuaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#anonfunctiondef.
    def visitAnonfunctiondef(self, ctx:LuaParser.AnonfunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#funcbody.
    def visitFuncbody(self, ctx:LuaParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#parlist.
    def visitParlist(self, ctx:LuaParser.ParlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tableconstructor.
    def visitTableconstructor(self, ctx:LuaParser.TableconstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx:LuaParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx:LuaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldsep.
    def visitFieldsep(self, ctx:LuaParser.FieldsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#number.
    def visitNumber(self, ctx:LuaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#string.
    def visitString(self, ctx:LuaParser.StringContext):
        return self.visitChildren(ctx)



del LuaParser