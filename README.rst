py-lua-parser
===============================================================================

A Lua parser and AST builder written in Python.

Installation:
------------------------------------------------------------------------------
The package can be installed through `pip`:

    python3.6 -m pip install .

Quickstart
==============================================================================

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
    print(ast.toPrettyStr(tree))

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

Working on tokens, modifying source code
------------------------------------------------------------------------------

Working directly on tokens is a convenient way to modify source code:

.. code-block:: python

    from luaparser import asttokens

    src = "local a = 1"

    atokens = asttokens.parse(src)
    for token in atokens.types(asttokens.Tokens.NAME):
        token.value.text = 'foo'

    print(atokens.toSource())

Will render:

.. code-block::

    local foo = 1

You can also work on both ast and tokens. In fact, you can retrieve and edit all tokens associated to a specific AST node.

The following example show how to automatically modify last argument in function call:

.. code-block:: python

    from luaparser import ast

    src = """\
    print('foo')
    process(1, 2, 3)
    """

    class CallVisitor(ast.ASTVisitor):
        def visit_Call(self, node):
            print('Call:', node.func.id)
            print('Args:', node.args.edit().toSource())
            print('Full line: ', node.edit().toSource())
            node.args.edit().last().text = 'replaced'

    tree = ast.parse(src)
    CallVisitor().visit(tree)

    print(tree.edit().toSource())


Output is:

.. code-block::

    Call: print
    Args: 'foo'
    Full line:  print('foo')

    Call: process
    Args: 1, 2, 3
    Full line:
    process(1, 2, 3)

    print(replaced)
    process(1, 2, replaced)
