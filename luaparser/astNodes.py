#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``astNodes`` module
    ===================

    Contains all Ast Node definitions.
"""


'''
AST base node.
'''
class Node(object):
    """Base class for lua AST Node"""
    def __init__(self, name, childs):
        self.name = name
        if childs == None:
            self.childs = []
        elif not isinstance(childs, list):
            self.childs = [childs]
        else:
            self.childs = childs

    def isTerm(self):
        """Test if the node is a terminal node.
        :return: true if the node is terminal
        :rtype: bool
        """
        return (len(self.childs)==0) or isinstance(self.childs[0], str)

    def getValue(self):
        if len(self.childs)==0:
            return ''
        else:
            return self.childs[0]

    def addChild(self, child):
        self.childs.append(child)


class Chunk(Node):
    """Define a Lua chunk"""
    def __init__(self, childs):
        super(Chunk, self).__init__('Chunk', childs)

class Block(Node):
    """Define a Lua Block"""
    def __init__(self, childs):
        super(Block, self).__init__('Block', childs)



'''
Statements.
'''
class Statement(Node):
    """Base class for Lua statement"""
    pass

class DoStat(Statement):
    """Define the 'do' lua statement"""
    def __init__(self, childs):
        super(DoStat, self).__init__('Do', childs)

class SetStat(Statement):
    """Define the 'set' lua statement"""
    def __init__(self, childs):
        super(SetStat, self).__init__('Set', childs)

class WhileStat(Statement):
    """Define the 'while' lua statement"""
    def __init__(self, childs):
        super(WhileStat, self).__init__('While', childs)

class RepeatStat(Statement):
    """Define the 'Repeat' lua statement"""
    def __init__(self, childs):
        super(RepeatStat, self).__init__('Repeat', childs)

class IfStat(Statement):
    """Define the 'If' lua statement"""
    def __init__(self, childs):
        super(IfStat, self).__init__('If', childs)

class FornumStat(Statement):
    """Define the 'Fornum' lua statement"""
    def __init__(self, childs):
        super(FornumStat, self).__init__('Fornum', childs)

class ForinStat(Statement):
    """Define the 'Forin' lua statement"""
    def __init__(self, childs):
        super(ForinStat, self).__init__('Forin', childs)

class LocalSetStat(Statement):
    """Define the 'Local' lua statement"""
    def __init__(self, childs):
        super(LocalSetStat, self).__init__('LocalSet', childs)

class CallStat(Statement):
    """Define the 'Call' lua statement"""
    def __init__(self, childs):
        super(CallStat, self).__init__('Call', childs)

class InvokeStat(Statement):
    """Define the 'Invoke' lua statement"""
    def __init__(self, childs):
        super(InvokeStat, self).__init__('Invoke', childs)

class LocalRecStat(Statement):
    """Lua local function statement"""
    def __init__(self, childs):
        super(LocalRecStat, self).__init__('Localrec', childs)

'''
Lua Expression nodes.
'''
class Expression(Node):
    """Define a Lua generic expression"""
    pass

'''
Types and values
'''
class NilExpr(Expression):
    """Define the Lua 'nil' expression"""
    def __init__(self, childs=None):
        super(NilExpr, self).__init__('Nil', childs)

class TrueExpr(Expression):
    """Define the Lua 'true' expression"""
    def __init__(self, childs=None):
        super(TrueExpr, self).__init__('True', childs)

class FalseExpr(Expression):
    """Define the Lua 'false' expression"""
    def __init__(self, childs=None):
        super(FalseExpr, self).__init__('False', childs)

class NumberExpr(Expression):
    """Define the Lua number expression"""
    def __init__(self, childs):
        super(NumberExpr, self).__init__('Number', childs)

class StringExpr(Expression):
    """Define the Lua string expression"""
    def __init__(self, childs):
        super(StringExpr, self).__init__('String', childs)

class DotsExpr(Expression):
    """Define the Lua dots (...) expression"""
    def __init__(self, childs=None):
        super(DotsExpr, self).__init__('Dots', childs)

class TableExpr(Expression):
    """Define the Lua table expression"""
    def __init__(self, childs):
        super(TableExpr, self).__init__('Table', childs)

class KeysExpr(Expression):
    """Table keys"""
    def __init__(self, childs):
        super(KeysExpr, self).__init__('Keys', childs)

class ValuesExpr(Expression):
    """Table values"""
    def __init__(self, childs):
        super(ValuesExpr, self).__init__('Values', childs)



class FunctionExpr(Expression):
    """Define the Lua function expression"""
    def __init__(self, childs):
        super(FunctionExpr, self).__init__('Function', childs)

class ArgsExpr(Expression):
    """Define a Lua arg list expression"""
    def __init__(self, childs):
        super(ArgsExpr, self).__init__('Args', childs)

class VarsExpr(Expression):
    """Define a Lua var list expression"""
    def __init__(self, childs):
        super(VarsExpr, self).__init__('Vars', childs)

class ExprsExpr(Expression):
    """Define a Lua expression list expression"""
    def __init__(self, childs):
        super(ExprsExpr, self).__init__('Exprs', childs)

'''
Operators
'''
class OpExpr(Expression):
    """Base class for operators"""
    pass

'''
Arithmetic Operators    
'''
class AriOpExpr(OpExpr):
    """Base class for Arithmetic Operators """
    pass

class AddOpExpr(AriOpExpr):
    """+ operator"""
    def __init__(self, childs):
        super(AddOpExpr, self).__init__('OpAdd', childs)

class SubOpExpr(AriOpExpr):
    """- operator"""
    def __init__(self, childs):
        super(SubOpExpr, self).__init__('OpSub', childs)

class MultOpExpr(AriOpExpr):
    """* operator"""
    def __init__(self, childs):
        super(MultOpExpr, self).__init__('OpMult', childs)

class FloatDivOpExpr(AriOpExpr):
    """/ operator"""
    def __init__(self, childs):
        super(FloatDivOpExpr, self).__init__('OpFloatDiv', childs)

class FloorDivOpExpr(AriOpExpr):
    """// operator"""
    def __init__(self, childs):
        super(FloorDivOpExpr, self).__init__('OpFloorDiv', childs)

class ModOpExpr(AriOpExpr):
    """# operator"""
    def __init__(self, childs):
        super(ModOpExpr, self).__init__('OpMod', childs)

class ExpoOpExpr(AriOpExpr):
    """^ operator"""
    def __init__(self, childs):
        super(ExpoOpExpr, self).__init__('OpExpo', childs)

'''
Bitwise Operators
'''
class BitOpExpr(OpExpr):
    """Base class for Bitwise Operators"""
    pass

class AndOpExpr(BitOpExpr):
    """And operator"""
    def __init__(self, childs):
        super(AndOpExpr, self).__init__('OpAnd', childs)

class OrOpExpr(BitOpExpr):
    """And operator"""
    def __init__(self, childs):
        super(OrOpExpr, self).__init__('OpOr', childs)

class XorOpExpr(BitOpExpr):
    """And operator"""
    def __init__(self, childs):
        super(XorOpExpr, self).__init__('OpXor', childs)

class ShiftROpExpr(BitOpExpr):
    """And operator"""
    def __init__(self, childs):
        super(ShiftROpExpr, self).__init__('OpShiftR', childs)

class ShiftLOpExpr(BitOpExpr):
    """And operator"""
    def __init__(self, childs):
        super(ShiftLOpExpr, self).__init__('OpShiftL', childs)


'''
Unitary Operators.
'''
class UnOpExpr(Expression):
    """Base class for Lua unitary operator"""
    pass

class UnOpNotExpr(UnOpExpr):
    """Lua not unitary operator expression"""
    def __init__(self, childs):
        super(UnOpNotExpr, self).__init__('UnOpNot', childs)

class UnOpMinExpr(UnOpExpr):
    """Lua minus unitary operator expression"""
    def __init__(self, childs):
        super(UnOpMinExpr, self).__init__('UnOpMin', childs)

'''
Left Hand Side expression.
'''
class LhsExpr(Expression):
    """Define a Lua Left Hand Side expression"""
    pass

class IdExpr(LhsExpr):
    """Define a Lua Id expression"""
    def __init__(self, childs):
        super(IdExpr, self).__init__('Id', childs)

class IndexExpr(LhsExpr):
    """Define a Lua Index expression"""
    def __init__(self, childs):
        super(IndexExpr, self).__init__('Index', childs)
