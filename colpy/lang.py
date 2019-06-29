#!/usr/bin/env python
import ply.lex as lex
import ply.yacc as yacc
import colormap
from .conversion import Color, RGB, HEX, HSV
import os

MODES = {
    'hex'   : HEX,
    'rgb'   : RGB,
    'rgba'  : RGB,
    'yuv'   : None,
    'cmy'   : None,
    'cmyk'  : None,
    'float' : None,
    'hsv'   : HSV,
    'hsl'   : None,
    'hls'   : None,
    }

class Parser(object):
    """
    Base class for a lexer/parser that has the rules defined as methods
    """
    tokens = ()
    precedence = ()

    def __init__(self, **kw):
        self.debug = kw.get('debug', 0)
        self.names = {}
        try:
            modname = os.path.split(os.path.splitext(__file__)[0])[
                1] + "_" + self.__class__.__name__
        except:
            modname = "parser" + "_" + self.__class__.__name__
        self.debugfile = modname + ".dbg"
        self.tabmodule = modname + "_" + "parsetab"
        # print self.debugfile, self.tabmodule

        # Build the lexer and parser
        lex.lex(module=self, debug=self.debug)
        yacc.yacc(module=self,
                  debug=self.debug,
                  debugfile=self.debugfile,
                  tabmodule=self.tabmodule)

    def run(self):
        while 1:
            try:
                s = input('> ')
            except EOFError:
                break
            if not s:
                continue
            yacc.parse(s)


class Calc(Parser):

    tokens = (
        'NAME', 'NUMBER', 'HEX_COLOR', 'RGB_COLOR', 'HSV_COLOR', 
        'PLUS', 'MINUS', 'EXP', 'TIMES', 'DIVIDE', 'EQUALS',
        'LPAREN', 'RPAREN',
    )

    # Tokens

    t_PLUS   = r'\+'
    t_MINUS  = r'-'
    t_EXP    = r'\*\*'
    t_TIMES  = r'\*'
    t_DIVIDE = r'/'
    t_EQUALS = r'='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_NAME   = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def __init__(self):
        super().__init__()
        self.mode = 'hex' 

    def t_HEX_COLOR(self, t):
        r'\#?[a-fA-F0-9]{6,8}' 
        self.mode = 'hex'
        try:
            t.value = HEX(t.value)
        except Exception as e:
            raise(e)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    def t_RGB_COLOR(self, t):
        r'rgb\(\d+,\d+,\d+(,\d+)?\)'
        regex = r'rgb\((\d)+,(\d+),(\d+)(?:,(\d+))?\)'
        self.mode = 'rgb'
        import re
        ms = re.match(regex, t.value)
        r = int(ms.group(1))
        g = int(ms.group(2))
        b = int(ms.group(3))
        a = int(ms.group(4)) if ms.group(4) else 0
        try:
            t.value = RGB(r,g,b,a)
        except Exception as e:
            raise(e)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    def t_HSV_COLOR(self, t):
        r'hsv\(\d+,\d+,\d+\)'
        regex = r'hsv\((\d)+,(\d+),(\d+)\)'
        self.mode = 'hsv'
        import re
        ms = re.match(regex, t.value)
        h = int(ms.group(1))
        s = int(ms.group(2))
        v = int(ms.group(3))
        try:
            t.value = HSV(h,s,v)
        except Exception as e:
            raise(e)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    def t_NUMBER(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %s" % t.value)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    t_ignore = " \t"

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Parsing rules

    precedence = (
        ('left'  , 'PLUS'   , 'MINUS'  )  ,
        ('left'  , 'TIMES'  , 'DIVIDE' )  ,
        ('left'  , 'EXP'    )          ,
        ('right' , 'UMINUS' )          ,
    )

    def p_statement_assign(self, p):
        'statement : NAME EQUALS expression'
        self.names[p[1]] = p[3]

    def p_statement_assignment_operation(self, p):
        """statement : NAME PLUS EQUALS expression
                     | NAME MINUS EQUALS expression
                     | NAME TIMES EQUALS expression
                     | NAME DIVIDE EQUALS expression
        """
        if p[2] == '+':
            self.names[p[1]] += p[4]
        elif p[2] == '-':
            self.names[p[1]] -= p[4]
        elif p[2] == '*':
            self.names[p[1]] *= p[4]
        elif p[2] == '/':
            self.names[p[1]] /= p[4]

    def p_statement_expr(self, p):
        'statement : expression'
        if isinstance(p[1], Color):
            print(p[1].to(MODES[self.mode]))
        else:
            print(p[1])

    def p_expression_binop(self, p):
        """
        expression : expression PLUS expression
                   | expression MINUS expression
                   | expression TIMES expression
                   | expression DIVIDE expression
                   | expression EXP expression
        """
        # print [repr(p[i]) for i in range(0,4)]
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '**':
            p[0] = p[1] ** p[3]

    def p_expression_uminus(self, p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = -p[2]

    def p_expression_group(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_objects(self, p):
        """
        expression : NUMBER
                   | HEX_COLOR
                   | HSV_COLOR
                   | RGB_COLOR
        """
        p[0] = p[1]

    def p_expression_name(self, p):
        'expression : NAME'
        try:
            p[0] = self.names[p[1]]
        except LookupError:
            print("Undefined name '%s'" % p[1])
            p[0] = 0

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")
     
    # def t_eof(self, t):
    #     import sys
        # sys.exit(0)

def main():
    calc = Calc()
    calc.run()

if __name__ == '__main__': main()
