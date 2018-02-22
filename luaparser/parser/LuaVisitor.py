# Generated from Lua.g4 by ANTLR 4.7.1
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


    # Visit a parse tree produced by LuaParser#do_block.
    def visitDo_block(self, ctx:LuaParser.Do_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#while_stat.
    def visitWhile_stat(self, ctx:LuaParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#repeat_stat.
    def visitRepeat_stat(self, ctx:LuaParser.Repeat_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#assignment.
    def visitAssignment(self, ctx:LuaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#local.
    def visitLocal(self, ctx:LuaParser.LocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#goto_stat.
    def visitGoto_stat(self, ctx:LuaParser.Goto_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#if_stat.
    def visitIf_stat(self, ctx:LuaParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#elseif_stat.
    def visitElseif_stat(self, ctx:LuaParser.Elseif_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#else_stat.
    def visitElse_stat(self, ctx:LuaParser.Else_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#for_stat.
    def visitFor_stat(self, ctx:LuaParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#function.
    def visitFunction(self, ctx:LuaParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#names.
    def visitNames(self, ctx:LuaParser.NamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#function_literal.
    def visitFunction_literal(self, ctx:LuaParser.Function_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#func_body.
    def visitFunc_body(self, ctx:LuaParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#param_list.
    def visitParam_list(self, ctx:LuaParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#ret_stat.
    def visitRet_stat(self, ctx:LuaParser.Ret_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#expr.
    def visitExpr(self, ctx:LuaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#or_expr.
    def visitOr_expr(self, ctx:LuaParser.Or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#and_expr.
    def visitAnd_expr(self, ctx:LuaParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#rel_expr.
    def visitRel_expr(self, ctx:LuaParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#concat_expr.
    def visitConcat_expr(self, ctx:LuaParser.Concat_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#add_expr.
    def visitAdd_expr(self, ctx:LuaParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#mult_expr.
    def visitMult_expr(self, ctx:LuaParser.Mult_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#bitwise_expr.
    def visitBitwise_expr(self, ctx:LuaParser.Bitwise_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#unary_expr.
    def visitUnary_expr(self, ctx:LuaParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#pow_expr.
    def visitPow_expr(self, ctx:LuaParser.Pow_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#atom.
    def visitAtom(self, ctx:LuaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx:LuaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#callee.
    def visitCallee(self, ctx:LuaParser.CalleeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_dot_index.
    def visitTail_dot_index(self, ctx:LuaParser.Tail_dot_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_brack_index.
    def visitTail_brack_index(self, ctx:LuaParser.Tail_brack_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_invoke.
    def visitTail_invoke(self, ctx:LuaParser.Tail_invokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_invoke_table.
    def visitTail_invoke_table(self, ctx:LuaParser.Tail_invoke_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_invoke_str.
    def visitTail_invoke_str(self, ctx:LuaParser.Tail_invoke_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_call.
    def visitTail_call(self, ctx:LuaParser.Tail_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_table.
    def visitTail_table(self, ctx:LuaParser.Tail_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tail_string.
    def visitTail_string(self, ctx:LuaParser.Tail_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#table_constructor.
    def visitTable_constructor(self, ctx:LuaParser.Table_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#field_list.
    def visitField_list(self, ctx:LuaParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx:LuaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#field_sep.
    def visitField_sep(self, ctx:LuaParser.Field_sepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx:LuaParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#var_list.
    def visitVar_list(self, ctx:LuaParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#expr_list.
    def visitExpr_list(self, ctx:LuaParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#name_list.
    def visitName_list(self, ctx:LuaParser.Name_listContext):
        return self.visitChildren(ctx)



del LuaParser