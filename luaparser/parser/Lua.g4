/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 by Bart Kiers
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * Project      : lua-parser; a Lua 5.2 grammar/parser
 * Developed by : Bart Kiers, bart@big-o.nl
 *                Eliott Dumeix, (update to antlr4 + Lua 5.3 grammar)
 */
grammar Lua;



//////////////////////////////// parser rules ////////////////////////////////

chunk
  : block EOF
  ;

block
  : stat* ret_stat?
  ;

stat
  : assignment
  | var[False]
  | do_block
  | while_stat
  | repeat_stat
  | local
  | goto_stat
  | if_stat
  | for_stat
  | function
  | label
  | BREAK
  | SEMCOL
  ;

do_block
  : DO block END
  ;

while_stat
  : WHILE expr do_block
  ;

repeat_stat
  : REPEAT block UNTIL expr
  ;

assignment
  : var_list ASSIGN expr_list // in every 'var' in 'var_list', the last must be an 'index', not a 'call'
  ;

local
  : LOCAL
  ( name_list (ASSIGN expr_list)?
  | FUNCTION NAME func_body)
  ;

goto_stat
  : GOTO NAME
  ;

if_stat
  : IF expr THEN block elseif_stat* else_stat? END
  ;

elseif_stat
  : ELSEIF expr THEN block
  ;

else_stat
  : ELSE block
  ;

for_stat
  : FOR
  ( NAME ASSIGN expr COMMA expr (COMMA expr)? do_block
  | name_list IN expr_list do_block
  )
  ;

function
  : FUNCTION names (COL NAME func_body | func_body)
  ;

names
  : NAME (DOT NAME)*
  ;

function_literal
  : FUNCTION func_body
  ;

func_body
  : OPAR param_list CPAR block END
  ;

param_list
  : name_list (COMMA VARARGS  )?
  | VARARGS?
  ;

ret_stat
  : RETURN expr_list? SEMCOL?
  ;

expr
  : or_expr
  ;

or_expr
  : and_expr (OR and_expr)*
  ;

and_expr
  : rel_expr (AND rel_expr)*
  ;

rel_expr
  : concat_expr ((LT | GT | LTEQ | GTEQ | NEQ | EQ) concat_expr)?
  ;

concat_expr
  : add_expr (CONCAT add_expr)*
  ;

add_expr
  : mult_expr ((ADD | MINUS) mult_expr)*
  ;

mult_expr
  : bitwise_expr ((MULT | DIV | MOD | FLOOR) bitwise_expr)*
  ;

bitwise_expr
  : unary_expr ((BITAND | BITOR | BITNOT | BITRSHIFT | BITRLEFT) unary_expr)*
  ;

unary_expr
  : MINUS unary_expr
  | LENGTH pow_expr
  | NOT unary_expr
  | BITNOT unary_expr
  | pow_expr
  ;

// right associative
pow_expr
  : atom (POW atom)*
  ;

atom
  : var[False]
  | function_literal
  | table_constructor
  | VARARGS
  | NUMBER
  | STRING
  | NIL
  | TRUE
  | FALSE
  ;

var[bool assign]
  : callee[assign] tail*
  ;

callee[bool assign]
  : OPAR expr CPAR | NAME
  ;

tail
  : DOT NAME                      # tail_dot_index
  | OBRACK expr CBRACK            # tail_brack_index
  | COL NAME OPAR expr_list? CPAR # tail_invoke
  | COL NAME table_constructor    # tail_invoke_table
  | COL NAME STRING               # tail_invoke_str
  | OPAR expr_list? CPAR          # tail_call
  | table_constructor             # tail_table
  | STRING                        # tail_string
  ;

table_constructor
  : OBRACE field_list? CBRACE
  ;

field_list
  : field (field_sep field)* field_sep?
  ;

field
  : OBRACK expr CBRACK ASSIGN expr
  | NAME ASSIGN expr
  | expr
  ;

field_sep
  : COMMA
  | SEMCOL
  ;

label
  : COLCOL NAME COLCOL
  ;

var_list
  : var[True] (COMMA var[True])*
  ;

expr_list
  : expr (COMMA expr)*
  ;

name_list
  : NAME (COMMA NAME)*
  ;

//////////////////////////////// lexer rules ////////////////////////////////

AND       : 'and';
BREAK     : 'break';
DO        : 'do';
ELSE      : 'else';
ELSEIF    : 'elseif';
END       : 'end';
FALSE     : 'false';
FOR       : 'for';
FUNCTION  : 'function';
GOTO      : 'goto';
IF        : 'if';
IN        : 'in';
LOCAL     : 'local';
NIL       : 'nil';
NOT       : 'not';
OR        : 'or';
REPEAT    : 'repeat';
RETURN    : 'return';
THEN      : 'then';
TRUE      : 'true';
UNTIL     : 'until';
WHILE     : 'while';
ADD       : '+';
MINUS     : '-';
MULT      : '*';
DIV       : '/';
FLOOR     : '//';
MOD       : '%';
POW       : '^';
LENGTH    : '#';
EQ        : '==';
NEQ       : '~=';
LTEQ      : '<=';
GTEQ      : '>=';
LT        : '<';
GT        : '>';
ASSIGN    : '=';
BITAND    : '&';
BITOR     : '|';
BITNOT    : '~';
BITRSHIFT : '>>';
BITRLEFT  : '<<';
OPAR      : '(';
CPAR      : ')';
OBRACE    : '{';
CBRACE    : '}';
OBRACK    : '[';
CBRACK    : ']';
COLCOL    : '::';
COL       : ':';
COMMA     : ',';
VARARGS   : '...';
CONCAT    : '..';
DOT       : '.';
SEMCOL     : ';';

NAME
  : (Letter | '_') (Letter | '_' | Digit)*
  ;

NUMBER
  : (Digit+ ('.' Digit*)? Exponent? | '.' Digit+ Exponent?)
  | '0' ('x' | 'X') HexDigits ('.' HexDigits?)? BinaryExponent?
  ;

STRING
  : '"'  (EscapeSequence | ~('\\' | '"'  | '\r' | '\n'))* '"'
  | '\'' (EscapeSequence | ~('\\' | '\'' | '\r' | '\n'))* '\''
  | LongBracket
  ;

//////////////////////////////// lexer rules to hide ////////////////////////////////
COMMENT
    : '--[' NESTED_STR ']' -> channel(HIDDEN)
    ;

LINE_COMMENT
    : '--'
    (                                               // --
    | '[' '='*                                      // --[==
    | '[' '='* ~('='|'['|'\r'|'\n') ~('\r'|'\n')*   // --[==AA
    | ~('['|'\r'|'\n') ~('\r'|'\n')*                // --AAA
    )
    -> channel(HIDDEN)
    ;

SPACE
  : (' ' | '\t')+ -> channel(HIDDEN)
  ;

NEWLINE
  : ('\r\n' | '\r' | '\n' | '\u000C')+ -> channel(HIDDEN)
  ;

SHEBANG
  : '#' '!' ~('\n'|'\r')* -> channel(HIDDEN)
  ;

//////////////////////////////// fragment lexer rules ////////////////////////////////
fragment Letter
  : 'a'..'z'
  | 'A'..'Z'
  ;

fragment Digit
  : '0'..'9'
  ;

fragment HexDigit
  : Digit
  | 'a'..'f'
  | 'A'..'F'
  ;

fragment HexDigits
  : HexDigit+
  ;

fragment Exponent
  : ('e' | 'E') ('-' | '+')? Digit+
  ;

fragment BinaryExponent
  : ('p' | 'P') ('-' | '+')? Digit+
  ;

fragment EscapeSequence
  : '\\'
  ( ('a' | 'b' | 'f' | 'n' | 'r' | 't' | 'v' | '\\' | '"' | '\'' | 'z' | LineBreak)
  | Digit (Digit Digit?)?
  | 'x' HexDigit HexDigit
  )
  ;

fragment LineBreak
  : '\r'? '\n'
  | '\r'
  ;

fragment NESTED_STR
  : '=' NESTED_STR '='
  | '[' .*? ']'
  ;

LongBracket
  : '[' NESTED_STR ']'
  ;
