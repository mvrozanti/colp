colp: lex.yy.c y.tab.c
	gcc -g lex.yy.c y.tab.c -o $@

lex.yy.c: y.tab.c colp.l
	lex $@.l

y.tab.c: colp.y
	yacc -d $@.y

clean: 
	rm -rf lex.yy.c y.tab.c y.tab.h colp colp.dSYM
