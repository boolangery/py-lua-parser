# Generated from luaparser/parser/LuaParser.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by LuaParser#stat.
    def enterStat(self, ctx:LuaParser.StatContext):
        pass

    # Exit a parse tree produced by LuaParser#stat.
    def exitStat(self, ctx:LuaParser.StatContext):
        pass


    # Enter a parse tree produced by LuaParser#assign.
    def enterAssign(self, ctx:LuaParser.AssignContext):
        pass

    # Exit a parse tree produced by LuaParser#assign.
    def exitAssign(self, ctx:LuaParser.AssignContext):
        pass


    # Enter a parse tree produced by LuaParser#goto.
    def enterGoto(self, ctx:LuaParser.GotoContext):
        pass

    # Exit a parse tree produced by LuaParser#goto.
    def exitGoto(self, ctx:LuaParser.GotoContext):
        pass


    # Enter a parse tree produced by LuaParser#do.
    def enterDo(self, ctx:LuaParser.DoContext):
        pass

    # Exit a parse tree produced by LuaParser#do.
    def exitDo(self, ctx:LuaParser.DoContext):
        pass


    # Enter a parse tree produced by LuaParser#while.
    def enterWhile(self, ctx:LuaParser.WhileContext):
        pass

    # Exit a parse tree produced by LuaParser#while.
    def exitWhile(self, ctx:LuaParser.WhileContext):
        pass


    # Enter a parse tree produced by LuaParser#repeat.
    def enterRepeat(self, ctx:LuaParser.RepeatContext):
        pass

    # Exit a parse tree produced by LuaParser#repeat.
    def exitRepeat(self, ctx:LuaParser.RepeatContext):
        pass


    # Enter a parse tree produced by LuaParser#if.
    def enterIf(self, ctx:LuaParser.IfContext):
        pass

    # Exit a parse tree produced by LuaParser#if.
    def exitIf(self, ctx:LuaParser.IfContext):
        pass


    # Enter a parse tree produced by LuaParser#for.
    def enterFor(self, ctx:LuaParser.ForContext):
        pass

    # Exit a parse tree produced by LuaParser#for.
    def exitFor(self, ctx:LuaParser.ForContext):
        pass


    # Enter a parse tree produced by LuaParser#forin.
    def enterForin(self, ctx:LuaParser.ForinContext):
        pass

    # Exit a parse tree produced by LuaParser#forin.
    def exitForin(self, ctx:LuaParser.ForinContext):
        pass


    # Enter a parse tree produced by LuaParser#functiondef.
    def enterFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by LuaParser#functiondef.
    def exitFunctiondef(self, ctx:LuaParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by LuaParser#localfunction.
    def enterLocalfunction(self, ctx:LuaParser.LocalfunctionContext):
        pass

    # Exit a parse tree produced by LuaParser#localfunction.
    def exitLocalfunction(self, ctx:LuaParser.LocalfunctionContext):
        pass


    # Enter a parse tree produced by LuaParser#localassign.
    def enterLocalassign(self, ctx:LuaParser.LocalassignContext):
        pass

    # Exit a parse tree produced by LuaParser#localassign.
    def exitLocalassign(self, ctx:LuaParser.LocalassignContext):
        pass


    # Enter a parse tree produced by LuaParser#attnamelist.
    def enterAttnamelist(self, ctx:LuaParser.AttnamelistContext):
        pass

    # Exit a parse tree produced by LuaParser#attnamelist.
    def exitAttnamelist(self, ctx:LuaParser.AttnamelistContext):
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


    # Enter a parse tree produced by LuaParser#functioncall.
    def enterFunctioncall(self, ctx:LuaParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by LuaParser#functioncall.
    def exitFunctioncall(self, ctx:LuaParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by LuaParser#tail.
    def enterTail(self, ctx:LuaParser.TailContext):
        pass

    # Exit a parse tree produced by LuaParser#tail.
    def exitTail(self, ctx:LuaParser.TailContext):
        pass


    # Enter a parse tree produced by LuaParser#nestedtail.
    def enterNestedtail(self, ctx:LuaParser.NestedtailContext):
        pass

    # Exit a parse tree produced by LuaParser#nestedtail.
    def exitNestedtail(self, ctx:LuaParser.NestedtailContext):
        pass


    # Enter a parse tree produced by LuaParser#args.
    def enterArgs(self, ctx:LuaParser.ArgsContext):
        pass

    # Exit a parse tree produced by LuaParser#args.
    def exitArgs(self, ctx:LuaParser.ArgsContext):
        pass


    # Enter a parse tree produced by LuaParser#anonfunctiondef.
    def enterAnonfunctiondef(self, ctx:LuaParser.AnonfunctiondefContext):
        pass

    # Exit a parse tree produced by LuaParser#anonfunctiondef.
    def exitAnonfunctiondef(self, ctx:LuaParser.AnonfunctiondefContext):
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