## 1+2 
import ply.lex as lex

tokens = ['ABRIR', 'FECHAR', 'NUM', 'START', 'END', 'SEP']#, 'EMPTY']

t_ABRIR = r'\['
t_FECHAR = r'\]'
t_NUM = r'\d+'
t_START = r'start'
t_END = r'end'
t_SEP = r','
# t_EMPTY = r'\s'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

