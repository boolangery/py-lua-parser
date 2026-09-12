###############################################################################
API reference
###############################################################################

For the node classes themselves, see :doc:`astnodes`.


ast module
===============================================================================

.. module:: luaparser.ast


Parsing
-------------------------------------------------------------------------------

.. autofunction:: luaparser.ast.parse

.. autofunction:: luaparser.ast.get_token_stream

.. autoclass:: luaparser.ast.SyntaxException
    :members:


Traversal
-------------------------------------------------------------------------------

.. autofunction:: luaparser.ast.walk

.. autoclass:: luaparser.ast.ASTVisitor
    :members:

.. autoclass:: luaparser.ast.ASTRecursiveVisitor
    :members:

.. autoclass:: luaparser.ast.ASTTransformer
    :members:


Rendering
-------------------------------------------------------------------------------

.. autofunction:: luaparser.ast.to_lua_source

.. autofunction:: luaparser.ast.to_pretty_str

.. autofunction:: luaparser.ast.to_xml_str

.. autofunction:: luaparser.ast.to_pretty_json


printers module
===============================================================================

These are the visitors behind the rendering functions above. Use them directly
when you need to subclass one or to hold on to a configured instance;
otherwise prefer the ``ast`` helpers.

.. autoclass:: luaparser.printers.LuaOutputVisitor
    :members: to_source

.. autoclass:: luaparser.printers.PythonStyleVisitor
    :members: visit

.. autoclass:: luaparser.printers.HTMLStyleVisitor
    :members: get_xml_string
