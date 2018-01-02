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
    def visitChildren(self, ctx, mergeList=False):
        if ctx.children:
            return self.visitChildrenList(ctx.children, mergeList)
        else:
            return []

    def visitChildrenList(self, children, mergeList=False):
        nodes = []
        for child in children:
            node = self.visit(child)
            if node != None:
                if mergeList and isinstance(node, list):
                    nodes.extend(node)
                else:
                    nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        return nodes

    def visitStartingFrom(self, ctx, index, mergeList=False):
        if ctx.children:
            return self.visitChildrenList(ctx.children[index:], mergeList)
        else:
            return []


    ''' Visiting root nodes.
    '''
    def visitChunk(self, ctx):
        return Chunk(
            self.visit(ctx.children[0]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitBlock(self, ctx):
        return Block(
            listify(self.visitChildren(ctx)),
            line=ctx.start.line,
            column=ctx.start.column)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.3 – Statements                                                        '''
    ''' ----------------------------------------------------------------------- '''
    def visitSetStat(self, ctx):
        symbol = EqSymbol(
            line=ctx.children[1].symbol.line,
            column=ctx.children[1].symbol.column)

        return AssignStat(
            targets=listify(self.visit(ctx.children[0])),
            symbol=symbol,
            values=listify(self.visit(ctx.children[2])),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitLocalset(self, ctx):
        # 'local' namelist ('=' explist)?
        if len(ctx.children) > 2:
            return LocalAssignStat(
                targets=listify(self.visit(ctx.children[1])),
                values=listify(self.visit(ctx.children[3])),
                line=ctx.start.line,
                column=ctx.start.column)
        else:
            return LocalAssignStat(
                targets=listify(self.visit(ctx.children[1])),
                values=[],
                line=ctx.start.line,
                column=ctx.start.column)

    def visitWhileStat(self, ctx):
        # 'while' exp 'do' block 'end' ;
        return WhileStat(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[3]).body,
            line=ctx.start.line,
            column=ctx.start.column)

    def visitRepeat(self, ctx):
        # 'repeat' block 'until' exp ;
        return RepeatStat(
            body=self.visit(ctx.children[1]).body,
            test=self.visit(ctx.children[3]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitCall(self, ctx):
        # varOrExp args+

        return CallStat(
            func=self.visit(ctx.children[0]), \
            args=listify(self.visitStartingFrom(ctx, 1)),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitInvoke(self, ctx):
        # varOrExp (':' name args)+
        child = InvokeStat(
            source=self.visit(ctx.children[0]), \
            func=self.visit(ctx.children[2]), \
            args=listify(self.visit(ctx.children[3])),
            line=ctx.start.line,
            column=ctx.start.column)
        # if nested invoke:
        if len(ctx.children)>4:
            # iterate (':' name args)
            for i in range(4, len(ctx.children), 3):
                root = InvokeStat(
                    source=child, \
                    func=self.visit(ctx.children[i+1]), \
                    args=listify(self.visit(ctx.children[i+2])),
                    line=ctx.start.line,
                    column=ctx.start.column)
                child = root
            return child
        else:
            return child

    def visitFornum(self, ctx):
        # 'for' name '=' exp ',' exp (',' exp)? 'do' block 'end' ;
        # if has step expr
        if len(ctx.children) > 8:
            return FornumStat(
                start=self.visit(ctx.children[3]),
                stop=self.visit(ctx.children[5]),
                step=self.visit(ctx.children[7]),
                line=ctx.start.line,
                column=ctx.start.column)
        else:
            return FornumStat(
                start=self.visit(ctx.children[3]),
                stop=self.visit(ctx.children[5]),
                step=NumberExpr(1),
                line=ctx.start.line,
                column=ctx.start.column)

    def visitForin(self, ctx):
        # 'for' namelist 'in' explist 'do' block 'end' ;
        return ForinStat(
            body=self.visit(ctx.children[5]).body,
            iter=self.visit(ctx.children[3]),
            targets=listify(self.visit(ctx.children[1])),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitIfStat(self, ctx):
        # 'if' exp 'then' block elseIfStat* elseStat? 'end' ;
        mainIf = IfStat(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[3]).body,
            orelse=None,
            line=ctx.start.line,
            column=ctx.start.column)
        lastStat = mainIf
        for node in ctx.children[4:-2]:
            elseIfNodes = self.visit(node)
            elseIf = IfStat(
                test=elseIfNodes[0],
                body=elseIfNodes[1],
                orelse=None,
                line=ctx.start.line,
                column=ctx.start.column)
            lastStat.orelse = elseIf
            lastStat = elseIf
        if isinstance(ctx.children[-2], LuaParser.ElseStatContext):
            lastStat.orelse = self.visit(ctx.children[-2])
        return mainIf

    def visitElseIfStat(self, ctx):
        # 'elseif' exp 'then' block
        return [
            self.visit(ctx.children[1]),
            self.visit(ctx.children[3]).body]

    def visitElseStat(self, ctx):
        # 'else' block
        return self.visit(ctx.children[1]).body

    def visitLabel(self, ctx):
        return LabelStat(
            id=self.visit(ctx.children[1]).id,
            line=ctx.start.line,
            column=ctx.start.column)

    def visitGoto(self, ctx):
        return GotoStat(
            label=self.visit(ctx.children[1]).id,
            line=ctx.start.line,
            column=ctx.start.column)

    def visitBreakStat(self, ctx):
        return BreakStat(
            self.visitChildren(ctx),
            line=ctx.start.line,
            column=ctx.start.column)

    ''' 
    Visiting expressions.
    '''
    ''' 
    Types and values
    '''
    def visitNil(self, ctx):
        return NilExpr(
            line=ctx.start.line,
            column=ctx.start.column)

    def visitTrue(self, ctx):
        return TrueExpr(
            line=ctx.start.line,
            column=ctx.start.column)

    def visitFalse(self, ctx):
        return FalseExpr(
            line=ctx.start.line,
            column=ctx.start.column)

    def visitNumber(self, ctx):
        # using python number eval to parse lua number:
        number = ast.literal_eval(ctx.children[0].getText())
        return NumberExpr(
            number,
            line=ctx.start.line,
            column=ctx.start.column)

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
        return StringExpr(
            luaStr,
            line=ctx.start.line,
            column=ctx.start.column)

    def visitName(self, ctx):
        return NameExpr(
            ctx.children[0].getText(),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitArgs(self, ctx):
        return self.visitChildren(ctx, mergeList=True)

    def visitVar(self, ctx):
        # : (name | '(' exp ')' varSuffix) varSuffix*
        # if name varSuffix*
        if len(ctx.children)>1 and isinstance(ctx.children[1], LuaParser.VarSuffixContext):
            child = IndexExpr(
                value=self.visit(ctx.children[0]),
                idx=self.visit(ctx.children[1]),
                line=ctx.start.line,
                column=ctx.start.column)
            for i in range(2, len(ctx.children)):
                root = IndexExpr(
                    value=child,
                    idx=self.visit(ctx.children[i]),
                    line=ctx.start.line,
                    column=ctx.start.column)
                child = root
            return child
        else:
            return self.visitChildren(ctx)

    '''
    Visiting arithmetic operator expressions
    '''
    def visitOpAdd(self, ctx):
        return AddOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpSub(self, ctx):
        return SubOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpMult(self, ctx):
        return MultOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpFloatDiv(self, ctx):
        return FloatDivOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpFloorDiv(self, ctx):
        return FloorDivOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpMod(self, ctx):
        return ModOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpExpo(self, ctx):
        return ExpoOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitOpMin(self, ctx):
        return NegOpExpr(
            self.visitChildren(ctx),
            line=ctx.start.line,
            column=ctx.start.column)

    '''
    Relational Operators
    '''
    def visitRelOpLess(self, ctx):
        return LessThanOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitRelOpGreater(self, ctx):
        return GreaterThanOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitRelOpLessEq(self, ctx):
        return LessOrEqThanOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitRelOpGreaterEq(self, ctx):
        return GreaterOrEqThanOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitRelOpNotEq(self, ctx):
        return NotEqToOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitRelOpEq(self, ctx):
        return EqToOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)


    '''
    3.4.2 – Bitwise Operators
    '''
    def visitBitOpAnd(self, ctx):
        return BAndOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitBitOpOr(self, ctx):
        return BOrOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitBitOpXor(self, ctx):
        return BXorOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitBitOpShiftR(self, ctx):
        return BShiftROpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitBitOpShiftL(self, ctx):
        return BShiftLOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    '''
    Unary Operators
    '''
    def visitUnOpMin(self, ctx):
        return USubOpExpr(
            operand=self.visit(ctx.children[1]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitUnOpBitNot(self, ctx):
        return UBNotOpExpr(
            operand=self.visit(ctx.children[1]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitUnOpNot(self, ctx):
        return ULNotOpExpr(
            self.visitChildren(ctx),
            line=ctx.start.line,
            column=ctx.start.column)

    '''
    3.4.5 – Logical Operators
    '''
    def visitLoOpAnd(self, ctx):
        return AndLoOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    def visitLoOpOr(self, ctx):
        return OrLoOpExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def visitConcat(self, ctx):
        return ConcatExpr(
            left=self.visit(ctx.children[0]),
            right=self.visit(ctx.children[2]),
            line=ctx.start.line,
            column=ctx.start.column)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.7 – The Length Operator                                             '''
    ''' ----------------------------------------------------------------------- '''
    def visitUnOpLength(self, ctx):
        return ULengthOP(
            operand=self.visit(ctx.children[1]),
            line=ctx.start.line,
            column=ctx.start.column)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def visitTableconstructor(self, ctx):
        # table      : '{' (field (fieldsep field)* fieldsep?)? '}'
        # field      : '[' tableKey ']' '=' tableValue | tableKey '=' tableValue | tableValue
        # tableKey   : exp | name
        # tableValue : exp
        keys    = []
        values  = []
        index   = 1 # lua array start index
        for field in ctx.children:
            if isinstance(field, LuaParser.FieldContext):
                hasKey = False
                for tblElem in field.children:
                    if isinstance(tblElem, LuaParser.TableKeyContext):
                        keys.append(self.visitChildren(tblElem))
                        hasKey = True
                    elif isinstance(tblElem, LuaParser.TableValueContext):
                        values.append(self.visitChildren(tblElem))
                # if no index found, create an integer key:
                if not hasKey:
                    keys.append(NumberExpr(index))
                    index += 1
        return TableExpr(
            keys,
            values,
            line=ctx.start.line,
            column=ctx.start.column)

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def visitFunctiondef(self, ctx):
        # 'function' funcbody
        argsBlock = self.visit(ctx.children[1])
        return FunctionExpr(
            name='',
            args=argsBlock[0],
            body=argsBlock[1].body,
            line=ctx.start.line,
            column=ctx.start.column)

    def visitFuncbody(self, ctx):
        # '(' parlist? ')' block 'end'
        if isinstance(ctx.children[1], LuaParser.ParlistContext):
            nodes = [self.visit(ctx.children[1]),
                     self.visit(ctx.children[3])]
        else:
            nodes = [[],self.visit(ctx.children[2])]
        return nodes

    def visitParlist(self, ctx):
        return self.visitChildren(ctx, True)


    def visitFunc(self, ctx):
        # 'function' funcname funcbody
        name      = self.visit(ctx.children[1])
        argsBlock = self.visit(ctx.children[2])

        if isinstance(name, NameExpr):
            return FunctionExpr(
                name=name.id,
                args=argsBlock[0],
                body=argsBlock[1].body,
                line=ctx.start.line,
                column=ctx.start.column)
        else:
            return AssignStat(
                targets=[name],
                values =[FunctionExpr(name='', args=argsBlock[0], body=argsBlock[1].body)],
                line=ctx.start.line,
                column=ctx.start.column)

    def visitLocalfunc(self, ctx):
        # 'local' 'function' name funcbody
        name      = self.visit(ctx.children[2])
        argsBlock = self.visit(ctx.children[3])
        return LocalFunctionExpr(
            name=name.id,
            args=argsBlock[0],
            body=argsBlock[1].body,
            line=ctx.start.line,
            column=ctx.start.column)


    def visitFuncname(self, ctx):
        # name ('.' name)* (':' name)?
        if len(ctx.children)>2:
            child = IndexExpr(
                value=self.visit(ctx.children[0]),
                idx=self.visit(ctx.children[2]).id,
                line=ctx.start.line,
                column=ctx.start.column)

            for i in range(3, len(ctx.children)):
                if isinstance(ctx.children[i], LuaParser.NameContext):
                    root = IndexExpr(
                        value=child,
                        idx=self.visit(ctx.children[i]).id,
                        line=ctx.start.line,
                        column=ctx.start.column)
                    child = root
            return child
        else:
            return self.visitChildren(ctx)


    ''' ----------------------------------------------------------------------- '''
    ''' Comments                                                                '''
    ''' ----------------------------------------------------------------------- '''
    def visitComment_rule(self, ctx):
        comment = self.visitString(ctx).s
        if comment.startswith('--'):
            comment = comment[2:]
        return CommentStat(
            comment.strip(' \t\n\r'),
            line=ctx.start.line,
            column=ctx.start.column)
