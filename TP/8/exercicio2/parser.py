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

def p_elementos(p):
    "Elementos : Elementos Folder"

def p_elemento_folder_unica(p):
    "Elementos : Folder"

def p_folder_vazia(p):
    "Folder : ID CHAVEDIR empty CHAVEESQ"
    folder_name = p[1]
    if parser.instrucoes == "":
        parser.instrucoes += "mkdir " + folder_name + "; cd " + folder_name + "; cd .." + ";"
    else: parser.instrucoes += " mkdir " + folder_name + "; cd " + folder_name + "; cd .." + ";"

def p_folder_multfolder(p):
    "Folder : ID CHAVEDIR Subfolder CHAVEESQ"
    folder_name = p[1]
    if parser.instrucoes == "":
        parser.instrucoes += "mkdir " + folder_name + "; cd " + folder_name + ";"
    else: parser.instrucoes += " mkdir " + folder_name + "; cd " + folder_name + ";"


def p_subfolder_empty(p):
    "Subfolder : Folder"

def p_subfolder(p):
    "Subfolder : Folder SEP Folder"


def p_folder_ficheiro(p):
    "Folder : ID CHAVEDIR Ficheiro CHAVEESQ"
    folder_name = p[1]
    if parser.instrucoes == "":
        parser.instrucoes += "mkdir " + folder_name + "; cd " + folder_name + ";"
    else: parser.instrucoes += " mkdir " + folder_name + "; cd " + folder_name + ";"

def p_ficheiro(p):
    "Ficheiro : ID"
    filename = p[1]
    parser.instrucoes += "touch " + filename + ";"

def p_ficheiros(p):
    "Ficheiro : Ficheiro SEP ID"
    filename = p[3]
    if parser.instrucoes == "":
        parser.instrucoes += "touch " + filename + ";"
    else: parser.instrucoes += "touch " + filename + ";"


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
for linha in sys.stdin:
    parser.success = True
    parser.instrucoes = ""
    parser.total = 0
    parser.parse(linha)
    if parser.success:
        # print("Frase válida!")
        print(parser.instrucoes)
    else:
        print("Frase inválida... Corrija e tente novamente!")