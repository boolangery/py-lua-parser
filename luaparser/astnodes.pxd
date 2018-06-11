"""
    ``astNodes`` module
    ===================

    Contains all Ast Node definitions.
"""

cdef class Node:
    cdef str _name
    cdef public object comments


cdef class Comment:
    pass

cdef class Chunk(Node):
    cdef public object body


cdef class Block(Node):
    cdef public object body


''' ----------------------------------------------------------------------- '''
''' Statements                                                              '''
''' ----------------------------------------------------------------------- '''
cdef class Statement(Node):
    pass


cdef class Assign(Statement):
    cdef public object targets
    cdef public object values


cdef class LocalAssign(Assign):
    pass


cdef class While(Statement):
    cdef public object test
    cdef public object body



cdef class Do(Statement):
    cdef public object body


cdef class Repeat(Statement):
    cdef public object test
    cdef public object body


cdef class If(Statement):
    cdef public object test
    cdef public object body
    cdef public object orelse


cdef class ElseIf(Statement):
    cdef public object test
    cdef public object body
    cdef public object orelse


cdef class Label(Statement):
    cdef public object id


cdef class Goto(Statement):
    cdef public object label


cdef class SemiColon(Statement):
    pass


cdef class Break(Statement):
    pass


cdef class Return(Statement):
    cdef public object values


cdef class Fornum(Statement):
    cdef public object target
    cdef public object start
    cdef public object stop
    cdef public object step
    cdef public object body


cdef class Forin(Statement):
    cdef public object body
    cdef public object iter
    cdef public object targets


cdef class Call(Statement):
    cdef public object func
    cdef public object args


cdef class Invoke(Statement):
    cdef public object source
    cdef public object func
    cdef public object args


cdef class Function(Statement):
    cdef public object name
    cdef public object args
    cdef public object body


cdef class LocalFunction(Statement):
    cdef public object name
    cdef public object args
    cdef public object body


cdef class Method(Statement):
    cdef public object source
    cdef public object name
    cdef public object args
    cdef public object body


''' ----------------------------------------------------------------------- '''
''' Lua Expression                                                          '''
''' ----------------------------------------------------------------------- '''
cdef class Expression(Node):
    pass

''' ----------------------------------------------------------------------- '''
''' Types and values                                                        '''
''' ----------------------------------------------------------------------- '''
cdef class Nil(Expression):
    pass


cdef class TrueExpr(Expression):
    pass


cdef class FalseExpr(Expression):
    pass


cdef class Number(Expression):
    cdef public object n


cdef class Varargs(Expression):
    pass


cdef class String(Expression):
    cdef public object s


cdef class Table(Expression):
    cdef public object fields


cdef class Field(Expression):
    cdef public object key
    cdef public object value


cdef class Dots(Expression):
    pass


cdef class AnonymousFunction(Expression):
    cdef public object args
    cdef public object body

''' ----------------------------------------------------------------------- '''
''' Operators                                                               '''
''' ----------------------------------------------------------------------- '''
cdef class Op(Expression):
    pass


cdef class BinaryOp(Op):
    cdef public object left
    cdef public object right


''' ----------------------------------------------------------------------- '''
''' 3.4.1 – Arithmetic Operators                                            '''
''' ----------------------------------------------------------------------- '''
cdef class AriOp(BinaryOp):
    pass


cdef class AddOp(AriOp):
    pass


cdef class SubOp(AriOp):
    pass


cdef class MultOp(AriOp):
    pass


cdef class FloatDivOp(AriOp):
    pass


cdef class FloorDivOp(AriOp):
    pass


cdef class ModOp(AriOp):
    pass


cdef class ExpoOp(AriOp):
    pass


''' ----------------------------------------------------------------------- '''
''' 3.4.2 – Bitwise Operators                                               '''
''' ----------------------------------------------------------------------- '''
cdef class BitOp(BinaryOp):
    pass


cdef class BAndOp(BitOp):
    pass


cdef class BOrOp(BitOp):
    pass


cdef class BXorOp(BitOp):
    pass


cdef class BShiftROp(BitOp):
    pass


cdef class BShiftLOp(BitOp):
    pass


''' ----------------------------------------------------------------------- '''
''' 3.4.4 – Relational Operators                                            '''
''' ----------------------------------------------------------------------- '''
cdef class RelOp(BinaryOp):
    pass


cdef class LessThanOp(RelOp):
    pass


cdef class GreaterThanOp(RelOp):
    pass


cdef class LessOrEqThanOp(RelOp):
    pass


cdef class GreaterOrEqThanOp(RelOp):
    pass


cdef class EqToOp(RelOp):
    pass


cdef class NotEqToOp(RelOp):
    pass

''' ----------------------------------------------------------------------- '''
''' 3.4.5 – Logical Operators                                               '''
''' ----------------------------------------------------------------------- '''
cdef class LoOp(BinaryOp):
    pass



cdef class AndLoOp(LoOp):
    pass


cdef class OrLoOp(LoOp):
    pass

''' ----------------------------------------------------------------------- '''
''' 3.4.6 Concat operators                                                  '''
''' ----------------------------------------------------------------------- '''
cdef class Concat(BinaryOp):
    pass

''' ----------------------------------------------------------------------- '''
''' Unary operators                                                         '''
''' ----------------------------------------------------------------------- '''
cdef class UnaryOp(Expression):
    cdef public object operand


cdef class UMinusOp(UnaryOp):
    pass


cdef class UBNotOp(UnaryOp):
    pass


cdef class ULNotOp(UnaryOp):
    pass

''' ----------------------------------------------------------------------- '''
''' 3.4.7 – The Length Operator                                             '''
''' ----------------------------------------------------------------------- '''
cdef class ULengthOP(UnaryOp):
    pass


'''
Left Hand Side expression.
'''
cdef class Lhs(Expression):
    pass


cdef class Name(Lhs):
    cdef public object id


cdef class Index(Lhs):
    cdef public object idx
    cdef public object value
