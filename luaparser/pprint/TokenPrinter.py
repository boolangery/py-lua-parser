from itertools import repeat

class TokenPrinter():
    def __init__(self):
        self._lines = []

    def toStr(self, tokens):
        for token in tokens:
            # extend current source:
            if token.line > len(self._lines):
                self._lines.extend(repeat('', (token.line - len(self._lines) + 1)))

            # Insert in source line:
            position = token.column
            s = self._lines[token.line]

            # extend string
            if position > len(s):
                s += ' ' * (position - len(s))

            # Use slicing to extract portion to replace:
            s = s[:position] + token.text + s[position+len(token.text):]
            self._lines[token.line] = s
        return '\n'.join(self._lines)