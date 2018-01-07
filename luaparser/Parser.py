#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``Parser`` module
    =================

    Main library entry point.

"""
from antlr4 import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaParser import LuaParser
from luaparser.LuaAstBuilder import ParseTreeVisitor



class Parser():
    def srcToParseTree(self, str):
        """
        Convert Lua source string to antlr4 parse tree.
        :param str: Lua source
        :return: An antlr4 parse tree
        """
        lexer = LuaLexer(InputStream(str))
        parser = LuaParser(CommonTokenStream(lexer))
        return parser.chunk()

    def srcToTokens(self, str):
        lexer = LuaLexer(InputStream(str))
        stream = CommonTokenStream(lexer)
        parser = LuaParser(stream)
        parser.chunk()
        return stream.tokens

    def fileToParseTree(self, filepath):
        """
        Convert Lua source file to antlr4 parse tree.
        :param str: Lua source file
        :return: An antlr4 parse tree
        """
        lexer = LuaLexer(FileStream(filepath))
        parser = LuaParser(CommonTokenStream(lexer))
        return parser.chunk()

    def srcToAST(self, str):
        """
        Convert Lua source string to an AST.
        :param str: Lua source
        :return: builded AST
        """
        parseTree = self.srcToParseTree(str)
        astVisitor = ParseTreeVisitor()
        return astVisitor.visit(parseTree)

    def fileToAST(self, filepath):
        """
        Convert Lua source file to an AST.
        :param str: Lua source file
        :return: builded AST
        """
        parseTree = self.fileToParseTree(filepath)
        astVisitor = ParseTreeVisitor()
        return astVisitor.visit(parseTree)
