# Generated from ./luaparser/parser/LuaParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LuaParser import LuaParser
else:
    from LuaParser import LuaParser

# This class defines a complete listener for a parse tree produced by LuaParser.
class LuaParserListener(ParseTreeListener):

    # Enter a parse tree produced by LuaParser#start_.
    def enterStart_(self, ctx:LuaParser.Start_Context):
        pass

    # Exit a parse tree produced by LuaParser#start_.
    def exitStart_(self, ctx:LuaParser.Start_Context):
        pass


    # Enter a parse tree produced by LuaParser#chunk.
    def enterChunk(self, ctx:LuaParser.ChunkContext):
        pass

    # Exit a parse tree produced by LuaParser#chunk.
    def exitChunk(self, ctx:LuaParser.ChunkContext):
        pass


    # Enter a parse tree produced by LuaParser#block.
    def enterBlock(self, ctx:LuaParser.BlockContext):
        pass

    # Exit a parse tree produced by LuaParser#block.
    def exitBlock(self, ctx:LuaParser.BlockContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_empty.
    def enterStat_empty(self, ctx:LuaParser.Stat_emptyContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_empty.
    def exitStat_empty(self, ctx:LuaParser.Stat_emptyContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_assignment.
    def enterStat_assignment(self, ctx:LuaParser.Stat_assignmentContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_assignment.
    def exitStat_assignment(self, ctx:LuaParser.Stat_assignmentContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_functioncall.
    def enterStat_functioncall(self, ctx:LuaParser.Stat_functioncallContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_functioncall.
    def exitStat_functioncall(self, ctx:LuaParser.Stat_functioncallContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_label.
    def enterStat_label(self, ctx:LuaParser.Stat_labelContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_label.
    def exitStat_label(self, ctx:LuaParser.Stat_labelContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_break.
    def enterStat_break(self, ctx:LuaParser.Stat_breakContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_break.
    def exitStat_break(self, ctx:LuaParser.Stat_breakContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_goto.
    def enterStat_goto(self, ctx:LuaParser.Stat_gotoContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_goto.
    def exitStat_goto(self, ctx:LuaParser.Stat_gotoContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_do.
    def enterStat_do(self, ctx:LuaParser.Stat_doContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_do.
    def exitStat_do(self, ctx:LuaParser.Stat_doContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_while.
    def enterStat_while(self, ctx:LuaParser.Stat_whileContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_while.
    def exitStat_while(self, ctx:LuaParser.Stat_whileContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_repeat.
    def enterStat_repeat(self, ctx:LuaParser.Stat_repeatContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_repeat.
    def exitStat_repeat(self, ctx:LuaParser.Stat_repeatContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_if.
    def enterStat_if(self, ctx:LuaParser.Stat_ifContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_if.
    def exitStat_if(self, ctx:LuaParser.Stat_ifContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_for.
    def enterStat_for(self, ctx:LuaParser.Stat_forContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_for.
    def exitStat_for(self, ctx:LuaParser.Stat_forContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_function.
    def enterStat_function(self, ctx:LuaParser.Stat_functionContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_function.
    def exitStat_function(self, ctx:LuaParser.Stat_functionContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_localfunction.
    def enterStat_localfunction(self, ctx:LuaParser.Stat_localfunctionContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_localfunction.
    def exitStat_localfunction(self, ctx:LuaParser.Stat_localfunctionContext):
        pass


    # Enter a parse tree produced by LuaParser#stat_local.
    def enterStat_local(self, ctx:LuaParser.Stat_localContext):
        pass

    # Exit a parse tree produced by LuaParser#stat_local.
    def exitStat_local(self, ctx:LuaParser.Stat_localContext):
        pass


    # Enter a parse tree produced by LuaParser#attnamelist.
    def enterAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        pass

    # Exit a parse tree produced by LuaParser#attnamelist.
    def exitAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        pass


    # Enter a parse tree produced by LuaParser#nameattrib.
    def enterNameattrib(self, ctx:LuaParser.NameattribContext):
        pass

    # Exit a parse tree produced by LuaParser#nameattrib.
    def exitNameattrib(self, ctx:LuaParser.NameattribContext):
        pass


    # Enter a parse tree produced by LuaParser#attrib.
    def enterAttrib(self, ctx:LuaParser.AttribContext):
        pass

    # Exit a parse tree produced by LuaParser#attrib.
    def exitAttrib(self, ctx:LuaParser.AttribContext):
        pass


    # Enter a parse tree produced by LuaParser#retstat.
    def enterRetstat(self, ctx:LuaParser.RetstatContext):
        pass

    # Exit a parse tree produced by LuaParser#retstat.
    def exitRetstat(self, ctx:LuaParser.RetstatContext):
        pass


    # Enter a parse tree produced by LuaParser#label.
    def enterLabel(self, ctx:LuaParser.LabelContext):
        pass

    # Exit a parse tree produced by LuaParser#label.
    def exitLabel(self, ctx:LuaParser.LabelContext):
        pass


    # Enter a parse tree produced by LuaParser#funcname.
    def enterFuncname(self, ctx:LuaParser.FuncnameContext):
        pass

    # Exit a parse tree produced by LuaParser#funcname.
    def exitFuncname(self, ctx:LuaParser.FuncnameContext):
        pass


    # Enter a parse tree produced by LuaParser#varlist.
    def enterVarlist(self, ctx:LuaParser.VarlistContext):
        pass

    # Exit a parse tree produced by LuaParser#varlist.
    def exitVarlist(self, ctx:LuaParser.VarlistContext):
        pass


    # Enter a parse tree produced by LuaParser#namelist.
    def enterNamelist(self, ctx:LuaParser.NamelistContext):
        pass

    # Exit a parse tree produced by LuaParser#namelist.
    def exitNamelist(self, ctx:LuaParser.NamelistContext):
        pass


    # Enter a parse tree produced by LuaParser#explist.
    def enterExplist(self, ctx:LuaParser.ExplistContext):
        pass

    # Exit a parse tree produced by LuaParser#explist.
    def exitExplist(self, ctx:LuaParser.ExplistContext):
        pass


    # Enter a parse tree produced by LuaParser#exp.
    def enterExp(self, ctx:LuaParser.ExpContext):
        pass

    # Exit a parse tree produced by LuaParser#exp.
    def exitExp(self, ctx:LuaParser.ExpContext):
        pass


    # Enter a parse tree produced by LuaParser#var.
    def enterVar(self, ctx:LuaParser.VarContext):
        pass

    # Exit a parse tree produced by LuaParser#var.
    def exitVar(self, ctx:LuaParser.VarContext):
        pass


    # Enter a parse tree produced by LuaParser#prefixexp.
    def enterPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        pass

    # Exit a parse tree produced by LuaParser#prefixexp.
    def exitPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall_exp.
    def enterFunctioncall_exp(self, ctx:LuaParser.Functioncall_expContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall_exp.
    def exitFunctioncall_exp(self, ctx:LuaParser.Functioncall_expContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall_expinvoke.
    def enterFunctioncall_expinvoke(self, ctx:LuaParser.Functioncall_expinvokeContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall_expinvoke.
    def exitFunctioncall_expinvoke(self, ctx:LuaParser.Functioncall_expinvokeContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall_invoke.
    def enterFunctioncall_invoke(self, ctx:LuaParser.Functioncall_invokeContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall_invoke.
    def exitFunctioncall_invoke(self, ctx:LuaParser.Functioncall_invokeContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall_nestedinvoke.
    def enterFunctioncall_nestedinvoke(self, ctx:LuaParser.Functioncall_nestedinvokeContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall_nestedinvoke.
    def exitFunctioncall_nestedinvoke(self, ctx:LuaParser.Functioncall_nestedinvokeContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall_name.
    def enterFunctioncall_name(self, ctx:LuaParser.Functioncall_nameContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall_name.
    def exitFunctioncall_name(self, ctx:LuaParser.Functioncall_nameContext):
        pass


    # Enter a parse tree produced by LuaParser#functioncall_nested.
    def enterFunctioncall_nested(self, ctx:LuaParser.Functioncall_nestedContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall_nested.
    def exitFunctioncall_nested(self, ctx:LuaParser.Functioncall_nestedContext):
        pass


    # Enter a parse tree produced by LuaParser#tail.
    def enterTail(self, ctx:LuaParser.TailContext):
        pass

    # Exit a parse tree produced by LuaParser#tail.
    def exitTail(self, ctx:LuaParser.TailContext):
        pass


    # Enter a parse tree produced by LuaParser#args.
    def enterArgs(self, ctx:LuaParser.ArgsContext):
        pass

    # Exit a parse tree produced by LuaParser#args.
    def exitArgs(self, ctx:LuaParser.ArgsContext):
        pass


    # Enter a parse tree produced by LuaParser#functiondef.
    def enterFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by LuaParser#functiondef.
    def exitFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by LuaParser#funcbody.
    def enterFuncbody(self, ctx:LuaParser.FuncbodyContext):
        pass

    # Exit a parse tree produced by LuaParser#funcbody.
    def exitFuncbody(self, ctx:LuaParser.FuncbodyContext):
        pass


    # Enter a parse tree produced by LuaParser#parlist.
    def enterParlist(self, ctx:LuaParser.ParlistContext):
        pass

    # Exit a parse tree produced by LuaParser#parlist.
    def exitParlist(self, ctx:LuaParser.ParlistContext):
        pass


    # Enter a parse tree produced by LuaParser#tableconstructor.
    def enterTableconstructor(self, ctx:LuaParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by LuaParser#tableconstructor.
    def exitTableconstructor(self, ctx:LuaParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by LuaParser#fieldlist.
    def enterFieldlist(self, ctx:LuaParser.FieldlistContext):
        pass

    # Exit a parse tree produced by LuaParser#fieldlist.
    def exitFieldlist(self, ctx:LuaParser.FieldlistContext):
        pass


    # Enter a parse tree produced by LuaParser#field.
    def enterField(self, ctx:LuaParser.FieldContext):
        pass

    # Exit a parse tree produced by LuaParser#field.
    def exitField(self, ctx:LuaParser.FieldContext):
        pass


    # Enter a parse tree produced by LuaParser#fieldsep.
    def enterFieldsep(self, ctx:LuaParser.FieldsepContext):
        pass

    # Exit a parse tree produced by LuaParser#fieldsep.
    def exitFieldsep(self, ctx:LuaParser.FieldsepContext):
        pass


    # Enter a parse tree produced by LuaParser#number.
    def enterNumber(self, ctx:LuaParser.NumberContext):
        pass

    # Exit a parse tree produced by LuaParser#number.
    def exitNumber(self, ctx:LuaParser.NumberContext):
        pass


    # Enter a parse tree produced by LuaParser#string.
    def enterString(self, ctx:LuaParser.StringContext):
        pass

    # Exit a parse tree produced by LuaParser#string.
    def exitString(self, ctx:LuaParser.StringContext):
        pass



del LuaParser