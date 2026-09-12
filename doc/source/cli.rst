###############################################################################
Command line
###############################################################################

Installing the package also installs a ``luaparser`` command, which parses a
file and prints the resulting tree.

.. code-block:: bash

    $ luaparser source.lua

.. code-block:: text

    Usage: luaparser [options] file|directory

    Options:
      --version           show program's version number and exit
      -h, --help          show this help message and exit

      CLI Options:
        -s F, --source=F  source passed in a string
        -x, --xml         set output format to xml
        --pretty          set output format to python ast pretty print style
        -o F, --output=F  write output to file


Output formats
===============================================================================

The default output is JSON. ``--xml`` and ``--pretty`` select the two other
representations described in :doc:`rendering`:

============  =====================================================
Flag          Output
============  =====================================================
*(none)*      JSON -- :func:`~luaparser.ast.to_pretty_json`
``--xml``     XML -- :func:`~luaparser.ast.to_xml_str`
``--pretty``  Indented tree -- :func:`~luaparser.ast.to_pretty_str`
============  =====================================================


Parsing a string
===============================================================================

``--source`` parses its argument directly instead of reading a file:

.. code-block:: bash

    $ luaparser --pretty -s "local a = 1"


Writing to a file
===============================================================================

``--output`` writes the result to a file rather than to standard output:

.. code-block:: bash

    $ luaparser source.lua -x -o tree.xml


Errors
===============================================================================

A file that does not parse produces a message on standard output and exits
normally:

.. code-block:: bash

    $ luaparser -s "local = "
    error: syntax errors: line 1:6: no viable alternative at input 'local ='

Note that the exit status is ``0`` in this case, so a shell script must check
the output rather than the return code.


Example
===============================================================================

Given:

.. code-block:: lua

    local function log(msg)
      print(msg)
    end

    log("hello world !")

``luaparser --pretty source.lua`` prints:

.. code-block:: text

    Chunk: {} 2 keys
      body: {} 2 keys
        Block: {} 2 keys
          body: [] 2 items
            0: {} 1 key
              LocalFunction: {} 5 keys
                wrapped: False
                name: {} 4 keys
                  Name: {} 4 keys
                    wrapped: False
                    id: 'log'
                args: [] 1 item
                  0: {} 1 key
                    Name: {} 4 keys
                      wrapped: False
                      id: 'msg'
                body: {} 2 keys
                  Block: {} 2 keys
                    body: [] 1 item
                      0: {} 1 key
                        Call: {} 5 keys
                          wrapped: False
                          func: {} 4 keys
                            Name: {} 4 keys
                              wrapped: False
                              id: 'print'
                          args: [] 1 item
                            0: {} 1 key
                              Name: {} 4 keys
                                wrapped: False
                                id: 'msg'
