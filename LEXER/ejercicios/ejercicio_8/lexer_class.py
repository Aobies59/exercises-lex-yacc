import ply.lex as lex


class Lexer_Class:

    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = [
        "NOMBRE",
        "DNI",
        "EMAIL",
        "NACIONALIDAD",
        "TELEFONO"
    ]

    t_NOMBRE = r'[A-Z][a-z]* [A-Z][a-z]* [A-Z][a-z]*'
    t_DNI = r'\d{8}[0-9]'
    t_EMAIL = r'(\w|\d|\_|\.|\-)+\@(\w|\d|\_|\.|\-)*\.\w{2,}'
    t_NACIONALIDAD = r'\w+\(\w+\)'
    t_TELEFONO = r'\+\d+\s\d{9}'

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
