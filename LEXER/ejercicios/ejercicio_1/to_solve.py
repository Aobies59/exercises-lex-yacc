import ply.lex as lex

# define tokens
tokens = [
    "PALABRA",
    "NUMERO"
]

t_PALABRA = r'[a-zA_Z][a-zA-Z0-9_]*'


# type, value, lineno, lexpos
def t_NUMERO(token):
    r'[1-9]+[0-9]*'
    token.value = int(token.value)
    return token


t_ignore = r' '


def t_newline(token):
    r'\n+'
    token.lexer.lineno += token.value.count('\n')


def t_error(token):
    print(f"Illegal character: {token.value}")
    token.lexer.skip(1)


# build the lexer
lexer = lex.lex()

# execute the lexer with a variable string
file = open("input.txt")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)
