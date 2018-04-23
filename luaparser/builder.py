from luaparser import ast, asttokens
from luaparser.astnodes import *
from luaparser.parser.LuaLexer import LuaLexer
from enum import Enum
import ast
import re


class SyntaxException(Exception):
    pass


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

LITERAL_NAMES = [ "<INVALID>",
            "'and'", "'break'", "'do'", "'else'", "'elseif'", "'end'", "'false'",
            "'for'", "'function'", "'goto'", "'if'", "'in'", "'local'",
            "'nil'", "'not'", "'or'", "'repeat'", "'return'", "'then'",
            "'true'", "'until'", "'while'", "'+'", "'-'", "'*'", "'/'",
            "'//'", "'%'", "'^'", "'#'", "'=='", "'~='", "'<='", "'>='",
            "'<'", "'>'", "'='", "'&'", "'|'", "'~'", "'>>'", "'<<'", "'('",
            "')'", "'{'", "'}'", "'['", "']'", "'::'", "':'", "','", "'...'",
            "'..'", "'.'", "';'", "NAME", "NUMBER", "STRING", "COMMENT", "LINE_COMMENT",
            "SPACE", "NEWLINE", "SHEBANG", "LONG_BRACKET"]


def _listify(obj):
    if not isinstance(obj, list):
        l = []
        l.append(obj)
        return l
    else:
        return obj



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
        self.type = -1  # last token type

        # contains expected token in case of invalid input code
        self._expected = []


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
        tok_type = token.type
        self._right_index = self._stream.index

        if tok_type == type:
            self.text = token.text
            self.type = tok_type
            self._stream.consume()
            if hidden_right:
                self.handle_hidden_right()
            return True
        self._expected.append(type)
        return False

    def next_is_c(self, type, hidden_right=True):
        token = self._stream.LT(1)
        tok_type = token.type
        self._right_index = self._stream.index

        if tok_type == type:
            self._stream.consume()
            if hidden_right:
                self.handle_hidden_right()
            return True
        self._expected.append(type)
        return False

    def next_is(self, type):
        if self._stream.LT(1).type == type:
            return True
        else:
            self._expected.append(type)
            return False

    def next_in_rc(self, types, hidden_right=True):
        token = self._stream.LT(1)
        tok_type = token.type
        self._right_index = self._stream.index

        if tok_type in types:
            self.type = tok_type
            self._stream.consume()
            if hidden_right:
                self.handle_hidden_right()
            return True
        self._expected.extend(types)
        return False

    def next_in(self, types):
        if self._stream.LT(1).type in types:
            return True
        else:
            self._expected.extend(types)
            return False

    def handle_hidden_left(self):
        tokens = self._stream.getHiddenTokensToLeft(self._stream.index)
        if tokens:
            for t in tokens:
                pass

    def handle_hidden_right(self, is_newline=False):
        tokens = self._stream.getHiddenTokensToRight(self._right_index)
        if tokens:
            for t in tokens:
                pass

    def abort(self):
        types_str = []
        token = self._stream.LT(2)
        expected = set(self._expected)
        for type in expected:
            types_str.append(LITERAL_NAMES[type])

        raise SyntaxException("Expecting one of " + ', '.join(types_str) + ' at line ' + str(token.line) + ', column ' + str(token.column))

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

        # optional ret stat
        stat = self.parse_ret_stat()
        if stat:
            statements.append(stat)
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
            return Do(stat)
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
            expr_list = self.parse_expr_list()  # optional
            # consume optional token
            if self.next_is(CTokens.SEMCOL):
                self.next_is_rc(CTokens.SEMCOL)

            self.success()
            return Return(expr_list)
        return self.failure()

    def parse_assignment(self):
        self.save()
        targets = self.parse_var_list()
        if targets:
            if self.next_is_rc(CTokens.ASSIGN):
                values = self.parse_expr_list()
                if values:
                    self.success()
                    return Assign(targets, values)
                else:
                    self.abort()

        return self.failure()

    def parse_var_list(self):
        vars = []
        self.save()
        var = self.parse_var()
        if var:
            vars.append(var)
            while True:
                self.save()
                if self.next_is_rc(CTokens.COMMA):
                    var = self.parse_var()
                    if var:
                        vars.append(var)
                        self.success()
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return vars
        return self.failure()

    def parse_var(self, is_stat=False):
        self.save()
        number_of_tail = 0
        root = self.parse_callee()

        # count number of tail and return callee if no tails
        if root:
            if self.parse_tail():
                number_of_tail += 1
                self.handle_hidden_right()
                while self.parse_tail():
                    self.handle_hidden_right()
                    number_of_tail += 1
            else:
                # only a callee
                self.success()
                return root

        # we have one callee or more
        self.failure_save()

        root = self.parse_callee()
        if root:
            for n in range(0, number_of_tail):
                tail = self.parse_tail()
                if isinstance(tail, Index):
                    tail.value = root
                elif isinstance(tail, Invoke):
                    tail.source = root
                elif isinstance(tail, Call):
                    tail.func = root
                else:
                    tail = Call(root, _listify(tail))
                root = tail
                if n < number_of_tail:
                    self.handle_hidden_right()

            self.handle_hidden_right()
            self.success()
            return root

        return self.failure()

    def parse_tail(self):
        # do not render last hidden
        self.save()
        if self.next_is_rc(CTokens.DOT) and self.next_is_rc(CTokens.NAME, False):
            self.success()
            return Index(Name(self.text), None)  # value must be set in parent

        self.failure_save()
        if self.next_is_rc(CTokens.OBRACK):
            expr = self.parse_expr()
            if expr and self.next_is_rc(CTokens.CBRACK, False):
                self.success()
                return Index(expr, None)  # value must be set in parent

        self.failure_save()
        if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME):
            name = Name(self.text)
            if self.next_is_rc(CTokens.OPAR):
                expr_list = self.parse_expr_list() or []
                if self.next_is_rc(CTokens.CPAR, False):
                    self.success()
                    return Invoke(None, name, expr_list)

        self.failure_save()
        if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME):
            name = Name(self.text)
            table = self.parse_table_constructor(False)
            if table:
                self.success()
                return Invoke(None, name, [table])

        self.failure_save()
        if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME):
            name = Name(self.text)
            if self.next_is_rc(CTokens.STRING, False):
                string = self.parse_lua_str(self.text)
                self.success()
                return Invoke(None, name, [string])

        self.failure_save()
        if self.next_is_rc(CTokens.OPAR, False):
            self.handle_hidden_right()
            expr_list = self.parse_expr_list() or []
            if self.next_is_rc(CTokens.CPAR, False):
                self.success()
                return Call(None, expr_list)

        self.failure_save()
        table = self.parse_table_constructor(False)
        if table:
            self.success()
            return table

        self.failure_save()
        if self.next_is_rc(CTokens.STRING, False):
            string = self.parse_lua_str(self.text)
            self.success()
            return string

        return self.failure()

    def parse_expr_list(self):
        expr_list = []
        self.save()
        expr = self.parse_expr()
        if expr:
            expr_list.append(expr)
            while True:
                self.save()
                if self.next_is_rc(CTokens.COMMA):
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

    def parse_do_block(self):
        self.save()
        if self.next_is_rc(CTokens.DO, False):
            self.handle_hidden_right()
            block = self.parse_block()
            if block:
                if self.next_is_rc(CTokens.END):
                    self.success()
                    return block
        return self.failure()

    def parse_while_stat(self):
        self.save()
        if self.next_is_rc(CTokens.WHILE):
            expr = self.parse_expr()
            if expr:
                body = self.parse_do_block()
                if body:
                    self.success()
                    return While(expr, body)

        return self.failure()

    def parse_repeat_stat(self):
        self.save()
        if self.next_is_rc(CTokens.REPEAT, False):
            self.handle_hidden_right()
            body = self.parse_block()
            if body:
                if self.next_is_rc(CTokens.UNTIL):
                    expr = self.parse_expr()
                    if expr:
                        self.success()
                        return Repeat(body, expr)

        return self.failure()

    def parse_local(self):
        self.save()
        self._expected = []
        if self.next_is_rc(CTokens.LOCAL):
            targets = self.parse_name_list()
            if targets:
                values = []
                self.save()
                if self.next_is_rc(CTokens.ASSIGN):
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
                return LocalAssign(targets, values)

            self.save()

            if self.next_is_rc(CTokens.FUNCTION) and self.next_is_rc(CTokens.NAME):
                name = Name(self.text)
                body = self.parse_func_body()
                if body:
                    self.success()
                    self.success()
                    return LocalFunction(name, body[0], body[1])
            self.failure()
            self.abort()

        return self.failure()

    def parse_goto_stat(self):
        self.save()
        if self.next_is_rc(CTokens.GOTO) and self.next_is_rc(CTokens.NAME):
            self.success()
            return Goto(Name(self.text))
        return self.failure()

    def parse_if_stat(self):
        self.save()
        if self.next_is_rc(CTokens.IFTOK):
            test = self.parse_expr()
            if test:
                if self.next_is_rc(CTokens.THEN, False):
                    self.handle_hidden_right()
                    body = self.parse_block()
                    if body:
                        main = If(test, body, None)
                        root = main
                        while True:  # zero or more
                            orelse = self.parse_elseif_stat()
                            if not orelse:
                                break
                            else:
                                root.orelse = orelse
                                root = orelse

                        else_exp = self.parse_else_stat()  # optional
                        root.orelse = else_exp
                        if self.next_is_rc(CTokens.END):
                            self.success()
                            return main
        return self.failure()

    def parse_elseif_stat(self):
        self.save()
        if self.next_is_rc(CTokens.ELSEIF):
            test = self.parse_expr()
            if test:
                if self.next_is_rc(CTokens.THEN, False):
                    self.handle_hidden_right()
                    body = self.parse_block()
                    if body:
                        self.success()
                        return ElseIf(test, body, None)  # orelse will be set in parent
        return self.failure()

    def parse_else_stat(self):
        self.save()
        if self.next_is(CTokens.ELSETOK):
            if self.next_is_rc(CTokens.ELSETOK, False):
                self.handle_hidden_right()
                body = self.parse_block()
                if body:
                    self.success()
                    return body
        return self.failure()

    def  parse_for_stat(self):
        self.save()
        if self.next_is_rc(CTokens.FOR):
            self.save()
            if self.next_is_rc(CTokens.NAME):
                target = Name(self.text)
                if self.next_is_rc(CTokens.ASSIGN):
                    start = self.parse_expr()
                    if start and self.next_is_rc(CTokens.COMMA):
                        stop = self.parse_expr()
                        if stop:
                            step = 1
                            # optional step
                            if self.next_is(CTokens.COMMA) and self.next_is_rc(CTokens.COMMA):
                                step = self.parse_expr()

                            body = self.parse_do_block()
                            if not body:
                                self.failure()
                                return self.failure()
                            self.success()
                            self.success()
                            return Fornum(target, start, stop, step, body)

            self.failure_save()
            target = self.parse_name_list()
            if target and self.next_is_rc(CTokens.IN):
                iter = self.parse_expr_list()
                if iter:
                    body = self.parse_do_block()
                    if body:
                        self.success()
                        self.success()
                        return Forin(body, iter, target)
            self.failure()

        return self.failure()

    def parse_function(self):
        self.save()
        self._expected = []
        if self.next_is_rc(CTokens.FUNCTION):
            names = self.parse_names()
            if names:
                self.save()
                if self.next_is_rc(CTokens.COL) and self.next_is_rc(CTokens.NAME):
                    name = Name(self.text)
                    func_body = self.parse_func_body()
                    if func_body:
                        self.success()
                        self.success()
                        return Method(names, name, func_body[0], func_body[1])

                self.failure()

                func_body = self.parse_func_body()
                if func_body:
                    return Function(names, func_body[0], func_body[1])
            self.abort()

        return self.failure()



    def parse_names(self):
        self.save()
        if self.next_is_rc(CTokens.NAME):
            child = Name(self.text)
            while True:
                self.save()
                if self.next_is_rc(CTokens.DOT) and self.next_is_rc(CTokens.NAME):
                    self.success()
                    child = Index(Name(self.text), child)
                else:
                    self.failure()
                    break
            self.success()
            return child
        self.failure()

    def parse_func_body(self):
        """If success, return a tuple (args, body)"""
        self.save()
        self._expected = []
        if self.next_is_rc(CTokens.OPAR, False):  # do not render right hidden
            self.handle_hidden_right()  # render hidden after new level
            args = self.parse_param_list()
            if args is not None:  # may be an empty table
                if self.next_is_rc(CTokens.CPAR, False):  # do not render right hidden
                    self.handle_hidden_right()  # render hidden after new level
                    body = self.parse_block()
                    if body:
                        self._expected = []
                        if self.next_is_rc(CTokens.END):
                            self.success()
                            return args, body
                        else:
                            self.abort()
                else:
                    self.abort()
        return self.failure()

    def parse_param_list(self):
        param_list = self.parse_name_list()
        if param_list:
            self.save()
            if self.next_is_rc(CTokens.COMMA) and \
                    self.next_is_rc(CTokens.VARARGS):
                self.success()
                param_list.append(Varargs())
                return param_list
            else:
                self.failure()
                return param_list

        self.save()
        if self.next_is_rc(CTokens.VARARGS):
            self.success()
            return [Varargs()]

        self.success()
        return []

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
        if self.next_is_rc(CTokens.COLCOL) and self.next_is_rc(CTokens.NAME):
            name = Name(self.text)
            if self.next_is_rc(CTokens.COLCOL):
                self.success()
                return Label(name)

        return self.failure()

    def parse_callee(self):
        self.save()
        if self.next_is_rc(CTokens.OPAR):
            expr = self.parse_expr()
            if expr:
                if self.next_is_rc(CTokens.CPAR):
                    self.success()
                    # TODO: create a node to indicate parenthesis
                    return expr
        self.failure()
        self.save()
        if self.next_is_rc(CTokens.NAME):
            self.success()
            return Name(self.text)
        return self.failure()

    def parse_expr(self):
        return self.parse_or_expr()

    def parse_or_expr(self):
        self.save()
        left = self.parse_and_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(CTokens.OR):
                    right = self.parse_and_expr()
                    if right:
                        self.success()
                        left = OrLoOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_and_expr(self):
        self.save()
        left = self.parse_rel_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(CTokens.AND):
                    right = self.parse_rel_expr()
                    if right:
                        self.success()
                        left = AndLoOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_rel_expr(self):
        self.save()
        left = self.parse_concat_expr()
        if left:
            self.save()
            if self.next_in_rc(self.REL_OPERATORS):
                op = self.type
                right = self.parse_concat_expr()
                if right:
                    self.success()
                    if op == CTokens.LT:
                        left = LessThanOp(left, right)
                    elif op == CTokens.GT:
                        left = GreaterThanOp(left, right)
                    elif op == CTokens.LTEQ:
                        left = LessOrEqThanOp(left, right)
                    elif op == CTokens.GTEQ:
                        left = GreaterOrEqThanOp(left, right)
                    elif op == CTokens.NEQ:
                        left = NotEqToOp(left, right)
                    elif op == CTokens.EQ:
                        left = EqToOp(left, right)
                else:
                    self.failure()
                    return self.failure()
            else:
                self.failure()
            self.success()
            return left
        return self.failure()

    def parse_concat_expr(self):
        self.save()
        left = self.parse_add_expr()
        if left:
            while True:
                self.save()
                if self.next_is_rc(CTokens.CONCAT):
                    self._expected = []
                    right = self.parse_add_expr()
                    if right:
                        self.success()
                        left = Concat(left, right)
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

    def parse_add_expr(self):
        self.save()
        left = self.parse_mult_expr()
        if left:
            while True:
                self.save()
                if self.next_in_rc([CTokens.ADD, CTokens.MINUS]):
                    op = self.type
                    right = self.parse_mult_expr()
                    if right:
                        self.success()
                        if op == CTokens.ADD:
                            left = AddOp(left, right)
                        elif op == CTokens.MINUS:
                            left = SubOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_mult_expr(self):
        self.save()
        left = self.parse_bitwise_expr()
        if left:
            while True:
                self.save()
                if self.next_in_rc([CTokens.MULT,
                                   CTokens.DIV,
                                   CTokens.MOD,
                                   CTokens.FLOOR]):
                    op = self.type
                    right = self.parse_bitwise_expr()
                    if right:
                        self.success()
                        if op == CTokens.MULT:
                            left = MultOp(left, right)
                        elif op == CTokens.DIV:
                            left = FloatDivOp(left, right)
                        elif op == CTokens.MOD:
                            left = ModOp(left, right)
                        elif op == CTokens.FLOOR:
                            left = FloorDivOp(left, right)
                    else:
                        self.failure()
                        return self.failure()
                else:
                    self.failure()
                    break
            self.success()
            return left

        return self.failure()

    def parse_bitwise_expr(self):
        self.save()
        left = self.parse_unary_expr()
        if left:
            while True:
                self.save()
                if self.next_in_rc([CTokens.BITAND,
                                    CTokens.BITOR,
                                    CTokens.BITNOT,
                                    CTokens.BITRSHIFT,
                                    CTokens.BITRLEFT]):
                    op = self.type
                    right = self.parse_unary_expr()
                    if right:
                        self.success()
                        if op == CTokens.BITAND:
                            left = BAndOp(left, right)
                        elif op == CTokens.BITOR:
                            left = BOrOp(left, right)
                        elif op == CTokens.BITNOT:
                            left = BXorOp(left, right)
                        elif op == CTokens.BITRSHIFT:
                            left = BShiftROp(left, right)
                        elif op == CTokens.BITRLEFT:
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

    def parse_unary_expr(self):
        self.save()
        if self.next_is_rc(CTokens.MINUS):
            expr = self.parse_unary_expr()
            if expr:
                self.success()
                return UMinusOp(expr)

        self.failure_save()
        if self.next_is_rc(CTokens.LENGTH):
            expr = self.parse_pow_expr()
            if expr:
                self.success()
                return ULengthOP(expr)

        self.failure_save()
        if self.next_is_rc(CTokens.NOT):
            expr = self.parse_unary_expr()
            if expr:
                self.success()
                return ULNotOp(expr)

        self.failure_save()
        if self.next_is_rc(CTokens.BITNOT):
            expr = self.parse_unary_expr()
            if expr:
                self.success()
                return UBNotOp(expr)

        self.failure_save()
        expr = self.parse_pow_expr()
        if expr:
            self.success()
            return expr

        return self.failure()

    def parse_pow_expr(self):
        self.save()
        left = self.parse_atom()
        if left:
            while True:
                self.save()
                if self.next_is_rc(CTokens.POW):
                    right = self.parse_atom()
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

    def parse_atom(self):
        atom = self.parse_var()
        if atom:
            return atom
        atom = self.parse_function_literal()
        if atom:
            return atom
        atom = self.parse_table_constructor()
        if atom:
            return atom
        if self.next_is(CTokens.VARARGS) and self.next_is_rc(CTokens.VARARGS):
            return Varargs()

        if self.next_is(CTokens.NUMBER) and self.next_is_rc(CTokens.NUMBER):
            # TODO: optimize
            # using python number eval to parse lua number
            try:
                number = ast.literal_eval(self.text)
            except:
                # exception occurs with leading zero number: 002
                number = float(self.text)
            return Number(number)

        if self.next_is(CTokens.STRING) and self.next_is_rc(CTokens.STRING):
            return self.parse_lua_str(self.text)

        if self.next_is(CTokens.NIL) and self.next_is_rc(CTokens.NIL):
            return Nil()

        if self.next_is(CTokens.TRUE) and self.next_is_rc(CTokens.TRUE):
            return TrueExpr()

        if self.next_is(CTokens.FALSE) and self.next_is_rc(CTokens.FALSE):
            return FalseExpr()
        return None

    def parse_lua_str(self, lua_str):
        p = re.compile(r'^\[=+\[(.*)\]=+\]')  # nested quote pattern
        # try remove double quote:
        if lua_str.startswith('"') and lua_str.endswith('"'):
            lua_str = lua_str[1:-1]
        # try remove single quote:
        elif lua_str.startswith("'") and lua_str.endswith("'"):
            lua_str = lua_str[1:-1]
        # try remove double square bracket:
        elif lua_str.startswith("[[") and lua_str.endswith("]]"):
            lua_str = lua_str[2:-2]
        # nested quote
        elif p.match(lua_str):
            lua_str = p.search(lua_str).group(1)
        return String(lua_str)

    def parse_function_literal(self):
        self.save()
        if self.next_is_rc(CTokens.FUNCTION):
            func_body = self.parse_func_body()
            if func_body:
                self.success()
                return AnonymousFunction(func_body[0], func_body[1])

        return self.failure()

    def parse_table_constructor(self, render_last_hidden=True):
        self.save()
        if self.next_is_rc(CTokens.OBRACE, False):  # do not render right hidden
            self.handle_hidden_right()  # render hidden after new level

            field_list = self.parse_field_list()
            if self.next_is_rc(CTokens.CBRACE, render_last_hidden):
                self.success()

                keys = []
                values = []
                table_index = 1
                if field_list:  # optional
                    for pair in field_list:
                        if pair[0] is None:
                            keys.append(Number(table_index))
                            table_index += 1
                        else:
                            keys.append(pair[0])
                        values.append(pair[1])

                return Table(keys, values)

        return self.failure()

    def parse_field_list(self):
        field_list = []
        self.save()
        field = self.parse_field()
        if field:
            field_list.append(field)
            while True:
                self.save()
                # if check_field_list, no space is allowed between COMMA and key
                if self.next_in_rc([CTokens.COMMA, CTokens.SEMCOL]):
                    field = self.parse_field()
                    if field:
                        field_list.append(field)
                        self.success()
                    else:
                        self.success()
                        self.success()
                        return field_list
                else:
                    self.failure()
                    break
            self.parse_field_sep()
            self.success()
            return field_list
        return self.failure()

    def parse_field(self):
        self.save()
        if self.next_is_rc(CTokens.OBRACK):
            key = self.parse_expr()
            if key and self.next_is_rc(CTokens.CBRACK):
                if self.next_is_rc(CTokens.ASSIGN):
                    value = self.parse_expr()
                    if value:
                        self.success()
                        return key, value

        self.failure_save()
        if self.next_is_rc(CTokens.NAME):
            key = Name(self.text)
            if self.next_is_rc(CTokens.ASSIGN):
                value = self.parse_expr()
                if value:
                    self.success()
                    return key, value

        self.failure_save()
        value = self.parse_expr()
        if value:
            self.success()
            return None, value

        return self.failure()

    def parse_field_sep(self):
        self.save()
        if self.next_in_rc([CTokens.COMMA, CTokens.SEMCOL]):
            return self.success()
        return self.failure()
