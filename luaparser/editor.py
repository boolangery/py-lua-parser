from luaparser.pprint.TokenPrinter import TokenPrinter
from enum import Enum

class Tokens(Enum):
    NIL = 1
    FALSE = 2
    TRUE = 3
    BREAK = 4
    GOTO = 5
    DO = 6
    WHILE = 7
    END = 8
    REPEAT = 9
    UNTIL = 10
    IF = 11
    FOR = 12
    LOCAL = 13
    FUNCTION = 14
    THEN = 15
    ELSE = 16
    ELSEIF = 17
    IN = 18
    RETURN = 19
    VARARGS = 20
    NOT = 21
    EQUAL = 22
    INDEX = 23
    COMMA = 24
    COLON = 25
    SEMI_COLON = 26
    LABEL = 27
    PARENT_R = 28
    PARENT_L = 29
    BRACE_R = 30
    BRACE_L = 31
    SQUARE_R = 32
    SQUARE_L = 33
    OP_LENGTH = 34
    OP_MINUS = 35
    OP_BIT_NOT = 36
    OP_ADD = 37
    OP_MULT = 38
    OP_FLOAT_DIV = 39
    OP_FLOOR_DIV = 40
    OP_MOD = 41
    OP_BIT_AND = 42
    OP_BIT_OR = 43
    OP_BIT_SR = 44
    OP_BIT_SL = 45
    OP_EXP = 46
    OP_CONCAT = 47
    OP_LT = 48
    OP_GT = 49
    OP_LTE = 50
    OP_GTE = 51
    OP_NEQ = 52
    OP_EQ = 53
    AND = 54
    OR = 55
    NAME = 56
    STRING = 57
    INT = 58
    HEX = 59
    FLOAT = 60
    HEX_FLOAT = 61
    COMMENT = 62
    LINE_COMMENT = 63
    WS = 64
    SHEBANG = 65

class TokenEditor():
    def __init__(self, programTokens, token):
        self._programTokens = programTokens
        self._token = token

    def setText(self, text):
        lenDiff = len(self._token.text) - len(text)
        self._token.text = text
        self.columnOffset(lenDiff)

    def columnOffset(self, offset):
        for t in self._programTokens:
            if t.tokenIndex > self._token.tokenIndex:
                if t.line == self._token.line:
                    t.column += offset

    @property
    def text(self):
        return self._token.text

    @property
    def line(self):
        return self._token.line

    @property
    def column(self):
        return self._token.column


class TokenGroupEditor():
    def __init__(self, programTokens, tokens):
        self._programTokens = programTokens
        self._tokens = tokens

    def setText(self, text):
        for token in self._tokens:
            TokenEditor(self._programTokens, token).setText(text)


class ProgramEditor():
    def __init__(self, programTokens, toEdit=None):
        self._programTokens = programTokens
        if toEdit == None:
            self._toEdit = programTokens
        else:
            if isinstance(toEdit, list):
                self._toEdit = toEdit
            else:
                self._toEdit = [toEdit]

    def toStr(self):
        return TokenPrinter().toStr(self._programTokens)

    def wrap(self, tokens):
        if isinstance(tokens, list):
            if len(tokens) == 1:
                return TokenEditor(self._programTokens, tokens[0])
            else:
                wrappers = []
                for token in tokens:
                    wrappers.append(TokenEditor(self._programTokens, token))
                return wrappers
        else:
            return TokenEditor(self._programTokens, tokens)

    def edit(self):
        return self.wrap(self._toEdit)

    def _raw(self):
        return self._toEdit

    def findByTypes(self, types):
        tokens = []
        for token in self._toEdit:
            if token.type in types:
                tokens.append(token)
        return ProgramEditor(self._programTokens, tokens)

    def findByLine(self, line):
        tokens = []
        for token in self._toEdit:
            if token.line == line:
                tokens.append(token)
        return ProgramEditor(self._programTokens, tokens)

    def findByMinColumn(self):
        min = 1000000
        first = None
        for token in self._toEdit:
            if token.column < min:
                min = token.column
                first = token
        return ProgramEditor(self._programTokens, first)

    def stripLeftLine(self, line):
        token = self.findFirstOnLine(line).edit()
        if token:
            token[0].columnOffset(-token[0].column)

    def indentLine(self, line, count):
        self.stripLeftLine(line)
        token = self.findFirstOnLine(line).edit()
        if token :
            token[0].columnOffset(count)

    @property
    def lineCount(self):
        max = 0
        for token in self._toEdit:
            if token.line > max:
                max = token.line
        return max