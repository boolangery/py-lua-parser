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
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

class Chunk(Node):
    """Define a Lua chunk"""
    def __init__(self, body):
        super(Chunk, self).__init__('Chunk')
        self.body = body

class Block(Node):
    """Define a Lua Block"""
    def __init__(self, body):
        super(Block, self).__init__('Block')
        self.body = body


''' ----------------------------------------------------------------------- '''
''' Statements                                                              '''
''' ----------------------------------------------------------------------- '''
class Statement(Node):
    """Base class for Lua statement"""
    pass

class AssignStat(Statement):
    """Define the 'set' lua statement"""
    def __init__(self, targets, values):
        super(AssignStat, self).__init__('Assign')
        self.targets = targets
        self.values  = values

class LocalAssignStat(Statement):
    """Define the 'Local assign' lua statement"""
    def __init__(self, targets, values):
        super(LocalAssignStat, self).__init__('LocalAssign')
        self.targets = targets
        self.values  = values

class WhileStat(Statement):
    """Define the 'while' lua statement"""
    def __init__(self, test, body):
        super(WhileStat, self).__init__('While')
        self.test = test
        self.body = body

class RepeatStat(Statement):
    """Define the 'Repeat' lua statement"""
    def __init__(self, body, test):
        super(RepeatStat, self).__init__('Repeat')
        self.body = body
        self.test = test

class IfStat(Statement):
    """Define the 'if' lua statement"""
    def __init__(self, test, body, orelse):
        super(IfStat, self).__init__('If')
        self.test = test
        self.body = body
        self.orelse = orelse

class LabelStat(Statement):
    """Define the '::label::' lua statement"""
    def __init__(self, id):
        super(LabelStat, self).__init__('Label')
        self.id = id

class GotoStat(Statement):
    """Define the 'goto' lua statement"""
    def __init__(self, label):
        super(GotoStat, self).__init__('Goto')
        self.label = label

class BreakStat(Statement):
    """Define the 'break' lua statement"""
    def __init__(self):
        super(BreakStat, self).__init__('Break')

class FornumStat(Statement):
    """Define the 'Fornum' lua statement"""
    def __init__(self, start, stop, step):
        super(FornumStat, self).__init__('Fornum')
        self.start = start
        self.stop = stop
        self.step = step

class ForinStat(Statement):
    """Define the 'Forin' lua statement"""
    def __init__(self, body, iter, targets):
        super(ForinStat, self).__init__('Forin')
        self.body = body
        self.iter = iter
        self.targets = targets

class CallStat(Statement):
    """Define the 'Call' lua statement"""
    def __init__(self, func, args):
        super(CallStat, self).__init__('Call')
        self.func = func
        self.args = args

class InvokeStat(Statement):
    """Define the 'Invoke' lua statement"""
    def __init__(self, source, func, args):
        super(InvokeStat, self).__init__('Invoke')
        self.source = source
        self.func = func
        self.args = args

class LocalFunctionExpr(Statement):
    """Define the Lua local function statement"""
    def __init__(self, name, args, body):
        super(LocalFunctionExpr, self).__init__('LocalFunctionDef')
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
    def __init__(self):
        super(NilExpr, self).__init__('Nil')

class TrueExpr(Expression):
    """Define the Lua 'true' expression"""
    def __init__(self):
        super(TrueExpr, self).__init__('True')

class FalseExpr(Expression):
    """Define the Lua 'false' expression"""
    def __init__(self):
        super(FalseExpr, self).__init__('False')

class NumberExpr(Expression):
    """Define the Lua number expression"""
    def __init__(self, n):
        super(NumberExpr, self).__init__('Number')
        self.n = n

class StringExpr(Expression):
    """Define the Lua string expression"""
    def __init__(self, s):
        super(StringExpr, self).__init__('String')
        self.s = s

class DotsExpr(Expression):
    """Define the Lua dots (...) expression"""
    def __init__(self):
        super(DotsExpr, self).__init__('Dots')

class TableExpr(Expression):
    """Define the Lua table expression"""
    def __init__(self, keys, values):
        super(TableExpr, self).__init__('Table')
        self.keys = keys
        self.values = values

class KeysExpr(Expression):
    """Table keys"""
    def __init__(self):
        super(KeysExpr, self).__init__('Keys')

class ValuesExpr(Expression):
    """Table values"""
    def __init__(self):
        super(ValuesExpr, self).__init__('Values')

class FunctionExpr(Expression):
    """Define the Lua function expression"""
    def __init__(self, name, args, body):
        super(FunctionExpr, self).__init__('FunctionDef')
        self.id   = name # TODO: rename after refactor name
        self.args = args
        self.body = body

class ArgsExpr(Expression):
    """Define a Lua arg list expression"""
    def __init__(self):
        super(ArgsExpr, self).__init__('Args')

class VarsExpr(Expression):
    """Define a Lua var list expression"""
    def __init__(self):
        super(VarsExpr, self).__init__('Vars')

class ExprsExpr(Expression):
    """Define a Lua expression list expression"""
    def __init__(self):
        super(ExprsExpr, self).__init__('Exprs')

''' ----------------------------------------------------------------------- '''
''' Operators                                                               '''
''' ----------------------------------------------------------------------- '''
class OpExpr(Expression):
    """Base class for operators"""
    pass

class LeftRightOpExpr(OpExpr):
    """Base class for 'Left Op Right' Arithmetic Operators"""
    def __init__(self, name, left, right):
        super(LeftRightOpExpr, self).__init__(name)
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
        super(UnOpExpr, self).__init__(name)
        self.operand = operand

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
        super(NameExpr, self).__init__('Name')
        self.id = id

class IndexExpr(LhsExpr):
    """Define a Lua Index expression"""
    def __init__(self, idx, value):
        super(IndexExpr, self).__init__('Index')
        self.idx    = idx
        self.value  = value

''' ----------------------------------------------------------------------- '''
''' Comments                                                                '''
''' ----------------------------------------------------------------------- '''
class CommentStat(Statement):
    def __init__(self, s):
        super(CommentStat, self).__init__('Comment')
        self.s = s
