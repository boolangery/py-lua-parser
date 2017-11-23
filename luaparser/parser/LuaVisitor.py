# Generated from Lua.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LuaParser import LuaParser
else:
    from LuaParser import LuaParser

# This class defines a complete generic visitor for a parse tree produced by LuaParser.

class LuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx:LuaParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx:LuaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stat.
    def visitStat(self, ctx:LuaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#setStat.
    def visitSetStat(self, ctx:LuaParser.SetStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#call.
    def visitCall(self, ctx:LuaParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#invoke.
    def visitInvoke(self, ctx:LuaParser.InvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx:LuaParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#breakStat.
    def visitBreakStat(self, ctx:LuaParser.BreakStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#goto.
    def visitGoto(self, ctx:LuaParser.GotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#do.
    def visitDo(self, ctx:LuaParser.DoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#whileStat.
    def visitWhileStat(self, ctx:LuaParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#repeat.
    def visitRepeat(self, ctx:LuaParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#ifStat.
    def visitIfStat(self, ctx:LuaParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fornum.
    def visitFornum(self, ctx:LuaParser.FornumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#forin.
    def visitForin(self, ctx:LuaParser.ForinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#func.
    def visitFunc(self, ctx:LuaParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#localfunc.
    def visitLocalfunc(self, ctx:LuaParser.LocalfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#localset.
    def visitLocalset(self, ctx:LuaParser.LocalsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#elseIfStat.
    def visitElseIfStat(self, ctx:LuaParser.ElseIfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#elseStat.
    def visitElseStat(self, ctx:LuaParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx:LuaParser.RetstatContext):
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


    # Visit a parse tree produced by LuaParser#name.
    def visitName(self, ctx:LuaParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#explist.
    def visitExplist(self, ctx:LuaParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#unOpLength.
    def visitUnOpLength(self, ctx:LuaParser.UnOpLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#relOpLessEq.
    def visitRelOpLessEq(self, ctx:LuaParser.RelOpLessEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#bitOpOr.
    def visitBitOpOr(self, ctx:LuaParser.BitOpOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opExpo.
    def visitOpExpo(self, ctx:LuaParser.OpExpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#relOpGreaterEq.
    def visitRelOpGreaterEq(self, ctx:LuaParser.RelOpGreaterEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opMult.
    def visitOpMult(self, ctx:LuaParser.OpMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#bitOpAnd.
    def visitBitOpAnd(self, ctx:LuaParser.BitOpAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#bitOpShiftL.
    def visitBitOpShiftL(self, ctx:LuaParser.BitOpShiftLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#loOpOr.
    def visitLoOpOr(self, ctx:LuaParser.LoOpOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#unOpBitNot.
    def visitUnOpBitNot(self, ctx:LuaParser.UnOpBitNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#bitOpXor.
    def visitBitOpXor(self, ctx:LuaParser.BitOpXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opSub.
    def visitOpSub(self, ctx:LuaParser.OpSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#bitOpShiftR.
    def visitBitOpShiftR(self, ctx:LuaParser.BitOpShiftRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#nil.
    def visitNil(self, ctx:LuaParser.NilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opAdd.
    def visitOpAdd(self, ctx:LuaParser.OpAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opFloorDiv.
    def visitOpFloorDiv(self, ctx:LuaParser.OpFloorDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#number.
    def visitNumber(self, ctx:LuaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#relOpEq.
    def visitRelOpEq(self, ctx:LuaParser.RelOpEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#relOpGreater.
    def visitRelOpGreater(self, ctx:LuaParser.RelOpGreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#relOpLess.
    def visitRelOpLess(self, ctx:LuaParser.RelOpLessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#table.
    def visitTable(self, ctx:LuaParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#unOpNot.
    def visitUnOpNot(self, ctx:LuaParser.UnOpNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#unOpMin.
    def visitUnOpMin(self, ctx:LuaParser.UnOpMinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opFloatDiv.
    def visitOpFloatDiv(self, ctx:LuaParser.OpFloatDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#todo6.
    def visitTodo6(self, ctx:LuaParser.Todo6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#false.
    def visitFalse(self, ctx:LuaParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#concat.
    def visitConcat(self, ctx:LuaParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#loOpAnd.
    def visitLoOpAnd(self, ctx:LuaParser.LoOpAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#opMod.
    def visitOpMod(self, ctx:LuaParser.OpModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#true.
    def visitTrue(self, ctx:LuaParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#todo4.
    def visitTodo4(self, ctx:LuaParser.Todo4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#relOpNotEq.
    def visitRelOpNotEq(self, ctx:LuaParser.RelOpNotEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#todo5.
    def visitTodo5(self, ctx:LuaParser.Todo5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#todo2.
    def visitTodo2(self, ctx:LuaParser.Todo2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#stringExp.
    def visitStringExp(self, ctx:LuaParser.StringExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#todo3.
    def visitTodo3(self, ctx:LuaParser.Todo3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx:LuaParser.PrefixexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varOrExp.
    def visitVarOrExp(self, ctx:LuaParser.VarOrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx:LuaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varSuffix.
    def visitVarSuffix(self, ctx:LuaParser.VarSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#nameAndArgs.
    def visitNameAndArgs(self, ctx:LuaParser.NameAndArgsContext):
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


    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx:LuaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tableKey.
    def visitTableKey(self, ctx:LuaParser.TableKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tableValue.
    def visitTableValue(self, ctx:LuaParser.TableValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldsep.
    def visitFieldsep(self, ctx:LuaParser.FieldsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#string.
    def visitString(self, ctx:LuaParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#comment_rule.
    def visitComment_rule(self, ctx:LuaParser.Comment_ruleContext):
        return self.visitChildren(ctx)



del LuaParser