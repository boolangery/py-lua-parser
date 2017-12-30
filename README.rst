py-lua-parser
===============================================================================

A Lua parser and AST builder written in Python.

Installation:
------------------------------------------------------------------------------
The package can be installed through `pip`:

    python3.6 -m pip install .

Quickstart
------------------------------------------------------------------------------

Minimal exemple:

.. code-block:: python

    from luaparser import Parser, Printer

    source = """
    -- sample program
    print('Hello world !')
    """

    ast = Parser().srcToAST(source)
    Printer.pprint(ast, style=Printer.Style.PYTHON, indent=True)

will display:

.. code-block::

    Chunk: {} 1 key
      body: {} 1 key
        Block: {} 1 key
          body: [] 2 items
            0: {} 1 key
              Comment: {} 1 key
                s: "sample program"
            1: {} 1 key
              Call: {} 2 keys
                func: {} 1 key
                  Name: {} 1 key
                    id: "print"
                args: [] 1 item
                  0: {} 1 key
                    String: {} 1 key
                      s: "Hello world !"
