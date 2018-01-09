from antlr4 import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.astNodes import *
from luaparser.parser.LuaParser import LuaParser


def parse(source):
    lexer = LuaLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    parser.chunk()
    return stream.tokens
