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
    : ';'																			# stat_empty
    | varlist '=' explist															# stat_assignment
    | functioncall																	# stat_functioncall
    | label																			# stat_label
    | 'break'																		# stat_break
    | 'goto' NAME																	# stat_goto
    | 'do' block 'end'																# stat_do
    | 'while' exp 'do' block 'end'													# stat_while
    | 'repeat' block 'until' exp													# stat_repeat
    | 'if' exp 'then' block ('elseif' exp 'then' block)* ('else' block)? 'end'		# stat_if
    | 'for' NAME '=' exp ',' exp (',' exp)? 'do' block 'end'						# stat_for
    | 'for' namelist 'in' explist 'do' block 'end'									# stat_for
    | 'function' funcname funcbody													# stat_function
    | 'local' 'function' NAME funcbody												# stat_localfunction
    | 'local' attnamelist ('=' explist)?											# stat_local
    ;

attnamelist
    : nameattrib (',' nameattrib)*
    ;

nameattrib
	: NAME attrib?
	;

attrib
    : ('<' NAME '>')
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
    | <assoc = right> exp (op = '^') exp
    | unary_op = ('not' | '#' | '-' | '~') exp
    | exp op = ('*' | '/' | '%' | '//') exp
    | exp op = ('+' | '-') exp
    | <assoc = right> exp (op = '..') exp
    | exp op = ('<<' | '>>') exp
    | exp (op = '&') exp
    | exp (op = '~') exp
    | exp (op = '|') exp
    | exp op = ('<' | '>' | '<=' | '>=' | '~=' | '==') exp
    | exp (op = 'and') exp
    | exp (op = 'or') exp
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
    : NAME tail* args					# functioncall_name
    | functioncall tail* args			# functioncall_nested
    | '(' exp ')' tail* args			# functioncall_exp
    | NAME tail* ':' NAME args			# functioncall_invoke
    | functioncall tail* ':' NAME args	# functioncall_nestedinvoke
    | '(' exp ')' tail* ':' NAME args	# functioncall_expinvoke
    ;

tail
	: ('[' exp ']' | '.' NAME)
	;

args
    : '(' explist? ')'
    | tableconstructor
    | string
    ;

functiondef
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