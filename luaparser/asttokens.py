from antlr4 import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.astnodes import *
from luaparser.parser.LuaParser import LuaParser
import llist
from enum import Enum


def parse(source):
    lexer = LuaLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    parser.chunk()
    tokens = stream.tokens
    return ProgramEditor(tokens)

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
    NEWLINE = 62
    SHEBANG = 63
    LongBracket = 64

class TokensEditor():
    """Initialize a token list editor.
    :param dllTokensToEdit: a list or a double linked list of token to edit"""
    def __init__(self, lTokensToEdit):
        # sort tokens by index and create a double linked list with them
        self._dllTokens = []
        if isinstance(lTokensToEdit, list):
            if lTokensToEdit:
                if isinstance(lTokensToEdit[0], llist.dllistnode):
                    self._dllTokens = lTokensToEdit
                else:
                    # we create a double linked list of token,
                    # to be able to navigate node with next, prev
                    # keep a ref on this ddlist to keep next, prev working
                    self._rawLlTokens = llist.dllist()
                    for token in lTokensToEdit:
                        self._rawLlTokens.append(token)
                    # and we store need nodes in a normal list
                    node = self._rawLlTokens.first
                    while node:
                        self._dllTokens.append(node)
                        node = node.next
        else:
            raise TypeError('lTokensToEdit must be none or a list of token or dllistnode')

    def __iter__(self):
        return iter(self._dllTokens)

    def __len__(self):
        return len(self._dllTokens)

    def __getitem__(self, i):
        return TokenEditor(self._dllTokens[i])

    def toSource(self):
        return TokenPrinter().toStr([t.value for t in self._dllTokens])

    def tokensEnumToValues(self, ltypes):
        types = []
        # convert enum to int value
        if not isinstance(ltypes, list):
            types = [ltypes.value]
        else:
            for t in ltypes:
                types.append(t.value)
        return types


class TokenEditor():
    """Utility class to edit a specific token.
    """
    def __init__(self, dllnodeTokenToEdit):
        assert isinstance(dllnodeTokenToEdit, llist.dllistnode)
        self._dllTokens = dllnodeTokenToEdit

    def toSource(self):
        return self._dllTokens.value.text

    def next(self):
        """Select next token.
        """
        node = self._dllTokens.next
        if node:
            return TokenEditor(node)
        return node

    def prev(self):
        """Select previous token.
        """
        node = self._dllTokens.prev
        if node:
            return TokenEditor(node)
        return node

    def nextOfType(self, type):
        node = self._dllTokens.next
        while node:
            if node.value.type == type.value:
                return TokenEditor(node)
            node = node.next
        return None

    def prevOfType(self, type):
        node = self._dllTokens.prev
        while node:
            if node.value.type == type.value:
                return TokenEditor(node)
            node = node.prev
        return None

    def __str__(self):
        return str(self._dllTokens.value)

    def __eq__(self, other):
        return isinstance(other, TokenEditor) and self._dllTokens.value == other._dllTokens.value

    def line(self):
        """Retrieve the line editor for this token."""
        # tokens are ordered by line
        line = self._dllTokens.value.lineNumber
        tokens = llist.dllist()
        # append on the left nodes before
        node = self._dllTokens.prev
        while node:
            if node.value.type != Tokens.NEWLINE.value:
                tokens.appendleft(node)
            else: break
            node = node.prev
        # append self
        tokens.append(self._dllTokens)
        # append nodes after
        node = self._dllTokens.next
        while node:
            if node.value.type != Tokens.NEWLINE.value:
                tokens.append(node)
            else:
                break
            node = node.next
        return LineEditor(tokens)

    def isFirstOnLine(self):
        if self._dllTokens.prev:
            # check if token before is on the same line
            return self._dllTokens.value.lineNumber != self._dllTokens.prev.value.lineNumber
        return True

    def grabUntil(self, type):
        """Starting from self, return a list of tokens until the specified type if found"""
        tokens = llist.dllist()
        node = self._dllTokens.next
        while node:
            tokens.append(node)
            if node.value.type == type.value:
                break
            node = node.next
        return GroupEditor(tokens)

    @property
    def text(self):
        return self._dllTokens.value.text

    @text.setter
    def text(self, text):
        self._dllTokens.value.text = text

    @property
    def lineNumber(self):
        return self._dllTokens.value.line

    @property
    def column(self):
        return self._dllTokens.value.column

    @property
    def type(self):
        return self._dllTokens.value.type


class GroupEditor(TokensEditor):
    def lineCount(self):
        count = 0
        if self._dllTokens: count += 1
        for node in self._dllTokens:
            if node.value.type == Tokens.NEWLINE.value:
                count += 1
        return count

    def lines(self):
        nodes = []
        for node in self._dllTokens:
            nodes.append(node)
            if node.value.type == Tokens.NEWLINE.value:
                yield LineEditor(nodes)
                nodes = []
        # yield last line
        if nodes: yield LineEditor(nodes)

    def types(self, ltypes):
        types = self.tokensEnumToValues(ltypes)
        nodes = []
        for token in self._dllTokens:
            if token.value.type in types:
                nodes.append(token)
        return GroupEditor(nodes)

    def first(self):
        """Retrieve the first token of this group.
        """
        if self._dllTokens:
            return TokenEditor(self._dllTokens[0])
        return None

    def last(self):
        """Retrieve the last token of this group.
        """
        if self._dllTokens:
            return TokenEditor(self._dllTokens[-1])
        return None


class ProgramEditor(GroupEditor):
    def range(self, start, stop):
        nodes = []
        for node in self._dllTokens:
            if node.value.tokenIndex >= start and node.value.tokenIndex <= stop:
                nodes.append(node)
        return GroupEditor(nodes)

    def fromAST(self, node):
        return self.range(node.start, node.stop)


class LineEditor(GroupEditor):
    """Utility class to edit a list of token representing a program line.
    """
    def lstrip(self, ltypes = [Tokens.SPACE]):
        """Delete all left whitespace on a line.
        """
        types = self.tokensEnumToValues(ltypes)
        if self._dllTokens:
            node = self._dllTokens[0]
            while node:
                current = node
                node = node.next
                if current.value.type in types:
                    self._dllTokens.remove(current)
                else: break
            return self

    def indent(self, count):
        node = self._dllTokens.first
        if node:
            # already a SPACE token, use it
            if node.value.type == Tokens.SPACE.value:
                node.value.text = ' ' * count
            # need to create a new token




        self.stripl()
        first = self.first()
        if first is not None:
            first.column = count

    def delete(self):
        """Delete all tokens on this line."""
        if not self._dllTokens:
            return None
        currentLine = self._dllTokens[0].line
        nextLine = self.next()
        # delete tokens on line by creating a new list
        self._dllTokens = []
        # shift line under this one
        while nextLine is not None:
            first = nextLine.first()
            if first is not None:
                for t in nextLine:
                    t.lineNumber = first.lineNumber - 1
            nextLine = nextLine.next()

    @property
    def lineNumber(self):
        if self._dllTokens:
            return self._dllTokens[0].line


class TokenPrinter():
    """Class to render a token list to a string.
    """
    def toStr(self, tokens):
        source = "".join((t.text) for t in tokens)

        if source.endswith('<EOF>'):
            source = source[:-5]
        return source
