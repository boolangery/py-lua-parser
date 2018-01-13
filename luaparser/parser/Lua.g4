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

//////////////////////////////////////////////////////////////////////////////////
//                                Grammar                                       //
//////////////////////////////////////////////////////////////////////////////////
grammar Lua;

chunk: block EOF;
block: stat* retstat?;

stat
    : SEMI_COLON
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

setStat: varlist EQUAL explist ;
call: varOrExp args+ ;
invoke: varOrExp (COLON name args)+ ;
label: LABEL name LABEL ;
breakStat: BREAK ;
goto: GOTO name ;
do: DO block END ;
whileStat: WHILE exp DO block END ;
repeat: REPEAT block UNTIL exp ;
ifStat: IF exp THEN block elseIfStat* elseStat? END ;
fornum: FOR name EQUAL exp COMMA exp (COMMA exp)? DO block END ;
forin: FOR namelist IN explist DO block END ;
func: FUNCTION funcname funcbody ;
localfunc: LOCAL FUNCTION name funcbody ;
localset: LOCAL namelist (EQUAL explist)? ;
elseIfStat: ELSEIF exp THEN block;
elseStat: ELSE block;
retstat: RETURN explist? SEMI_COLON?;

funcname: name (INDEX name)* (COLON name)?;
varlist: var (COMMA var)*;
namelist: name (COMMA name)*;
name: NAME;
explist: exp (COMMA exp)*;

exp
    : NIL                                       # nil
    | FALSE                                     # false
    | TRUE                                      # true
    | (INT | HEX | FLOAT | HEX_FLOAT)           # number
    | string                                    # stringExp
    | VARARGS                                   # todo2
    | call                                      # todo3
    | invoke                                    # todo4
    | functiondef                               # todo5
    | prefixexp                                 # todo6
    | tableconstructor                          # table
    | NOT exp                                   # unOpNot
    | OP_LENGTH exp                             # unOpLength
    | OP_MINUS exp                              # unOpMin
    | OP_BIT_NOT exp                            # unOpBitNot
    | exp OP_ADD exp                            # opAdd
    | exp OP_MINUS exp                          # opSub
    | exp OP_MULT exp                           # opMult
    | exp OP_FLOAT_DIV exp                      # opFloatDiv
    | exp OP_FLOOR_DIV exp                      # opFloorDiv
    | exp OP_MOD exp                            # opMod
    | exp OP_BIT_AND exp                        # bitOpAnd
    | exp OP_BIT_OR exp                         # bitOpOr
    | exp OP_BIT_NOT exp                        # bitOpXor
    | exp OP_BIT_SR exp                         # bitOpShiftR
    | exp OP_BIT_SL exp                         # bitOpShiftL
    | <assoc=right> exp OP_EXP exp              # opExpo
    | <assoc=right> exp OP_CONCAT exp           # concat
    | exp OP_LT exp                             # relOpLess
    | exp OP_GT exp                             # relOpGreater
    | exp OP_LTE exp                            # relOpLessEq
    | exp OP_GTE exp                            # relOpGreaterEq
    | exp OP_NEQ exp                            # relOpNotEq
    | exp OP_EQ exp                             # relOpEq
    | exp AND exp                               # loOpAnd
    | exp OR exp                                # loOpOr
    ;


prefixexp
    : varOrExp nameAndArgs*
    ;

varOrExp
    : var | PARENT_R exp PARENT_L
    ;

var
    : (name | PARENT_R exp PARENT_L varSuffix) varSuffix*
    ;

varSuffix
    : nameAndArgs* (SQUARE_R exp SQUARE_L | INDEX name)
    ;

nameAndArgs
    : (COLON name)? args
    ;

args
    : PARENT_R explist? PARENT_L | tableconstructor | string
    ;

functiondef
    : FUNCTION funcbody
    ;

funcbody
    : PARENT_R parlist? PARENT_L block END
    ;

parlist
    : namelist (COMMA VARARGS)? | VARARGS
    ;

tableconstructor
    : BRACE_R (field (fieldsep field)* fieldsep?)? BRACE_L
    ;

field
    : SQUARE_R tableKey SQUARE_L EQUAL tableValue | tableKey EQUAL tableValue | tableValue
    ;

tableKey
    : exp | name
    ;

tableValue
    : exp
    ;

fieldsep
    : COMMA | SEMI_COLON
    ;

string
    : STRING
    ;

comment_rule
    : COMMENT
    ;

//////////////////////////////////////////////////////////////////////////////////
//                                    Lexer                                     //
//////////////////////////////////////////////////////////////////////////////////
// keyword:
NIL: 'nil';
FALSE: 'false';
TRUE: 'true';
BREAK: 'break';
GOTO: 'goto';
DO: 'do';
WHILE: 'while';
END: 'end';
REPEAT: 'repeat';
UNTIL: 'until';
IF: 'if';
FOR: 'for';
LOCAL: 'local';
FUNCTION: 'function';
THEN: 'then';
ELSE: 'else';
ELSEIF: 'elseif';
IN: 'in';
RETURN: 'return';

VARARGS: '...';
NOT: 'not';
EQUAL: '=';
INDEX: '.';
COMMA: ',';
COLON: ':';
SEMI_COLON: ';' -> channel(HIDDEN);
LABEL: '::';
PARENT_R: '(';
PARENT_L: ')';
BRACE_R: '{';
BRACE_L: '}';
SQUARE_R: '[';
SQUARE_L: ']';

OP_LENGTH: '#';
OP_MINUS: '-';
OP_BIT_NOT: '~';
OP_ADD: '+';
OP_MULT: '*';
OP_FLOAT_DIV: '/';
OP_FLOOR_DIV: '//';
OP_MOD: '%';
OP_BIT_AND: '&';
OP_BIT_OR: '|';
OP_BIT_SR: '>>';
OP_BIT_SL: '<<';
OP_EXP: '^';
OP_CONCAT: '..';
OP_LT: '<';
OP_GT: '>';
OP_LTE: '<=';
OP_GTE: '>=';
OP_NEQ: '~=';
OP_EQ: '==';
AND: 'and';
OR: 'or';

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

STRING
    : ('"' ( EscapeSequence | ~('\\'|'"') )* '"')
    | ('\'' ( EscapeSequence | ~('\''|'\\') )* '\'')
    | ('[' NESTED_STR ']')
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

//////////////////////////////////////////////////////////////////////////////////
//                                 Fragments                                    //
//////////////////////////////////////////////////////////////////////////////////
fragment
NESTED_STR
    : '=' NESTED_STR '='
    | '[' .*? ']'
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
    : ('--[' NESTED_STR ']')
    | '--'
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
