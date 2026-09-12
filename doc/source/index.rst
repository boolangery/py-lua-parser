###############################################################################
py-lua-parser
###############################################################################

A Lua parser and AST builder written in Python, usable both as a library and as
a command line tool. It reads Lua 5.1 to 5.5 source and gives back a tree of
typed nodes that you can walk, rewrite and render back to Lua.

.. code-block:: python

    from luaparser import ast

    tree = ast.parse("local x = 1 + 2")
    print(ast.to_lua_source(tree))


Installation
===============================================================================

.. code-block:: bash

    $ python3 -m pip install luaparser

This installs the library and the ``luaparser`` shell command. Python 3.10 or
later is required.


Supported Lua versions
===============================================================================

==================  =============================  ===================
Lua source version  Recommended ``luaparser``      Grammar support
==================  =============================  ===================
Lua 5.1 -- 5.3      ``luaparser>=3.2.1``           Supported
Lua 5.4             ``luaparser>=3.3.0``           Supported
Lua 5.5             Unreleased (after 4.2.0)       Supported
==================  =============================  ===================

Grammar support is backward compatible, so a recent release parses source
written for an older Lua version. Note that ``luaparser`` does not enforce
every compile-time restriction of a given Lua version, so a successful parse is
not a substitute for checking the source with that version's ``luac``.


Where to go next
===============================================================================

* :doc:`parsing` -- turning source into a tree, and what a node carries.
* :doc:`visitors` -- walking a tree, and rewriting it in place.
* :doc:`rendering` -- going back to Lua source, or to a debug representation.
* :doc:`cli` -- the ``luaparser`` command.
* :doc:`astnodes` -- reference for every node type.
* :doc:`api` -- reference for the ``ast`` and ``printers`` modules.

.. toctree::
   :maxdepth: 2
   :hidden:

   parsing
   visitors
   rendering
   cli
   astnodes
   api


Indices and tables
===============================================================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
