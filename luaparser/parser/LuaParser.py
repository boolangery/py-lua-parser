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
        4,1,68,466,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,1,1,1,
        1,2,5,2,83,8,2,10,2,12,2,86,9,2,1,2,3,2,89,8,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,106,8,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,139,8,9,10,
        9,12,9,142,9,9,1,9,1,9,3,9,146,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,158,8,10,1,10,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,1,14,3,14,185,8,14,1,15,1,15,1,15,1,15,1,
        15,5,15,192,8,15,10,15,12,15,195,9,15,1,16,1,16,1,16,3,16,200,8,
        16,1,17,1,17,3,17,204,8,17,1,17,1,17,3,17,208,8,17,1,17,3,17,211,
        8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,220,8,19,10,19,12,19,
        223,9,19,1,19,1,19,3,19,227,8,19,1,20,1,20,1,20,5,20,232,8,20,10,
        20,12,20,235,9,20,1,21,1,21,1,21,5,21,240,8,21,10,21,12,21,243,9,
        21,1,22,1,22,1,22,5,22,248,8,22,10,22,12,22,251,9,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,265,8,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,5,23,291,8,
        23,10,23,12,23,294,9,23,1,24,1,24,1,24,1,24,3,24,300,8,24,1,25,1,
        25,5,25,304,8,25,10,25,12,25,307,9,25,1,25,1,25,5,25,311,8,25,10,
        25,12,25,314,9,25,1,25,1,25,1,25,1,25,5,25,320,8,25,10,25,12,25,
        323,9,25,3,25,325,8,25,1,26,1,26,1,26,5,26,330,8,26,10,26,12,26,
        333,9,26,1,26,1,26,1,26,1,26,1,26,5,26,340,8,26,10,26,12,26,343,
        9,26,1,26,1,26,1,26,1,26,5,26,349,8,26,10,26,12,26,352,9,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,5,26,361,8,26,10,26,12,26,364,9,26,
        1,26,1,26,1,26,1,26,3,26,370,8,26,1,26,1,26,5,26,374,8,26,10,26,
        12,26,377,9,26,1,26,1,26,1,26,5,26,382,8,26,10,26,12,26,385,9,26,
        1,26,1,26,1,26,5,26,390,8,26,10,26,12,26,393,9,26,1,27,1,27,1,27,
        1,27,1,27,1,27,3,27,401,8,27,1,28,1,28,3,28,405,8,28,1,28,1,28,1,
        28,3,28,410,8,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,
        31,1,31,1,31,3,31,424,8,31,1,31,1,31,3,31,428,8,31,1,32,1,32,3,32,
        432,8,32,1,32,1,32,1,33,1,33,1,33,1,33,5,33,440,8,33,10,33,12,33,
        443,9,33,1,33,3,33,446,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,3,34,458,8,34,1,35,1,35,1,36,1,36,1,37,1,37,1,37,0,
        2,46,52,38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,0,8,2,0,28,
        30,33,33,3,0,37,38,45,45,54,54,2,0,29,29,44,44,4,0,19,20,40,41,50,
        50,56,56,3,0,28,28,34,36,52,52,2,0,1,1,15,15,1,0,61,64,1,0,58,60,
        504,0,76,1,0,0,0,2,79,1,0,0,0,4,84,1,0,0,0,6,105,1,0,0,0,8,107,1,
        0,0,0,10,111,1,0,0,0,12,114,1,0,0,0,14,118,1,0,0,0,16,124,1,0,0,
        0,18,129,1,0,0,0,20,149,1,0,0,0,22,163,1,0,0,0,24,171,1,0,0,0,26,
        175,1,0,0,0,28,180,1,0,0,0,30,186,1,0,0,0,32,199,1,0,0,0,34,207,
        1,0,0,0,36,212,1,0,0,0,38,216,1,0,0,0,40,228,1,0,0,0,42,236,1,0,
        0,0,44,244,1,0,0,0,46,264,1,0,0,0,48,299,1,0,0,0,50,324,1,0,0,0,
        52,369,1,0,0,0,54,400,1,0,0,0,56,409,1,0,0,0,58,411,1,0,0,0,60,414,
        1,0,0,0,62,427,1,0,0,0,64,429,1,0,0,0,66,435,1,0,0,0,68,457,1,0,
        0,0,70,459,1,0,0,0,72,461,1,0,0,0,74,463,1,0,0,0,76,77,3,2,1,0,77,
        78,5,0,0,1,78,1,1,0,0,0,79,80,3,4,2,0,80,3,1,0,0,0,81,83,3,6,3,0,
        82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,88,1,
        0,0,0,86,84,1,0,0,0,87,89,3,34,17,0,88,87,1,0,0,0,88,89,1,0,0,0,
        89,5,1,0,0,0,90,106,5,1,0,0,91,106,3,8,4,0,92,106,3,52,26,0,93,106,
        3,36,18,0,94,106,5,3,0,0,95,106,3,10,5,0,96,106,3,12,6,0,97,106,
        3,14,7,0,98,106,3,16,8,0,99,106,3,18,9,0,100,106,3,20,10,0,101,106,
        3,22,11,0,102,106,3,24,12,0,103,106,3,26,13,0,104,106,3,28,14,0,
        105,90,1,0,0,0,105,91,1,0,0,0,105,92,1,0,0,0,105,93,1,0,0,0,105,
        94,1,0,0,0,105,95,1,0,0,0,105,96,1,0,0,0,105,97,1,0,0,0,105,98,1,
        0,0,0,105,99,1,0,0,0,105,100,1,0,0,0,105,101,1,0,0,0,105,102,1,0,
        0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,7,1,0,0,0,107,108,3,40,20,
        0,108,109,5,2,0,0,109,110,3,44,22,0,110,9,1,0,0,0,111,112,5,4,0,
        0,112,113,5,57,0,0,113,11,1,0,0,0,114,115,5,5,0,0,115,116,3,4,2,
        0,116,117,5,6,0,0,117,13,1,0,0,0,118,119,5,7,0,0,119,120,3,46,23,
        0,120,121,5,5,0,0,121,122,3,4,2,0,122,123,5,6,0,0,123,15,1,0,0,0,
        124,125,5,8,0,0,125,126,3,4,2,0,126,127,5,9,0,0,127,128,3,46,23,
        0,128,17,1,0,0,0,129,130,5,10,0,0,130,131,3,46,23,0,131,132,5,11,
        0,0,132,140,3,4,2,0,133,134,5,12,0,0,134,135,3,46,23,0,135,136,5,
        11,0,0,136,137,3,4,2,0,137,139,1,0,0,0,138,133,1,0,0,0,139,142,1,
        0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,145,1,0,0,0,142,140,1,
        0,0,0,143,144,5,13,0,0,144,146,3,4,2,0,145,143,1,0,0,0,145,146,1,
        0,0,0,146,147,1,0,0,0,147,148,5,6,0,0,148,19,1,0,0,0,149,150,5,14,
        0,0,150,151,5,57,0,0,151,152,5,2,0,0,152,153,3,46,23,0,153,154,5,
        15,0,0,154,157,3,46,23,0,155,156,5,15,0,0,156,158,3,46,23,0,157,
        155,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,5,0,0,160,
        161,3,4,2,0,161,162,5,6,0,0,162,21,1,0,0,0,163,164,5,14,0,0,164,
        165,3,42,21,0,165,166,5,16,0,0,166,167,3,44,22,0,167,168,5,5,0,0,
        168,169,3,4,2,0,169,170,5,6,0,0,170,23,1,0,0,0,171,172,5,17,0,0,
        172,173,3,38,19,0,173,174,3,60,30,0,174,25,1,0,0,0,175,176,5,18,
        0,0,176,177,5,17,0,0,177,178,5,57,0,0,178,179,3,60,30,0,179,27,1,
        0,0,0,180,181,5,18,0,0,181,184,3,42,21,0,182,183,5,2,0,0,183,185,
        3,44,22,0,184,182,1,0,0,0,184,185,1,0,0,0,185,29,1,0,0,0,186,187,
        5,57,0,0,187,193,3,32,16,0,188,189,5,15,0,0,189,190,5,57,0,0,190,
        192,3,32,16,0,191,188,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,
        194,1,0,0,0,194,31,1,0,0,0,195,193,1,0,0,0,196,197,5,19,0,0,197,
        198,5,57,0,0,198,200,5,20,0,0,199,196,1,0,0,0,199,200,1,0,0,0,200,
        33,1,0,0,0,201,203,5,21,0,0,202,204,3,44,22,0,203,202,1,0,0,0,203,
        204,1,0,0,0,204,208,1,0,0,0,205,208,5,3,0,0,206,208,5,22,0,0,207,
        201,1,0,0,0,207,205,1,0,0,0,207,206,1,0,0,0,208,210,1,0,0,0,209,
        211,5,1,0,0,210,209,1,0,0,0,210,211,1,0,0,0,211,35,1,0,0,0,212,213,
        5,23,0,0,213,214,5,57,0,0,214,215,5,23,0,0,215,37,1,0,0,0,216,221,
        5,57,0,0,217,218,5,27,0,0,218,220,5,57,0,0,219,217,1,0,0,0,220,223,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,226,1,0,0,0,223,221,
        1,0,0,0,224,225,5,39,0,0,225,227,5,57,0,0,226,224,1,0,0,0,226,227,
        1,0,0,0,227,39,1,0,0,0,228,233,3,48,24,0,229,230,5,15,0,0,230,232,
        3,48,24,0,231,229,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,
        1,0,0,0,234,41,1,0,0,0,235,233,1,0,0,0,236,241,5,57,0,0,237,238,
        5,15,0,0,238,240,5,57,0,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,43,1,0,0,0,243,241,1,0,0,0,244,249,3,
        46,23,0,245,246,5,15,0,0,246,248,3,46,23,0,247,245,1,0,0,0,248,251,
        1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,45,1,0,0,0,251,249,1,
        0,0,0,252,253,6,23,-1,0,253,265,5,24,0,0,254,265,5,25,0,0,255,265,
        5,26,0,0,256,265,3,72,36,0,257,265,3,74,37,0,258,265,5,55,0,0,259,
        265,3,24,12,0,260,265,3,50,25,0,261,265,3,64,32,0,262,263,7,0,0,
        0,263,265,3,46,23,8,264,252,1,0,0,0,264,254,1,0,0,0,264,255,1,0,
        0,0,264,256,1,0,0,0,264,257,1,0,0,0,264,258,1,0,0,0,264,259,1,0,
        0,0,264,260,1,0,0,0,264,261,1,0,0,0,264,262,1,0,0,0,265,292,1,0,
        0,0,266,267,10,9,0,0,267,268,5,53,0,0,268,291,3,46,23,9,269,270,
        10,7,0,0,270,271,7,1,0,0,271,291,3,46,23,8,272,273,10,6,0,0,273,
        274,7,2,0,0,274,291,3,46,23,7,275,276,10,5,0,0,276,277,5,51,0,0,
        277,291,3,46,23,5,278,279,10,4,0,0,279,280,7,3,0,0,280,291,3,46,
        23,5,281,282,10,3,0,0,282,283,5,42,0,0,283,291,3,46,23,4,284,285,
        10,2,0,0,285,286,5,43,0,0,286,291,3,46,23,3,287,288,10,1,0,0,288,
        289,7,4,0,0,289,291,3,46,23,2,290,266,1,0,0,0,290,269,1,0,0,0,290,
        272,1,0,0,0,290,275,1,0,0,0,290,278,1,0,0,0,290,281,1,0,0,0,290,
        284,1,0,0,0,290,287,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,
        293,1,0,0,0,293,47,1,0,0,0,294,292,1,0,0,0,295,300,5,57,0,0,296,
        297,3,50,25,0,297,298,3,54,27,0,298,300,1,0,0,0,299,295,1,0,0,0,
        299,296,1,0,0,0,300,49,1,0,0,0,301,305,5,57,0,0,302,304,3,54,27,
        0,303,302,1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,
        0,306,325,1,0,0,0,307,305,1,0,0,0,308,312,3,52,26,0,309,311,3,54,
        27,0,310,309,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,312,313,1,0,
        0,0,313,325,1,0,0,0,314,312,1,0,0,0,315,316,5,31,0,0,316,317,3,46,
        23,0,317,321,5,32,0,0,318,320,3,54,27,0,319,318,1,0,0,0,320,323,
        1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,325,1,0,0,0,323,321,
        1,0,0,0,324,301,1,0,0,0,324,308,1,0,0,0,324,315,1,0,0,0,325,51,1,
        0,0,0,326,327,6,26,-1,0,327,331,5,57,0,0,328,330,3,54,27,0,329,328,
        1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,334,
        1,0,0,0,333,331,1,0,0,0,334,370,3,56,28,0,335,336,5,31,0,0,336,337,
        3,46,23,0,337,341,5,32,0,0,338,340,3,54,27,0,339,338,1,0,0,0,340,
        343,1,0,0,0,341,339,1,0,0,0,341,342,1,0,0,0,342,344,1,0,0,0,343,
        341,1,0,0,0,344,345,3,56,28,0,345,370,1,0,0,0,346,350,5,57,0,0,347,
        349,3,54,27,0,348,347,1,0,0,0,349,352,1,0,0,0,350,348,1,0,0,0,350,
        351,1,0,0,0,351,353,1,0,0,0,352,350,1,0,0,0,353,354,5,39,0,0,354,
        355,5,57,0,0,355,370,3,56,28,0,356,357,5,31,0,0,357,358,3,46,23,
        0,358,362,5,32,0,0,359,361,3,54,27,0,360,359,1,0,0,0,361,364,1,0,
        0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,365,1,0,0,0,364,362,1,0,
        0,0,365,366,5,39,0,0,366,367,5,57,0,0,367,368,3,56,28,0,368,370,
        1,0,0,0,369,326,1,0,0,0,369,335,1,0,0,0,369,346,1,0,0,0,369,356,
        1,0,0,0,370,391,1,0,0,0,371,375,10,5,0,0,372,374,3,54,27,0,373,372,
        1,0,0,0,374,377,1,0,0,0,375,373,1,0,0,0,375,376,1,0,0,0,376,378,
        1,0,0,0,377,375,1,0,0,0,378,390,3,56,28,0,379,383,10,2,0,0,380,382,
        3,54,27,0,381,380,1,0,0,0,382,385,1,0,0,0,383,381,1,0,0,0,383,384,
        1,0,0,0,384,386,1,0,0,0,385,383,1,0,0,0,386,387,5,39,0,0,387,388,
        5,57,0,0,388,390,3,56,28,0,389,371,1,0,0,0,389,379,1,0,0,0,390,393,
        1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,53,1,0,0,0,393,391,1,
        0,0,0,394,395,5,48,0,0,395,396,3,46,23,0,396,397,5,49,0,0,397,401,
        1,0,0,0,398,399,5,27,0,0,399,401,5,57,0,0,400,394,1,0,0,0,400,398,
        1,0,0,0,401,55,1,0,0,0,402,404,5,31,0,0,403,405,3,44,22,0,404,403,
        1,0,0,0,404,405,1,0,0,0,405,406,1,0,0,0,406,410,5,32,0,0,407,410,
        3,64,32,0,408,410,3,74,37,0,409,402,1,0,0,0,409,407,1,0,0,0,409,
        408,1,0,0,0,410,57,1,0,0,0,411,412,5,17,0,0,412,413,3,60,30,0,413,
        59,1,0,0,0,414,415,5,31,0,0,415,416,3,62,31,0,416,417,5,32,0,0,417,
        418,3,4,2,0,418,419,5,6,0,0,419,61,1,0,0,0,420,423,3,42,21,0,421,
        422,5,15,0,0,422,424,5,55,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,
        428,1,0,0,0,425,428,5,55,0,0,426,428,1,0,0,0,427,420,1,0,0,0,427,
        425,1,0,0,0,427,426,1,0,0,0,428,63,1,0,0,0,429,431,5,46,0,0,430,
        432,3,66,33,0,431,430,1,0,0,0,431,432,1,0,0,0,432,433,1,0,0,0,433,
        434,5,47,0,0,434,65,1,0,0,0,435,441,3,68,34,0,436,437,3,70,35,0,
        437,438,3,68,34,0,438,440,1,0,0,0,439,436,1,0,0,0,440,443,1,0,0,
        0,441,439,1,0,0,0,441,442,1,0,0,0,442,445,1,0,0,0,443,441,1,0,0,
        0,444,446,3,70,35,0,445,444,1,0,0,0,445,446,1,0,0,0,446,67,1,0,0,
        0,447,448,5,48,0,0,448,449,3,46,23,0,449,450,5,49,0,0,450,451,5,
        2,0,0,451,452,3,46,23,0,452,458,1,0,0,0,453,454,5,57,0,0,454,455,
        5,2,0,0,455,458,3,46,23,0,456,458,3,46,23,0,457,447,1,0,0,0,457,
        453,1,0,0,0,457,456,1,0,0,0,458,69,1,0,0,0,459,460,7,5,0,0,460,71,
        1,0,0,0,461,462,7,6,0,0,462,73,1,0,0,0,463,464,7,7,0,0,464,75,1,
        0,0,0,43,84,88,105,140,145,157,184,193,199,203,207,210,221,226,233,
        241,249,264,290,292,299,305,312,321,324,331,341,350,362,369,375,
        383,389,391,400,404,409,423,427,431,441,445,457
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
    RULE_assign = 4
    RULE_goto = 5
    RULE_do = 6
    RULE_while = 7
    RULE_repeat = 8
    RULE_if = 9
    RULE_for = 10
    RULE_forin = 11
    RULE_functiondef = 12
    RULE_localfunction = 13
    RULE_localassign = 14
    RULE_attnamelist = 15
    RULE_attrib = 16
    RULE_retstat = 17
    RULE_label = 18
    RULE_funcname = 19
    RULE_varlist = 20
    RULE_namelist = 21
    RULE_explist = 22
    RULE_exp = 23
    RULE_var = 24
    RULE_prefixexp = 25
    RULE_functioncall = 26
    RULE_tail = 27
    RULE_args = 28
    RULE_anonfunctiondef = 29
    RULE_funcbody = 30
    RULE_parlist = 31
    RULE_tableconstructor = 32
    RULE_fieldlist = 33
    RULE_field = 34
    RULE_fieldsep = 35
    RULE_number = 36
    RULE_string = 37

    ruleNames =  [ "start_", "chunk", "block", "stat", "assign", "goto", 
                   "do", "while", "repeat", "if", "for", "forin", "functiondef", 
                   "localfunction", "localassign", "attnamelist", "attrib", 
                   "retstat", "label", "funcname", "varlist", "namelist", 
                   "explist", "exp", "var", "prefixexp", "functioncall", 
                   "tail", "args", "anonfunctiondef", "funcbody", "parlist", 
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
            self.state = 76
            self.chunk()
            self.state = 77
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
            self.state = 79
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
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.stat() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291464) != 0):
                self.state = 87
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

        def assign(self):
            return self.getTypedRuleContext(LuaParser.AssignContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def label(self):
            return self.getTypedRuleContext(LuaParser.LabelContext,0)


        def BREAK(self):
            return self.getToken(LuaParser.BREAK, 0)

        def goto(self):
            return self.getTypedRuleContext(LuaParser.GotoContext,0)


        def do(self):
            return self.getTypedRuleContext(LuaParser.DoContext,0)


        def while_(self):
            return self.getTypedRuleContext(LuaParser.WhileContext,0)


        def repeat(self):
            return self.getTypedRuleContext(LuaParser.RepeatContext,0)


        def if_(self):
            return self.getTypedRuleContext(LuaParser.IfContext,0)


        def for_(self):
            return self.getTypedRuleContext(LuaParser.ForContext,0)


        def forin(self):
            return self.getTypedRuleContext(LuaParser.ForinContext,0)


        def functiondef(self):
            return self.getTypedRuleContext(LuaParser.FunctiondefContext,0)


        def localfunction(self):
            return self.getTypedRuleContext(LuaParser.LocalfunctionContext,0)


        def localassign(self):
            return self.getTypedRuleContext(LuaParser.LocalassignContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = LuaParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(LuaParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.functioncall(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 95
                self.goto()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 96
                self.do()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 97
                self.while_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 98
                self.repeat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 99
                self.if_()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 100
                self.for_()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 101
                self.forin()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 102
                self.functiondef()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 103
                self.localfunction()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 104
                self.localassign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varlist(self):
            return self.getTypedRuleContext(LuaParser.VarlistContext,0)


        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = LuaParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.varlist()
            self.state = 108
            self.match(LuaParser.EQ)
            self.state = 109
            self.explist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(LuaParser.GOTO, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_goto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto" ):
                listener.enterGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto" ):
                listener.exitGoto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto" ):
                return visitor.visitGoto(self)
            else:
                return visitor.visitChildren(self)




    def goto(self):

        localctx = LuaParser.GotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(LuaParser.GOTO)
            self.state = 112
            self.match(LuaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoContext(ParserRuleContext):
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
            return LuaParser.RULE_do

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo" ):
                listener.enterDo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo" ):
                listener.exitDo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo" ):
                return visitor.visitDo(self)
            else:
                return visitor.visitChildren(self)




    def do(self):

        localctx = LuaParser.DoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_do)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(LuaParser.DO)
            self.state = 115
            self.block()
            self.state = 116
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return LuaParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = LuaParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(LuaParser.WHILE)
            self.state = 119
            self.exp(0)
            self.state = 120
            self.match(LuaParser.DO)
            self.state = 121
            self.block()
            self.state = 122
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):
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

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)




    def repeat(self):

        localctx = LuaParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(LuaParser.REPEAT)
            self.state = 125
            self.block()
            self.state = 126
            self.match(LuaParser.UNTIL)
            self.state = 127
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return LuaParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = LuaParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(LuaParser.IF)
            self.state = 130
            self.exp(0)
            self.state = 131
            self.match(LuaParser.THEN)
            self.state = 132
            self.block()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 133
                self.match(LuaParser.ELSEIF)
                self.state = 134
                self.exp(0)
                self.state = 135
                self.match(LuaParser.THEN)
                self.state = 136
                self.block()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 143
                self.match(LuaParser.ELSE)
                self.state = 144
                self.block()


            self.state = 147
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return LuaParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = LuaParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(LuaParser.FOR)
            self.state = 150
            self.match(LuaParser.NAME)
            self.state = 151
            self.match(LuaParser.EQ)
            self.state = 152
            self.exp(0)
            self.state = 153
            self.match(LuaParser.COMMA)
            self.state = 154
            self.exp(0)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 155
                self.match(LuaParser.COMMA)
                self.state = 156
                self.exp(0)


            self.state = 159
            self.match(LuaParser.DO)
            self.state = 160
            self.block()
            self.state = 161
            self.match(LuaParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LuaParser.FOR, 0)

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def IN(self):
            return self.getToken(LuaParser.IN, 0)

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def DO(self):
            return self.getToken(LuaParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def END(self):
            return self.getToken(LuaParser.END, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_forin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForin" ):
                listener.enterForin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForin" ):
                listener.exitForin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin" ):
                return visitor.visitForin(self)
            else:
                return visitor.visitChildren(self)




    def forin(self):

        localctx = LuaParser.ForinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LuaParser.FOR)
            self.state = 164
            self.namelist()
            self.state = 165
            self.match(LuaParser.IN)
            self.state = 166
            self.explist()
            self.state = 167
            self.match(LuaParser.DO)
            self.state = 168
            self.block()
            self.state = 169
            self.match(LuaParser.END)
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

        def funcname(self):
            return self.getTypedRuleContext(LuaParser.FuncnameContext,0)


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
        self.enterRule(localctx, 24, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(LuaParser.FUNCTION)
            self.state = 172
            self.funcname()
            self.state = 173
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalfunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCAL(self):
            return self.getToken(LuaParser.LOCAL, 0)

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_localfunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalfunction" ):
                listener.enterLocalfunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalfunction" ):
                listener.exitLocalfunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalfunction" ):
                return visitor.visitLocalfunction(self)
            else:
                return visitor.visitChildren(self)




    def localfunction(self):

        localctx = LuaParser.LocalfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_localfunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LuaParser.LOCAL)
            self.state = 176
            self.match(LuaParser.FUNCTION)
            self.state = 177
            self.match(LuaParser.NAME)
            self.state = 178
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCAL(self):
            return self.getToken(LuaParser.LOCAL, 0)

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_localassign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalassign" ):
                listener.enterLocalassign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalassign" ):
                listener.exitLocalassign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalassign" ):
                return visitor.visitLocalassign(self)
            else:
                return visitor.visitChildren(self)




    def localassign(self):

        localctx = LuaParser.LocalassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_localassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(LuaParser.LOCAL)
            self.state = 181
            self.namelist()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 182
                self.match(LuaParser.EQ)
                self.state = 183
                self.explist()


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttnamelist" ):
                return visitor.visitAttnamelist(self)
            else:
                return visitor.visitChildren(self)




    def attnamelist(self):

        localctx = LuaParser.AttnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_attnamelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(LuaParser.NAME)
            self.state = 187
            self.attrib()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 188
                self.match(LuaParser.COMMA)
                self.state = 189
                self.match(LuaParser.NAME)
                self.state = 190
                self.attrib()
                self.state = 195
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrib" ):
                return visitor.visitAttrib(self)
            else:
                return visitor.visitChildren(self)




    def attrib(self):

        localctx = LuaParser.AttribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attrib)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 196
                self.match(LuaParser.LT)
                self.state = 197
                self.match(LuaParser.NAME)
                self.state = 198
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
        self.enterRule(localctx, 34, self.RULE_retstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 201
                self.match(LuaParser.RETURN)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 202
                    self.explist()


                pass
            elif token in [3]:
                self.state = 205
                self.match(LuaParser.BREAK)
                pass
            elif token in [22]:
                self.state = 206
                self.match(LuaParser.CONTINUE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 209
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
        self.enterRule(localctx, 36, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(LuaParser.CC)
            self.state = 213
            self.match(LuaParser.NAME)
            self.state = 214
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
        self.enterRule(localctx, 38, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(LuaParser.NAME)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 217
                self.match(LuaParser.DOT)
                self.state = 218
                self.match(LuaParser.NAME)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 224
                self.match(LuaParser.COL)
                self.state = 225
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
        self.enterRule(localctx, 40, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.var()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 229
                self.match(LuaParser.COMMA)
                self.state = 230
                self.var()
                self.state = 235
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
        self.enterRule(localctx, 42, self.RULE_namelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(LuaParser.NAME)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self.match(LuaParser.COMMA)
                    self.state = 238
                    self.match(LuaParser.NAME) 
                self.state = 243
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
        self.enterRule(localctx, 44, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.exp(0)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 245
                self.match(LuaParser.COMMA)
                self.state = 246
                self.exp(0)
                self.state = 251
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 253
                self.match(LuaParser.NIL)
                pass
            elif token in [25]:
                self.state = 254
                self.match(LuaParser.FALSE)
                pass
            elif token in [26]:
                self.state = 255
                self.match(LuaParser.TRUE)
                pass
            elif token in [61, 62, 63, 64]:
                self.state = 256
                self.number()
                pass
            elif token in [58, 59, 60]:
                self.state = 257
                self.string()
                pass
            elif token in [55]:
                self.state = 258
                self.match(LuaParser.DDD)
                pass
            elif token in [17]:
                self.state = 259
                self.functiondef()
                pass
            elif token in [31, 57]:
                self.state = 260
                self.prefixexp()
                pass
            elif token in [46]:
                self.state = 261
                self.tableconstructor()
                pass
            elif token in [28, 29, 30, 33]:
                self.state = 262
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10468982784) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.exp(8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 290
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 266
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")

                        self.state = 267
                        self.match(LuaParser.CARET)
                        self.state = 268
                        self.exp(9)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 269
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 270
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18049995198431232) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 271
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 272
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 273
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==44):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 274
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 275
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 276
                        self.match(LuaParser.DD)
                        self.state = 277
                        self.exp(5)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 278
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 279
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 73186792481226752) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 280
                        self.exp(5)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 281
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 282
                        self.match(LuaParser.AND)
                        self.state = 283
                        self.exp(4)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 284
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 285
                        self.match(LuaParser.OR)
                        self.state = 286
                        self.exp(3)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 287
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 288
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503720154890240) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 289
                        self.exp(2)
                        pass

             
                self.state = 294
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
        self.enterRule(localctx, 48, self.RULE_var)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.prefixexp()
                self.state = 297
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
        self.enterRule(localctx, 50, self.RULE_prefixexp)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(LuaParser.NAME)
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 302
                        self.tail() 
                    self.state = 307
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.functioncall(0)
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 309
                        self.tail() 
                    self.state = 314
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(LuaParser.OP)
                self.state = 316
                self.exp(0)
                self.state = 317
                self.match(LuaParser.CP)
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 318
                        self.tail() 
                    self.state = 323
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

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def OP(self):
            return self.getToken(LuaParser.OP, 0)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctioncall" ):
                return visitor.visitFunctioncall(self)
            else:
                return visitor.visitChildren(self)



    def functioncall(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.FunctioncallContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_functioncall, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 327
                self.match(LuaParser.NAME)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 328
                    self.tail()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 334
                self.args()
                pass

            elif la_ == 2:
                self.state = 335
                self.match(LuaParser.OP)
                self.state = 336
                self.exp(0)
                self.state = 337
                self.match(LuaParser.CP)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 338
                    self.tail()
                    self.state = 343
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 344
                self.args()
                pass

            elif la_ == 3:
                self.state = 346
                self.match(LuaParser.NAME)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 347
                    self.tail()
                    self.state = 352
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 353
                self.match(LuaParser.COL)
                self.state = 354
                self.match(LuaParser.NAME)
                self.state = 355
                self.args()
                pass

            elif la_ == 4:
                self.state = 356
                self.match(LuaParser.OP)
                self.state = 357
                self.exp(0)
                self.state = 358
                self.match(LuaParser.CP)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27 or _la==48:
                    self.state = 359
                    self.tail()
                    self.state = 364
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 365
                self.match(LuaParser.COL)
                self.state = 366
                self.match(LuaParser.NAME)
                self.state = 367
                self.args()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 389
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.FunctioncallContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 371
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 375
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27 or _la==48:
                            self.state = 372
                            self.tail()
                            self.state = 377
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 378
                        self.args()
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.FunctioncallContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 379
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 383
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==27 or _la==48:
                            self.state = 380
                            self.tail()
                            self.state = 385
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 386
                        self.match(LuaParser.COL)
                        self.state = 387
                        self.match(LuaParser.NAME)
                        self.state = 388
                        self.args()
                        pass

             
                self.state = 393
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
        self.enterRule(localctx, 54, self.RULE_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 394
                self.match(LuaParser.OB)
                self.state = 395
                self.exp(0)
                self.state = 396
                self.match(LuaParser.CB)
                pass
            elif token in [27]:
                self.state = 398
                self.match(LuaParser.DOT)
                self.state = 399
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
        self.enterRule(localctx, 56, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(LuaParser.OP)
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 403
                    self.explist()


                self.state = 406
                self.match(LuaParser.CP)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.tableconstructor()
                pass
            elif token in [58, 59, 60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
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


    class AnonfunctiondefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)

        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_anonfunctiondef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnonfunctiondef" ):
                listener.enterAnonfunctiondef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnonfunctiondef" ):
                listener.exitAnonfunctiondef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnonfunctiondef" ):
                return visitor.visitAnonfunctiondef(self)
            else:
                return visitor.visitChildren(self)




    def anonfunctiondef(self):

        localctx = LuaParser.AnonfunctiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_anonfunctiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(LuaParser.FUNCTION)
            self.state = 412
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
        self.enterRule(localctx, 60, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(LuaParser.OP)
            self.state = 415
            self.parlist()
            self.state = 416
            self.match(LuaParser.CP)
            self.state = 417
            self.block()
            self.state = 418
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
        self.enterRule(localctx, 62, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.namelist()
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 421
                    self.match(LuaParser.COMMA)
                    self.state = 422
                    self.match(LuaParser.DDD)


                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
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
        self.enterRule(localctx, 64, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(LuaParser.OCU)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280653027441537) != 0):
                self.state = 430
                self.fieldlist()


            self.state = 433
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
        self.enterRule(localctx, 66, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.field()
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 436
                    self.fieldsep()
                    self.state = 437
                    self.field() 
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==15:
                self.state = 444
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
        self.enterRule(localctx, 68, self.RULE_field)
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(LuaParser.OB)
                self.state = 448
                self.exp(0)
                self.state = 449
                self.match(LuaParser.CB)
                self.state = 450
                self.match(LuaParser.EQ)
                self.state = 451
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(LuaParser.NAME)
                self.state = 454
                self.match(LuaParser.EQ)
                self.state = 455
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 456
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
        self.enterRule(localctx, 70, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
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
        self.enterRule(localctx, 72, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
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
        self.enterRule(localctx, 74, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
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
        self._predicates[23] = self.exp_sempred
        self._predicates[26] = self.functioncall_sempred
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
         




