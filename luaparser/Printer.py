#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ``Printer`` module
    ==================

    Class used to pretty print AST.

"""
from enum import Enum
from luaparser.pprint.DefaultVisitor import DefaultVisitor


class PrinterException(Exception):
    def __init__(self, message):
        self.message = message

class Printer():
    class Style(Enum):
        DEFAULT = 0
        METALUA = 1

    @staticmethod
    def toStr(ast, style = Style.DEFAULT, indent=False, indentValue=2):
        visitor = None
        if style == Printer.Style.DEFAULT:
            visitor = DefaultVisitor(indent, indentValue)
        elif style == Printer.Style.METALUA:
            visitor = MetaluaVisitor()
        else:
            raise PrinterException('No such style: ' + str(style))
        return visitor.visit(ast)