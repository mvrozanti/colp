
# lang_Calc_parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftEXPrightUMINUSDIVIDE EQUALS EXP HEX_COLOR HSV_COLOR LPAREN MINUS NAME NUMBER PLUS RGB_COLOR RPAREN TIMESstatement : NAME EQUALS expressionstatement : NAME PLUS EQUALS expression\n                     | NAME MINUS EQUALS expression\n                     | NAME TIMES EQUALS expression\n                     | NAME DIVIDE EQUALS expression\n        statement : expression\n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression TIMES expression\n                   | expression DIVIDE expression\n                   | expression EXP expression\n        expression : MINUS expression %prec UMINUSexpression : LPAREN expression RPAREN\n        expression : NUMBER\n                   | HEX_COLOR\n                   | HSV_COLOR\n                   | RGB_COLOR\n        expression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[2,21,21,21,21,21,21,21,21,21,21,21,21,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[4,12,16,4,4,-14,-15,-16,-17,4,4,4,4,4,4,-12,-18,16,16,4,4,4,4,-7,-8,-9,-10,-11,-13,16,16,16,16,]),'LPAREN':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[5,5,5,5,5,5,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'HEX_COLOR':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'HSV_COLOR':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'RGB_COLOR':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,3,6,7,8,9,20,21,23,28,29,30,31,32,33,34,35,36,37,],[0,-18,-6,-14,-15,-16,-17,-12,-18,-1,-7,-8,-9,-10,-11,-13,-2,-3,-4,-5,]),'EQUALS':([2,11,12,13,14,],[10,24,25,26,27,]),'PLUS':([2,3,6,7,8,9,20,21,22,23,28,29,30,31,32,33,34,35,36,37,],[11,15,-14,-15,-16,-17,-12,-18,15,15,-7,-8,-9,-10,-11,-13,15,15,15,15,]),'TIMES':([2,3,6,7,8,9,20,21,22,23,28,29,30,31,32,33,34,35,36,37,],[13,17,-14,-15,-16,-17,-12,-18,17,17,17,17,-9,-10,-11,-13,17,17,17,17,]),'DIVIDE':([2,3,6,7,8,9,20,21,22,23,28,29,30,31,32,33,34,35,36,37,],[14,18,-14,-15,-16,-17,-12,-18,18,18,18,18,-9,-10,-11,-13,18,18,18,18,]),'EXP':([2,3,6,7,8,9,20,21,22,23,28,29,30,31,32,33,34,35,36,37,],[-18,19,-14,-15,-16,-17,-12,-18,19,19,19,19,19,19,-11,-13,19,19,19,19,]),'RPAREN':([6,7,8,9,20,21,22,28,29,30,31,32,33,],[-14,-15,-16,-17,-12,-18,33,-7,-8,-9,-10,-11,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,10,15,16,17,18,19,24,25,26,27,],[3,20,22,23,28,29,30,31,32,34,35,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','lang.py',158),
  ('statement -> NAME PLUS EQUALS expression','statement',4,'p_statement_assignment_operation','lang.py',162),
  ('statement -> NAME MINUS EQUALS expression','statement',4,'p_statement_assignment_operation','lang.py',163),
  ('statement -> NAME TIMES EQUALS expression','statement',4,'p_statement_assignment_operation','lang.py',164),
  ('statement -> NAME DIVIDE EQUALS expression','statement',4,'p_statement_assignment_operation','lang.py',165),
  ('statement -> expression','statement',1,'p_statement_expr','lang.py',177),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','lang.py',185),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','lang.py',186),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','lang.py',187),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','lang.py',188),
  ('expression -> expression EXP expression','expression',3,'p_expression_binop','lang.py',189),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','lang.py',204),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','lang.py',208),
  ('expression -> NUMBER','expression',1,'p_expression_objects','lang.py',213),
  ('expression -> HEX_COLOR','expression',1,'p_expression_objects','lang.py',214),
  ('expression -> HSV_COLOR','expression',1,'p_expression_objects','lang.py',215),
  ('expression -> RGB_COLOR','expression',1,'p_expression_objects','lang.py',216),
  ('expression -> NAME','expression',1,'p_expression_name','lang.py',221),
]
