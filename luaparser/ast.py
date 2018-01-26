import ast
import re
from antlr4 import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaVisitor import LuaVisitor
from luaparser.astnodes import *
from luaparser.asttokens import Tokens
from luaparser.parser.LuaParser import LuaParser
from luaparser import printers
from antlr4.error.ErrorListener import ErrorListener

def parse(source):
    lexer = LuaLexer(InputStream(source))
    parser = LuaParser(CommonTokenStream(lexer))
    parser.addErrorListener(ParserErrorListener())
    astVisitor = ParseTreeVisitor()
    return astVisitor.visit(parser.chunk())

def walk(root):
    # base case:
    if root is None:
        return
    nodeStack = []
    nodeStack.append(root)

    while(len(nodeStack) > 0):
        node = nodeStack.pop()
        # push childs to the stack:
        if isinstance(node, Node):
            yield node

            # add childs
            childs = [attr for attr in node.__dict__.keys() if not attr.startswith("_")]
            for child in childs:
                nodeStack.append(node.__dict__[child])
        elif isinstance(node, list):
            # append node list in reversal order
            for n in reversed(node):
                nodeStack.append(n)

def toPrettyStr(tree, indent=2):
    return printers.PythonStyleVisitor(indent).visit(tree)

def _listify(obj):
    if not isinstance(obj, list):
        return [obj]
    else:
        return obj

def _setMetadata(ctx, node):
    if isinstance(ctx, TerminalNode):
        node.tokens.append(ctx.symbol)
    elif isinstance(ctx, list):
        # merge tokens from all ctx in list
        for context in ctx:
            if isinstance(context, TerminalNode):
                node.tokens.append(context.symbol)
            else:
                for t in context.parser._input.getTokens(context.start.tokenIndex, context.stop.tokenIndex + 1):
                    node.tokens.append(t)
    else:
        if ctx.start and ctx.stop:
            for t in ctx.parser._input.getTokens(ctx.start.tokenIndex, ctx.stop.tokenIndex + 1):
                node.tokens.append(t)
    return node

class ParseTreeVisitor(LuaVisitor):
    def visitChildren(self, ctx, mergeList=False):
        if ctx.children:
            return self.visitChildrenList(ctx.children, mergeList)
        else:
            return []

    def visitChildrenList(self, children, mergeList=False):
        nodes = []
        for child in children:
            node = self.visit(child)
            if node != None:
                if mergeList and isinstance(node, list):
                    nodes.extend(node)
                else:
                    nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        return nodes

    def visitStartingFrom(self, ctx, index, mergeList=False):
        if ctx.children:
            return self.visitChildrenList(ctx.children[index:], mergeList)
        else:
            return []

    ''' Visiting root nodes.
    '''
    def visitChunk(self, ctx):
        return _setMetadata(ctx, Chunk(self.visit(ctx.children[0])))

    def visitBlock(self, ctx):
        return _setMetadata(ctx, Block(_listify(self.visitChildren(ctx))))

    def visitStat(self, ctx):
        return self.visit(ctx.children[0])

    ''' Statements '''
    def visitAssignment(self, ctx):
        # var_list ASSIGN expr_list
        return _setMetadata(ctx, Assign(
            targets=_listify(self.visit(ctx.children[0])),
            values=_listify(self.visit(ctx.children[2]))))

    def visitLocal(self, ctx):
        """local
        : LOCAL
        ( name_list (ASSIGN expr_list)?
        | FUNCTION NAME func_body)"""
        # LOCAL name_list (ASSIGN expr_list)?
        if isinstance(ctx.children[1], LuaParser.Name_listContext):
            # LOCAL name_list (ASSIGN expr_list)?
            if len(ctx.children)>2:
                return _setMetadata(ctx, LocalAssign(
                    targets=_listify(self.visit(ctx.children[1])),
                    values=_listify(self.visit(ctx.children[3]))))
            # LOCAL name_list
            else:
                return _setMetadata(ctx, LocalAssign(
                    targets=_listify(self.visit(ctx.children[1])),
                    values=[]))

        # LOCAL FUNCTION NAME func_body
        else:
            name     = self.visit(ctx.children[2])
            funcBody = self.visit(ctx.children[3])
            return _setMetadata(ctx, LocalFunction(name=name, args=funcBody[0], body=funcBody[1]))

    def visitFunc_body(self, ctx):
        """func_body
        : OPAR param_list CPAR block END"""
        params = self.visit(ctx.children[1])
        body   = self.visit(ctx.children[3]).body
        return (params, body)

    def visitVar_list(self, ctx):
        # var[True] (COMMA var[True])*
        return self.visitChildren(ctx)

    def visitVar(self, ctx):
        """var[bool assign]
        : callee[assign] tail*"""
        if len(ctx.children) < 2:
            return self.visit(ctx.children[0])
        else:
            root = self.visit(ctx.children[0])

            for i in range(1, len(ctx.children)):
                tail = self.visit(ctx.children[i])
                if isinstance(tail, Index):
                    tail.value = root
                elif isinstance(tail, Invoke):
                    tail.source = root
                elif isinstance(tail, Call):
                    tail.func = root
                else:
                    tail = Call(
                        func=root,
                        args=_listify(tail))

                # extend with child tokens
                tail.tokens.extend(root.tokens)
                _setMetadata(ctx.children[i], tail)

                root = tail
            return root


    def visitCallee(self, ctx):
        """callee[bool assign]
        : OPAR expr CPAR | NAME"""
        return self.visitChildren(ctx)

    def visitTail(self, ctx):
        """ tail
        : DOT NAME
        | OBRACK expr CBRACK
        | COL NAME OPAR expr_list? CPAR
        | COL NAME table_constructor
        | COL NAME STRING
        | OPAR expr_list? CPAR
        | table_constructor
        | STRING"""
        return 'rr'

    def visitTail_dot_index(self, ctx):
        """DOT NAME"""
        return Index(
            value=None, # to set in parent
            idx=self.visit(ctx.children[1]))

    def visitTail_brack_index(self, ctx):
        """OBRACK expr CBRACK"""
        return Index(
            value=None,  # to set in parent
            idx=self.visit(ctx.children[1]))

    def visitTail_invoke(self, ctx):
        """COL NAME OPAR expr_list? CPAR"""
        return Invoke(
            source=None,  # to set in parent
            func=self.visit(ctx.children[1]),
            args=_listify(self.visit(ctx.children[3]) or []))

    def visitTail_invoke_table(self, ctx):
        """COL NAME table_constructor"""
        return Invoke(
            source=None,  # to set in parent
            func=self.visit(ctx.children[1]),
            args=_listify(self.visit(ctx.children[2]) or []))

    def visitTail_invoke_str(self, ctx):
        """COL NAME STRING"""
        return Invoke(
            source=None,  # to set in parent
            func=self.visit(ctx.children[1]),
            args=_listify(self.visit(ctx.children[2]) or []))

    def visitTail_call(self, ctx):
        """OPAR expr_list? CPAR"""
        return Call(
            func=None,  # to set in parent
            args=_listify(self.visit(ctx.children[1]) or []))

    def visitTail_table(self, ctx):
        """table_constructor"""
        return self.visit(ctx.children[0])

    def visitTail_string(self, ctx):
        """STRING"""
        return self.visit(ctx.children[0])

    def visitTerminal(self, ctx):
        def NilHandler(ctx): return _setMetadata(ctx, Nil())
        def NameHandler(ctx): return _setMetadata(ctx, Name(ctx.getText()))
        def TrueHandler(ctx):return _setMetadata(ctx, TrueExpr())
        def FalseHandler(ctx):return _setMetadata(ctx, FalseExpr())
        def NumberHandler(ctx):
            # using python number eval to parse lua number
            number = ast.literal_eval(ctx.getText())
            return _setMetadata(ctx, Number(number))
        def StringHandler(ctx):
            luaStr = ctx.getText()
            p = re.compile('^\[=+\[(.*)\]=+\]')  # nested quote pattern
            # try remove double quote:
            if luaStr.startswith('"') and luaStr.endswith('"'):
                luaStr = luaStr[1:-1]
            # try remove single quote:
            elif luaStr.startswith("'") and luaStr.endswith("'"):
                luaStr = luaStr[1:-1]
            # try remove double square bracket:
            elif luaStr.startswith("[[") and luaStr.endswith("]]"):
                luaStr = luaStr[2:-2]
            # nested quote
            elif p.match(luaStr):
                luaStr = p.search(luaStr).group(1)
            return _setMetadata(ctx, String(luaStr))
        def BreakHandler(ctx): return Break()

        handlers = {
            Tokens.NIL.value    : NilHandler,
            Tokens.NAME.value   : NameHandler,
            Tokens.TRUE.value   : TrueHandler,
            Tokens.FALSE.value  : FalseHandler,
            Tokens.NUMBER.value : NumberHandler,
            Tokens.STRING.value : StringHandler,
            Tokens.BREAK.value  : BreakHandler,
        }

        if ctx.symbol.type in handlers:
            return handlers[ctx.symbol.type](ctx)
        else:
            return None

    '''Operators'''
    def visitLeftRightOperator(self, ctx, nodeOnToken):
        """transform context of type: expr ((TOKEN_1 | TOKEN_N) expr)*
        to nodes.
        :param nodeOnToken dictionary of Node class per token type"""
        # expr ((TOKEN_1 | TOKEN_N) expr)*
        if len(ctx.children)>1:
            left = self.visit(ctx.children[0])
            for i in range(1, len(ctx.children), 2):
                right = self.visit(ctx.children[i + 1])
                root  = _setMetadata(ctx, nodeOnToken[ctx.children[i].symbol.type](
                    left=left,
                    right=right))
                left = root
            return left
        # expr
        else:
            return self.visit(ctx.children[0])

    def visitAdd_expr(self, ctx):
        return self.visitLeftRightOperator(ctx, {
            Tokens.ADD.value    : AddOp,
            Tokens.MINUS.value  : SubOp,
        })

    def visitMult_expr(self, ctx):
        return self.visitLeftRightOperator(ctx, {
            Tokens.MULT.value   : MultOp,
            Tokens.DIV.value    : FloatDivOp,
            Tokens.FLOOR.value  : FloorDivOp,
            Tokens.MOD.value    : ModOp,
        })

    def visitUnary_expr(self, ctx):
        """unary_expr
        : MINUS unary_expr
        | LENGTH pow_expr
        | NOT unary_expr
        | BITNOT unary_expr
        | pow_expr"""
        if len(ctx.children)>1:
            if ctx.children[0].symbol.type == Tokens.MINUS.value:
                return _setMetadata(ctx, USubOp(self.visit(ctx.children[1])))
            elif ctx.children[0].symbol.type == Tokens.LENGTH.value:
                return _setMetadata(ctx, ULengthOP(self.visit(ctx.children[1])))
            elif ctx.children[0].symbol.type == Tokens.NOT.value:
                return _setMetadata(ctx, ULNotOp(self.visit(ctx.children[1])))
            else:
                return _setMetadata(ctx, UBNotOp(self.visit(ctx.children[1])))
        else:
            return self.visit(ctx.children[0])

    def visitPow_expr(self, ctx):
        """pow_expr
        : atom (POW atom)*"""
        return self.visitLeftRightOperator(ctx, {
            Tokens.POW.value: ExpoOp,
        })

    def visitBitwise_expr(self, ctx):
        """bitwise_expr
        : unary_expr ((BITAND | BITOR | BITXOR | BITRSHIFT | BITRLEFT | BITNOT) unary_expr)*"""
        return self.visitLeftRightOperator(ctx, {
            Tokens.BITAND.value     : BAndOp,
            Tokens.BITOR.value      : BOrOp,
            Tokens.BITNOT.value     : BXorOp,
            Tokens.BITRSHIFT.value  : BShiftROp,
            Tokens.BITRLEFT.value   : BShiftLOp,
        })

    def visitRel_expr(self, ctx):
        """rel_expr
        : concat_expr ((LT | GT | LTEQ | GTEQ | NEQ | EQ) concat_expr)?"""
        return self.visitLeftRightOperator(ctx, {
            Tokens.LT.value     : LessThanOp,
            Tokens.GT.value     : GreaterThanOp,
            Tokens.LTEQ.value   : LessOrEqThanOp,
            Tokens.GTEQ.value   : GreaterOrEqThanOp,
            Tokens.NEQ.value    : NotEqToOp,
            Tokens.EQ.value     : EqToOp,
        })

    def visitOr_expr(self, ctx):
        return self.visitLeftRightOperator(ctx, {
            Tokens.OR.value: OrLoOp,
        })

    def visitAnd_expr(self, ctx):
        return self.visitLeftRightOperator(ctx, {
            Tokens.AND.value: AndLoOp,
        })

    def visitConcat_expr(self, ctx):
        return self.visitLeftRightOperator(ctx, {
            Tokens.CONCAT.value: Concat,
        })


    def visitTable_constructor(self, ctx):
        """table_constructor
        : OBRACE field_list? CBRACE"""
        if len(ctx.children) > 2:
            keys   = []
            values = []
            fields = self.visit(ctx.children[1])
            tableIndex = 1
            for field in fields:
                # no key, array like table
                if field[0] is None:
                    keys.append(Number(tableIndex))
                    tableIndex += 1
                else:
                    keys.append(field[0])
                values.append(field[1])
            return _setMetadata(ctx, Table(keys, values))
        else:
            return _setMetadata(ctx, Table([], []))

    def visitField_list(self, ctx):
        """field_list
        : field (field_sep field)* field_sep?"""
        fields = []
        for child in ctx.children:
            if isinstance(child, LuaParser.FieldContext):
                fields.append(self.visit(child))
        return fields

    def visitField(self, ctx):
        """field
        : OBRACK expr CBRACK ASSIGN expr
        | NAME ASSIGN expr
        | expr"""
        lenght = len(ctx.children)
        # OBRACK expr CBRACK ASSIGN expr
        if lenght > 3:
            return (self.visit(ctx.children[1]), self.visit(ctx.children[4]))
        # NAME ASSIGN expr
        elif lenght > 2:
            return (self.visit(ctx.children[0]), self.visit(ctx.children[2]))
        # expr
        else:
            return (None, self.visit(ctx.children[0]))


    def visitFunction(self, ctx):
        """function
        : FUNCTION names (COL NAME func_body | func_body)"""
        names = self.visit(ctx.children[1])
        # FUNCTION names COL NAME func_body
        if len(ctx.children) > 3:
            funcBody = self.visit(ctx.children[4])
            return _setMetadata(ctx, Method(
                source=names,
                name=self.visit(ctx.children[3]),
                args=funcBody[0],
                body=funcBody[1]))
        # FUNCTION names func_body
        else:
            funcBody = self.visit(ctx.children[2])
            return _setMetadata(ctx, Function(
                name=names,
                args=funcBody[0],
                body=funcBody[1]))

    def visitNames(self, ctx):
        """names
        : NAME (DOT NAME)*"""
        if len(ctx.children) > 1:
            child = Index(
                value=self.visit(ctx.children[0]),
                idx=self.visit(ctx.children[2]))
            for i in range(3, len(ctx.children), 2):
                root = Index(
                    value=child,
                    idx=self.visit(ctx.children[i+1]))
                child = root
            return _setMetadata(ctx, child)
        else:
            return self.visitChildren(ctx)


    def visitFunction_literal(self, ctx):
        """function_literal
        : FUNCTION func_body"""
        funcBody = self.visit(ctx.children[1])
        return _setMetadata(ctx, AnonymousFunction(
            args=funcBody[0],
            body=funcBody[1]))

    def visitDo_block(self, ctx):
        """do_block
        : DO block END"""
        return _setMetadata(ctx, Do(self.visit(ctx.children[1]).body))

    def visitFor_stat(self, ctx):
        """for_stat
        : FOR
        ( NAME ASSIGN expr COMMA expr (COMMA expr)? do_block
        | name_list IN expr_list do_block
        )"""
        # FOR NAME ASSIGN expr COMMA expr (COMMA expr)? do_block
        if len(ctx.children) > 5:
            start = self.visit(ctx.children[3])
            stop  = self.visit(ctx.children[5])
            step  = 1
            # if has step
            if len(ctx.children) > 6:
                step = self.visit(ctx.children[7])

            return _setMetadata(ctx, Fornum(
                target=self.visit(ctx.children[1]),
                start=start,
                stop=stop,
                step=step,
                body=self.visit(ctx.children[-1]).body)) # visitDo_block
        # FOR name_list IN expr_list do_block
        else:
            return _setMetadata(ctx, Forin(
                body=self.visit(ctx.children[4]).body,
                iter=self.visit(ctx.children[3]),
                targets=_listify(self.visit(ctx.children[1]))))

    def visitWhile_stat(self, ctx):
        """while_stat
        : WHILE expr do_block"""
        return _setMetadata(ctx, While(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[2]).body))

    def visitRepeat_stat(self, ctx):
        """repeat_stat
        : REPEAT block UNTIL expr"""
        return _setMetadata(ctx, Repeat(
            body=self.visit(ctx.children[1]).body,
            test=self.visit(ctx.children[3])))

    def visitIf_stat(self, ctx):
        """if_stat
        : IF expr THEN block elseif_stat* else_stat? END"""
        mainIf = If(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[3]).body,
            orelse=None)
        lastStat = mainIf

        for node in ctx.children[4:-1]:
            if isinstance(node, LuaParser.Else_statContext):
                lastStat.orelse = self.visit(node)
            else:
                elseIfNodes = self.visit(node)
                elseIf = ElseIf(test=elseIfNodes[0], body=elseIfNodes[1], orelse=None)
                lastStat.orelse = elseIf
                lastStat = elseIf
        return _setMetadata(ctx, mainIf)

    def visitElseif_stat(self, ctx):
        """elseif_stat
        : ELSEIF expr THEN block"""
        return [
            self.visit(ctx.children[1]),
            self.visit(ctx.children[3]).body]

    def visitElse_stat(self, ctx):
        """else_stat
        : ELSE block"""
        return self.visit(ctx.children[1]).body

    def visitLabel(self, ctx):
        """label
        : COLCOL NAME COLCOL"""
        return _setMetadata(ctx, Label(id=self.visit(ctx.children[1])))

    def visitGoto_stat(self, ctx):
        return _setMetadata(ctx, Goto(label=self.visit(ctx.children[1])))

    def visitRet_stat(self, ctx):
        """ret_stat
        : RETURN expr_list? SEMCOL?"""
        return _setMetadata(ctx, Return(_listify(self.visitChildren(ctx))))










    """

    ''' ----------------------------------------------------------------------- '''
    ''' 3.3 – Statements                                                        '''
    ''' ----------------------------------------------------------------------- '''

    def visitLocalset(self, ctx):
        # 'local' namelist ('=' explist)?
        if len(ctx.children) > 2:
            return _setMetadata(ctx, LocalAssign(
                targets=_listify(self.visit(ctx.children[1])), \
                values=_listify(self.visit(ctx.children[3]))))
        else:
            return _setMetadata(ctx, LocalAssign(
                targets=_listify(self.visit(ctx.children[1])), \
                values=[]))

    def visitWhileStat(self, ctx):
        # 'while' exp 'do' block 'end' ;
        return _setMetadata(ctx, While(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[3]).body))

    def visitDo(self, ctx):
        return _setMetadata(ctx, Do(self.visit(ctx.children[1]).body))

    def visitRepeat(self, ctx):
        # 'repeat' block 'until' exp ;
        return _setMetadata(ctx, Repeat(
            body=self.visit(ctx.children[1]).body,
            test=self.visit(ctx.children[3])))

    def visitCall(self, ctx):
        # varOrExp args+

        return _setMetadata(ctx, Call(
            func=self.visit(ctx.children[0]), \
            args=_listify(self.visitStartingFrom(ctx, 1))))

    def visitInvoke(self, ctx):
        # varOrExp (':' name args)+
        child = Invoke(
            source=self.visit(ctx.children[0]), \
            func=self.visit(ctx.children[2]), \
            args=_listify(self.visit(ctx.children[3])))
        # if nested invoke:
        if len(ctx.children)>4:
            # iterate (':' name args)
            for i in range(4, len(ctx.children), 3):
                root = Invoke(
                    source=child, \
                    func=self.visit(ctx.children[i+1]), \
                    args=_listify(self.visit(ctx.children[i+2])))
                child = root
            return _setMetadata(ctx, child)
        else:
            return _setMetadata(ctx, child)

    def visitFornum(self, ctx):
        # 'for' name '=' exp ',' exp (',' exp)? 'do' block 'end' ;
        # if has step expr
        if len(ctx.children) > 8:
            return _setMetadata(ctx, Fornum(
                target=self.visit(ctx.children[1]),
                start=self.visit(ctx.children[3]),
                stop=self.visit(ctx.children[5]),
                step=self.visit(ctx.children[7]),
                body=self.visit(ctx.children[-2]).body))
        else:
            return _setMetadata(ctx, Fornum(
                target=self.visit(ctx.children[1]),
                start=self.visit(ctx.children[3]),
                stop=self.visit(ctx.children[5]),
                step=Number(1),
                body=self.visit(ctx.children[-2]).body))

    def visitForin(self, ctx):
        # 'for' namelist 'in' explist 'do' block 'end' ;
        return _setMetadata(ctx, Forin(
            body=self.visit(ctx.children[5]).body,
            iter=self.visit(ctx.children[3]),
            targets=_listify(self.visit(ctx.children[1]))))

    def visitPrefixexp(self, ctx):
        # varOrExp nameAndArgs*

        nodes = self.visitChildren(ctx, True)
        print('\nvisitPrefixexp')
        print(vars(ctx))
        print(nodes)

        if isinstance(nodes, list):
            if len(nodes) > 1:
                if isinstance(nodes[0], Name) or isinstance(nodes[0], Index):
                    if isinstance(nodes[-1], Invoke):
                        nodes[-1].source = nodes[0]
                        for i in range(len(nodes)-1, 0, -1):
                            if isinstance(nodes[i], Invoke):
                                nodes[i].source = nodes[i-1]
                        return _setMetadata(ctx, nodes[-1])
                    else:
                        return _setMetadata(ctx, Call(
                            func=nodes[0],
                            args=nodes[1:]
                        ))


        return self.visitChildren(ctx)

    def visitNameAndArgs(self, ctx):
        # (COLON name)? args
        if len(ctx.children)>1:
            return _setMetadata(ctx, Invoke(
                source=None, # will be filled in parent visitor
                func=self.visit(ctx.children[1]),
                args=_listify(self.visit(ctx.children[2]))))
        else:
            return self.visit(ctx.children[0])

    def visitIfStat(self, ctx):
        # 'if' exp 'then' block elseIfStat* elseStat? 'end' ;
        mainIf = If(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[3]).body,
            orelse=None)
        lastStat = mainIf

        for node in ctx.children[4:-1]:
            if isinstance(node, LuaParser.ElseStatContext):
                lastStat.orelse = self.visit(node)
            else:
                elseIfNodes = self.visit(node)
                elseIf = ElseIf(test=elseIfNodes[0], body=elseIfNodes[1], orelse=None)
                lastStat.orelse = elseIf
                lastStat = elseIf
        return _setMetadata(ctx, mainIf)

    def visitElseIfStat(self, ctx):
        # 'elseif' exp 'then' block
        return [
            self.visit(ctx.children[1]),
            self.visit(ctx.children[3]).body]

    def visitElseStat(self, ctx):
        # 'else' block
        return self.visit(ctx.children[1]).body

    def visitLabel(self, ctx):
        return _setMetadata(ctx, Label(id=self.visit(ctx.children[1]).id))

    def visitGoto(self, ctx):
        return _setMetadata(ctx, Goto(label=self.visit(ctx.children[1]).id))

    def visitBreakStat(self, ctx):
        return _setMetadata(ctx, Break())

    '''
    Visiting expressions.
    '''
    '''
    Types and values
    '''
    def visitNil(self, ctx):
        return _setMetadata(ctx, Nil())

    def visitTrue(self, ctx):
        return _setMetadata(ctx, TrueExpr())

    def visitFalse(self, ctx):
        return _setMetadata(ctx, FalseExpr())

    def visitNumber(self, ctx):
        # using python number eval to parse lua number:
        number = ast.literal_eval(ctx.children[0].getText())
        return _setMetadata(ctx, Number(number))

    def visitString(self, ctx):
        luaStr = ctx.children[0].getText()
        p = re.compile('^\[=+\[(.*)\]=+\]') # nested quote pattern
        # try remove double quote:
        if luaStr.startswith('"') and luaStr.endswith('"'):
            luaStr = luaStr[1:-1]
        # try remove single quote:
        elif luaStr.startswith("'") and luaStr.endswith("'"):
            luaStr = luaStr[1:-1]
        # try remove double square bracket:
        elif luaStr.startswith("[[") and luaStr.endswith("]]"):
            luaStr = luaStr[2:-2]
        # nested quote
        elif p.match(luaStr):
            luaStr = p.search(luaStr).group(1)
        return _setMetadata(ctx, String(luaStr))

    def _visitName(self, ctx):
        return _setMetadata(ctx, Name(ctx.children[0].getText()))

    def visitArgs(self, ctx):
        return self.visitChildren(ctx, mergeList=True)

    def _visitVar(self, ctx):
        # : (name | '(' exp ')' varSuffix) varSuffix*
        # if name varSuffix*
        if len(ctx.children)>1 and isinstance(ctx.children[1], LuaParser.VarSuffixContext):
            child = Index(value=self.visit(ctx.children[0]), idx=self.visit(ctx.children[1]))
            for i in range(2, len(ctx.children)):
                root = Index(value=child, idx=self.visit(ctx.children[i]))
                child = root
            print(toPrettyStr(child))
            return _setMetadata(ctx, child)
        else:
            return self.visitChildren(ctx)

    '''
    Visiting arithmetic operator expressions
    '''
    def visitOpAdd(self, ctx):
        return _setMetadata(ctx, AddOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpSub(self, ctx):
        return _setMetadata(ctx, SubOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpMult(self, ctx):
        return _setMetadata(ctx, MultOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpFloatDiv(self, ctx):
        return _setMetadata(ctx, FloatDivOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpFloorDiv(self, ctx):
        return _setMetadata(ctx, FloorDivOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpMod(self, ctx):
        return _setMetadata(ctx, ModOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpExpo(self, ctx):
        return _setMetadata(ctx, ExpoOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitOpMin(self, ctx):
        return _setMetadata(ctx, NegOp(self.visitChildren(ctx)))

    '''
    Relational Operators
    '''
    def visitRelOpLess(self, ctx):
        return _setMetadata(ctx, LessThanOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitRelOpGreater(self, ctx):
        return _setMetadata(ctx, GreaterThanOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitRelOpLessEq(self, ctx):
        return _setMetadata(ctx, LessOrEqThanOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitRelOpGreaterEq(self, ctx):
        return _setMetadata(ctx, GreaterOrEqThanOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitRelOpNotEq(self, ctx):
        return _setMetadata(ctx, NotEqToOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitRelOpEq(self, ctx):
        return _setMetadata(ctx, EqToOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))


    '''
    3.4.2 – Bitwise Operators
    '''
    def visitBitOpAnd(self, ctx):
        return _setMetadata(ctx, BAndOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitBitOpOr(self, ctx):
        return _setMetadata(ctx, BOrOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitBitOpXor(self, ctx):
        return _setMetadata(ctx, BXorOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitBitOpShiftR(self, ctx):
        return _setMetadata(ctx, BShiftROp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitBitOpShiftL(self, ctx):
        return _setMetadata(ctx, BShiftLOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    '''
    Unary Operators
    '''
    def visitUnOpMin(self, ctx):
        return _setMetadata(ctx, USubOp(operand=self.visit(ctx.children[1])))

    def visitUnOpBitNot(self, ctx):
        return _setMetadata(ctx, UBNotOp(operand=self.visit(ctx.children[1])))

    def visitUnOpNot(self, ctx):
        return _setMetadata(ctx, ULNotOp(self.visitChildren(ctx)))

    '''
    3.4.5 – Logical Operators
    '''
    def visitLoOpAnd(self, ctx):
        return _setMetadata(ctx, AndLoOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    def visitLoOpOr(self, ctx):
        return _setMetadata(ctx, OrLoOp(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.6 – Concatenation                                                   '''
    ''' ----------------------------------------------------------------------- '''
    def visitConcat(self, ctx):
        return _setMetadata(ctx, Concat(
            left=self.visit(ctx.children[0]), \
            right=self.visit(ctx.children[2])))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.7 – The Length Operator                                             '''
    ''' ----------------------------------------------------------------------- '''
    def visitUnOpLength(self, ctx):
        return _setMetadata(ctx, ULengthOP(operand=self.visit(ctx.children[1])))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.9 – Table Constructors                                              '''
    ''' ----------------------------------------------------------------------- '''
    def visitdTableconstructor(self, ctx):
        # table      : '{' (field (fieldsep field)* fieldsep?)? '}'
        # field      : '[' tableKey ']' '=' tableValue | tableKey '=' tableValue | tableValue
        # tableKey   : exp | name
        # tableValue : exp
        keys    = []
        values  = []
        index   = 1 # lua array start index
        for field in ctx.children:
            if isinstance(field, LuaParser.FieldContext):
                hasKey = False
                for tblElem in field.children:
                    if isinstance(tblElem, LuaParser.TableKeyContext):
                        keys.append(self.visitChildren(tblElem))
                        hasKey = True
                    elif isinstance(tblElem, LuaParser.TableValueContext):
                        values.append(self.visitChildren(tblElem))
                # if no index found, create an integer key:
                if not hasKey:
                    keys.append(Number(index))
                    index += 1
        return _setMetadata(ctx, Table(keys, values))

    ''' ----------------------------------------------------------------------- '''
    ''' 3.4.11 – Function Definitions                                           '''
    ''' ----------------------------------------------------------------------- '''
    def visitFunctiondef(self, ctx):
        # 'function' funcbody
        argsBlock = self.visit(ctx.children[1])
        return _setMetadata(ctx, Function(name='', args=argsBlock[0], body=argsBlock[1].body))

    def visitFuncbody(self, ctx):
        # '(' parlist? ')' block 'end'
        if isinstance(ctx.children[1], LuaParser.ParlistContext):
            nodes = [_listify(self.visit(ctx.children[1])),
                     self.visit(ctx.children[3])]
        else:
            nodes = [[],self.visit(ctx.children[2])]
        return nodes

    def visitParlist(self, ctx):
        return self.visitChildren(ctx, True)

    def visitFunc(self, ctx):
        # 'function' funcname funcbody
        name      = self.visit(ctx.children[1])
        argsBlock = self.visit(ctx.children[2])

        if isinstance(name, Name):
            return _setMetadata(ctx, Function(name=name.id, args=argsBlock[0], body=argsBlock[1].body))
        else:
            return _setMetadata(ctx, Function(name=name, args=argsBlock[0], body=argsBlock[1].body))

    def visitLocalfunc(self, ctx):
        # 'local' 'function' name funcbody
        name      = self.visit(ctx.children[2])
        argsBlock = self.visit(ctx.children[3])
        return _setMetadata(ctx, LocalFunction(name=name.id, args=argsBlock[0], body=argsBlock[1].body))

    def visitRetstat(self, ctx):
        # RETURN explist? SEMI_COLON?
        return _setMetadata(ctx, Return(_listify(self.visitChildren(ctx))))

    def visitFuncname(self, ctx):
        # name ('.' name)* (':' name)?
        if len(ctx.children)>2:
            child = Index(value=self.visit(ctx.children[0]), idx=self.visit(ctx.children[2]).id)

            for i in range(3, len(ctx.children)):
                if isinstance(ctx.children[i], LuaParser.NameContext):
                    root = Index(value=child, idx=self.visit(ctx.children[i]).id)
                    child = root
            return _setMetadata(ctx, child)
        else:
            return self.visitChildren(ctx)


    ''' ----------------------------------------------------------------------- '''
    ''' Comments                                                                '''
    ''' ----------------------------------------------------------------------- '''
    def visitComment_rule(self, ctx):
        comment = self.visitString(ctx).s
        if comment.startswith('--'):
            comment = comment[2:]
        return _setMetadata(ctx, Comment(comment.strip(' \t\n\r')))
"""

class ASTVisitor():
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

class ASTRecursiveVisitor():
    def visit(self, node):
        if isinstance(node, Node):
            # call enter node method
            # if no visitor method found for this arg type,
            # search in parent arg type:
            parentType = node.__class__
            while parentType != object:
                name = 'enter_' + node.__class__.__name__
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
                name = 'exit_' + node.__class__.__name__
                visitor = getattr(self, name, None)
                if visitor:
                    visitor(node)
                    break
                else:
                    parentType = parentType.__bases__[0]
        elif isinstance(node, list):
            for n in node:
                self.visit(n)

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