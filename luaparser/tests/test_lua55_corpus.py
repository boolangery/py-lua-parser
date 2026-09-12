"""Round trip the official Lua 5.5 test suite through the parser and printer.

The corpus lives in ``lua55_corpus/`` and is described by its README. Every file
is checked for three properties:

Comments are compared as a set rather than by attachment point: which node a
comment hangs off is a positional detail that legitimately shifts when the
source is reformatted, but no comment may be dropped or altered.
"""

import os

from luaparser import ast
from luaparser.utils import tests

CORPUS_DIR = os.path.join(os.path.dirname(__file__), "lua55_corpus")

# The suite deliberately contains files with bytes that are not valid UTF-8
# (strings.lua tests 8-bit cleanliness), so the corpus is read as latin-1 to
# preserve them byte for byte.
CORPUS_ENCODING = "latin-1"


def corpus_files():
    return sorted(f for f in os.listdir(CORPUS_DIR) if f.endswith(".lua"))


def strip_comments(tree):
    for node in ast.walk(tree):
        if getattr(node, "comments", None):
            node.comments = []
    return tree


def all_comments(tree):
    return sorted(c.s for node in ast.walk(tree) for c in getattr(node, "comments", None) or [])


class Lua55CorpusTestCase(tests.TestCase):
    def test_corpus_is_present(self):
        # Guards against the round trip test silently passing on an empty
        # directory if the corpus ever fails to be packaged.
        self.assertEqual(34, len(corpus_files()))

    def test_corpus_round_trip(self):
        for filename in corpus_files():
            with self.subTest(filename=filename):
                path = os.path.join(CORPUS_DIR, filename)
                with open(path, encoding=CORPUS_ENCODING) as f:
                    source = f.read()

                tree = ast.parse(source)
                output = ast.to_lua_source(tree)

                reparsed = ast.parse(output)
                self.assertEqual(
                    all_comments(tree),
                    all_comments(reparsed),
                    f"{filename}: comments were lost or altered by the round trip",
                )
                self.assertEqual(
                    output,
                    ast.to_lua_source(reparsed),
                    f"{filename}: printing is not a fixpoint",
                )
                # strip_comments mutates, so it has to come after everything
                # that renders these trees.
                self.assertEqual(
                    ast.to_pretty_str(strip_comments(tree)),
                    ast.to_pretty_str(strip_comments(reparsed)),
                    f"{filename}: round trip changed the tree",
                )
