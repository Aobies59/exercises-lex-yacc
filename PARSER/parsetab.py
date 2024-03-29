
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ID NUMBERprogram : assign ";"\n            | assign ";" programassign : ID "=" NUMBER'
    
_lr_action_items = {'ID':([0,4,],[3,3,]),'$end':([1,4,6,],[0,-1,-2,]),';':([2,7,],[4,-3,]),'=':([3,],[5,]),'NUMBER':([5,],[7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,4,],[1,6,]),'assign':([0,4,],[2,2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> assign ;','program',2,'p_program','main.py',35),
  ('program -> assign ; program','program',3,'p_program','main.py',36),
  ('assign -> ID = NUMBER','assign',3,'p_assign','main.py',44),
]
