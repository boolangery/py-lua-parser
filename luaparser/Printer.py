#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``Printer`` module
    ==================

    Class used to pretty print AST.

"""
from enum import Enum
from luaparser.pprint.DefaultVisitor import DefaultVisitor
from luaparser.pprint.PythonStyleVisitor import PythonStyleVisitor
from luaparser.pprint.LuaStyleVisitor import LuaStyleVisitor


class PrinterException(Exception):
    def __init__(self, message):
        self.message = message

class Printer():
    class Style(Enum):
        DEFAULT = 0
        PYTHON  = 1
        LUA     = 2

    @staticmethod
    def pprint(ast, style = Style.PYTHON, indent=True, lineInfo=True, indentValue=2):
        print(Printer.toStr(ast, style, indent, lineInfo, indentValue))

    @staticmethod
    def toStr(ast, style = Style.PYTHON, indent=True, lineInfo=True, indentValue=2):
        visitor = None
        if style == Printer.Style.DEFAULT:
            visitor = DefaultVisitor(indent, lineInfo, indentValue)
        elif style == Printer.Style.PYTHON:
            visitor = PythonStyleVisitor(indent, lineInfo, indentValue)
        elif style == Printer.Style.LUA:
            visitor = LuaStyleVisitor(indent, lineInfo, indentValue)
        else:
            raise PrinterException('No such style: ' + str(style))
        return visitor.visit(ast)