from luaparser.astNodes import *
from luaparser.visitor import *


class DefaultVisitor():
    def __init__(self, indent, indentValue):
        self.indent = indent
        self.indentValue = indentValue
        self.currentIndent = 0

    @visitor(str)
    def visit(self, node):
        if node.startswith('"') and node.endswith('"'):
            node = node[1:-1]
        return '"' + node + '"'

    @visitor(list)
    def visit(self, node):
        return 'list'

    @visitor(Node)
    def visit(self, node):
        res = '`' + node.name + '{ '
        if self.indent:
            self.currentIndent += self.indentValue
            res += '\n' + ' ' * self.currentIndent
        if len(node.childs)>0:
            for child in node.childs:
                res += self.visit(child) + ', '
            res = res[:-2]
        if self.indent:
            self.currentIndent -= self.indentValue
            res += '\n' + ' ' * self.currentIndent
        return res + ' }'

