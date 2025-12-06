def ucs_to_utf8(code_point):
    if code_point < 0x80:
        # 1-byte sequence (0xxxxxxx)
        return bytes([code_point])
    elif code_point < 0x800:
        # 2-byte sequence (110xxxxx 10xxxxxx)
        return bytes([
            0xC0 | (code_point >> 6),
            0x80 | (code_point & 0x3F)
        ])
    elif code_point < 0x10000:
        # 3-byte sequence (1110xxxx 10xxxxxx 10xxxxxx)
        return bytes([
            0xE0 | (code_point >> 12),
            0x80 | ((code_point >> 6) & 0x3F),
            0x80 | (code_point & 0x3F)
        ])
    elif code_point < 0x200000:
        # 4-byte sequence (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
        return bytes([
            0xF0 | (code_point >> 18),
            0x80 | ((code_point >> 12) & 0x3F),
            0x80 | ((code_point >> 6) & 0x3F),
            0x80 | (code_point & 0x3F)
        ])
    elif code_point < 0x4000000:
        # 5-byte sequence (111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx)
        return bytes([
            0xF8 | (code_point >> 24),
            0x80 | ((code_point >> 18) & 0x3F),
            0x80 | ((code_point >> 12) & 0x3F),
            0x80 | ((code_point >> 6) & 0x3F),
            0x80 | (code_point & 0x3F)
        ])
    elif code_point <= 0x7FFFFFFF:
        # 6-byte sequence (1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx)
        return bytes([
            0xFC | (code_point >> 30),
            0x80 | ((code_point >> 24) & 0x3F),
            0x80 | ((code_point >> 18) & 0x3F),
            0x80 | ((code_point >> 12) & 0x3F),
            0x80 | ((code_point >> 6) & 0x3F),
            0x80 | (code_point & 0x3F)
        ])

# This function assumes that the grammar is correctly specified and has range checks
def unescape_lua_string(s: str) -> bytes:
    unescaped_bytes = []
    i = 0
    while i < len(s):
        char = s[i]
        if char == "\\":
            i += 1
            escaped_char = s[i]
            if escaped_char == "a":
                unescaped_bytes.append(b"\a")
            elif escaped_char == "b":
                unescaped_bytes.append(b"\b")
            elif escaped_char == "f":
                unescaped_bytes.append(b"\f")
            elif escaped_char == "n":
                unescaped_bytes.append(b"\n")
            elif escaped_char == "r":
                unescaped_bytes.append(b"\r")
            elif escaped_char == "t":
                unescaped_bytes.append(b"\t")
            elif escaped_char == "v":
                unescaped_bytes.append(b"\v")
            elif escaped_char == "\\":
                unescaped_bytes.append(b"\\")
            elif escaped_char == '"':
                unescaped_bytes.append(b'"')
            elif escaped_char == "'":
                unescaped_bytes.append(b"'")
            elif escaped_char == "z":
                while i + 1 < len(s):
                    # Lua only ignores ASCII spaces after \z, not all Unicode spaces.
                    if not (s[i + 1].isspace() and s[i + 1].isascii()):
                        break
                    i += 1
            elif escaped_char == "x":
                hex_code = int(s[i+1:i+3], 16)
                unescaped_bytes.append(ucs_to_utf8(hex_code))
                i += 2
            elif escaped_char.isdigit():
                digits = [escaped_char]
                if i + 1 < len(s) and s[i + 1].isdigit():
                    digits.append(s[i + 1])
                    i += 1
                    if i + 1 < len(s) and s[i + 1].isdigit():
                        digits.append(s[i + 1])
                        i += 1
                num = int("".join(digits))
                unescaped_bytes.append(ucs_to_utf8(num))
            elif escaped_char == "u":
                i += 1
                hex_chars = []
                while s[i + 1] != "}":
                    hex_chars.append(s[i + 1])
                    i += 1
                hex_code = int("".join(hex_chars), 16)
                unescaped_bytes.append(ucs_to_utf8(hex_code))
                i += 1
        else:
            unescaped_bytes.append(char.encode("utf-8"))
        i += 1

    return b"".join(unescaped_bytes)
