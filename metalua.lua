local parser = require "lua-parser.parser"
local pp = require "lua-parser.pp"

function readAll(file)
    local f = io.open(file, "rb")
    local content = f:read("*all")
    f:close()
    return content
end

if #arg ~= 1 then
    print("Usage: parse.lua <filename>")
    os.exit(1)
end

local content = readAll(arg[1])
local ast, error_msg = parser.parse(content, arg[1])
if not ast then
    print(error_msg)
    os.exit(1)
end

pp.print(ast)
os.exit(0)