import ast
import re
from typing import Tuple
from typing import TypeVar

from antlr4 import CommonTokenStream, ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

from luaparser.astnodes import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaParser import LuaParser
from luaparser.parser.LuaParserVisitor import LuaParserVisitor

TNode = TypeVar("TNode", bound=Node)


def _listify(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj


class BuilderVisitor(LuaParserVisitor):
    VISITED_CHANNEL = -1  # a magic number used to mark a token as visited
    COMMENT_CHANNEL = 2

    def __init__(self, comment_token_stream: CommonTokenStream):
        super().__init__()
        self.comment_token_stream = comment_token_stream

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
        if type(nextResult) is list:
            nextResult.append(aggregate)
            return nextResult
        if type(aggregate) is list:
            aggregate.append(nextResult)
            return aggregate
        if nextResult is None:
            return aggregate
        return [nextResult, aggregate]

    def add_comments(self, start, stop: CommonToken, node: TNode,
                     allow_right_ctx: bool = False, ignore_right_nl: bool = False, ignore_left_comma: bool = False,
                     ignore_left_double_nl: bool = False) -> TNode:
        """Add comments to a node.
        """
        # Get left token until a double newline is found, meaning that comments are separated by a block.
        # Ignore COMMA tokens.
        next_left_token = start.tokenIndex - 1
        left_comments: List[Comment] = []
        while next_left_token >= 0:
            token = self.comment_token_stream.get(next_left_token)
            token_next = self.comment_token_stream.get(next_left_token - 1)
            next_left_token -= 1

            if ((token.channel is LuaLexer.DEFAULT_TOKEN_CHANNEL and
                 (token.type is not LuaLexer.COMMA) or (token.type is LuaLexer.COMMA and not ignore_left_comma)) or
                    ((token.type is LuaLexer.NL) and (token_next.type is LuaLexer.NL) and not ignore_left_double_nl)):
                break

            if token.channel == self.COMMENT_CHANNEL:
                left_comments.append(Comment(
                    token.text,
                    is_multi_line=token.type == LuaLexer.COMMENT,
                    first_token=token,
                    last_token=token,
                ))
                token.channel = self.VISITED_CHANNEL  # prevent from being visited again

        if left_comments:
            # Reverse the comments to get the correct order:
            node.comments.extend(reversed(left_comments))

        if allow_right_ctx:
            # Get right comment until a new line is found
            # A newline indicates the end of the comment and the next one should be assigned to next node.
            # We do not use getHiddenTokensToRight because we want to ignore COMMAs.
            next_right_token = stop.tokenIndex + 1 if stop else None
            while next_right_token:
                token = self.comment_token_stream.get(next_right_token)
                next_right_token += 1

                if ((token.channel is LuaLexer.DEFAULT_TOKEN_CHANNEL and token.type is not LuaLexer.COMMA) or
                        (token.type is LuaLexer.NL and not ignore_right_nl)):
                    break

                if token.channel == self.COMMENT_CHANNEL:
                    node.comments.append(Comment(
                        token.text,
                        is_multi_line=token.type == LuaLexer.COMMENT,
                        first_token=token,
                        last_token=token,
                    ))
                    token.channel = self.VISITED_CHANNEL

        return node

    def add_context(self, parser_nodes: ParserRuleContext or List[ParserRuleContext or TerminalNodeImpl], node: TNode,
                    allow_right_ctx: bool = False, ignore_right_nl: bool = False, ignore_left_comma: bool = False,
                    ignore_left_double_nl: bool = False, without_start_stop_tokens: bool = False) -> TNode:
        """Add comments and tokens to a node.

        Args:
            parser_nodes: The parser nodes to add the context from.
            node: The node to add the context to.
            allow_right_ctx: Whether to allow right context. Defaults to False. If true, will add comments from the
                right of the node.
            ignore_right_nl: Whether to ignore right newlines. Defaults to False.
            ignore_left_comma: Whether to ignore left commas. Defaults to False. Ignoring left commas is useful when
                we want to grab comments from the left even when the line start by a comma. This can be the case for
                table fields with a weird formatting.
            ignore_left_double_nl: Whether to ignore left double newlines. Defaults to False. Ignoring left double
                newlines is useful for chunk nodes where we want to grab comments from the left even when the line
                start by a double newline.
            without_start_stop_tokens: Whether to add the start and stop tokens. Defaults to False.
        """
        start_obj = parser_nodes[0] if isinstance(parser_nodes, list) else parser_nodes
        stop_obj = parser_nodes[-1] if isinstance(parser_nodes, list) else parser_nodes
        start = start_obj.start if isinstance(start_obj, ParserRuleContext) else start_obj.symbol
        stop = stop_obj.stop if isinstance(stop_obj, ParserRuleContext) else stop_obj.symbol

        node = self.add_comments(start, stop, node, allow_right_ctx, ignore_right_nl, ignore_left_comma,
                                 ignore_left_double_nl)

        if not without_start_stop_tokens:
            node.first_token = start
            node.last_token = stop

        return node

    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx: LuaParser.ChunkContext):
        return self.add_context(ctx, Chunk(
            body=self.visitChildren(ctx),
        ), ignore_left_double_nl=True, allow_right_ctx=True, ignore_right_nl=True)

    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx: LuaParser.BlockContext):
        statements = [self.visit(stat) for stat in ctx.stat()]
        if ctx.retstat():
            statements.append(self.visit(ctx.retstat()))
        return self.add_context(ctx, Block(
            body=statements
        ))

    # Visit a parse tree produced by LuaParser#stat_empty.
    def visitStat_empty(self, ctx: LuaParser.Stat_emptyContext):
        return SemiColon()

    # Visit a parse tree produced by LuaParser#stat_assignment.
    def visitStat_assignment(self, ctx: LuaParser.Stat_assignmentContext):
        return self.add_context(ctx, Assign(
            targets=_listify(self.visit(ctx.varlist())),
            values=_listify(self.visit(ctx.explist())),
        ), allow_right_ctx=True)

    # Visit a parse tree produced by LuaParser#stat_functioncall.
    def visitStat_functioncall(self, ctx: LuaParser.Stat_functioncallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_label.
    def visitStat_label(self, ctx: LuaParser.Stat_labelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LuaParser#stat_break.
    def visitStat_break(self, ctx: LuaParser.Stat_breakContext):
        return self.add_context(ctx, Break(), allow_right_ctx=True)

    # Visit a parse tree produced by LuaParser#stat_goto.
    def visitStat_goto(self, ctx: LuaParser.Stat_gotoContext):
        return self.add_context(ctx, Goto(self.visit(ctx.NAME())))

    # Visit a parse tree produced by LuaParser#stat_do.
    def visitStat_do(self, ctx: LuaParser.Stat_doContext):
        return self.add_context(ctx, Do(body=self.visit(ctx.block())))

    # Visit a parse tree produced by LuaParser#stat_while.
    def visitStat_while(self, ctx: LuaParser.Stat_whileContext):
        return self.add_context(ctx, While(
            test=self.visit(ctx.exp()),
            body=self.visit(ctx.block()),
        ))

    # Visit a parse tree produced by LuaParser#stat_repeat.
    def visitStat_repeat(self, ctx: LuaParser.Stat_repeatContext):
        return self.add_context(ctx, Repeat(
            body=self.visit(ctx.block()),
            test=self.visit(ctx.exp()),
        ))

    # Visit a parse tree produced by LuaParser#stat_if.
    def visitStat_if(self, ctx: LuaParser.Stat_ifContext):
        expressions = ctx.exp()
        blocks = ctx.block()
        nb_else_if = len(ctx.ELSEIF())
        if_stat = self.add_context(ctx, If(
            test=self.visit(expressions[0]),
            body=self.visit(blocks[0]),
            orelse=None,
        ))

        or_else_leaf = None
        if nb_else_if > 0:
            or_else_root = self.add_context([ctx.ELSEIF(0), blocks[1]], ElseIf(
                test=self.visit(expressions[1]),
                body=self.visit(blocks[1]),
                orelse=None,
            ))

            or_else_leaf = or_else_root
            for i in range(nb_else_if - 1):
                or_else_leaf.orelse = self.add_context([ctx.ELSEIF(i + 1), blocks[i + 2]], ElseIf(
                    test=self.visit(expressions[i + 2]),
                    body=self.visit(blocks[i + 2]),
                    orelse=None,
                ))
                or_else_leaf = or_else_leaf.orelse

            if_stat.orelse = or_else_root

        if ctx.ELSE():
            block = self.visit(blocks[len(blocks) - 1])
            if if_stat.orelse is None:
                if_stat.orelse = block
            else:
                or_else_leaf.orelse = block

        return if_stat

    # Visit a parse tree produced by LuaParser#stat_for.
    def visitStat_for(self, ctx: LuaParser.Stat_forContext):
        if ctx.IN():  # forin
            return self.add_context(ctx, Forin(
                body=self.visit(ctx.block()),
                iter=self.visit(ctx.explist()),
                targets=self.visit(ctx.namelist()),
            ))
        else:  # fornum
            return self.add_context(ctx, Fornum(
                target=self.visit(ctx.NAME()),
                start=self.visit(ctx.exp(0)),
                stop=self.visit(ctx.exp(1)),
                step=self.visit(ctx.exp(2)) if ctx.exp(2) else 1,
                body=self.visit(ctx.block()),
            ))

    # Visit a parse tree produced by LuaParser#stat_function.
    def visitStat_function(self, ctx: LuaParser.Stat_functionContext):
        func_name = self.visitFuncname(ctx.funcname())
        param_list, block = self.visitFuncbody(ctx.funcbody())

        if isinstance(func_name, Method):
            func_name.args = param_list
            func_name.body = block
            return self.add_context(ctx, func_name)

        return self.add_context(ctx, Function(func_name, param_list, block))

    # Visit a parse tree produced by LuaParser#stat_localfunction.
    def visitStat_localfunction(self, ctx: LuaParser.Stat_localfunctionContext):
        func_name = self.visit(ctx.NAME())
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return self.add_context(ctx, LocalFunction(func_name, param_list, block))

    # Visit a parse tree produced by LuaParser#stat_local.
    def visitStat_local(self, ctx: LuaParser.Stat_localContext):
        att_name_list = self.visitAttnamelist(ctx.attnamelist())

        if ctx.EQ():
            exp_list = self.visitExplist(ctx.explist())
        else:
            exp_list = []

        return self.add_context(ctx, LocalAssign(targets=att_name_list, values=exp_list))

    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx: LuaParser.FunctiondefContext) -> AnonymousFunction:
        param_list, block = self.visitFuncbody(ctx.funcbody())
        return self.add_context(ctx, AnonymousFunction(param_list, block))

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
        return Attribute(self.visit(ctx.NAME()))

    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx: LuaParser.RetstatContext):
        if ctx.RETURN():
            return self.add_context(ctx, Return(
                values=self.visit(ctx.explist()) if ctx.explist() else [],
            ))
        elif ctx.BREAK():
            return self.add_context(ctx, Break())
        else:
            return self.add_context(ctx, Continue())

    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx: LuaParser.LabelContext):
        return self.add_context(ctx, Label(label_id=self.visit(ctx.NAME())))

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
            return self.add_context(ctx, Method(
                source=root,
                name=self.visit(names[-1]),
                args=[],
                body=Block([])
            ))

        return self.add_context(ctx, root)

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
    def visitExp(self, ctx: LuaParser.ExpContext) -> Expression:
        exp: Expression = Nil()

        if ctx.NIL():
            exp = Nil()
        elif ctx.FALSE():
            exp = FalseExpr()
        elif ctx.TRUE():
            exp = TrueExpr()
        elif ctx.number():
            exp = self.visit(ctx.number())
        elif ctx.string():
            exp = self.visit(ctx.string())
        elif ctx.DDD():
            exp = Dots()
        elif ctx.functiondef():
            exp = self.visit(ctx.functiondef())
        elif ctx.prefixexp():
            exp = self.visit(ctx.prefixexp())
        elif ctx.tableconstructor():
            exp = self.visit(ctx.tableconstructor())
        elif ctx.unary_op:
            if ctx.unary_op.type == LuaParser.NOT:
                exp = ULNotOp(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.POUND:
                exp = ULengthOP(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.MINUS:
                exp = UMinusOp(self.visit(ctx.exp(0)))
            elif ctx.unary_op.type == LuaParser.SQUIG:
                exp = UBNotOp(self.visit(ctx.exp(0)))

        elif ctx.op:
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))

            if ctx.op.type == LuaParser.CARET:
                exp = ExpoOp(left, right)
            elif ctx.op.type == LuaParser.STAR:
                exp = MultOp(left, right)
            elif ctx.op.type == LuaParser.SLASH:
                exp = FloatDivOp(left, right)
            elif ctx.op.type == LuaParser.PER:
                exp = ModOp(left, right)
            elif ctx.op.type == LuaParser.SS:
                exp = FloorDivOp(left, right)
            elif ctx.op.type == LuaParser.PLUS:
                exp = AddOp(left, right)
            elif ctx.op.type == LuaParser.MINUS:
                exp = SubOp(left, right)
            elif ctx.op.type == LuaParser.DD:
                exp = Concat(left, right)
            elif ctx.op.type == LuaParser.LT:
                exp = LessThanOp(left, right)
            elif ctx.op.type == LuaParser.GT:
                exp = GreaterThanOp(left, right)
            elif ctx.op.type == LuaParser.LE:
                exp = LessOrEqThanOp(left, right)
            elif ctx.op.type == LuaParser.GE:
                exp = GreaterOrEqThanOp(left, right)
            elif ctx.op.type == LuaParser.SQEQ:
                exp = NotEqToOp(left, right)
            elif ctx.op.type == LuaParser.EE:
                exp = EqToOp(left, right)
            elif ctx.op.type == LuaParser.AND:
                exp = AndLoOp(left, right)
            elif ctx.op.type == LuaParser.OR:
                exp = OrLoOp(left, right)
            elif ctx.op.type == LuaParser.AMP:
                exp = BAndOp(left, right)
            elif ctx.op.type == LuaParser.PIPE:
                exp = BOrOp(left, right)
            elif ctx.op.type == LuaParser.SQUIG:
                exp = BXorOp(left, right)
            elif ctx.op.type == LuaParser.LL:
                exp = BShiftLOp(left, right)
            elif ctx.op.type == LuaParser.GG:
                exp = BShiftROp(left, right)

        return self.add_context(ctx, exp)

    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx: LuaParser.VarContext):
        if ctx.NAME():
            return Name(ctx.NAME().getText())
        else:  # prefixexp tail
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

    # Visit a parse tree produced by LuaParser#functioncall_name.
    def visitFunctioncall_name(self, ctx: LuaParser.Functioncall_nameContext):
        name = self.visit(ctx.NAME())
        tail = self.visitAllTails(name, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Call(tail, _listify(args),
                                          style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_nested.
    def visitFunctioncall_nested(self, ctx: LuaParser.Functioncall_nestedContext):
        call = self.visit(ctx.functioncall())
        tail = self.visitAllTails(call, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Call(tail, _listify(args),
                                          style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_exp.
    def visitFunctioncall_exp(self, ctx: LuaParser.Functioncall_expContext):
        exp = self.visitExp(ctx.exp())
        exp.wrapped = True
        tail = self.visitAllTails(exp, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Call(tail, _listify(args),
                                          style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_expinvoke.
    def visitFunctioncall_expinvoke(self, ctx: LuaParser.Functioncall_expinvokeContext):
        exp = self.visitExp(ctx.exp())
        exp.wrapped = True
        tail = self.visitAllTails(exp, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        func = self.visit(ctx.NAME())
        return self.add_context(ctx, Invoke(tail, func, _listify(args),
                                            style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_invoke.
    def visitFunctioncall_invoke(self, ctx: LuaParser.Functioncall_invokeContext):
        source = self.visit(ctx.NAME(0))
        func = self.visit(ctx.NAME(1))
        tail = self.visitAllTails(source, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Invoke(tail, func, _listify(args),
                                            style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

    # Visit a parse tree produced by LuaParser#functioncall_nestedinvoke.
    def visitFunctioncall_nestedinvoke(self, ctx: LuaParser.Functioncall_nestedinvokeContext):
        call = self.visit(ctx.functioncall())
        func = self.visit(ctx.NAME())
        tail = self.visitAllTails(call, ctx.tail())
        par, args = self.visitArgs(ctx.args())
        return self.add_context(ctx, Invoke(tail, func, _listify(args),
                                            style=CallStyle.DEFAULT if par else CallStyle.NO_PARENTHESIS))

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
            return self.add_context(ctx, Index(
                idx=self.visit(ctx.exp()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.SQUARE,
            ))
        else:
            return self.add_context(ctx, Index(
                idx=self.visit(ctx.NAME()),
                value=Name(""),  # value must be set in parent
                notation=IndexNotation.DOT,
            ))

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
            return self.add_context(ctx, Table(fields))
        return self.add_context(ctx, Table([]))

    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx: LuaParser.FieldlistContext):
        fields = [self.visit(f) for f in ctx.field()]

        # Grab right comments after last field ignoring commas:
        self.add_context(ctx.field(len(fields) - 1), fields[-1], allow_right_ctx=True, ignore_right_nl=True)

        return fields

    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx: LuaParser.FieldContext):
        if ctx.OB():  # '[' exp ']' '=' exp
            key = self.visit(ctx.exp(0))
            value = self.visit(ctx.exp(1))
            return self.add_context(ctx, Field(key, value, between_brackets=True), allow_right_ctx=True,
                                    ignore_left_comma=True)
        elif ctx.NAME():  # NAME '=' exp
            key = Name(ctx.NAME().getText())
            value = self.visit(ctx.exp(0))
            return self.add_context(ctx, Field(key, value), allow_right_ctx=True, ignore_left_comma=True)
        else:  # exp
            # Key will be set in parent call:
            return self.add_context(ctx, Field(None, self.visit(ctx.exp(0))), allow_right_ctx=True,
                                    ignore_left_comma=True)

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

        # Eval string to unescape:
        try:
            lua_str = ast.literal_eval(F'"{lua_str}"')
        except:
            pass
        return String(lua_str, delimiter)
