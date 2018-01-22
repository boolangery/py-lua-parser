from luaparser.astnodes import *
from luaparser.utils.visitor import *
from enum import Enum

class Style(Enum):
    PYTHON  = 1

class PythonStyleVisitor():
    def __init__(self, indent):
        self.indentValue = indent
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
        res = ' ' * self.currentIndent
        if newLine:
            res = '\n' + res
        return res

    def indent(self):
        self.currentIndent += self.indentValue

    def dedent(self):
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
            keyCount = len([attr for attr in object.__dict__.keys() if not attr.startswith("_")])
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
        res = self.indentStr() + node.displayName + ': ' + self.prettyCount(node)

        self.indent()
        for attr, attrValue in node.__dict__.items():
            if not attr.startswith('_'):
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

