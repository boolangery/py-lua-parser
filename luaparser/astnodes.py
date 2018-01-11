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
        self._name = name
        self._start = 0
        self._stop = 0

    @property
    def name(self):
        return self._name
    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def stop(self):
        return self._stop

    @start.setter
    def stop(self, value):
        self._stop = value

    def equalDicts(self, d1, d2, ignore_keys):
        ignored = set(ignore_keys)
        for k1, v1 in d1.items():
            if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
                return False
        for k2, v2 in d2.items():
            if k2 not in ignored and k2 not in d1:
                return False
        return True

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.equalDicts(self.__dict__, other.__dict__, ['_start', '_stop'])
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

class Assign(Statement):
    """Define the 'set' lua statement"""
    def __init__(self, targets, values):
        super(Assign, self).__init__('Assign')
        self.targets = targets
        self.values  = values

class LocalAssign(Statement):
    """Define the 'Local assign' lua statement"""
    def __init__(self, targets, values):
        super(LocalAssign, self).__init__('LocalAssign')
        self.targets = targets
        self.values  = values

class While(Statement):
    """Define the 'while' lua statement"""
    def __init__(self, test, body):
        super(While, self).__init__('While')
        self.test = test
        self.body = body

class Repeat(Statement):
    """Define the 'Repeat' lua statement"""
    def __init__(self, body, test):
        super(Repeat, self).__init__('Repeat')
        self.body = body
        self.test = test

class If(Statement):
    """Define the 'if' lua statement"""
    def __init__(self, test, body, orelse):
        super(If, self).__init__('If')
        self.test = test
        self.body = body
        self.orelse = orelse

class Label(Statement):
    """Define the '::label::' lua statement"""
    def __init__(self, id):
        super(Label, self).__init__('Label')
        self.id = id

class Goto(Statement):
    """Define the 'goto' lua statement"""
    def __init__(self, label):
        super(Goto, self).__init__('Goto')
        self.label = label

class Break(Statement):
    """Define the 'break' lua statement"""
    def __init__(self):
        super(Break, self).__init__('Break')

class Fornum(Statement):
    """Define the 'Fornum' lua statement"""
    def __init__(self, start, stop, step):
        super(Fornum, self).__init__('Fornum')
        self.start = start
        self.stop = stop
        self.step = step

class Forin(Statement):
    """Define the 'Forin' lua statement"""
    def __init__(self, body, iter, targets):
        super(Forin, self).__init__('Forin')
        self.body = body
        self.iter = iter
        self.targets = targets

class Call(Statement):
    """Define the 'Call' lua statement"""
    def __init__(self, func, args):
        super(Call, self).__init__('Call')
        self.func = func
        self.args = args

class Invoke(Statement):
    """Define the 'Invoke' lua statement"""
    def __init__(self, source, func, args):
        super(Invoke, self).__init__('Invoke')
        self.source = source
        self.func = func
        self.args = args

class LocalFunction(Statement):
    """Define the Lua local function statement"""
    def __init__(self, name, args, body):
        super(LocalFunction, self).__init__('LocalFunctionDef')
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
class Nil(Expression):
    """Define the Lua 'nil' expression"""
    def __init__(self):
        super(Nil, self).__init__('Nil')

class TrueExpr(Expression):
    """Define the Lua 'true' expression"""
    def __init__(self):
        super(TrueExpr, self).__init__('True')

class FalseExpr(Expression):
    """Define the Lua 'false' expression"""
    def __init__(self):
        super(FalseExpr, self).__init__('False')

class Number(Expression):
    """Define the Lua number expression"""
    def __init__(self, n):
        super(Number, self).__init__('Number')
        self.n = n

class String(Expression):
    """Define the Lua string expression"""
    def __init__(self, s):
        super(String, self).__init__('String')
        self.s = s

class Dots(Expression):
    """Define the Lua dots (...) expression"""
    def __init__(self):
        super(Dots, self).__init__('Dots')

class Table(Expression):
    """Define the Lua table expression"""
    def __init__(self, keys, values):
        super(Table, self).__init__('Table')
        self.keys = keys
        self.values = values

class Function(Expression):
    """Define the Lua function expression"""
    def __init__(self, name, args, body):
        super(Function, self).__init__('FunctionDef')
        self.id   = name # TODO: rename after refactor name
        self.args = args
        self.body = body

''' ----------------------------------------------------------------------- '''
''' Operators                                                               '''
''' ----------------------------------------------------------------------- '''
class Op(Expression):
    """Base class for operators"""
    pass

class LeftRightOp(Op):
    """Base class for 'Left Op Right' Arithmetic Operators"""
    def __init__(self, name, left, right):
        super(LeftRightOp, self).__init__(name)
        self.left = left
        self.right = right

''' ----------------------------------------------------------------------- '''
''' 3.4.1 – Arithmetic Operators                                            '''
''' ----------------------------------------------------------------------- '''
class AriOp(LeftRightOp):
    """Base class for Arithmetic Operators"""
    pass

class AddOp(AriOp):
    """+ operator"""
    def __init__(self, left, right):
        super(AddOp, self).__init__('AddOp', left, right)

class SubOp(AriOp):
    """- operator"""
    def __init__(self, left, right):
        super(SubOp, self).__init__('SubOp', left, right)

class MultOp(AriOp):
    """* operator"""
    def __init__(self, left, right):
        super(MultOp, self).__init__('MultOp', left, right)

class FloatDivOp(AriOp):
    """/ operator"""
    def __init__(self, left, right):
        super(FloatDivOp, self).__init__('FloatDivOp', left, right)

class FloorDivOp(AriOp):
    """// operator"""
    def __init__(self, left, right):
        super(FloorDivOp, self).__init__('FloorDivOp', left, right)

class ModOp(AriOp):
    """# operator"""
    def __init__(self, left, right):
        super(ModOp, self).__init__('ModOp', left, right)

class ExpoOp(AriOp):
    """^ operator"""
    def __init__(self, left, right):
        super(ExpoOp, self).__init__('ExpoOp', left, right)


''' ----------------------------------------------------------------------- '''
''' 3.4.2 – Bitwise Operators                                               '''
''' ----------------------------------------------------------------------- '''
class BitOp(LeftRightOp):
    """Base class for Bitwise Operators"""
    pass

class BAndOp(BitOp):
    """Bitwise And operator"""
    def __init__(self, left, right):
        super(BAndOp, self).__init__('BAndOp', left, right)

class BOrOp(BitOp):
    """Bitwise Or operator"""
    def __init__(self, left, right):
        super(BOrOp, self).__init__('BOrOp', left, right)

class BXorOp(BitOp):
    """Bitwise Xor operator"""
    def __init__(self, left, right):
        super(BXorOp, self).__init__('BXorOp', left, right)

class BShiftROp(BitOp):
    """Bitwise Shift Right operator"""
    def __init__(self, left, right):
        super(BShiftROp, self).__init__('BShiftROp', left, right)

class BShiftLOp(BitOp):
    """Bitwise Shift Left operator"""
    def __init__(self, left, right):
        super(BShiftLOp, self).__init__('BShiftLOp', left, right)


''' ----------------------------------------------------------------------- '''
''' 3.4.4 – Relational Operators                                            '''
''' ----------------------------------------------------------------------- '''
class RelOp(LeftRightOp):
    """Base class for Relational Operators """
    pass

class LessThanOp(RelOp):
    def __init__(self, left, right):
        super(LessThanOp, self).__init__('RLtOp', left, right)

class GreaterThanOp(RelOp):
    def __init__(self, left, right):
        super(GreaterThanOp, self).__init__('RGtOp', left, right)

class LessOrEqThanOp(RelOp):
    def __init__(self, left, right):
        super(LessOrEqThanOp, self).__init__('RLtEqOp', left, right)

class GreaterOrEqThanOp(RelOp):
    def __init__(self, left, right):
        super(GreaterOrEqThanOp, self).__init__('RGtEqOp', left, right)

class EqToOp(RelOp):
    def __init__(self, left, right):
        super(EqToOp, self).__init__('REqOp', left, right)

class NotEqToOp(RelOp):
    def __init__(self, left, right):
        super(NotEqToOp, self).__init__('RNotEqOp', left, right)

''' ----------------------------------------------------------------------- '''
''' 3.4.5 – Logical Operators                                               '''
''' ----------------------------------------------------------------------- '''
class LoOp(LeftRightOp):
    """Base class for Logical Operators """
    pass

class AndLoOp(LoOp):
    """Logical And operator"""
    def __init__(self, left, right):
        super(AndLoOp, self).__init__('LAndOp', left, right)

class OrLoOp(LoOp):
    """Logical Or operator"""
    def __init__(self, left, right):
        super(OrLoOp, self).__init__('LOrOp', left, right)



''' ----------------------------------------------------------------------- '''
''' 3.4.6 – Concatenation operator                                          '''
''' ----------------------------------------------------------------------- '''
class Concat(LeftRightOp):
    def __init__(self, left, right):
        super(Concat, self).__init__('ConcatOp', left, right)

'''
Unitary Operators.
'''
class UnOp(Expression):
    """Base class for Lua unitary operator"""
    def __init__(self, name, operand):
        super(UnOp, self).__init__(name)
        self.operand = operand

class UBNotOp(UnOp):
    """Lua binary not unitary operator expression"""
    def __init__(self, operand):
        super(UBNotOp, self).__init__('UBNotOp', operand)

class USubOp(UnOp):
    """Lua negation unitary operator expression"""
    def __init__(self, operand):
        super(USubOp, self).__init__('USubOp', operand)

class ULNotOp(UnOp):
    """Logical Not operator"""
    def __init__(self, operand):
        super(ULNotOp, self).__init__('ULNotOp', operand)

''' ----------------------------------------------------------------------- '''
''' 3.4.7 – The Length Operator                                             '''
''' ----------------------------------------------------------------------- '''
class ULengthOP(UnOp):
    def __init__(self, operand):
        super(ULengthOP, self).__init__('ULengthOp', operand)

'''
Left Hand Side expression.
'''
class Lhs(Expression):
    """Define a Lua Left Hand Side expression"""
    pass

class Name(Lhs):
    """Define a Lua Id expression"""
    def __init__(self, id):
        super(Name, self).__init__('Name')
        self.id = id

class Index(Lhs):
    """Define a Lua Index expression"""
    def __init__(self, idx, value):
        super(Index, self).__init__('Index')
        self.idx    = idx
        self.value  = value

''' ----------------------------------------------------------------------- '''
''' Comments                                                                '''
''' ----------------------------------------------------------------------- '''
class Comment(Statement):
    def __init__(self, s):
        super(Comment, self).__init__('Comment')
        self.s = s
