# Generated from luaparser/parser/Lua.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,412,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,1,1,5,1,87,8,1,10,1,12,1,90,9,1,1,1,3,1,93,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,108,
        8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,3,7,131,8,7,1,7,1,7,1,7,3,7,136,8,7,1,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,146,8,9,10,9,12,9,149,9,9,1,9,3,
        9,152,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,172,8,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,181,8,12,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,189,8,13,1,14,1,14,1,14,5,14,194,8,14,10,14,12,14,197,9,14,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,3,17,211,
        8,17,1,17,3,17,214,8,17,3,17,216,8,17,1,18,1,18,3,18,220,8,18,1,
        18,3,18,223,8,18,1,19,1,19,1,20,1,20,1,20,5,20,230,8,20,10,20,12,
        20,233,9,20,1,21,1,21,1,21,5,21,238,8,21,10,21,12,21,241,9,21,1,
        22,1,22,1,22,3,22,246,8,22,1,23,1,23,1,23,5,23,251,8,23,10,23,12,
        23,254,9,23,1,24,1,24,1,24,5,24,259,8,24,10,24,12,24,262,9,24,1,
        25,1,25,1,25,5,25,267,8,25,10,25,12,25,270,9,25,1,26,1,26,1,26,5,
        26,275,8,26,10,26,12,26,278,9,26,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,3,27,289,8,27,1,28,1,28,1,28,5,28,294,8,28,10,28,12,
        28,297,9,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,308,
        8,29,1,30,1,30,5,30,312,8,30,10,30,12,30,315,9,30,1,31,1,31,1,31,
        1,31,1,31,3,31,322,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,3,32,334,8,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,3,32,345,8,32,1,32,1,32,1,32,3,32,350,8,32,1,33,1,33,3,33,354,
        8,33,1,33,1,33,1,34,1,34,1,34,1,34,5,34,362,8,34,10,34,12,34,365,
        9,34,1,34,3,34,368,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,3,35,380,8,35,1,36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,
        1,38,5,38,391,8,38,10,38,12,38,394,9,38,1,39,1,39,1,39,5,39,399,
        8,39,10,39,12,39,402,9,39,1,40,1,40,1,40,5,40,407,8,40,10,40,12,
        40,410,9,40,1,40,0,0,41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,0,5,1,0,31,36,1,0,23,24,1,0,25,28,1,0,38,42,2,0,51,51,
        55,55,436,0,82,1,0,0,0,2,88,1,0,0,0,4,107,1,0,0,0,6,109,1,0,0,0,
        8,113,1,0,0,0,10,117,1,0,0,0,12,122,1,0,0,0,14,126,1,0,0,0,16,137,
        1,0,0,0,18,140,1,0,0,0,20,155,1,0,0,0,22,160,1,0,0,0,24,163,1,0,
        0,0,26,182,1,0,0,0,28,190,1,0,0,0,30,198,1,0,0,0,32,201,1,0,0,0,
        34,215,1,0,0,0,36,217,1,0,0,0,38,224,1,0,0,0,40,226,1,0,0,0,42,234,
        1,0,0,0,44,242,1,0,0,0,46,247,1,0,0,0,48,255,1,0,0,0,50,263,1,0,
        0,0,52,271,1,0,0,0,54,288,1,0,0,0,56,290,1,0,0,0,58,307,1,0,0,0,
        60,309,1,0,0,0,62,321,1,0,0,0,64,349,1,0,0,0,66,351,1,0,0,0,68,357,
        1,0,0,0,70,379,1,0,0,0,72,381,1,0,0,0,74,383,1,0,0,0,76,387,1,0,
        0,0,78,395,1,0,0,0,80,403,1,0,0,0,82,83,3,2,1,0,83,84,5,0,0,1,84,
        1,1,0,0,0,85,87,3,4,2,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,
        0,88,89,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,93,3,36,18,0,92,91,
        1,0,0,0,92,93,1,0,0,0,93,3,1,0,0,0,94,108,3,12,6,0,95,108,3,60,30,
        0,96,108,3,6,3,0,97,108,3,8,4,0,98,108,3,10,5,0,99,108,3,14,7,0,
        100,108,3,16,8,0,101,108,3,18,9,0,102,108,3,24,12,0,103,108,3,26,
        13,0,104,108,3,74,37,0,105,108,5,2,0,0,106,108,5,55,0,0,107,94,1,
        0,0,0,107,95,1,0,0,0,107,96,1,0,0,0,107,97,1,0,0,0,107,98,1,0,0,
        0,107,99,1,0,0,0,107,100,1,0,0,0,107,101,1,0,0,0,107,102,1,0,0,0,
        107,103,1,0,0,0,107,104,1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,
        108,5,1,0,0,0,109,110,5,3,0,0,110,111,3,2,1,0,111,112,5,6,0,0,112,
        7,1,0,0,0,113,114,5,22,0,0,114,115,3,38,19,0,115,116,3,6,3,0,116,
        9,1,0,0,0,117,118,5,17,0,0,118,119,3,2,1,0,119,120,5,21,0,0,120,
        121,3,38,19,0,121,11,1,0,0,0,122,123,3,76,38,0,123,124,5,37,0,0,
        124,125,3,78,39,0,125,13,1,0,0,0,126,135,5,13,0,0,127,130,3,80,40,
        0,128,129,5,37,0,0,129,131,3,78,39,0,130,128,1,0,0,0,130,131,1,0,
        0,0,131,136,1,0,0,0,132,133,5,9,0,0,133,134,5,56,0,0,134,136,3,32,
        16,0,135,127,1,0,0,0,135,132,1,0,0,0,136,15,1,0,0,0,137,138,5,10,
        0,0,138,139,5,56,0,0,139,17,1,0,0,0,140,141,5,11,0,0,141,142,3,38,
        19,0,142,143,5,19,0,0,143,147,3,2,1,0,144,146,3,20,10,0,145,144,
        1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,151,
        1,0,0,0,149,147,1,0,0,0,150,152,3,22,11,0,151,150,1,0,0,0,151,152,
        1,0,0,0,152,153,1,0,0,0,153,154,5,6,0,0,154,19,1,0,0,0,155,156,5,
        5,0,0,156,157,3,38,19,0,157,158,5,19,0,0,158,159,3,2,1,0,159,21,
        1,0,0,0,160,161,5,4,0,0,161,162,3,2,1,0,162,23,1,0,0,0,163,180,5,
        8,0,0,164,165,5,56,0,0,165,166,5,37,0,0,166,167,3,38,19,0,167,168,
        5,51,0,0,168,171,3,38,19,0,169,170,5,51,0,0,170,172,3,38,19,0,171,
        169,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,3,6,3,0,174,
        181,1,0,0,0,175,176,3,80,40,0,176,177,5,12,0,0,177,178,3,78,39,0,
        178,179,3,6,3,0,179,181,1,0,0,0,180,164,1,0,0,0,180,175,1,0,0,0,
        181,25,1,0,0,0,182,183,5,9,0,0,183,188,3,28,14,0,184,185,5,50,0,
        0,185,186,5,56,0,0,186,189,3,32,16,0,187,189,3,32,16,0,188,184,1,
        0,0,0,188,187,1,0,0,0,189,27,1,0,0,0,190,195,5,56,0,0,191,192,5,
        54,0,0,192,194,5,56,0,0,193,191,1,0,0,0,194,197,1,0,0,0,195,193,
        1,0,0,0,195,196,1,0,0,0,196,29,1,0,0,0,197,195,1,0,0,0,198,199,5,
        9,0,0,199,200,3,32,16,0,200,31,1,0,0,0,201,202,5,43,0,0,202,203,
        3,34,17,0,203,204,5,44,0,0,204,205,3,2,1,0,205,206,5,6,0,0,206,33,
        1,0,0,0,207,210,3,80,40,0,208,209,5,51,0,0,209,211,5,52,0,0,210,
        208,1,0,0,0,210,211,1,0,0,0,211,216,1,0,0,0,212,214,5,52,0,0,213,
        212,1,0,0,0,213,214,1,0,0,0,214,216,1,0,0,0,215,207,1,0,0,0,215,
        213,1,0,0,0,216,35,1,0,0,0,217,219,5,18,0,0,218,220,3,78,39,0,219,
        218,1,0,0,0,219,220,1,0,0,0,220,222,1,0,0,0,221,223,5,55,0,0,222,
        221,1,0,0,0,222,223,1,0,0,0,223,37,1,0,0,0,224,225,3,40,20,0,225,
        39,1,0,0,0,226,231,3,42,21,0,227,228,5,16,0,0,228,230,3,42,21,0,
        229,227,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,
        232,41,1,0,0,0,233,231,1,0,0,0,234,239,3,44,22,0,235,236,5,1,0,0,
        236,238,3,44,22,0,237,235,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,
        0,239,240,1,0,0,0,240,43,1,0,0,0,241,239,1,0,0,0,242,245,3,46,23,
        0,243,244,7,0,0,0,244,246,3,46,23,0,245,243,1,0,0,0,245,246,1,0,
        0,0,246,45,1,0,0,0,247,252,3,48,24,0,248,249,5,53,0,0,249,251,3,
        48,24,0,250,248,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,
        1,0,0,0,253,47,1,0,0,0,254,252,1,0,0,0,255,260,3,50,25,0,256,257,
        7,1,0,0,257,259,3,50,25,0,258,256,1,0,0,0,259,262,1,0,0,0,260,258,
        1,0,0,0,260,261,1,0,0,0,261,49,1,0,0,0,262,260,1,0,0,0,263,268,3,
        52,26,0,264,265,7,2,0,0,265,267,3,52,26,0,266,264,1,0,0,0,267,270,
        1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,51,1,0,0,0,270,268,1,
        0,0,0,271,276,3,54,27,0,272,273,7,3,0,0,273,275,3,54,27,0,274,272,
        1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,276,277,1,0,0,0,277,53,1,
        0,0,0,278,276,1,0,0,0,279,280,5,24,0,0,280,289,3,54,27,0,281,282,
        5,30,0,0,282,289,3,56,28,0,283,284,5,15,0,0,284,289,3,54,27,0,285,
        286,5,40,0,0,286,289,3,54,27,0,287,289,3,56,28,0,288,279,1,0,0,0,
        288,281,1,0,0,0,288,283,1,0,0,0,288,285,1,0,0,0,288,287,1,0,0,0,
        289,55,1,0,0,0,290,295,3,58,29,0,291,292,5,29,0,0,292,294,3,58,29,
        0,293,291,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,
        0,296,57,1,0,0,0,297,295,1,0,0,0,298,308,3,60,30,0,299,308,3,30,
        15,0,300,308,3,66,33,0,301,308,5,52,0,0,302,308,5,57,0,0,303,308,
        5,58,0,0,304,308,5,14,0,0,305,308,5,20,0,0,306,308,5,7,0,0,307,298,
        1,0,0,0,307,299,1,0,0,0,307,300,1,0,0,0,307,301,1,0,0,0,307,302,
        1,0,0,0,307,303,1,0,0,0,307,304,1,0,0,0,307,305,1,0,0,0,307,306,
        1,0,0,0,308,59,1,0,0,0,309,313,3,62,31,0,310,312,3,64,32,0,311,310,
        1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,61,1,
        0,0,0,315,313,1,0,0,0,316,317,5,43,0,0,317,318,3,38,19,0,318,319,
        5,44,0,0,319,322,1,0,0,0,320,322,5,56,0,0,321,316,1,0,0,0,321,320,
        1,0,0,0,322,63,1,0,0,0,323,324,5,54,0,0,324,350,5,56,0,0,325,326,
        5,47,0,0,326,327,3,38,19,0,327,328,5,48,0,0,328,350,1,0,0,0,329,
        330,5,50,0,0,330,331,5,56,0,0,331,333,5,43,0,0,332,334,3,78,39,0,
        333,332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,350,5,44,0,0,
        336,337,5,50,0,0,337,338,5,56,0,0,338,350,3,66,33,0,339,340,5,50,
        0,0,340,341,5,56,0,0,341,350,5,58,0,0,342,344,5,43,0,0,343,345,3,
        78,39,0,344,343,1,0,0,0,344,345,1,0,0,0,345,346,1,0,0,0,346,350,
        5,44,0,0,347,350,3,66,33,0,348,350,5,58,0,0,349,323,1,0,0,0,349,
        325,1,0,0,0,349,329,1,0,0,0,349,336,1,0,0,0,349,339,1,0,0,0,349,
        342,1,0,0,0,349,347,1,0,0,0,349,348,1,0,0,0,350,65,1,0,0,0,351,353,
        5,45,0,0,352,354,3,68,34,0,353,352,1,0,0,0,353,354,1,0,0,0,354,355,
        1,0,0,0,355,356,5,46,0,0,356,67,1,0,0,0,357,363,3,70,35,0,358,359,
        3,72,36,0,359,360,3,70,35,0,360,362,1,0,0,0,361,358,1,0,0,0,362,
        365,1,0,0,0,363,361,1,0,0,0,363,364,1,0,0,0,364,367,1,0,0,0,365,
        363,1,0,0,0,366,368,3,72,36,0,367,366,1,0,0,0,367,368,1,0,0,0,368,
        69,1,0,0,0,369,370,5,47,0,0,370,371,3,38,19,0,371,372,5,48,0,0,372,
        373,5,37,0,0,373,374,3,38,19,0,374,380,1,0,0,0,375,376,5,56,0,0,
        376,377,5,37,0,0,377,380,3,38,19,0,378,380,3,38,19,0,379,369,1,0,
        0,0,379,375,1,0,0,0,379,378,1,0,0,0,380,71,1,0,0,0,381,382,7,4,0,
        0,382,73,1,0,0,0,383,384,5,49,0,0,384,385,5,56,0,0,385,386,5,49,
        0,0,386,75,1,0,0,0,387,392,3,60,30,0,388,389,5,51,0,0,389,391,3,
        60,30,0,390,388,1,0,0,0,391,394,1,0,0,0,392,390,1,0,0,0,392,393,
        1,0,0,0,393,77,1,0,0,0,394,392,1,0,0,0,395,400,3,38,19,0,396,397,
        5,51,0,0,397,399,3,38,19,0,398,396,1,0,0,0,399,402,1,0,0,0,400,398,
        1,0,0,0,400,401,1,0,0,0,401,79,1,0,0,0,402,400,1,0,0,0,403,408,5,
        56,0,0,404,405,5,51,0,0,405,407,5,56,0,0,406,404,1,0,0,0,407,410,
        1,0,0,0,408,406,1,0,0,0,408,409,1,0,0,0,409,81,1,0,0,0,410,408,1,
        0,0,0,38,88,92,107,130,135,147,151,171,180,188,195,210,213,215,219,
        222,231,239,245,252,260,268,276,288,295,307,313,321,333,344,349,
        353,363,367,379,392,400,408
    ]

class LuaParser ( Parser ):

    grammarFileName = "Lua.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'break'", "'do'", "'else'", 
                     "'elseif'", "'end'", "'false'", "'for'", "'function'", 
                     "'goto'", "'if'", "'in'", "'local'", "'nil'", "'not'", 
                     "'or'", "'repeat'", "'return'", "'then'", "'true'", 
                     "'until'", "'while'", "'+'", "'-'", "'*'", "'/'", "'//'", 
                     "'%'", "'^'", "'#'", "'=='", "'~='", "'<='", "'>='", 
                     "'<'", "'>'", "'='", "'&'", "'|'", "'~'", "'>>'", "'<<'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "'::'", "':'", 
                     "','", "'...'", "'..'", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>", "AND", "BREAK", "DO", "ELSE", "ELSEIF", 
                      "END", "FALSE", "FOR", "FUNCTION", "GOTO", "IF", "IN", 
                      "LOCAL", "NIL", "NOT", "OR", "REPEAT", "RETURN", "THEN", 
                      "TRUE", "UNTIL", "WHILE", "ADD", "MINUS", "MULT", 
                      "DIV", "FLOOR", "MOD", "POW", "LENGTH", "EQ", "NEQ", 
                      "LTEQ", "GTEQ", "LT", "GT", "ASSIGN", "BITAND", "BITOR", 
                      "BITNOT", "BITRSHIFT", "BITRLEFT", "OPAR", "CPAR", 
                      "OBRACE", "CBRACE", "OBRACK", "CBRACK", "COLCOL", 
                      "COL", "COMMA", "VARARGS", "CONCAT", "DOT", "SEMCOL", 
                      "NAME", "NUMBER", "STRING", "COMMENT", "LINE_COMMENT", 
                      "SPACE", "NEWLINE", "SHEBANG", "LongBracket" ]

    RULE_chunk = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_do_block = 3
    RULE_while_stat = 4
    RULE_repeat_stat = 5
    RULE_assignment = 6
    RULE_local = 7
    RULE_goto_stat = 8
    RULE_if_stat = 9
    RULE_elseif_stat = 10
    RULE_else_stat = 11
    RULE_for_stat = 12
    RULE_function = 13
    RULE_names = 14
    RULE_function_literal = 15
    RULE_func_body = 16
    RULE_param_list = 17
    RULE_ret_stat = 18
    RULE_expr = 19
    RULE_or_expr = 20
    RULE_and_expr = 21
    RULE_rel_expr = 22
    RULE_concat_expr = 23
    RULE_add_expr = 24
    RULE_mult_expr = 25
    RULE_bitwise_expr = 26
    RULE_unary_expr = 27
    RULE_pow_expr = 28
    RULE_atom = 29
    RULE_var = 30
    RULE_callee = 31
    RULE_tail = 32
    RULE_table_constructor = 33
    RULE_field_list = 34
    RULE_field = 35
    RULE_field_sep = 36
    RULE_label = 37
    RULE_var_list = 38
    RULE_expr_list = 39
    RULE_name_list = 40

    ruleNames =  [ "chunk", "block", "stat", "do_block", "while_stat", "repeat_stat", 
                   "assignment", "local", "goto_stat", "if_stat", "elseif_stat", 
                   "else_stat", "for_stat", "function", "names", "function_literal", 
                   "func_body", "param_list", "ret_stat", "expr", "or_expr", 
                   "and_expr", "rel_expr", "concat_expr", "add_expr", "mult_expr", 
                   "bitwise_expr", "unary_expr", "pow_expr", "atom", "var", 
                   "callee", "tail", "table_constructor", "field_list", 
                   "field", "field_sep", "label", "var_list", "expr_list", 
                   "name_list" ]

    EOF = Token.EOF
    AND=1
    BREAK=2
    DO=3
    ELSE=4
    ELSEIF=5
    END=6
    FALSE=7
    FOR=8
    FUNCTION=9
    GOTO=10
    IF=11
    IN=12
    LOCAL=13
    NIL=14
    NOT=15
    OR=16
    REPEAT=17
    RETURN=18
    THEN=19
    TRUE=20
    UNTIL=21
    WHILE=22
    ADD=23
    MINUS=24
    MULT=25
    DIV=26
    FLOOR=27
    MOD=28
    POW=29
    LENGTH=30
    EQ=31
    NEQ=32
    LTEQ=33
    GTEQ=34
    LT=35
    GT=36
    ASSIGN=37
    BITAND=38
    BITOR=39
    BITNOT=40
    BITRSHIFT=41
    BITRLEFT=42
    OPAR=43
    CPAR=44
    OBRACE=45
    CBRACE=46
    OBRACK=47
    CBRACK=48
    COLCOL=49
    COL=50
    COMMA=51
    VARARGS=52
    CONCAT=53
    DOT=54
    SEMCOL=55
    NAME=56
    NUMBER=57
    STRING=58
    COMMENT=59
    LINE_COMMENT=60
    SPACE=61
    NEWLINE=62
    SHEBANG=63
    LongBracket=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ChunkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def EOF(self):
            return self.getToken(LuaParser.EOF, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_chunk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChunk" ):
                listener.enterChunk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChunk" ):
                listener.exitChunk(self)




    def chunk(self):

        localctx = LuaParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chunk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.block()
            self.state = 83
            self.match(LuaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.StatContext)
            else:
                return self.getTypedRuleContext(LuaParser.StatContext,i)


        def ret_stat(self):
            return self.getTypedRuleContext(LuaParser.Ret_statContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = LuaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 108658137107672844) != 0):
                self.state = 85
                self.stat()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 91
                self.ret_stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LuaParser.AssignmentContext,0)


        def var(self):
            return self.getTypedRuleContext(LuaParser.VarContext,0)


        def do_block(self):
            return self.getTypedRuleContext(LuaParser.Do_blockContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(LuaParser.While_statContext,0)


        def repeat_stat(self):
            return self.getTypedRuleContext(LuaParser.Repeat_statContext,0)


        def local(self):
            return self.getTypedRuleContext(LuaParser.LocalContext,0)


        def goto_stat(self):
            return self.getTypedRuleContext(LuaParser.Goto_statContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(LuaParser.If_statContext,0)


        def for_stat(self):
            return self.getTypedRuleContext(LuaParser.For_statContext,0)


        def function(self):
            return self.getTypedRuleContext(LuaParser.FunctionContext,0)


        def label(self):
            return self.getTypedRuleContext(LuaParser.LabelContext,0)


        def BREAK(self):
            return self.getToken(LuaParser.BREAK, 0)

        def SEMCOL(self):
            return self.getToken(LuaParser.SEMCOL, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = LuaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.var(False)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.do_block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.while_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.repeat_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
                self.local()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 100
                self.goto_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 101
                self.if_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 102
                self.for_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 103
                self.function()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 104
                self.label()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 105
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 106
                self.match(LuaParser.SEMCOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(LuaParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def END(self):
            return self.getToken(LuaParser.END, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_do_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_block" ):
                listener.enterDo_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_block" ):
                listener.exitDo_block(self)




    def do_block(self):

        localctx = LuaParser.Do_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_do_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(LuaParser.DO)
            self.state = 110
            self.block()
            self.state = 111
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LuaParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(LuaParser.ExprContext,0)


        def do_block(self):
            return self.getTypedRuleContext(LuaParser.Do_blockContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)




    def while_stat(self):

        localctx = LuaParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(LuaParser.WHILE)
            self.state = 114
            self.expr()
            self.state = 115
            self.do_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Repeat_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(LuaParser.REPEAT, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def UNTIL(self):
            return self.getToken(LuaParser.UNTIL, 0)

        def expr(self):
            return self.getTypedRuleContext(LuaParser.ExprContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_repeat_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat_stat" ):
                listener.enterRepeat_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat_stat" ):
                listener.exitRepeat_stat(self)




    def repeat_stat(self):

        localctx = LuaParser.Repeat_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_repeat_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(LuaParser.REPEAT)
            self.state = 118
            self.block()
            self.state = 119
            self.match(LuaParser.UNTIL)
            self.state = 120
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self):
            return self.getTypedRuleContext(LuaParser.Var_listContext,0)


        def ASSIGN(self):
            return self.getToken(LuaParser.ASSIGN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(LuaParser.Expr_listContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = LuaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.var_list()
            self.state = 123
            self.match(LuaParser.ASSIGN)
            self.state = 124
            self.expr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCAL(self):
            return self.getToken(LuaParser.LOCAL, 0)

        def name_list(self):
            return self.getTypedRuleContext(LuaParser.Name_listContext,0)


        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def func_body(self):
            return self.getTypedRuleContext(LuaParser.Func_bodyContext,0)


        def ASSIGN(self):
            return self.getToken(LuaParser.ASSIGN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(LuaParser.Expr_listContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_local

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal" ):
                listener.enterLocal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal" ):
                listener.exitLocal(self)




    def local(self):

        localctx = LuaParser.LocalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_local)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(LuaParser.LOCAL)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.state = 127
                self.name_list()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 128
                    self.match(LuaParser.ASSIGN)
                    self.state = 129
                    self.expr_list()


                pass
            elif token in [9]:
                self.state = 132
                self.match(LuaParser.FUNCTION)
                self.state = 133
                self.match(LuaParser.NAME)
                self.state = 134
                self.func_body()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Goto_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(LuaParser.GOTO, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_goto_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto_stat" ):
                listener.enterGoto_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto_stat" ):
                listener.exitGoto_stat(self)




    def goto_stat(self):

        localctx = LuaParser.Goto_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_goto_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(LuaParser.GOTO)
            self.state = 138
            self.match(LuaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LuaParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(LuaParser.ExprContext,0)


        def THEN(self):
            return self.getToken(LuaParser.THEN, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def END(self):
            return self.getToken(LuaParser.END, 0)

        def elseif_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Elseif_statContext)
            else:
                return self.getTypedRuleContext(LuaParser.Elseif_statContext,i)


        def else_stat(self):
            return self.getTypedRuleContext(LuaParser.Else_statContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)




    def if_stat(self):

        localctx = LuaParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(LuaParser.IF)
            self.state = 141
            self.expr()
            self.state = 142
            self.match(LuaParser.THEN)
            self.state = 143
            self.block()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 144
                self.elseif_stat()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 150
                self.else_stat()


            self.state = 153
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(LuaParser.ELSEIF, 0)

        def expr(self):
            return self.getTypedRuleContext(LuaParser.ExprContext,0)


        def THEN(self):
            return self.getToken(LuaParser.THEN, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_elseif_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_stat" ):
                listener.enterElseif_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_stat" ):
                listener.exitElseif_stat(self)




    def elseif_stat(self):

        localctx = LuaParser.Elseif_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elseif_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LuaParser.ELSEIF)
            self.state = 156
            self.expr()
            self.state = 157
            self.match(LuaParser.THEN)
            self.state = 158
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LuaParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_else_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stat" ):
                listener.enterElse_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stat" ):
                listener.exitElse_stat(self)




    def else_stat(self):

        localctx = LuaParser.Else_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_else_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(LuaParser.ELSE)
            self.state = 161
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LuaParser.FOR, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def ASSIGN(self):
            return self.getToken(LuaParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExprContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def do_block(self):
            return self.getTypedRuleContext(LuaParser.Do_blockContext,0)


        def name_list(self):
            return self.getTypedRuleContext(LuaParser.Name_listContext,0)


        def IN(self):
            return self.getToken(LuaParser.IN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(LuaParser.Expr_listContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_for_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stat" ):
                listener.enterFor_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stat" ):
                listener.exitFor_stat(self)




    def for_stat(self):

        localctx = LuaParser.For_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_for_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LuaParser.FOR)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(LuaParser.NAME)
                self.state = 165
                self.match(LuaParser.ASSIGN)
                self.state = 166
                self.expr()
                self.state = 167
                self.match(LuaParser.COMMA)
                self.state = 168
                self.expr()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==51:
                    self.state = 169
                    self.match(LuaParser.COMMA)
                    self.state = 170
                    self.expr()


                self.state = 173
                self.do_block()
                pass

            elif la_ == 2:
                self.state = 175
                self.name_list()
                self.state = 176
                self.match(LuaParser.IN)
                self.state = 177
                self.expr_list()
                self.state = 178
                self.do_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def names(self):
            return self.getTypedRuleContext(LuaParser.NamesContext,0)


        def COL(self):
            return self.getToken(LuaParser.COL, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def func_body(self):
            return self.getTypedRuleContext(LuaParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = LuaParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(LuaParser.FUNCTION)
            self.state = 183
            self.names()
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.state = 184
                self.match(LuaParser.COL)
                self.state = 185
                self.match(LuaParser.NAME)
                self.state = 186
                self.func_body()
                pass
            elif token in [43]:
                self.state = 187
                self.func_body()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.DOT)
            else:
                return self.getToken(LuaParser.DOT, i)

        def getRuleIndex(self):
            return LuaParser.RULE_names

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNames" ):
                listener.enterNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNames" ):
                listener.exitNames(self)




    def names(self):

        localctx = LuaParser.NamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(LuaParser.NAME)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 191
                self.match(LuaParser.DOT)
                self.state = 192
                self.match(LuaParser.NAME)
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def func_body(self):
            return self.getTypedRuleContext(LuaParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_function_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_literal" ):
                listener.enterFunction_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_literal" ):
                listener.exitFunction_literal(self)




    def function_literal(self):

        localctx = LuaParser.Function_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(LuaParser.FUNCTION)
            self.state = 199
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPAR(self):
            return self.getToken(LuaParser.OPAR, 0)

        def param_list(self):
            return self.getTypedRuleContext(LuaParser.Param_listContext,0)


        def CPAR(self):
            return self.getToken(LuaParser.CPAR, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def END(self):
            return self.getToken(LuaParser.END, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_func_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_body" ):
                listener.enterFunc_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_body" ):
                listener.exitFunc_body(self)




    def func_body(self):

        localctx = LuaParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(LuaParser.OPAR)
            self.state = 202
            self.param_list()
            self.state = 203
            self.match(LuaParser.CPAR)
            self.state = 204
            self.block()
            self.state = 205
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_list(self):
            return self.getTypedRuleContext(LuaParser.Name_listContext,0)


        def COMMA(self):
            return self.getToken(LuaParser.COMMA, 0)

        def VARARGS(self):
            return self.getToken(LuaParser.VARARGS, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = LuaParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.name_list()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==51:
                    self.state = 208
                    self.match(LuaParser.COMMA)
                    self.state = 209
                    self.match(LuaParser.VARARGS)


                pass
            elif token in [44, 52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 212
                    self.match(LuaParser.VARARGS)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LuaParser.RETURN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(LuaParser.Expr_listContext,0)


        def SEMCOL(self):
            return self.getToken(LuaParser.SEMCOL, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_ret_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet_stat" ):
                listener.enterRet_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet_stat" ):
                listener.exitRet_stat(self)




    def ret_stat(self):

        localctx = LuaParser.Ret_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ret_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(LuaParser.RETURN)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 508951838961222272) != 0):
                self.state = 218
                self.expr_list()


            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 221
                self.match(LuaParser.SEMCOL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expr(self):
            return self.getTypedRuleContext(LuaParser.Or_exprContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = LuaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.or_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.And_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.And_exprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.OR)
            else:
                return self.getToken(LuaParser.OR, i)

        def getRuleIndex(self):
            return LuaParser.RULE_or_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expr" ):
                listener.enterOr_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expr" ):
                listener.exitOr_expr(self)




    def or_expr(self):

        localctx = LuaParser.Or_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_or_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.and_expr()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 227
                self.match(LuaParser.OR)
                self.state = 228
                self.and_expr()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rel_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Rel_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.Rel_exprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.AND)
            else:
                return self.getToken(LuaParser.AND, i)

        def getRuleIndex(self):
            return LuaParser.RULE_and_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expr" ):
                listener.enterAnd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expr" ):
                listener.exitAnd_expr(self)




    def and_expr(self):

        localctx = LuaParser.And_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_and_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.rel_expr()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 235
                self.match(LuaParser.AND)
                self.state = 236
                self.rel_expr()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Concat_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.Concat_exprContext,i)


        def LT(self):
            return self.getToken(LuaParser.LT, 0)

        def GT(self):
            return self.getToken(LuaParser.GT, 0)

        def LTEQ(self):
            return self.getToken(LuaParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(LuaParser.GTEQ, 0)

        def NEQ(self):
            return self.getToken(LuaParser.NEQ, 0)

        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_rel_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_expr" ):
                listener.enterRel_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_expr" ):
                listener.exitRel_expr(self)




    def rel_expr(self):

        localctx = LuaParser.Rel_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_rel_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.concat_expr()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0):
                self.state = 243
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 244
                self.concat_expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Add_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.Add_exprContext,i)


        def CONCAT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.CONCAT)
            else:
                return self.getToken(LuaParser.CONCAT, i)

        def getRuleIndex(self):
            return LuaParser.RULE_concat_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat_expr" ):
                listener.enterConcat_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat_expr" ):
                listener.exitConcat_expr(self)




    def concat_expr(self):

        localctx = LuaParser.Concat_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_concat_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.add_expr()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 248
                self.match(LuaParser.CONCAT)
                self.state = 249
                self.add_expr()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Mult_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.Mult_exprContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.ADD)
            else:
                return self.getToken(LuaParser.ADD, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.MINUS)
            else:
                return self.getToken(LuaParser.MINUS, i)

        def getRuleIndex(self):
            return LuaParser.RULE_add_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_expr" ):
                listener.enterAdd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_expr" ):
                listener.exitAdd_expr(self)




    def add_expr(self):

        localctx = LuaParser.Add_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_add_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.mult_expr()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 256
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.mult_expr()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mult_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwise_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Bitwise_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.Bitwise_exprContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.MULT)
            else:
                return self.getToken(LuaParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.DIV)
            else:
                return self.getToken(LuaParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.MOD)
            else:
                return self.getToken(LuaParser.MOD, i)

        def FLOOR(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.FLOOR)
            else:
                return self.getToken(LuaParser.FLOOR, i)

        def getRuleIndex(self):
            return LuaParser.RULE_mult_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult_expr" ):
                listener.enterMult_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult_expr" ):
                listener.exitMult_expr(self)




    def mult_expr(self):

        localctx = LuaParser.Mult_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mult_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.bitwise_expr()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0):
                self.state = 264
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.bitwise_expr()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bitwise_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Unary_exprContext)
            else:
                return self.getTypedRuleContext(LuaParser.Unary_exprContext,i)


        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.BITAND)
            else:
                return self.getToken(LuaParser.BITAND, i)

        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.BITOR)
            else:
                return self.getToken(LuaParser.BITOR, i)

        def BITNOT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.BITNOT)
            else:
                return self.getToken(LuaParser.BITNOT, i)

        def BITRSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.BITRSHIFT)
            else:
                return self.getToken(LuaParser.BITRSHIFT, i)

        def BITRLEFT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.BITRLEFT)
            else:
                return self.getToken(LuaParser.BITRLEFT, i)

        def getRuleIndex(self):
            return LuaParser.RULE_bitwise_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwise_expr" ):
                listener.enterBitwise_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwise_expr" ):
                listener.exitBitwise_expr(self)




    def bitwise_expr(self):

        localctx = LuaParser.Bitwise_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_bitwise_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.unary_expr()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521215115264) != 0):
                self.state = 272
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8521215115264) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self.unary_expr()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(LuaParser.MINUS, 0)

        def unary_expr(self):
            return self.getTypedRuleContext(LuaParser.Unary_exprContext,0)


        def LENGTH(self):
            return self.getToken(LuaParser.LENGTH, 0)

        def pow_expr(self):
            return self.getTypedRuleContext(LuaParser.Pow_exprContext,0)


        def NOT(self):
            return self.getToken(LuaParser.NOT, 0)

        def BITNOT(self):
            return self.getToken(LuaParser.BITNOT, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_unary_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expr" ):
                listener.enterUnary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expr" ):
                listener.exitUnary_expr(self)




    def unary_expr(self):

        localctx = LuaParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unary_expr)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(LuaParser.MINUS)
                self.state = 280
                self.unary_expr()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(LuaParser.LENGTH)
                self.state = 282
                self.pow_expr()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(LuaParser.NOT)
                self.state = 284
                self.unary_expr()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 285
                self.match(LuaParser.BITNOT)
                self.state = 286
                self.unary_expr()
                pass
            elif token in [7, 9, 14, 20, 43, 45, 52, 56, 57, 58]:
                self.enterOuterAlt(localctx, 5)
                self.state = 287
                self.pow_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pow_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.AtomContext)
            else:
                return self.getTypedRuleContext(LuaParser.AtomContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.POW)
            else:
                return self.getToken(LuaParser.POW, i)

        def getRuleIndex(self):
            return LuaParser.RULE_pow_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow_expr" ):
                listener.enterPow_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow_expr" ):
                listener.exitPow_expr(self)




    def pow_expr(self):

        localctx = LuaParser.Pow_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_pow_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.atom()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 291
                self.match(LuaParser.POW)
                self.state = 292
                self.atom()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LuaParser.VarContext,0)


        def function_literal(self):
            return self.getTypedRuleContext(LuaParser.Function_literalContext,0)


        def table_constructor(self):
            return self.getTypedRuleContext(LuaParser.Table_constructorContext,0)


        def VARARGS(self):
            return self.getToken(LuaParser.VARARGS, 0)

        def NUMBER(self):
            return self.getToken(LuaParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(LuaParser.STRING, 0)

        def NIL(self):
            return self.getToken(LuaParser.NIL, 0)

        def TRUE(self):
            return self.getToken(LuaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LuaParser.FALSE, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = LuaParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_atom)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43, 56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.var(False)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.function_literal()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 300
                self.table_constructor()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.match(LuaParser.VARARGS)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 5)
                self.state = 302
                self.match(LuaParser.NUMBER)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 6)
                self.state = 303
                self.match(LuaParser.STRING)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 304
                self.match(LuaParser.NIL)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 8)
                self.state = 305
                self.match(LuaParser.TRUE)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 9)
                self.state = 306
                self.match(LuaParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, assign:bool=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self.assign = assign

        def callee(self):
            return self.getTypedRuleContext(LuaParser.CalleeContext,0)


        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self, assign:bool):

        localctx = LuaParser.VarContext(self, self._ctx, self.state, assign)
        self.enterRule(localctx, 60, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.callee(assign)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 310
                    self.tail() 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalleeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, assign:bool=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.assign = None
            self.assign = assign

        def OPAR(self):
            return self.getToken(LuaParser.OPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(LuaParser.ExprContext,0)


        def CPAR(self):
            return self.getToken(LuaParser.CPAR, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_callee

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallee" ):
                listener.enterCallee(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallee" ):
                listener.exitCallee(self)




    def callee(self, assign:bool):

        localctx = LuaParser.CalleeContext(self, self._ctx, self.state, assign)
        self.enterRule(localctx, 62, self.RULE_callee)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(LuaParser.OPAR)
                self.state = 317
                self.expr()
                self.state = 318
                self.match(LuaParser.CPAR)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(LuaParser.NAME)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_tail

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Tail_invokeContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COL(self):
            return self.getToken(LuaParser.COL, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def OPAR(self):
            return self.getToken(LuaParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(LuaParser.CPAR, 0)
        def expr_list(self):
            return self.getTypedRuleContext(LuaParser.Expr_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_invoke" ):
                listener.enterTail_invoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_invoke" ):
                listener.exitTail_invoke(self)


    class Tail_brack_indexContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OBRACK(self):
            return self.getToken(LuaParser.OBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(LuaParser.ExprContext,0)

        def CBRACK(self):
            return self.getToken(LuaParser.CBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_brack_index" ):
                listener.enterTail_brack_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_brack_index" ):
                listener.exitTail_brack_index(self)


    class Tail_tableContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def table_constructor(self):
            return self.getTypedRuleContext(LuaParser.Table_constructorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_table" ):
                listener.enterTail_table(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_table" ):
                listener.exitTail_table(self)


    class Tail_invoke_tableContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COL(self):
            return self.getToken(LuaParser.COL, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def table_constructor(self):
            return self.getTypedRuleContext(LuaParser.Table_constructorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_invoke_table" ):
                listener.enterTail_invoke_table(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_invoke_table" ):
                listener.exitTail_invoke_table(self)


    class Tail_invoke_strContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COL(self):
            return self.getToken(LuaParser.COL, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def STRING(self):
            return self.getToken(LuaParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_invoke_str" ):
                listener.enterTail_invoke_str(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_invoke_str" ):
                listener.exitTail_invoke_str(self)


    class Tail_callContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(LuaParser.OPAR, 0)
        def CPAR(self):
            return self.getToken(LuaParser.CPAR, 0)
        def expr_list(self):
            return self.getTypedRuleContext(LuaParser.Expr_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_call" ):
                listener.enterTail_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_call" ):
                listener.exitTail_call(self)


    class Tail_stringContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(LuaParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_string" ):
                listener.enterTail_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_string" ):
                listener.exitTail_string(self)


    class Tail_dot_indexContext(TailContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.TailContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(LuaParser.DOT, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail_dot_index" ):
                listener.enterTail_dot_index(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail_dot_index" ):
                listener.exitTail_dot_index(self)



    def tail(self):

        localctx = LuaParser.TailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_tail)
        self._la = 0 # Token type
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Tail_dot_indexContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(LuaParser.DOT)
                self.state = 324
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                localctx = LuaParser.Tail_brack_indexContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(LuaParser.OBRACK)
                self.state = 326
                self.expr()
                self.state = 327
                self.match(LuaParser.CBRACK)
                pass

            elif la_ == 3:
                localctx = LuaParser.Tail_invokeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 329
                self.match(LuaParser.COL)
                self.state = 330
                self.match(LuaParser.NAME)
                self.state = 331
                self.match(LuaParser.OPAR)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 508951838961222272) != 0):
                    self.state = 332
                    self.expr_list()


                self.state = 335
                self.match(LuaParser.CPAR)
                pass

            elif la_ == 4:
                localctx = LuaParser.Tail_invoke_tableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                self.match(LuaParser.COL)
                self.state = 337
                self.match(LuaParser.NAME)
                self.state = 338
                self.table_constructor()
                pass

            elif la_ == 5:
                localctx = LuaParser.Tail_invoke_strContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 339
                self.match(LuaParser.COL)
                self.state = 340
                self.match(LuaParser.NAME)
                self.state = 341
                self.match(LuaParser.STRING)
                pass

            elif la_ == 6:
                localctx = LuaParser.Tail_callContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 342
                self.match(LuaParser.OPAR)
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 508951838961222272) != 0):
                    self.state = 343
                    self.expr_list()


                self.state = 346
                self.match(LuaParser.CPAR)
                pass

            elif la_ == 7:
                localctx = LuaParser.Tail_tableContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 347
                self.table_constructor()
                pass

            elif la_ == 8:
                localctx = LuaParser.Tail_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 348
                self.match(LuaParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_constructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBRACE(self):
            return self.getToken(LuaParser.OBRACE, 0)

        def CBRACE(self):
            return self.getToken(LuaParser.CBRACE, 0)

        def field_list(self):
            return self.getTypedRuleContext(LuaParser.Field_listContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_table_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_constructor" ):
                listener.enterTable_constructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_constructor" ):
                listener.exitTable_constructor(self)




    def table_constructor(self):

        localctx = LuaParser.Table_constructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_table_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(LuaParser.OBRACE)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 509092576449577600) != 0):
                self.state = 352
                self.field_list()


            self.state = 355
            self.match(LuaParser.CBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldContext,i)


        def field_sep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.Field_sepContext)
            else:
                return self.getTypedRuleContext(LuaParser.Field_sepContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list" ):
                listener.enterField_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list" ):
                listener.exitField_list(self)




    def field_list(self):

        localctx = LuaParser.Field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_field_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.field()
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 358
                    self.field_sep()
                    self.state = 359
                    self.field() 
                self.state = 365
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51 or _la==55:
                self.state = 366
                self.field_sep()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBRACK(self):
            return self.getToken(LuaParser.OBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExprContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExprContext,i)


        def CBRACK(self):
            return self.getToken(LuaParser.CBRACK, 0)

        def ASSIGN(self):
            return self.getToken(LuaParser.ASSIGN, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = LuaParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_field)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(LuaParser.OBRACK)
                self.state = 370
                self.expr()
                self.state = 371
                self.match(LuaParser.CBRACK)
                self.state = 372
                self.match(LuaParser.ASSIGN)
                self.state = 373
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(LuaParser.NAME)
                self.state = 376
                self.match(LuaParser.ASSIGN)
                self.state = 377
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_sepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(LuaParser.COMMA, 0)

        def SEMCOL(self):
            return self.getToken(LuaParser.SEMCOL, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_field_sep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_sep" ):
                listener.enterField_sep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_sep" ):
                listener.exitField_sep(self)




    def field_sep(self):

        localctx = LuaParser.Field_sepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_field_sep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            _la = self._input.LA(1)
            if not(_la==51 or _la==55):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLCOL(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COLCOL)
            else:
                return self.getToken(LuaParser.COLCOL, i)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = LuaParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(LuaParser.COLCOL)
            self.state = 384
            self.match(LuaParser.NAME)
            self.state = 385
            self.match(LuaParser.COLCOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def getRuleIndex(self):
            return LuaParser.RULE_var_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_list" ):
                listener.enterVar_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_list" ):
                listener.exitVar_list(self)




    def var_list(self):

        localctx = LuaParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.var(True)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 388
                self.match(LuaParser.COMMA)
                self.state = 389
                self.var(True)
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExprContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def getRuleIndex(self):
            return LuaParser.RULE_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_list" ):
                listener.enterExpr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_list" ):
                listener.exitExpr_list(self)




    def expr_list(self):

        localctx = LuaParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.expr()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 396
                self.match(LuaParser.COMMA)
                self.state = 397
                self.expr()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def getRuleIndex(self):
            return LuaParser.RULE_name_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_list" ):
                listener.enterName_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_list" ):
                listener.exitName_list(self)




    def name_list(self):

        localctx = LuaParser.Name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_name_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(LuaParser.NAME)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 404
                    self.match(LuaParser.COMMA)
                    self.state = 405
                    self.match(LuaParser.NAME) 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





