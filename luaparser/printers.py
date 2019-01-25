"""
    ``printers`` module
    ===================

    Contains utilities to render an ast tree to text or html.
"""

from luaparser.astnodes import *
from luaparser.utils.visitor import *
from enum import Enum
import xml.etree.cElementTree as ET
from xml.dom import minidom


class Style(Enum):
    PYTHON = 1
    HTML = 2


class PythonStyleVisitor:
    def __init__(self, indent):
        self.indentValue = indent
        self.currentIndent = 0

    @visitor(str)
    def visit(self, node):
        return repr(node)

    @visitor(float)
    def visit(self, node):
        return str(node)

    @visitor(int)
    def visit(self, node):
        return str(node)

    def indent_str(self, newLine=True):
        res = ' ' * self.currentIndent
        if newLine:
            res = '\n' + res
        return res

    def indent(self):
        self.currentIndent += self.indentValue

    def dedent(self):
        self.currentIndent -= self.indentValue

    @staticmethod
    def pretty_count(node, is_list=False):
        res = ''
        if isinstance(node, list):
            item_count = len(node)
            res += '[] ' + str(item_count) + ' '
            if item_count > 1:
                res += 'items'
            else:
                res += 'item'
        elif isinstance(node, Node):
            if is_list:
                return '{} 1 key'
            key_count = len([attr for attr in node.__dict__.keys() if not attr.startswith("_")])
            res += '{} ' + str(key_count) + ' '
            if key_count > 1:
                res += 'keys'
            else:
                res += 'key'
        else:
            res += '[unknow]'
        return res

    @visitor(list)
    def visit(self, obj):
        res = ''
        k = 0
        for itemValue in obj:
            res += self.indent_str() + str(k) + ': ' + self.pretty_count(itemValue, True)
            self.indent()
            res += self.indent_str(False) + self.visit(itemValue)
            self.dedent()
            k += 1
        return res

    @visitor(Node)
    def visit(self, node):
        res = self.indent_str() + node.display_name + ': ' + self.pretty_count(node)

        self.indent()

        # comments
        comments = node.comments
        if comments:
            res += self.indent_str() + 'comments' + ': ' + self.pretty_count(comments)
            k = 0
            self.indent()
            for c in comments:
                res += self.indent_str() + str(k) + ': ' + self.visit(c.s)
                k += 1
            self.dedent()

        for attr, attrValue in node.__dict__.items():
            if not attr.startswith(('_', 'comments')):
                if isinstance(attrValue, Node) or isinstance(attrValue, list):
                    res += self.indent_str() + attr + ': ' + self.pretty_count(attrValue)
                    self.indent()
                    res += self.visit(attrValue)
                    self.dedent()
                else:
                    if attrValue is not None:
                        res += self.indent_str() + attr + ': ' + self.visit(attrValue)
        self.dedent()
        return res


escape_dict = {
    '\a': r'\a',
    '\b': r'\b',
    '\c': r'\c',
    '\f': r'\f',
    '\n': r'\n',
    '\r': r'\r',
    '\t': r'\t',
    '\v': r'\v',
    '\'': r'\'',
    '\"': r'\"',
    '\0': r'\0',
    '\1': r'\1',
    '\2': r'\2',
    '\3': r'\3',
    '\4': r'\4',
    '\5': r'\5',
    '\6': r'\6',
    '\7': r'\7',
    '\8': r'\8',
    '\9': r'\9'
}


def raw(text):
    """Returns a raw string representation of text"""
    new_string = ''
    for char in text:
        try:
            new_string += escape_dict[char]
        except KeyError:
            new_string += char
    return new_string


class HTMLStyleVisitor:
    def __init__(self):
        pass

    def get_xml_string(self, tree):
        xml = self.visit(tree)

        ast = ET.Element("ast")
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
        xml_node = ET.Element(node.display_name)

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

        return xml_node
