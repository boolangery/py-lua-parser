"""
    ``printers`` module
    ===================

    Contains utilities to render an ast tree to text or html.
"""

from luaparser.astnodes import *
from luaparser.utils.visitor import *
from enum import Enum
import xml.etree.cElementTree as ElementTree
from xml.dom import minidom
from textwrap import indent
from multimethod import multimethod


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

    @visitor(Enum)
    def visit(self, node):
        return str(node.name)

    def indent_str(self, newLine=True):
        res = " " * self.currentIndent
        if newLine:
            res = "\n" + res
        return res

    def indent(self):
        self.currentIndent += self.indentValue

    def dedent(self):
        self.currentIndent -= self.indentValue

    @staticmethod
    def pretty_count(node, is_list=False):
        res = ""
        if isinstance(node, list):
            item_count = len(node)
            res += "[] " + str(item_count) + " "
            if item_count > 1:
                res += "items"
            else:
                res += "item"
        elif isinstance(node, Node):
            if is_list:
                return "{} 1 key"
            key_count = len(
                [attr for attr in node.__dict__.keys() if not attr.startswith("_")]
            )
            res += "{} " + str(key_count) + " "
            if key_count > 1:
                res += "keys"
            else:
                res += "key"
        else:
            res += "[unknow]"
        return res

    @visitor(list)
    def visit(self, obj):
        res = ""
        k = 0
        for itemValue in obj:
            res += (
                    self.indent_str() + str(k) + ": " + self.pretty_count(itemValue, True)
            )
            self.indent()
            res += self.indent_str(False) + self.visit(itemValue)
            self.dedent()
            k += 1
        return res

    @visitor(Node)
    def visit(self, node):
        res = self.indent_str() + node.display_name + ": " + self.pretty_count(node)

        self.indent()

        # comments
        comments = node.comments
        if comments:
            res += self.indent_str() + "comments" + ": " + self.pretty_count(comments)
            k = 0
            self.indent()
            for c in comments:
                res += self.indent_str() + str(k) + ": " + self.visit(c.s)
                k += 1
            self.dedent()

        for attr, attrValue in node.__dict__.items():
            if not attr.startswith(("_", "comments")):
                if isinstance(attrValue, Node) or isinstance(attrValue, list):
                    res += (
                            self.indent_str() + attr + ": " + self.pretty_count(attrValue)
                    )
                    self.indent()
                    res += self.visit(attrValue)
                    self.dedent()
                else:
                    if attrValue is not None:
                        res += self.indent_str() + attr + ": " + self.visit(attrValue)
        self.dedent()
        return res


escape_dict = {
    "\a": r"\a",
    "\b": r"\b",
    "\c": r"\c",
    "\f": r"\f",
    "\n": r"\n",
    "\r": r"\r",
    "\t": r"\t",
    "\v": r"\v",
    "'": r"\'",
    '"': r"\"",
    "\0": r"\0",
    "\1": r"\1",
    "\2": r"\2",
    "\3": r"\3",
    "\4": r"\4",
    "\5": r"\5",
    "\6": r"\6",
    "\7": r"\7",
    "\8": r"\8",
    "\9": r"\9",
}


def raw(text):
    """Returns a raw string representation of text"""
    new_string = ""
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

        ast = ElementTree.Element("ast")
        doc = ElementTree.SubElement(ast, "doc")
        doc.append(xml)

        return minidom.parseString(ElementTree.tostring(doc)).toprettyxml(indent="   ")

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

    @visitor(Enum)
    def visit(self, node):
        return str(node)

    @visitor(Node)
    def visit(self, node):
        xml_node = ElementTree.Element(node.display_name)

        # attributes
        for attr, attrValue in node.__dict__.items():
            if not attr.startswith("_") and attrValue is not None:
                xml_attr = ElementTree.SubElement(xml_node, attr)
                child_node = self.visit(attrValue)
                if type(child_node) is str:
                    xml_attr.text = child_node
                elif type(child_node) is list:
                    xml_attr.extend(child_node)
                else:
                    xml_attr.append(child_node)

        return xml_node


class LuaOutputVisitor:
    def __init__(self, indent_size: int):
        self._indent_size = indent_size
        self._level = 0

    def do_visit(self, node: Node) -> str:
        if isinstance(node, Expression) and node.wrapped:
            return "(" + self.visit(node) + ")"
        return self.visit(node)

    @multimethod
    def visit(self, node: Chunk) -> str:
        return self.do_visit(node.body)

    @visit.register
    def visit(self, node: Block) -> str:
        self._level += 1
        output = indent(
            "\n".join([self.do_visit(n) for n in node.body]), " " * (self._indent_size if self._level > 1 else 0)
        )
        self._level -= 1
        return output

    @visit.register
    def visit(self, node: str) -> str:
        return node

    @visit.register
    def visit(self, node: float) -> str:
        return str(node)

    @visit.register
    def visit(self, node: int) -> str:
        return str(node)

    @visit.register
    def visit(self, node: list) -> str:
        return ", ".join([self.do_visit(n) for n in node])

    @visit.register
    def visit(self, node: None) -> str:
        return ""

    @visit.register
    def visit(self, node: Assign) -> str:
        return self.do_visit(node.targets) + " = " + self.do_visit(node.values)

    @visit.register
    def visit(self, node: LocalAssign) -> str:
        res = self.do_visit(node.values)
        if res == '':
            return "local " + self.do_visit(node.targets)
        return "local " + self.do_visit(node.targets) + " = " + res

    @visit.register
    def visit(self, node: While) -> str:
        return (
                "while " + self.do_visit(node.test) + " do\n" + self.do_visit(node.body) + "\nend"
        )

    @visit.register
    def visit(self, node: Do) -> str:
        return "do\n" + self.do_visit(node.body) + "\nend"

    @visit.register
    def visit(self, node: If) -> str:
        output = (
                "if " + self.do_visit(node.test) + " then\n" + self.do_visit(node.body)
        )
        if isinstance(node.orelse, ElseIf):
            output += "\n" + self.do_visit(node.orelse)
        elif node.orelse:
            output += "\nelse\n" + self.do_visit(node.orelse)
        output += "\nend"
        return output

    @visit.register
    def visit(self, node: ElseIf) -> str:
        output = (
                "elseif " + self.do_visit(node.test) + " then\n" + self.do_visit(node.body)
        )
        if isinstance(node.orelse, ElseIf):
            output += "\n" + self.do_visit(node.orelse)
        elif node.orelse:
            output += "\nelse\n" + self.do_visit(node.orelse)
        return output

    @visit.register
    def visit(self, node: Label) -> str:
        return "::" + self.do_visit(node.id) + "::"

    @visit.register
    def visit(self, node: Goto) -> str:
        return "goto " + self.do_visit(node.label)

    @visit.register
    def visit(self, node: Break) -> str:
        return "break"

    @visit.register
    def visit(self, node: Return) -> str:
        res = self.do_visit(node.values)
        if res == "False":
            return "return"
        return "return " + res

    @visit.register
    def visit(self, node: Fornum) -> str:
        output = " ".join(
            [
                "for",
                self.do_visit(node.target),
                "=",
                ", ".join([self.do_visit(node.start), self.do_visit(node.stop)]),
            ]
        )
        if node.step != 1:
            output += ", " + self.do_visit(node.step)
        output += " do\n" + self.do_visit(node.body) + "\nend"
        return output

    @visit.register
    def visit(self, node: Forin) -> str:
        return (
                " ".join(
                    ["for", self.do_visit(node.targets), "in", self.do_visit(node.iter), "do"]
                )
                + "\n"
                + self.do_visit(node.body)
                + "\nend"
        )

    @visit.register
    def visit(self, node: Call) -> str:
        return self.do_visit(node.func) + "(" + self.do_visit(node.args) + ")"

    @visit.register
    def visit(self, node: Invoke) -> str:
        return (
                self.do_visit(node.source)
                + ":"
                + self.do_visit(node.func)
                + "("
                + self.do_visit(node.args)
                + ")"
        )

    @visit.register
    def visit(self, node: Function) -> str:
        return (
                "function "
                + self.do_visit(node.name)
                + "("
                + self.do_visit(node.args)
                + ")\n"
                + self.do_visit(node.body)
                + "\nend"
        )

    @visit.register
    def visit(self, node: LocalFunction) -> str:
        return (
                "local function "
                + self.do_visit(node.name)
                + "("
                + self.do_visit(node.args)
                + ")\n"
                + self.do_visit(node.body)
                + "\nend"
        )

    @visit.register
    def visit(self, node: Method) -> str:
        return (
                "function "
                + self.do_visit(node.source)
                + ":"
                + self.do_visit(node.name)
                + "("
                + self.do_visit(node.args)
                + ")\n"
                + self.do_visit(node.body)
                + "\nend"
        )

    @visit.register
    def visit(self, node: Nil) -> str:
        return "nil"

    @visit.register
    def visit(self, node: TrueExpr) -> str:
        return "true"

    @visit.register
    def visit(self, node: FalseExpr) -> str:
        return "false"

    @visit.register
    def visit(self, node: Number) -> str:
        return self.do_visit(node.n)

    @visit.register
    def visit(self, node: String) -> str:
        if node.delimiter == StringDelimiter.SINGLE_QUOTE:
            return "'" + self.do_visit(node.s) + "'"
        elif node.delimiter == StringDelimiter.DOUBLE_QUOTE:
            return '"' + self.do_visit(node.s) + '"'
        else:
            return "[[" + self.do_visit(node.s) + "]]"

    @visit.register
    def visit(self, node: Table):
        output = "{\n"
        for field in node.fields:
            output += indent(self.do_visit(field) + ",\n", " " * self._indent_size)
        output += "}"
        return output

    @visit.register
    def visit(self, node: Field):
        output = "[" if node.between_brackets else ""
        output += self.do_visit(node.key)
        output += "]" if node.between_brackets else ""
        output += " = "
        output += self.do_visit(node.value)
        return output

    @visit.register
    def visit(self, node: Dots) -> str:
        return "..."

    @visit.register
    def visit(self, node: AnonymousFunction) -> str:
        return (
                "function("
                + self.do_visit(node.args)
                + ")\n"
                + self.do_visit(node.body)
                + "\nend"
        )

    @visit.register
    def visit(self, node: AddOp) -> str:
        return self.do_visit(node.left) + " + " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: SubOp) -> str:
        return self.do_visit(node.left) + " - " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: MultOp) -> str:
        return self.do_visit(node.left) + " * " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: FloatDivOp) -> str:
        return self.do_visit(node.left) + " / " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: FloorDivOp) -> str:
        return self.do_visit(node.left) + " // " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: ModOp) -> str:
        return self.do_visit(node.left) + " % " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: ExpoOp) -> str:
        return self.do_visit(node.left) + " ^ " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: BAndOp) -> str:
        return self.do_visit(node.left) + " & " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: BOrOp) -> str:
        return self.do_visit(node.left) + " | " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: BXorOp) -> str:
        return self.do_visit(node.left) + " ~ " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: BShiftROp) -> str:
        return self.do_visit(node.left) + " >> " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: BShiftLOp) -> str:
        return self.do_visit(node.left) + " << " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: LessThanOp) -> str:
        return self.do_visit(node.left) + " < " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: GreaterThanOp) -> str:
        return self.do_visit(node.left) + " > " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: LessOrEqThanOp) -> str:
        return self.do_visit(node.left) + " <= " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: GreaterOrEqThanOp) -> str:
        return self.do_visit(node.left) + " >= " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: EqToOp) -> str:
        return self.do_visit(node.left) + " == " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: NotEqToOp) -> str:
        return self.do_visit(node.left) + " ~= " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: AndLoOp) -> str:
        return self.do_visit(node.left) + " and " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: OrLoOp) -> str:
        return self.do_visit(node.left) + " or " + self.do_visit(node.right)

    @visit.register
    def visit(self, node: Concat) -> str:
        return self.do_visit(node.left) + ".." + self.do_visit(node.right)

    @visit.register
    def visit(self, node: UMinusOp) -> str:
        return "-" + self.do_visit(node.operand)

    @visit.register
    def visit(self, node: UBNotOp) -> str:
        return "~" + self.do_visit(node.operand)

    @visit.register
    def visit(self, node: ULNotOp) -> str:
        return "not " + self.do_visit(node.operand)

    @visit.register
    def visit(self, node: ULengthOP) -> str:
        return "#" + self.do_visit(node.operand)

    @visit.register
    def visit(self, node: Name) -> str:
        return self.do_visit(node.id)

    @visit.register
    def visit(self, node: Index) -> str:
        if node.notation == IndexNotation.DOT:
            return self.do_visit(node.value) + "." + self.do_visit(node.idx)
        else:
            return self.do_visit(node.value) + "[" + self.do_visit(node.idx) + "]"

    @visit.register
    def visit(self, node: Varargs) -> str:
        return "..."

    @visit.register
    def visit(self, node: Repeat) -> str:
        return "repeat\n" + self.do_visit(node.body) + "\nuntil " + self.do_visit(node.test)

    @visit.register
    def visit(self, node: SemiColon) -> str:
        return ";"
