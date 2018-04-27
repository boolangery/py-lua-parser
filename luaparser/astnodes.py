"""
    ``astNodes`` module
    ===================

    Contains all Ast Node definitions.
"""

def _equalDicts(d1, d2, ignore_keys):
        ignored = set(ignore_keys)
        for k1, v1 in d1.items():
            if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
                return False
        for k2, v2 in d2.items():
            if k2 not in ignored and k2 not in d1:
                return False
        return True


class Node:
    """Base class for AST node.

    Attributes:
        displayName (`str`): Node display name (to pretty print).
    """
    def __init__(self, name, comments=[]):
        self._name = name
        self.comments = comments

    @property
    def displayName(self):
        return self._name

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return _equalDicts(self.__dict__, other.__dict__, [])
        return False


class Comment:
    def __init__(self, s, is_multi_line=False):
        self.s = s
        self.is_multi_line = is_multi_line

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return _equalDicts(self.__dict__, other.__dict__, [])
        return False


class Chunk(Node):
    """Define a Lua chunk.

    Attributes:
        body (`Block`): Chunk body.
    """
    def __init__(self, body):
        super(Chunk, self).__init__('Chunk')
        self.body = body


class Block(Node):
    """Define a Lua Block.

    Attributes:
        body (`list<Statement>`): Block body.
    """
    def __init__(self, body):
        super(Block, self).__init__('Block')
        self.body = body


''' ----------------------------------------------------------------------- '''
''' Statements                                                              '''
''' ----------------------------------------------------------------------- '''
class Statement(Node):
    """Base class for Lua statement.
    """
    pass


class Assign(Statement):
    """Lua global assignment statement.

    Attributes:
        targets (`list<Node>`): List of targets.
        values (`list<Node>`): List of values.

    """
    def __init__(self, targets, values, comments=[]):
        super(Assign, self).__init__('Assign', comments)
        self.targets = targets
        self.values  = values


class LocalAssign(Assign):
    """Lua local assignment statement.

    Attributes:
        targets (`list<Node>`): List of targets.
        values (`list<Node>`): List of values.
    """
    def __init__(self, targets, values, comments=[]):
        super(LocalAssign, self).__init__(targets, values, comments)
        self._name = 'LocalAssign'


class While(Statement):
    """Lua while statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, test, body):
        super(While, self).__init__('While')
        self.test = test
        self.body = body


class Do(Statement):
    """Lua do end statement.

    Attributes:
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, body):
        super(Do, self).__init__('Do')
        self.body = body


class Repeat(Statement):
    """Lua repeat until statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, body, test, comments=[]):
        super(Repeat, self).__init__('Repeat', comments)
        self.body = body
        self.test = test


class If(Statement):
    """Lua if statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`list<Statement>`): List of statements to execute if test is true.
        orelse (`list<Node> or ElseIf`): List of statements or ElseIf if test if false.
    """
    def __init__(self, test, body, orelse, comments=[]):
        super(If, self).__init__('If', comments)
        self.test = test
        self.body = body
        self.orelse = orelse


class ElseIf(Statement):
    """Define the elseif lua statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`list<Statement>`): List of statements to execute if test is true.
        orelse (`list<Node> or ElseIf`): List of statements or ElseIf if test if false.
    """
    def __init__(self, test, body, orelse):
        super(ElseIf, self).__init__('ElseIf')
        self.test = test
        self.body = body
        self.orelse = orelse


class Label(Statement):
    """Define the label lua statement.

    Attributes:
        id (`Node`): Label name.
    """
    def __init__(self, id):
        super(Label, self).__init__('Label')
        self.id = id


class Goto(Statement):
    """Define the goto lua statement.

    Attributes:
        label (`Node`): Label node.
    """
    def __init__(self, label, comments=[]):
        super(Goto, self).__init__('Goto', comments)
        self.label = label


class SemiColon(Statement):
    """Define the semi-colon lua statement.
    """
    def __init__(self):
        super(SemiColon, self).__init__('SemiColon')


class Break(Statement):
    """Define the break lua statement.

    """
    def __init__(self):
        super(Break, self).__init__('Break')


class Return(Statement):
    """Define the Lua return statement.

    Attributes:
        values (`list<Expression>`): Values to return.
    """
    def __init__(self, values):
        super(Return, self).__init__('Return')
        self.values = values


class Fornum(Statement):
    """Define the numeric for lua statement.

    Attributes:
        target (`Name`): Target name.
        start (`Expression`): Start index value.
        stop (`Expression`): Stop index value.
        step (`Expression`): Step value.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, target, start, stop, step, body, comments=[]):
        super(Fornum, self).__init__('Fornum', comments)
        self.target = target
        self.start  = start
        self.stop   = stop
        self.step   = step
        self.body   = body


class Forin(Statement):
    """Define the for in lua statement.

    Attributes:
        body (`list<Statement>`): List of statements to execute.
        iter (`list<Expression>`): Iterable expressions.
        targets (`list<Name>`): Start index value.
    """
    def __init__(self, body, iter, targets, comments=[]):
        super(Forin, self).__init__('Forin', comments)
        self.body = body
        self.iter = iter
        self.targets = targets


class Call(Statement):
    """Define the function call lua statement.

    Attributes:
        func (`Expression`): Function to call.
        args (`list<Expression>`): Function call arguments.
    """
    def __init__(self, func, args):
        super(Call, self).__init__('Call')
        self.func = func
        self.args = args


class Invoke(Statement):
    """Define the invoke function call lua statement (magic syntax with ':').

    Attributes:
        source (`Expression`): Source expression where function is invoked.
        func (`Expression`): Function to call.
        args (`list<Expression>`): Function call arguments.
    """
    def __init__(self, source, func, args):
        super(Invoke, self).__init__('Invoke')
        self.source = source
        self.func = func
        self.args = args


class Function(Statement):
    """Define the Lua function declaration statement.

    Attributes:
        name (`Expression`): Function name.
        args (`list<Expression>`): Function arguments.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, name, args, body):
        super(Function, self).__init__('Function')
        self.name = name
        self.args = args
        self.body = body


class LocalFunction(Statement):
    """Define the Lua local function declaration statement.

    Attributes:
        name (`Expression`): Function name.
        args (`list<Expression>`): Function arguments.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, name, args, body):
        super(LocalFunction, self).__init__('LocalFunction')
        self.name = name
        self.args = args
        self.body = body


class Method(Statement):
    """Define the Lua Object Oriented function statement.

    Attributes:
        source (`Expression`): Source expression where method is defined.
        name (`Expression`): Function name.
        args (`list<Expression>`): Function arguments.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, source, name, args, body, comments=[]):
        super(Method, self).__init__('Method', comments)
        self.source = source
        self.name = name
        self.args = args
        self.body = body


''' ----------------------------------------------------------------------- '''
''' Lua Expression                                                          '''
''' ----------------------------------------------------------------------- '''
class Expression(Node):
    """Define a Lua expression.
    """
    pass

''' ----------------------------------------------------------------------- '''
''' Types and values                                                        '''
''' ----------------------------------------------------------------------- '''
class Nil(Expression):
    """Define the Lua nil expression.
    """
    def __init__(self):
        super(Nil, self).__init__('Nil')


class TrueExpr(Expression):
    """Define the Lua true expression.
    """
    def __init__(self):
        super(TrueExpr, self).__init__('True')


class FalseExpr(Expression):
    """Define the Lua false expression.
    """
    def __init__(self):
        super(FalseExpr, self).__init__('False')


class Number(Expression):
    """Define the Lua number expression.

    Attributes:
        n (`int|float`): Numeric value.
    """
    def __init__(self, n):
        super(Number, self).__init__('Number')
        self.n = n


class Varargs(Expression):
    """Define the Lua Varargs expression (...).

    """
    def __init__(self):
        super(Varargs, self).__init__('Varargs')


class String(Expression):
    """Define the Lua string expression.

    Attributes:
        s (`string`): String value.
    """
    def __init__(self, s):
        super(String, self).__init__('String')
        self.s = s


class Table(Expression):
    """Define the Lua table expression.

    Attributes:
        fields (`list<TableField>`): Table fields.
    """
    def __init__(self, fields):
        super(Table, self).__init__('Table')
        self.fields = fields


class Field(Expression):
    """Define a lua table field expression

    Attributes:
        key (`Expression`): Key.
        value (`Expression`): Value.
    """
    def __init__(self, key, value, comments=[]):
        super(Field, self).__init__('Field', comments)
        self.key = key
        self.value = value


class Dots(Expression):
    """Define the Lua dots (...) expression.
    """
    def __init__(self):
        super(Dots, self).__init__('Dots')


class AnonymousFunction(Expression):
    """Define the Lua anonymous function expression.

    Attributes:
        args (`list<Expression>`): Function arguments.
        body (`list<Statement>`): List of statements to execute.
    """
    def __init__(self, args, body):
        super(AnonymousFunction, self).__init__('AnonymousFunction')
        self.args = args
        self.body = body

''' ----------------------------------------------------------------------- '''
''' Operators                                                               '''
''' ----------------------------------------------------------------------- '''
class Op(Expression):
    """Base class for Lua operators.
    """
    pass


class BinaryOp(Op):
    """Base class for Lua 'Left Op Right' Operators.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, name, left, right):
        super(BinaryOp, self).__init__(name)
        self.left = left
        self.right = right

''' ----------------------------------------------------------------------- '''
''' 3.4.1 – Arithmetic Operators                                            '''
''' ----------------------------------------------------------------------- '''
class AriOp(BinaryOp):
    """Base class for Arithmetic Operators"""
    pass


class AddOp(AriOp):
    """Add expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(AddOp, self).__init__('AddOp', left, right)


class SubOp(AriOp):
    """Substract expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(SubOp, self).__init__('SubOp', left, right)


class MultOp(AriOp):
    """Multiplication expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(MultOp, self).__init__('MultOp', left, right)


class FloatDivOp(AriOp):
    """Float division expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(FloatDivOp, self).__init__('FloatDivOp', left, right)


class FloorDivOp(AriOp):
    """Floor division expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(FloorDivOp, self).__init__('FloorDivOp', left, right)


class ModOp(AriOp):
    """Modulo expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(ModOp, self).__init__('ModOp', left, right)


class ExpoOp(AriOp):
    """Exponent expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(ExpoOp, self).__init__('ExpoOp', left, right)


''' ----------------------------------------------------------------------- '''
''' 3.4.2 – Bitwise Operators                                               '''
''' ----------------------------------------------------------------------- '''
class BitOp(BinaryOp):
    """Base class for bitwise Operators.
    """
    pass


class BAndOp(BitOp):
    """Bitwise and expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(BAndOp, self).__init__('BAndOp', left, right)


class BOrOp(BitOp):
    """Bitwise or expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(BOrOp, self).__init__('BOrOp', left, right)


class BXorOp(BitOp):
    """Bitwise xor expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(BXorOp, self).__init__('BXorOp', left, right)


class BShiftROp(BitOp):
    """Bitwise right shift expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(BShiftROp, self).__init__('BShiftROp', left, right)


class BShiftLOp(BitOp):
    """Bitwise left shift expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(BShiftLOp, self).__init__('BShiftLOp', left, right)


''' ----------------------------------------------------------------------- '''
''' 3.4.4 – Relational Operators                                            '''
''' ----------------------------------------------------------------------- '''
class RelOp(BinaryOp):
    """Base class for Lua relational operators.
    """
    pass


class LessThanOp(RelOp):
    """Less than expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(LessThanOp, self).__init__('RLtOp', left, right)


class GreaterThanOp(RelOp):
    """Greater than expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(GreaterThanOp, self).__init__('RGtOp', left, right)


class LessOrEqThanOp(RelOp):
    """Less or equal expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(LessOrEqThanOp, self).__init__('RLtEqOp', left, right)


class GreaterOrEqThanOp(RelOp):
    """Greater or equal expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(GreaterOrEqThanOp, self).__init__('RGtEqOp', left, right)


class EqToOp(RelOp):
    """Equal to expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(EqToOp, self).__init__('REqOp', left, right)


class NotEqToOp(RelOp):
    """Not equal to expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(NotEqToOp, self).__init__('RNotEqOp', left, right)

''' ----------------------------------------------------------------------- '''
''' 3.4.5 – Logical Operators                                               '''
''' ----------------------------------------------------------------------- '''
class LoOp(BinaryOp):
    """Base class for logical operators.
    """
    pass


class AndLoOp(LoOp):
    """Logical and expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(AndLoOp, self).__init__('LAndOp', left, right)


class OrLoOp(LoOp):
    """Logical or expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(OrLoOp, self).__init__('LOrOp', left, right)

''' ----------------------------------------------------------------------- '''
''' 3.4.6 Concat operators                                                  '''
''' ----------------------------------------------------------------------- '''
class Concat(BinaryOp):
    """Concat expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """
    def __init__(self, left, right):
        super(Concat, self).__init__('Concat', left, right)

''' ----------------------------------------------------------------------- '''
''' Unary operators                                                         '''
''' ----------------------------------------------------------------------- '''
class UnaryOp(Expression):
    """Base class for Lua unitary operator.

    Attributes:
        operand (`Expression`): Operand.
    """
    def __init__(self, name, operand):
        super(UnaryOp, self).__init__(name)
        self.operand = operand


class UMinusOp(UnaryOp):
    """Lua minus unitary operator.

    Attributes:
        operand (`Expression`): Operand.
    """
    def __init__(self, operand):
        super(UMinusOp, self).__init__('UMinusOp', operand)


class UBNotOp(UnaryOp):
    """Lua binary not unitary operator.

    Attributes:
        operand (`Expression`): Operand.
    """
    def __init__(self, operand):
        super(UBNotOp, self).__init__('UBNotOp', operand)


class ULNotOp(UnaryOp):
    """Logical not operator.

    Attributes:
        operand (`Expression`): Operand.
    """
    def __init__(self, operand):
        super(ULNotOp, self).__init__('ULNotOp', operand)

''' ----------------------------------------------------------------------- '''
''' 3.4.7 – The Length Operator                                             '''
''' ----------------------------------------------------------------------- '''
class ULengthOP(UnaryOp):
    """Length operator.
    """
    def __init__(self, operand):
        super(ULengthOP, self).__init__('ULengthOp', operand)


'''
Left Hand Side expression.
'''
class Lhs(Expression):
    """Define a Lua Left Hand Side expression.
    """
    pass


class Name(Lhs):
    """Define a Lua name expression.

    Attributes:
        id (`string`): Id.
    """
    def __init__(self, id):
        super(Name, self).__init__('Name')
        self.id = id


class Index(Lhs):
    """Define a Lua index expression.

    Attributes:
        idx (`Expression`): Index expression.
        value (`string`): Id.
    """
    def __init__(self, idx, value):
        super(Index, self).__init__('Index')
        self.idx   = idx
        self.value = value
