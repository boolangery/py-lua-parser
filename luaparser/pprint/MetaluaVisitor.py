from luaparser.astNodes import *
from luaparser.visitor import *


class MetaluaVisitor():
    def pprint_childs(self, node):
        """Pretty print node's children"""
        res = ''
        if len(node.childs)>0:
            for child in node.childs:
                res += self.visit(child) + ', '
            res = res[:-2]
        return res

    def pprint_childsWrap(self, node):
        """Pretty print node's children
            wrap each children with brackets"""
        res = ''
        if len(node.childs)>0:
            for child in node.childs:
                res += self.pprint_wrap(self.visit(child)) + ', '
            res = res[:-2]
        return res

    def pprint_wrap(self, obj):
        """Wrap a string with brackets"""
        return '{ ' + str(obj) + ' }'

    def pprint_fullNodeWW(self, node):
        """ Pretty print a node with full wrapping
            { `name{...} }
        """
        return '{ `' + node.name + self.pprint_wrap(self.pprint_childsWrap(node)) + ' }'

    def pprint_fullNodeW(self, node):
        """ Pretty print a node with no wrapping for children.
            { `name ... }
        """
        return '{ `' + node.name + self.pprint_wrap(self.pprint_childs(node)) + ' }'

    def pprint_fullNode(self, node):
        """ Pretty print a node with no wrapping .
            `name ...
        """
        return '`' + node.name + self.pprint_wrap(self.pprint_childs(node))

    def pprint_termNodeValue(self, node):
        if len(node.childs)>0:
            return  '`' + node.name + ' ' + self.pprint_childs(node)
        else:
            return  '`' + node.name

    def pprint_ignoreNode(self, node):
        return self.pprint_childs(node)

    @visitor(str)
    def visit(self, node):
        if node.startswith('"') and node.endswith('"'):
            node = node[1:-1]
        return '"' + str(node) + '"'

    @visitor(Node)
    def visit(self, node):
        return self.pprint_fullNodeWW(node)

    @visitor(Chunk)
    def visit(self, node):
        return self.pprint_ignoreNode(node)

    @visitor(Block)
    def visit(self, node):
        return self.pprint_ignoreNode(node)

    ''' Statements
    '''
    @visitor(CallStat)
    def visit(self, node):
        return self.pprint_fullNodeW(node)

    @visitor(InvokeStat)
    def visit(self, node):
        return self.pprint_fullNodeW(node)

    ''' Expression
    '''
    @visitor(IdExpr)
    def visit(self, node):
        return self.pprint_termNodeValue(node)

    @visitor(IndexExpr)
    def visit(self, node):
        return self.pprint_fullNode(node)

    @visitor(NumberExpr)
    def visit(self, node):
        return self.pprint_termNodeValue(node)

    @visitor(StringExpr)
    def visit(self, node):
        return self.pprint_termNodeValue(node)

    @visitor(TrueExpr)
    def visit(self, node):
        return self.pprint_termNodeValue(node)

    @visitor(FalseExpr)
    def visit(self, node):
        return self.pprint_termNodeValue(node)

    @visitor(ArgsExpr)
    def visit(self, node):
        return self.pprint_ignoreNode(node)

    @visitor(VarsExpr)
    def visit(self, node):
        return self.pprint_ignoreNode(node)

    @visitor(ExprsExpr)
    def visit(self, node):
        return self.pprint_ignoreNode(node)