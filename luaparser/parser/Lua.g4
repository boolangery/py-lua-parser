/*
BSD License

Copyright (c) 2013, Kazunori Sakamoto
Copyright (c) 2016, Alexander Alexeev
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the NAME of Rainer Schuster nor the NAMEs of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

This grammar file derived from:

    Lua 5.3 Reference Manual
    http://www.lua.org/manual/5.3/manual.html

    Lua 5.2 Reference Manual
    http://www.lua.org/manual/5.2/manual.html

    Lua 5.1 grammar written by Nicolai Mainiero
    http://www.antlr3.org/grammar/1178608849736/Lua.g

Tested by Kazunori Sakamoto with Test suite for Lua 5.2 (http://www.lua.org/tests/5.2/)

Tested by Alexander Alexeev with Test suite for Lua 5.3 http://www.lua.org/tests/lua-5.3.2-tests.tar.gz
*/

grammar Lua;

chunk
    : block EOF
    ;

block
    : stat* retstat?
    ;

stat
    : BLOCK_SEP
    | comment_rule
    | setStat
    | call
    | invoke
    | label
    | breakStat
    | goto
    | do
    | whileStat
    | repeat
    | ifStat
    | fornum
    | forin
    | func
    | localfunc
    | localset
    ;

setStat     : varlist '=' explist ;
call        : varOrExp args+ ;
invoke      : varOrExp (':' name args)+ ;
label       : '::' name '::' ;
breakStat   : 'break' ;
goto        : 'goto' name ;
do          : 'do' block 'end' ;
whileStat   : 'while' exp 'do' block 'end' ;
repeat      : 'repeat' block 'until' exp ;
ifStat      : 'if' exp 'then' block elseIfStat* elseStat? 'end' ;
fornum      : 'for' name '=' exp ',' exp (',' exp)? 'do' block 'end' ;
forin       : 'for' namelist 'in' explist 'do' block 'end' ;
func        : 'function' funcname funcbody ;
localfunc   : 'local' 'function' name funcbody ;
localset    : 'local' namelist ('=' explist)? ;

elseIfStat
    : 'elseif' exp 'then' block
    ;

elseStat
    : 'else' block
    ;

retstat
    : 'return' explist? ';'?
    ;

funcname
    : name ('.' name)* (':' name)?
    ;

varlist
    : var (',' var)*
    ;

namelist
    : name (',' name)*
    ;

name
    : NAME
    ;

explist
    : exp (',' exp)*
    ;

exp
    : 'nil'                                     # nil
    | 'false'                                   # false
    | 'true'                                    # true
    | (INT | HEX | FLOAT | HEX_FLOAT)           # number
    | string                                    # stringExp
    | '...'                                     # todo2
    | call                                      # todo3
    | invoke                                    # todo4
    | functiondef                               # todo5
    | prefixexp                                 # todo6
    | tableconstructor                          # table
    | 'not' exp                                 # unOpNot
    | '#' exp                                   # unOpLength
    | '-' exp                                   # unOpMin
    | '~' exp                                   # unOpBitNot
    | exp '+' exp                               # opAdd
    | exp '-' exp                               # opSub
    | exp '*' exp                               # opMult
    | exp '/' exp                               # opFloatDiv
    | exp '//' exp                              # opFloorDiv
    | exp '%' exp                               # opMod
    | exp '&' exp                               # bitOpAnd
    | exp '|' exp                               # bitOpOr
    | exp '~' exp                               # bitOpXor
    | exp '>>' exp                              # bitOpShiftR
    | exp '<<' exp                              # bitOpShiftL
    | <assoc=right> exp '^' exp                 # opExpo
    | <assoc=right> exp '..' exp                # concat
    | exp '<' exp                               # relOpLess
    | exp '>' exp                               # relOpGreater
    | exp '<=' exp                              # relOpLessEq
    | exp '>=' exp                              # relOpGreaterEq
    | exp '~=' exp                              # relOpNotEq
    | exp '==' exp                              # relOpEq
    | exp 'and' exp                             # loOpAnd
    | exp 'or' exp                              # loOpOr
    ;

prefixexp
    : varOrExp nameAndArgs*
    ;

varOrExp
    : var | '(' exp ')'
    ;

var
    : (name | '(' exp ')' varSuffix) varSuffix*
    ;

varSuffix
    : nameAndArgs* ('[' exp ']' | '.' name)
    ;

nameAndArgs
    : (':' name)? args
    ;

/*
var
    : NAME | prefixexp '[' exp ']' | prefixexp '.' NAME
    ;

prefixexp
    : var | functioncall | '(' exp ')'
    ;

functioncall
    : prefixexp args | prefixexp ':' NAME args
    ;
*/

args
    : '(' explist? ')' | tableconstructor | string
    ;

functiondef
    : 'function' funcbody
    ;

funcbody
    : '(' parlist? ')' block 'end'
    ;

parlist
    : namelist (',' '...')? | '...'
    ;

tableconstructor
    : '{' (field (fieldsep field)* fieldsep?)? '}'
    ;

field
    : '[' tableKey ']' '=' tableValue | tableKey '=' tableValue | tableValue
    ;

tableKey
    : exp | name
    ;

tableValue
    : exp
    ;

fieldsep
    : ',' | ';'
    ;

string
    : NORMALSTRING | CHARSTRING | LONGSTRING
    ;

comment_rule
    : COMMENT | LINE_COMMENT
    ;

// LEXER

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

NORMALSTRING
    : '"' ( EscapeSequence | ~('\\'|'"') )* '"'
    ;

CHARSTRING
    : '\'' ( EscapeSequence | ~('\''|'\\') )* '\''
    ;

LONGSTRING
    : '[' NESTED_STR ']'
    ;

fragment
NESTED_STR
    : '=' NESTED_STR '='
    | '[' .*? ']'
    ;

INT
    : Digit+
    ;

HEX
    : '0' [xX] HexDigit+
    ;

FLOAT
    : Digit+ '.' Digit* ExponentPart?
    | '.' Digit+ ExponentPart?
    | Digit+ ExponentPart
    ;

HEX_FLOAT
    : '0' [xX] HexDigit+ '.' HexDigit* HexExponentPart?
    | '0' [xX] '.' HexDigit+ HexExponentPart?
    | '0' [xX] HexDigit+ HexExponentPart
    ;

fragment
ExponentPart
    : [eE] [+-]? Digit+
    ;

fragment
HexExponentPart
    : [pP] [+-]? Digit+
    ;

fragment
EscapeSequence
    : '\\' [abfnrtvz"'\\]
    | '\\' '\r'? '\n'
    | DecimalEscape
    | HexEscape
    | UtfEscape
    ;

fragment
DecimalEscape
    : '\\' Digit
    | '\\' Digit Digit
    | '\\' [0-2] Digit Digit
    ;

fragment
HexEscape
    : '\\' 'x' HexDigit HexDigit
    ;

fragment
UtfEscape
    : '\\' 'u{' HexDigit+ '}'
    ;

fragment
Digit
    : [0-9]
    ;

fragment
HexDigit
    : [0-9a-fA-F]
    ;

COMMENT
    : '--[' NESTED_STR ']'
    ;

LINE_COMMENT
    : '--'
    (                                               // --
    | '[' '='*                                      // --[==
    | '[' '='* ~('='|'['|'\r'|'\n') ~('\r'|'\n')*   // --[==AA
    | ~('['|'\r'|'\n') ~('\r'|'\n')*                // --AAA
    ) ('\r\n'|'\r'|'\n'|EOF)
    ;

WS
    : [ \t\u000C\r\n]+ -> skip
    ;

SHEBANG
    : '#' '!' ~('\n'|'\r')* -> channel(HIDDEN)
    ;

BLOCK_SEP
    : ';' -> channel(HIDDEN)
    ;
