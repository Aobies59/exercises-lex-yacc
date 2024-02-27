import ply.lex as lex


class LexerClass:

    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = [
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "EQUALS",
        "NUMBER"
    ]

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r'='

    def t_NUMBER(self, token):
        r'\d+'
        token.value = int(token.value)
        return token

    t_ignore = ' \t'

    def t_error(self, token):
        token.lexer.skip(1)

    def t_newline(self, token):
        r'\n+'
        token.lexer.lineno += token.value.count('\n')

    def test(self, string):
        self.lexer.input(string)
        for token in self.lexer:
            print(token.type, token.value)