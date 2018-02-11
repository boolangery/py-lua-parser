from antlr4 import *
from antlr4.Token import CommonToken
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

    dlltokens = llist.dllist()
    for t in tokens:
        dlltokens.append(t)
    return ProgramEditor(None, dlltokens)

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

DEFAULT_IGNORE = [Tokens.SPACE, Tokens.NEWLINE, Tokens.SHEBANG]

class AbstractTokensEditor():
    def tokensEnumToValues(self, ltypes):
        types = []
        # convert enum to int value
        if not isinstance(ltypes, list):
            types = [ltypes.value]
        else:
            for t in ltypes:
                types.append(t.value)
        return types

class TokensEditor(AbstractTokensEditor):
    """Initialize a token list editor.
    :param dllTokensToEdit: a list or a double linked list of token to edit"""
    def __init__(self, lTokensToEdit, dllAll):
        # sort tokens by index and create a double linked list with them
        self._dllTokens = []
        self._dllAll = llist.dllist()

        # initialization
        if lTokensToEdit is None:
            assert isinstance(dllAll, llist.dllist)
            for token in dllAll:
                self._dllAll.append(token)
            # and we store needed nodes in a normal list
            node = self._dllAll.first
            while node:
                self._dllTokens.append(node)
                node = node.next
        else:
            assert isinstance(dllAll, llist.dllist)
            assert isinstance(lTokensToEdit, list)
            if lTokensToEdit:
                assert isinstance(lTokensToEdit[0], llist.dllistnode)
            self._dllTokens = lTokensToEdit
            self._dllAll = dllAll

    def __iter__(self):
        for node in self._dllTokens:
            yield TokenEditor(node, self._dllAll)

    def __len__(self):
        return len(self._dllTokens)

    def __getitem__(self, i):
        return TokenEditor(self._dllTokens[i], self._dllAll)

    def toSource(self):
        return TokenPrinter().toStr([t.value for t in self._dllTokens])

    def allToSource(self):
        return TokenPrinter().toStr([t for t in self._dllAll])

class TokenEditor(AbstractTokensEditor):
    """Utility class to edit a specific token.
    """
    def __init__(self, dllnodeTokenToEdit, dllAll):
        assert isinstance(dllnodeTokenToEdit, llist.dllistnode)
        assert isinstance(dllAll, llist.dllist)
        self._dllTokens = dllnodeTokenToEdit
        self._dllAll = dllAll

    def toSource(self):
        return self._dllTokens.value.text

    def next(self, lignore=DEFAULT_IGNORE):
        """Select next token.
        """
        types = self.tokensEnumToValues(lignore)
        node = self._dllTokens.next
        while node:
            if node.value.type not in types:
                return TokenEditor(node, self._dllAll)
            node = node.next
        return None

    def prev(self, lignore=DEFAULT_IGNORE):
        """Select previous token.
        """
        types = self.tokensEnumToValues(lignore)
        node = self._dllTokens.prev
        while node:
            if node.value.type not in types:
                return TokenEditor(node, self._dllAll)
            node = node.prev
        return None

    def nextOfType(self, type):
        node = self._dllTokens.next
        while node:
            if node.value.type == type.value:
                return TokenEditor(node, self._dllAll)
            node = node.next
        return None

    def prevOfType(self, type):
        node = self._dllTokens.prev
        while node:
            if node.value.type == type.value:
                return TokenEditor(node, self._dllAll)
            node = node.prev
        return None

    def __str__(self):
        return str(self._dllTokens.value)

    def __eq__(self, other):
        return isinstance(other, TokenEditor) and self._dllTokens.value == other._dllTokens.value

    def line(self):
        """Retrieve the line editor for this token."""
        # tokens are ordered by line
        line = self._dllTokens.value.line
        tokens = []
        # append on the left nodes before
        node = self._dllTokens.prev
        while node:
            if node.value.type != Tokens.NEWLINE.value:
                tokens.insert(0, node)
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
        return LineEditor(tokens, self._dllAll)

    def isFirstOnLine(self, lignore = DEFAULT_IGNORE):
        ignore = self.tokensEnumToValues(lignore)
        node = self._dllTokens.prev
        while node:
            if node.value.line == self._dllTokens.value.line:
                if node.value.type not in ignore:
                    return False
            node = node.prev
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
        return GroupEditor(tokens, self._dllAll)

    def insertLeft(self, type, text):
        token = CommonToken()
        token.type = type.value
        token.text = text
        token.line = self._dllTokens.value.line
        token.tokenIndex = self._dllTokens.value.tokenIndex
        inserted = self._dllAll.insert(token, self._dllTokens)
        return TokenEditor(inserted, self._dllAll)

    def insertRight(self, type, text):
        token = CommonToken()
        token.type = type.value
        token.text = text
        token.line = self._dllTokens.value.line
        token.tokenIndex = self._dllTokens.value.tokenIndex

        next = self._dllTokens.next
        if next:
            inserted = self._dllAll.insert(token, next)
        else:
            inserted = self._dllAll.append(token)
        return TokenEditor(inserted, self._dllAll)

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
                yield LineEditor(nodes, self._dllAll)
                nodes = []
        # yield last line
        if nodes: yield LineEditor(nodes, self._dllAll)

    def types(self, ltypes):
        types = self.tokensEnumToValues(ltypes)
        nodes = []
        for token in self._dllTokens:
            if token.value.type in types:
                nodes.append(token)
        return GroupEditor(nodes, self._dllAll)

    def lastOfType(self, type):
        for node in reversed(self._dllTokens):
            if node.value.type == type.value:
                return TokenEditor(node, self._dllAll)
        return None

    def lastOfNotType(self, ltypes):
        types = self.tokensEnumToValues(ltypes)
        for node in reversed(self._dllTokens):
            if node.value.type not in types:
                return TokenEditor(node, self._dllAll)
        return None

    def firstOfType(self, type):
        for node in self._dllTokens:
            if node.value.type == type.value:
                return TokenEditor(node, self._dllAll)
        return None

    def firstOfNotType(self, ltypes):
        types = self.tokensEnumToValues(ltypes)
        for node in self._dllTokens:
            if node.value.type not in types:
                return TokenEditor(node, self._dllAll)
        return None

    def first(self, lignore=DEFAULT_IGNORE):
        """Retrieve the first token of this group.
        """
        return self.firstOfNotType(lignore)

    def last(self, lignore=DEFAULT_IGNORE):
        """Retrieve the last token of this group.
        """
        return self.lastOfNotType(lignore)


class ProgramEditor(GroupEditor):
    def range(self, start, stop):
        nodes = []
        for node in self._dllTokens:
            if node.value.tokenIndex >= start and node.value.tokenIndex <= stop:
                nodes.append(node)
        return GroupEditor(nodes, self._dllAll)

    def fromAST(self, node):
        return self.range(node.start, node.stop)


class LineEditor(GroupEditor):
    """Utility class to edit a list of token representing a program line.
    """
    def lstrip(self, ltypes = [Tokens.SPACE]):
        """Delete all left whitespace on a line.
        """
        types = self.tokensEnumToValues(ltypes)
        nodesToDelete = []
        if self._dllTokens:
            for node in self._dllTokens:
                if node.value.type in types:
                    nodesToDelete.append(node)
                else: break
            # delete from dll list
            for node in nodesToDelete:
                self._dllTokens.remove(node)
                self._dllAll.remove(node)
        return self

    def rstrip(self, ltypes = [Tokens.SPACE], lignore = [Tokens.NEWLINE]):
        """Delete all right whitespace on a line.
        """
        types = self.tokensEnumToValues(ltypes)
        ignore = self.tokensEnumToValues(lignore)
        nodesToDelete = []
        if self._dllTokens:
            for node in reversed(self._dllTokens):
                if node.value.type in types:
                    nodesToDelete.append(node)
                elif node.value.type not in ignore:
                    break
            # delete from dll list
            for node in nodesToDelete:
                self._dllTokens.remove(node)
                self._dllAll.remove(node)
        return self

    def indent(self, count, indent_char=' ', lignore = [Tokens.NEWLINE]):
        node = self._dllTokens[0]

        if node:
            # already a SPACE token, use it
            if node.value.type == Tokens.SPACE.value:
                node.value.text = indent_char * count
            elif count != 0:
                editor = TokenEditor(node, self._dllAll)
                newEditor = editor.insertLeft(Tokens.SPACE, indent_char * count)
                self._dllTokens.insert(0, newEditor._dllTokens)

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

    def next(self):
        last = self.last()
        if last:
            firstOnNextLine = last.next()
            if firstOnNextLine:
                return firstOnNextLine.line()
        return None

    def nextLines(self):
        next = self.next()
        while next:
            yield next
            next = next.next()

    @property
    def lineNumber(self):
        if self._dllTokens:
            return self._dllTokens[0].value.line


class TokenPrinter():
    """Class to render a token list to a string.
    """
    def toStr(self, tokens):
        source = "".join((t.text) for t in tokens)

        if source.endswith('<EOF>'):
            source = source[:-5]
        return source
