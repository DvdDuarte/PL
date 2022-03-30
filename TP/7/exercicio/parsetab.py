
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRIR END FECHAR NUM SEP STARTLista : ABRIR Elementos FECHARElementos : Elementos SEP ElementoElementos : emptyElementos : ElementoElemento : NUMElemento : STARTElemento : ENDempty :'
    
_lr_action_items = {'ABRIR':([0,],[2,]),'$end':([1,9,],[0,-1,]),'FECHAR':([2,3,4,5,6,7,8,11,],[-8,9,-4,-3,-5,-6,-7,-2,]),'SEP':([2,3,4,5,6,7,8,11,],[-8,10,-4,-3,-5,-6,-7,-2,]),'NUM':([2,10,],[6,6,]),'START':([2,10,],[7,7,]),'END':([2,10,],[8,8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Lista':([0,],[1,]),'Elementos':([2,],[3,]),'Elemento':([2,10,],[4,11,]),'empty':([2,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Lista","S'",1,None,None,None),
  ('Lista -> ABRIR Elementos FECHAR','Lista',3,'p_Frase','parser.py',21),
  ('Elementos -> Elementos SEP Elemento','Elementos',3,'p_Elementos','parser.py',24),
  ('Elementos -> empty','Elementos',1,'p_Elementos_Vazio','parser.py',27),
  ('Elementos -> Elemento','Elementos',1,'p_Elementos_Simples','parser.py',30),
  ('Elemento -> NUM','Elemento',1,'p_Elemento_NUM','parser.py',33),
  ('Elemento -> START','Elemento',1,'p_Elemento_START','parser.py',39),
  ('Elemento -> END','Elemento',1,'p_Elemento_END','parser.py',44),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',53),
]