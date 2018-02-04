astnodes module
******************************************************************************


Root node
===============================================================================

.. autoclass:: luaparser.astnodes.Node
    :members:


Statements
===============================================================================

.. autoclass:: luaparser.astnodes.Block
    :members:

.. autoclass:: luaparser.astnodes.Chunk
    :members:


Assignment
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Assign
    :members:

.. autoclass:: luaparser.astnodes.LocalAssign
    :members:


Control Structures
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.While
    :members:

.. autoclass:: luaparser.astnodes.Do
    :members:

.. autoclass:: luaparser.astnodes.Repeat
    :members:

.. autoclass:: luaparser.astnodes.If
    :members:

.. autoclass:: luaparser.astnodes.ElseIf
    :members:

.. autoclass:: luaparser.astnodes.Label
    :members:

.. autoclass:: luaparser.astnodes.Goto
    :members:

.. autoclass:: luaparser.astnodes.Break
    :members:

.. autoclass:: luaparser.astnodes.Return
    :members:


For Statement
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Fornum
    :members:

.. autoclass:: luaparser.astnodes.Forin
    :members:


Function Calls as Statements
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Call
    :members:

.. autoclass:: luaparser.astnodes.Invoke
    :members:


Function declaration
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Function
    :members:

.. autoclass:: luaparser.astnodes.LocalFunction
    :members:

.. autoclass:: luaparser.astnodes.Method
    :members:


Expressions
===============================================================================


Types and values
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Nil
    :members:

.. autoclass:: luaparser.astnodes.TrueExpr
    :members:

.. autoclass:: luaparser.astnodes.FalseExpr
    :members:

.. autoclass:: luaparser.astnodes.Number
    :members:

.. autoclass:: luaparser.astnodes.String
    :members:

.. autoclass:: luaparser.astnodes.Table
    :members:

.. autoclass:: luaparser.astnodes.Dots
    :members:

.. autoclass:: luaparser.astnodes.AnonymousFunction
    :members:

Operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Op
    :members:

.. autoclass:: luaparser.astnodes.BinaryOp
    :members:


Arithmetic operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.AriOp
    :members:

.. autoclass:: luaparser.astnodes.AddOp
    :members:

.. autoclass:: luaparser.astnodes.SubOp
    :members:

.. autoclass:: luaparser.astnodes.MultOp
    :members:

.. autoclass:: luaparser.astnodes.FloatDivOp
    :members:

.. autoclass:: luaparser.astnodes.FloorDivOp
    :members:

.. autoclass:: luaparser.astnodes.ModOp
    :members:

.. autoclass:: luaparser.astnodes.ExpoOp
    :members:


Bitwise operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.BitOp
    :members:

.. autoclass:: luaparser.astnodes.BAndOp
    :members:

.. autoclass:: luaparser.astnodes.BOrOp
    :members:

.. autoclass:: luaparser.astnodes.BXorOp
    :members:

.. autoclass:: luaparser.astnodes.BShiftROp
    :members:

.. autoclass:: luaparser.astnodes.BShiftLOp
    :members:


Relational operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.RelOp
    :members:

.. autoclass:: luaparser.astnodes.LessThanOp
    :members:

.. autoclass:: luaparser.astnodes.GreaterThanOp
    :members:

.. autoclass:: luaparser.astnodes.LessOrEqThanOp
    :members:

.. autoclass:: luaparser.astnodes.GreaterOrEqThanOp
    :members:

.. autoclass:: luaparser.astnodes.EqToOp
    :members:

.. autoclass:: luaparser.astnodes.NotEqToOp
    :members:


Logical Operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.LoOp
    :members:

.. autoclass:: luaparser.astnodes.AndLoOp
    :members:

.. autoclass:: luaparser.astnodes.OrLoOp
    :members:


Concat operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Concat
    :members:


Unary operators
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.UnaryOp
    :members:

.. autoclass:: luaparser.astnodes.UMinusOp
    :members:

.. autoclass:: luaparser.astnodes.UBNotOp
    :members:

.. autoclass:: luaparser.astnodes.ULNotOp
    :members:

.. autoclass:: luaparser.astnodes.ULengthOP
    :members:


Left hand Side expression
-------------------------------------------------------------------------------

.. autoclass:: luaparser.astnodes.Lhs
    :members:

.. autoclass:: luaparser.astnodes.Name
    :members:

.. autoclass:: luaparser.astnodes.Index
    :members:
