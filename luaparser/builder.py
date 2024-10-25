import ast
import re
from typing import Literal, TypeVar
from typing import Tuple

from antlr4 import InputStream, CommonTokenStream, ParserRuleContext
from antlr4.Token import Token
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

from luaparser.astnodes import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaParser import LuaParser
from luaparser.parser.LuaParserVisitor import LuaParserVisitor

TNode = TypeVar("TNode", bound=Node)


class SyntaxException(Exception):
    def __init__(self, user_msg, token=None):
        if token:
            message = (
                "(" + str(token.line) + "," + str(token.start) + "): Error: " + user_msg
            )
        else:
            message = "Error: " + user_msg
        super().__init__(message)


class Expr(Enum):
    OR = 1
    AND = 2
    REL = 3
    CONCAT = 4
    ADD = 5
    MULT = 6
    BITWISE = 7
    UNARY = 8
    POW = 9
    ATOM = 10


class Tokens:
    AND = 1
    BREAK = 2
    DO = 3
    ELSETOK = 4
    ELSEIF = 5
    END = 6
    FALSE = 7
    FOR = 8
    FUNCTION = 9
    GOTO = 10
    IFTOK = 11
    IN = 12
    LOCAL = 13
    NIL = 14
    NOT = 15
    OR = 16
    REPEAT = 17
    RETURN = 18
    THEN = 19
    TRUE = 20
    UNTIL = 21
    WHILE = 22
    ADD = 23
    MINUS = 24
    MULT = 25
    DIV = 26
    FLOOR = 27
    MOD = 28
    POW = 29
    LENGTH = 30
    EQ = 31
    NEQ = 32
    LTEQ = 33
    GTEQ = 34
    LT = 35
    GT = 36
    ASSIGN = 37
    BITAND = 38
    BITOR = 39
    BITNOT = 40
    BITRSHIFT = 41
    BITRLEFT = 42
    OPAR = 43
    CPAR = 44
    OBRACE = 45
    CBRACE = 46
    OBRACK = 47
    CBRACK = 48
    COLCOL = 49
    COL = 50
    COMMA = 51
    VARARGS = 52
    CONCAT = 53
    DOT = 54
    SEMCOL = 55
    NAME = 56
    NUMBER = 57
    STRING = 58
    COMMENT = 59
    LINE_COMMENT = 60
    SPACE = 61
    NEWLINE = 62
    SHEBANG = 63
    LongBracket = 64


LITERAL_NAMES = [
    "<INVALID>",
    "'and'",
    "'break'",
    "'do'",
    "'else'",
    "'elseif'",
    "'end'",
    "'false'",
    "'for'",
    "'function'",
    "'goto'",
    "'if'",
    "'in'",
    "'local'",
    "'nil'",
    "'not'",
    "'or'",
    "'repeat'",
    "'return'",
    "'then'",
    "'true'",
    "'until'",
    "'while'",
    "'+'",
    "'-'",
    "'*'",
    "'/'",
    "'//'",
    "'%'",
    "'^'",
    "'#'",
    "'=='",
    "'~='",
    "'<='",
    "'>='",
    "'<'",
    "'>'",
    "'='",
    "'&'",
    "'|'",
    "'~'",
    "'>>'",
    "'<<'",
    "'('",
    "')'",
    "'{'",
    "'}'",
    "'['",
    "']'",
    "'::'",
    "':'",
    "','",
    "'...'",
    "'..'",
    "'.'",
    "';'",
    "NAME",
    "NUMBER",
    "STRING",
    "COMMENT",
    "LINE_COMMENT",
    "SPACE",
    "NEWLINE",
    "SHEBANG",
    "LONG_BRACKET",
]


def _listify(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj


class Builder:
    CLOSING_TOKEN = [Tokens.END, Tokens.CBRACE, Tokens.CPAR]

    HIDDEN_TOKEN = [
        Tokens.SHEBANG,
        Tokens.LINE_COMMENT,
        Tokens.COMMENT,
        Tokens.NEWLINE,
        Tokens.SPACE,
        -2,
    ]

    REL_OPERATORS = [
        Tokens.LT,
        Tokens.GT,
        Tokens.LTEQ,
        Tokens.GTEQ,
        Tokens.NEQ,
        Tokens.EQ,
    ]

    def __init__(self, source):
        self._stream = CommonTokenStream(LuaLexer(InputStream(source)))
        # contains a list of CommonTokens
        self._line_count: int = 0
        self._right_index: int = 0
        self._last_expr_type: Optional[int] = None

        # following stack are used to backup values
        self._index_stack: List[int] = []
        self._right_index_stack: List[int] = []
        self.text: str = ""  # last token text
        self.type: int = -1  # last token type

        # contains expected token in case of invalid input code
        self._expected = []

        # comments waiting to be inserted into ast nodes
        self._comments_index_stack: List[int] = []
        self.comments: List[Comment] = []
        self._hidden_handled: bool = False
        self._hidden_handled_stack: List[bool] = []

    @property
    def _LT(self) -> CommonToken:
        """Last token that was consumed in next_i*_* method."""
        return self._stream.LT(-1)

    def process(self) -> Chunk:
        node = self.parse_chunk()

        if not node:
            raise SyntaxException("Expecting a chunk")
        return node

    def save(self):
        # logging.debug('trying ' + inspect.stack()[1][3])
        self._index_stack.append(self._stream.index)
        self._right_index_stack.append(self._right_index)
        self._comments_index_stack.append(len(self.comments))
        self._hidden_handled_stack.append(self._hidden_handled)

    def success(self):
        self._index_stack.pop()
        self._right_index_stack.pop()
        self._comments_index_stack.pop()
        self._hidden_handled_stack.pop()
        return True

    def failure(self):
        self._stream.seek(self._index_stack.pop())
        self._right_index = self._right_index_stack.pop()
        self._hidden_handled = self._hidden_handled_stack.pop()
        n_elem_to_delete = len(self.comments) - self._comments_index_stack.pop()
        if n_elem_to_delete >= 1:
            del self.comments[-n_elem_to_delete:]
        return False

    def failure_save(self):
        self._stream.seek(self._index_stack.pop())
        self._right_index = self._right_index_stack.pop()
        self._hidden_handled = self._hidden_handled_stack.pop()
        n_elem_to_delete = len(self.comments) - self._comments_index_stack.pop()
        if n_elem_to_delete >= 1:
            del self.comments[-n_elem_to_delete:]

        self._index_stack.append(self._stream.index)
        self._right_index_stack.append(self._right_index)
        self._comments_index_stack.append(len(self.comments))
        self._hidden_handled_stack.append(self._hidden_handled)

    def next_is_rc(
        self, type_to_seek: int, hidden_right: bool = True
    ) -> Optional[Token]:
        token = self._stream.LT(1)
        tok_type: int = token.type
        self._right_index = self._stream.index

        if tok_type == type_to_seek:
            self.text = token.text
            self.type = tok_type
            self._stream.consume()
            self._hidden_handled = False
            if hidden_right:
                self.handle_hidden_right()
            return token
        self._expected.append(type_to_seek)
        return None

    def next_is_c(self, type_to_seek: int, hidden_right: bool = True) -> bool:
        token = self._stream.LT(1)
        tok_type: int = token.type
        self._right_index = self._stream.index

        if tok_type == type_to_seek:
            self._stream.consume()
            self._hidden_handled = False
            if hidden_right:
                self.handle_hidden_right()
            return True
        self._expected.append(type_to_seek)
        return False

    def next_is(self, type_to_seek) -> bool:
        if self._stream.LT(1).type == type_to_seek:
            return True
        else:
            self._expected.append(type_to_seek)
            return False

    def prev_is(self, type_to_seek) -> bool:
        return self._stream.LT(-1).type == type_to_seek

    def next_in_rc(self, types: List[int], hidden_right: bool = True) -> bool:
        token = self._stream.LT(1)
        tok_type: int = token.type
        self._right_index = self._stream.index

        if tok_type in types:
            self.type = tok_type
            self._stream.consume()
            self._hidden_handled = False
            if hidden_right:
                self.handle_hidden_right()
            return True
        self._expected.extend(types)
        return False

    def next_in(self, types: List[int]) -> bool:
        if self._stream.LT(1).type in types:
            return True
        else:
            self._expected.extend(types)
            return False

    def handle_hidden_left(self) -> None:
        if self._hidden_handled:
            return
        tokens = self._stream.getHiddenTokensToLeft(self._stream.index)
        if tokens:
            for t in tokens:
                if t.type == Tokens.LINE_COMMENT:
                    self.comments.append(
                        Comment(
                            t.text,
                            first_token=t,
                            last_token=t,
                        )
                    )
                elif t.type == Tokens.COMMENT:
                    self.comments.append(
                        Comment(
                            t.text,
                            True,
                            first_token=t,
                            last_token=t,
                        )
                    )
                elif t.type == Tokens.NEWLINE:
                    # append n time a None value (indicate newline)
                    self.comments += t.text.count("\n") * [None]

        self._hidden_handled = True

    def handle_hidden_right(self) -> None:
        if self._hidden_handled:
            return
        tokens = self._stream.getHiddenTokensToRight(self._right_index)
        if tokens:
            for t in tokens:
                if t.type == Tokens.LINE_COMMENT:
                    self.comments.append(
                        Comment(
                            t.text,
                            first_token=t,
                            last_token=t,
                        )
                    )
                elif t.type == Tokens.COMMENT:
                    self.comments.append(
                        Comment(
                            t.text,
                            True,
                            first_token=t,
                            last_token=t,
                        )
                    )
                elif t.type == Tokens.NEWLINE:
                    # append n time a None value (indicate newline)
                    self.comments += t.text.count("\n") * [None]

        self._hidden_handled = True

    def get_comments(self) -> Comments:
        comments = [c for c in self.comments if c is not None]
        self.comments = []
        return comments

    def get_comments_followed_by_blank_line(self) -> Comments:
        """Returns comments followed by a blank line."""
        if not self.comments:
            return []

        idx = 0
        comments: List[Comment] = []

        # search first comment
        while idx < len(self.comments) and self.comments[idx] is None:
            idx += 1
        # get comments starting from this index
        while idx < len(self.comments) and self.comments[idx] is not None:
            comments.append(self.comments[idx])
            idx += 1
        # check if followed by a blank line
        if idx + 1 < len(self.comments):
            if self.comments[idx] is None and self.comments[idx + 1] is None:
                # clean list
                self.comments = self.comments[idx + 2:]
                return comments
        return []

    def get_inline_comment(self) -> Comment or None:
        if self.comments:
            c = self.comments.pop(0)
            if c is None:
                return None
            else:
                return c
        return None

    def has_newline_before(self) -> bool:
        return None in self.comments

    def abort(self) -> None:
        types_str = []
        token = self._stream.LT(2)
        expected = set(self._expected)
        for type_to_seek in expected:
            types_str.append(LITERAL_NAMES[type_to_seek])

        raise SyntaxException(
            "Expecting one of "
            + ", ".join(types_str)
            + " at line "
            + str(token.line)
            + ", column "
            + str(token.column)
        )

    def parse_chunk(self) -> Chunk or None:
        first_token: Token = self._stream.LT(1)
        self.handle_hidden_left()
        comments = self.get_comments_followed_by_blank_line()
        block = self.parse_block()
        if block:
            token = self._stream.LT(1)
            if token.type == -1:
                # do not consume EOF
                return Chunk(
                    block,
                    comments=comments,
                    first_token=first_token,
                    last_token=self._LT,
                )
        return False

    def parse_block(self) -> Block:
        t: Token = self._stream.LT(1)
        statements = []

        while True:
            stat = self.parse_stat()
            if not stat:
                break
            statements.append(stat)

        # optional ret stat
        stat = self.parse_ret_stat()
        if stat:
            statements.append(stat)

        # force handle trailing hidden tokens after block
        self._hidden_handled = False
        self.handle_hidden_right()
        return Block(
            statements,
            first_token=t,
            last_token=statements[-1].last_token if statements else None,
            comments=self.get_comments(),
        )

    def parse_stat(self) -> Statement or None:
        comments = self.get_comments()

        stat = (
            self.parse_assignment()
            or self.parse_var(is_statement=True)
            or self.parse_while_stat()
            or self.parse_repeat_stat()
            or self.parse_local()
            or self.parse_goto_stat()
            or self.parse_if_stat()
            or self.parse_for_stat()
            or self.parse_function()
            or self.parse_label()
        )

        if stat:
            stat.comments = comments
            return stat

        stat = self.parse_do_block()
        if stat:
            self.handle_hidden_right()
            return Do(stat)

        if self.next_is(Tokens.BREAK) and self.next_is_rc(Tokens.BREAK):
            self.handle_hidden_right()
            return Break()
        if self.next_is(Tokens.SEMCOL) and self.next_is_rc(Tokens.SEMCOL):
            self.handle_hidden_right()
            return SemiColon()

        return None

    def parse_ret_stat(self) -> Return or bool:
        self.save()
        if self.next_is_rc(Tokens.RETURN):
            t: Token = self._LT
            expr_list = self.parse_expr_list()  # optional
            # consume optional token
            if self.next_is(Tokens.SEMCOL):
                self.next_is_rc(Tokens.SEMCOL)

            self.success()
            return Return(expr_list, first_token=t, last_token=self._LT)
        return self.failure()

    def parse_assignment(self) -> Assign or bool:
        self.save()
        t: Token = self._stream.LT(1)
        targets = self.parse_var_list()
        if targets:
            if self.next_is_rc(Tokens.ASSIGN):
                values = self.parse_expr_list()
                if values:
                    self.success()
                    return Assign(
                        targets,
                        values,
                        first_token=t,
                        last_token=self._LT,
                    )
                else:
                    self.abort()

        return self.failure()

    def parse_var_list(self) -> List[Expression] or bool:
        lua_vars = []
        self.save()
        var = self.parse_var()
        if var:
            lua_vars.append(var)
            while True:
                self.save()
                if self.next_is_rc(Tokens.COMMA):
                    var = self.parse_var()
                    if var:
                        lua_vars.append(var)
                        self.success()
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return lua_vars
        return self.failure()

    # When is_statement is true, root must be a Statement.
    def parse_var(self, is_statement=False) -> Node or bool:
        self.save()
        root = self.parse_callee()
        if root:
            tail = self.parse_tail()
            while tail:
                tail.first_token = root.first_token

                if isinstance(tail, Call):
                    tail.func = root
                elif isinstance(tail, Index):
                    tail.value = root
                elif isinstance(tail, Invoke):
                    tail.source = root
                else:
                    args = _listify(tail)
                    tail = Call(
                        root,
                        args,
                        first_token=root.first_token,
                        last_token=args[-1].last_token if args else None,
                    )
                root = tail

                tail = self.parse_tail()
                if tail:
                    self.handle_hidden_right()
            if is_statement and not isinstance(root, Statement):
                return self.failure()
            self.handle_hidden_right()
            self.success()
            return root

        return self.failure()

    def parse_tail(self) -> Node or bool:
        # do not render last hidden
        self.save()
        if self.next_is_rc(Tokens.DOT) and self.next_is_rc(Tokens.NAME, False):
            self.success()
            return Index(
                Name(
                    self.text,
                    first_token=self._LT,
                    last_token=self._LT,
                ),
                # value must be set in parent
                Name(""),
                last_token=self._LT,
            )

        self.failure_save()
        if self.next_is_rc(Tokens.OBRACK):
            expr = self.parse_expr()
            if expr and self.next_is_rc(Tokens.CBRACK, False):
                self.success()
                return Index(
                    expr,
                    Name(""),
                    notation=IndexNotation.SQUARE,
                    # value must be set in parent
                )

        self.failure_save()
        if self.next_is_rc(Tokens.COL) and self.next_is_rc(Tokens.NAME):
            name = Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
            if self.next_is_rc(Tokens.OPAR):
                expr_list = self.parse_expr_list() or []
                if self.next_is_rc(Tokens.CPAR, False):
                    self.success()
                    # noinspection PyTypeChecker
                    return Invoke(None, name, expr_list)

        self.failure_save()
        if self.next_is_rc(Tokens.COL) and self.next_is_rc(Tokens.NAME):
            name = Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
            table = self.parse_table_constructor(False)
            if table:
                self.success()
                # noinspection PyTypeChecker
                return Invoke(None, name, [table])

        self.failure_save()
        if self.next_is_rc(Tokens.COL) and self.next_is_rc(Tokens.NAME):
            name = Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
            if self.next_is_rc(Tokens.STRING, False):
                string = self.parse_lua_str(self.text, self._LT)
                self.success()
                # noinspection PyTypeChecker
                return Invoke(None, name, [string])

        self.failure_save()
        if self.next_is(Tokens.OPAR):
            # handle the ambiguous syntax
            # http://lua-users.org/lists/lua-l/2009-08/msg00543.html
            # example:
            #   a = b + c;
            #   (print or io.write)('foo')

            # check if a newline is present before OPAR
            tokens = self._stream.getHiddenTokensToLeft(self._stream.index)
            if tokens:
                for t in tokens:
                    if t.type == Tokens.NEWLINE and not self.prev_is(Tokens.SEMCOL):
                        raise SyntaxException(
                            "Ambiguous syntax detected", self._stream.LT(-1)
                        )

        if self.next_is_rc(Tokens.OPAR, False):
            self.handle_hidden_right()
            expr_list = self.parse_expr_list() or []
            if self.next_is_rc(Tokens.CPAR, False):
                self.success()
                # noinspection PyTypeChecker
                return Call(None, expr_list, last_token=self._LT)

        self.failure_save()
        table = self.parse_table_constructor(False)
        if table:
            self.success()
            return table

        self.failure_save()
        if self.next_is_rc(Tokens.STRING, False):
            string = self.parse_lua_str(self.text, self._LT)
            self.success()
            return string

        return self.failure()

    def parse_expr_list(self) -> List[Expression] or bool:
        expr_list: List[Expression] = []
        self.save()
        expr = self.parse_expr()
        if expr:
            expr_list.append(expr)
            while True:
                self.save()
                if self.next_is_rc(Tokens.COMMA):
                    self._expected = []
                    expr = self.parse_expr()
                    if expr:
                        expr_list.append(expr)
                        self.success()
                    else:
                        # a comma is alone at the end
                        self.failure()
                        self.failure()
                        self.abort()
                else:
                    self.failure()
                    break
            self.success()
            return expr_list
        return self.failure()

    def parse_do_block(self) -> Block or bool:
        self.save()
        if self.next_is_rc(Tokens.DO, False):
            t: Token = self._LT
            self.handle_hidden_right()
            block = self.parse_block()
            if block:
                if self.next_is_rc(Tokens.END):
                    block.first_token = t
                    block.last_token = self._LT
                    self.success()
                    return block
        return self.failure()

    def parse_while_stat(self) -> While or bool:
        self.save()
        first_token = self._stream.LT(1)
        if self.next_is_rc(Tokens.WHILE):
            self._expected = []
            expr = self.parse_expr()
            if expr:
                self._expected = []
                body = self.parse_do_block()
                if body:
                    self.success()
                    return While(expr, body, first_token=first_token, last_token=body.last_token)
            self.abort()

        return self.failure()

    def parse_repeat_stat(self) -> Repeat or bool:
        self.save()
        first_token = self._stream.LT(1)
        if self.next_is_rc(Tokens.REPEAT, False):
            self.handle_hidden_right()
            body = self.parse_block()
            if body:
                if self.next_is_rc(Tokens.UNTIL):
                    expr = self.parse_expr()
                    if expr:
                        self.success()
                        return Repeat(body, expr, first_token=first_token, last_token=expr.last_token)

        return self.failure()

    def parse_local(self) -> Node or bool:
        self.save()
        self._expected = []
        start_token = self.next_is_rc(Tokens.LOCAL)
        if start_token:
            targets = self.parse_name_list()
            if targets:
                values = []
                self.save()
                if self.next_is_rc(Tokens.ASSIGN):
                    values = self.parse_expr_list()
                    if values:
                        self.success()
                    else:
                        self.failure()
                        self.failure()
                        self.abort()
                else:
                    self.failure()

                self.success()
                return LocalAssign(
                    targets,
                    values,
                    first_token=start_token,
                    last_token=values[-1].last_token if values else None,
                )

            self.save()

            if self.next_is_rc(Tokens.FUNCTION) and self.next_is_rc(Tokens.NAME):
                name = Name(
                    self.text,
                    first_token=self._LT,
                    last_token=self._LT,
                )
                body = self.parse_func_body()
                if body:
                    self.success()
                    self.success()
                    node = LocalFunction(name, body[0], body[1])
                    self.handle_hidden_right()
                    node.first_token = start_token
                    node.last_token = body[1].last_token
                    return node
            self.failure()
            self.abort()

        return self.failure()

    def parse_goto_stat(self) -> Goto or bool:
        self.save()
        if self.next_is_rc(Tokens.GOTO) and self.next_is_rc(Tokens.NAME):
            self.success()
            return Goto(
                Name(
                    self.text,
                    first_token=self._LT,
                    last_token=self._LT,
                )
            )
        return self.failure()

    def parse_if_stat(self) -> If or bool:
        self.save()
        first_token = self._stream.LT(1)
        if self.next_is_rc(Tokens.IFTOK):
            self._expected = []
            test = self.parse_expr()
            if test:
                if self.next_is_rc(Tokens.THEN, False):
                    self.handle_hidden_right()
                    body = self.parse_block()
                    if body:
                        main = If(test, body, None, first_token=first_token)
                        root = main
                        while True:  # zero or more
                            orelse = self.parse_elseif_stat()
                            if not orelse:
                                break
                            else:
                                root.orelse = orelse
                                root = orelse

                        else_exp = self.parse_else_stat()  # optional
                        if else_exp:
                            root.orelse = else_exp
                        last_token = self._stream.LT(1)
                        if self.next_is_rc(Tokens.END):
                            main.last_token = last_token
                            self.success()
                            return main
            self.abort()
        return self.failure()

    def parse_elseif_stat(self) -> ElseIf or bool:
        self.save()
        first_token = self._stream.LT(1)
        if self.next_is_rc(Tokens.ELSEIF):
            test = self.parse_expr()
            if test:
                if self.next_is_rc(Tokens.THEN, False):
                    self.handle_hidden_right()
                    body = self.parse_block()
                    if body:
                        self.success()
                        return ElseIf(test, body, None, first_token=first_token,
                                      last_token=body.last_token)  # orelse will be set in parent
        return self.failure()

    def parse_else_stat(self) -> Block or bool:
        self.save()
        if self.next_is(Tokens.ELSETOK):
            if self.next_is_rc(Tokens.ELSETOK, False):
                self.handle_hidden_right()
                body = self.parse_block()
                if body:
                    self.success()
                    return body
        return self.failure()

    def parse_for_stat(self) -> Fornum or Forin or bool:
        self.save()
        first_token = self._stream.LT(1)
        if self.next_is_rc(Tokens.FOR):
            self.save()
            if self.next_is_rc(Tokens.NAME):
                target = Name(
                    self.text,
                    first_token=self._LT,
                    last_token=self._LT,
                )
                if self.next_is_rc(Tokens.ASSIGN):
                    start = self.parse_expr()
                    if start and self.next_is_rc(Tokens.COMMA):
                        stop = self.parse_expr()
                        if stop:
                            step = 1
                            # optional step
                            if self.next_is(Tokens.COMMA) and self.next_is_rc(
                                Tokens.COMMA
                            ):
                                step = self.parse_expr()

                            body = self.parse_do_block()
                            if not body:
                                self.failure()
                                return self.failure()
                            self.success()
                            self.success()
                            return Fornum(target, start, stop, step, body, first_token=first_token,
                                          last_token=body.last_token)

            self.failure_save()
            target = self.parse_name_list()
            if target and self.next_is_rc(Tokens.IN):
                iter_expr = self.parse_expr_list()
                if iter_expr:
                    body = self.parse_do_block()
                    if body:
                        self.success()
                        self.success()
                        return Forin(body, iter_expr, target, first_token=first_token, last_token=body.last_token)
            self.failure()

        return self.failure()

    def parse_function(self) -> Method or Function or bool:
        self.save()
        self._expected = []
        start_token = self.next_is_rc(Tokens.FUNCTION)
        if start_token:
            names = self.parse_names()
            if names:
                self.save()
                if self.next_is_rc(Tokens.COL) and self.next_is_rc(Tokens.NAME):
                    name = Name(
                        self.text,
                        first_token=self._LT,
                        last_token=self._LT,
                    )
                    func_body = self.parse_func_body()
                    if func_body:
                        self.success()
                        self.success()
                        node = Method(
                            names,
                            name,
                            func_body[0],
                            func_body[1],
                            first_token=start_token,
                            last_token=func_body[1].last_token,
                        )
                        self.handle_hidden_right()
                        return node

                self.failure()

                func_body = self.parse_func_body()
                if func_body:
                    self.success()
                    node = Function(
                        names,
                        func_body[0],
                        func_body[1],
                        first_token=start_token,
                        last_token=func_body[1].last_token,
                    )
                    self.handle_hidden_right()
                    return node
            self.abort()

        return self.failure()

    def parse_names(self) -> Name or Index or bool:
        self.save()
        if self.next_is_rc(Tokens.NAME):
            root = Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
            while True:
                self.save()
                if self.next_is_rc(Tokens.DOT) and self.next_is_rc(Tokens.NAME):
                    self.success()
                    child = Index(
                        Name(
                            self.text,
                            first_token=self._LT,
                            last_token=self._LT,
                        ),
                        root,
                    )
                    root = child
                else:
                    self.failure()
                    break
            self.success()
            return root
        self.failure()

    def parse_func_body(self):
        """If success, return a tuple (args, body)"""
        self.save()
        self._expected = []
        if self.next_is_rc(Tokens.OPAR, False):  # do not render right hidden
            self.handle_hidden_right()  # render hidden after new level
            args = self.parse_param_list()
            if args is not None:  # may be an empty table
                if self.next_is_rc(Tokens.CPAR, False):  # do not render right hidden
                    self.handle_hidden_right()  # render hidden after new level
                    body = self.parse_block()
                    if body:
                        self._expected = []
                        token = self.next_is_rc(Tokens.END, False)
                        if token:
                            body.last_token = token
                            self.success()
                            return args, body
                        else:
                            self.abort()
                else:
                    self.abort()
        return self.failure()

    def parse_param_list(self) -> List[Expression] or bool:
        param_list: List[Expression] = self.parse_name_list()
        if param_list:
            self.save()
            if self.next_is_rc(Tokens.COMMA) and self.next_is_rc(Tokens.VARARGS):
                t: Token = self._LT
                self.success()
                param_list.append(Varargs(first_token=t, last_token=t))
                return param_list
            else:
                self.failure()
                return param_list

        self.save()
        if self.next_is_rc(Tokens.VARARGS):
            t: Token = self._LT
            self.success()
            return [Varargs(first_token=t, last_token=t)]

        self.success()
        return []

    def parse_name_list(self) -> List[Name] or bool:
        self.save()
        names: List[Name] = []
        if self.next_is_rc(Tokens.NAME):
            names.append(
                Name(
                    self.text,
                    first_token=self._LT,
                    last_token=self._LT,
                )
            )
            while True:
                self.save()
                if self.next_is_rc(Tokens.COMMA) and self.next_is_rc(Tokens.NAME):
                    names.append(
                        Name(
                            self.text,
                            first_token=self._LT,
                            last_token=self._LT,
                        )
                    )
                    self.success()
                else:
                    self.failure()
                    break
            self.success()
            return names
        return self.failure()

    def parse_label(self) -> Label or bool:
        self.save()
        if self.next_is_rc(Tokens.COLCOL) and self.next_is_rc(Tokens.NAME):
            name = Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
            if self.next_is_rc(Tokens.COLCOL):
                t: Token = self._LT
                self.success()
                return Label(name, first_token=t, last_token=t)

        return self.failure()

    def parse_callee(self) -> Expression or bool:
        self.save()
        if self.next_is_rc(Tokens.OPAR):
            expr = self.parse_expr()
            if expr:
                if self.next_is_rc(Tokens.CPAR):
                    self.success()
                    expr.wrapped = True
                    return expr
        self.failure()
        self.save()
        if self.next_is_rc(Tokens.NAME):
            self.success()
            return Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
        return self.failure()

    def parse_expr(self) -> Expression or bool:
        return self.parse_or_expr()

    def parse_or_expr(self) -> Expression or Literal[False]:
        self.save()
        left = self.parse_and_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.OR):
                    right = self.parse_and_expr()
                    if right:
                        self.success()
                        left = OrLoOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_and_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_rel_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.AND):
                    right = self.parse_rel_expr()
                    if right:
                        self.success()
                        left = AndLoOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_rel_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_bit_or_expr()
        if left:
            self.save()
            if self.next_in_rc(self.REL_OPERATORS):
                op = self.type
                right = self.parse_bit_or_expr()
                if right:
                    self.success()
                    if op == Tokens.LT:
                        left = LessThanOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    elif op == Tokens.GT:
                        left = GreaterThanOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    elif op == Tokens.LTEQ:
                        left = LessOrEqThanOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    elif op == Tokens.GTEQ:
                        left = GreaterOrEqThanOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    elif op == Tokens.NEQ:
                        left = NotEqToOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    elif op == Tokens.EQ:
                        left = EqToOp(left, right, first_token=left.first_token, last_token=right.last_token)
                else:
                    self.failure()
                    return self.failure()
            else:
                self.failure()
            self.success()
            return left
        return self.failure()

    def parse_bit_or_expr(self) -> Expression or Literal[False]:
        self.save()
        left = self.parse_bit_not_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.BITOR):
                    right = self.parse_bit_not_expr()
                    if right:
                        self.success()
                        left = BOrOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_bit_not_expr(self) -> Expression or Literal[False]:
        self.save()
        left = self.parse_bit_and_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.BITNOT):
                    right = self.parse_bit_and_expr()
                    if right:
                        self.success()
                        left = BXorOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_bit_and_expr(self) -> Expression or Literal[False]:
        self.save()
        left = self.parse_bit_shift_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.BITAND):
                    right = self.parse_bit_shift_expr()
                    if right:
                        self.success()
                        left = BAndOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_bit_shift_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_concat_expr()
        if left:
            while True:
                self.save()
                if self.next_in_rc(
                    [
                        Tokens.BITRSHIFT,
                        Tokens.BITRLEFT,
                    ]
                ):
                    op = self.type
                    right = self.parse_concat_expr()
                    if right:
                        self.success()
                        if op == Tokens.BITRSHIFT:
                            left = BShiftROp(left, right)
                        elif op == Tokens.BITRLEFT:
                            left = BShiftLOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_concat_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_add_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.CONCAT):
                    self._expected = []
                    right = self.parse_add_expr()
                    if right:
                        self.success()
                        left = Concat(left, right, first_token=left.first_token, last_token=right.last_token)
                    else:
                        self.failure()
                        self.failure()
                        self.abort()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_add_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_mult_expr()
        if left:
            while True:
                self.save()
                if self.next_in_rc([Tokens.ADD, Tokens.MINUS]):
                    op = self.type
                    right = self.parse_mult_expr()
                    if right:
                        self.success()
                        if op == Tokens.ADD:
                            left = AddOp(left, right, first_token=left.first_token, last_token=right.last_token)
                        elif op == Tokens.MINUS:
                            left = SubOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_mult_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_unary_expr()
        if left:
            while True:
                self.save()
                if self.next_in_rc([Tokens.MULT, Tokens.DIV, Tokens.MOD, Tokens.FLOOR]):
                    op = self.type
                    right = self.parse_unary_expr()
                    if right:
                        self.success()
                        if op == Tokens.MULT:
                            left = MultOp(left, right, first_token=left.first_token, last_token=right.last_token)
                        elif op == Tokens.DIV:
                            left = FloatDivOp(left, right, first_token=left.first_token, last_token=right.last_token)
                        elif op == Tokens.MOD:
                            left = ModOp(left, right, first_token=left.first_token, last_token=right.last_token)
                        elif op == Tokens.FLOOR:
                            left = FloorDivOp(left, right, first_token=left.first_token, last_token=right.last_token)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_unary_expr(self) -> Expression or bool:
        self.save()
        if self.next_is_rc(Tokens.NOT):
            t: Token = self._LT
            expr = self.parse_unary_expr()
            if expr:
                self.success()
                return ULNotOp(expr, first_token=t, last_token=t)

        self.failure_save()
        if self.next_is_rc(Tokens.LENGTH):
            t: Token = self._LT
            expr = self.parse_expr()
            if expr:
                self.success()
                return ULengthOP(expr, first_token=t, last_token=t)

        self.failure_save()
        if self.next_is_rc(Tokens.MINUS):
            t: Token = self._LT
            expr = self.parse_unary_expr()
            if expr:
                self.success()
                return UMinusOp(expr, first_token=t, last_token=t)

        self.failure_save()
        if self.next_is_rc(Tokens.BITNOT):
            t: Token = self._LT
            expr = self.parse_unary_expr()
            if expr:
                self.success()
                return UBNotOp(expr, first_token=t, last_token=t)

        self.failure_save()
        expr = self.parse_pow_expr()
        if expr:
            self.success()
            return expr

        return self.failure()

    def parse_pow_expr(self) -> Expression or bool:
        self.save()
        left = self.parse_atom()
        if left:
            while True:
                self.save()
                if self.next_is_rc(Tokens.POW):
                    right = self.parse_expr()
                    if right:
                        self.success()
                        left = ExpoOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        self.failure()

    def parse_atom(self) -> Expression or bool:
        atom = self.parse_var()
        if atom:
            return atom
        atom = self.parse_function_literal()
        if atom:
            return atom
        atom = self.parse_table_constructor()
        if atom:
            return atom
        if self.next_is(Tokens.VARARGS) and self.next_is_rc(Tokens.VARARGS):
            return Varargs()

        if self.next_is(Tokens.NUMBER) and self.next_is_rc(Tokens.NUMBER):
            # TODO: optimize
            # using python number eval to parse lua number
            try:
                number = ast.literal_eval(self.text)
            except:
                # exception occurs with leading zero number: 002
                number = float(self.text)
            return Number(
                number,
                first_token=self._LT,
                last_token=self._LT,
            )

        if self.next_is(Tokens.STRING) and self.next_is_rc(Tokens.STRING):
            string = self.parse_lua_str(self.text, self._LT)
            return string

        if self.next_is(Tokens.NIL) and self.next_is_rc(Tokens.NIL):
            return Nil(first_token=self._LT, last_token=self._LT)

        if self.next_is(Tokens.TRUE) and self.next_is_rc(Tokens.TRUE):
            return TrueExpr(first_token=self._LT, last_token=self._LT)

        if self.next_is(Tokens.FALSE) and self.next_is_rc(Tokens.FALSE):
            return FalseExpr(first_token=self._LT, last_token=self._LT)
        return None

    @staticmethod
    def parse_lua_str(lua_str, token: Optional[CommonToken] = None) -> String:
        delimiter: StringDelimiter = StringDelimiter.SINGLE_QUOTE
        p = re.compile(r"^\[=+\[(.*)]=+]")  # nested quote pattern
        # try remove double quote:
        if lua_str.startswith('"') and lua_str.endswith('"'):
            lua_str = lua_str[1:-1]
            delimiter = StringDelimiter.DOUBLE_QUOTE
        # try remove single quote:
        elif lua_str.startswith("'") and lua_str.endswith("'"):
            lua_str = lua_str[1:-1]
            delimiter = StringDelimiter.SINGLE_QUOTE
        # try remove double square bracket:
        elif lua_str.startswith("[[") and lua_str.endswith("]]"):
            lua_str = lua_str[2:-2]
            delimiter = StringDelimiter.DOUBLE_SQUARE
        # nested quote
        elif p.match(lua_str):
            lua_str = p.search(lua_str).group(1)
        return String(lua_str, delimiter, first_token=token, last_token=token)

    def parse_function_literal(self) -> AnonymousFunction or bool:
        self.save()
        if self.next_is_rc(Tokens.FUNCTION):
            t: Token = self._LT
            func_body = self.parse_func_body()
            if func_body:
                self.success()
                node = AnonymousFunction(
                    func_body[0],
                    func_body[1],
                    first_token=t,
                    last_token=self._LT,
                )
                self.handle_hidden_right()
                return node

        return self.failure()

    def parse_table_constructor(self, render_last_hidden=True) -> Table or bool:
        self.save()
        if self.next_is_rc(Tokens.OBRACE, False):  # do not render right hidden
            first_token = self._LT
            self.handle_hidden_right()  # render hidden after new level

            fields = self.parse_field_list()
            if self.next_is_rc(Tokens.CBRACE, render_last_hidden):
                last_token = self._LT
                self.success()

                array_like_index = 1
                if fields:  # optional
                    for field in fields:
                        if field.key is None:
                            field.key = Number(array_like_index)
                            field.between_brackets = True
                            array_like_index += 1

                return Table(fields or [], first_token=first_token, last_token=last_token)

        return self.failure()

    def parse_field_list(self) -> List[Field] or bool:
        field_list = []
        self.save()
        field, _ = self.parse_field()
        if field:
            field_list.append(field)
            while True:
                self.save()
                if self.next_in_rc([Tokens.COMMA, Tokens.SEMCOL]):
                    inline_com = self.get_inline_comment()
                    if inline_com:
                        field.comments.append(inline_com)
                    prev_field = field
                    field, remaining_comments = self.parse_field()
                    if field:
                        field_list.append(field)
                        self.success()
                    else:
                        prev_field.comments.extend(remaining_comments)
                        self.success()
                        self.success()
                        return field_list
                else:
                    field.comments.extend(self.get_comments())
                    self.failure()
                    break
            self.parse_field_sep()
            self.success()
            return field_list
        return self.failure()

    def parse_field(self) -> Tuple[Field or bool, Comments]:
        self.save()

        if self.next_is_rc(Tokens.OBRACK):
            first_token: Token = self._LT
            key = self.parse_expr()
            if key and self.next_is_rc(Tokens.CBRACK):
                if self.next_is_rc(Tokens.ASSIGN):
                    comments = self.get_comments()
                    value = self.parse_expr()
                    if value:
                        last_token = value.last_token
                        self.success()
                        return (
                            Field(key, value, comments=comments, between_brackets=True,
                                  first_token=first_token, last_token=last_token),
                            comments,
                        )

        self.failure_save()
        if self.next_is_rc(Tokens.NAME):
            first_token = self._LT
            key = Name(
                self.text,
                first_token=self._LT,
                last_token=self._LT,
            )
            if self.next_is_rc(Tokens.ASSIGN):
                comments = self.get_comments()
                value = self.parse_expr()
                last_token = value.last_token
                if value:
                    self.success()
                    return Field(key, value, comments=comments, first_token=first_token,
                                 last_token=last_token), comments

        self.failure_save()
        comments = self.get_comments()
        value = self.parse_expr()
        if value:
            self.success()
            # noinspection PyTypeChecker
            return (
                Field(None, value, comments=comments, first_token=value.first_token, last_token=value.last_token),
                [],
            )  # Key will be set in parse_table_constructor

        return self.failure(), comments

    def parse_field_sep(self) -> bool:
        self.save()
        if self.next_in_rc([Tokens.COMMA, Tokens.SEMCOL]):
            return self.success()
        return self.failure()


class BuilderVisitor(LuaParserVisitor):
    COMMENT_CHANNEL = 2

    def __init__(self, comment_token_stream: CommonTokenStream):
        super().__init__()
        self.comment_token_stream = comment_token_stream

    # Visit a parse tree produced by LuaParser#start_.
    def visitStart_(self, ctx: LuaParser.Start_Context):
        return self.visitChildren(ctx)

    def visitTerminal(self, node: TerminalNodeImpl):
        if node.symbol.type == LuaParser.EOF:
            return None
        elif node.symbol.type == LuaParser.NAME:
            return Name(node.getText())
        else:
            return node.getText()

    def visitErrorNode(self, node: ErrorNodeImpl):
        return "error:" + node.getText()

    def defaultResult(self):
        return None

    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return nextResult
        if type(nextResult) is list:
            nextResult.append(aggregate)
            return nextResult
        if type(aggregate) is list:
            aggregate.append(nextResult)
            return aggregate
        if nextResult is None:
            return aggregate
        return [nextResult, aggregate]

    @staticmethod
    def has_double_nl(tokens: List[CommonToken]) -> bool:
        """Returns True if the last two tokens are newlines."""
        return len(tokens) > 1 and tokens[-1].type is LuaLexer.NL and tokens[-2] is LuaLexer.NL

    def add_comment_context(self, ctx: ParserRuleContext, node: Node):
        hidden_tokens_left = self.comment_token_stream.getHiddenTokensToLeft(ctx.start.tokenIndex)
        if hidden_tokens_left is None:
            return

        if self.has_double_nl(hidden_tokens_left):
            return

        for token in hidden_tokens_left:
            if token.channel == self.COMMENT_CHANNEL:
                node.comments.append(Comment(token.text, is_multi_line=token.type == LuaLexer.COMMENT))

        return

    def add_context(self, ctx: ParserRuleContext, node: TNode) -> TNode:
        self.add_comment_context(ctx, node)
        return node

    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx: LuaParser.ChunkContext):
        return self.add_context(ctx, Chunk(
            body=self.visitChildren(ctx)
        ))

    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx: LuaParser.BlockContext):
        statements = [self.visit(stat) for stat in ctx.stat()]
        if ctx.retstat():
            statements.append(self.visit(ctx.retstat()))
        return self.add_context(ctx, Block(
            body=statements
        ))

    # Visit a parse tree produced by LuaParser#stat_empty.
    def visitStat_empty(self, ctx: LuaParser.Stat_emptyContext):
        return SemiColon()

    # Visit a parse tree produced by LuaParser#stat_assignment.
    def visitStat_assignment(self, ctx: LuaParser.Stat_assignmentContext):
        return self.add_context(ctx, Assign(
            targets=_listify(self.visit(ctx.varlist())),
            values=_listify(self.visit(ctx.explist())),
        ))

    # Visit a parse tree produced by LuaParser#stat_functioncall.
    def visitStat_functioncall(self, ctx: LuaParser.Stat_functioncallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_label.
    def visitStat_label(self, ctx: LuaParser.Stat_labelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_break.
    def visitStat_break(self, ctx: LuaParser.Stat_breakContext):
        return self.add_context(ctx, Break())

    # Visit a parse tree produced by LuaParser#stat_goto.
    def visitStat_goto(self, ctx: LuaParser.Stat_gotoContext):
        return self.add_context(ctx, Goto(self.visit(ctx.NAME())))

    # Visit a parse tree produced by LuaParser#stat_do.
    def visitStat_do(self, ctx: LuaParser.Stat_doContext):
        return self.add_context(ctx, Do(body=self.visit(ctx.block())))

    # Visit a parse tree produced by LuaParser#stat_while.
    def visitStat_while(self, ctx: LuaParser.Stat_whileContext):
        return self.add_context(ctx, While(
            test=self.visit(ctx.exp()),
            body=self.visit(ctx.block()),
        ))

    # Visit a parse tree produced by LuaParser#stat_repeat.
    def visitStat_repeat(self, ctx: LuaParser.Stat_repeatContext):
        return self.add_context(ctx, Repeat(
            body=self.visit(ctx.block()),
            test=self.visit(ctx.exp()),
        ))

    # Visit a parse tree produced by LuaParser#stat_if.
    def visitStat_if(self, ctx: LuaParser.Stat_ifContext):
        expressions = ctx.exp()
        blocks = ctx.block()
        nb_else_if = len(ctx.ELSEIF())
        if_stat = self.add_context(expressions[0], If(
            test=self.visit(expressions[0]),
            body=self.visit(blocks[0]),
            orelse=None,
        ))

        or_else_leaf = None
        if nb_else_if > 0:
            or_else_root = self.add_context(expressions[1], ElseIf(
                test=self.visit(expressions[1]),
                body=self.visit(blocks[1]),
                orelse=None,
            ))

            or_else_leaf = or_else_root
            for i in range(nb_else_if - 1):
                or_else_leaf.orelse = self.add_context(expressions[i + 2], ElseIf(
                    test=self.visit(expressions[i + 2]),
                    body=self.visit(blocks[i + 2]),
                    orelse=None,
                ))
                or_else_leaf = or_else_leaf.orelse

            if_stat.orelse = or_else_root

        if ctx.ELSE():
            block = self.visit(blocks[len(blocks) - 1])
            if if_stat.orelse is None:
                if_stat.orelse = block
            else:
                or_else_leaf.orelse = block

        return if_stat

    # Visit a parse tree produced by LuaParser#stat_for.
    def visitStat_for(self, ctx: LuaParser.Stat_forContext):
        if ctx.IN():  # forin
            return self.add_context(ctx, Forin(
                body=self.visit(ctx.block()),
                iter=self.visit(ctx.explist()),
                targets=self.visit(ctx.namelist()),
            ))
        else:  # fornum
            return self.add_context(ctx, Fornum(
                target=self.visit(ctx.NAME()),
                start=self.visit(ctx.exp(0)),
                stop=self.visit(ctx.exp(1)),
                step=self.visit(ctx.exp(2)) if ctx.exp(2) else None,
                body=self.visit(ctx.block()),
            ))

    # Visit a parse tree produced by LuaParser#stat_function.
    def visitStat_function(self, ctx: LuaParser.Stat_functionContext):
        func_name = self.visitFuncname(ctx.funcname())
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return self.add_context(ctx, Function(func_name, param_list, block))

    # Visit a parse tree produced by LuaParser#stat_localfunction.
    def visitStat_localfunction(self, ctx: LuaParser.Stat_localfunctionContext):
        func_name = self.visit(ctx.NAME())
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return self.add_context(ctx, LocalFunction(func_name, param_list, block))

    # Visit a parse tree produced by LuaParser#stat_local.
    def visitStat_local(self, ctx: LuaParser.Stat_localContext):
        att_name_list = self.visitAttnamelist(ctx.attnamelist())

        if ctx.EQ():
            exp_list = self.visitExplist(ctx.explist())
        else:
            exp_list = []

        return self.add_context(ctx, LocalAssign(targets=att_name_list, values=exp_list))

    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx: LuaParser.FunctiondefContext) -> AnonymousFunction:
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return self.add_context(ctx, AnonymousFunction(param_list, block))

    # Visit a parse tree produced by LuaParser#attnamelist.
    def visitAttnamelist(self, ctx: LuaParser.AttnamelistContext):
        return [self.visit(a) for a in ctx.nameattrib()]

    def visitNameattrib(self, ctx: LuaParser.NameattribContext):
        name = self.visit(ctx.NAME())
        if ctx.attrib():
            attrib = self.visit(ctx.attrib())
            name.attribute = attrib
        return name

    # Visit a parse tree produced by LuaParser#attrib.
    def visitAttrib(self, ctx: LuaParser.AttribContext):
        return Attribute(self.visit(ctx.NAME()))

    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx: LuaParser.RetstatContext):
        if ctx.RETURN():
            return self.add_context(ctx, Return(
                values=self.visit(ctx.explist())
            ))
        elif ctx.BREAK():
            return self.add_context(ctx, Break())
        else:
            return self.add_context(ctx, Continue())

    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx: LuaParser.LabelContext):
        return self.add_context(ctx, Label(label_id=self.visit(ctx.NAME())))

    # Visit a parse tree produced by LuaParser#funcname.
    def visitFuncname(self, ctx: LuaParser.FuncnameContext):
        names = ctx.NAME()
        has_invoke = ctx.COL() is not None
        root = self.visit(names[0])
        until = len(names) - 1 if has_invoke else len(names)
        for i in range(1, until):
            root = Index(
                idx=self.visit(names[i]),
                value=root,
                notation=IndexNotation.DOT,
            )

        if has_invoke:
            return self.add_context(ctx, Invoke(root, self.visit(names[-1]), []))

        return self.add_context(ctx, root)

    # Visit a parse tree produced by LuaParser#varlist.
    def visitVarlist(self, ctx: LuaParser.VarlistContext):
        return [self.visit(v) for v in ctx.var()]

    # Visit a parse tree produced by LuaParser#namelist.
    def visitNamelist(self, ctx: LuaParser.NamelistContext) -> List[Name]:
        return [self.visit(n) for n in ctx.NAME()]

    # Visit a parse tree produced by LuaParser#explist.
    def visitExplist(self, ctx: LuaParser.ExplistContext):
        return [self.visit(exp) for exp in ctx.exp()]

    # Visit a parse tree produced by LuaParser#exp.
    def visitExp(self, ctx: LuaParser.ExpContext) -> Expression:
        exp: Expression = Nil()

        if ctx.NIL():
            exp = Nil()
        elif ctx.FALSE():
            exp = FalseExpr()
        elif ctx.TRUE():
            exp = TrueExpr()
        elif ctx.number():
            exp = self.visit(ctx.number())
        elif ctx.string():
            exp = self.visit(ctx.string())
        elif ctx.DDD():
            exp = Dots()
        elif ctx.functiondef():
            exp = self.visit(ctx.functiondef())
        elif ctx.prefixexp():
            exp = self.visit(ctx.prefixexp())
        elif ctx.tableconstructor():
            exp = self.visit(ctx.tableconstructor())
        elif ctx.unary_op:
            if ctx.unary_op.type == LuaParser.NOT:
                exp = ULNotOp(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.POUND:
                exp = ULengthOP(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.MINUS:
                exp = UMinusOp(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.SQUIG:
                exp = UBNotOp(self.visit(ctx.exp(0)))

        elif ctx.op:
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))

            if ctx.op.type == LuaParser.CARET:
                exp = ExpoOp(left, right)
            elif ctx.op.type == LuaParser.STAR:
                exp = MultOp(left, right)
            elif ctx.op.type == LuaParser.SLASH:
                exp = FloatDivOp(left, right)
            elif ctx.op.type == LuaParser.PER:
                exp = ModOp(left, right)
            elif ctx.op.type == LuaParser.SS:
                exp = FloorDivOp(left, right)
            elif ctx.op.type == LuaParser.PLUS:
                exp = AddOp(left, right)
            elif ctx.op.type == LuaParser.MINUS:
                exp = SubOp(left, right)
            elif ctx.op.type == LuaParser.DD:
                exp = Concat(left, right)
            elif ctx.op.type == LuaParser.LT:
                exp = LessThanOp(left, right)
            elif ctx.op.type == LuaParser.GT:
                exp = GreaterThanOp(left, right)
            elif ctx.op.type == LuaParser.LE:
                exp = LessOrEqThanOp(left, right)
            elif ctx.op.type == LuaParser.GE:
                exp = GreaterOrEqThanOp(left, right)
            elif ctx.op.type == LuaParser.SQEQ:
                exp = NotEqToOp(left, right)
            elif ctx.op.type == LuaParser.EE:
                exp = EqToOp(left, right)
            elif ctx.op.type == LuaParser.AND:
                exp = AndLoOp(left, right)
            elif ctx.op.type == LuaParser.OR:
                exp = OrLoOp(left, right)
            elif ctx.op.type == LuaParser.AMP:
                exp = BAndOp(left, right)
            elif ctx.op.type == LuaParser.PIPE:
                exp = BOrOp(left, right)
            elif ctx.op.type == LuaParser.SQUIG:
                exp = BXorOp(left, right)
            elif ctx.op.type == LuaParser.LL:
                exp = BShiftLOp(left, right)
            elif ctx.op.type == LuaParser.GG:
                exp = BShiftROp(left, right)

        return self.add_context(ctx, exp)

    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx: LuaParser.VarContext):
        if ctx.NAME():
            return self.add_context(ctx, Name(ctx.NAME().getText()))
        else:  # prefixexp tail
            root = self.visit(ctx.prefixexp())
            return self.visitAllTails(root, [ctx.tail()])

    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
        if ctx.NAME():  # NAME tail*
            root = self.visit(ctx.NAME())
        elif ctx.functioncall():  # functioncall tail*
            root = self.visit(ctx.functioncall())
        else:  # '(' exp ')' tail*
            root: Expression = self.visit(ctx.exp())
            root.wrapped = True

        tail = self.visitAllTails(root, ctx.tail())
        return tail

    # Visit a parse tree produced by LuaParser#functioncall_name.
    def visitFunctioncall_name(self, ctx: LuaParser.Functioncall_nameContext):
        name = self.visit(ctx.NAME())
        tail = self.visitAllTails(name, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Call(tail, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_nested.
    def visitFunctioncall_nested(self, ctx: LuaParser.Functioncall_nestedContext):
        call = self.visit(ctx.functioncall())
        tail = self.visitAllTails(call, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Call(tail, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_exp.
    def visitFunctioncall_exp(self, ctx: LuaParser.Functioncall_expContext):
        exp = self.visitExp(ctx.exp())
        exp.wrapped = True
        tail = self.visitAllTails(exp, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Call(tail, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_expinvoke.
    def visitFunctioncall_expinvoke(self, ctx: LuaParser.Functioncall_expinvokeContext):
        exp = self.visitExp(ctx.exp())
        exp.wrapped = True
        tail = self.visitAllTails(exp, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        func = self.visit(ctx.NAME())
        return self.add_context(ctx, Invoke(tail, func, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_invoke.
    def visitFunctioncall_invoke(self, ctx: LuaParser.Functioncall_invokeContext):
        source = self.visit(ctx.NAME(0))
        func = self.visit(ctx.NAME(1))
        tail = self.visitAllTails(source, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Invoke(tail, func, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_nestedinvoke.
    def visitFunctioncall_nestedinvoke(self, ctx: LuaParser.Functioncall_nestedinvokeContext):
        call = self.visit(ctx.functioncall())
        func = self.visit(ctx.NAME())
        tail = self.visitAllTails(call, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Invoke(tail, func, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    def visitAllTails(self, root_exp: Expression, tails: List[LuaParser.TailContext]):
        if not tails:
            return root_exp

        root = root_exp  # parent root will be set in caller
        tail: Index = self.visitTail(tails[0])  # root tail
        i = 1
        while tail:
            tail.value = root
            root = tail

            if i >= len(tails):
                break

            tail = self.visit(tails[i])
            i += 1
        return root

    def visitTail(self, ctx: LuaParser.TailContext):
        if ctx.OB() and ctx.CB():
            return self.add_context(ctx, Index(
                idx=self.visit(ctx.exp()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.SQUARE,
            ))
        else:
            return self.add_context(ctx, Index(
                idx=self.visit(ctx.NAME()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.DOT,
            ))

    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx: LuaParser.ArgsContext):
        if ctx.OP() and ctx.CP():  # '(' explist? ')'
            exp_list = []
            if ctx.explist():
                exp_list = self.visit(ctx.explist())

            return True, exp_list
        elif ctx.tableconstructor():  # tableconstructor
            return False, self.visit(ctx.tableconstructor())
        else:  # string
            return False, self.visit(ctx.string())

    # Visit a parse tree produced by LuaParser#funcbody.
    def visitFuncbody(self, ctx: LuaParser.FuncbodyContext) -> Tuple[List[Expression], Block]:
        par_list = self.visitParlist(ctx.parlist())
        block = self.visit(ctx.block())
        return par_list, block

    # Visit a parse tree produced by LuaParser#parlist.
    def visitParlist(self, ctx: LuaParser.ParlistContext) -> List[Expression]:
        if ctx.namelist():
            name_list: List[Expression] = self.visitNamelist(ctx.namelist())
        else:
            name_list = []

        if ctx.DDD():
            name_list.append(Varargs())
        return name_list

    # Visit a parse tree produced by LuaParser#tableconstructor.
    def visitTableconstructor(self, ctx: LuaParser.TableconstructorContext):
        if ctx.fieldlist():
            fields = self.visit(ctx.fieldlist())

            array_like_index = 1
            if fields:  # optional
                for field in fields:
                    if field.key is None:
                        field.key = Number(array_like_index)
                        field.between_brackets = True
                        array_like_index += 1
            return self.add_context(ctx, Table(fields))
        return self.add_context(ctx, Table([]))

    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx: LuaParser.FieldlistContext):
        return [self.visit(f) for f in ctx.field()]

    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx: LuaParser.FieldContext):
        if ctx.OB():  # '[' exp ']' '=' exp
            key = self.visit(ctx.exp(0))
            value = self.visit(ctx.exp(1))
            return self.add_context(ctx, Field(key, value, between_brackets=True))
        elif ctx.NAME():  # NAME '=' exp
            key = Name(ctx.NAME().getText())
            value = self.visit(ctx.exp(0))
            return self.add_context(ctx, Field(key, value))
        else:  # exp
            # Key will be set in parent call:
            return self.add_context(ctx, Field(None, self.visit(ctx.exp(0))))

    # Visit a parse tree produced by LuaParser#fieldsep.
    def visitFieldsep(self, ctx: LuaParser.FieldsepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#number.
    def visitNumber(self, ctx: LuaParser.NumberContext):
        number_text = self.visitChildren(ctx)
        try:
            number = ast.literal_eval(number_text)
        except:
            # exception occurs with leading zero number: 002
            number = float(number_text)
        return Number(
            number,
        )

    # Visit a parse tree produced by LuaParser#string.
    def visitString(self, ctx: LuaParser.StringContext):
        lua_str = ctx.getText()

        delimiter: StringDelimiter = StringDelimiter.SINGLE_QUOTE
        p = re.compile(r"^\[=+\[(.*)]=+]")  # nested quote pattern
        # try remove double quote:
        if lua_str.startswith('"') and lua_str.endswith('"'):
            lua_str = lua_str[1:-1]
            delimiter = StringDelimiter.DOUBLE_QUOTE
        # try remove single quote:
        elif lua_str.startswith("'") and lua_str.endswith("'"):
            lua_str = lua_str[1:-1]
            delimiter = StringDelimiter.SINGLE_QUOTE
        # try remove double square bracket:
        elif lua_str.startswith("[[") and lua_str.endswith("]]"):
            lua_str = lua_str[2:-2]
            delimiter = StringDelimiter.DOUBLE_SQUARE
        # nested quote
        elif p.match(lua_str):
            lua_str = p.search(lua_str).group(1)

        return String(lua_str, delimiter)
