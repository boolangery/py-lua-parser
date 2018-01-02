from luaparser.astNodes import *
from luaparser.visitor import *
from itertools import repeat

class LuaFidelityVisitor():
    def __init__(self, indent, lineInfo, indentValue):
        self.indentEnabled = indent
        self.lineInfo = lineInfo
        self.indentValue = indentValue
        self.currentIndent = 0
        self.lines = []

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


    def fidelityPrint(self, node):
        if isinstance(node, list):
            for n in node:
                self.fidelityPrint(n)
            return

        # extend current source:
        if node.line > len(self.lines):
            self.lines.extend(repeat('', (node.line - len(self.lines))))

        # Insert in source line:
        line = node.line -1
        text = self.visit(node)
        position = node.column
        s = self.lines[line]
        # extend string
        if position > len(s):
            s += ' ' * (position - len(s))

        # Use slicing to extract portion to replace:
        s = s[:position] + text + s[position+len(text):]
        self.lines[line] = s

    @visitor(Chunk)
    def visit(self, node):
        return self.visit(node.body)

    @visitor(Block)
    def visit(self, node):
        self.visitList(node.body)
        return '\n'.join(self.lines)
        # return '\n'.join(self.visitList(node.body))

    @visitor(NameExpr)
    def visit(self, node):
        return node.id

    @visitor(Symbol)
    def visit(self, node):
        return node.s

    @visitor(NumberExpr)
    def visit(self, node):
        return str(node.n)

    @visitor(StringExpr)
    def visit(self, node):
        return "'" + str(node.s) + "'"

    @visitor(AssignStat)
    def visit(self, node):
        self.fidelityPrint(node.targets)
        self.fidelityPrint(node.symbol)
        self.fidelityPrint(node.values)
        # return ' '.join([', '.join(self.visitList(node.targets)), '=', ', '.join(self.visitList(node.values))])

    @visitor(LocalAssignStat)
    def visit(self, node):
        return ' '.join(['local', ', '.join(self.visitList(node.targets)), '=', ', '.join(self.visitList(node.values))])

    @visitor(TableExpr)
    def visit(self, node):
        pairs = []
        for k in range(0, len(node.keys)):
            pairs.append(' '.join([self.visit(node.keys[k]), '=', self.visit(node.values[k])]))
        return '{' + '\n'.join(pairs) + '}'
