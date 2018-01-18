from antlr4 import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.astnodes import *
from luaparser.parser.LuaParser import LuaParser
from itertools import repeat
from enum import Enum


def parse(source):
    lexer = LuaLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    parser.chunk()
    tokens = stream.tokens
    return ProgramEditor(tokens, tokens)

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

class TokensEditor():
    def __init__(self, allTokens, tokensToEdit):
        # sort tokens by index:
        self._all = sorted(allTokens, key=lambda token: token.tokenIndex)
        self._tokens = tokensToEdit
        if isinstance(tokensToEdit, list):
            self._tokens = sorted(tokensToEdit, key=lambda token: token.tokenIndex)

    def __iter__(self):
        for token in self._tokens:
            yield TokenEditor(self._all, token)

    def __len__(self):
        return len(self._tokens)

    def __getitem__(self, i):
        return self._tokens[i]

    def toSource(self):
        return TokenPrinter().toStr(self._tokens)

class GroupEditor(TokensEditor):
    def lineCount(self):
        max = 0
        for token in self._tokens:
            if token.line > max:
                max = token.line
        return max

    def lines(self):
        lines = []
        count = self.lineCount()
        for i in range(1, count+1):
            # grab all token on line i
            ltokens = []
            for token in self._tokens:
                if token.line == i:
                    ltokens.append(token)
            if len(ltokens) > 0:
                lines.append(LineEditor(self._all, ltokens))
        return lines

    def types(self, types):
        _types = []
        # convert enum to int value
        if not isinstance(types, list):
            _types = [types.value]
        else:
            for t in types:
                _types.append(t.value)
        tokens = []
        for token in self._tokens:
            if token.type in _types:
                tokens.append(token)
        return GroupEditor(self._all, tokens)

    def first(self):
        """Retrieve the first token based on index.
        """
        if self._tokens:
            first = self._tokens[0]
            for token in self._tokens:
                if token.tokenIndex < first.tokenIndex:
                    first = token
            return TokenEditor(self._all, first)
        return None

    def last(self):
        # tokens are ordered by tokenIndex
        if self._tokens:
            return TokenEditor(self._all, self._tokens[-1])
        return None

    def __getitem__(self, key):
        if isinstance(key, slice):
            return GroupEditor(self._all, self._tokens[key])
        return TokenEditor(self._all, self._tokens[key])

class ProgramEditor(GroupEditor):
    def range(self, start, stop):
        tokens = []
        for token in self._tokens:
            if token.tokenIndex >= start and token.tokenIndex <= stop:
                tokens.append(token)
        return GroupEditor(self._all, tokens)

    def fromAST(self, node):
        return self.range(node.start, node.stop)

class TokenEditor(TokensEditor):
    """Utility class to edit a specific token.
    """
    def next(self):
        """Select next token.
        """
        # tokens are sorted by index
        for i, t in enumerate(self._all):
            if t.tokenIndex == self._tokens.tokenIndex:
                # return next element:
                if (i+1) < len(self._all):
                    return TokenEditor(self._all, self._all[i+1])
                else:
                    return None
        return None

    def prev(self):
        """Select previous token.
        """
        # tokens are sorted by index
        for i, t in enumerate(self._all):
            if t.tokenIndex == self._tokens.tokenIndex:
                # return previous element if exist:
                if (i-1) > 0:
                    return TokenEditor(self._all, self._all[i-1])
                else:
                    return None
        return None

    def nextOfType(self, type):
        next = self.next()
        while next is not None:
            if next.type == type.value:
                return next
            next = next.next()
        return None

    def prevOfType(self, type):
        prev = self.prev()
        while prev is not None:
            if prev.type == type.value:
                return prev
            prev = prev.prev()
        return None

    def __str__(self):
        return str(self._tokens)

    def __eq__(self, other):
        return isinstance(other, TokenEditor) and self._tokens == other._tokens

    def line(self):
        """Retrieve the line editor for this token."""
        tokens = []
        for t in self._all:
            if t.line == self._tokens.line:
                tokens.append(t)
        return LineEditor(self._all, tokens)

    def isFirstOnLine(self):
        line = self.line()
        return self == line.first()

    def grabUntil(self, type):
        """Starting from self, return a list of tokens until the specified type if found"""
        tokens = [self._tokens] # include this token
        for t in self._all:
            if t.tokenIndex > self._tokens.tokenIndex:
                if t.type != type.value:
                    tokens.append(t)
                else:
                    tokens.append(t)
                    break
        return GroupEditor(self._all, tokens)


    @property
    def text(self):
        return self._tokens.text

    @text.setter
    def text(self, text):
        # compute text len diff
        diff = len(text) - len(self._tokens.text)
        self._tokens.text = text
        # apply offset to next token
        next = self.next()
        if next is not Node:
            next.column = next.column + diff

    @property
    def lineNumber(self):
        return self._tokens.line

    @lineNumber.setter
    def lineNumber(self, value):
        self._tokens.line = value

    @property
    def column(self):
        return self._tokens.column

    @column.setter
    def column(self, column):
        """Set column and modify all token on the same line.
        """
        diff = column - self._tokens.column
        self._tokens.column = column
        if diff != 0:
            for t in self._all:
                if t.tokenIndex > self._tokens.tokenIndex:
                    if t.line == self._tokens.line:
                        t.column += diff

    @property
    def type(self):
        return self._tokens.type

class LineEditor(GroupEditor):
    """Utility class to edit a list of token representing a program line.
    """
    def next(self):
        """Get next line editor on None if no new line."""
        if not self._tokens:
            return None
        tokens = []
        for t in self._all:
            if t.line == (self._tokens[0].line + 1):
                tokens.append(t)
        if not tokens:
            return None
        return LineEditor(self._all, tokens)

    def stripl(self):
        """Delete all left whitespace on a line.
        """
        first = self.first()
        if first != None:
            first.column = 0

    def indent(self, count):
        self.stripl()
        first = self.first()
        if first is not None:
            first.column = count

    def delete(self):
        """Delete all tokens on this line."""
        if not self._tokens:
            return None
        currentLine = self._tokens[0].line
        nextLine = self.next()
        # delete tokens on line by creating a new list
        self._all[:] = [token for token in self._all if token.line == currentLine]
        self._tokens = []
        # shift line under this one
        while nextLine is not None:
            first = nextLine.first()
            if first is not None:
                for t in nextLine:
                    t.lineNumber = first.lineNumber - 1
            nextLine = nextLine.next()

    def toSource(self):
        line = TokenPrinter().toStr(self._tokens)
        return line.strip()

    @property
    def lineNumber(self):
        if self._tokens:
            return self._tokens[0].line


class TokenPrinter():
    """Class to render a token list to a string.
    """
    def toStr(self, tokens):
        lines = []
        for token in tokens:
            # extend current source:
            if token.line > len(lines):
                lines.extend(repeat('', (token.line - len(lines))))

            # Insert in source line:
            line = token.line -1
            text = token.text
            position = token.column
            s = lines[line]
            # extend string
            if position > len(s):
                s += ' ' * (position - len(s))
            # Use slicing to extract portion to replace:
            s = s[:position] + text + s[position+len(text):]
            lines[line] = s

        source = '\n'.join(lines)
        if source.endswith('<EOF>'):
            source = source[:-5]
        return source
