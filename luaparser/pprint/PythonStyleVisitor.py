from luaparser.astNodes import *
from luaparser.visitor import *


class PythonStyleVisitor():
    def __init__(self, indent, indentValue):
        self.indentEnabled = indent
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

    def prettyCount(self, object, isList=False):
        res = ''
        if isinstance(object, list):
            itemCount = len(object)
            res += '[] ' + str(itemCount) + ' '
            if itemCount > 1 : res += 'items'
            else             : res += 'item'
        elif isinstance(object, Node):
            if isList:
                return '{} 1 key'
            keyCount = len(object.__dict__.items()) - 1 # name
            res += '{} ' + str(keyCount) + ' '
            if keyCount > 1 : res += 'keys'
            else            : res += 'key'
        else:
            res += '[unknow]'
        return res



    @visitor(list)
    def visit(self, obj):
        res = ''
        k = 0
        for itemValue in obj:
            res += self.indentStr() + str(k) + ': ' + self.prettyCount(itemValue, True)
            self.indent()
            res += self.indentStr(False) + self.visit(itemValue)
            self.dedent()
            k += 1
        return res

    @visitor(Node)
    def visit(self, node):
        res = self.indentStr() + node.name + ': ' + self.prettyCount(node)

        self.indent()
        for attr, attrValue in node.__dict__.items():
            if attr != 'name':
                if isinstance(attrValue, Node) or isinstance(attrValue, list):
                    res += self.indentStr() + attr + ': ' + self.prettyCount(attrValue)
                    self.indent()
                    res += self.visit(attrValue)
                    self.dedent()
                else:
                    if attrValue is not None:
                        res += self.indentStr() + attr + ': ' + self.visit(attrValue)
        self.dedent()
        return res

