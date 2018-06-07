from antlr4 import InputStream, CommonTokenStream
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.astnodes import *
from luaparser import printers
from luaparser.utils.visitor import *
from antlr4.error.ErrorListener import ErrorListener


def parse(source):
    from luaparser.builder import Builder
    return Builder(source).process()

def get_token_stream(source):
    lexer = LuaLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    return stream

def walk(root):
    # base case:
    if root is None:
        return

    visitor = WalkVisitor()
    visitor.visit(root)
    for n in visitor.nodes:
        yield n

def toPrettyStr(tree, indent=2):
    return printers.PythonStyleVisitor(indent).visit(tree)

def toXmlStr(tree):
    visitor = printers.HTMLStyleVisitor()
    return visitor.get_xml_string(tree)


class ASTVisitor:
    def visit(self, root):
        # base case:
        if root is None:
            return
        nodeStack = []
        nodeStack.append(root)

        while(len(nodeStack) > 0):
            node = nodeStack.pop()
            # push childs to the stack:
            if isinstance(node, Node):
                # call visit method
                name = 'visit_' + node.__class__.__name__
                visitor = getattr(self, name, None)
                if visitor:
                    visitor(node)

                # add childs
                childs = [attr for attr in node.__dict__.keys() if not attr.startswith("_")]
                for child in childs:
                    nodeStack.append(node.__dict__[child])
            elif isinstance(node, list):
                # append node list in reversal order
                for n in reversed(node):
                    nodeStack.append(n)


class ASTRecursiveVisitor:
    def visit(self, node):
        if isinstance(node, Node):
            # call enter node method
            # if no visitor method found for this arg type,
            # search in parent arg type:
            parentType = node.__class__
            while parentType != object:
                name = 'enter_' + parentType.__name__
                visitor = getattr(self, name, None)
                if visitor:
                    visitor(node)
                    break
                else:
                    parentType = parentType.__bases__[0]

            # visit all object public attributes:
            childs = [attr for attr in node.__dict__.keys() if not attr.startswith("_")]
            for child in childs:
                self.visit(node.__dict__[child])

            # call exit node method
            # if no visitor method found for this arg type,
            # search in parent arg type:
            parentType = node.__class__
            while parentType != object:
                name = 'exit_' + parentType.__name__
                visitor = getattr(self, name, None)
                if visitor:
                    visitor(node)
                    break
                else:
                    parentType = parentType.__bases__[0]
        elif isinstance(node, list):
            for n in node:
                self.visit(n)


class WalkVisitor:
    def __init__(self):
        self._nodes = []

    @property
    def nodes(self):
        return self._nodes

    @visitor(str)
    def visit(self, node):
        pass

    @visitor(float)
    def visit(self, node):
        pass

    @visitor(int)
    def visit(self, node):
        pass

    @visitor(list)
    def visit(self, node):
        for n in node:
            self.visit(n)

    @visitor(Chunk)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.body)

    @visitor(Block)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.body)

    @visitor(Assign)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.targets)
        self.visit(node.values)

    @visitor(While)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.test)
        self.visit(node.body)

    @visitor(Do)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.body)

    @visitor(If)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.test)
        self.visit(node.body)
        self.visit(node.orelse)

    @visitor(ElseIf)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.test)
        self.visit(node.body)
        self.visit(node.orelse)

    @visitor(Label)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Goto)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Break)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Return)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.values)

    @visitor(Fornum)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.target)
        self.visit(node.start)
        self.visit(node.stop)
        self.visit(node.step)
        self.visit(node.body)

    @visitor(Forin)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.targets)
        self.visit(node.iter)
        self.visit(node.body)

    @visitor(Call)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.func)
        self.visit(node.args)

    @visitor(Invoke)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.source)
        self.visit(node.func)
        self.visit(node.args)

    @visitor(Function)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.name)
        self.visit(node.args)
        self.visit(node.body)

    @visitor(LocalFunction)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.name)
        self.visit(node.args)
        self.visit(node.body)

    @visitor(Method)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.source)
        self.visit(node.name)
        self.visit(node.args)
        self.visit(node.body)

    @visitor(Nil)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(TrueExpr)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(FalseExpr)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Number)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(String)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Table)
    def visit(self, node):
        self._nodes.append(node)
        for key, value in zip(node.keys, node.values):
            self.visit(key)
            self.visit(value)

    @visitor(Dots)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(AnonymousFunction)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.args)
        self.visit(node.body)

    @visitor(BinaryOp)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.left)
        self.visit(node.right)

    @visitor(UnaryOp)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.operand)

    @visitor(Name)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Index)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.value)
        self.visit(node.idx)


class SyntaxException(Exception):
    pass

class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException(str(line) + ":" + str(column) + ': ' + str(msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
