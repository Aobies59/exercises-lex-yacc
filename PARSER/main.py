import sys
import ply.lex as lex
import ply.yacc as yacc

def main(args):
    if len(args) < 2:
        print(f"Usage: {args[0]} <input file>")
        return

    literals = ('=', ';')
    tokens = ('ID', 'NUMBER')

    def t_ID(token):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return token

    def t_NUMBER(token):
        r'\d+'
        token.value = int(token.value)
        return token

    t_ignore = ' \t\n'

    def t_error(token):
        print(f"Lexer error in line {token.lineno}: {token.value[0]}")
        token.lexer.skip(1)

    def t_newline(token):
        r'\n+'
        token.lexer.lineno += len(token.value)

    lexer = lex.lex()

    def p_program(p):
        '''program : assign ";"
            | assign ";" program'''
        if len(p) == 3:
            p[0] = p[1]
        else:
            p[0] = p[3] + p[1]
        print(p[0])

    def p_assign(p):
        '''assign : ID "=" NUMBER'''
        p[0] = p[1] + p[2] + str(p[3])

    def p_error(p):
        if p and p.value:
            print(f"Parser error in line {p.lineno}: {p.value[0]}")
        else:
            print(f"Parser error EOF.")

    parser = yacc.yacc()

    with open(args[1], 'r') as f:
        lexer.input(f.read())
        for token in lexer:
            print(f"{token.type}\t{token.value}")
        parser.parse(f.read())

    return 0

if __name__ == '__main__':
    main(sys.argv)