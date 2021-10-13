"""
    ``astnodes`` module
    ===================

    Contains all Ast Node definitions.
"""
from enum import Enum
from typing import List, Optional

Comments = Optional[List["Comment"]]


def _equal_dicts(d1, d2, ignore_keys):
    ignored = set(ignore_keys)
    for k1, v1 in d1.items():
        if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
            return False
    for k2, v2 in d2.items():
        if k2 not in ignored and k2 not in d1:
            return False
    return True


class Node:
    """Base class for AST node."""

    def __init__(
        self,
        name: str,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        if comments is None:
            comments = []
        self._name: str = name
        self.comments: List[str] = comments
        self.start_char: Optional[int] = start_char
        self.stop_char: Optional[int] = stop_char
        self.lineno: Optional[int] = lineno

    @property
    def display_name(self) -> str:
        return self._name

    def __eq__(self, other) -> bool:
        if isinstance(self, other.__class__):
            return _equal_dicts(
                self.__dict__, other.__dict__, ["start_char", "stop_char", "lineno"]
            )
        return False

    def to_json(self) -> any:
        return {
            self._name: {
                k: v for k, v in self.__dict__.items() if not k.startswith("_") and v
            }
        }


class Comment(Node):
    def __init__(
        self,
        s: str,
        is_multi_line: bool = False,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Comment, self).__init__(
            "Comment", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.s: str = s
        self.is_multi_line: bool = is_multi_line


class Statement(Node):
    """Base class for Lua statement."""


class Expression(Node):
    """Define a Lua expression."""


class Block(Node):
    """Define a Lua Block."""

    def __init__(
        self,
        body: List[Statement],
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Block, self).__init__(
            "Block", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.body: List[Statement] = body


class Chunk(Node):
    """Define a Lua chunk.

    Attributes:
        body (`Block`): Chunk body.
    """

    def __init__(
        self,
        body: Block,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Chunk, self).__init__("Chunk", comments, start_char, stop_char, lineno)
        self.body = body


"""
Left Hand Side expression.
"""


class Lhs(Expression):
    """Define a Lua Left Hand Side expression."""


class Name(Lhs):
    """Define a Lua name expression.

    Attributes:
        id (`string`): Id.
    """

    def __init__(
        self,
        identifier: str,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Name, self).__init__(
            "Name", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.id: str = identifier


class IndexNotation(Enum):
    DOT = 0  # obj.foo
    SQUARE = 1  # obj[foo]


class Index(Lhs):
    """Define a Lua index expression.

    Attributes:
        idx (`Expression`): Index expression.
        value (`string`): Id.
    """

    def __init__(
        self,
        idx: Expression,
        value: Name,
        notation: IndexNotation = IndexNotation.DOT,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Index, self).__init__(
            "Index", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.idx: Name = idx
        self.value: Expression = value
        self.notation: IndexNotation = notation


""" ----------------------------------------------------------------------- """
""" Statements                                                              """
""" ----------------------------------------------------------------------- """


class Assign(Statement):
    """Lua global assignment statement.

    Attributes:
        targets (`list<Node>`): List of targets.
        values (`list<Node>`): List of values.

    """

    def __init__(
        self,
        targets: List[Node],
        values: List[Node],
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Assign, self).__init__("Assign", comments, start_char, stop_char, lineno)
        self.targets: List[Node] = targets
        self.values: List[Node] = values


class LocalAssign(Assign):
    """Lua local assignment statement.

    Attributes:
        targets (`list<Node>`): List of targets.
        values (`list<Node>`): List of values.
    """

    def __init__(
        self,
        targets: List[Node],
        values: List[Node],
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(LocalAssign, self).__init__(
            targets, values, comments, start_char, stop_char, lineno
        )
        self._name: str = "LocalAssign"


class While(Statement):
    """Lua while statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        test: Expression,
        body: Block,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(While, self).__init__(
            "While", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.test: Expression = test
        self.body: Block = body


class Do(Statement):
    """Lua do end statement.

    Attributes:
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        body: Block,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Do, self).__init__(
            "Do", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.body: Block = body


class Repeat(Statement):
    """Lua repeat until statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        body: Block,
        test: Expression,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Repeat, self).__init__("Repeat", comments, start_char, stop_char, lineno)
        self.body: Block = body
        self.test: Expression = test


class ElseIf(Statement):
    """Define the elseif lua statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`list<Statement>`): List of statements to execute if test is true.
        orelse (`list<Statement> or ElseIf`): List of statements or ElseIf if test if false.
    """

    def __init__(
        self,
        test: Node,
        body: Block,
        orelse,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(ElseIf, self).__init__(
            "ElseIf", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.test: Node = test
        self.body: Block = body
        self.orelse = orelse


class If(Statement):
    """Lua if statement.

    Attributes:
        test (`Node`): Expression to test.
        body (`Block`): List of statements to execute if test is true.
        orelse (`list<Statement> or ElseIf`): List of statements or ElseIf if test if false.
    """

    def __init__(
        self,
        test: Expression,
        body: Block,
        orelse: List[Statement] or ElseIf,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(If, self).__init__("If", comments, start_char, stop_char, lineno)
        self.test: Expression = test
        self.body: Block = body
        self.orelse = orelse


class Label(Statement):
    """Define the label lua statement.

    Attributes:
        id (`Name`): Label name.
    """

    def __init__(
        self,
        label_id: Name,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Label, self).__init__(
            "Label", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.id: Name = label_id


class Goto(Statement):
    """Define the goto lua statement.

    Attributes:
        label (`Name`): Label node.
    """

    def __init__(
        self,
        label: Name,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Goto, self).__init__("Goto", comments, start_char, stop_char, lineno)
        self.label: Name = label


class SemiColon(Statement):
    """Define the semi-colon lua statement."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(SemiColon, self).__init__(
            "SemiColon", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


class Break(Statement):
    """Define the break lua statement."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Break, self).__init__(
            "Break", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


class Return(Statement):
    """Define the Lua return statement.

    Attributes:
        values (`list<Expression>`): Values to return.
    """

    def __init__(
        self,
        values,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Return, self).__init__(
            "Return", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.values = values


class Fornum(Statement):
    """Define the numeric for lua statement.

    Attributes:
        target (`Name`): Target name.
        start (`Expression`): Start index value.
        stop (`Expression`): Stop index value.
        step (`Expression`): Step value.
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        target: Name,
        start: Expression,
        stop: Expression,
        step: Expression,
        body: Block,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Fornum, self).__init__("Fornum", comments, start_char, stop_char, lineno)
        self.target: Name = target
        self.start: Expression = start
        self.stop: Expression = stop
        self.step: Expression = step
        self.body: Block = body


class Forin(Statement):
    """Define the for in lua statement.

    Attributes:
        body (`Block`): List of statements to execute.
        iter (`list<Expression>`): Iterable expressions.
        targets (`list<Name>`): Start index value.
    """

    def __init__(
        self,
        body: Block,
        iter: List[Expression],
        targets: List[Name],
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Forin, self).__init__("Forin", comments, start_char, stop_char, lineno)
        self.body: Block = body
        self.iter: List[Expression] = iter
        self.targets: List[Name] = targets


class Call(Statement):
    """Define the function call lua statement.

    Attributes:
        func (`Expression`): Function to call.
        args (`list<Expression>`): Function call arguments.
    """

    def __init__(
        self,
        func: Expression,
        args: List[Expression],
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Call, self).__init__("Call", comments, start_char, stop_char, lineno)
        self.func: Expression = func
        self.args: List[Expression] = args


class Invoke(Statement):
    """Define the invoke function call lua statement (magic syntax with ':').

    Attributes:
        source (`Expression`): Source expression where function is invoked.
        func (`Expression`): Function to call.
        args (`list<Expression>`): Function call arguments.
    """

    def __init__(
        self,
        source: Expression,
        func: Expression,
        args: List[Expression],
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Invoke, self).__init__(
            "Invoke", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.source: Expression = source
        self.func: Expression = func
        self.args: List[Expression] = args


class Function(Statement):
    """Define the Lua function declaration statement.

    Attributes:
        name (`Expression`): Function name.
        args (`list<Expression>`): Function arguments.
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        name: Expression,
        args: List[Expression],
        body: Block,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Function, self).__init__(
            "Function", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.name: Expression = name
        self.args: List[Expression] = args
        self.body: Block = body


class LocalFunction(Statement):
    """Define the Lua local function declaration statement.

    Attributes:
        name (`Expression`): Function name.
        args (`list<Expression>`): Function arguments.
        body (`list<Statement>`): List of statements to execute.
    """

    def __init__(
        self,
        name: Expression,
        args: List[Expression],
        body: Block,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(LocalFunction, self).__init__(
            "LocalFunction", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.name: Expression = name
        self.args: List[Expression] = args
        self.body: Block = body


class Method(Statement):
    """Define the Lua Object Oriented function statement.

    Attributes:
        source (`Expression`): Source expression where method is defined.
        name (`Expression`): Function name.
        args (`list<Expression>`): Function arguments.
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        source: Expression,
        name: Expression,
        args: List[Expression],
        body: Block,
        comments: Comments = None,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Method, self).__init__("Method", comments, start_char, stop_char, lineno)
        self.source: Expression = source
        self.name: Expression = name
        self.args: List[Expression] = args
        self.body: Block = body


""" ----------------------------------------------------------------------- """
""" Lua Expression                                                          """
""" ----------------------------------------------------------------------- """

""" ----------------------------------------------------------------------- """
""" Types and values                                                        """
""" ----------------------------------------------------------------------- """


class Nil(Expression):
    """Define the Lua nil expression."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Nil, self).__init__(
            "Nil", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


class TrueExpr(Expression):
    """Define the Lua true expression."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(TrueExpr, self).__init__(
            "True", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


class FalseExpr(Expression):
    """Define the Lua false expression."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(FalseExpr, self).__init__(
            "False", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


NumberType = int or float


class Number(Expression):
    """Define the Lua number expression.

    Attributes:
        n (`int|float`): Numeric value.
    """

    def __init__(
        self,
        n: NumberType,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Number, self).__init__(
            "Number", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.n: NumberType = n


class Varargs(Expression):
    """Define the Lua Varargs expression (...)."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Varargs, self).__init__(
            "Varargs", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


class StringDelimiter(Enum):
    SINGLE_QUOTE = 0  # 'foo'
    DOUBLE_QUOTE = 1  # "foo"
    DOUBLE_SQUARE = 2  # [[foo]]


class String(Expression):
    """Define the Lua string expression.

    Attributes:
        s (`string`): String value.
        delimiter (`StringDelimiter`): The string delimiter
    """

    def __init__(
        self,
        s: str,
        delimiter: StringDelimiter = StringDelimiter.SINGLE_QUOTE,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(String, self).__init__(
            "String", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.s: str = s
        self.delimiter: StringDelimiter = delimiter


class Field(Expression):
    """Define a lua table field expression

    Attributes:
        key (`Expression`): Key.
        value (`Expression`): Value.
    """

    def __init__(
        self,
        key: Expression,
        value: Expression,
        comments: Comments = None,
        between_brackets: bool = False,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Field, self).__init__("Field", comments, start_char, stop_char, lineno)
        self.key: Expression = key
        self.value: Expression = value
        self.between_brackets: bool = between_brackets


class Table(Expression):
    """Define the Lua table expression.

    Attributes:
        fields (`list<Field>`): Table fields.
    """

    def __init__(
        self,
        fields: List[Field],
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Table, self).__init__(
            "Table", start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.fields: List[Field] = fields


class Dots(Expression):
    """Define the Lua dots (...) expression."""

    def __init__(
        self,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Dots, self).__init__(
            "Dots", start_char=start_char, stop_char=stop_char, lineno=lineno
        )


class AnonymousFunction(Expression):
    """Define the Lua anonymous function expression.

    Attributes:
        args (`list<Expression>`): Function arguments.
        body (`Block`): List of statements to execute.
    """

    def __init__(
        self,
        args: List[Expression],
        body: Block,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(AnonymousFunction, self).__init__(
            "AnonymousFunction",
            start_char=start_char,
            stop_char=stop_char,
            lineno=lineno,
        )
        self.args: List[Expression] = args
        self.body: Block = body


""" ----------------------------------------------------------------------- """
""" Operators                                                               """
""" ----------------------------------------------------------------------- """


class Op(Expression):
    """Base class for Lua operators."""


class BinaryOp(Op):
    """Base class for Lua 'Left Op Right' Operators.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        name,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(BinaryOp, self).__init__(
            name, start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.left: Expression = left
        self.right: Expression = right


""" ----------------------------------------------------------------------- """
""" 3.4.1 – Arithmetic Operators                                            """
""" ----------------------------------------------------------------------- """


class AriOp(BinaryOp):
    """Base class for Arithmetic Operators"""


class AddOp(AriOp):
    """Add expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(AddOp, self).__init__("AddOp", left, right, start_char, stop_char, lineno)


class SubOp(AriOp):
    """Substract expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(SubOp, self).__init__("SubOp", left, right, start_char, stop_char, lineno)


class MultOp(AriOp):
    """Multiplication expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(MultOp, self).__init__(
            "MultOp", left, right, start_char, stop_char, lineno
        )


class FloatDivOp(AriOp):
    """Float division expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(FloatDivOp, self).__init__(
            "FloatDivOp", left, right, start_char, stop_char, lineno
        )


class FloorDivOp(AriOp):
    """Floor division expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(FloorDivOp, self).__init__(
            "FloorDivOp", left, right, start_char, stop_char, lineno
        )


class ModOp(AriOp):
    """Modulo expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(ModOp, self).__init__("ModOp", left, right, start_char, stop_char, lineno)


class ExpoOp(AriOp):
    """Exponent expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(ExpoOp, self).__init__(
            "ExpoOp", left, right, start_char, stop_char, lineno
        )


""" ----------------------------------------------------------------------- """
""" 3.4.2 – Bitwise Operators                                               """
""" ----------------------------------------------------------------------- """


class BitOp(BinaryOp):
    """Base class for bitwise Operators."""


class BAndOp(BitOp):
    """Bitwise and expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(BAndOp, self).__init__(
            "BAndOp", left, right, start_char, stop_char, lineno
        )


class BOrOp(BitOp):
    """Bitwise or expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(BOrOp, self).__init__("BOrOp", left, right, start_char, stop_char, lineno)


class BXorOp(BitOp):
    """Bitwise xor expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(BXorOp, self).__init__(
            "BXorOp", left, right, start_char, stop_char, lineno
        )


class BShiftROp(BitOp):
    """Bitwise right shift expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(BShiftROp, self).__init__(
            "BShiftROp", left, right, start_char, stop_char, lineno
        )


class BShiftLOp(BitOp):
    """Bitwise left shift expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(BShiftLOp, self).__init__(
            "BShiftLOp", left, right, start_char, stop_char, lineno
        )


""" ----------------------------------------------------------------------- """
""" 3.4.4 – Relational Operators                                            """
""" ----------------------------------------------------------------------- """


class RelOp(BinaryOp):
    """Base class for Lua relational operators."""


class LessThanOp(RelOp):
    """Less than expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(LessThanOp, self).__init__(
            "RLtOp", left, right, start_char, stop_char, lineno
        )


class GreaterThanOp(RelOp):
    """Greater than expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(GreaterThanOp, self).__init__(
            "RGtOp", left, right, start_char, stop_char, lineno
        )


class LessOrEqThanOp(RelOp):
    """Less or equal expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(LessOrEqThanOp, self).__init__(
            "RLtEqOp", left, right, start_char, stop_char, lineno
        )


class GreaterOrEqThanOp(RelOp):
    """Greater or equal expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(GreaterOrEqThanOp, self).__init__(
            "RGtEqOp", left, right, start_char, stop_char, lineno
        )


class EqToOp(RelOp):
    """Equal to expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(EqToOp, self).__init__(
            "REqOp", left, right, start_char, stop_char, lineno
        )


class NotEqToOp(RelOp):
    """Not equal to expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(NotEqToOp, self).__init__(
            "RNotEqOp", left, right, start_char, stop_char, lineno
        )


""" ----------------------------------------------------------------------- """
""" 3.4.5 – Logical Operators                                               """
""" ----------------------------------------------------------------------- """


class LoOp(BinaryOp):
    """Base class for logical operators."""


class AndLoOp(LoOp):
    """Logical and expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(AndLoOp, self).__init__(
            "LAndOp", left, right, start_char, stop_char, lineno
        )


class OrLoOp(LoOp):
    """Logical or expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(OrLoOp, self).__init__(
            "LOrOp", left, right, start_char, stop_char, lineno
        )


""" ----------------------------------------------------------------------- """
""" 3.4.6 Concat operators                                                  """
""" ----------------------------------------------------------------------- """


class Concat(BinaryOp):
    """Concat expression.

    Attributes:
        left (`Expression`): Left expression.
        right (`Expression`): Right expression.
    """

    def __init__(
        self,
        left: Expression,
        right: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(Concat, self).__init__(
            "Concat", left, right, start_char, stop_char, lineno
        )


""" ----------------------------------------------------------------------- """
""" Unary operators                                                         """
""" ----------------------------------------------------------------------- """


class UnaryOp(Expression):
    """Base class for Lua unitary operator.

    Attributes:
        operand (`Expression`): Operand.
    """

    def __init__(
        self,
        name: str,
        operand: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(UnaryOp, self).__init__(
            name, start_char=start_char, stop_char=stop_char, lineno=lineno
        )
        self.operand = operand


class UMinusOp(UnaryOp):
    """Lua minus unitary operator.

    Attributes:
        operand (`Expression`): Operand.
    """

    def __init__(
        self,
        operand: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(UMinusOp, self).__init__(
            "UMinusOp", operand, start_char, stop_char, lineno
        )


class UBNotOp(UnaryOp):
    """Lua binary not unitary operator.

    Attributes:
        operand (`Expression`): Operand.
    """

    def __init__(
        self,
        operand: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(UBNotOp, self).__init__("UBNotOp", operand, start_char, stop_char, lineno)


class ULNotOp(UnaryOp):
    """Logical not operator.

    Attributes:
        operand (`Expression`): Operand.
    """

    def __init__(
        self,
        operand: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(ULNotOp, self).__init__("ULNotOp", operand, start_char, stop_char, lineno)


""" ----------------------------------------------------------------------- """
""" 3.4.7 – The Length Operator                                             """
""" ----------------------------------------------------------------------- """


class ULengthOP(UnaryOp):
    """Length operator."""

    def __init__(
        self,
        operand: Expression,
        start_char: Optional[int] = None,
        stop_char: Optional[int] = None,
        lineno: Optional[int] = None,
    ):
        super(ULengthOP, self).__init__(
            "ULengthOp", operand, start_char, stop_char, lineno
        )
