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
        4,1,69,443,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,1,1,1,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,
        2,3,2,69,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,5,3,105,8,3,10,3,12,3,108,9,3,1,3,1,3,3,3,112,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,124,8,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,150,8,3,3,3,152,8,3,1,4,1,4,1,4,5,4,
        157,8,4,10,4,12,4,160,9,4,1,5,1,5,3,5,164,8,5,1,6,1,6,1,6,1,6,1,
        7,1,7,3,7,172,8,7,1,7,1,7,3,7,176,8,7,1,7,3,7,179,8,7,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,5,9,188,8,9,10,9,12,9,191,9,9,1,9,1,9,3,9,195,
        8,9,1,10,1,10,1,10,5,10,200,8,10,10,10,12,10,203,9,10,1,11,1,11,
        1,11,5,11,208,8,11,10,11,12,11,211,9,11,1,12,1,12,1,12,5,12,216,
        8,12,10,12,12,12,219,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,3,13,233,8,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,268,8,13,10,13,12,13,271,9,13,1,14,1,14,1,14,1,14,3,14,
        277,8,14,1,15,1,15,5,15,281,8,15,10,15,12,15,284,9,15,1,15,1,15,
        5,15,288,8,15,10,15,12,15,291,9,15,1,15,1,15,1,15,1,15,5,15,297,
        8,15,10,15,12,15,300,9,15,3,15,302,8,15,1,16,1,16,1,16,5,16,307,
        8,16,10,16,12,16,310,9,16,1,16,1,16,1,16,1,16,1,16,5,16,317,8,16,
        10,16,12,16,320,9,16,1,16,1,16,1,16,1,16,5,16,326,8,16,10,16,12,
        16,329,9,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,338,8,16,10,
        16,12,16,341,9,16,1,16,1,16,1,16,1,16,3,16,347,8,16,1,16,1,16,5,
        16,351,8,16,10,16,12,16,354,9,16,1,16,1,16,1,16,5,16,359,8,16,10,
        16,12,16,362,9,16,1,16,1,16,1,16,5,16,367,8,16,10,16,12,16,370,9,
        16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,378,8,17,1,18,1,18,3,18,382,
        8,18,1,18,1,18,1,18,3,18,387,8,18,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,3,21,401,8,21,1,21,1,21,3,21,405,8,
        21,1,22,1,22,3,22,409,8,22,1,22,1,22,1,23,1,23,1,23,1,23,5,23,417,
        8,23,10,23,12,23,420,9,23,1,23,3,23,423,8,23,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,3,24,435,8,24,1,25,1,25,1,26,1,26,
        1,27,1,27,1,27,0,2,26,32,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,8,2,0,28,30,33,33,3,
        0,37,38,45,45,54,54,2,0,29,29,44,44,1,0,34,35,4,0,19,20,40,41,50,
        50,56,56,2,0,1,1,15,15,1,0,61,64,1,0,58,60,494,0,56,1,0,0,0,2,59,
        1,0,0,0,4,64,1,0,0,0,6,151,1,0,0,0,8,153,1,0,0,0,10,161,1,0,0,0,
        12,165,1,0,0,0,14,175,1,0,0,0,16,180,1,0,0,0,18,184,1,0,0,0,20,196,
        1,0,0,0,22,204,1,0,0,0,24,212,1,0,0,0,26,232,1,0,0,0,28,276,1,0,
        0,0,30,301,1,0,0,0,32,346,1,0,0,0,34,377,1,0,0,0,36,386,1,0,0,0,
        38,388,1,0,0,0,40,391,1,0,0,0,42,404,1,0,0,0,44,406,1,0,0,0,46,412,
        1,0,0,0,48,434,1,0,0,0,50,436,1,0,0,0,52,438,1,0,0,0,54,440,1,0,
        0,0,56,57,3,2,1,0,57,58,5,0,0,1,58,1,1,0,0,0,59,60,3,4,2,0,60,3,
        1,0,0,0,61,63,3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,
        64,65,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,67,69,3,14,7,0,68,67,1,
        0,0,0,68,69,1,0,0,0,69,5,1,0,0,0,70,152,5,1,0,0,71,72,3,20,10,0,
        72,73,5,2,0,0,73,74,3,24,12,0,74,152,1,0,0,0,75,152,3,32,16,0,76,
        152,3,16,8,0,77,152,5,3,0,0,78,79,5,4,0,0,79,152,5,57,0,0,80,81,
        5,5,0,0,81,82,3,4,2,0,82,83,5,6,0,0,83,152,1,0,0,0,84,85,5,7,0,0,
        85,86,3,26,13,0,86,87,5,5,0,0,87,88,3,4,2,0,88,89,5,6,0,0,89,152,
        1,0,0,0,90,91,5,8,0,0,91,92,3,4,2,0,92,93,5,9,0,0,93,94,3,26,13,
        0,94,152,1,0,0,0,95,96,5,10,0,0,96,97,3,26,13,0,97,98,5,11,0,0,98,
        106,3,4,2,0,99,100,5,12,0,0,100,101,3,26,13,0,101,102,5,11,0,0,102,
        103,3,4,2,0,103,105,1,0,0,0,104,99,1,0,0,0,105,108,1,0,0,0,106,104,
        1,0,0,0,106,107,1,0,0,0,107,111,1,0,0,0,108,106,1,0,0,0,109,110,
        5,13,0,0,110,112,3,4,2,0,111,109,1,0,0,0,111,112,1,0,0,0,112,113,
        1,0,0,0,113,114,5,6,0,0,114,152,1,0,0,0,115,116,5,14,0,0,116,117,
        5,57,0,0,117,118,5,2,0,0,118,119,3,26,13,0,119,120,5,15,0,0,120,
        123,3,26,13,0,121,122,5,15,0,0,122,124,3,26,13,0,123,121,1,0,0,0,
        123,124,1,0,0,0,124,125,1,0,0,0,125,126,5,5,0,0,126,127,3,4,2,0,
        127,128,5,6,0,0,128,152,1,0,0,0,129,130,5,14,0,0,130,131,3,22,11,
        0,131,132,5,16,0,0,132,133,3,24,12,0,133,134,5,5,0,0,134,135,3,4,
        2,0,135,136,5,6,0,0,136,152,1,0,0,0,137,138,5,17,0,0,138,139,3,18,
        9,0,139,140,3,40,20,0,140,152,1,0,0,0,141,142,5,18,0,0,142,143,5,
        17,0,0,143,144,5,57,0,0,144,152,3,40,20,0,145,146,5,18,0,0,146,149,
        3,8,4,0,147,148,5,2,0,0,148,150,3,24,12,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,152,1,0,0,0,151,70,1,0,0,0,151,71,1,0,0,0,151,75,1,0,
        0,0,151,76,1,0,0,0,151,77,1,0,0,0,151,78,1,0,0,0,151,80,1,0,0,0,
        151,84,1,0,0,0,151,90,1,0,0,0,151,95,1,0,0,0,151,115,1,0,0,0,151,
        129,1,0,0,0,151,137,1,0,0,0,151,141,1,0,0,0,151,145,1,0,0,0,152,
        7,1,0,0,0,153,158,3,10,5,0,154,155,5,15,0,0,155,157,3,10,5,0,156,
        154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,
        9,1,0,0,0,160,158,1,0,0,0,161,163,5,57,0,0,162,164,3,12,6,0,163,
        162,1,0,0,0,163,164,1,0,0,0,164,11,1,0,0,0,165,166,5,19,0,0,166,
        167,5,57,0,0,167,168,5,20,0,0,168,13,1,0,0,0,169,171,5,21,0,0,170,
        172,3,24,12,0,171,170,1,0,0,0,171,172,1,0,0,0,172,176,1,0,0,0,173,
        176,5,3,0,0,174,176,5,22,0,0,175,169,1,0,0,0,175,173,1,0,0,0,175,
        174,1,0,0,0,176,178,1,0,0,0,177,179,5,1,0,0,178,177,1,0,0,0,178,
        179,1,0,0,0,179,15,1,0,0,0,180,181,5,23,0,0,181,182,5,57,0,0,182,
        183,5,23,0,0,183,17,1,0,0,0,184,189,5,57,0,0,185,186,5,27,0,0,186,
        188,5,57,0,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,
        190,1,0,0,0,190,194,1,0,0,0,191,189,1,0,0,0,192,193,5,39,0,0,193,
        195,5,57,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,19,1,0,0,0,196,
        201,3,28,14,0,197,198,5,15,0,0,198,200,3,28,14,0,199,197,1,0,0,0,
        200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,21,1,0,0,0,203,
        201,1,0,0,0,204,209,5,57,0,0,205,206,5,15,0,0,206,208,5,57,0,0,207,
        205,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,
        23,1,0,0,0,211,209,1,0,0,0,212,217,3,26,13,0,213,214,5,15,0,0,214,
        216,3,26,13,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,
        218,1,0,0,0,218,25,1,0,0,0,219,217,1,0,0,0,220,221,6,13,-1,0,221,
        233,5,24,0,0,222,233,5,25,0,0,223,233,5,26,0,0,224,233,3,52,26,0,
        225,233,3,54,27,0,226,233,5,55,0,0,227,233,3,38,19,0,228,233,3,30,
        15,0,229,233,3,44,22,0,230,231,7,0,0,0,231,233,3,26,13,11,232,220,
        1,0,0,0,232,222,1,0,0,0,232,223,1,0,0,0,232,224,1,0,0,0,232,225,
        1,0,0,0,232,226,1,0,0,0,232,227,1,0,0,0,232,228,1,0,0,0,232,229,
        1,0,0,0,232,230,1,0,0,0,233,269,1,0,0,0,234,235,10,12,0,0,235,236,
        5,53,0,0,236,268,3,26,13,12,237,238,10,10,0,0,238,239,7,1,0,0,239,
        268,3,26,13,11,240,241,10,9,0,0,241,242,7,2,0,0,242,268,3,26,13,
        10,243,244,10,8,0,0,244,245,5,51,0,0,245,268,3,26,13,8,246,247,10,
        7,0,0,247,248,7,3,0,0,248,268,3,26,13,8,249,250,10,6,0,0,250,251,
        5,36,0,0,251,268,3,26,13,7,252,253,10,5,0,0,253,254,5,28,0,0,254,
        268,3,26,13,6,255,256,10,4,0,0,256,257,5,52,0,0,257,268,3,26,13,
        5,258,259,10,3,0,0,259,260,7,4,0,0,260,268,3,26,13,4,261,262,10,
        2,0,0,262,263,5,42,0,0,263,268,3,26,13,3,264,265,10,1,0,0,265,266,
        5,43,0,0,266,268,3,26,13,2,267,234,1,0,0,0,267,237,1,0,0,0,267,240,
        1,0,0,0,267,243,1,0,0,0,267,246,1,0,0,0,267,249,1,0,0,0,267,252,
        1,0,0,0,267,255,1,0,0,0,267,258,1,0,0,0,267,261,1,0,0,0,267,264,
        1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,27,1,
        0,0,0,271,269,1,0,0,0,272,277,5,57,0,0,273,274,3,30,15,0,274,275,
        3,34,17,0,275,277,1,0,0,0,276,272,1,0,0,0,276,273,1,0,0,0,277,29,
        1,0,0,0,278,282,5,57,0,0,279,281,3,34,17,0,280,279,1,0,0,0,281,284,
        1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,302,1,0,0,0,284,282,
        1,0,0,0,285,289,3,32,16,0,286,288,3,34,17,0,287,286,1,0,0,0,288,
        291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,302,1,0,0,0,291,
        289,1,0,0,0,292,293,5,31,0,0,293,294,3,26,13,0,294,298,5,32,0,0,
        295,297,3,34,17,0,296,295,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,
        0,298,299,1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,301,278,1,0,0,
        0,301,285,1,0,0,0,301,292,1,0,0,0,302,31,1,0,0,0,303,304,6,16,-1,
        0,304,308,5,57,0,0,305,307,3,34,17,0,306,305,1,0,0,0,307,310,1,0,
        0,0,308,306,1,0,0,0,308,309,1,0,0,0,309,311,1,0,0,0,310,308,1,0,
        0,0,311,347,3,36,18,0,312,313,5,31,0,0,313,314,3,26,13,0,314,318,
        5,32,0,0,315,317,3,34,17,0,316,315,1,0,0,0,317,320,1,0,0,0,318,316,
        1,0,0,0,318,319,1,0,0,0,319,321,1,0,0,0,320,318,1,0,0,0,321,322,
        3,36,18,0,322,347,1,0,0,0,323,327,5,57,0,0,324,326,3,34,17,0,325,
        324,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,
        330,1,0,0,0,329,327,1,0,0,0,330,331,5,39,0,0,331,332,5,57,0,0,332,
        347,3,36,18,0,333,334,5,31,0,0,334,335,3,26,13,0,335,339,5,32,0,
        0,336,338,3,34,17,0,337,336,1,0,0,0,338,341,1,0,0,0,339,337,1,0,
        0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,339,1,0,0,0,342,343,5,39,
        0,0,343,344,5,57,0,0,344,345,3,36,18,0,345,347,1,0,0,0,346,303,1,
        0,0,0,346,312,1,0,0,0,346,323,1,0,0,0,346,333,1,0,0,0,347,368,1,
        0,0,0,348,352,10,5,0,0,349,351,3,34,17,0,350,349,1,0,0,0,351,354,
        1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,0,354,352,
        1,0,0,0,355,367,3,36,18,0,356,360,10,2,0,0,357,359,3,34,17,0,358,
        357,1,0,0,0,359,362,1,0,0,0,360,358,1,0,0,0,360,361,1,0,0,0,361,
        363,1,0,0,0,362,360,1,0,0,0,363,364,5,39,0,0,364,365,5,57,0,0,365,
        367,3,36,18,0,366,348,1,0,0,0,366,356,1,0,0,0,367,370,1,0,0,0,368,
        366,1,0,0,0,368,369,1,0,0,0,369,33,1,0,0,0,370,368,1,0,0,0,371,372,
        5,48,0,0,372,373,3,26,13,0,373,374,5,49,0,0,374,378,1,0,0,0,375,
        376,5,27,0,0,376,378,5,57,0,0,377,371,1,0,0,0,377,375,1,0,0,0,378,
        35,1,0,0,0,379,381,5,31,0,0,380,382,3,24,12,0,381,380,1,0,0,0,381,
        382,1,0,0,0,382,383,1,0,0,0,383,387,5,32,0,0,384,387,3,44,22,0,385,
        387,3,54,27,0,386,379,1,0,0,0,386,384,1,0,0,0,386,385,1,0,0,0,387,
        37,1,0,0,0,388,389,5,17,0,0,389,390,3,40,20,0,390,39,1,0,0,0,391,
        392,5,31,0,0,392,393,3,42,21,0,393,394,5,32,0,0,394,395,3,4,2,0,
        395,396,5,6,0,0,396,41,1,0,0,0,397,400,3,22,11,0,398,399,5,15,0,
        0,399,401,5,55,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,405,1,0,0,
        0,402,405,5,55,0,0,403,405,1,0,0,0,404,397,1,0,0,0,404,402,1,0,0,
        0,404,403,1,0,0,0,405,43,1,0,0,0,406,408,5,46,0,0,407,409,3,46,23,
        0,408,407,1,0,0,0,408,409,1,0,0,0,409,410,1,0,0,0,410,411,5,47,0,
        0,411,45,1,0,0,0,412,418,3,48,24,0,413,414,3,50,25,0,414,415,3,48,
        24,0,415,417,1,0,0,0,416,413,1,0,0,0,417,420,1,0,0,0,418,416,1,0,
        0,0,418,419,1,0,0,0,419,422,1,0,0,0,420,418,1,0,0,0,421,423,3,50,
        25,0,422,421,1,0,0,0,422,423,1,0,0,0,423,47,1,0,0,0,424,425,5,48,
        0,0,425,426,3,26,13,0,426,427,5,49,0,0,427,428,5,2,0,0,428,429,3,
        26,13,0,429,435,1,0,0,0,430,431,5,57,0,0,431,432,5,2,0,0,432,435,
        3,26,13,0,433,435,3,26,13,0,434,424,1,0,0,0,434,430,1,0,0,0,434,
        433,1,0,0,0,435,49,1,0,0,0,436,437,7,5,0,0,437,51,1,0,0,0,438,439,
        7,6,0,0,439,53,1,0,0,0,440,441,7,7,0,0,441,55,1,0,0,0,43,64,68,106,
        111,123,149,151,158,163,171,175,178,189,194,201,209,217,232,267,
        269,276,282,289,298,301,308,318,327,339,346,352,360,366,368,377,
        381,386,400,404,408,418,422,434
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
                      "INT", "HEX", "FLOAT", "HEX_FLOAT", "COMMENT", "LINE_COMMENT", 
                      "WS", "NL", "SHEBANG" ]

    RULE_start_ = 0
    RULE_chunk = 1
    RULE_block = 2
    RULE_stat = 3
    RULE_attnamelist = 4
    RULE_nameattrib = 5
    RULE_attrib = 6
    RULE_retstat = 7
    RULE_label = 8
    RULE_funcname = 9
    RULE_varlist = 10
    RULE_namelist = 11
    RULE_explist = 12
    RULE_exp = 13
    RULE_var = 14
    RULE_prefixexp = 15
    RULE_functioncall = 16
    RULE_tail = 17
    RULE_args = 18
    RULE_functiondef = 19
    RULE_funcbody = 20
    RULE_parlist = 21
    RULE_tableconstructor = 22
    RULE_fieldlist = 23
    RULE_field = 24
    RULE_fieldsep = 25
    RULE_number = 26
    RULE_string = 27

    ruleNames =  [ "start_", "chunk", "block", "stat", "attnamelist", "nameattrib", 
                   "attrib", "retstat", "label", "funcname", "varlist", 
                   "namelist", "explist", "exp", "var", "prefixexp", "functioncall", 
                   "tail", "args", "functiondef", "funcbody", "parlist", 
                   "tableconstructor", "fieldlist", "field", "fieldsep", 
                   "number", "string" ]

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
    LINE_COMMENT=66
    WS=67
    NL=68
    SHEBANG=69

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_" ):
                return visitor.visitStart_(self)
            else:
                return visitor.visitChildren(self)




    def start_(self):

        localctx = LuaParser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.chunk()
            self.state = 57
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChunk" ):
                return visitor.visitChunk(self)
            else:
                return visitor.visitChildren(self)




    def chunk(self):

        localctx = LuaParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_chunk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LuaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    self.stat() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291464) != 0):
                self.state = 67
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


        def getRuleIndex(self):
            return LuaParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Stat_emptyContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(LuaParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_empty" ):
                listener.enterStat_empty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_empty" ):
                listener.exitStat_empty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_empty" ):
                return visitor.visitStat_empty(self)
            else:
                return visitor.visitChildren(self)


    class Stat_ifContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(LuaParser.IF, 0)
        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.THEN)
            else:
                return self.getToken(LuaParser.THEN, i)
        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.BlockContext)
            else:
                return self.getTypedRuleContext(LuaParser.BlockContext,i)

        def END(self):
            return self.getToken(LuaParser.END, 0)
        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.ELSEIF)
            else:
                return self.getToken(LuaParser.ELSEIF, i)
        def ELSE(self):
            return self.getToken(LuaParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_if" ):
                listener.enterStat_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_if" ):
                listener.exitStat_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_if" ):
                return visitor.visitStat_if(self)
            else:
                return visitor.visitChildren(self)


    class Stat_assignmentContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varlist(self):
            return self.getTypedRuleContext(LuaParser.VarlistContext,0)

        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)
        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_assignment" ):
                listener.enterStat_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_assignment" ):
                listener.exitStat_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_assignment" ):
                return visitor.visitStat_assignment(self)
            else:
                return visitor.visitChildren(self)


    class Stat_localContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOCAL(self):
            return self.getToken(LuaParser.LOCAL, 0)
        def attnamelist(self):
            return self.getTypedRuleContext(LuaParser.AttnamelistContext,0)

        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)
        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_local" ):
                listener.enterStat_local(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_local" ):
                listener.exitStat_local(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_local" ):
                return visitor.visitStat_local(self)
            else:
                return visitor.visitChildren(self)


    class Stat_labelContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(LuaParser.LabelContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_label" ):
                listener.enterStat_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_label" ):
                listener.exitStat_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_label" ):
                return visitor.visitStat_label(self)
            else:
                return visitor.visitChildren(self)


    class Stat_gotoContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GOTO(self):
            return self.getToken(LuaParser.GOTO, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_goto" ):
                listener.enterStat_goto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_goto" ):
                listener.exitStat_goto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_goto" ):
                return visitor.visitStat_goto(self)
            else:
                return visitor.visitChildren(self)


    class Stat_breakContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(LuaParser.BREAK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_break" ):
                listener.enterStat_break(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_break" ):
                listener.exitStat_break(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_break" ):
                return visitor.visitStat_break(self)
            else:
                return visitor.visitChildren(self)


    class Stat_repeatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REPEAT(self):
            return self.getToken(LuaParser.REPEAT, 0)
        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)

        def UNTIL(self):
            return self.getToken(LuaParser.UNTIL, 0)
        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_repeat" ):
                listener.enterStat_repeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_repeat" ):
                listener.exitStat_repeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_repeat" ):
                return visitor.visitStat_repeat(self)
            else:
                return visitor.visitChildren(self)


    class Stat_forContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(LuaParser.FOR, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)
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
        def DO(self):
            return self.getToken(LuaParser.DO, 0)
        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)

        def END(self):
            return self.getToken(LuaParser.END, 0)
        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)

        def IN(self):
            return self.getToken(LuaParser.IN, 0)
        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_for" ):
                listener.enterStat_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_for" ):
                listener.exitStat_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_for" ):
                return visitor.visitStat_for(self)
            else:
                return visitor.visitChildren(self)


    class Stat_functioncallContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_functioncall" ):
                listener.enterStat_functioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_functioncall" ):
                listener.exitStat_functioncall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_functioncall" ):
                return visitor.visitStat_functioncall(self)
            else:
                return visitor.visitChildren(self)


    class Stat_localfunctionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOCAL(self):
            return self.getToken(LuaParser.LOCAL, 0)
        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_localfunction" ):
                listener.enterStat_localfunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_localfunction" ):
                listener.exitStat_localfunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_localfunction" ):
                return visitor.visitStat_localfunction(self)
            else:
                return visitor.visitChildren(self)


    class Stat_whileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(LuaParser.WHILE, 0)
        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)

        def DO(self):
            return self.getToken(LuaParser.DO, 0)
        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)

        def END(self):
            return self.getToken(LuaParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_while" ):
                listener.enterStat_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_while" ):
                listener.exitStat_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_while" ):
                return visitor.visitStat_while(self)
            else:
                return visitor.visitChildren(self)


    class Stat_doContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DO(self):
            return self.getToken(LuaParser.DO, 0)
        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)

        def END(self):
            return self.getToken(LuaParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_do" ):
                listener.enterStat_do(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_do" ):
                listener.exitStat_do(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_do" ):
                return visitor.visitStat_do(self)
            else:
                return visitor.visitChildren(self)


    class Stat_functionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)
        def funcname(self):
            return self.getTypedRuleContext(LuaParser.FuncnameContext,0)

        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_function" ):
                listener.enterStat_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_function" ):
                listener.exitStat_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_function" ):
                return visitor.visitStat_function(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = LuaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Stat_emptyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(LuaParser.SEMI)
                pass

            elif la_ == 2:
                localctx = LuaParser.Stat_assignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.varlist()
                self.state = 72
                self.match(LuaParser.EQ)
                self.state = 73
                self.explist()
                pass

            elif la_ == 3:
                localctx = LuaParser.Stat_functioncallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.functioncall(0)
                pass

            elif la_ == 4:
                localctx = LuaParser.Stat_labelContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.label()
                pass

            elif la_ == 5:
                localctx = LuaParser.Stat_breakContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 6:
                localctx = LuaParser.Stat_gotoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.match(LuaParser.GOTO)
                self.state = 79
                self.match(LuaParser.NAME)
                pass

            elif la_ == 7:
                localctx = LuaParser.Stat_doContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.match(LuaParser.DO)
                self.state = 81
                self.block()
                self.state = 82
                self.match(LuaParser.END)
                pass

            elif la_ == 8:
                localctx = LuaParser.Stat_whileContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 84
                self.match(LuaParser.WHILE)
                self.state = 85
                self.exp(0)
                self.state = 86
                self.match(LuaParser.DO)
                self.state = 87
                self.block()
                self.state = 88
                self.match(LuaParser.END)
                pass

            elif la_ == 9:
                localctx = LuaParser.Stat_repeatContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.match(LuaParser.REPEAT)
                self.state = 91
                self.block()
                self.state = 92
                self.match(LuaParser.UNTIL)
                self.state = 93
                self.exp(0)
                pass

            elif la_ == 10:
                localctx = LuaParser.Stat_ifContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 95
                self.match(LuaParser.IF)
                self.state = 96
                self.exp(0)
                self.state = 97
                self.match(LuaParser.THEN)
                self.state = 98
                self.block()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 99
                    self.match(LuaParser.ELSEIF)
                    self.state = 100
                    self.exp(0)
                    self.state = 101
                    self.match(LuaParser.THEN)
                    self.state = 102
                    self.block()
                    self.state = 108
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 109
                    self.match(LuaParser.ELSE)
                    self.state = 110
                    self.block()


                self.state = 113
                self.match(LuaParser.END)
                pass

            elif la_ == 11:
                localctx = LuaParser.Stat_forContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 115
                self.match(LuaParser.FOR)
                self.state = 116
                self.match(LuaParser.NAME)
                self.state = 117
                self.match(LuaParser.EQ)
                self.state = 118
                self.exp(0)
                self.state = 119
                self.match(LuaParser.COMMA)
                self.state = 120
                self.exp(0)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 121
                    self.match(LuaParser.COMMA)
                    self.state = 122
                    self.exp(0)


                self.state = 125
                self.match(LuaParser.DO)
                self.state = 126
                self.block()
                self.state = 127
                self.match(LuaParser.END)
                pass

            elif la_ == 12:
                localctx = LuaParser.Stat_forContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 129
                self.match(LuaParser.FOR)
                self.state = 130
                self.namelist()
                self.state = 131
                self.match(LuaParser.IN)
                self.state = 132
                self.explist()
                self.state = 133
                self.match(LuaParser.DO)
                self.state = 134
                self.block()
                self.state = 135
                self.match(LuaParser.END)
                pass

            elif la_ == 13:
                localctx = LuaParser.Stat_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 137
                self.match(LuaParser.FUNCTION)
                self.state = 138
                self.funcname()
                self.state = 139
                self.funcbody()
                pass

            elif la_ == 14:
                localctx = LuaParser.Stat_localfunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 141
                self.match(LuaParser.LOCAL)
                self.state = 142
                self.match(LuaParser.FUNCTION)
                self.state = 143
                self.match(LuaParser.NAME)
                self.state = 144
                self.funcbody()
                pass

            elif la_ == 15:
                localctx = LuaParser.Stat_localContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 145
                self.match(LuaParser.LOCAL)
                self.state = 146
                self.attnamelist()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 147
                    self.match(LuaParser.EQ)
                    self.state = 148
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

        def nameattrib(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameattribContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameattribContext,i)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttnamelist" ):
                return visitor.visitAttnamelist(self)
            else:
                return visitor.visitChildren(self)




    def attnamelist(self):

        localctx = LuaParser.AttnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attnamelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.nameattrib()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 154
                self.match(LuaParser.COMMA)
                self.state = 155
                self.nameattrib()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameattribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def attrib(self):
            return self.getTypedRuleContext(LuaParser.AttribContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_nameattrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameattrib" ):
                listener.enterNameattrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameattrib" ):
                listener.exitNameattrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameattrib" ):
                return visitor.visitNameattrib(self)
            else:
                return visitor.visitChildren(self)




    def nameattrib(self):

        localctx = LuaParser.NameattribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_nameattrib)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LuaParser.NAME)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 162
                self.attrib()


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrib" ):
                return visitor.visitAttrib(self)
            else:
                return visitor.visitChildren(self)




    def attrib(self):

        localctx = LuaParser.AttribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(LuaParser.LT)
            self.state = 166
            self.match(LuaParser.NAME)
            self.state = 167
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetstat" ):
                return visitor.visitRetstat(self)
            else:
                return visitor.visitChildren(self)




    def retstat(self):

        localctx = LuaParser.RetstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_retstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 169
                self.match(LuaParser.RETURN)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 170
                    self.explist()


                pass
            elif token in [3]:
                self.state = 173
                self.match(LuaParser.BREAK)
                pass
            elif token in [22]:
                self.state = 174
                self.match(LuaParser.CONTINUE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 177
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = LuaParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(LuaParser.CC)
            self.state = 181
            self.match(LuaParser.NAME)
            self.state = 182
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncname" ):
                return visitor.visitFuncname(self)
            else:
                return visitor.visitChildren(self)




    def funcname(self):

        localctx = LuaParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(LuaParser.NAME)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 185
                self.match(LuaParser.DOT)
                self.state = 186
                self.match(LuaParser.NAME)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 192
                self.match(LuaParser.COL)
                self.state = 193
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = LuaParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.var()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 197
                self.match(LuaParser.COMMA)
                self.state = 198
                self.var()
                self.state = 203
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamelist" ):
                return visitor.visitNamelist(self)
            else:
                return visitor.visitChildren(self)




    def namelist(self):

        localctx = LuaParser.NamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_namelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(LuaParser.NAME)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.match(LuaParser.COMMA)
                    self.state = 206
                    self.match(LuaParser.NAME) 
                self.state = 211
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = LuaParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.exp(0)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 213
                self.match(LuaParser.COMMA)
                self.state = 214
                self.exp(0)
                self.state = 219
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
            self.unary_op = None # Token
            self.op = None # Token

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

        def LL(self):
            return self.getToken(LuaParser.LL, 0)

        def GG(self):
            return self.getToken(LuaParser.GG, 0)

        def AMP(self):
            return self.getToken(LuaParser.AMP, 0)

        def PIPE(self):
            return self.getToken(LuaParser.PIPE, 0)

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

        def getRuleIndex(self):
            return LuaParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 221
                self.match(LuaParser.NIL)
                pass
            elif token in [25]:
                self.state = 222
                self.match(LuaParser.FALSE)
                pass
            elif token in [26]:
                self.state = 223
                self.match(LuaParser.TRUE)
                pass
            elif token in [61, 62, 63, 64]:
                self.state = 224
                self.number()
                pass
            elif token in [58, 59, 60]:
                self.state = 225
                self.string()
                pass
            elif token in [55]:
                self.state = 226
                self.match(LuaParser.DDD)
                pass
            elif token in [17]:
                self.state = 227
                self.functiondef()
                pass
            elif token in [31, 57]:
                self.state = 228
                self.prefixexp()
                pass
            elif token in [46]:
                self.state = 229
                self.tableconstructor()
                pass
            elif token in [28, 29, 30, 33]:
                self.state = 230
                localctx.unary_op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10468982784) != 0)):
                    localctx.unary_op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 231
                self.exp(11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 267
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 234
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")

                        self.state = 235
                        localctx.op = self.match(LuaParser.CARET)
                        self.state = 236
                        self.exp(12)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 237
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 238
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18049995198431232) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 239
                        self.exp(11)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 240
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 241
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==44):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 242
                        self.exp(10)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 243
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")

                        self.state = 244
                        localctx.op = self.match(LuaParser.DD)
                        self.state = 245
                        self.exp(8)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 246
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 247
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 248
                        self.exp(8)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 249
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 250
                        localctx.op = self.match(LuaParser.AMP)
                        self.state = 251
                        self.exp(7)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 252
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 253
                        localctx.op = self.match(LuaParser.SQUIG)
                        self.state = 254
                        self.exp(6)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 255
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 256
                        localctx.op = self.match(LuaParser.PIPE)
                        self.state = 257
                        self.exp(5)
                        pass

                    elif la_ == 9:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 258
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 259
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 73186792481226752) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 260
                        self.exp(4)
                        pass

                    elif la_ == 10:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 261
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 262
                        localctx.op = self.match(LuaParser.AND)
                        self.state = 263
                        self.exp(3)
                        pass

                    elif la_ == 11:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 264
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                        self.state = 265
                        localctx.op = self.match(LuaParser.OR)
                        self.state = 266
                        self.exp(2)
                        pass

             
                self.state = 271
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


        def tail(self):
            return self.getTypedRuleContext(LuaParser.TailContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LuaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.prefixexp()
                self.state = 274
                self.tail()
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

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def OP(self):
            return self.getToken(LuaParser.OP, 0)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixexp" ):
                return visitor.visitPrefixexp(self)
            else:
                return visitor.visitChildren(self)




    def prefixexp(self):

        localctx = LuaParser.PrefixexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_prefixexp)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(LuaParser.NAME)
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 279
                        self.tail() 
                    self.state = 284
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.functioncall(0)
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 286
                        self.tail() 
                    self.state = 291
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(LuaParser.OP)
                self.state = 293
                self.exp(0)
                self.state = 294
                self.match(LuaParser.CP)
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 295
                        self.tail() 
                    self.state = 300
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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


        def getRuleIndex(self):
            return LuaParser.RULE_functioncall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Functioncall_expContext(FunctioncallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.FunctioncallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(LuaParser.OP, 0)
        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)

        def CP(self):
            return self.getToken(LuaParser.CP, 0)
        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall_exp" ):
                listener.enterFunctioncall_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall_exp" ):
                listener.exitFunctioncall_exp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall_exp" ):
                return visitor.visitFunctioncall_exp(self)
            else:
                return visitor.visitChildren(self)


    class Functioncall_expinvokeContext(FunctioncallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.FunctioncallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(LuaParser.OP, 0)
        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)

        def CP(self):
            return self.getToken(LuaParser.CP, 0)
        def COL(self):
            return self.getToken(LuaParser.COL, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall_expinvoke" ):
                listener.enterFunctioncall_expinvoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall_expinvoke" ):
                listener.exitFunctioncall_expinvoke(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall_expinvoke" ):
                return visitor.visitFunctioncall_expinvoke(self)
            else:
                return visitor.visitChildren(self)


    class Functioncall_invokeContext(FunctioncallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.FunctioncallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)
        def COL(self):
            return self.getToken(LuaParser.COL, 0)
        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall_invoke" ):
                listener.enterFunctioncall_invoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall_invoke" ):
                listener.exitFunctioncall_invoke(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall_invoke" ):
                return visitor.visitFunctioncall_invoke(self)
            else:
                return visitor.visitChildren(self)


    class Functioncall_nestedinvokeContext(FunctioncallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.FunctioncallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)

        def COL(self):
            return self.getToken(LuaParser.COL, 0)
        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall_nestedinvoke" ):
                listener.enterFunctioncall_nestedinvoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall_nestedinvoke" ):
                listener.exitFunctioncall_nestedinvoke(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall_nestedinvoke" ):
                return visitor.visitFunctioncall_nestedinvoke(self)
            else:
                return visitor.visitChildren(self)


    class Functioncall_nameContext(FunctioncallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.FunctioncallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall_name" ):
                listener.enterFunctioncall_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall_name" ):
                listener.exitFunctioncall_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall_name" ):
                return visitor.visitFunctioncall_name(self)
            else:
                return visitor.visitChildren(self)


    class Functioncall_nestedContext(FunctioncallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.FunctioncallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall_nested" ):
                listener.enterFunctioncall_nested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall_nested" ):
                listener.exitFunctioncall_nested(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall_nested" ):
                return visitor.visitFunctioncall_nested(self)
            else:
                return visitor.visitChildren(self)



    def functioncall(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.FunctioncallContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_functioncall, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Functioncall_nameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 304
                self.match(LuaParser.NAME)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 305
                    self.tail()
                    self.state = 310
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 311
                self.args()
                pass

            elif la_ == 2:
                localctx = LuaParser.Functioncall_expContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 312
                self.match(LuaParser.OP)
                self.state = 313
                self.exp(0)
                self.state = 314
                self.match(LuaParser.CP)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 315
                    self.tail()
                    self.state = 320
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 321
                self.args()
                pass

            elif la_ == 3:
                localctx = LuaParser.Functioncall_invokeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 323
                self.match(LuaParser.NAME)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 324
                    self.tail()
                    self.state = 329
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 330
                self.match(LuaParser.COL)
                self.state = 331
                self.match(LuaParser.NAME)
                self.state = 332
                self.args()
                pass

            elif la_ == 4:
                localctx = LuaParser.Functioncall_expinvokeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 333
                self.match(LuaParser.OP)
                self.state = 334
                self.exp(0)
                self.state = 335
                self.match(LuaParser.CP)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 336
                    self.tail()
                    self.state = 341
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 342
                self.match(LuaParser.COL)
                self.state = 343
                self.match(LuaParser.NAME)
                self.state = 344
                self.args()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 366
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.Functioncall_nestedContext(self, LuaParser.FunctioncallContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 348
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 352
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27 or _la==48:
                            self.state = 349
                            self.tail()
                            self.state = 354
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 355
                        self.args()
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.Functioncall_nestedinvokeContext(self, LuaParser.FunctioncallContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 356
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 360
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27 or _la==48:
                            self.state = 357
                            self.tail()
                            self.state = 362
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 363
                        self.match(LuaParser.COL)
                        self.state = 364
                        self.match(LuaParser.NAME)
                        self.state = 365
                        self.args()
                        pass

             
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(LuaParser.OB, 0)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def CB(self):
            return self.getToken(LuaParser.CB, 0)

        def DOT(self):
            return self.getToken(LuaParser.DOT, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail" ):
                listener.enterTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail" ):
                listener.exitTail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail" ):
                return visitor.visitTail(self)
            else:
                return visitor.visitChildren(self)




    def tail(self):

        localctx = LuaParser.TailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 371
                self.match(LuaParser.OB)
                self.state = 372
                self.exp(0)
                self.state = 373
                self.match(LuaParser.CB)
                pass
            elif token in [27]:
                self.state = 375
                self.match(LuaParser.DOT)
                self.state = 376
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = LuaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(LuaParser.OP)
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 380
                    self.explist()


                self.state = 383
                self.match(LuaParser.CP)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.tableconstructor()
                pass
            elif token in [58, 59, 60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctiondef" ):
                return visitor.visitFunctiondef(self)
            else:
                return visitor.visitChildren(self)




    def functiondef(self):

        localctx = LuaParser.FunctiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(LuaParser.FUNCTION)
            self.state = 389
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncbody" ):
                return visitor.visitFuncbody(self)
            else:
                return visitor.visitChildren(self)




    def funcbody(self):

        localctx = LuaParser.FuncbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(LuaParser.OP)
            self.state = 392
            self.parlist()
            self.state = 393
            self.match(LuaParser.CP)
            self.state = 394
            self.block()
            self.state = 395
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParlist" ):
                return visitor.visitParlist(self)
            else:
                return visitor.visitChildren(self)




    def parlist(self):

        localctx = LuaParser.ParlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.namelist()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 398
                    self.match(LuaParser.COMMA)
                    self.state = 399
                    self.match(LuaParser.DDD)


                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableconstructor" ):
                return visitor.visitTableconstructor(self)
            else:
                return visitor.visitChildren(self)




    def tableconstructor(self):

        localctx = LuaParser.TableconstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(LuaParser.OCU)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280653027441537) != 0):
                self.state = 407
                self.fieldlist()


            self.state = 410
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldlist" ):
                return visitor.visitFieldlist(self)
            else:
                return visitor.visitChildren(self)




    def fieldlist(self):

        localctx = LuaParser.FieldlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.field()
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 413
                    self.fieldsep()
                    self.state = 414
                    self.field() 
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==15:
                self.state = 421
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = LuaParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_field)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(LuaParser.OB)
                self.state = 425
                self.exp(0)
                self.state = 426
                self.match(LuaParser.CB)
                self.state = 427
                self.match(LuaParser.EQ)
                self.state = 428
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(LuaParser.NAME)
                self.state = 431
                self.match(LuaParser.EQ)
                self.state = 432
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldsep" ):
                return visitor.visitFieldsep(self)
            else:
                return visitor.visitChildren(self)




    def fieldsep(self):

        localctx = LuaParser.FieldsepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = LuaParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = LuaParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
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
        self._predicates[13] = self.exp_sempred
        self._predicates[16] = self.functioncall_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def functioncall_sempred(self, localctx:FunctioncallContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




