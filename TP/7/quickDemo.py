import sys
import ply.yacc as yacc
from listas_lex import tokens

# To comment multi line use CTRL + SHIFT + / (7)

# Elementos(1+2)
#           /|\
#          1 2 3 
# 1: Elementos(1) -> NUM -> 1
# 2: OP -> +
# 3: Elemento(2) -> NUM -> 2  


# Frase : Elementos
# Elementos: Elementos OP Elemento
#          | Elemento
# Elemento: NUM

#def p_grammar(p):
#    """"
#    Frase : Elementos
#    Elementos: Elementos OP Elemento
#             | Elemento
#    Elemento: NUM
#    """
# definir acoes spbre produções

def p_Frase(p):
    "Frase : Elementos"

def p_Elementos(p):
    "Elementos : Elementos OP Elemento"
    # print(p[1],p[2],p[3])
    if(p[1]):
    # Pegar nos elementos abaixo e efetuar a op de acordo com o OP
        if(p[2]=="+"):
            parser.output += int(p[1])+p[3]
        else:
            parser.output += int(p[1])-p[3]
    else: 
        if(p[2]=="+"):
            parser.output += int(p[3])
        else:
            parser.output += int(p[3])

def p_Elementos_simples(p):
    "Elementos : Elemento"

def p_Elemento(p):
    "Elemento : NUM"
    print(p[1])
    p[0] = p[1]

def p_error(p):
    print("Error", p)
    parser.erro = True

parser = yacc.yacc()


for linha in sys.stdin:
    parser.output = 0
    parser.erro = False
    parser.parse(linha)
    if not parser.erro:
        print("Frase Valida")
        print(parser.output)
    else:
        print("Frase invalida")  