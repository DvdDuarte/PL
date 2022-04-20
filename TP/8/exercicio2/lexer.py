# PL { doc {} , aulas { { f1,f2,f3} } }
# PL { doc {} , aulas { { f1,f2,f3} } }

import ply.lex as lex

tokens = ['CHAVEDIR','CHAVEESQ','ID', 'SEP']

t_CHAVEDIR = r'\{'
t_CHAVEESQ = r'\}'
t_ID = r'[A-Z|a-z|\-|0-9]+'
t_SEP = R'\,'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()