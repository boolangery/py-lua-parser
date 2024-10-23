# Generated from ./luaparser/parser/LuaParser.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by LuaParser#stat_empty.
    def visitStat_empty(self, ctx:LuaParser.Stat_emptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_assignment.
    def visitStat_assignment(self, ctx:LuaParser.Stat_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_functioncall.
    def visitStat_functioncall(self, ctx:LuaParser.Stat_functioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_label.
    def visitStat_label(self, ctx:LuaParser.Stat_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_break.
    def visitStat_break(self, ctx:LuaParser.Stat_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_goto.
    def visitStat_goto(self, ctx:LuaParser.Stat_gotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_do.
    def visitStat_do(self, ctx:LuaParser.Stat_doContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_while.
    def visitStat_while(self, ctx:LuaParser.Stat_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_repeat.
    def visitStat_repeat(self, ctx:LuaParser.Stat_repeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_if.
    def visitStat_if(self, ctx:LuaParser.Stat_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_for.
    def visitStat_for(self, ctx:LuaParser.Stat_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_function.
    def visitStat_function(self, ctx:LuaParser.Stat_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_localfunction.
    def visitStat_localfunction(self, ctx:LuaParser.Stat_localfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat_local.
    def visitStat_local(self, ctx:LuaParser.Stat_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#attnamelist.
    def visitAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#nameattrib.
    def visitNameattrib(self, ctx:LuaParser.NameattribContext):
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


    # Visit a parse tree produced by LuaParser#functioncall_exp.
    def visitFunctioncall_exp(self, ctx:LuaParser.Functioncall_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall_expinvoke.
    def visitFunctioncall_expinvoke(self, ctx:LuaParser.Functioncall_expinvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall_invoke.
    def visitFunctioncall_invoke(self, ctx:LuaParser.Functioncall_invokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall_nestedinvoke.
    def visitFunctioncall_nestedinvoke(self, ctx:LuaParser.Functioncall_nestedinvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall_name.
    def visitFunctioncall_name(self, ctx:LuaParser.Functioncall_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall_nested.
    def visitFunctioncall_nested(self, ctx:LuaParser.Functioncall_nestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail.
    def visitTail(self, ctx:LuaParser.TailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx:LuaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx:LuaParser.FunctiondefContext):
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