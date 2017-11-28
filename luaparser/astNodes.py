#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``astNodes`` module
    ===================

    Contains all Ast Node definitions.
"""

''' ----------------------------------------------------------------------- '''
''' AST base nodes                                                          '''
''' ----------------------------------------------------------------------- '''
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
    def __init__(self, body):
        super(Chunk, self).__init__('Chunk', [])
        self.body = body
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.body == other.body
        return False

class Block(Node):
    """Define a Lua Block"""
    def __init__(self, body):
        super(Block, self).__init__('Block', [])
        self.body = body
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.body == other.body
        return False



''' ----------------------------------------------------------------------- '''
''' Statements                                                              '''
''' ----------------------------------------------------------------------- '''
class Statement(Node):
    """Base class for Lua statement"""
    pass

class DoStat(Statement):
    """Define the 'do' lua statement"""
    def __init__(self, childs):
        super(DoStat, self).__init__('Do', childs)

class AssignStat(Statement):
    """Define the 'set' lua statement"""
    def __init__(self, targets, values):
        super(AssignStat, self).__init__('Assign', [])
        self.targets = targets
        self.values  = values
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (self.targets == other.targets) \
                    and (self.values == other.values)
        return False

class LocalAssignStat(Statement):
    """Define the 'Local assign' lua statement"""
    def __init__(self, targets, values):
        super(LocalAssignStat, self).__init__('LocalAssign', [])
        self.targets = targets
        self.values  = values
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (self.targets == other.targets) \
                   and (self.values == other.values)
        return False


class WhileStat(Statement):
    """Define the 'while' lua statement"""
    def __init__(self, childs):
        super(WhileStat, self).__init__('While', childs)

class RepeatStat(Statement):
    """Define the 'Repeat' lua statement"""
    def __init__(self, childs):
        super(RepeatStat, self).__init__('Repeat', childs)

class IfStat(Statement):
    """Define the 'if' lua statement"""
    def __init__(self, childs):
        super(IfStat, self).__init__('If', childs)

class ElseIfStat(Statement):
    """Define the 'elseif' lua statement"""
    def __init__(self, childs):
        super(ElseIfStat, self).__init__('ElseIf', childs)

class ElseStat(Statement):
    """Define the 'else' lua statement"""
    def __init__(self, childs):
        super(ElseStat, self).__init__('Else', childs)

class LabelStat(Statement):
    """Define the '::label::' lua statement"""
    def __init__(self, childs):
        super(LabelStat, self).__init__('Label', childs)

class GotoStat(Statement):
    """Define the 'goto' lua statement"""
    def __init__(self, childs):
        super(GotoStat, self).__init__('Goto', childs)

class BreakStat(Statement):
    """Define the 'break' lua statement"""
    def __init__(self, childs):
        super(BreakStat, self).__init__('Break', childs)

class FornumStat(Statement):
    """Define the 'Fornum' lua statement"""
    def __init__(self, childs):
        super(FornumStat, self).__init__('Fornum', childs)

class ForinStat(Statement):
    """Define the 'Forin' lua statement"""
    def __init__(self, childs):
        super(ForinStat, self).__init__('Forin', childs)

class CallStat(Statement):
    """Define the 'Call' lua statement"""
    def __init__(self, func, args):
        super(CallStat, self).__init__('Call', [])
        self.func = func
        self.args = args
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (self.args == other.args) and \
                   (self.func == other.func)
        return False

class InvokeStat(Statement):
    """Define the 'Invoke' lua statement"""
    def __init__(self, source, func, args):
        super(InvokeStat, self).__init__('Invoke', [])
        self.source = source
        self.func = func
        self.args = args
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (self.args == other.args) and \
                   (self.func == other.func) and \
                   (self.source == other.source)
            return False

class LocalRecStat(Statement):
    """Lua local function statement"""
    def __init__(self, childs):
        super(LocalRecStat, self).__init__('Localrec', childs)

''' ----------------------------------------------------------------------- '''
''' Lua Expression                                                          '''
''' ----------------------------------------------------------------------- '''
class Expression(Node):
    """Define a Lua generic expression"""
    pass

''' ----------------------------------------------------------------------- '''
''' Types and values                                                        '''
''' ----------------------------------------------------------------------- '''
class NilExpr(Expression):
    """Define the Lua 'nil' expression"""
    def __init__(self, childs=None):
        super(NilExpr, self).__init__('Nil', childs)
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return True
        return False

class TrueExpr(Expression):
    """Define the Lua 'true' expression"""
    def __init__(self, childs=None):
        super(TrueExpr, self).__init__('True', childs)
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return True
        return False

class FalseExpr(Expression):
    """Define the Lua 'false' expression"""
    def __init__(self, childs=None):
        super(FalseExpr, self).__init__('False', childs)
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return True
        return False

class NumberExpr(Expression):
    """Define the Lua number expression"""
    def __init__(self, n):
        super(NumberExpr, self).__init__('Number', [])
        self.n = n
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.n == other.n
        return False


class StringExpr(Expression):
    """Define the Lua string expression"""
    def __init__(self, s):
        super(StringExpr, self).__init__('String', [])
        self.s = s
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.s == other.s
        return False

class DotsExpr(Expression):
    """Define the Lua dots (...) expression"""
    def __init__(self, childs=None):
        super(DotsExpr, self).__init__('Dots', childs)

class TableExpr(Expression):
    """Define the Lua table expression"""
    def __init__(self, keys, values):
        super(TableExpr, self).__init__('Table', [])
        self.keys = keys
        self.values = values
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.keys == other.keys and self.values == other.values
        return False

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
    def __init__(self, name, args, body):
        super(FunctionExpr, self).__init__('FunctionDef', [])
        self.id   = name # TODO: rename after refactor name
        self.args = args
        self.body = body
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id and \
                   self.args == other.args and \
                   self.body == other.body
        return False

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

''' ----------------------------------------------------------------------- '''
''' Operators                                                               '''
''' ----------------------------------------------------------------------- '''
class OpExpr(Expression):
    """Base class for operators"""
    pass

class LeftRightOpExpr(OpExpr):
    """Base class for 'Left Op Right' Arithmetic Operators"""
    def __init__(self, name, left, right):
        super(LeftRightOpExpr, self).__init__(name, [])
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.left == other.left and \
                   self.right == other.right
        return False

''' ----------------------------------------------------------------------- '''
''' 3.4.1 – Arithmetic Operators                                            '''
''' ----------------------------------------------------------------------- '''
class AriOpExpr(LeftRightOpExpr):
    """Base class for Arithmetic Operators"""
    pass

class AddOpExpr(AriOpExpr):
    """+ operator"""
    def __init__(self, left, right):
        super(AddOpExpr, self).__init__('AddOp', left, right)

class SubOpExpr(AriOpExpr):
    """- operator"""
    def __init__(self, left, right):
        super(SubOpExpr, self).__init__('SubOp', left, right)

class MultOpExpr(AriOpExpr):
    """* operator"""
    def __init__(self, left, right):
        super(MultOpExpr, self).__init__('MultOp', left, right)

class FloatDivOpExpr(AriOpExpr):
    """/ operator"""
    def __init__(self, left, right):
        super(FloatDivOpExpr, self).__init__('FloatDivOp', left, right)

class FloorDivOpExpr(AriOpExpr):
    """// operator"""
    def __init__(self, left, right):
        super(FloorDivOpExpr, self).__init__('FloorDivOp', left, right)

class ModOpExpr(AriOpExpr):
    """# operator"""
    def __init__(self, left, right):
        super(ModOpExpr, self).__init__('ModOp', left, right)

class ExpoOpExpr(AriOpExpr):
    """^ operator"""
    def __init__(self, left, right):
        super(ExpoOpExpr, self).__init__('ExpoOp', left, right)


''' ----------------------------------------------------------------------- '''
''' 3.4.2 – Bitwise Operators                                               '''
''' ----------------------------------------------------------------------- '''
class BitOpExpr(LeftRightOpExpr):
    """Base class for Bitwise Operators"""
    pass

class BAndOpExpr(BitOpExpr):
    """Bitwise And operator"""
    def __init__(self, left, right):
        super(BAndOpExpr, self).__init__('BAndOp', left, right)

class BOrOpExpr(BitOpExpr):
    """Bitwise Or operator"""
    def __init__(self, left, right):
        super(BOrOpExpr, self).__init__('BOrOp', left, right)

class BXorOpExpr(BitOpExpr):
    """Bitwise Xor operator"""
    def __init__(self, left, right):
        super(BXorOpExpr, self).__init__('BXorOp', left, right)

class BShiftROpExpr(BitOpExpr):
    """Bitwise Shift Right operator"""
    def __init__(self, left, right):
        super(BShiftROpExpr, self).__init__('BShiftROp', left, right)

class BShiftLOpExpr(BitOpExpr):
    """Bitwise Shift Left operator"""
    def __init__(self, left, right):
        super(BShiftLOpExpr, self).__init__('BShiftLOp', left, right)


''' ----------------------------------------------------------------------- '''
''' 3.4.4 – Relational Operators                                            '''
''' ----------------------------------------------------------------------- '''
class RelOpExpr(LeftRightOpExpr):
    """Base class for Relational Operators """
    pass

class LessThanOpExpr(RelOpExpr):
    def __init__(self, left, right):
        super(LessThanOpExpr, self).__init__('RLtOp', left, right)

class GreaterThanOpExpr(RelOpExpr):
    def __init__(self, left, right):
        super(GreaterThanOpExpr, self).__init__('RGtOp', left, right)

class LessOrEqThanOpExpr(RelOpExpr):
    def __init__(self, left, right):
        super(LessOrEqThanOpExpr, self).__init__('RLtEqOp', left, right)

class GreaterOrEqThanOpExpr(RelOpExpr):
    def __init__(self, left, right):
        super(GreaterOrEqThanOpExpr, self).__init__('RGtEqOp', left, right)

class EqToOpExpr(RelOpExpr):
    def __init__(self, left, right):
        super(EqToOpExpr, self).__init__('REqOp', left, right)

class NotEqToOpExpr(RelOpExpr):
    def __init__(self, left, right):
        super(NotEqToOpExpr, self).__init__('RNotEqOp', left, right)

''' ----------------------------------------------------------------------- '''
''' 3.4.5 – Logical Operators                                               '''
''' ----------------------------------------------------------------------- '''
class LoOpExpr(LeftRightOpExpr):
    """Base class for Logical Operators """
    pass

class AndLoOpExpr(LoOpExpr):
    """Logical And operator"""
    def __init__(self, left, right):
        super(AndLoOpExpr, self).__init__('LAndOp', left, right)

class OrLoOpExpr(LoOpExpr):
    """Logical Or operator"""
    def __init__(self, left, right):
        super(OrLoOpExpr, self).__init__('LOrOp', left, right)



''' ----------------------------------------------------------------------- '''
''' 3.4.6 – Concatenation operator                                          '''
''' ----------------------------------------------------------------------- '''
class ConcatExpr(LeftRightOpExpr):
    def __init__(self, left, right):
        super(ConcatExpr, self).__init__('ConcatOp', left, right)

'''
Unitary Operators.
'''
class UnOpExpr(Expression):
    """Base class for Lua unitary operator"""
    def __init__(self, name, operand):
        super(UnOpExpr, self).__init__(name, [])
        self.operand = operand
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.operand == other.operand
        return False

class UBNotOpExpr(UnOpExpr):
    """Lua binary not unitary operator expression"""
    def __init__(self, operand):
        super(UBNotOpExpr, self).__init__('UBNotOp', operand)

class USubOpExpr(UnOpExpr):
    """Lua negation unitary operator expression"""
    def __init__(self, operand):
        super(USubOpExpr, self).__init__('USubOp', operand)

class ULNotOpExpr(UnOpExpr):
    """Logical Not operator"""
    def __init__(self, operand):
        super(ULNotOpExpr, self).__init__('ULNotOp', operand)

''' ----------------------------------------------------------------------- '''
''' 3.4.7 – The Length Operator                                             '''
''' ----------------------------------------------------------------------- '''
class ULengthOP(UnOpExpr):
    def __init__(self, operand):
        super(ULengthOP, self).__init__('ULengthOp', operand)

'''
Left Hand Side expression.
'''
class LhsExpr(Expression):
    """Define a Lua Left Hand Side expression"""
    pass

class NameExpr(LhsExpr):
    """Define a Lua Id expression"""
    def __init__(self, id):
        super(NameExpr, self).__init__('Name', [])
        self.id = id
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.id == other.id
        return False

class IndexExpr(LhsExpr):
    """Define a Lua Index expression"""
    def __init__(self, idx, value):
        super(IndexExpr, self).__init__('Index', [])
        self.idx    = idx
        self.value  = value
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.idx == other.idx and self.value == other.value
        return False
