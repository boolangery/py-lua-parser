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
              LocalFunctionDef: {} 3 keys
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
        token.text = 'foo'

    print(atokens.toSource())

Will render:

.. code-block::

    local foo = 1

You can also work on both ast and tokens:

.. code-block:: python

    import textwrap
    from luaparser import ast
    from luaparser import asttokens
    from luaparser import astnodes

    src = textwrap.dedent("""
        local a = 1
        local b, c = '11'""")

    tree = ast.parse(src)
    atokens = asttokens.parse(src)

    for node in ast.walk(tree):
        if isinstance(node, LocalAssign):
            tokens = atokens.fromAST(node)
            for name in tokens.types(asttokens.Tokens.NAME):
                name.text = '_' + name.text

Will render:

.. code-block::

    local _a = 1
    local _b, _c = '11'
