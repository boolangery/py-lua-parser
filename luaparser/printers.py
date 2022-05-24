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

    @visitor(str)
    def visit(self, node) -> str:
        return str(node)

    @visitor(float)
    def visit(self, node) -> str:
        return str(node)

    @visitor(int)
    def visit(self, node) -> str:
        return str(node)

    @visitor(list)
    def visit(self, node: List) -> str:
        return ", ".join([self.visit(n) for n in node])

    @visitor(type(None))
    def visit(self, node) -> str:
        return ""

    @visitor(Chunk)
    def visit(self, node) -> str:
        return self.visit(node.body)

    @visitor(Block)
    def visit(self, node: Block) -> str:
        self._level += 1
        output = indent(
            "\n".join([self.visit(n) for n in node.body]), " " * (self._indent_size if self._level > 1 else 0)
        )
        self._level -= 1
        return output

    @visitor(Assign)
    def visit(self, node: Assign) -> str:
        return self.visit(node.targets) + " = " + self.visit(node.values)

    @visitor(LocalAssign)
    def visit(self, node: LocalAssign) -> str:
        return "local " + self.visit(node.targets) + " = " + self.visit(node.values)

    @visitor(While)
    def visit(self, node: While) -> str:
        return (
            "while " + self.visit(node.test) + " do\n" + self.visit(node.body) + "\nend"
        )

    @visitor(Do)
    def visit(self, node: Do) -> str:
        return "do\n" + self.visit(node.body) + "\nend"

    @visitor(If)
    def visit(self, node: If) -> str:
        output = (
            "if " + self.visit(node.test) + " then\n" + self.visit(node.body)
        )
        if isinstance(node.orelse, ElseIf):
            output += "\n" + self.visit(node.orelse)
        elif node.orelse:
            output += "\nelse\n" + self.visit(node.orelse)
        output += "\nend"
        return output

    @visitor(ElseIf)
    def visit(self, node: ElseIf) -> str:
        output = (
            "elseif " + self.visit(node.test) + " then\n" + self.visit(node.body)
        )
        if isinstance(node.orelse, ElseIf):
            output += "\n" + self.visit(node.orelse)
        elif node.orelse:
            output += "\nelse\n" + self.visit(node.orelse)
        return output

    @visitor(Label)
    def visit(self, node: Label) -> str:
        return "::" + self.visit(node.id) + "::"

    @visitor(Goto)
    def visit(self, node: Goto) -> str:
        return "goto " + self.visit(node.label)

    @visitor(Break)
    def visit(self, node: Break) -> str:
        return "break"

    @visitor(Return)
    def visit(self, node: Return) -> str:
        return "return " + self.visit(node.values)

    @visitor(Fornum)
    def visit(self, node: Fornum) -> str:
        output = " ".join(
            [
                "for",
                self.visit(node.target),
                "=",
                ", ".join([self.visit(node.start), self.visit(node.stop)]),
            ]
        )
        if node.step != 1:
            output += ", " + self.visit(node.step)
        output += " do\n" + self.visit(node.body) + "\nend"
        return output

    @visitor(Forin)
    def visit(self, node: Forin) -> str:
        return (
            " ".join(
                ["for", self.visit(node.targets), "in", self.visit(node.iter), "do"]
            )
            + "\n"
            + self.visit(node.body)
            + "\nend"
        )

    @visitor(Call)
    def visit(self, node: Call) -> str:
        return self.visit(node.func) + "(" + self.visit(node.args) + ")"

    @visitor(Invoke)
    def visit(self, node: Invoke) -> str:
        return (
            self.visit(node.source)
            + ":"
            + self.visit(node.func)
            + "("
            + self.visit(node.args)
            + ")"
        )

    @visitor(Function)
    def visit(self, node: Function) -> str:
        return (
            "function "
            + self.visit(node.name)
            + "("
            + self.visit(node.args)
            + ")\n"
            + self.visit(node.body)
            + "\nend"
        )

    @visitor(LocalFunction)
    def visit(self, node) -> str:
        return (
            "local function "
            + self.visit(node.name)
            + "("
            + self.visit(node.args)
            + ")\n"
            + self.visit(node.body)
            + "\nend"
        )

    @visitor(Method)
    def visit(self, node: Method) -> str:
        return (
            "function "
            + self.visit(node.source)
            + ":"
            + self.visit(node.name)
            + "("
            + self.visit(node.args)
            + ")\n"
            + self.visit(node.body)
            + "\nend"
        )

    @visitor(Nil)
    def visit(self, node) -> str:
        return "nil"

    @visitor(TrueExpr)
    def visit(self, node) -> str:
        return "true"

    @visitor(FalseExpr)
    def visit(self, node) -> str:
        return "false"

    @visitor(Number)
    def visit(self, node) -> str:
        return self.visit(node.n)

    @visitor(String)
    def visit(self, node: String) -> str:
        if node.delimiter == StringDelimiter.SINGLE_QUOTE:
            return "'" + self.visit(node.s) + "'"
        elif node.delimiter == StringDelimiter.DOUBLE_QUOTE:
            return '"' + self.visit(node.s) + '"'
        else:
            return "[[" + self.visit(node.s) + "]]"

    @visitor(Table)
    def visit(self, node: Table):
        output = "{\n"
        for field in node.fields:
            output += indent(self.visit(field) + ",\n", " " * self._indent_size)
        output += "}"
        return output

    @visitor(Field)
    def visit(self, node: Field):
        output = "[" if node.between_brackets else ""
        output += self.visit(node.key)
        output += "]" if node.between_brackets else ""
        output += " = "
        output += self.visit(node.value)
        return output

    @visitor(Dots)
    def visit(self, node) -> str:
        return "..."

    @visitor(AnonymousFunction)
    def visit(self, node: AnonymousFunction) -> str:
        return (
            "function("
            + self.visit(node.args)
            + ")\n"
            + self.visit(node.body)
            + "\nend"
        )

    @visitor(AddOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " + " + self.visit(node.right)

    @visitor(SubOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " - " + self.visit(node.right)

    @visitor(MultOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " * " + self.visit(node.right)

    @visitor(FloatDivOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " / " + self.visit(node.right)

    @visitor(FloorDivOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " // " + self.visit(node.right)

    @visitor(ModOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " % " + self.visit(node.right)

    @visitor(ExpoOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " ^ " + self.visit(node.right)

    @visitor(BAndOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " & " + self.visit(node.right)

    @visitor(BOrOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " | " + self.visit(node.right)

    @visitor(BXorOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " ~ " + self.visit(node.right)

    @visitor(BShiftROp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " >> " + self.visit(node.right)

    @visitor(BShiftLOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " << " + self.visit(node.right)

    @visitor(LessThanOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " < " + self.visit(node.right)

    @visitor(GreaterThanOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " > " + self.visit(node.right)

    @visitor(LessOrEqThanOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " <= " + self.visit(node.right)

    @visitor(GreaterOrEqThanOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " >= " + self.visit(node.right)

    @visitor(EqToOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " == " + self.visit(node.right)

    @visitor(NotEqToOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " ~= " + self.visit(node.right)

    @visitor(AndLoOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " and " + self.visit(node.right)

    @visitor(OrLoOp)
    def visit(self, node) -> str:
        return self.visit(node.left) + " or " + self.visit(node.right)

    @visitor(Concat)
    def visit(self, node) -> str:
        return self.visit(node.left) + ".." + self.visit(node.right)

    @visitor(UMinusOp)
    def visit(self, node) -> str:
        return "-" + self.visit(node.operand)

    @visitor(UBNotOp)
    def visit(self, node) -> str:
        return "~" + self.visit(node.operand)

    @visitor(ULNotOp)
    def visit(self, node) -> str:
        return "not " + self.visit(node.operand)

    @visitor(ULengthOP)
    def visit(self, node) -> str:
        return "#" + self.visit(node.operand)

    @visitor(Name)
    def visit(self, node: Name) -> str:
        return self.visit(node.id)

    @visitor(Index)
    def visit(self, node: Index) -> str:
        if node.notation == IndexNotation.DOT:
            return self.visit(node.value) + "." + self.visit(node.idx)
        else:
            return self.visit(node.value) + "[" + self.visit(node.idx) + "]"

    @visitor(Varargs)
    def visit(self, node) -> str:
        return "..."

    @visitor(Repeat)
    def visit(self, node: Repeat) -> str:
        return "repeat\n" + self.visit(node.body) + "\nuntil " + self.visit(node.test)

    @visitor(SemiColon)
    def visit(self, node) -> str:
        return ";"
