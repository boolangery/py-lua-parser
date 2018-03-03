import ast
import re
from antlr4 import *
from luaparser.parser.LuaLexer import LuaLexer
from luaparser.parser.LuaVisitor import LuaVisitor
from luaparser.astnodes import *
from luaparser.asttokens import Tokens
from luaparser.parser.LuaParser import LuaParser
from luaparser import printers
from luaparser.utils.visitor import *
from antlr4.error.ErrorListener import ErrorListener
import llist

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

    visitor = WalkVisitor()
    visitor.visit(root)
    for n in visitor.nodes:
        yield n

def toPrettyStr(tree, indent=2):
    return printers.PythonStyleVisitor(indent).visit(tree)

def toXmlStr(tree):
    visitor = printers.HTMLStyleVisitor()
    return visitor.get_xml_string(tree)

def _listify(obj):
    if not isinstance(obj, NodeList):
        l = NodeList()
        l.append(obj)
        return l
    else:
        return obj

class ParseTreeVisitor(LuaVisitor):
    def _initNode(self, ctx, node, isBlock=False):
        if isinstance(ctx, TerminalNode):
            return self._initNodeFromIndex(ctx.symbol.tokenIndex, ctx.symbol.tokenIndex, node, isBlock)
        else:
            return self._initNodeFromIndex(ctx.start.tokenIndex, ctx.stop.tokenIndex, node, isBlock)

    def _initNodeFromIndex(self, start, stop, node, isBlock=False):
        # include hidden tokens:
        hiddenTokens = self._tokenStream.getHiddenTokensToLeft(start)
        if hiddenTokens:
            start -= len(hiddenTokens)

        if isBlock:
            hiddenTokens = self._tokenStream.getHiddenTokensToRight(stop)
            if hiddenTokens:
                stop += len(hiddenTokens)

        return node.initTokens(self._dllAll, start, stop)

    def getTokenNodes(self, start, stop):
        subset = []
        if stop >= len(self._dllAll):
            stop = len(self._dllAll) - 1
        for i in range(start, stop):
            node = self._dllAll.nodeat(i)
            subset.append(node)
        return subset

    def visitChildren(self, ctx, mergeList=False):
        if ctx.children:
            return self.visitChildrenList(ctx.children, mergeList)
        else:
            return NodeList()

    def visitChildrenList(self, children, mergeList=False):
        nodes = NodeList()
        for child in children:
            node = self.visit(child)
            if node != None:
                if mergeList and isinstance(node, NodeList):
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
            return NodeList()

    ''' Visiting root nodes.
    '''
    def visitChunk(self, ctx):
        # create a double linked list of all token
        # to be shared across all nodes:
        self._tokenStream = ctx.parser._input
        self._dllAll = llist.dllist()
        for token in ctx.parser._input.tokens:
            self._dllAll.append(token)

        node = self._initNode(ctx, Chunk(self.visit(ctx.children[0])))

        # add all tokens to chunk (include comments)
        node.start = 0
        node.stop = ctx.stop.tokenIndex

        return node

    def visitBlock(self, ctx):
        """block
        : stat* ret_stat?"""
        body = self._initNode(ctx, _listify(self.visitChildren(ctx)), True)
        return self._initNode(ctx, Block(body), True)

    def visitStat(self, ctx):
        return self.visit(ctx.children[0])

    ''' Statements '''
    def visitAssignment(self, ctx):
        # var_list ASSIGN expr_list
        return self._initNode(ctx, Assign(
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
                return self._initNode(ctx, LocalAssign(
                    targets=_listify(self.visit(ctx.children[1])),
                    values=_listify(self.visit(ctx.children[3]))))
            # LOCAL name_list
            else:
                return self._initNode(ctx, LocalAssign(
                    targets=_listify(self.visit(ctx.children[1])),
                    values=NodeList()))

        # LOCAL FUNCTION NAME func_body
        else:
            name     = self.visit(ctx.children[2])
            funcBody = self.visit(ctx.children[3])
            return self._initNode(ctx, LocalFunction(name=name, args=funcBody[0], body=funcBody[1]))

    def visitFunc_body(self, ctx):
        """func_body
        : OPAR param_list CPAR block END"""
        params = self._initNode(ctx.children[1], self.visit(ctx.children[1]))

        body = self.visit(ctx.children[3])

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
                self._initNode(ctx.children[i], tail)
                if isinstance(tail, Index):
                    tail.value = root
                elif isinstance(tail, Invoke):
                    tail.source = root
                elif isinstance(tail, Call):
                    tail.func = root
                else:
                    tail = Call(
                        func=root,
                        args=self._initNode(ctx.children[i], _listify(tail)))

                # extend with child tokens
                self._initNode(ctx.children[i], tail)
                tail.start = root.start

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
        return self._initNode(ctx, Index(
            value=None, # to set in parent
            idx=self.visit(ctx.children[1])))

    def visitTail_brack_index(self, ctx):
        """OBRACK expr CBRACK"""
        return self._initNode(ctx, Index(
            value=None,  # to set in parent
            idx=self.visit(ctx.children[1])))

    def visitTail_invoke(self, ctx):
        """COL NAME OPAR expr_list? CPAR"""
        args = _listify(self.visit(ctx.children[3]) or NodeList())
        if len(ctx.children) > 4: self._initNode(ctx.children[3], args)
        return self._initNode(ctx, Invoke(
            source=None,  # to set in parent
            func=self.visit(ctx.children[1]),
            args=args))

    def visitTail_invoke_table(self, ctx):
        """COL NAME table_constructor"""
        args = self._initNode(ctx.children[2], _listify(self.visit(ctx.children[2])))
        return self._initNode(ctx, Invoke(
            source=None,  # to set in parent
            func=self.visit(ctx.children[1]),
            args=args))

    def visitTail_invoke_str(self, ctx):
        """COL NAME STRING"""
        args = self._initNode(ctx.children[2], _listify(self.visit(ctx.children[2])))
        return self._initNode(ctx, Invoke(
            source=None,  # to set in parent
            func=self.visit(ctx.children[1]),
            args=args))

    def visitTail_call(self, ctx):
        """OPAR expr_list? CPAR"""
        if len(ctx.children) > 2:
            args = self._initNode(
                ctx.children[1],
                _listify(self.visit(ctx.children[1])))
        else:
            args = NodeList()

        return self._initNode(ctx, Call(
            func=None,  # to set in parent
            args=args))

    def visitTail_table(self, ctx):
        """table_constructor"""
        return self.visit(ctx.children[0])

    def visitTail_string(self, ctx):
        """STRING"""
        return self.visit(ctx.children[0])

    def visitTerminal(self, ctx):
        def NilHandler(ctx): return self._initNode(ctx, Nil())
        def NameHandler(ctx): return self._initNode(ctx, Name(ctx.getText()))
        def TrueHandler(ctx):return self._initNode(ctx, TrueExpr())
        def FalseHandler(ctx):return self._initNode(ctx, FalseExpr())
        def NumberHandler(ctx):
            # using python number eval to parse lua number
            try:
                number = ast.literal_eval(ctx.getText())
            except:
                # exception occurs with leading zero number: 002
                number = float(ctx.getText())
            return self._initNode(ctx, Number(number))
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
            return self._initNode(ctx, String(luaStr))
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
                root  = self._initNode(ctx, nodeOnToken[ctx.children[i].symbol.type](
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
                return self._initNode(ctx, UMinusOp(self.visit(ctx.children[1])))
            elif ctx.children[0].symbol.type == Tokens.LENGTH.value:
                return self._initNode(ctx, ULengthOP(self.visit(ctx.children[1])))
            elif ctx.children[0].symbol.type == Tokens.NOT.value:
                return self._initNode(ctx, ULNotOp(self.visit(ctx.children[1])))
            else:
                return self._initNode(ctx, UBNotOp(self.visit(ctx.children[1])))
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
            keys   = NodeList()
            values = NodeList()
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
            return self._initNode(ctx, Table(keys, values))
        else:
            return self._initNode(ctx, Table(NodeList(), NodeList()))

    def visitField_list(self, ctx):
        """field_list
        : field (field_sep field)* field_sep?"""
        fields = NodeList()
        for child in ctx.children:
            if isinstance(child, LuaParser.FieldContext):
                fields.append(self.visit(child))
        return fields

    def visitField(self, ctx):
        """field
        : OBRACK expr CBRACK ASSIGN expr
        | NAME ASSIGN expr
        | expr"""
        length = len(ctx.children)
        # OBRACK expr CBRACK ASSIGN expr
        if length > 3:
            key = self.visit(ctx.children[1])
            # include OBRACK and CBRACK in token list
            self._initNodeFromIndex(ctx.children[0].symbol.tokenIndex, ctx.children[2].symbol.tokenIndex, key)
            value = self.visit(ctx.children[4])
        # NAME ASSIGN expr
        elif length > 2:
            key = self.visit(ctx.children[0])
            value = self.visit(ctx.children[2])
        # expr
        else:
            key = None
            value = self.visit(ctx.children[0])
        return (key, value)


    def visitFunction(self, ctx):
        """function
        : FUNCTION names (COL NAME func_body | func_body)"""
        names = self.visit(ctx.children[1])
        # FUNCTION names COL NAME func_body
        if len(ctx.children) > 3:
            funcBody = self.visit(ctx.children[4])
            return self._initNode(ctx, Method(
                source=names,
                name=self.visit(ctx.children[3]),
                args=funcBody[0],
                body=funcBody[1]))
        # FUNCTION names func_body
        else:
            funcBody = self.visit(ctx.children[2])
            return self._initNode(ctx, Function(
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
            return self._initNode(ctx, child)
        else:
            return self.visitChildren(ctx)


    def visitFunction_literal(self, ctx):
        """function_literal
        : FUNCTION func_body"""
        funcBody = self.visit(ctx.children[1])
        return self._initNode(ctx, AnonymousFunction(
            args=funcBody[0],
            body=funcBody[1]))

    def visitDo_block(self, ctx):
        """do_block
        : DO block END"""
        body = self.visit(ctx.children[1])
        return self._initNode(ctx, Do(body))

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
            if len(ctx.children) > 7:
                step = self.visit(ctx.children[7])

            return self._initNode(ctx, Fornum(
                target=self.visit(ctx.children[1]),
                start=start,
                stop=stop,
                step=step,
                body=self.visit(ctx.children[-1]).body)) # visitDo_block
        # FOR name_list IN expr_list do_block
        else:
            return self._initNode(ctx, Forin(
                body=self.visit(ctx.children[4]).body,
                iter=self.visit(ctx.children[3]),
                targets=_listify(self.visit(ctx.children[1]))))

    def visitWhile_stat(self, ctx):
        """while_stat
        : WHILE expr do_block"""
        return self._initNode(ctx, While(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[2]).body))

    def visitRepeat_stat(self, ctx):
        """repeat_stat
        : REPEAT block UNTIL expr"""
        return self._initNode(ctx, Repeat(
            body=self.visit(ctx.children[1]),
            test=self.visit(ctx.children[3])))

    def visitIf_stat(self, ctx):
        """if_stat
        : IF expr THEN block elseif_stat* else_stat? END"""
        mainIf = If(
            test=self.visit(ctx.children[1]),
            body=self.visit(ctx.children[3]),
            orelse=None)
        lastStat = mainIf

        for node in ctx.children[4:-1]:
            if isinstance(node, LuaParser.Else_statContext):
                lastStat.orelse = self.visit(node)
            else:
                elseIfNodes = self.visit(node)
                elseIf = self._initNode(node, ElseIf(test=elseIfNodes[0], body=elseIfNodes[1], orelse=None))
                lastStat.orelse = elseIf
                lastStat = elseIf
        return self._initNode(ctx, mainIf)

    def visitElseif_stat(self, ctx):
        """elseif_stat
        : ELSEIF expr THEN block"""
        return [
            self.visit(ctx.children[1]),
            self.visit(ctx.children[3])]

    def visitElse_stat(self, ctx):
        """else_stat
        : ELSE block"""
        return self.visit(ctx.children[1])

    def visitLabel(self, ctx):
        """label
        : COLCOL NAME COLCOL"""
        return self._initNode(ctx, Label(id=self.visit(ctx.children[1])))

    def visitGoto_stat(self, ctx):
        return self._initNode(ctx, Goto(label=self.visit(ctx.children[1])))

    def visitRet_stat(self, ctx):
        """ret_stat
        : RETURN expr_list? SEMCOL?"""
        exp_list = _listify(self.visitChildren(ctx))
        if len(exp_list) > 0:
            self._initNode(ctx.children[1], exp_list)
        return self._initNode(ctx, Return(exp_list))


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
