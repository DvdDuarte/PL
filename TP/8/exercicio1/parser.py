import ply.yacc as yacc
from lexer import tokens

# def p_grammar(p):
#     """
#     Frase       : Elementos
    # Elementos   : Elementos MAI Elementos
    #             | Elementos MEN Elementos
    #             | Elementos MUL Elementos
    #             | Expressao
#     Expressao   : NUM
#     """

# 1+2*3

precedence =(
    ('left','MAI','MEN'),
    ('left','MUL','DIV'),
)
def p_frase(p):
    "Frase       : Elementos"

def p_elementos_mais(p):
    "Elementos   : Elementos MAI Elementos"
    if parser.total == 0 and parser.flag == False:
        parser.total = int(p[1])+int(p[3])
        parser.flag = True
    elif p[1]: parser.total += int(p[1])
    elif p[3]: parser.total += int(p[3])
    # print("mais: ", parser.total)

def p_elementos_menos(p):
    "Elementos   : Elementos MEN Elementos"
    if parser.total == 0 and parser.flag == False:
        parser.total = int(p[1])-int(p[3])
        parser.flag = True
    elif p[1]: parser.total -= int(p[1])
    elif p[3]: parser.total -= int(p[3])
    # print("menos: ", parser.total)

def p_elementos_vezes(p):
    "Elementos   : Elementos MUL Elementos"
    if parser.total == 0 and parser.flag == False:
        parser.total = int(p[1])*int(p[3])
    elif p[1]: parser.total *= int(p[1])
    elif p[3]: parser.total *= int(p[3])
    # print("vezes: ", parser.total)

def p_elementos_div(p):
    "Elementos : Elementos DIV Elementos"
    if parser.total == 0 and parser.flag == False:
        parser.total = int(p[1])/int(p[3])
        parser.flag = True
    elif p[1]: parser.total /= int(p[1])
    elif p[3]: parser.total /= int(p[3])
    # print("divisao: ", parser.total)

def p_elementos_expressao(p):
    "Elementos  : Expressao"
    p[0] = p[1]

def p_expressao(p):
    "Expressao  : NUM"
    p[0] = p[1]

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
import sys
for linha in sys.stdin:
    parser.flag = False
    parser.success = True
    parser.total = 0
    parser.parse(linha)
    if parser.success:
       # print("Frase válida!")
        print("Resultado: ", parser.total)

    else:
        print("Frase inválida... Corrija e tente novamente!")