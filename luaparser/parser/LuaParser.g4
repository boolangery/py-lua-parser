/*

MIT license

Author: Ken Domino, October 2023

Based on previous work of: Kazunori Sakamoto, Alexander Alexeev

*/

// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

parser grammar LuaParser;

options {
    tokenVocab = LuaLexer;
}

start_
    : chunk EOF
    ;

chunk
    : block
    ;

block
    : stat* retstat?
    ;

stat
    : ';'
    | assign
    | functioncall
    | label
    | 'break'
    | goto
    | do
    | while
    | repeat
    | if
    | for
    | forin
    | functiondef
    | localfunction
    | localassign
    ;

assign
	: varlist '=' explist
	;

goto
	: 'goto' NAME
	;

do
	: 'do' block 'end'
	;

while
	: 'while' exp 'do' block 'end'
	;

repeat
	: 'repeat' block 'until' exp
	;

if
	: 'if' exp 'then' block ('elseif' exp 'then' block)* ('else' block)? 'end'
	;

for
	: 'for' NAME '=' exp ',' exp (',' exp)? 'do' block 'end'
	;

forin
	: 'for' namelist 'in' explist 'do' block 'end'
	;

functiondef
	: 'function' funcname funcbody
	;

localfunction
	: 'local' 'function' NAME funcbody
	;

localassign
	: 'local' namelist ('=' explist)?
	;


attnamelist
    : NAME attrib (',' NAME attrib)*
    ;

attrib
    : ('<' NAME '>')?
    ;

retstat
    : ('return' explist? | 'break' | 'continue') ';'?
    ;

label
    : '::' NAME '::'
    ;

funcname
    : NAME ('.' NAME)* (':' NAME)?
    ;

varlist
    : var (',' var)*
    ;

namelist
    : NAME (',' NAME)*
    ;

explist
    : exp (',' exp)*
    ;

exp
    : 'nil'
    | 'false'
    | 'true'
    | number
    | string
    | '...'
    | functiondef
    | prefixexp
    | tableconstructor
    | <assoc = right> exp ('^') exp
    | ('not' | '#' | '-' | '~') exp
    | exp ('*' | '/' | '%' | '//') exp
    | exp ('+' | '-') exp
    | <assoc = right> exp ('..') exp
    | exp ('<' | '>' | '<=' | '>=' | '~=' | '==') exp
    | exp ('and') exp
    | exp ('or') exp
    | exp ('&' | '|' | '~' | '<<' | '>>') exp
    ;

// var ::=  Name | prefixexp '[' exp ']' | prefixexp '.' Name
var
    : NAME
    | prefixexp tail
    ;

// prefixexp ::= var | functioncall | '(' exp ')'
prefixexp
    : NAME tail*
    | functioncall tail*
    | '(' exp ')' tail*
    ;

// functioncall ::=  prefixexp args | prefixexp ':' Name args;
functioncall
    : NAME tail* args
    | functioncall tail* args
    | '(' exp ')' tail* args
    | NAME tail* ':' NAME args
    | functioncall tail* ':' NAME args
    | '(' exp ')' tail* ':' NAME args
    ;

tail
	: ('[' exp ']' | '.' NAME)
	;

args
    : '(' explist? ')'
    | tableconstructor
    | string
    ;

anonfunctiondef
    : 'function' funcbody
    ;

funcbody
    : '(' parlist ')' block 'end'
    ;

/* lparser.c says "is 'parlist' not empty?"
 * That code does so by checking la(1) == ')'.
 * This means that parlist can derive empty.
 */
parlist
    : namelist (',' '...')?
    | '...'
    |
    ;

tableconstructor
    : '{' fieldlist? '}'
    ;

fieldlist
    : field (fieldsep field)* fieldsep?
    ;

field
    : '[' exp ']' '=' exp
    | NAME '=' exp
    | exp
    ;

fieldsep
    : ','
    | ';'
    ;

number
    : INT
    | HEX
    | FLOAT
    | HEX_FLOAT
    ;

string
    : NORMALSTRING
    | CHARSTRING
    | LONGSTRING
    ;