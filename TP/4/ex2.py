# 2
import re 
import ply.lex as lex

tokens=["STRING", "NUM", "PARESQ", "PARDIR", "EQUAL", "TIPO", "URL", "ANO"]

t_NUM = r'\d+'
t_STRING = r'\w*'
t_EQUAL = r'='
t_ANO = r'\d{1,4}'
t_TIPO = r'@\w+'
t_URL = r'()'


input = open("input_ex2.txt")