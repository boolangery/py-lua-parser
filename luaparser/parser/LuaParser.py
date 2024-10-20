# Generated from luaparser/parser/LuaParser.g4 by ANTLR 4.13.2
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
        4,1,68,472,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,1,1,1,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,3,2,65,8,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,101,8,3,10,3,12,3,104,9,3,1,3,1,3,3,3,108,8,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,120,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,146,8,3,3,3,148,8,3,1,4,1,4,1,4,1,4,1,4,5,4,155,8,4,10,
        4,12,4,158,9,4,1,5,1,5,1,5,3,5,163,8,5,1,6,1,6,3,6,167,8,6,1,6,1,
        6,3,6,171,8,6,1,6,3,6,174,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,183,
        8,8,10,8,12,8,186,9,8,1,8,1,8,3,8,190,8,8,1,9,1,9,1,9,5,9,195,8,
        9,10,9,12,9,198,9,9,1,10,1,10,1,10,5,10,203,8,10,10,10,12,10,206,
        9,10,1,11,1,11,1,11,5,11,211,8,11,10,11,12,11,214,9,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,228,8,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,254,
        8,12,10,12,12,12,257,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,267,8,13,3,13,269,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,
        14,278,8,14,10,14,12,14,281,9,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,5,14,290,8,14,10,14,12,14,293,9,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,5,14,304,8,14,10,14,12,14,307,9,14,3,14,309,8,
        14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,319,8,15,10,15,12,
        15,322,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,
        15,334,8,15,10,15,12,15,337,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,5,15,348,8,15,10,15,12,15,351,9,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,365,8,15,10,15,12,
        15,368,9,15,1,15,1,15,1,15,1,15,3,15,374,8,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,5,15,383,8,15,10,15,12,15,386,9,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,5,15,396,8,15,10,15,12,15,399,9,15,1,15,
        1,15,1,15,5,15,404,8,15,10,15,12,15,407,9,15,1,16,1,16,3,16,411,
        8,16,1,16,1,16,1,16,3,16,416,8,16,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,19,1,19,1,19,3,19,430,8,19,1,19,1,19,3,19,434,8,
        19,1,20,1,20,3,20,438,8,20,1,20,1,20,1,21,1,21,1,21,1,21,5,21,446,
        8,21,10,21,12,21,449,9,21,1,21,3,21,452,8,21,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,3,22,464,8,22,1,23,1,23,1,24,1,24,
        1,25,1,25,1,25,0,2,24,30,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,0,8,2,0,28,30,33,33,3,0,37,38,
        45,45,54,54,2,0,29,29,44,44,4,0,19,20,40,41,50,50,56,56,3,0,28,28,
        34,36,52,52,2,0,1,1,15,15,1,0,61,64,1,0,58,60,531,0,52,1,0,0,0,2,
        55,1,0,0,0,4,60,1,0,0,0,6,147,1,0,0,0,8,149,1,0,0,0,10,162,1,0,0,
        0,12,170,1,0,0,0,14,175,1,0,0,0,16,179,1,0,0,0,18,191,1,0,0,0,20,
        199,1,0,0,0,22,207,1,0,0,0,24,227,1,0,0,0,26,268,1,0,0,0,28,308,
        1,0,0,0,30,373,1,0,0,0,32,415,1,0,0,0,34,417,1,0,0,0,36,420,1,0,
        0,0,38,433,1,0,0,0,40,435,1,0,0,0,42,441,1,0,0,0,44,463,1,0,0,0,
        46,465,1,0,0,0,48,467,1,0,0,0,50,469,1,0,0,0,52,53,3,2,1,0,53,54,
        5,0,0,1,54,1,1,0,0,0,55,56,3,4,2,0,56,3,1,0,0,0,57,59,3,6,3,0,58,
        57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,64,1,0,0,
        0,62,60,1,0,0,0,63,65,3,12,6,0,64,63,1,0,0,0,64,65,1,0,0,0,65,5,
        1,0,0,0,66,148,5,1,0,0,67,68,3,18,9,0,68,69,5,2,0,0,69,70,3,22,11,
        0,70,148,1,0,0,0,71,148,3,30,15,0,72,148,3,14,7,0,73,148,5,3,0,0,
        74,75,5,4,0,0,75,148,5,57,0,0,76,77,5,5,0,0,77,78,3,4,2,0,78,79,
        5,6,0,0,79,148,1,0,0,0,80,81,5,7,0,0,81,82,3,24,12,0,82,83,5,5,0,
        0,83,84,3,4,2,0,84,85,5,6,0,0,85,148,1,0,0,0,86,87,5,8,0,0,87,88,
        3,4,2,0,88,89,5,9,0,0,89,90,3,24,12,0,90,148,1,0,0,0,91,92,5,10,
        0,0,92,93,3,24,12,0,93,94,5,11,0,0,94,102,3,4,2,0,95,96,5,12,0,0,
        96,97,3,24,12,0,97,98,5,11,0,0,98,99,3,4,2,0,99,101,1,0,0,0,100,
        95,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,107,
        1,0,0,0,104,102,1,0,0,0,105,106,5,13,0,0,106,108,3,4,2,0,107,105,
        1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,5,6,0,0,110,148,
        1,0,0,0,111,112,5,14,0,0,112,113,5,57,0,0,113,114,5,2,0,0,114,115,
        3,24,12,0,115,116,5,15,0,0,116,119,3,24,12,0,117,118,5,15,0,0,118,
        120,3,24,12,0,119,117,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,
        122,5,5,0,0,122,123,3,4,2,0,123,124,5,6,0,0,124,148,1,0,0,0,125,
        126,5,14,0,0,126,127,3,20,10,0,127,128,5,16,0,0,128,129,3,22,11,
        0,129,130,5,5,0,0,130,131,3,4,2,0,131,132,5,6,0,0,132,148,1,0,0,
        0,133,134,5,17,0,0,134,135,3,16,8,0,135,136,3,36,18,0,136,148,1,
        0,0,0,137,138,5,18,0,0,138,139,5,17,0,0,139,140,5,57,0,0,140,148,
        3,36,18,0,141,142,5,18,0,0,142,145,3,8,4,0,143,144,5,2,0,0,144,146,
        3,22,11,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,66,
        1,0,0,0,147,67,1,0,0,0,147,71,1,0,0,0,147,72,1,0,0,0,147,73,1,0,
        0,0,147,74,1,0,0,0,147,76,1,0,0,0,147,80,1,0,0,0,147,86,1,0,0,0,
        147,91,1,0,0,0,147,111,1,0,0,0,147,125,1,0,0,0,147,133,1,0,0,0,147,
        137,1,0,0,0,147,141,1,0,0,0,148,7,1,0,0,0,149,150,5,57,0,0,150,156,
        3,10,5,0,151,152,5,15,0,0,152,153,5,57,0,0,153,155,3,10,5,0,154,
        151,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,
        9,1,0,0,0,158,156,1,0,0,0,159,160,5,19,0,0,160,161,5,57,0,0,161,
        163,5,20,0,0,162,159,1,0,0,0,162,163,1,0,0,0,163,11,1,0,0,0,164,
        166,5,21,0,0,165,167,3,22,11,0,166,165,1,0,0,0,166,167,1,0,0,0,167,
        171,1,0,0,0,168,171,5,3,0,0,169,171,5,22,0,0,170,164,1,0,0,0,170,
        168,1,0,0,0,170,169,1,0,0,0,171,173,1,0,0,0,172,174,5,1,0,0,173,
        172,1,0,0,0,173,174,1,0,0,0,174,13,1,0,0,0,175,176,5,23,0,0,176,
        177,5,57,0,0,177,178,5,23,0,0,178,15,1,0,0,0,179,184,5,57,0,0,180,
        181,5,27,0,0,181,183,5,57,0,0,182,180,1,0,0,0,183,186,1,0,0,0,184,
        182,1,0,0,0,184,185,1,0,0,0,185,189,1,0,0,0,186,184,1,0,0,0,187,
        188,5,39,0,0,188,190,5,57,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,
        17,1,0,0,0,191,196,3,26,13,0,192,193,5,15,0,0,193,195,3,26,13,0,
        194,192,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,
        197,19,1,0,0,0,198,196,1,0,0,0,199,204,5,57,0,0,200,201,5,15,0,0,
        201,203,5,57,0,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,
        204,205,1,0,0,0,205,21,1,0,0,0,206,204,1,0,0,0,207,212,3,24,12,0,
        208,209,5,15,0,0,209,211,3,24,12,0,210,208,1,0,0,0,211,214,1,0,0,
        0,212,210,1,0,0,0,212,213,1,0,0,0,213,23,1,0,0,0,214,212,1,0,0,0,
        215,216,6,12,-1,0,216,228,5,24,0,0,217,228,5,25,0,0,218,228,5,26,
        0,0,219,228,3,48,24,0,220,228,3,50,25,0,221,228,5,55,0,0,222,228,
        3,34,17,0,223,228,3,28,14,0,224,228,3,40,20,0,225,226,7,0,0,0,226,
        228,3,24,12,8,227,215,1,0,0,0,227,217,1,0,0,0,227,218,1,0,0,0,227,
        219,1,0,0,0,227,220,1,0,0,0,227,221,1,0,0,0,227,222,1,0,0,0,227,
        223,1,0,0,0,227,224,1,0,0,0,227,225,1,0,0,0,228,255,1,0,0,0,229,
        230,10,9,0,0,230,231,5,53,0,0,231,254,3,24,12,9,232,233,10,7,0,0,
        233,234,7,1,0,0,234,254,3,24,12,8,235,236,10,6,0,0,236,237,7,2,0,
        0,237,254,3,24,12,7,238,239,10,5,0,0,239,240,5,51,0,0,240,254,3,
        24,12,5,241,242,10,4,0,0,242,243,7,3,0,0,243,254,3,24,12,5,244,245,
        10,3,0,0,245,246,5,42,0,0,246,254,3,24,12,4,247,248,10,2,0,0,248,
        249,5,43,0,0,249,254,3,24,12,3,250,251,10,1,0,0,251,252,7,4,0,0,
        252,254,3,24,12,2,253,229,1,0,0,0,253,232,1,0,0,0,253,235,1,0,0,
        0,253,238,1,0,0,0,253,241,1,0,0,0,253,244,1,0,0,0,253,247,1,0,0,
        0,253,250,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,
        0,256,25,1,0,0,0,257,255,1,0,0,0,258,269,5,57,0,0,259,266,3,28,14,
        0,260,261,5,48,0,0,261,262,3,24,12,0,262,263,5,49,0,0,263,267,1,
        0,0,0,264,265,5,27,0,0,265,267,5,57,0,0,266,260,1,0,0,0,266,264,
        1,0,0,0,267,269,1,0,0,0,268,258,1,0,0,0,268,259,1,0,0,0,269,27,1,
        0,0,0,270,279,5,57,0,0,271,272,5,48,0,0,272,273,3,24,12,0,273,274,
        5,49,0,0,274,278,1,0,0,0,275,276,5,27,0,0,276,278,5,57,0,0,277,271,
        1,0,0,0,277,275,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,
        1,0,0,0,280,309,1,0,0,0,281,279,1,0,0,0,282,291,3,30,15,0,283,284,
        5,48,0,0,284,285,3,24,12,0,285,286,5,49,0,0,286,290,1,0,0,0,287,
        288,5,27,0,0,288,290,5,57,0,0,289,283,1,0,0,0,289,287,1,0,0,0,290,
        293,1,0,0,0,291,289,1,0,0,0,291,292,1,0,0,0,292,309,1,0,0,0,293,
        291,1,0,0,0,294,295,5,31,0,0,295,296,3,24,12,0,296,305,5,32,0,0,
        297,298,5,48,0,0,298,299,3,24,12,0,299,300,5,49,0,0,300,304,1,0,
        0,0,301,302,5,27,0,0,302,304,5,57,0,0,303,297,1,0,0,0,303,301,1,
        0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,309,1,
        0,0,0,307,305,1,0,0,0,308,270,1,0,0,0,308,282,1,0,0,0,308,294,1,
        0,0,0,309,29,1,0,0,0,310,311,6,15,-1,0,311,320,5,57,0,0,312,313,
        5,48,0,0,313,314,3,24,12,0,314,315,5,49,0,0,315,319,1,0,0,0,316,
        317,5,27,0,0,317,319,5,57,0,0,318,312,1,0,0,0,318,316,1,0,0,0,319,
        322,1,0,0,0,320,318,1,0,0,0,320,321,1,0,0,0,321,323,1,0,0,0,322,
        320,1,0,0,0,323,374,3,32,16,0,324,325,5,31,0,0,325,326,3,24,12,0,
        326,335,5,32,0,0,327,328,5,48,0,0,328,329,3,24,12,0,329,330,5,49,
        0,0,330,334,1,0,0,0,331,332,5,27,0,0,332,334,5,57,0,0,333,327,1,
        0,0,0,333,331,1,0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,335,336,1,
        0,0,0,336,338,1,0,0,0,337,335,1,0,0,0,338,339,3,32,16,0,339,374,
        1,0,0,0,340,349,5,57,0,0,341,342,5,48,0,0,342,343,3,24,12,0,343,
        344,5,49,0,0,344,348,1,0,0,0,345,346,5,27,0,0,346,348,5,57,0,0,347,
        341,1,0,0,0,347,345,1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,0,349,
        350,1,0,0,0,350,352,1,0,0,0,351,349,1,0,0,0,352,353,5,39,0,0,353,
        354,5,57,0,0,354,374,3,32,16,0,355,356,5,31,0,0,356,357,3,24,12,
        0,357,366,5,32,0,0,358,359,5,48,0,0,359,360,3,24,12,0,360,361,5,
        49,0,0,361,365,1,0,0,0,362,363,5,27,0,0,363,365,5,57,0,0,364,358,
        1,0,0,0,364,362,1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,
        1,0,0,0,367,369,1,0,0,0,368,366,1,0,0,0,369,370,5,39,0,0,370,371,
        5,57,0,0,371,372,3,32,16,0,372,374,1,0,0,0,373,310,1,0,0,0,373,324,
        1,0,0,0,373,340,1,0,0,0,373,355,1,0,0,0,374,405,1,0,0,0,375,384,
        10,5,0,0,376,377,5,48,0,0,377,378,3,24,12,0,378,379,5,49,0,0,379,
        383,1,0,0,0,380,381,5,27,0,0,381,383,5,57,0,0,382,376,1,0,0,0,382,
        380,1,0,0,0,383,386,1,0,0,0,384,382,1,0,0,0,384,385,1,0,0,0,385,
        387,1,0,0,0,386,384,1,0,0,0,387,404,3,32,16,0,388,397,10,2,0,0,389,
        390,5,48,0,0,390,391,3,24,12,0,391,392,5,49,0,0,392,396,1,0,0,0,
        393,394,5,27,0,0,394,396,5,57,0,0,395,389,1,0,0,0,395,393,1,0,0,
        0,396,399,1,0,0,0,397,395,1,0,0,0,397,398,1,0,0,0,398,400,1,0,0,
        0,399,397,1,0,0,0,400,401,5,39,0,0,401,402,5,57,0,0,402,404,3,32,
        16,0,403,375,1,0,0,0,403,388,1,0,0,0,404,407,1,0,0,0,405,403,1,0,
        0,0,405,406,1,0,0,0,406,31,1,0,0,0,407,405,1,0,0,0,408,410,5,31,
        0,0,409,411,3,22,11,0,410,409,1,0,0,0,410,411,1,0,0,0,411,412,1,
        0,0,0,412,416,5,32,0,0,413,416,3,40,20,0,414,416,3,50,25,0,415,408,
        1,0,0,0,415,413,1,0,0,0,415,414,1,0,0,0,416,33,1,0,0,0,417,418,5,
        17,0,0,418,419,3,36,18,0,419,35,1,0,0,0,420,421,5,31,0,0,421,422,
        3,38,19,0,422,423,5,32,0,0,423,424,3,4,2,0,424,425,5,6,0,0,425,37,
        1,0,0,0,426,429,3,20,10,0,427,428,5,15,0,0,428,430,5,55,0,0,429,
        427,1,0,0,0,429,430,1,0,0,0,430,434,1,0,0,0,431,434,5,55,0,0,432,
        434,1,0,0,0,433,426,1,0,0,0,433,431,1,0,0,0,433,432,1,0,0,0,434,
        39,1,0,0,0,435,437,5,46,0,0,436,438,3,42,21,0,437,436,1,0,0,0,437,
        438,1,0,0,0,438,439,1,0,0,0,439,440,5,47,0,0,440,41,1,0,0,0,441,
        447,3,44,22,0,442,443,3,46,23,0,443,444,3,44,22,0,444,446,1,0,0,
        0,445,442,1,0,0,0,446,449,1,0,0,0,447,445,1,0,0,0,447,448,1,0,0,
        0,448,451,1,0,0,0,449,447,1,0,0,0,450,452,3,46,23,0,451,450,1,0,
        0,0,451,452,1,0,0,0,452,43,1,0,0,0,453,454,5,48,0,0,454,455,3,24,
        12,0,455,456,5,49,0,0,456,457,5,2,0,0,457,458,3,24,12,0,458,464,
        1,0,0,0,459,460,5,57,0,0,460,461,5,2,0,0,461,464,3,24,12,0,462,464,
        3,24,12,0,463,453,1,0,0,0,463,459,1,0,0,0,463,462,1,0,0,0,464,45,
        1,0,0,0,465,466,7,5,0,0,466,47,1,0,0,0,467,468,7,6,0,0,468,49,1,
        0,0,0,469,470,7,7,0,0,470,51,1,0,0,0,52,60,64,102,107,119,145,147,
        156,162,166,170,173,184,189,196,204,212,227,253,255,266,268,277,
        279,289,291,303,305,308,318,320,333,335,347,349,364,366,373,382,
        384,395,397,403,405,410,415,429,433,437,447,451,463
    ]

class LuaParser ( Parser ):

    grammarFileName = "LuaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'break'", "'goto'", "'do'", 
                     "'end'", "'while'", "'repeat'", "'until'", "'if'", 
                     "'then'", "'elseif'", "'else'", "'for'", "','", "'in'", 
                     "'function'", "'local'", "'<'", "'>'", "'return'", 
                     "'continue'", "'::'", "'nil'", "'false'", "'true'", 
                     "'.'", "'~'", "'-'", "'#'", "'('", "')'", "'not'", 
                     "'<<'", "'>>'", "'&'", "'//'", "'%'", "':'", "'<='", 
                     "'>='", "'and'", "'or'", "'+'", "'*'", "'{'", "'}'", 
                     "'['", "']'", "'=='", "'..'", "'|'", "'^'", "'/'", 
                     "'...'", "'~='" ]

    symbolicNames = [ "<INVALID>", "SEMI", "EQ", "BREAK", "GOTO", "DO", 
                      "END", "WHILE", "REPEAT", "UNTIL", "IF", "THEN", "ELSEIF", 
                      "ELSE", "FOR", "COMMA", "IN", "FUNCTION", "LOCAL", 
                      "LT", "GT", "RETURN", "CONTINUE", "CC", "NIL", "FALSE", 
                      "TRUE", "DOT", "SQUIG", "MINUS", "POUND", "OP", "CP", 
                      "NOT", "LL", "GG", "AMP", "SS", "PER", "COL", "LE", 
                      "GE", "AND", "OR", "PLUS", "STAR", "OCU", "CCU", "OB", 
                      "CB", "EE", "DD", "PIPE", "CARET", "SLASH", "DDD", 
                      "SQEQ", "NAME", "NORMALSTRING", "CHARSTRING", "LONGSTRING", 
                      "INT", "HEX", "FLOAT", "HEX_FLOAT", "COMMENT", "WS", 
                      "NL", "SHEBANG" ]

    RULE_start_ = 0
    RULE_chunk = 1
    RULE_block = 2
    RULE_stat = 3
    RULE_attnamelist = 4
    RULE_attrib = 5
    RULE_retstat = 6
    RULE_label = 7
    RULE_funcname = 8
    RULE_varlist = 9
    RULE_namelist = 10
    RULE_explist = 11
    RULE_exp = 12
    RULE_var = 13
    RULE_prefixexp = 14
    RULE_functioncall = 15
    RULE_args = 16
    RULE_functiondef = 17
    RULE_funcbody = 18
    RULE_parlist = 19
    RULE_tableconstructor = 20
    RULE_fieldlist = 21
    RULE_field = 22
    RULE_fieldsep = 23
    RULE_number = 24
    RULE_string = 25

    ruleNames =  [ "start_", "chunk", "block", "stat", "attnamelist", "attrib", 
                   "retstat", "label", "funcname", "varlist", "namelist", 
                   "explist", "exp", "var", "prefixexp", "functioncall", 
                   "args", "functiondef", "funcbody", "parlist", "tableconstructor", 
                   "fieldlist", "field", "fieldsep", "number", "string" ]

    EOF = Token.EOF
    SEMI=1
    EQ=2
    BREAK=3
    GOTO=4
    DO=5
    END=6
    WHILE=7
    REPEAT=8
    UNTIL=9
    IF=10
    THEN=11
    ELSEIF=12
    ELSE=13
    FOR=14
    COMMA=15
    IN=16
    FUNCTION=17
    LOCAL=18
    LT=19
    GT=20
    RETURN=21
    CONTINUE=22
    CC=23
    NIL=24
    FALSE=25
    TRUE=26
    DOT=27
    SQUIG=28
    MINUS=29
    POUND=30
    OP=31
    CP=32
    NOT=33
    LL=34
    GG=35
    AMP=36
    SS=37
    PER=38
    COL=39
    LE=40
    GE=41
    AND=42
    OR=43
    PLUS=44
    STAR=45
    OCU=46
    CCU=47
    OB=48
    CB=49
    EE=50
    DD=51
    PIPE=52
    CARET=53
    SLASH=54
    DDD=55
    SQEQ=56
    NAME=57
    NORMALSTRING=58
    CHARSTRING=59
    LONGSTRING=60
    INT=61
    HEX=62
    FLOAT=63
    HEX_FLOAT=64
    COMMENT=65
    WS=66
    NL=67
    SHEBANG=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chunk(self):
            return self.getTypedRuleContext(LuaParser.ChunkContext,0)


        def EOF(self):
            return self.getToken(LuaParser.EOF, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_start_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_" ):
                listener.enterStart_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_" ):
                listener.exitStart_(self)




    def start_(self):

        localctx = LuaParser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.chunk()
            self.state = 53
            self.match(LuaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChunkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


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
        self.enterRule(localctx, 2, self.RULE_chunk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.block()
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


        def retstat(self):
            return self.getTypedRuleContext(LuaParser.RetstatContext,0)


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
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.stat() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291464) != 0):
                self.state = 63
                self.retstat()


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

        def SEMI(self):
            return self.getToken(LuaParser.SEMI, 0)

        def varlist(self):
            return self.getTypedRuleContext(LuaParser.VarlistContext,0)


        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def label(self):
            return self.getTypedRuleContext(LuaParser.LabelContext,0)


        def BREAK(self):
            return self.getToken(LuaParser.BREAK, 0)

        def GOTO(self):
            return self.getToken(LuaParser.GOTO, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def DO(self):
            return self.getToken(LuaParser.DO, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.BlockContext)
            else:
                return self.getTypedRuleContext(LuaParser.BlockContext,i)


        def END(self):
            return self.getToken(LuaParser.END, 0)

        def WHILE(self):
            return self.getToken(LuaParser.WHILE, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def REPEAT(self):
            return self.getToken(LuaParser.REPEAT, 0)

        def UNTIL(self):
            return self.getToken(LuaParser.UNTIL, 0)

        def IF(self):
            return self.getToken(LuaParser.IF, 0)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.THEN)
            else:
                return self.getToken(LuaParser.THEN, i)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.ELSEIF)
            else:
                return self.getToken(LuaParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(LuaParser.ELSE, 0)

        def FOR(self):
            return self.getToken(LuaParser.FOR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def IN(self):
            return self.getToken(LuaParser.IN, 0)

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def funcname(self):
            return self.getTypedRuleContext(LuaParser.FuncnameContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def LOCAL(self):
            return self.getToken(LuaParser.LOCAL, 0)

        def attnamelist(self):
            return self.getTypedRuleContext(LuaParser.AttnamelistContext,0)


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
        self.enterRule(localctx, 6, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(LuaParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.varlist()
                self.state = 68
                self.match(LuaParser.EQ)
                self.state = 69
                self.explist()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.functioncall(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.match(LuaParser.GOTO)
                self.state = 75
                self.match(LuaParser.NAME)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 76
                self.match(LuaParser.DO)
                self.state = 77
                self.block()
                self.state = 78
                self.match(LuaParser.END)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.match(LuaParser.WHILE)
                self.state = 81
                self.exp(0)
                self.state = 82
                self.match(LuaParser.DO)
                self.state = 83
                self.block()
                self.state = 84
                self.match(LuaParser.END)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 86
                self.match(LuaParser.REPEAT)
                self.state = 87
                self.block()
                self.state = 88
                self.match(LuaParser.UNTIL)
                self.state = 89
                self.exp(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 91
                self.match(LuaParser.IF)
                self.state = 92
                self.exp(0)
                self.state = 93
                self.match(LuaParser.THEN)
                self.state = 94
                self.block()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 95
                    self.match(LuaParser.ELSEIF)
                    self.state = 96
                    self.exp(0)
                    self.state = 97
                    self.match(LuaParser.THEN)
                    self.state = 98
                    self.block()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 105
                    self.match(LuaParser.ELSE)
                    self.state = 106
                    self.block()


                self.state = 109
                self.match(LuaParser.END)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 111
                self.match(LuaParser.FOR)
                self.state = 112
                self.match(LuaParser.NAME)
                self.state = 113
                self.match(LuaParser.EQ)
                self.state = 114
                self.exp(0)
                self.state = 115
                self.match(LuaParser.COMMA)
                self.state = 116
                self.exp(0)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 117
                    self.match(LuaParser.COMMA)
                    self.state = 118
                    self.exp(0)


                self.state = 121
                self.match(LuaParser.DO)
                self.state = 122
                self.block()
                self.state = 123
                self.match(LuaParser.END)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 125
                self.match(LuaParser.FOR)
                self.state = 126
                self.namelist()
                self.state = 127
                self.match(LuaParser.IN)
                self.state = 128
                self.explist()
                self.state = 129
                self.match(LuaParser.DO)
                self.state = 130
                self.block()
                self.state = 131
                self.match(LuaParser.END)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 133
                self.match(LuaParser.FUNCTION)
                self.state = 134
                self.funcname()
                self.state = 135
                self.funcbody()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 137
                self.match(LuaParser.LOCAL)
                self.state = 138
                self.match(LuaParser.FUNCTION)
                self.state = 139
                self.match(LuaParser.NAME)
                self.state = 140
                self.funcbody()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 141
                self.match(LuaParser.LOCAL)
                self.state = 142
                self.attnamelist()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 143
                    self.match(LuaParser.EQ)
                    self.state = 144
                    self.explist()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttnamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def attrib(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.AttribContext)
            else:
                return self.getTypedRuleContext(LuaParser.AttribContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def getRuleIndex(self):
            return LuaParser.RULE_attnamelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttnamelist" ):
                listener.enterAttnamelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttnamelist" ):
                listener.exitAttnamelist(self)




    def attnamelist(self):

        localctx = LuaParser.AttnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attnamelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(LuaParser.NAME)
            self.state = 150
            self.attrib()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 151
                self.match(LuaParser.COMMA)
                self.state = 152
                self.match(LuaParser.NAME)
                self.state = 153
                self.attrib()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(LuaParser.LT, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def GT(self):
            return self.getToken(LuaParser.GT, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_attrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrib" ):
                listener.enterAttrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrib" ):
                listener.exitAttrib(self)




    def attrib(self):

        localctx = LuaParser.AttribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrib)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 159
                self.match(LuaParser.LT)
                self.state = 160
                self.match(LuaParser.NAME)
                self.state = 161
                self.match(LuaParser.GT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(LuaParser.RETURN, 0)

        def BREAK(self):
            return self.getToken(LuaParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(LuaParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(LuaParser.SEMI, 0)

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_retstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetstat" ):
                listener.enterRetstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetstat" ):
                listener.exitRetstat(self)




    def retstat(self):

        localctx = LuaParser.RetstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_retstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 164
                self.match(LuaParser.RETURN)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 165
                    self.explist()


                pass
            elif token in [3]:
                self.state = 168
                self.match(LuaParser.BREAK)
                pass
            elif token in [22]:
                self.state = 169
                self.match(LuaParser.CONTINUE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 172
                self.match(LuaParser.SEMI)


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

        def CC(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.CC)
            else:
                return self.getToken(LuaParser.CC, i)

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
        self.enterRule(localctx, 14, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LuaParser.CC)
            self.state = 176
            self.match(LuaParser.NAME)
            self.state = 177
            self.match(LuaParser.CC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncnameContext(ParserRuleContext):
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

        def COL(self):
            return self.getToken(LuaParser.COL, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_funcname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncname" ):
                listener.enterFuncname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncname" ):
                listener.exitFuncname(self)




    def funcname(self):

        localctx = LuaParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(LuaParser.NAME)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 180
                self.match(LuaParser.DOT)
                self.state = 181
                self.match(LuaParser.NAME)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 187
                self.match(LuaParser.COL)
                self.state = 188
                self.match(LuaParser.NAME)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
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
            return LuaParser.RULE_varlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarlist" ):
                listener.enterVarlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarlist" ):
                listener.exitVarlist(self)




    def varlist(self):

        localctx = LuaParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.var()
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 192
                self.match(LuaParser.COMMA)
                self.state = 193
                self.var()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamelistContext(ParserRuleContext):
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
            return LuaParser.RULE_namelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamelist" ):
                listener.enterNamelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamelist" ):
                listener.exitNamelist(self)




    def namelist(self):

        localctx = LuaParser.NamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_namelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(LuaParser.NAME)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    self.match(LuaParser.COMMA)
                    self.state = 201
                    self.match(LuaParser.NAME) 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.COMMA)
            else:
                return self.getToken(LuaParser.COMMA, i)

        def getRuleIndex(self):
            return LuaParser.RULE_explist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplist" ):
                listener.enterExplist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplist" ):
                listener.exitExplist(self)




    def explist(self):

        localctx = LuaParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.exp(0)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 208
                self.match(LuaParser.COMMA)
                self.state = 209
                self.exp(0)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(LuaParser.NIL, 0)

        def FALSE(self):
            return self.getToken(LuaParser.FALSE, 0)

        def TRUE(self):
            return self.getToken(LuaParser.TRUE, 0)

        def number(self):
            return self.getTypedRuleContext(LuaParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def DDD(self):
            return self.getToken(LuaParser.DDD, 0)

        def functiondef(self):
            return self.getTypedRuleContext(LuaParser.FunctiondefContext,0)


        def prefixexp(self):
            return self.getTypedRuleContext(LuaParser.PrefixexpContext,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def NOT(self):
            return self.getToken(LuaParser.NOT, 0)

        def POUND(self):
            return self.getToken(LuaParser.POUND, 0)

        def MINUS(self):
            return self.getToken(LuaParser.MINUS, 0)

        def SQUIG(self):
            return self.getToken(LuaParser.SQUIG, 0)

        def CARET(self):
            return self.getToken(LuaParser.CARET, 0)

        def STAR(self):
            return self.getToken(LuaParser.STAR, 0)

        def SLASH(self):
            return self.getToken(LuaParser.SLASH, 0)

        def PER(self):
            return self.getToken(LuaParser.PER, 0)

        def SS(self):
            return self.getToken(LuaParser.SS, 0)

        def PLUS(self):
            return self.getToken(LuaParser.PLUS, 0)

        def DD(self):
            return self.getToken(LuaParser.DD, 0)

        def LT(self):
            return self.getToken(LuaParser.LT, 0)

        def GT(self):
            return self.getToken(LuaParser.GT, 0)

        def LE(self):
            return self.getToken(LuaParser.LE, 0)

        def GE(self):
            return self.getToken(LuaParser.GE, 0)

        def SQEQ(self):
            return self.getToken(LuaParser.SQEQ, 0)

        def EE(self):
            return self.getToken(LuaParser.EE, 0)

        def AND(self):
            return self.getToken(LuaParser.AND, 0)

        def OR(self):
            return self.getToken(LuaParser.OR, 0)

        def AMP(self):
            return self.getToken(LuaParser.AMP, 0)

        def PIPE(self):
            return self.getToken(LuaParser.PIPE, 0)

        def LL(self):
            return self.getToken(LuaParser.LL, 0)

        def GG(self):
            return self.getToken(LuaParser.GG, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 216
                self.match(LuaParser.NIL)
                pass
            elif token in [25]:
                self.state = 217
                self.match(LuaParser.FALSE)
                pass
            elif token in [26]:
                self.state = 218
                self.match(LuaParser.TRUE)
                pass
            elif token in [61, 62, 63, 64]:
                self.state = 219
                self.number()
                pass
            elif token in [58, 59, 60]:
                self.state = 220
                self.string()
                pass
            elif token in [55]:
                self.state = 221
                self.match(LuaParser.DDD)
                pass
            elif token in [17]:
                self.state = 222
                self.functiondef()
                pass
            elif token in [31, 57]:
                self.state = 223
                self.prefixexp()
                pass
            elif token in [46]:
                self.state = 224
                self.tableconstructor()
                pass
            elif token in [28, 29, 30, 33]:
                self.state = 225
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10468982784) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.exp(8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 253
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 229
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")

                        self.state = 230
                        self.match(LuaParser.CARET)
                        self.state = 231
                        self.exp(9)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 232
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 233
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18049995198431232) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 234
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 235
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 236
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==44):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 237
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 238
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 239
                        self.match(LuaParser.DD)
                        self.state = 240
                        self.exp(5)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 241
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 242
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 73186792481226752) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 243
                        self.exp(5)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 244
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 245
                        self.match(LuaParser.AND)
                        self.state = 246
                        self.exp(4)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 247
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 248
                        self.match(LuaParser.OR)
                        self.state = 249
                        self.exp(3)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 250
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 251
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503720154890240) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 252
                        self.exp(2)
                        pass

             
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def prefixexp(self):
            return self.getTypedRuleContext(LuaParser.PrefixexpContext,0)


        def OB(self):
            return self.getToken(LuaParser.OB, 0)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def CB(self):
            return self.getToken(LuaParser.CB, 0)

        def DOT(self):
            return self.getToken(LuaParser.DOT, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = LuaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.prefixexp()
                self.state = 266
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [48]:
                    self.state = 260
                    self.match(LuaParser.OB)
                    self.state = 261
                    self.exp(0)
                    self.state = 262
                    self.match(LuaParser.CB)
                    pass
                elif token in [27]:
                    self.state = 264
                    self.match(LuaParser.DOT)
                    self.state = 265
                    self.match(LuaParser.NAME)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrefixexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def OB(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.OB)
            else:
                return self.getToken(LuaParser.OB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def CB(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.CB)
            else:
                return self.getToken(LuaParser.CB, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.DOT)
            else:
                return self.getToken(LuaParser.DOT, i)

        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def OP(self):
            return self.getToken(LuaParser.OP, 0)

        def CP(self):
            return self.getToken(LuaParser.CP, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_prefixexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixexp" ):
                listener.enterPrefixexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixexp" ):
                listener.exitPrefixexp(self)




    def prefixexp(self):

        localctx = LuaParser.PrefixexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_prefixexp)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(LuaParser.NAME)
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 277
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [48]:
                            self.state = 271
                            self.match(LuaParser.OB)
                            self.state = 272
                            self.exp(0)
                            self.state = 273
                            self.match(LuaParser.CB)
                            pass
                        elif token in [27]:
                            self.state = 275
                            self.match(LuaParser.DOT)
                            self.state = 276
                            self.match(LuaParser.NAME)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 281
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.functioncall(0)
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 289
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [48]:
                            self.state = 283
                            self.match(LuaParser.OB)
                            self.state = 284
                            self.exp(0)
                            self.state = 285
                            self.match(LuaParser.CB)
                            pass
                        elif token in [27]:
                            self.state = 287
                            self.match(LuaParser.DOT)
                            self.state = 288
                            self.match(LuaParser.NAME)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 293
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.match(LuaParser.OP)
                self.state = 295
                self.exp(0)
                self.state = 296
                self.match(LuaParser.CP)
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 303
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [48]:
                            self.state = 297
                            self.match(LuaParser.OB)
                            self.state = 298
                            self.exp(0)
                            self.state = 299
                            self.match(LuaParser.CB)
                            pass
                        elif token in [27]:
                            self.state = 301
                            self.match(LuaParser.DOT)
                            self.state = 302
                            self.match(LuaParser.NAME)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 307
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


        def OB(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.OB)
            else:
                return self.getToken(LuaParser.OB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def CB(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.CB)
            else:
                return self.getToken(LuaParser.CB, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.DOT)
            else:
                return self.getToken(LuaParser.DOT, i)

        def OP(self):
            return self.getToken(LuaParser.OP, 0)

        def CP(self):
            return self.getToken(LuaParser.CP, 0)

        def COL(self):
            return self.getToken(LuaParser.COL, 0)

        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)



    def functioncall(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.FunctioncallContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_functioncall, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 311
                self.match(LuaParser.NAME)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 318
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [48]:
                        self.state = 312
                        self.match(LuaParser.OB)
                        self.state = 313
                        self.exp(0)
                        self.state = 314
                        self.match(LuaParser.CB)
                        pass
                    elif token in [27]:
                        self.state = 316
                        self.match(LuaParser.DOT)
                        self.state = 317
                        self.match(LuaParser.NAME)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 322
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 323
                self.args()
                pass

            elif la_ == 2:
                self.state = 324
                self.match(LuaParser.OP)
                self.state = 325
                self.exp(0)
                self.state = 326
                self.match(LuaParser.CP)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 333
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [48]:
                        self.state = 327
                        self.match(LuaParser.OB)
                        self.state = 328
                        self.exp(0)
                        self.state = 329
                        self.match(LuaParser.CB)
                        pass
                    elif token in [27]:
                        self.state = 331
                        self.match(LuaParser.DOT)
                        self.state = 332
                        self.match(LuaParser.NAME)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 338
                self.args()
                pass

            elif la_ == 3:
                self.state = 340
                self.match(LuaParser.NAME)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 347
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [48]:
                        self.state = 341
                        self.match(LuaParser.OB)
                        self.state = 342
                        self.exp(0)
                        self.state = 343
                        self.match(LuaParser.CB)
                        pass
                    elif token in [27]:
                        self.state = 345
                        self.match(LuaParser.DOT)
                        self.state = 346
                        self.match(LuaParser.NAME)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 352
                self.match(LuaParser.COL)
                self.state = 353
                self.match(LuaParser.NAME)
                self.state = 354
                self.args()
                pass

            elif la_ == 4:
                self.state = 355
                self.match(LuaParser.OP)
                self.state = 356
                self.exp(0)
                self.state = 357
                self.match(LuaParser.CP)
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 364
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [48]:
                        self.state = 358
                        self.match(LuaParser.OB)
                        self.state = 359
                        self.exp(0)
                        self.state = 360
                        self.match(LuaParser.CB)
                        pass
                    elif token in [27]:
                        self.state = 362
                        self.match(LuaParser.DOT)
                        self.state = 363
                        self.match(LuaParser.NAME)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 368
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 369
                self.match(LuaParser.COL)
                self.state = 370
                self.match(LuaParser.NAME)
                self.state = 371
                self.args()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 403
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.FunctioncallContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 375
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 384
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27 or _la==48:
                            self.state = 382
                            self._errHandler.sync(self)
                            token = self._input.LA(1)
                            if token in [48]:
                                self.state = 376
                                self.match(LuaParser.OB)
                                self.state = 377
                                self.exp(0)
                                self.state = 378
                                self.match(LuaParser.CB)
                                pass
                            elif token in [27]:
                                self.state = 380
                                self.match(LuaParser.DOT)
                                self.state = 381
                                self.match(LuaParser.NAME)
                                pass
                            else:
                                raise NoViableAltException(self)

                            self.state = 386
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 387
                        self.args()
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.FunctioncallContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 388
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 397
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27 or _la==48:
                            self.state = 395
                            self._errHandler.sync(self)
                            token = self._input.LA(1)
                            if token in [48]:
                                self.state = 389
                                self.match(LuaParser.OB)
                                self.state = 390
                                self.exp(0)
                                self.state = 391
                                self.match(LuaParser.CB)
                                pass
                            elif token in [27]:
                                self.state = 393
                                self.match(LuaParser.DOT)
                                self.state = 394
                                self.match(LuaParser.NAME)
                                pass
                            else:
                                raise NoViableAltException(self)

                            self.state = 399
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 400
                        self.match(LuaParser.COL)
                        self.state = 401
                        self.match(LuaParser.NAME)
                        self.state = 402
                        self.args()
                        pass

             
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(LuaParser.OP, 0)

        def CP(self):
            return self.getToken(LuaParser.CP, 0)

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = LuaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(LuaParser.OP)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 409
                    self.explist()


                self.state = 412
                self.match(LuaParser.CP)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.tableconstructor()
                pass
            elif token in [58, 59, 60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.string()
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


    class FunctiondefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_functiondef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctiondef" ):
                listener.enterFunctiondef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctiondef" ):
                listener.exitFunctiondef(self)




    def functiondef(self):

        localctx = LuaParser.FunctiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(LuaParser.FUNCTION)
            self.state = 418
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(LuaParser.OP, 0)

        def parlist(self):
            return self.getTypedRuleContext(LuaParser.ParlistContext,0)


        def CP(self):
            return self.getToken(LuaParser.CP, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def END(self):
            return self.getToken(LuaParser.END, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_funcbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncbody" ):
                listener.enterFuncbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncbody" ):
                listener.exitFuncbody(self)




    def funcbody(self):

        localctx = LuaParser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(LuaParser.OP)
            self.state = 421
            self.parlist()
            self.state = 422
            self.match(LuaParser.CP)
            self.state = 423
            self.block()
            self.state = 424
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def COMMA(self):
            return self.getToken(LuaParser.COMMA, 0)

        def DDD(self):
            return self.getToken(LuaParser.DDD, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_parlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParlist" ):
                listener.enterParlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParlist" ):
                listener.exitParlist(self)




    def parlist(self):

        localctx = LuaParser.ParlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.namelist()
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 427
                    self.match(LuaParser.COMMA)
                    self.state = 428
                    self.match(LuaParser.DDD)


                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(LuaParser.DDD)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)

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


    class TableconstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCU(self):
            return self.getToken(LuaParser.OCU, 0)

        def CCU(self):
            return self.getToken(LuaParser.CCU, 0)

        def fieldlist(self):
            return self.getTypedRuleContext(LuaParser.FieldlistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_tableconstructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableconstructor" ):
                listener.enterTableconstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableconstructor" ):
                listener.exitTableconstructor(self)




    def tableconstructor(self):

        localctx = LuaParser.TableconstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(LuaParser.OCU)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280653027441537) != 0):
                self.state = 436
                self.fieldlist()


            self.state = 439
            self.match(LuaParser.CCU)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldContext,i)


        def fieldsep(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.FieldsepContext)
            else:
                return self.getTypedRuleContext(LuaParser.FieldsepContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_fieldlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldlist" ):
                listener.enterFieldlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldlist" ):
                listener.exitFieldlist(self)




    def fieldlist(self):

        localctx = LuaParser.FieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.field()
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 442
                    self.fieldsep()
                    self.state = 443
                    self.field() 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==15:
                self.state = 450
                self.fieldsep()


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

        def OB(self):
            return self.getToken(LuaParser.OB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def CB(self):
            return self.getToken(LuaParser.CB, 0)

        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)

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
        self.enterRule(localctx, 44, self.RULE_field)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(LuaParser.OB)
                self.state = 454
                self.exp(0)
                self.state = 455
                self.match(LuaParser.CB)
                self.state = 456
                self.match(LuaParser.EQ)
                self.state = 457
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.match(LuaParser.NAME)
                self.state = 460
                self.match(LuaParser.EQ)
                self.state = 461
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.exp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldsepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(LuaParser.COMMA, 0)

        def SEMI(self):
            return self.getToken(LuaParser.SEMI, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_fieldsep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldsep" ):
                listener.enterFieldsep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldsep" ):
                listener.exitFieldsep(self)




    def fieldsep(self):

        localctx = LuaParser.FieldsepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            _la = self._input.LA(1)
            if not(_la==1 or _la==15):
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LuaParser.INT, 0)

        def HEX(self):
            return self.getToken(LuaParser.HEX, 0)

        def FLOAT(self):
            return self.getToken(LuaParser.FLOAT, 0)

        def HEX_FLOAT(self):
            return self.getToken(LuaParser.HEX_FLOAT, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = LuaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & 15) != 0)):
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


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORMALSTRING(self):
            return self.getToken(LuaParser.NORMALSTRING, 0)

        def CHARSTRING(self):
            return self.getToken(LuaParser.CHARSTRING, 0)

        def LONGSTRING(self):
            return self.getToken(LuaParser.LONGSTRING, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = LuaParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2017612633061982208) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.exp_sempred
        self._predicates[15] = self.functioncall_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def functioncall_sempred(self, localctx:FunctioncallContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




