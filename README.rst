py-lua-parser (Work in progress)
================================

A Lua parser and AST builder written in Python.


Usage
=====

.. code-block:: python
    from luaparser import Parser
    from luaparser import Printer


    parser = Parser()

    ast = parser.fileToAST('local var = 42')

    print('** Default AST ***')
    print(Printer.toStr(ast, Printer.Style.DEFAULT))

    print('** Metalua AST ***')
    print(Printer.toStr(ast, Printer.Style.METALUA))


To generate parser
------------------

http://www.antlr.org/download/antlr-4.7-complete.jar

java -Xmx500M -cp ../antlr-4.7-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 -visitor Lua.g4

https://github.com/antlr/antlr4/blob/master/doc/python-target.md

python3.6 parser_v2.py ../tests/dog.lua
python3.6 -m pip install --upgrade ../ --user && python3.6 parser_v2.py ../tests/dog.lua
