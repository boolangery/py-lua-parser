from itertools import repeat

class TokenPrinter():
    def __init__(self):
        self._lines = []

    def toStr(self, tokens):
        for token in tokens:
            # extend current source:
            if token.line > len(self._lines):
                self._lines.extend(repeat('', (token.line - len(self._lines))))

            # Insert in source line:
            line = token.line -1
            text = token.text
            position = token.column
            s = self._lines[line]
            # extend string
            if position > len(s):
                s += ' ' * (position - len(s))

            # Use slicing to extract portion to replace:
            s = s[:position] + text + s[position+len(text):]
            self._lines[line] = s


        return '\n'.join(self._lines)