import sys
from luaparser import Parser
from luaparser import Printer


def main(argv):
    parser = Parser()

    parseTree = parser.fileToParseTree(argv[1])
    ast = parser.fileToAST(argv[1])

    print('*** Parse Tree ***')
    print(str(parseTree))

    print('** Default AST ***')
    print(Printer.toStr(ast, Printer.Style.DEFAULT))

    print('** Metalua AST ***')
    print(Printer.toStr(ast, Printer.Style.METALUA))


if __name__ == '__main__':
    main(sys.argv)

