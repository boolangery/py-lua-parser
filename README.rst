py-lua-parser
===============================================================================

.. image:: https://travis-ci.org/boolangery/py-lua-parser.svg?branch=master
    :target: https://travis-ci.org/boolangery/py-lua-parser
.. image:: https://img.shields.io/pypi/v/luaparser.svg
    :target: https://pypi.python.org/pypi/luaparser/
.. image:: https://img.shields.io/pypi/pyversions/luaparser.svg
    :target: https://pypi.python.org/pypi/luaparser/

A Lua parser and AST builder written in Python.

It's both a development library and a command line tool.


Installation:
------------------------------------------------------------------------------

The package can be installed through `pip`:

.. code-block::

    $ python3.6 -m pip install luaparser

It will install the shell command 'luaparser'.


Options
------------------------------------------------------------------------------

These are the command-line flags:

Usage: luaparser [options] filename

.. code-block::

    CLI Options:
      --version                     Show program's version number and exit
      -h, --help                    Show this help message and exit
      -s, --source                  Source passed in a string
      -x, --xml                     Set output format to xml
      -o, --output                  Write output to file


Quickstart
==============================================================================

Node structure
------------------------------------------------------------------------------

Each node contains the following data:

.. code-block:: python

	class Node:
		"""Base class for AST node."""
		comments: Comments
		first_token: Optional[Token]
		last_token: Optional[Token]
		start_char: Optional[int]
		stop_char: Optional[int]
		line: Optional[int]


Working on AST tree
------------------------------------------------------------------------------

Minimal exemple:

.. code-block:: python

    from luaparser import ast

    src = """
        local function sayHello()
          print('hello world !')
        end
        sayHello()
        """

    tree = ast.parse(src)
    print(ast.to_pretty_str(tree))

will display:

.. code-block::

    Chunk: {} 1 key
      body: {} 1 key
        Block: {} 1 key
          body: [] 2 items
            0: {} 1 key
              LocalFunction: {} 3 keys
                name: {} 1 key
                  Name: {} 1 key
                    id: "sayHello"
                args: [] 0 item
                body: [] 1 item
                  0: {} 1 key
                    Call: {} 2 keys
                      func: {} 1 key
                        Name: {} 1 key
                          id: "print"
                      args: [] 1 item
                        0: {} 1 key
                          String: {} 1 key
                            s: "hello world !"
            1: {} 1 key
              Call: {} 2 keys
                func: {} 1 key
                  Name: {} 1 key
                    id: "sayHello"
                args: [] 0 item


You can run through the list of all the nodes in the tree using ast.walk(tree):

.. code-block:: python

    from luaparser import ast
    from luaparser import astnodes

    tree = ast.parse("local foo = 'bar'")

    for node in ast.walk(tree):
        if isinstance(node, astnodes.Name):
            process(node)


Alternatively, you can use a node visitor:

.. code-block:: python

    from luaparser import ast
    from luaparser import astnodes

    src = "local a = 42"

    class NumberVisitor(ast.ASTVisitor):
        def visit_Number(self, node):
            print('Number value = ' + str(node.n))

    tree = ast.parse(src)
    NumberVisitor().visit(tree)


Rendering lua code
------------------------------------------------------------------------------

.. warning:: Experimental feature

.. code-block:: python

    exp = Chunk(Block([
        Forin(
            targets=[Name('k'), Name('v')],
            iter=[
                Invoke(
                    source=Name('bar'),
                    func=Name('foo'),
                    args=[Number(42)]
                )
            ],
            body=Block([
                Call(func=Name('print'), args=[Name('k'), Name('v')])
            ]),

        )
    ]))

    print(ast.to_lua_source(exp))


Will render:

.. code-block:: lua

    for k, v in bar:foo(42) do
        print(k, v)
    end


Command line
==============================================================================

Given:

.. code-block:: lua

    local function log(msg)
      print(msg)
    end

    log("hello world !")


.. code-block:: bash

    $ luaparser source.lua


Will output:

.. code-block:: json

    {
        "Chunk": {
            "body": {
                "Block": {
                    "body": [
                        {
                            "LocalFunction": {
                                "name": {
                                    "Name": {
                                        "id": "log"
                                    }
                                },
                                "args": [
                                    {
                                        "Name": {
                                            "id": "msg"
                                        }
                                    }
                                ],
                                "body": {
                                    "Block": {
                                        "body": [
                                            {
                                                "Call": {
                                                    "func": {
                                                        "Name": {
                                                            "id": "print"
                                                        }
                                                    },
                                                    "args": [
                                                        {
                                                            "Name": {
                                                                "id": "msg"
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        },
                        {
                            "Call": {
                                "func": {
                                    "Name": {
                                        "id": "log"
                                    }
                                },
                                "args": [
                                    {
                                        "String": {
                                            "s": "hello world !"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }
