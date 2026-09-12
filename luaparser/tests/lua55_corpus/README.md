# Lua 5.5 corpus

The official Lua test suite, vendored verbatim from
<https://github.com/lua/lua/tree/v5.5.1/testes> (tag `v5.5.1`).

It is used by `test_lua55_corpus.py` as a real-world exercise of the parser and
of `ast.to_lua_source`: these files are hand-written Lua that leans on the
awkward corners of the syntax (long bracket strings, `\z` continuations,
parenthesis-less calls, chained unary minus, comments inside table
constructors), which is exactly where a round trip tends to break.

Lua is distributed under the MIT license; see <https://www.lua.org/license.html>.
