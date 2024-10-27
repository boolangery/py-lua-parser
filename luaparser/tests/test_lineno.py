import textwrap
import unittest
import sys

sys.path.insert(0, "./")
from luaparser import ast
from luaparser.astnodes import *
from luaparser.utils import tests


class LineNoTest(tests.TestCase):
    def test_while_loop(self):
        lua_code = """
            function func()
                print(func)
            end
            while i < 10 do -- line 5
                while j < 10 do -- line 6
                    print(j)
                end -- line 8
                print(i)
                i = i + 1
                func()
            end -- line 12
        """
        lua_code = textwrap.dedent(lua_code)
        tree = ast.parse(lua_code)

        expect_line = [[5, 12], [6, 8]]
        idx = 0
        for node in ast.walk(tree):
            if isinstance(node, While):
                self.assertEqual(node.first_token.line, expect_line[idx][0])
                self.assertEqual(node.last_token.line, expect_line[idx][1])
                idx += 1

    def test_repeat_loop(self):
        lua_code = """
            function func()
                print(func)
            end
            local i, j = 0, 0
            repeat -- line 6
                i = i + 1
                repeat -- line 8
                    j = j + 1
                until j < 10 -- line 10
            until (i < 10) -- line 11
        """
        lua_code = textwrap.dedent(lua_code)
        tree = ast.parse(lua_code)
        expect_line = [[6, 11], [8, 10]]
        idx = 0
        for node in ast.walk(tree):
            if isinstance(node, Repeat):
                self.assertEqual(node.first_token.line, expect_line[idx][0])
                self.assertEqual(node.last_token.line, expect_line[idx][1])
                idx += 1

    def test_if_stat(self):
        lua_code = """
            local i, j = 0, 0
            if i + 1 > 0 then -- line 3
                print(i + 1)
                if j + 1 > 0 then -- line 5
                    print(j + 1)
                end -- line 7
            elseif i + 1 > 2 then
                print(i + 1)
            end -- line 10
        """
        lua_code = textwrap.dedent(lua_code)
        tree = ast.parse(lua_code)
        expect_line = [[3, 10], [5, 7]]
        idx = 0
        for node in ast.walk(tree):
            if isinstance(node, If):
                self.assertEqual(node.first_token.line, expect_line[idx][0])
                self.assertEqual(node.last_token.line, expect_line[idx][1])
                idx += 1

    def test_for_stat(self):
        lua_code = """
            local i, j = 0, 0
            for i = 1, 10, 1 do -- line 3
                print(i + j)
            end -- line 5
        """
        lua_code = textwrap.dedent(lua_code)
        tree = ast.parse(lua_code)
        expect_line = [[3, 5]]
        idx = 0
        for node in ast.walk(tree):
            if isinstance(node, Fornum):
                self.assertEqual(node.first_token.line, expect_line[idx][0])
                self.assertEqual(node.last_token.line, expect_line[idx][1])
                idx += 1

    def test_table_expression(self):
        lua_code = """
            local t = { -- line 2
                ["name"] = "number",
                ["key"] = "val",
                [123] = 456
    
            } -- line 7
        """
        lua_code = textwrap.dedent(lua_code)
        tree = ast.parse(lua_code)
        expect_line = [[2, 7]]
        idx = 0
        for node in ast.walk(tree):
            if isinstance(node, Table):
                self.assertEqual(node.first_token.line, expect_line[idx][0])
                self.assertEqual(node.last_token.line, expect_line[idx][1])
                idx += 1


if __name__ == "__main__":
    unittest.main()
