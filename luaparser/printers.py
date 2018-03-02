from luaparser.astnodes import *
from luaparser.utils.visitor import *
from enum import Enum
import xml.etree.cElementTree as ET
from luaparser.asttokens import Tokens
from xml.dom import minidom

class Style(Enum):
    PYTHON  = 1
    HTML    = 2

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


escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string


class HTMLStyleVisitor:
    def __init__(self):
        pass

    def get_xml_string(self, tree):
        xml = self.visit(tree)

        ast= ET.Element("ast")
        doc = ET.SubElement(ast, "doc")
        doc.append(xml)

        return minidom.parseString(ET.tostring(doc)).toprettyxml(indent="   ")

    @visitor(str)
    def visit(self, node):
        if node.startswith('"') and node.endswith('"'):
            node = node[1:-1]
        return node

    @visitor(float)
    def visit(self, node):
        return str(node)

    @visitor(int)
    def visit(self, node):
        return str(node)

    @visitor(list)
    def visit(self, obj):
        xml_nodes = []
        for itemValue in obj:
            xml_nodes.append(self.visit(itemValue))
        return xml_nodes

    @visitor(Node)
    def visit(self, node):
        xml_node = ET.Element(node.displayName)

        # attributes
        for attr, attrValue in node.__dict__.items():
            if not attr.startswith('_') and attrValue is not None:
                xml_attr = ET.SubElement(xml_node, attr)
                child_node = self.visit(attrValue)
                if type(child_node) is str:
                    xml_attr.text = child_node
                elif type(child_node) is list:
                    xml_attr.extend(child_node)
                else:
                    xml_attr.append(child_node)

        # tokens
        xml_tokens = ET.SubElement(xml_node, 'tokens')
        for token in node.tokens:
            ET.SubElement(xml_tokens, Tokens(token.value.type).name, text=raw(token.value.text))

        return xml_node

