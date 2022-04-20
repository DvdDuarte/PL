import ply.yacc as yacc
from lexer import tokens

# precedence =(
#     ('left','MAI','MEN'),
#     ('left','MUL'),
# )

# PL { f1,f2,f3 }

# def p_frase(p): 
#     """
#         Frase : Elementos
#         Elementos : Elementos Folder
#                   | Folder
#         Folder : ID CHAVEDIR CHAVEESQ
#                | ID CHAVEDIR Folder CHAVEESQ
#                | ID CHAVEDIR Ficheiro CHAVEESQ
#         Ficheiro : ID
#                  | Ficheiro SEP ID
#     """

def p_frase(p):
    "Frase : Elementos"
    print(parser.instrucoes)


def p_elementos(p):
    "Elementos : Elementos Folder"
    parser.instrucoes = p[1] + p[2]

def p_elemento_folder_unica(p):
    "Elementos : Folder"
    parser.instrucoes = p[1]

def p_folder_vazia(p):
    "Folder : ID CHAVEDIR empty CHAVEESQ"
    p[0] = " mkdir " + p[1] + "; cd " + p[1] + "; cd ..; "


def p_folder_multfolder(p):
    "Folder : ID CHAVEDIR Subfolder CHAVEESQ"
    p[0] = " mkdir " + p[1] + "; cd " + p[1] + ";" + p[3] + "cd ..; "


def p_subfolder_empty(p):
    "Subfolder : Folder"
    p[0] = p[1]

def p_subfolder(p):
    "Subfolder : Subfolder SEP Folder"
    p[0] = p[1] + p[3]


def p_folder_ficheiro(p):
    "Folder : ID CHAVEDIR Ficheiro CHAVEESQ"
    p[0] = " mkdir " + p[1] + "; cd " + p[1] + ";" + p[3] + " cd ..; "

def p_ficheiro(p):
    "Ficheiro : ID"
    p[0] = " touch " + p[1] + ";"

def p_ficheiros(p):
    "Ficheiro : Ficheiro SEP ID"
    p[0] = p[1] + " touch " + p[3] + ";"

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False

def p_empty(p):
    'empty :'
    pass

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it

import sys
txt = open(sys.argv[1]).read()
parser.parse(txt)

# for linha in sys.stdin:
#     parser.success = True
#     parser.instrucoes = ""
#     parser.total = 0
#     parser.parse(linha)
#     if parser.success:
#         #print("---------------------------------------------------------------------------------")
#         #print("Comando Inserido: ", linha)
#         print(parser.instrucoes)
#         #print("---------------------------------------------------------------------------------")
#     else:
#         #print("---------------------------------------------------------------------------------")
#         print("Frase inválida... Corrija e tente novamente!")
#         #print("---------------------------------------------------------------------------------")