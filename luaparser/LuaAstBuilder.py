#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``LuaAstBuilder`` module
    ===================

    Contains all Ast Node definitions.
"""
import ast
import re

from luaparser.parser.LuaVisitor import LuaVisitor
from luaparser.astNodes import *
from luaparser.parser.LuaParser import LuaParser

def listify(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj

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
        return Chunk(self.visit(ctx.children[0]))

    def visitBlock(self, ctx):
        return Block(listify(self.visitChildren(ctx)))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.3 – Statements                                                        '''
    ''' ----------------------------------------------------------------------- '''
    def visitSetStat(self, ctx):
        return AssignStat(
            targets=listify(self.visit(ctx.children[0])), \
            values=listify(self.visit(ctx.children[2])))

    def visitLocalset(self, ctx):
        # 'local' namelist ('=' explist)?
        if len(ctx.children) > 1:
            return LocalAssignStat(
                targets=listify(self.visit(ctx.children[1])), \
                values=listify(self.visit(ctx.children[3])))
        else:
            return LocalAssignStat(
                targets=listify(self.visit(ctx.children[1])), \
                values=[])

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

    def visitIfStat(self, ctx):
        return IfStat(self.visitChildren(ctx))

    def visitElseIfStat(self, ctx):
        return ElseIfStat(self.visitChildren(ctx))

    def visitElseStat(self, ctx):
        return ElseStat(self.visitChildren(ctx))

    def visitLabel(self, ctx):
        return LabelStat(self.visitChildren(ctx))

    def visitGoto(self, ctx):
        return GotoStat(self.visitChildren(ctx))

    def visitBreakStat(self, ctx):
        return BreakStat(self.visitChildren(ctx))

    ''' 
    Visiting expressions.
    '''
    ''' 
    Types and values
    '''
    def visitNil(self, ctx):
        return NilExpr(self.visitChildren(ctx))

    def visitTrue(self, ctx):
        return TrueExpr(self.visitChildren(ctx))

    def visitFalse(self, ctx):
        return FalseExpr(self.visitChildren(ctx))

    def visitNumber(self, ctx):
        # using python number eval to parse lua number:
        number = ast.literal_eval(ctx.children[0].getText())
        return NumberExpr(number)

    def visitString(self, ctx):
        luaStr = ctx.children[0].getText()
        p = re.compile('^\[=+\[(.*)\]=+\]') # nested quote pattern
        # try remove double quote:
        if luaStr.startswith('"') and luaStr.endswith('"'):
            luaStr = luaStr[1:-1]
        # try remove single quote:
        elif luaStr.startswith("'") and luaStr.endswith("'"):
            luaStr = luaStr[1:-1]
        # try remove double square bracket:
        elif luaStr.startswith("[[") and luaStr.endswith("]]"):
            luaStr = luaStr[2:-2]
        # nested quote
        elif p.match(luaStr):
            luaStr = p.search(luaStr).group(1)
        return StringExpr(luaStr)

    def visitName(self, ctx):
        return NameExpr(ctx.children[0].getText())

    def visitArgs(self, ctx):
        return ArgsExpr(self.visitChildren(ctx))

    #def visitVarlist(self, ctx):
    #    return VarsExpr(self.visitChildren(ctx))

    #def visitNamelist(self, ctx):
    #    return VarsExpr(self.visitChildren(ctx))

    def visitVar(self, ctx):
        # : (name | '(' exp ')' varSuffix) varSuffix*
        # if name varSuffix*
        if len(ctx.children)>1 and isinstance(ctx.children[1], LuaParser.VarSuffixContext):
            child = IndexExpr([self.visit(ctx.children[0]), self.visit(ctx.children[1])])
            for i in range(2, len(ctx.children)):
                root = IndexExpr([child, self.visit(ctx.children[i])])
                child = root
            return child
        else:
            return self.visitChildren(ctx)

    #def visitExplist(self, ctx):
    #    return ExprsExpr(self.visitChildren(ctx))

    '''
    Visiting arithmetic operator expressions
    '''
    def visitOpAdd(self, ctx):
        return AddOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpSub(self, ctx):
        return SubOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpMult(self, ctx):
        return MultOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpFloatDiv(self, ctx):
        return FloatDivOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpFloorDiv(self, ctx):
        return FloorDivOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpMod(self, ctx):
        return ModOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpExpo(self, ctx):
        return ExpoOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitOpMin(self, ctx):
        return NegOpExpr(self.visitChildren(ctx))

    '''
    Relational Operators
    '''
    def visitRelOpLess(self, ctx):
        return LessThanOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitRelOpGreater(self, ctx):
        return GreaterThanOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitRelOpLessEq(self, ctx):
        return LessOrEqThanOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitRelOpGreaterEq(self, ctx):
        return GreaterOrEqThanOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitRelOpNotEq(self, ctx):
        return NotEqToOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitRelOpEq(self, ctx):
        return EqToOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))


    '''
    3.4.2 – Bitwise Operators
    '''
    def visitBitOpAnd(self, ctx):
        return BAndOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitBitOpOr(self, ctx):
        return BOrOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitBitOpXor(self, ctx):
        return BXorOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitBitOpShiftR(self, ctx):
        return BShiftROpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    def visitBitOpShiftL(self, ctx):
        return BShiftLOpExpr(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2]))

    '''
    Unary Operators
    '''
    def visitUnOpMin(self, ctx):
        return USubOpExpr(operand=self.visit(ctx.children[1]))

    def visitUnOpBitNot(self, ctx):
        return UNotOpExpr(operand=self.visit(ctx.children[1]))

    '''
    3.4.5 – Logical Operators
    '''
    def visitLoOpAnd(self, ctx):
        return AndLoOpExpr(self.visitChildren(ctx))

    def visitLoOpOr(self, ctx):
        return OrLoOpExpr(self.visitChildren(ctx))

    def visitUnOpNot(self, ctx):
        return NotLoOpExpr(self.visitChildren(ctx))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def visitConcat(self, ctx):
        return ConcatExpr(self.visitChildren(ctx))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.7 – The Length Operator                                             '''
    ''' ----------------------------------------------------------------------- '''
    def visitUnOpLength(self, ctx):
        return LengthExpr(self.visitChildren(ctx))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def visitTableconstructor(self, ctx):
        # table      : '{' (field (fieldsep field)* fieldsep?)? '}'
        # field      : '[' tableKey ']' '=' tableValue | tableKey '=' tableValue | tableValue
        # tableKey   : exp | name
        # tableValue : exp
        keys    = KeysExpr(None)
        values  = ValuesExpr(None)
        index   = 1 # lua array start index
        for field in ctx.children:
            if isinstance(field, LuaParser.FieldContext):
                hasKey = False
                for tblElem in field.children:
                    if isinstance(tblElem, LuaParser.TableKeyContext):
                        keys.addChild(self.visitChildren(tblElem))
                        hasKey = True
                    elif isinstance(tblElem, LuaParser.TableValueContext):
                        values.addChild(self.visitChildren(tblElem))
                # if no index found, create an integer key:
                if not hasKey:
                    keys.addChild(NumberExpr(index))
                    index += 1
        return TableExpr([keys, values])

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def visitFunc(self, ctx):
        pass
        # 'function' funcname funcbody
        #return AssignStat(self.visitChildren(ctx))

    def visitLocalfunc(self, ctx):
        return LocalRecStat(self.visitChildren(ctx))

    def visitFuncbody(self, ctx):
        return FunctionExpr(self.visitChildren(ctx))

    def visitFuncname(self, ctx):
        # name ('.' name)* (':' name)?
        if len(ctx.children)>2:
            child = IndexExpr([self.visit(ctx.children[0]), self.visit(ctx.children[2])])
            for i in range(3, len(ctx.children)):
                if isinstance(ctx.children[i], LuaParser.NameContext):
                    root = IndexExpr([child, self.visit(ctx.children[i])])
                    child = root
            return child
        else:
            return self.visitChildren(ctx)