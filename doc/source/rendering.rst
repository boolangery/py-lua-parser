###############################################################################
Rendering
###############################################################################

A tree can be rendered back to Lua, or to one of three debug representations.
All of them are thin wrappers over the visitors in
:mod:`luaparser.printers`.

=====================================  ==========================
Function                               Output
=====================================  ==========================
:func:`~luaparser.ast.to_lua_source`   Lua source
:func:`~luaparser.ast.to_pretty_str`   Indented tree, for reading
:func:`~luaparser.ast.to_xml_str`      XML
:func:`~luaparser.ast.to_pretty_json`  JSON
=====================================  ==========================


Back to Lua
===============================================================================

.. code-block:: python

    from luaparser import ast

    tree = ast.parse("local function f(a) return a * 2 end")
    print(ast.to_lua_source(tree))

.. code-block:: lua

    local function f(a)
        return a * 2
    end

The ``indent`` argument sets the width, defaulting to 4:

.. code-block:: python

    ast.to_lua_source(tree, indent=2)


What the renderer guarantees
-------------------------------------------------------------------------------

``to_lua_source`` is a pretty-printer, not a byte-for-byte reproduction of the
file you parsed. It promises that:

* the code keeps its meaning;
* every comment survives;
* parsing the output gives back the same tree;
* rendering that tree again gives the exact same text.

These properties are tested on the official Lua 5.5 test suite -- 34 real-world
files -- on every commit.

It does *not* promise to preserve layout. The output is re-indented, blank
lines between statements are dropped, and a comment may end up attached to a
neighbouring node. Round-tripping a file you care about will therefore produce
a diff, even though the two versions behave identically.

Comments are re-emitted in place, including trailing ones:

.. code-block:: python

    print(ast.to_lua_source(ast.parse("-- hello\nlocal a = 1 -- trailing")))

.. code-block:: lua

    -- hello
    local a = 1 -- trailing


Rendering a tree you built yourself
-------------------------------------------------------------------------------

Nothing requires the tree to have come from :func:`~luaparser.ast.parse`. Nodes
constructed by hand render the same way, which is how you generate Lua rather
than merely reformat it:

.. code-block:: python

    from luaparser import ast
    from luaparser.astnodes import *

    tree = Chunk(Block([
        Forin(
            targets=[Name('k'), Name('v')],
            iter=[Invoke(source=Name('bar'), func=Name('foo'), args=[Number(42)])],
            body=Block([
                Call(func=Name('print'), args=[Name('k'), Name('v')])
            ]),
        )
    ]))

    print(ast.to_lua_source(tree))

.. code-block:: lua

    for k, v in bar:foo(42) do
        print(k, v)
    end


Inspecting a tree
===============================================================================

:func:`~luaparser.ast.to_pretty_str` renders the tree itself rather than the
code, which is the fastest way to find out what a piece of Lua actually parsed
to:

.. code-block:: python

    print(ast.to_pretty_str(ast.parse("local a = 1")))

.. code-block:: text

    Chunk: {} 2 keys
      body: {} 2 keys
        Block: {} 2 keys
          body: [] 1 item
            0: {} 1 key
              LocalAssign: {} 5 keys
                wrapped: False
                targets: [] 1 item
                  0: {} 1 key
                    Name: {} 4 keys
                      wrapped: False
                      id: 'a'
                values: [] 1 item
                  0: {} 1 key
                    Number: {} 3 keys
                      wrapped: False
                      n: 1

It takes an ``indent`` argument too, defaulting to 2.

:func:`~luaparser.ast.to_xml_str` and :func:`~luaparser.ast.to_pretty_json`
produce the same information as XML and JSON, for feeding another tool. Both
are what the :doc:`cli` emits with ``--xml`` and by default.
