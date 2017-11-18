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

    @visitor(float)
    def visit(self, node):
        return str(node)

    @visitor(int)
    def visit(self, node):
        return str(node)

    @visitor(list)
    def visit(self, node):
        return '[notHandled: ' + str(node) +  ']'

    @visitor(Node)
    def visit(self, node):
        if node.isTerm():
            res = '`' + node.name + ' "' + node.getValue() + '"'
        else:
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
            res += ' }'
        return res

