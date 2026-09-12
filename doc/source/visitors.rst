###############################################################################
Walking and transforming
###############################################################################

There are four ways to traverse a tree, in increasing order of control:
:func:`~luaparser.ast.walk` for a flat iteration,
:class:`~luaparser.ast.ASTVisitor` for per-type callbacks,
:class:`~luaparser.ast.ASTRecursiveVisitor` when you need to know where a
subtree begins and ends, and :class:`~luaparser.ast.ASTTransformer` when you
want to rewrite nodes rather than only read them.


Iterating over every node
===============================================================================

:func:`luaparser.ast.walk` yields every node in the tree, so ordinary Python
control flow does the filtering:

.. code-block:: python

    from luaparser import ast
    from luaparser import astnodes

    tree = ast.parse("local foo = 'bar'")

    for node in ast.walk(tree):
        if isinstance(node, astnodes.Name):
            print(node.id)

The nodes above arrive in this order:

.. code-block:: text

    Chunk, Block, LocalAssign, Name, String

This is the right tool when you want to collect or count something. It gives
you no notion of nesting: a ``Name`` yielded by ``walk`` looks the same whether
it sat at the top level or ten blocks deep.


Reacting to one node type
===============================================================================

Subclass :class:`~luaparser.ast.ASTVisitor` and define a ``visit_<NodeType>``
method for each type you care about. Nodes with no matching method are simply
traversed:

.. code-block:: python

    from luaparser import ast

    class NumberVisitor(ast.ASTVisitor):
        def visit_Number(self, node):
            print('Number value = ' + str(node.n))

    NumberVisitor().visit(ast.parse("local a = 42"))

.. code-block:: text

    Number value = 42

The method name must match the node class name exactly --
``visit_LocalAssign``, ``visit_Forin``, ``visit_AnonymousFunction``. See
:doc:`astnodes` for the full list.


Tracking nesting with enter/exit
===============================================================================

:class:`~luaparser.ast.ASTRecursiveVisitor` calls ``enter_<NodeType>`` on the
way down and ``exit_<NodeType>`` on the way back up, which is what you need to
maintain a depth counter, a scope stack, or anything else with a lifetime:

.. code-block:: python

    from luaparser import ast

    class Depth(ast.ASTRecursiveVisitor):
        def __init__(self):
            self.depth = 0

        def enter_Function(self, node):
            self.depth += 1
            print(' ' * self.depth + 'enter ' + node.name.id)

        def exit_Function(self, node):
            print(' ' * self.depth + 'exit ' + node.name.id)
            self.depth -= 1

    Depth().visit(ast.parse("function a() end\nfunction b() end"))

.. code-block:: text

     enter a
     exit a
     enter b
     exit b

Unlike :class:`~luaparser.ast.ASTVisitor`, this visitor follows the class
hierarchy: if no handler matches the exact node type it looks for one on the
base classes. Defining ``enter_Node`` therefore catches everything, and
``enter_Statement`` or ``enter_Expression`` catches a whole family:

.. code-block:: python

    class All(ast.ASTRecursiveVisitor):
        def enter_Node(self, node):
            print(type(node).__name__)

    All().visit(ast.parse("x = 1"))

.. code-block:: text

    Chunk
    Block
    Assign
    Name
    Number

Only the most specific handler runs -- defining both ``enter_Number`` and
``enter_Node`` calls ``enter_Number`` for numbers, not both.


Rewriting a tree
===============================================================================

:class:`~luaparser.ast.ASTTransformer` is the only visitor that can change the
tree. A ``visit_<NodeType>`` method may return a replacement node; returning
``None`` or the node itself leaves it alone:

.. code-block:: python

    from luaparser import ast
    from luaparser.astnodes import Number

    class NumberDoubler(ast.ASTTransformer):
        def visit_Number(self, node):
            return Number(node.n * 2)

    tree = NumberDoubler().visit(ast.parse("x = 5 + 10"))
    print(ast.to_lua_source(tree))

.. code-block:: lua

    x = 10 + 20

Two things are worth knowing:

* :meth:`~luaparser.ast.ASTTransformer.visit` returns the root, which may
  itself be a replacement. Always use the returned value rather than assuming
  the original root was modified in place.
* After a replacement, the children of the *new* node are visited, not those of
  the node it replaced. A handler that returns a node of the same type it
  matches on will recurse -- ``visit_Number`` returning a ``Number`` is safe
  because a number has no child nodes, but the same shape on a container node
  needs care.

A replacement node you build yourself has no position information, so
``line`` and ``start_char`` are ``None`` on it. That is harmless for rendering,
which does not use them, but it means you cannot mix rewritten nodes with
offset-based edits to the original text.
