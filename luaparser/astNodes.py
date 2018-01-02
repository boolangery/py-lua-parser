"""
    ``astNodes`` module
    ===================

    Contains all Ast Node definitions.
"""


def equal_dicts(d1, d2, ignore_keys):
    ignored = set(ignore_keys)
    for k1, v1 in d1.items():
        if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
            return False
    for k2, v2 in d2.items():
        if k2 not in ignored and k2 not in d1:
            return False
    return True

''' ----------------------------------------------------------------------- '''
''' AST base nodes                                                          '''
''' ----------------------------------------------------------------------- '''
class Node(object):
    """Base class for lua AST Node"""
    def __init__(self, name, line=0, column=0):
        self.name = name
        self.line = line
        self.column = column

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            # TODO: refactor all test to include line and column:
            return equal_dicts(self.__dict__, other.__dict__, ['line', 'column'])
            # return self.__dict__ == other.__dict__
        return False

class Chunk(Node):
    """Define a Lua chunk"""
    def __init__(self, body, line=0, column=0):
        super(Chunk, self).__init__('Chunk', line, column)
        self.body = body

class Block(Node):
    """Define a Lua Block"""
    def __init__(self, body, line=0, column=0):
        super(Block, self).__init__('Block', line, column)
        self.body = body


''' ----------------------------------------------------------------------- '''
''' Statements                                                              '''
''' ----------------------------------------------------------------------- '''
class Statement(Node):
    """Base class for Lua statement"""
    pass

class AssignStat(Statement):
    """Define the 'set' lua statement"""
    def __init__(self, targets, values, line=0, column=0):
        super(AssignStat, self).__init__('Assign', line, column)
        self.targets = targets
        self.values  = values

class LocalAssignStat(Statement):
    """Define the 'Local assign' lua statement"""
    def __init__(self, targets, values, line=0, column=0):
        super(LocalAssignStat, self).__init__('LocalAssign', line, column)
        self.targets = targets
        self.values  = values

class WhileStat(Statement):
    """Define the 'while' lua statement"""
    def __init__(self, test, body, line=0, column=0):
        super(WhileStat, self).__init__('While', line, column)
        self.test = test
        self.body = body

class RepeatStat(Statement):
    """Define the 'Repeat' lua statement"""
    def __init__(self, body, test, line=0, column=0):
        super(RepeatStat, self).__init__('Repeat', line, column)
        self.body = body
        self.test = test

class IfStat(Statement):
    """Define the 'if' lua statement"""
    def __init__(self, test, body, orelse, line=0, column=0):
        super(IfStat, self).__init__('If', line, column)
        self.test = test
        self.body = body
        self.orelse = orelse

class LabelStat(Statement):
    """Define the '::label::' lua statement"""
    def __init__(self, id, line=0, column=0):
        super(LabelStat, self).__init__('Label', line, column)
        self.id = id

class GotoStat(Statement):
    """Define the 'goto' lua statement"""
    def __init__(self, label, line=0, column=0):
        super(GotoStat, self).__init__('Goto', line, column)
        self.label = label

class BreakStat(Statement):
    """Define the 'break' lua statement"""
    def __init__(self, line=0, column=0):
        super(BreakStat, self).__init__('Break', line, column)

class FornumStat(Statement):
    """Define the 'Fornum' lua statement"""
    def __init__(self, start, stop, step, line=0, column=0):
        super(FornumStat, self).__init__('Fornum', line, column)
        self.start = start
        self.stop = stop
        self.step = step

class ForinStat(Statement):
    """Define the 'Forin' lua statement"""
    def __init__(self, body, iter, targets, line=0, column=0):
        super(ForinStat, self).__init__('Forin', line, column)
        self.body = body
        self.iter = iter
        self.targets = targets

class CallStat(Statement):
    """Define the 'Call' lua statement"""
    def __init__(self, func, args, line=0, column=0):
        super(CallStat, self).__init__('Call', line, column)
        self.func = func
        self.args = args

class InvokeStat(Statement):
    """Define the 'Invoke' lua statement"""
    def __init__(self, source, func, args, line=0, column=0):
        super(InvokeStat, self).__init__('Invoke', line, column)
        self.source = source
        self.func = func
        self.args = args

class LocalFunctionExpr(Statement):
    """Define the Lua local function statement"""
    def __init__(self, name, args, body, line=0, column=0):
        super(LocalFunctionExpr, self).__init__('LocalFunctionDef', line, column)
        self.id   = name
        self.args = args
        self.body = body

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
    def __init__(self, line=0, column=0):
        super(NilExpr, self).__init__('Nil', line, column)

class TrueExpr(Expression):
    """Define the Lua 'true' expression"""
    def __init__(self, line=0, column=0):
        super(TrueExpr, self).__init__('True', line, column)

class FalseExpr(Expression):
    """Define the Lua 'false' expression"""
    def __init__(self, line=0, column=0):
        super(FalseExpr, self).__init__('False', line, column)

class NumberExpr(Expression):
    """Define the Lua number expression"""
    def __init__(self, n, line=0, column=0):
        super(NumberExpr, self).__init__('Number', line, column)
        self.n = n

class StringExpr(Expression):
    """Define the Lua string expression"""
    def __init__(self, s, line=0, column=0):
        super(StringExpr, self).__init__('String', line, column)
        self.s = s

class DotsExpr(Expression):
    """Define the Lua dots (...) expression"""
    def __init__(self, line=0, column=0):
        super(DotsExpr, self).__init__('Dots', line, column)

class TableExpr(Expression):
    """Define the Lua table expression"""
    def __init__(self, keys, values, line=0, column=0):
        super(TableExpr, self).__init__('Table', line, column)
        self.keys = keys
        self.values = values

class KeysExpr(Expression):
    """Table keys"""
    def __init__(self, line=0, column=0):
        super(KeysExpr, self).__init__('Keys', line, column)

class ValuesExpr(Expression):
    """Table values"""
    def __init__(self, line=0, column=0):
        super(ValuesExpr, self).__init__('Values', line, column)

class FunctionExpr(Expression):
    """Define the Lua function expression"""
    def __init__(self, name, args, body, line=0, column=0):
        super(FunctionExpr, self).__init__('FunctionDef', line, column)
        self.id   = name # TODO: rename after refactor name
        self.args = args
        self.body = body

class ArgsExpr(Expression):
    """Define a Lua arg list expression"""
    def __init__(self, line=0, column=0):
        super(ArgsExpr, self).__init__('Args', line, column)

class VarsExpr(Expression):
    """Define a Lua var list expression"""
    def __init__(self, line=0, column=0):
        super(VarsExpr, self).__init__('Vars', line, column)

class ExprsExpr(Expression):
    """Define a Lua expression list expression"""
    def __init__(self, line=0, column=0):
        super(ExprsExpr, self).__init__('Exprs', line, column)

''' ----------------------------------------------------------------------- '''
''' Operators                                                               '''
''' ----------------------------------------------------------------------- '''
class OpExpr(Expression):
    """Base class for operators"""
    pass

class LeftRightOpExpr(OpExpr):
    """Base class for 'Left Op Right' Arithmetic Operators"""
    def __init__(self, name, left, right, line=0, column=0):
        super(LeftRightOpExpr, self).__init__(name, line, column)
        self.left = left
        self.right = right

''' ----------------------------------------------------------------------- '''
''' 3.4.1 – Arithmetic Operators                                            '''
''' ----------------------------------------------------------------------- '''
class AriOpExpr(LeftRightOpExpr):
    """Base class for Arithmetic Operators"""
    pass

class AddOpExpr(AriOpExpr):
    """+ operator"""
    def __init__(self, left, right, line=0, column=0):
        super(AddOpExpr, self).__init__('AddOp', left, right, line, column)

class SubOpExpr(AriOpExpr):
    """- operator"""
    def __init__(self, left, right, line=0, column=0):
        super(SubOpExpr, self).__init__('SubOp', left, right, line, column)

class MultOpExpr(AriOpExpr):
    """* operator"""
    def __init__(self, left, right, line=0, column=0):
        super(MultOpExpr, self).__init__('MultOp', left, right, line, column)

class FloatDivOpExpr(AriOpExpr):
    """/ operator"""
    def __init__(self, left, right, line=0, column=0):
        super(FloatDivOpExpr, self).__init__('FloatDivOp', left, right, line, column)

class FloorDivOpExpr(AriOpExpr):
    """// operator"""
    def __init__(self, left, right, line=0, column=0):
        super(FloorDivOpExpr, self).__init__('FloorDivOp', left, right, line, column)

class ModOpExpr(AriOpExpr):
    """# operator"""
    def __init__(self, left, right, line=0, column=0):
        super(ModOpExpr, self).__init__('ModOp', left, right, line, column)

class ExpoOpExpr(AriOpExpr):
    """^ operator"""
    def __init__(self, left, right, line=0, column=0):
        super(ExpoOpExpr, self).__init__('ExpoOp', left, right, line, column)


''' ----------------------------------------------------------------------- '''
''' 3.4.2 – Bitwise Operators                                               '''
''' ----------------------------------------------------------------------- '''
class BitOpExpr(LeftRightOpExpr):
    """Base class for Bitwise Operators"""
    pass

class BAndOpExpr(BitOpExpr):
    """Bitwise And operator"""
    def __init__(self, left, right, line=0, column=0):
        super(BAndOpExpr, self).__init__('BAndOp', left, right, line, column)

class BOrOpExpr(BitOpExpr):
    """Bitwise Or operator"""
    def __init__(self, left, right, line=0, column=0):
        super(BOrOpExpr, self).__init__('BOrOp', left, right, line, column)

class BXorOpExpr(BitOpExpr):
    """Bitwise Xor operator"""
    def __init__(self, left, right, line=0, column=0):
        super(BXorOpExpr, self).__init__('BXorOp', left, right, line, column)

class BShiftROpExpr(BitOpExpr):
    """Bitwise Shift Right operator"""
    def __init__(self, left, right, line=0, column=0):
        super(BShiftROpExpr, self).__init__('BShiftROp', left, right, line, column)

class BShiftLOpExpr(BitOpExpr):
    """Bitwise Shift Left operator"""
    def __init__(self, left, right, line=0, column=0):
        super(BShiftLOpExpr, self).__init__('BShiftLOp', left, right, line, column)


''' ----------------------------------------------------------------------- '''
''' 3.4.4 – Relational Operators                                            '''
''' ----------------------------------------------------------------------- '''
class RelOpExpr(LeftRightOpExpr):
    """Base class for Relational Operators """
    pass

class LessThanOpExpr(RelOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(LessThanOpExpr, self).__init__('RLtOp', left, right, line, column)

class GreaterThanOpExpr(RelOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(GreaterThanOpExpr, self).__init__('RGtOp', left, right, line, column)

class LessOrEqThanOpExpr(RelOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(LessOrEqThanOpExpr, self).__init__('RLtEqOp', left, right, line, column)

class GreaterOrEqThanOpExpr(RelOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(GreaterOrEqThanOpExpr, self).__init__('RGtEqOp', left, right, line, column)

class EqToOpExpr(RelOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(EqToOpExpr, self).__init__('REqOp', left, right, line, column)

class NotEqToOpExpr(RelOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(NotEqToOpExpr, self).__init__('RNotEqOp', left, right, line, column)

''' ----------------------------------------------------------------------- '''
''' 3.4.5 – Logical Operators                                               '''
''' ----------------------------------------------------------------------- '''
class LoOpExpr(LeftRightOpExpr):
    """Base class for Logical Operators """
    pass

class AndLoOpExpr(LoOpExpr):
    """Logical And operator"""
    def __init__(self, left, right, line=0, column=0):
        super(AndLoOpExpr, self).__init__('LAndOp', left, right, line, column)

class OrLoOpExpr(LoOpExpr):
    """Logical Or operator"""
    def __init__(self, left, right, line=0, column=0):
        super(OrLoOpExpr, self).__init__('LOrOp', left, right, line, column)



''' ----------------------------------------------------------------------- '''
''' 3.4.6 – Concatenation operator                                          '''
''' ----------------------------------------------------------------------- '''
class ConcatExpr(LeftRightOpExpr):
    def __init__(self, left, right, line=0, column=0):
        super(ConcatExpr, self).__init__('ConcatOp', left, right, line, column)

'''
Unitary Operators.
'''
class UnOpExpr(Expression):
    """Base class for Lua unitary operator"""
    def __init__(self, name, operand, line=0, column=0):
        super(UnOpExpr, self).__init__(name, line, column)
        self.operand = operand

class UBNotOpExpr(UnOpExpr):
    """Lua binary not unitary operator expression"""
    def __init__(self, operand, line=0, column=0):
        super(UBNotOpExpr, self).__init__('UBNotOp', operand, line, column)

class USubOpExpr(UnOpExpr):
    """Lua negation unitary operator expression"""
    def __init__(self, operand, line=0, column=0):
        super(USubOpExpr, self).__init__('USubOp', operand, line, column)

class ULNotOpExpr(UnOpExpr):
    """Logical Not operator"""
    def __init__(self, operand, line=0, column=0):
        super(ULNotOpExpr, self).__init__('ULNotOp', operand, line, column)

''' ----------------------------------------------------------------------- '''
''' 3.4.7 – The Length Operator                                             '''
''' ----------------------------------------------------------------------- '''
class ULengthOP(UnOpExpr):
    def __init__(self, operand, line=0, column=0):
        super(ULengthOP, self).__init__('ULengthOp', operand, line, column)

'''
Left Hand Side expression.
'''
class LhsExpr(Expression):
    """Define a Lua Left Hand Side expression"""
    pass

class NameExpr(LhsExpr):
    """Define a Lua Id expression"""
    def __init__(self, id, line=0, column=0):
        super(NameExpr, self).__init__('Name', line, column)
        self.id = id

class IndexExpr(LhsExpr):
    """Define a Lua Index expression"""
    def __init__(self, idx, value, line=0, column=0):
        super(IndexExpr, self).__init__('Index', line, column)
        self.idx    = idx
        self.value  = value

''' ----------------------------------------------------------------------- '''
''' Comments                                                                '''
''' ----------------------------------------------------------------------- '''
class CommentStat(Statement):
    def __init__(self, s, line=0, column=0):
        super(CommentStat, self).__init__('Comment', line, column)
        self.s = s
