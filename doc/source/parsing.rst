###############################################################################
Parsing
###############################################################################

From source to a tree
===============================================================================

:func:`luaparser.ast.parse` takes Lua source and returns a
:class:`~luaparser.astnodes.Chunk`, the root of every tree:

.. code-block:: python

    from luaparser import ast

    tree = ast.parse("local x = 1 + 2")

A ``Chunk`` holds a single :class:`~luaparser.astnodes.Block`, and a ``Block``
holds a list of statements:

.. code-block:: python

    tree.body            # the Block
    tree.body.body       # the list of statements
    tree.body.body[0]    # LocalAssign(targets=[Name('x')], values=[AddOp(...)])

Attributes are plain Python, so a tree can be inspected directly:

.. code-block:: python

    stat = ast.parse("local x = 1").body.body[0]

    [t.id for t in stat.targets]   # ['x']
    [v.n for v in stat.values]     # [1]


Syntax errors
===============================================================================

A source that does not parse raises
:class:`~luaparser.ast.SyntaxException`. The message carries the line and
column of the offending token:

.. code-block:: python

    from luaparser import ast

    try:
        ast.parse("local = ")
    except ast.SyntaxException as e:
        print(e)

.. code-block:: text

    syntax errors: line 1:6: no viable alternative at input 'local ='

Note that ``luaparser`` checks syntax only. It does not apply the semantic
restrictions a real Lua compiler adds on top of the grammar, so a tree you get
back is not guaranteed to be accepted by ``luac``.


What a node carries
===============================================================================

Every node derives from :class:`~luaparser.astnodes.Node` and, beyond its own
attributes, records where it came from:

.. code-block:: python

    class Node:
        comments: Comments
        first_token: Optional[Token]
        last_token: Optional[Token]
        start_char: Optional[int]
        stop_char: Optional[int]
        line: Optional[int]

``line``, ``start_char`` and ``stop_char`` locate the node in the original
source, which is what you need to report a diagnostic or to splice text back
into the file:

.. code-block:: python

    stat = ast.parse("local x = 1").body.body[0]

    stat.line         # 1
    stat.start_char   # 0
    stat.stop_char    # 10

``first_token`` and ``last_token`` expose the underlying ANTLR tokens, which is
mostly useful when you need the token index rather than a character offset.


Comments
===============================================================================

Comments are not statements; each one is attached to the ``comments`` list of a
nearby node. A comment is treated as *leading* the node that follows it, and a
comment with no node after it attaches to the enclosing
:class:`~luaparser.astnodes.Chunk`:

.. code-block:: python

    from luaparser import ast

    src = "-- leading\nlocal x = 1 -- trailing\n"

    for node in ast.walk(ast.parse(src)):
        if node.comments:
            print(type(node).__name__, [c.s for c in node.comments])

.. code-block:: text

    Chunk ['-- trailing']
    LocalAssign ['-- leading']

Because attachment is positional, reformatting a tree can move a comment from
one node to another. :doc:`rendering` keeps every comment, but does not promise
that it stays on the same node.


Working with tokens directly
===============================================================================

:func:`luaparser.ast.get_token_stream` returns the raw ANTLR
``CommonTokenStream`` for a source, bypassing tree construction. Use it when
you want lexical information -- whitespace, token indices, the hidden channel
-- that the AST deliberately does not keep.
