import logging
from luaparser import ast, asttokens
from luaparser.astnodes import *
from luaparser.asttokens import Tokens
from enum import Enum
from antlr4.Token import CommonToken



class Expr(Enum):
    OR      = 1
    AND     = 2
    REL     = 3
    CONCAT  = 4
    ADD     = 5
    MULT    = 6
    BITWISE = 7
    UNARY   = 8
    POW     = 9
    ATOM    = 10


class CTokens:
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



class Builder:
    CLOSING_TOKEN = [
        CTokens.END,
        CTokens.CBRACE,
        CTokens.CPAR]

    HIDDEN_TOKEN = [
        CTokens.SHEBANG,
        CTokens.LINE_COMMENT,
        CTokens.COMMENT,
        CTokens.NEWLINE,
        CTokens.SPACE,
        -2]

    REL_OPERATORS = [
        CTokens.LT,
        CTokens.GT,
        CTokens.LTEQ,
        CTokens.GTEQ,
        CTokens.NEQ,
        CTokens.EQ]


    def __init__(self, source):
        self._stream = asttokens.get_token_stream(source)
        # contains a list of CommonTokens
        self._line_count = 0
        self._right_index = 0
        self._last_expr_type = None

        # following stack are used to backup values
        self._index_stack = []
        self._right_index_stack = []
        self.text = ''  # last token text

    def process(self):
        node = self.parse_chunk()
        if not node:
            raise Exception("Expecting a chunk")
        return node

    def save(self):
        #logging.debug('trying ' + inspect.stack()[1][3])
        self._index_stack.append(self._stream.index)
        self._right_index_stack.append(self._right_index)

    def success(self):
        self._index_stack.pop()
        self._right_index_stack.pop()
        #logging.debug('success ' + inspect.stack()[1][3])
        return True

    def failure(self):
        #logging.debug('failure ' + inspect.stack()[1][3])
        self._stream.seek(self._index_stack.pop())
        self._right_index = self._right_index_stack.pop()
        return None

    def failure_save(self):
        self.failure()
        self.save()

    def next_is_rc(self, type, hidden_right=True):
        token = self._stream.LT(1)
        toktype = token.type
        self._right_index = self._stream.index

        if toktype == type:
            self.text = token.text
            self._stream.consume()
            if hidden_right:
                self.handle_hidden_right()
            return True
        return False

    def next_is_c(self, type, hidden_right=True):
        token = self._stream.LT(1)
        toktype = token.type
        self._right_index = self._stream.index

        if toktype == type:
            self._stream.consume()
            if hidden_right:
                self.handle_hidden_right()
            return True
        return False

    def next_is(self, type):
        return self._stream.LT(1).type == type

    def next_in_rc(self, types, hidden_right=True):
        token = self._stream.LT(1)
        tok_type = token.type
        self._right_index = self._stream.index

        if tok_type in types:
            self._stream.consume()
            if hidden_right:
                self.handle_hidden_right()
            return True
        return False

    def next_in(self, types):
        return self._stream.LT(1).type in types

    def handle_hidden_left(self):
        tokens = self._stream.getHiddenTokensToLeft(self._stream.index)
        if tokens:
            for t in tokens:
                print(t)

    def handle_hidden_right(self, is_newline=False):
        tokens = self._stream.getHiddenTokensToRight(self._right_index)
        if tokens:
            for t in tokens:
                print(t)

    def parse_chunk(self):
        self.save()
        self._stream.LT(1)
        self.handle_hidden_left()
        block = self.parse_block()
        if block:
            token = self._stream.LT(1)
            if token.type == -1:
                # do not consume EOF
                self.success()
                return Chunk(block)
        return self.failure()

    def parse_block(self):
        self.save()
        statements = []

        while True:
            stat = self.parse_stat()
            if not stat:
                break
            statements.append(stat)

        self.parse_ret_stat()
        self.success()
        return Block(statements)

    def parse_stat(self):
        stat = self.parse_assignment()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_var(True)
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_do_block()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_while_stat()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_repeat_stat()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_local()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_goto_stat()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_if_stat()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_for_stat()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_function()
        if stat:
            self.handle_hidden_right()
            return stat
        stat = self.parse_label()
        if stat:
            self.handle_hidden_right()
            return stat

        if self.next_is(CTokens.BREAK) and self.next_is_rc(CTokens.BREAK):
            self.handle_hidden_right()
            return Break()
        if self.next_is(CTokens.SEMCOL) and self.next_is_rc(CTokens.SEMCOL):
            self.handle_hidden_right()
            return SemiColon()

        return False

    def parse_ret_stat(self):
        self.save()
        if self.next_is_rc(CTokens.RETURN):
            self.parse_expr_list()  # optional
            self.save()
            if self.next_is_rc(CTokens.SEMCOL):
                self.success()
            else:
                self.failure()

            return self.success()
        return self.failure()

    def parse_assignment(self):
        self.save()
        if self.parse_var_list():
            if self.next_is_rc(CTokens.ASSIGN):
                if self.parse_expr_list():
                    return self.success()
        return self.failure()

    def parse_var_list(self):
        self.save()
        if self.parse_var():
            while True:
                self.save()
                if self.next_is_rc(CTokens.COMMA) and self.parse_var():
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        return self.failure()

    def parse_var(self, is_stat=False):
        self.save()
        number_of_tail = 0
        if self.parse_callee():
            if self.parse_tail():
                self.handle_hidden_right()
                while self.parse_tail():
                    self.handle_hidden_right()
                    number_of_tail += 1
            if number_of_tail < 2:
                return self.success()


        self.failure_save()
        if self.parse_callee():
            for n in range(0, number_of_tail):
                self.parse_tail()
                self.handle_hidden_right()
            self.parse_tail()

            self.handle_hidden_right()
            return self.success()

        return self.failure()

    def parse_tail(self):
        # do not render last hidden
        self.save()
        if self.next_is_rc(CTokens.DOT) and self.next_is_rc(CTokens.NAME, False):
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.OBRACK) and self.parse_expr() and self.next_is_rc(CTokens.CBRACK, False):
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME) and self.next_is_rc(CTokens.OPAR):
            self.parse_expr_list(True)
            if self.next_is_rc(CTokens.CPAR, False):
                return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME) and self.parse_table_constructor(False):
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME) and self.next_is_rc(CTokens.STRING, False):
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.OPAR, False):
            self.handle_hidden_right()
            self.parse_expr_list(False, True)
            if self.next_is_rc(CTokens.CPAR, False):
                return self.success()

        self.failure_save()
        if self.parse_table_constructor(False):
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.STRING, False):
            return self.success()

        return self.failure()

    def parse_expr_list(self, force_indent=False, force_no_indent=False):
        self.save()
        if self.parse_expr():
            while True:
                self.save()
                if self.next_is_rc(CTokens.COMMA) and self.parse_expr():
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        return self.failure()

    def parse_do_block(self):
        save = self.save()
        if self.next_is_rc(CTokens.DO, False):
            self.handle_hidden_right()
            if self.parse_block():
                self.dec_level()
                if self.next_is_rc(CTokens.END):
                    return self.success()
        return self.failure()

    def parse_while_stat(self):
        self.save()
        if self.next_is_rc(CTokens.WHILE) and self.parse_expr() and self.parse_do_block():
            return self.success()

        return self.failure()

    def parse_repeat_stat(self):
        self.save()
        if self.next_is_rc(CTokens.REPEAT, False):
            self.handle_hidden_right()
            if self.parse_block():
                if self.next_is_rc(CTokens.UNTIL) and self.parse_expr():
                    return self.success()

        return self.failure()

    def parse_local(self):
        self.save()
        if self.next_is_rc(CTokens.LOCAL):
            self.save()
            targets = self.parse_name_list()
            if targets:
                # optional
                self.save()
                if self.next_is_rc(CTokens.ASSIGN) and self.parse_expr_list():
                    self.success()
                else:
                    self.failure()
                self.success()
                self.success()
                return LocalAssign(targets, None)

            self.failure_save()
            if self.next_is_rc(CTokens.FUNCTION) and self.next_is_rc(CTokens.NAME) and self.parse_func_body():
                self.success()
                return self.success()
            self.failure()

        return self.failure()

    def parse_goto_stat(self):
        self.save()
        if self.next_is_rc(CTokens.GOTO) and self.next_is_rc(CTokens.NAME):
            return self.success()
        return self.failure()

    def parse_if_stat(self):
        self.save()
        if self.next_is_rc(CTokens.IFTOK):
            if self.parse_expr():
                if self.next_is_rc(CTokens.THEN, False):
                    self.handle_hidden_right()
                    if self.parse_block():
                        while self.parse_elseif_stat():  # one or more
                            pass
                        self.parse_else_stat()  # optional
                        if self.next_is_rc(CTokens.END):
                            return self.success()
        return self.failure()

    def parse_elseif_stat(self):
        self.save()
        if self.next_is(CTokens.ELSEIF):
            if self.next_is_rc(CTokens.ELSEIF):
                if self.parse_expr():
                    if self.next_is_rc(CTokens.THEN, False):
                        self.handle_hidden_right()
                        if self.parse_block():
                            return self.success()
        return self.failure()

    def parse_else_stat(self):
        self.save()
        if self.next_is(CTokens.ELSETOK):
            if self.next_is_rc(CTokens.ELSETOK, False):
                self.handle_hidden_right()
                if self.parse_block():
                    return self.success()
        return self.failure()

    def  parse_for_stat(self):
        self.save()
        if self.next_is_rc(CTokens.FOR):
            self.save()
            if self.next_is_rc(CTokens.NAME) and \
                    self.next_is_rc(CTokens.ASSIGN) and \
                    self.parse_expr() and \
                    self.next_is_rc(CTokens.COMMA) and \
                    self.parse_expr():
                self.save()
                if self.next_is_rc(CTokens.COMMA) and self.parse_expr():
                    self.success()
                else:
                    self.failure()
                if self.parse_do_block():
                    self.success()
                    return self.success()

            self.failure_save()
            if self.parse_name_list() and \
                    self.next_is_rc(CTokens.IN) and \
                    self.parse_expr_list(True) and \
                    self.parse_do_block():
                self.success()
                return self.success()
            self.failure()

        return self.failure()

    def parse_function(self):
        self.save()
        if self.next_is_rc(CTokens.FUNCTION) and self.parse_names():
            self.save()
            if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME):
                if self.parse_func_body():
                    self.success()
                    return self.success()

            self.failure_save()
            if self.parse_func_body():
                return self.success()
            self.failure()

        return self.failure()

    def parse_names(self):
        self.save()
        if self.next_is_rc(CTokens.NAME):
            while True:
                self.save()
                if self.next_is_rc(CTokens.DOT) and self.next_is_rc(CTokens.NAME):
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_func_body(self):
        self.save()
        if self.next_is_rc(CTokens.OPAR, False):  # do not render right hidden
            self.handle_hidden_right()  # render hidden after new level
            if self.parse_param_list():
                if self.next_is_rc(CTokens.CPAR, False):  # do not render right hidden
                    self.handle_hidden_right()  # render hidden after new level
                    if self.parse_block():
                        if self.next_is_rc(CTokens.END):
                            return self.success()
        return self.failure()

    def parse_param_list(self):
        self.save()
        if self.parse_name_list():
            self.save()
            if self.next_is_rc(CTokens.COMMA) and \
                    self.next_is_rc(CTokens.VARARGS):
                self.success()
            else:
                self.failure()
            return self.success()
        self.failure_save()

        if self.next_is_rc(CTokens.VARARGS):
            return self.success()

        return self.success()

    def parse_name_list(self):
        self.save()
        names = []
        if self.next_is_rc(CTokens.NAME):
            names.append(Name(self.text))
            while True:
                self.save()
                if self.next_is_rc(CTokens.COMMA) and self.next_is_rc(CTokens.NAME):
                    names.append(Name(self.text))
                    self.success()
                else:
                    self.failure()
                    break
            self.success()
            return names
        return self.failure()

    def parse_label(self):
        self.save()
        if self.next_is_rc(CTokens.COLCOL) and self.next_is_rc(CTokens.NAME) and self.next_is_rc(CTokens.COLCOL):
            return self.success()

        return self.failure()

    def parse_callee(self):
        self.save()
        if self.next_is_rc(CTokens.OPAR):
            if self.parse_expr():
                if self.next_is_rc(CTokens.CPAR):
                    return self.success()
        self.failure()
        self.save()
        if self.next_is_rc(CTokens.NAME):
            return self.success()
        return self.failure()

    def parse_expr(self):
        return self.parse_or_expr()

    def parse_or_expr(self):
        self.save()
        if self.parse_and_expr():
            while True:
                self.save()
                if self.next_is_rc(CTokens.OR) and \
                        self.parse_and_expr():
                    self._last_expr_type = Expr.OR
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_and_expr(self):
        self.save()
        if self.parse_rel_expr():
            while True:
                self.save()
                if self.next_is_rc(CTokens.AND) and \
                        self.parse_rel_expr():
                    self._last_expr_type = Expr.AND
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_rel_expr(self):
        self.save()
        if self.parse_concat_expr():
            self.save()
            if self.next_in_rc(self.REL_OPERATORS) and \
                    self.parse_concat_expr():
                self._last_expr_type = Expr.REL
                self.success()
            else:
                self.failure()
            return self.success()
        self.failure()

    def  parse_concat_expr(self):
        self.save()
        if self.parse_add_expr():
            while True:
                self.save()
                if self.next_is_rc(CTokens.CONCAT) and self.parse_add_expr():
                    self._last_expr_type = Expr.CONCAT
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_add_expr(self):
        self.save()
        if self.parse_mult_expr():
            while True:
                self.save()
                if self.next_in_rc([CTokens.ADD, CTokens.MINUS]) and \
                        self.parse_mult_expr():
                    self._last_expr_type = Expr.ADD
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_mult_expr(self):
        self.save()
        if self.parse_bitwise_expr():
            while True:
                self.save()
                if self.next_in_rc([CTokens.MULT,
                                   CTokens.DIV,
                                   CTokens.MOD,
                                   CTokens.FLOOR]) and self.parse_bitwise_expr():
                    self._last_expr_type = Expr.MULT
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_bitwise_expr(self):
        self.save()
        if self.parse_unary_expr():
            while True:
                self.save()
                if self.next_in_rc([CTokens.BITAND,
                                 CTokens.BITOR,
                                 CTokens.BITNOT,
                                 CTokens.BITRSHIFT,
                                 CTokens.BITRLEFT]) and self.parse_unary_expr():
                    self._last_expr_type = Expr.BITWISE
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_unary_expr(self):
        self.save()
        if self.next_is_rc(CTokens.MINUS) and self.parse_unary_expr():
            self._last_expr_type = Expr.UNARY
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.LENGTH) and self.parse_pow_expr():
            self._last_expr_type = Expr.UNARY
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.NOT) and self.parse_unary_expr():
            self._last_expr_type = Expr.UNARY
            return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.BITNOT) and self.parse_unary_expr():
            self._last_expr_type = Expr.UNARY
            return self.success()

        self.failure_save()
        if self.parse_pow_expr():
            return self.success()

        return self.failure()

    def parse_pow_expr(self):
        self.save()
        if self.parse_atom():
            while True:
                self.save()
                if self.next_is_rc(CTokens.POW) and self.parse_atom():
                    self._last_expr_type = Expr.POW
                    self.success()
                else:
                    self.failure()
                    break
            return self.success()
        self.failure()

    def parse_atom(self):
        self.save()
        if self.parse_var() or \
                self.parse_function_literal() or \
                self.parse_table_constructor() or \
                self.next_in_rc([CTokens.VARARGS,
                                 CTokens.NUMBER,
                                 CTokens.STRING,
                                 CTokens.NIL,
                                 CTokens.TRUE,
                                 CTokens.FALSE]):
            self._last_expr_type = Expr.ATOM
            return self.success()
        return self.failure()

    def parse_function_literal(self):
        self.save()
        if self.next_is_rc(CTokens.FUNCTION) and self.parse_func_body():
            return self.success()

        return self.failure()

    def parse_table_constructor(self, render_last_hidden=True):
        self.save()
        if self.next_is_rc(CTokens.OBRACE, False):  # do not render right hidden
            self.handle_hidden_right()  # render hidden after new level

            self.parse_field_list()
            if self.next_is_rc(CTokens.CBRACE, render_last_hidden):
                return self.success()
        return self.failure()

    def parse_field_list(self):
        self.save()
        if self.parse_field():
            while True:
                self.save()
                # if check_field_list, no space is allowed between COMMA and key
                if self.next_in_rc([CTokens.COMMA, CTokens.SEMCOL]) and \
                        self.parse_field():
                    self.success()
                else:
                    self.failure()
                    break
            self.parse_field_sep()
            return self.success()
        return self.failure()


    def parse_field(self):
        self.save()
        if self.next_is_rc(CTokens.OBRACK) and self.parse_expr() \
                and self.next_is_rc(CTokens.CBRACK):
            if self.next_is_rc(CTokens.ASSIGN):
                if self.parse_expr():
                    return self.success()

        self.failure_save()
        if self.next_is_rc(CTokens.NAME):
            if self.next_is_rc(CTokens.ASSIGN):
                if self.parse_expr():
                    return self.success()

        self.failure_save()
        if self.parse_expr():
            return self.success()

        return self.failure()

    def parse_field_sep(self):
        self.save()
        if self.next_in_rc([CTokens.COMMA, CTokens.SEMCOL]):
            return self.success()
        return self.failure()
