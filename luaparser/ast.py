import ast
import re

from antlr4 import InputStream, CommonTokenStream
from antlr4.tree.Tree import ParseTreeVisitor, TerminalNodeImpl, ErrorNodeImpl
from antlr_ast.ast import LexerErrorListener, StrictErrorListener, ConsoleErrorListener

from luaparser.parser.LuaLexer import LuaLexer
from luaparser.astnodes import *
from luaparser import printers
from luaparser.builder import Builder
from luaparser.parser.LuaParser import LuaParser
from luaparser.parser.LuaParserVisitor import LuaParserVisitor
from luaparser.utils.visitor import *
from antlr4.error.ErrorListener import ErrorListener
import json
from typing import Generator


def _listify(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj


class MyVisitor(LuaParserVisitor):
    # Visit a parse tree produced by LuaParser#start_.
    def visitStart_(self, ctx: LuaParser.Start_Context):
        return self.visitChildren(ctx)

    def visitTerminal(self, node: TerminalNodeImpl):
        match node.symbol.type:
            case LuaParser.EOF:
                return None
            case LuaParser.NAME:
                return Name(node.getText())
            case _:
                return node.getText()

    def visitErrorNode(self, node: ErrorNodeImpl):
        return "error:" + node.getText()

    def defaultResult(self):
        return None

    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return nextResult
        if type(nextResult) == list:
            nextResult.append(aggregate)
            return nextResult
        if type(aggregate) == list:
            aggregate.append(nextResult)
            return aggregate
        if nextResult == None:
            return aggregate
        return [nextResult, aggregate]

    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx: LuaParser.ChunkContext):
        return Chunk(
            body=self.visitChildren(ctx)
        )

    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx: LuaParser.BlockContext):
        statements = [self.visit(stat) for stat in ctx.stat()]
        if ctx.retstat():
            statements.append(self.visit(ctx.retstat()))
        return Block(
            body=statements
        )

    # Visit a parse tree produced by LuaParser#stat.
    def visitStat(self, ctx: LuaParser.StatContext):
        if ctx.SEMI():
            return SemiColon()
        elif ctx.BREAK():
            return Break()
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#assign.
    def visitAssign(self, ctx: LuaParser.AssignContext):
        return Assign(
            targets=_listify(self.visit(ctx.varlist())),
            values=_listify(self.visit(ctx.explist())),
        )

    # Visit a parse tree produced by LuaParser#goto.
    def visitGoto(self, ctx: LuaParser.GotoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#do.
    def visitDo(self, ctx: LuaParser.DoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#while.
    def visitWhile(self, ctx: LuaParser.WhileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#repeat.
    def visitRepeat(self, ctx: LuaParser.RepeatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#if.
    def visitIf(self, ctx: LuaParser.IfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#for.
    def visitFor(self, ctx: LuaParser.ForContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#forin.
    def visitForin(self, ctx: LuaParser.ForinContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx: LuaParser.FunctiondefContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#localfunction.
    def visitLocalfunction(self, ctx: LuaParser.LocalfunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#localassign.
    def visitLocalassign(self, ctx: LuaParser.LocalassignContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#attnamelist.
    def visitAttnamelist(self, ctx: LuaParser.AttnamelistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#attrib.
    def visitAttrib(self, ctx: LuaParser.AttribContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx: LuaParser.RetstatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx: LuaParser.LabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#funcname.
    def visitFuncname(self, ctx: LuaParser.FuncnameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#varlist.
    def visitVarlist(self, ctx: LuaParser.VarlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#namelist.
    def visitNamelist(self, ctx: LuaParser.NamelistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#explist.
    def visitExplist(self, ctx: LuaParser.ExplistContext):
        return [self.visit(exp) for exp in ctx.exp()]

    # Visit a parse tree produced by LuaParser#exp.
    def visitExp(self, ctx: LuaParser.ExpContext):
        if ctx.NIL():
            return Nil()
        elif ctx.FALSE():
            return FalseExpr()
        elif ctx.TRUE():
            return TrueExpr()
        elif ctx.number():
            return self.visit(ctx.number())
        elif ctx.string():
            return self.visit(ctx.string())
        elif ctx.DDD():
            return Dots()
        elif ctx.functiondef():
            return self.visit(ctx.functiondef())
        elif ctx.prefixexp():
            return self.visit(ctx.prefixexp())
        elif ctx.tableconstructor():
            return self.visit(ctx.tableconstructor())
        else:
            expressions = ctx.exp()

            if len(expressions) == 2 and ctx.CARET():
                left = self.visit(expressions[0])
                right = self.visit(expressions[1])
                return ExpoOp(left, right)
            elif len(expressions) == 1:
                left = self.visit(expressions[0])

                if ctx.NOT():
                    return ULNotOp(left)
                elif ctx.POUND():
                    return ULengthOP(left)
                elif ctx.MINUS():
                    return UMinusOp(left)
                elif ctx.SQUIG():
                    return UBNotOp(left)
            elif len(expressions) == 2:
                left = self.visit(expressions[0])
                right = self.visit(expressions[1])

                if ctx.STAR():
                    return MultOp(left, right)
                elif ctx.SLASH():
                    return FloatDivOp(left, right)
                elif ctx.PER():
                    return ModOp(left, right)
                elif ctx.SS():
                    return FloorDivOp(left, right)
                elif ctx.PLUS():
                    return AddOp(left, right)
                elif ctx.MINUS():
                    return SubOp(left, right)
                elif ctx.DD():
                    return Concat(left, right)
                elif ctx.LT():
                    return LessThanOp(left, right)
                elif ctx.GT():
                    return GreaterThanOp(left, right)
                elif ctx.LE():
                    return LessOrEqThanOp(left, right)
                elif ctx.GE():
                    return GreaterOrEqThanOp(left, right)
                elif ctx.SQEQ():
                    return NotEqToOp(left, right)
                elif ctx.EE():
                    return EqToOp(left, right)
                elif ctx.AND():
                    return AndLoOp(left, right)
                elif ctx.OR():
                    return OrLoOp(left, right)
                elif ctx.AMP():
                    return BAndOp(left, right)
                elif ctx.PIPE():
                    return BOrOp(left, right)
                elif ctx.SQUIG():
                    return BXorOp(left, right)
                elif ctx.LL():
                    return BShiftLOp(left, right)
                elif ctx.GG():
                    return BShiftROp(left, right)
            else:
                return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx: LuaParser.VarContext):
        if ctx.NAME():
            return Name(ctx.NAME().getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
        tail = self.visit(ctx.nestedtail())

        if ctx.NAME():  # NAME nestedtail
            if isinstance(tail, Index):
                tail.value = self.visit(ctx.NAME())
                return tail
            else:
                raise Exception("Invalid tail type")
        elif ctx.functioncall():  # functioncall nestedtail
            raise Exception("functioncall not implemented")
        else:  # '(' exp ')' nestedtail
            exp = self.visit(ctx.exp())
            exp.wrapped = True
            # TODO: handle tail
            return exp

    # Visit a parse tree produced by LuaParser#functioncall.
    def visitFunctioncall(self, ctx: LuaParser.FunctioncallContext):
        args = self.visit(ctx.args())
        names = ctx.NAME()

        tails = None
        if ctx.tail():
            tails = [self.visit(t) for t in ctx.tail()]

        if len(names) == 1:  # NAME tail* args
            if isinstance(args, Call):
                args.func = self.visit(names[0])
                return args

        return Call(
            func=ctx.NAME(),
            args=self.visit(ctx.args()),
        )

    def visitAnonfunctiondef(self, ctx: LuaParser.AnonfunctiondefContext):
        return self.visitChildren(ctx)

    def visitNestedtail(self, ctx: LuaParser.NestedtailContext):
        return self.visitChildren(ctx)

    def visitTail(self, ctx: LuaParser.TailContext):
        if ctx.OB() and ctx.CB():
            return Index(
                idx=self.visit(ctx.exp()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.SQUARE,
            )
        else:
            return Index(
                idx=Name(self.visit(ctx.NAME())),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.DOT,
            )

    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx: LuaParser.ArgsContext):
        if ctx.OP() and ctx.CP():
            exp_list = []
            if ctx.explist():
                exp_list = self.visit(ctx.explist())

            return Call(None, exp_list)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx: LuaParser.FunctiondefContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#funcbody.
    def visitFuncbody(self, ctx: LuaParser.FuncbodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#parlist.
    def visitParlist(self, ctx: LuaParser.ParlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#tableconstructor.
    def visitTableconstructor(self, ctx: LuaParser.TableconstructorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx: LuaParser.FieldlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx: LuaParser.FieldContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#fieldsep.
    def visitFieldsep(self, ctx: LuaParser.FieldsepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#number.
    def visitNumber(self, ctx: LuaParser.NumberContext):
        number_text = self.visitChildren(ctx)
        try:
            number = ast.literal_eval(number_text)
        except:
            # exception occurs with leading zero number: 002
            number = float(number_text)
        return Number(
            number,
        )

    # Visit a parse tree produced by LuaParser#string.
    def visitString(self, ctx: LuaParser.StringContext):
        lua_str = ctx.getText()

        delimiter: StringDelimiter = StringDelimiter.SINGLE_QUOTE
        p = re.compile(r"^\[=+\[(.*)]=+]")  # nested quote pattern
        # try remove double quote:
        if lua_str.startswith('"') and lua_str.endswith('"'):
            lua_str = lua_str[1:-1]
            delimiter = StringDelimiter.DOUBLE_QUOTE
        # try remove single quote:
        elif lua_str.startswith("'") and lua_str.endswith("'"):
            lua_str = lua_str[1:-1]
            delimiter = StringDelimiter.SINGLE_QUOTE
        # try remove double square bracket:
        elif lua_str.startswith("[[") and lua_str.endswith("]]"):
            lua_str = lua_str[2:-2]
            delimiter = StringDelimiter.DOUBLE_SQUARE
        # nested quote
        elif p.match(lua_str):
            lua_str = p.search(lua_str).group(1)

        return String(lua_str, delimiter)


def parse(source: str) -> Chunk:
    """Parse Lua source to a Chunk."""
    lexer = LuaLexer(InputStream(source))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ConsoleErrorListener())
    lexer.addErrorListener(LexerErrorListener())

    token_stream = CommonTokenStream(lexer)
    parser = LuaParser(token_stream)
    parser.addErrorListener(ConsoleErrorListener())
    parser.addErrorListener(StrictErrorListener())
    tree = parser.start_()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxException("syntax errors")
    else:
        v = MyVisitor()
        val = v.visit(tree)
        print(val)
        return val


def get_token_stream(source: str) -> CommonTokenStream:
    """Get the antlr token stream."""
    lexer = LuaLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    return stream


def walk(root: Node) -> Generator[None, Node, None]:
    # base case:
    if root is None:
        return

    tree_visitor = WalkVisitor()
    tree_visitor.visit(root)
    for n in tree_visitor.nodes:
        yield n


def to_pretty_str(root: Node, indent=2) -> str:
    return printers.PythonStyleVisitor(indent).visit(root)


def to_lua_source(root: Node, indent=4) -> str:
    return printers.LuaOutputVisitor(indent_size=indent).visit(root)


def to_xml_str(tree):
    tree_visitor = printers.HTMLStyleVisitor()
    return tree_visitor.get_xml_string(tree)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_json = getattr(o, "to_json")
            if callable(to_json):
                return to_json()

        except AttributeError:
            return {k: v for k, v in o.__dict__.items() if not k.startswith("_")}


def to_pretty_json(root: Node) -> str:
    return json.dumps(root, cls=JSONEncoder, indent=4)


class ASTVisitor:
    def visit(self, root):
        # base case:
        if root is None:
            return
        node_stack = [root]

        while len(node_stack) > 0:
            node = node_stack.pop()
            # push childs to the stack:
            if isinstance(node, Node):
                # call visit method
                name = "visit_" + node.__class__.__name__
                tree_visitor = getattr(self, name, None)
                if tree_visitor:
                    tree_visitor(node)

                # add childs
                children = [
                    attr for attr in node.__dict__.keys() if not attr.startswith("_")
                ]
                for child in children:
                    node_stack.append(node.__dict__[child])
            elif isinstance(node, list):
                # append node list in reversal order
                for n in reversed(node):
                    node_stack.append(n)


class ASTRecursiveVisitor:
    def visit(self, node):
        if isinstance(node, Node):
            # call enter node method
            # if no visitor method found for this arg type,
            # search in parent arg type:
            parent_type = node.__class__
            while parent_type != object:
                name = "enter_" + parent_type.__name__
                tree_visitor = getattr(self, name, None)
                if tree_visitor:
                    tree_visitor(node)
                    break
                else:
                    parent_type = parent_type.__bases__[0]

            # visit all object public attributes:
            children = [
                attr for attr in node.__dict__.keys() if not attr.startswith("_")
            ]
            for child in children:
                self.visit(node.__dict__[child])

            # call exit node method
            # if no visitor method found for this arg type,
            # search in parent arg type:
            parent_type = node.__class__
            while parent_type != object:
                name = "exit_" + parent_type.__name__
                tree_visitor = getattr(self, name, None)
                if tree_visitor:
                    tree_visitor(node)
                    break
                else:
                    parent_type = parent_type.__bases__[0]
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

    @visitor(type(None))
    def visit(self, node):
        pass

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
    def visit(self, node: Table):
        self._nodes.append(node)
        for field in node.fields:
            self.visit(field)

    @visitor(Field)
    def visit(self, node: Field):
        self._nodes.append(node)
        self.visit(node.key)
        self.visit(node.value)

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

    @visitor(Varargs)
    def visit(self, node):
        self._nodes.append(node)

    @visitor(Repeat)
    def visit(self, node):
        self._nodes.append(node)
        self.visit(node.body)
        self.visit(node.test)

    @visitor(SemiColon)
    def visit(self, node):
        self._nodes.append(node)


class SyntaxException(Exception):
    pass


class ParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        raise SyntaxException(str(line) + ":" + str(column) + ": " + str(msg))

    def reportAmbiguity(
            self, recognizer, dfa, start_index, stop_index, exact, ambig_alts, configs
    ):
        pass

    def reportAttemptingFullContext(
            self, recognizer, dfa, start_index, stop_index, conflicting_alts, configs
    ):
        pass

    def reportContextSensitivity(
            self, recognizer, dfa, start_index, stop_index, prediction, configs
    ):
        pass
