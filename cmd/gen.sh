#!/bin/zsh

java -jar ~/Downloads/antlr-4.13.2-complete.jar -visitor -Dlanguage=Python3 luaparser/parser/LuaLexer.g4 luaparser/parser/LuaParser.g4
