#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``LuaAstBuilder`` module
    ===================

    Contains all Ast Node definitions.
"""

from luaparser.parser.LuaVisitor import LuaVisitor
from luaparser.astNodes import *

from luaparser.parser.LuaParser import LuaParser


class ParseTreeVisitor(LuaVisitor):
    def visitChildren(self, ctx):
        nodes = []
        if ctx.children:
            for child in ctx.children:
                node = self.visit(child)
                if node != None:
                    nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        return nodes


    ''' Visiting root nodes.
    '''
    def visitChunk(self, ctx):
        return Chunk(self.visitChildren(ctx))

    def visitBlock(self, ctx):
        return Block(self.visitChildren(ctx))

    ''' Visiting statements.
    '''
    def visitSetStat(self, ctx):
        return SetStat(self.visitChildren(ctx))

    def visitLocalset(self, ctx):
        return LocalStat(self.visitChildren(ctx))

    def visitWhileStat(self, ctx):
        return WhileStat(self.visitChildren(ctx))

    def visitRepeat(self, ctx):
        return RepeatStat(self.visitChildren(ctx))

    def visitCall(self, ctx):
        return CallStat(self.visitChildren(ctx))

    def visitInvoke(self, ctx):
        return InvokeStat(self.visitChildren(ctx))

    def visitFornum(self, ctx):
        return FornumStat(self.visitChildren(ctx))

    def visitForin(self, ctx):
        return ForinStat(self.visitChildren(ctx))

    def visitFunc(self, ctx):
        # 'function' funcname funcbody
        return SetStat(self.visitChildren(ctx))

    def visitLocalfunc(self, ctx):
        return LocalRecStat(self.visitChildren(ctx))

    def visitFuncbody(self, ctx):
        return FunctionExpr(self.visitChildren(ctx))


    ''' Visiting expressions.
    '''
    def visitName(self, ctx):
        return IdExpr(ctx.children[0].getText())

    def visitArgs(self, ctx):
        return ArgsExpr(self.visitChildren(ctx))

    def visitNumber(self, ctx):
        return NumberExpr(ctx.children[0].getText())

    def visitString(self, ctx):
        return StringExpr(ctx.children[0].getText())

    def visitTrue(self, ctx):
        return TrueExpr(self.visitChildren(ctx))

    def visitFalse(self, ctx):
        return FalseExpr(self.visitChildren(ctx))

    def visitUnOpMin(self, ctx):
        return UnOpMinExpr(self.visitChildren(ctx))

    def visitVarlist(self, ctx):
        return VarsExpr(self.visitChildren(ctx))

    def visitVar(self, ctx):
        # : (name | '(' exp ')' varSuffix) varSuffix*
        print(vars(ctx))
        # if name varSuffix*
        if len(ctx.children)>1 and isinstance(ctx.children[1], LuaParser.VarSuffixContext):
            child = IndexExpr([self.visit(ctx.children[0]), self.visit(ctx.children[0])])
            for i in range(2, len(ctx.children)):
                root = IndexExpr([child, self.visit(ctx.children[i])])
                child = root
            return child
        else:
            return self.visitChildren(ctx)

    def visitExplist(self, ctx):
        return ExprsExpr(self.visitChildren(ctx))

    '''
    Visiting operator expressions
    '''
    def visitOpAdd(self, ctx):
        return AddOpExpr(self.visitChildren(ctx))