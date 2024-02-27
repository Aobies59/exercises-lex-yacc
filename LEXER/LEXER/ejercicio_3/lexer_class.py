import ply.lex as lex


class LexerClass:

    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = [
        "INLINECOMMENT",
        "MULTILINECOMMENT"
    ]

    t_INLINECOMMENT = r'\#(?:(?!\#).)*'
    t_MULTILINECOMMENT = r'\/\*(?:(?!\*\/|\/\*).|\n)*\*\/'

    def t_newline(self, token):
        r'\n'
        token.lexer.lineno += token.value.count('\n')

    def t_error(self, token):
        token.lexer.skip(1)

    def test(self, string):
        self.lexer.input(string)
        for token in self.lexer:
            print(token.type, token.value)

    def test_with_filename(self, filename):
        file = open(filename)
        self.lexer.input(file.read())
        for token in self.lexer:
            print(token.type, token.value)
