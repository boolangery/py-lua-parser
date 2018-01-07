from luaparser.astNodes import *
from luaparser.visitor import *


class LuaStyleVisitor():
    def __init__(self, indent, lineInfo, indentValue):
        self.indentEnabled = indent
        self.lineInfo = lineInfo
        self.indentValue = indentValue
        self.currentIndent = 0

    def indentStr(self, newLine=True):
        res = ''
        if self.indentEnabled:
            res =  ' ' * self.currentIndent
        if newLine:
            res = '\n' + res
        return res

    def indent(self):
        if self.indentEnabled:
            self.currentIndent += self.indentValue

    def dedent(self):
        if self.indentEnabled:
            self.currentIndent -= self.indentValue

    def visitList(self, nodes):
        visited = []
        for node in nodes:
            visited.append(self.visit(node))
        return visited

    @visitor(Chunk)
    def visit(self, node):
        return self.visit(node.body)

    @visitor(Block)
    def visit(self, node):
        return '\n'.join(self.visitList(node.body))

    @visitor(NameExpr)
    def visit(self, node):
        return node.id

    @visitor(NumberExpr)
    def visit(self, node):
        return str(node.n)

    @visitor(StringExpr)
    def visit(self, node):
        return "'" + str(node.s) + "'"

    @visitor(AssignStat)
    def visit(self, node):
        return ' '.join([', '.join(self.visitList(node.targets)), '=', ', '.join(self.visitList(node.values))])

    @visitor(LocalAssignStat)
    def visit(self, node):
        return ' '.join(['local', ', '.join(self.visitList(node.targets)), '=', ', '.join(self.visitList(node.values))])

    @visitor(TableExpr)
    def visit(self, node):
        pairs = []
        for k in range(0, len(node.keys)):
            pairs.append(' '.join([self.visit(node.keys[k]), '=', self.visit(node.values[k])]))
        return '{' + '\n'.join(pairs) + '}'
