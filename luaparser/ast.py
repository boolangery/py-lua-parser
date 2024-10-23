import ast
import re

from antlr4 import InputStream, CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

from luaparser.parser.LuaLexer import LuaLexer
from luaparser.astnodes import *
from luaparser import printers
from luaparser.parser.LuaParser import LuaParser
from luaparser.parser.LuaParserVisitor import LuaParserVisitor
from luaparser.utils.visitor import *
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
import json
from typing import Generator, Tuple


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
        if node.symbol.type == LuaParser.EOF:
            return None
        elif node.symbol.type == LuaParser.NAME:
            return Name(node.getText())
        else:
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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_empty.
    def visitStat_empty(self, ctx: LuaParser.Stat_emptyContext):
        return SemiColon()

    # Visit a parse tree produced by LuaParser#stat_assignment.
    def visitStat_assignment(self, ctx: LuaParser.Stat_assignmentContext):
        return Assign(
            targets=_listify(self.visit(ctx.varlist())),
            values=_listify(self.visit(ctx.explist())),
        )

    # Visit a parse tree produced by LuaParser#stat_functioncall.
    def visitStat_functioncall(self, ctx: LuaParser.Stat_functioncallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_label.
    def visitStat_label(self, ctx: LuaParser.Stat_labelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_break.
    def visitStat_break(self, ctx: LuaParser.Stat_breakContext):
        return Break()

    # Visit a parse tree produced by LuaParser#stat_goto.
    def visitStat_goto(self, ctx: LuaParser.Stat_gotoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_do.
    def visitStat_do(self, ctx: LuaParser.Stat_doContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_while.
    def visitStat_while(self, ctx: LuaParser.Stat_whileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_repeat.
    def visitStat_repeat(self, ctx: LuaParser.Stat_repeatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_if.
    def visitStat_if(self, ctx: LuaParser.Stat_ifContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_for.
    def visitStat_for(self, ctx: LuaParser.Stat_forContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_function.
    def visitStat_function(self, ctx: LuaParser.Stat_functionContext):
        func_name = self.visitFuncname(ctx.funcname())
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return Function(func_name, param_list, block)

    # Visit a parse tree produced by LuaParser#stat_localfunction.
    def visitStat_localfunction(self, ctx: LuaParser.Stat_localfunctionContext):
        func_name = self.visit(ctx.NAME())
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return LocalFunction(func_name, param_list, block)

    # Visit a parse tree produced by LuaParser#stat_local.
    def visitStat_local(self, ctx: LuaParser.Stat_localContext):
        att_name_list = self.visitAttnamelist(ctx.attnamelist())

        if ctx.EQ():
            exp_list = self.visitExplist(ctx.explist())
        else:
            exp_list = []

        return LocalAssign(targets=att_name_list, values=exp_list)

    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx: LuaParser.FunctiondefContext) -> AnonymousFunction:
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return AnonymousFunction(param_list, block)

    # Visit a parse tree produced by LuaParser#attnamelist.
    def visitAttnamelist(self, ctx: LuaParser.AttnamelistContext):
        return [self.visit(a) for a in ctx.nameattrib()]

    def visitNameattrib(self, ctx: LuaParser.NameattribContext):
        name = self.visit(ctx.NAME())
        if ctx.attrib():
            attrib = self.visit(ctx.attrib())
            name.attribute = attrib
        return name

    # Visit a parse tree produced by LuaParser#attrib.
    def visitAttrib(self, ctx: LuaParser.AttribContext):
        return Attribute(ctx.NAME().getText())

    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx: LuaParser.RetstatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx: LuaParser.LabelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#funcname.
    def visitFuncname(self, ctx: LuaParser.FuncnameContext):
        names = ctx.NAME()
        has_invoke = ctx.COL() is not None
        root = self.visit(names[0])
        until = len(names) - 1 if has_invoke else len(names)
        for i in range(1, until):
            root = Index(
                idx=self.visit(names[i]),
                value=root,
                notation=IndexNotation.DOT,
            )

        if has_invoke:
            return Invoke(root, self.visit(names[-1]), [])

        return root

    # Visit a parse tree produced by LuaParser#varlist.
    def visitVarlist(self, ctx: LuaParser.VarlistContext):
        return [self.visit(v) for v in ctx.var()]

    # Visit a parse tree produced by LuaParser#namelist.
    def visitNamelist(self, ctx: LuaParser.NamelistContext) -> List[Name]:
        return [self.visit(n) for n in ctx.NAME()]

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
        elif ctx.unary_op:
            if ctx.unary_op.type == LuaParser.NOT:
                return ULNotOp(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.POUND:
                return ULengthOP(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.MINUS:
                return UMinusOp(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.SQUIG:
                return UBNotOp(self.visit(ctx.exp(0)))

        elif ctx.op:
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))

            if ctx.op.type == LuaParser.CARET:
                return ExpoOp(left, right)
            elif ctx.op.type == LuaParser.STAR:
                return MultOp(left, right)
            elif ctx.op.type == LuaParser.SLASH:
                return FloatDivOp(left, right)
            elif ctx.op.type == LuaParser.PER:
                return ModOp(left, right)
            elif ctx.op.type == LuaParser.SS:
                return FloorDivOp(left, right)
            elif ctx.op.type == LuaParser.PLUS:
                return AddOp(left, right)
            elif ctx.op.type == LuaParser.MINUS:
                return SubOp(left, right)
            elif ctx.op.type == LuaParser.DD:
                return Concat(left, right)
            elif ctx.op.type == LuaParser.LT:
                return LessThanOp(left, right)
            elif ctx.op.type == LuaParser.GT:
                return GreaterThanOp(left, right)
            elif ctx.op.type == LuaParser.LE:
                return LessOrEqThanOp(left, right)
            elif ctx.op.type == LuaParser.GE:
                return GreaterOrEqThanOp(left, right)
            elif ctx.op.type == LuaParser.SQEQ:
                return NotEqToOp(left, right)
            elif ctx.op.type == LuaParser.EE:
                return EqToOp(left, right)
            elif ctx.op.type == LuaParser.AND:
                return AndLoOp(left, right)
            elif ctx.op.type == LuaParser.OR:
                return OrLoOp(left, right)
            elif ctx.op.type == LuaParser.AMP:
                return BAndOp(left, right)
            elif ctx.op.type == LuaParser.PIPE:
                return BOrOp(left, right)
            elif ctx.op.type == LuaParser.SQUIG:
                return BXorOp(left, right)
            elif ctx.op.type == LuaParser.LL:
                return BShiftLOp(left, right)
            elif ctx.op.type == LuaParser.GG:
                return BShiftROp(left, right)

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx: LuaParser.VarContext):
        if ctx.NAME():
            return Name(ctx.NAME().getText())
        else: # prefixexp tail
            root = self.visit(ctx.prefixexp())
            return self.visitAllTails(root, [ctx.tail()])

    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx: LuaParser.PrefixexpContext):
        if ctx.NAME():  # NAME tail*
            root = self.visit(ctx.NAME())
        elif ctx.functioncall():  # functioncall tail*
            root = self.visit(ctx.functioncall())
        else:  # '(' exp ')' tail*
            root: Expression = self.visit(ctx.exp())
            root.wrapped = True

        tail = self.visitAllTails(root, ctx.tail())
        return tail

    # Visit a parse tree produced by LuaParser#functioncall.
    def visitFunctioncall(self, ctx: LuaParser.FunctioncallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#functioncall_name.
    def visitFunctioncall_name(self, ctx: LuaParser.Functioncall_nameContext):
        name = self.visit(ctx.NAME())
        tail = self.visitAllTails(name, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return Call(tail, _listify(args), style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS)

    # Visit a parse tree produced by LuaParser#functioncall_nested.
    def visitFunctioncall_nested(self, ctx: LuaParser.Functioncall_nestedContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#functioncall_exp.
    def visitFunctioncall_exp(self, ctx: LuaParser.Functioncall_expContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#functioncall_expinvoke.
    def visitFunctioncall_expinvoke(self, ctx: LuaParser.Functioncall_expinvokeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#functioncall_invoke.
    def visitFunctioncall_invoke(self, ctx: LuaParser.Functioncall_invokeContext):
        source = self.visit(ctx.NAME(0))
        func = self.visit(ctx.NAME(1))
        tail = self.visitAllTails(source, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return Invoke(tail, func, _listify(args))

    # Visit a parse tree produced by LuaParser#functioncall_nestedinvoke.
    def visitFunctioncall_nestedinvoke(self, ctx: LuaParser.Functioncall_nestedinvokeContext):
        call = self.visit(ctx.functioncall())
        func = self.visit(ctx.NAME())
        tail = self.visitAllTails(call, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return Invoke(tail, func, _listify(args))

    def visitAllTails(self, root_exp: Expression, tails: List[LuaParser.TailContext]):
        if not tails:
            return root_exp

        root = root_exp  # parent root will be set in caller
        tail: Index = self.visitTail(tails[0])  # root tail
        i = 1
        while tail:
            tail.value = root
            root = tail

            if i >= len(tails):
                break

            tail = self.visit(tails[i])
            i += 1
        return root

    def visitTail(self, ctx: LuaParser.TailContext):
        if ctx.OB() and ctx.CB():
            return Index(
                idx=self.visit(ctx.exp()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.SQUARE,
            )
        else:
            return Index(
                idx=self.visit(ctx.NAME()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.DOT,
            )

    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx: LuaParser.ArgsContext):
        if ctx.OP() and ctx.CP():  # '(' explist? ')'
            exp_list = []
            if ctx.explist():
                exp_list = self.visit(ctx.explist())

            return True, exp_list
        elif ctx.tableconstructor():  # tableconstructor
            return False, self.visit(ctx.tableconstructor())
        else:  # string
            return False, self.visit(ctx.string())

    # Visit a parse tree produced by LuaParser#funcbody.
    def visitFuncbody(self, ctx: LuaParser.FuncbodyContext) -> Tuple[List[Expression], Block]:
        par_list = self.visitParlist(ctx.parlist())
        block = self.visit(ctx.block())
        return par_list, block

    # Visit a parse tree produced by LuaParser#parlist.
    def visitParlist(self, ctx: LuaParser.ParlistContext) -> List[Expression]:
        if ctx.namelist():
            name_list: List[Expression] = self.visitNamelist(ctx.namelist())
        else:
            name_list = []

        if ctx.DDD():
            name_list.append(Varargs())
        return name_list

    # Visit a parse tree produced by LuaParser#tableconstructor.
    def visitTableconstructor(self, ctx: LuaParser.TableconstructorContext):
        if ctx.fieldlist():
            fields = self.visit(ctx.fieldlist())

            array_like_index = 1
            if fields:  # optional
                for field in fields:
                    if field.key is None:
                        field.key = Number(array_like_index)
                        field.between_brackets = True
                        array_like_index += 1
            return Table(fields)
        return Table([])

    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx: LuaParser.FieldlistContext):
        return [self.visit(f) for f in ctx.field()]

    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx: LuaParser.FieldContext):
        if ctx.OB():  # '[' exp ']' '=' exp
            key = self.visit(ctx.exp(0))
            value = self.visit(ctx.exp(1))
            return Field(key, value, between_brackets=True)
        elif ctx.NAME():  # NAME '=' exp
            key = Name(ctx.NAME().getText())
            value = self.visit(ctx.exp(0))
            return Field(key, value)
        else:  # exp
            # Key will be set in parent call:
            return Field(None, self.visit(ctx.exp(0)))

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

    token_stream = CommonTokenStream(lexer)
    parser = LuaParser(token_stream)
    parser.addErrorListener(ConsoleErrorListener())
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
