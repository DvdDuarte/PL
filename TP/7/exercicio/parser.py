import ply.yacc as yacc
import sys
from lexer import tokens

# Frases válidas
# [1,2,3,4,5]
# [1,2,3,start,2,3,end,5]

# def p_grammar(p):
#     """
#     Lista : ABRIR Elementos FECHAR
#     Elementos : EMPTY
#               | Elementos SEP Elemento
#               | Elemento
#     Elemento : NUM
#              | START
#              | END
#     """ 

def p_Frase(p):
    "Lista : ABRIR Elementos FECHAR"

def p_Elementos(p):
    "Elementos : Elementos SEP Elemento"

def p_Elementos_Vazio(p):
    "Elementos : empty"

def p_Elementos_Simples(p):
    "Elementos : Elemento"

def p_Elemento_NUM(p):
    "Elemento : NUM"
    parser.output += 1
    if parser.start:
        parser.sum += int(p[1])

def p_Elemento_START(p):
    "Elemento : START"
    parser.output += 1
    parser.start = True

def p_Elemento_END(p):
    "Elemento : END"
    parser.output += 1
    parser.start = False
    res = input("Deseja imprimir o somatorio (Y/N): ")
    if res == "Y":
        parser.print = True
    else:
        parser.print = False
    if parser.print:
            print("Sum: ", parser.sum)

def p_error(p):
    print("Error", p)
    parser.erro = True

def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()

for linha in sys.stdin:
    parser.output = 0
    parser.erro = False

    parser.start = False
    parser.print = False
    parser.sum = 0
    parser.parse(linha)
    if not parser.erro:
        # print("Frase Valida")
        print("Comprimento: ", parser.output)
    else:
        print("Frase invalida")  