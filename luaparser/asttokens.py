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
    AND = 1
    BREAK = 2
    DO = 3
    ELSE = 4
    ELSEIF = 5
    END = 6
    FALSE = 7
    FOR = 8
    FUNCTION = 9
    GOTO = 10
    IF = 11
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
    SHEBANG = 62
    LongBracket = 63

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
