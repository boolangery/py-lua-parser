# Generated from luaparser/parser/LuaParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if "." in __name__:
    from .LuaParserBase import LuaParserBase
else:
    from LuaParserBase import LuaParserBase

def serializedATN():
    return [
        4,1,68,492,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,1,1,1,1,2,
        5,2,69,8,2,10,2,12,2,72,9,2,1,2,3,2,75,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,111,8,3,10,
        3,12,3,114,9,3,1,3,1,3,3,3,118,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,130,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,157,
        8,3,3,3,159,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,171,
        8,4,1,4,1,4,1,4,3,4,176,8,4,1,4,3,4,179,8,4,1,5,3,5,182,8,5,1,5,
        1,5,1,5,5,5,187,8,5,10,5,12,5,190,9,5,1,6,1,6,3,6,194,8,6,1,7,1,
        7,1,7,1,7,1,8,1,8,3,8,202,8,8,1,8,3,8,205,8,8,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,5,10,214,8,10,10,10,12,10,217,9,10,1,10,1,10,3,10,221,
        8,10,1,11,1,11,1,11,5,11,226,8,11,10,11,12,11,229,9,11,1,12,1,12,
        1,12,5,12,234,8,12,10,12,12,12,237,9,12,1,13,1,13,1,13,5,13,242,
        8,13,10,13,12,13,245,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,3,14,259,8,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,5,14,294,8,14,10,14,12,14,297,9,14,1,15,1,15,1,15,1,15,3,15,
        303,8,15,1,16,1,16,5,16,307,8,16,10,16,12,16,310,9,16,1,16,1,16,
        1,16,5,16,315,8,16,10,16,12,16,318,9,16,1,16,1,16,1,16,1,16,5,16,
        324,8,16,10,16,12,16,327,9,16,3,16,329,8,16,1,17,1,17,1,17,4,17,
        334,8,17,11,17,12,17,335,1,17,1,17,1,17,1,17,4,17,342,8,17,11,17,
        12,17,343,1,17,1,17,5,17,348,8,17,10,17,12,17,351,9,17,1,17,1,17,
        1,17,1,17,5,17,357,8,17,10,17,12,17,360,9,17,1,17,1,17,1,17,1,17,
        5,17,366,8,17,10,17,12,17,369,9,17,1,17,1,17,1,17,1,17,5,17,375,
        8,17,10,17,12,17,378,9,17,3,17,380,8,17,1,17,1,17,4,17,384,8,17,
        11,17,12,17,385,1,17,1,17,5,17,390,8,17,10,17,12,17,393,9,17,1,17,
        1,17,1,17,1,17,5,17,399,8,17,10,17,12,17,402,9,17,5,17,404,8,17,
        10,17,12,17,407,9,17,1,18,5,18,410,8,18,10,18,12,18,413,9,18,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,423,8,19,1,20,1,20,3,20,
        427,8,20,1,20,1,20,1,20,3,20,432,8,20,1,21,1,21,1,21,1,22,1,22,1,
        22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,446,8,23,1,23,1,23,3,23,450,
        8,23,1,24,1,24,3,24,454,8,24,1,25,1,25,3,25,458,8,25,1,25,1,25,1,
        26,1,26,1,26,1,26,5,26,466,8,26,10,26,12,26,469,9,26,1,26,3,26,472,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,484,
        8,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,0,2,28,34,31,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,0,8,2,0,27,29,32,32,3,0,36,37,44,44,53,53,2,0,28,28,43,
        43,1,0,33,34,4,0,19,20,39,40,49,49,55,55,2,0,1,1,15,15,1,0,60,63,
        1,0,57,59,549,0,62,1,0,0,0,2,65,1,0,0,0,4,70,1,0,0,0,6,158,1,0,0,
        0,8,178,1,0,0,0,10,181,1,0,0,0,12,191,1,0,0,0,14,195,1,0,0,0,16,
        199,1,0,0,0,18,206,1,0,0,0,20,210,1,0,0,0,22,222,1,0,0,0,24,230,
        1,0,0,0,26,238,1,0,0,0,28,258,1,0,0,0,30,302,1,0,0,0,32,328,1,0,
        0,0,34,379,1,0,0,0,36,411,1,0,0,0,38,422,1,0,0,0,40,431,1,0,0,0,
        42,433,1,0,0,0,44,436,1,0,0,0,46,449,1,0,0,0,48,451,1,0,0,0,50,455,
        1,0,0,0,52,461,1,0,0,0,54,483,1,0,0,0,56,485,1,0,0,0,58,487,1,0,
        0,0,60,489,1,0,0,0,62,63,3,2,1,0,63,64,5,0,0,1,64,1,1,0,0,0,65,66,
        3,4,2,0,66,3,1,0,0,0,67,69,3,6,3,0,68,67,1,0,0,0,69,72,1,0,0,0,70,
        68,1,0,0,0,70,71,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,73,75,3,16,
        8,0,74,73,1,0,0,0,74,75,1,0,0,0,75,5,1,0,0,0,76,159,5,1,0,0,77,78,
        3,22,11,0,78,79,5,2,0,0,79,80,3,26,13,0,80,159,1,0,0,0,81,159,3,
        34,17,0,82,159,3,18,9,0,83,159,5,3,0,0,84,85,5,4,0,0,85,159,5,56,
        0,0,86,87,5,5,0,0,87,88,3,4,2,0,88,89,5,6,0,0,89,159,1,0,0,0,90,
        91,5,7,0,0,91,92,3,28,14,0,92,93,5,5,0,0,93,94,3,4,2,0,94,95,5,6,
        0,0,95,159,1,0,0,0,96,97,5,8,0,0,97,98,3,4,2,0,98,99,5,9,0,0,99,
        100,3,28,14,0,100,159,1,0,0,0,101,102,5,10,0,0,102,103,3,28,14,0,
        103,104,5,11,0,0,104,112,3,4,2,0,105,106,5,12,0,0,106,107,3,28,14,
        0,107,108,5,11,0,0,108,109,3,4,2,0,109,111,1,0,0,0,110,105,1,0,0,
        0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,117,1,0,0,
        0,114,112,1,0,0,0,115,116,5,13,0,0,116,118,3,4,2,0,117,115,1,0,0,
        0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,5,6,0,0,120,159,1,0,0,
        0,121,122,5,14,0,0,122,123,5,56,0,0,123,124,5,2,0,0,124,125,3,28,
        14,0,125,126,5,15,0,0,126,129,3,28,14,0,127,128,5,15,0,0,128,130,
        3,28,14,0,129,127,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,
        5,5,0,0,132,133,3,4,2,0,133,134,5,6,0,0,134,159,1,0,0,0,135,136,
        5,14,0,0,136,137,3,24,12,0,137,138,5,16,0,0,138,139,3,26,13,0,139,
        140,5,5,0,0,140,141,3,4,2,0,141,142,5,6,0,0,142,159,1,0,0,0,143,
        144,5,17,0,0,144,145,3,20,10,0,145,146,3,44,22,0,146,159,1,0,0,0,
        147,148,5,18,0,0,148,149,5,17,0,0,149,150,5,56,0,0,150,159,3,44,
        22,0,151,159,3,8,4,0,152,153,5,18,0,0,153,156,3,10,5,0,154,155,5,
        2,0,0,155,157,3,26,13,0,156,154,1,0,0,0,156,157,1,0,0,0,157,159,
        1,0,0,0,158,76,1,0,0,0,158,77,1,0,0,0,158,81,1,0,0,0,158,82,1,0,
        0,0,158,83,1,0,0,0,158,84,1,0,0,0,158,86,1,0,0,0,158,90,1,0,0,0,
        158,96,1,0,0,0,158,101,1,0,0,0,158,121,1,0,0,0,158,135,1,0,0,0,158,
        143,1,0,0,0,158,147,1,0,0,0,158,151,1,0,0,0,158,152,1,0,0,0,159,
        7,1,0,0,0,160,161,4,4,0,0,161,162,5,56,0,0,162,163,5,17,0,0,163,
        164,5,56,0,0,164,179,3,44,22,0,165,166,4,4,1,0,166,167,5,56,0,0,
        167,170,3,10,5,0,168,169,5,2,0,0,169,171,3,26,13,0,170,168,1,0,0,
        0,170,171,1,0,0,0,171,179,1,0,0,0,172,173,4,4,2,0,173,175,5,56,0,
        0,174,176,3,14,7,0,175,174,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,
        0,177,179,5,44,0,0,178,160,1,0,0,0,178,165,1,0,0,0,178,172,1,0,0,
        0,179,9,1,0,0,0,180,182,3,14,7,0,181,180,1,0,0,0,181,182,1,0,0,0,
        182,183,1,0,0,0,183,188,3,12,6,0,184,185,5,15,0,0,185,187,3,12,6,
        0,186,184,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,
        0,189,11,1,0,0,0,190,188,1,0,0,0,191,193,5,56,0,0,192,194,3,14,7,
        0,193,192,1,0,0,0,193,194,1,0,0,0,194,13,1,0,0,0,195,196,5,19,0,
        0,196,197,5,56,0,0,197,198,5,20,0,0,198,15,1,0,0,0,199,201,5,21,
        0,0,200,202,3,26,13,0,201,200,1,0,0,0,201,202,1,0,0,0,202,204,1,
        0,0,0,203,205,5,1,0,0,204,203,1,0,0,0,204,205,1,0,0,0,205,17,1,0,
        0,0,206,207,5,22,0,0,207,208,5,56,0,0,208,209,5,22,0,0,209,19,1,
        0,0,0,210,215,5,56,0,0,211,212,5,26,0,0,212,214,5,56,0,0,213,211,
        1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,220,
        1,0,0,0,217,215,1,0,0,0,218,219,5,38,0,0,219,221,5,56,0,0,220,218,
        1,0,0,0,220,221,1,0,0,0,221,21,1,0,0,0,222,227,3,30,15,0,223,224,
        5,15,0,0,224,226,3,30,15,0,225,223,1,0,0,0,226,229,1,0,0,0,227,225,
        1,0,0,0,227,228,1,0,0,0,228,23,1,0,0,0,229,227,1,0,0,0,230,235,5,
        56,0,0,231,232,5,15,0,0,232,234,5,56,0,0,233,231,1,0,0,0,234,237,
        1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,25,1,0,0,0,237,235,1,
        0,0,0,238,243,3,28,14,0,239,240,5,15,0,0,240,242,3,28,14,0,241,239,
        1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,27,1,
        0,0,0,245,243,1,0,0,0,246,247,6,14,-1,0,247,259,5,23,0,0,248,259,
        5,24,0,0,249,259,5,25,0,0,250,259,3,58,29,0,251,259,3,60,30,0,252,
        259,5,54,0,0,253,259,3,42,21,0,254,259,3,32,16,0,255,259,3,50,25,
        0,256,257,7,0,0,0,257,259,3,28,14,11,258,246,1,0,0,0,258,248,1,0,
        0,0,258,249,1,0,0,0,258,250,1,0,0,0,258,251,1,0,0,0,258,252,1,0,
        0,0,258,253,1,0,0,0,258,254,1,0,0,0,258,255,1,0,0,0,258,256,1,0,
        0,0,259,295,1,0,0,0,260,261,10,12,0,0,261,262,5,52,0,0,262,294,3,
        28,14,12,263,264,10,10,0,0,264,265,7,1,0,0,265,294,3,28,14,11,266,
        267,10,9,0,0,267,268,7,2,0,0,268,294,3,28,14,10,269,270,10,8,0,0,
        270,271,5,50,0,0,271,294,3,28,14,8,272,273,10,7,0,0,273,274,7,3,
        0,0,274,294,3,28,14,8,275,276,10,6,0,0,276,277,5,35,0,0,277,294,
        3,28,14,7,278,279,10,5,0,0,279,280,5,27,0,0,280,294,3,28,14,6,281,
        282,10,4,0,0,282,283,5,51,0,0,283,294,3,28,14,5,284,285,10,3,0,0,
        285,286,7,4,0,0,286,294,3,28,14,4,287,288,10,2,0,0,288,289,5,41,
        0,0,289,294,3,28,14,3,290,291,10,1,0,0,291,292,5,42,0,0,292,294,
        3,28,14,2,293,260,1,0,0,0,293,263,1,0,0,0,293,266,1,0,0,0,293,269,
        1,0,0,0,293,272,1,0,0,0,293,275,1,0,0,0,293,278,1,0,0,0,293,281,
        1,0,0,0,293,284,1,0,0,0,293,287,1,0,0,0,293,290,1,0,0,0,294,297,
        1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,29,1,0,0,0,297,295,1,
        0,0,0,298,303,5,56,0,0,299,300,3,32,16,0,300,301,3,38,19,0,301,303,
        1,0,0,0,302,298,1,0,0,0,302,299,1,0,0,0,303,31,1,0,0,0,304,308,3,
        34,17,0,305,307,3,38,19,0,306,305,1,0,0,0,307,310,1,0,0,0,308,306,
        1,0,0,0,308,309,1,0,0,0,309,329,1,0,0,0,310,308,1,0,0,0,311,312,
        4,16,14,0,312,316,5,56,0,0,313,315,3,38,19,0,314,313,1,0,0,0,315,
        318,1,0,0,0,316,314,1,0,0,0,316,317,1,0,0,0,317,329,1,0,0,0,318,
        316,1,0,0,0,319,320,5,30,0,0,320,321,3,28,14,0,321,325,5,31,0,0,
        322,324,3,38,19,0,323,322,1,0,0,0,324,327,1,0,0,0,325,323,1,0,0,
        0,325,326,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,328,304,1,0,0,
        0,328,311,1,0,0,0,328,319,1,0,0,0,329,33,1,0,0,0,330,331,6,17,-1,
        0,331,333,5,56,0,0,332,334,3,36,18,0,333,332,1,0,0,0,334,335,1,0,
        0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,380,1,0,0,0,337,338,5,30,
        0,0,338,339,3,28,14,0,339,341,5,31,0,0,340,342,3,36,18,0,341,340,
        1,0,0,0,342,343,1,0,0,0,343,341,1,0,0,0,343,344,1,0,0,0,344,380,
        1,0,0,0,345,349,5,56,0,0,346,348,3,38,19,0,347,346,1,0,0,0,348,351,
        1,0,0,0,349,347,1,0,0,0,349,350,1,0,0,0,350,352,1,0,0,0,351,349,
        1,0,0,0,352,353,5,38,0,0,353,354,5,56,0,0,354,358,3,40,20,0,355,
        357,3,36,18,0,356,355,1,0,0,0,357,360,1,0,0,0,358,356,1,0,0,0,358,
        359,1,0,0,0,359,380,1,0,0,0,360,358,1,0,0,0,361,362,5,30,0,0,362,
        363,3,28,14,0,363,367,5,31,0,0,364,366,3,38,19,0,365,364,1,0,0,0,
        366,369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,
        369,367,1,0,0,0,370,371,5,38,0,0,371,372,5,56,0,0,372,376,3,40,20,
        0,373,375,3,36,18,0,374,373,1,0,0,0,375,378,1,0,0,0,376,374,1,0,
        0,0,376,377,1,0,0,0,377,380,1,0,0,0,378,376,1,0,0,0,379,330,1,0,
        0,0,379,337,1,0,0,0,379,345,1,0,0,0,379,361,1,0,0,0,380,405,1,0,
        0,0,381,383,10,5,0,0,382,384,3,36,18,0,383,382,1,0,0,0,384,385,1,
        0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,404,1,0,0,0,387,391,10,
        2,0,0,388,390,3,38,19,0,389,388,1,0,0,0,390,393,1,0,0,0,391,389,
        1,0,0,0,391,392,1,0,0,0,392,394,1,0,0,0,393,391,1,0,0,0,394,395,
        5,38,0,0,395,396,5,56,0,0,396,400,3,40,20,0,397,399,3,36,18,0,398,
        397,1,0,0,0,399,402,1,0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,
        404,1,0,0,0,402,400,1,0,0,0,403,381,1,0,0,0,403,387,1,0,0,0,404,
        407,1,0,0,0,405,403,1,0,0,0,405,406,1,0,0,0,406,35,1,0,0,0,407,405,
        1,0,0,0,408,410,3,38,19,0,409,408,1,0,0,0,410,413,1,0,0,0,411,409,
        1,0,0,0,411,412,1,0,0,0,412,414,1,0,0,0,413,411,1,0,0,0,414,415,
        3,40,20,0,415,37,1,0,0,0,416,417,5,47,0,0,417,418,3,28,14,0,418,
        419,5,48,0,0,419,423,1,0,0,0,420,421,5,26,0,0,421,423,5,56,0,0,422,
        416,1,0,0,0,422,420,1,0,0,0,423,39,1,0,0,0,424,426,5,30,0,0,425,
        427,3,26,13,0,426,425,1,0,0,0,426,427,1,0,0,0,427,428,1,0,0,0,428,
        432,5,31,0,0,429,432,3,50,25,0,430,432,3,60,30,0,431,424,1,0,0,0,
        431,429,1,0,0,0,431,430,1,0,0,0,432,41,1,0,0,0,433,434,5,17,0,0,
        434,435,3,44,22,0,435,43,1,0,0,0,436,437,5,30,0,0,437,438,3,46,23,
        0,438,439,5,31,0,0,439,440,3,4,2,0,440,441,5,6,0,0,441,45,1,0,0,
        0,442,445,3,24,12,0,443,444,5,15,0,0,444,446,3,48,24,0,445,443,1,
        0,0,0,445,446,1,0,0,0,446,450,1,0,0,0,447,450,3,48,24,0,448,450,
        1,0,0,0,449,442,1,0,0,0,449,447,1,0,0,0,449,448,1,0,0,0,450,47,1,
        0,0,0,451,453,5,54,0,0,452,454,5,56,0,0,453,452,1,0,0,0,453,454,
        1,0,0,0,454,49,1,0,0,0,455,457,5,45,0,0,456,458,3,52,26,0,457,456,
        1,0,0,0,457,458,1,0,0,0,458,459,1,0,0,0,459,460,5,46,0,0,460,51,
        1,0,0,0,461,467,3,54,27,0,462,463,3,56,28,0,463,464,3,54,27,0,464,
        466,1,0,0,0,465,462,1,0,0,0,466,469,1,0,0,0,467,465,1,0,0,0,467,
        468,1,0,0,0,468,471,1,0,0,0,469,467,1,0,0,0,470,472,3,56,28,0,471,
        470,1,0,0,0,471,472,1,0,0,0,472,53,1,0,0,0,473,474,5,47,0,0,474,
        475,3,28,14,0,475,476,5,48,0,0,476,477,5,2,0,0,477,478,3,28,14,0,
        478,484,1,0,0,0,479,480,5,56,0,0,480,481,5,2,0,0,481,484,3,28,14,
        0,482,484,3,28,14,0,483,473,1,0,0,0,483,479,1,0,0,0,483,482,1,0,
        0,0,484,55,1,0,0,0,485,486,7,5,0,0,486,57,1,0,0,0,487,488,7,6,0,
        0,488,59,1,0,0,0,489,490,7,7,0,0,490,61,1,0,0,0,51,70,74,112,117,
        129,156,158,170,175,178,181,188,193,201,204,215,220,227,235,243,
        258,293,295,302,308,316,325,328,335,343,349,358,367,376,379,385,
        391,400,403,405,411,422,426,431,445,449,453,457,467,471,483
    ]

class LuaParser ( LuaParserBase ):

    grammarFileName = "LuaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'break'", "'goto'", "'do'", 
                     "'end'", "'while'", "'repeat'", "'until'", "'if'", 
                     "'then'", "'elseif'", "'else'", "'for'", "','", "'in'", 
                     "'function'", "'local'", "'<'", "'>'", "'return'", 
                     "'::'", "'nil'", "'false'", "'true'", "'.'", "'~'", 
                     "'-'", "'#'", "'('", "')'", "'not'", "'<<'", "'>>'", 
                     "'&'", "'//'", "'%'", "':'", "'<='", "'>='", "'and'", 
                     "'or'", "'+'", "'*'", "'{'", "'}'", "'['", "']'", "'=='", 
                     "'..'", "'|'", "'^'", "'/'", "'...'", "'~='" ]

    symbolicNames = [ "<INVALID>", "SEMI", "EQ", "BREAK", "GOTO", "DO", 
                      "END", "WHILE", "REPEAT", "UNTIL", "IF", "THEN", "ELSEIF", 
                      "ELSE", "FOR", "COMMA", "IN", "FUNCTION", "LOCAL", 
                      "LT", "GT", "RETURN", "CC", "NIL", "FALSE", "TRUE", 
                      "DOT", "SQUIG", "MINUS", "POUND", "OP", "CP", "NOT", 
                      "LL", "GG", "AMP", "SS", "PER", "COL", "LE", "GE", 
                      "AND", "OR", "PLUS", "STAR", "OCU", "CCU", "OB", "CB", 
                      "EE", "DD", "PIPE", "CARET", "SLASH", "DDD", "SQEQ", 
                      "NAME", "NORMALSTRING", "CHARSTRING", "LONGSTRING", 
                      "INT", "HEX", "FLOAT", "HEX_FLOAT", "COMMENT", "LINE_COMMENT", 
                      "WS", "NL", "SHEBANG" ]

    RULE_start_ = 0
    RULE_chunk = 1
    RULE_block = 2
    RULE_stat = 3
    RULE_globalstat = 4
    RULE_attnamelist = 5
    RULE_nameattrib = 6
    RULE_attrib = 7
    RULE_retstat = 8
    RULE_label = 9
    RULE_funcname = 10
    RULE_varlist = 11
    RULE_namelist = 12
    RULE_explist = 13
    RULE_exp = 14
    RULE_var = 15
    RULE_prefixexp = 16
    RULE_functioncall = 17
    RULE_call = 18
    RULE_tail = 19
    RULE_args = 20
    RULE_functiondef = 21
    RULE_funcbody = 22
    RULE_parlist = 23
    RULE_varargparam = 24
    RULE_tableconstructor = 25
    RULE_fieldlist = 26
    RULE_field = 27
    RULE_fieldsep = 28
    RULE_number = 29
    RULE_string = 30

    ruleNames =  [ "start_", "chunk", "block", "stat", "globalstat", "attnamelist", 
                   "nameattrib", "attrib", "retstat", "label", "funcname", 
                   "varlist", "namelist", "explist", "exp", "var", "prefixexp", 
                   "functioncall", "call", "tail", "args", "functiondef", 
                   "funcbody", "parlist", "varargparam", "tableconstructor", 
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
    CC=22
    NIL=23
    FALSE=24
    TRUE=25
    DOT=26
    SQUIG=27
    MINUS=28
    POUND=29
    OP=30
    CP=31
    NOT=32
    LL=33
    GG=34
    AMP=35
    SS=36
    PER=37
    COL=38
    LE=39
    GE=40
    AND=41
    OR=42
    PLUS=43
    STAR=44
    OCU=45
    CCU=46
    OB=47
    CB=48
    EE=49
    DD=50
    PIPE=51
    CARET=52
    SLASH=53
    DDD=54
    SQEQ=55
    NAME=56
    NORMALSTRING=57
    CHARSTRING=58
    LONGSTRING=59
    INT=60
    HEX=61
    FLOAT=62
    HEX_FLOAT=63
    COMMENT=64
    LINE_COMMENT=65
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
            self.state = 62
            self.chunk()
            self.state = 63
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
            self.state = 65
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
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self.stat() 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 73
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


    class Stat_globalContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def globalstat(self):
            return self.getTypedRuleContext(LuaParser.GlobalstatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_global" ):
                listener.enterStat_global(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_global" ):
                listener.exitStat_global(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_global" ):
                return visitor.visitStat_global(self)
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
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Stat_emptyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(LuaParser.SEMI)
                pass

            elif la_ == 2:
                localctx = LuaParser.Stat_assignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.varlist()
                self.state = 78
                self.match(LuaParser.EQ)
                self.state = 79
                self.explist()
                pass

            elif la_ == 3:
                localctx = LuaParser.Stat_functioncallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.functioncall(0)
                pass

            elif la_ == 4:
                localctx = LuaParser.Stat_labelContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.label()
                pass

            elif la_ == 5:
                localctx = LuaParser.Stat_breakContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 6:
                localctx = LuaParser.Stat_gotoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.match(LuaParser.GOTO)
                self.state = 85
                self.match(LuaParser.NAME)
                pass

            elif la_ == 7:
                localctx = LuaParser.Stat_doContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 86
                self.match(LuaParser.DO)
                self.state = 87
                self.block()
                self.state = 88
                self.match(LuaParser.END)
                pass

            elif la_ == 8:
                localctx = LuaParser.Stat_whileContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 90
                self.match(LuaParser.WHILE)
                self.state = 91
                self.exp(0)
                self.state = 92
                self.match(LuaParser.DO)
                self.state = 93
                self.block()
                self.state = 94
                self.match(LuaParser.END)
                pass

            elif la_ == 9:
                localctx = LuaParser.Stat_repeatContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 96
                self.match(LuaParser.REPEAT)
                self.state = 97
                self.block()
                self.state = 98
                self.match(LuaParser.UNTIL)
                self.state = 99
                self.exp(0)
                pass

            elif la_ == 10:
                localctx = LuaParser.Stat_ifContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 101
                self.match(LuaParser.IF)
                self.state = 102
                self.exp(0)
                self.state = 103
                self.match(LuaParser.THEN)
                self.state = 104
                self.block()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 105
                    self.match(LuaParser.ELSEIF)
                    self.state = 106
                    self.exp(0)
                    self.state = 107
                    self.match(LuaParser.THEN)
                    self.state = 108
                    self.block()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 115
                    self.match(LuaParser.ELSE)
                    self.state = 116
                    self.block()


                self.state = 119
                self.match(LuaParser.END)
                pass

            elif la_ == 11:
                localctx = LuaParser.Stat_forContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 121
                self.match(LuaParser.FOR)
                self.state = 122
                self.match(LuaParser.NAME)
                self.state = 123
                self.match(LuaParser.EQ)
                self.state = 124
                self.exp(0)
                self.state = 125
                self.match(LuaParser.COMMA)
                self.state = 126
                self.exp(0)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 127
                    self.match(LuaParser.COMMA)
                    self.state = 128
                    self.exp(0)


                self.state = 131
                self.match(LuaParser.DO)
                self.state = 132
                self.block()
                self.state = 133
                self.match(LuaParser.END)
                pass

            elif la_ == 12:
                localctx = LuaParser.Stat_forContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 135
                self.match(LuaParser.FOR)
                self.state = 136
                self.namelist()
                self.state = 137
                self.match(LuaParser.IN)
                self.state = 138
                self.explist()
                self.state = 139
                self.match(LuaParser.DO)
                self.state = 140
                self.block()
                self.state = 141
                self.match(LuaParser.END)
                pass

            elif la_ == 13:
                localctx = LuaParser.Stat_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 143
                self.match(LuaParser.FUNCTION)
                self.state = 144
                self.funcname()
                self.state = 145
                self.funcbody()
                pass

            elif la_ == 14:
                localctx = LuaParser.Stat_localfunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 147
                self.match(LuaParser.LOCAL)
                self.state = 148
                self.match(LuaParser.FUNCTION)
                self.state = 149
                self.match(LuaParser.NAME)
                self.state = 150
                self.funcbody()
                pass

            elif la_ == 15:
                localctx = LuaParser.Stat_globalContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 151
                self.globalstat()
                pass

            elif la_ == 16:
                localctx = LuaParser.Stat_localContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 152
                self.match(LuaParser.LOCAL)
                self.state = 153
                self.attnamelist()
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 154
                    self.match(LuaParser.EQ)
                    self.state = 155
                    self.explist()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_globalstat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Globalstat_functionContext(GlobalstatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.GlobalstatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LuaParser.NAME)
            else:
                return self.getToken(LuaParser.NAME, i)
        def FUNCTION(self):
            return self.getToken(LuaParser.FUNCTION, 0)
        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalstat_function" ):
                listener.enterGlobalstat_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalstat_function" ):
                listener.exitGlobalstat_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalstat_function" ):
                return visitor.visitGlobalstat_function(self)
            else:
                return visitor.visitChildren(self)


    class Globalstat_namesContext(GlobalstatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.GlobalstatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def attnamelist(self):
            return self.getTypedRuleContext(LuaParser.AttnamelistContext,0)

        def EQ(self):
            return self.getToken(LuaParser.EQ, 0)
        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalstat_names" ):
                listener.enterGlobalstat_names(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalstat_names" ):
                listener.exitGlobalstat_names(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalstat_names" ):
                return visitor.visitGlobalstat_names(self)
            else:
                return visitor.visitChildren(self)


    class Globalstat_wildcardContext(GlobalstatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.GlobalstatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)
        def STAR(self):
            return self.getToken(LuaParser.STAR, 0)
        def attrib(self):
            return self.getTypedRuleContext(LuaParser.AttribContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalstat_wildcard" ):
                listener.enterGlobalstat_wildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalstat_wildcard" ):
                listener.exitGlobalstat_wildcard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalstat_wildcard" ):
                return visitor.visitGlobalstat_wildcard(self)
            else:
                return visitor.visitChildren(self)



    def globalstat(self):

        localctx = LuaParser.GlobalstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_globalstat)
        self._la = 0 # Token type
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Globalstat_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                if not  self.IsGlobal() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " self.IsGlobal() ")
                self.state = 161
                self.match(LuaParser.NAME)
                self.state = 162
                self.match(LuaParser.FUNCTION)
                self.state = 163
                self.match(LuaParser.NAME)
                self.state = 164
                self.funcbody()
                pass

            elif la_ == 2:
                localctx = LuaParser.Globalstat_namesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                if not  self.IsGlobal() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " self.IsGlobal() ")
                self.state = 166
                self.match(LuaParser.NAME)
                self.state = 167
                self.attnamelist()
                self.state = 170
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 168
                    self.match(LuaParser.EQ)
                    self.state = 169
                    self.explist()


                pass

            elif la_ == 3:
                localctx = LuaParser.Globalstat_wildcardContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                if not  self.IsGlobal() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " self.IsGlobal() ")
                self.state = 173
                self.match(LuaParser.NAME)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 174
                    self.attrib()


                self.state = 177
                self.match(LuaParser.STAR)
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


        def attrib(self):
            return self.getTypedRuleContext(LuaParser.AttribContext,0)


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
        self.enterRule(localctx, 10, self.RULE_attnamelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 180
                self.attrib()


            self.state = 183
            self.nameattrib()
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 184
                    self.match(LuaParser.COMMA)
                    self.state = 185
                    self.nameattrib() 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_nameattrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(LuaParser.NAME)
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 192
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
        self.enterRule(localctx, 14, self.RULE_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(LuaParser.LT)
            self.state = 196
            self.match(LuaParser.NAME)
            self.state = 197
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

        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def SEMI(self):
            return self.getToken(LuaParser.SEMI, 0)

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
        self.enterRule(localctx, 16, self.RULE_retstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(LuaParser.RETURN)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 200
                self.explist()


            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 203
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
        self.enterRule(localctx, 18, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(LuaParser.CC)
            self.state = 207
            self.match(LuaParser.NAME)
            self.state = 208
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
        self.enterRule(localctx, 20, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(LuaParser.NAME)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 211
                self.match(LuaParser.DOT)
                self.state = 212
                self.match(LuaParser.NAME)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 218
                self.match(LuaParser.COL)
                self.state = 219
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
        self.enterRule(localctx, 22, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.var()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 223
                self.match(LuaParser.COMMA)
                self.state = 224
                self.var()
                self.state = 229
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
        self.enterRule(localctx, 24, self.RULE_namelist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(LuaParser.NAME)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 231
                    self.match(LuaParser.COMMA)
                    self.state = 232
                    self.match(LuaParser.NAME) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_explist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.exp(0)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 239
                    self.match(LuaParser.COMMA)
                    self.state = 240
                    self.exp(0) 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 247
                self.match(LuaParser.NIL)
                pass

            elif la_ == 2:
                self.state = 248
                self.match(LuaParser.FALSE)
                pass

            elif la_ == 3:
                self.state = 249
                self.match(LuaParser.TRUE)
                pass

            elif la_ == 4:
                self.state = 250
                self.number()
                pass

            elif la_ == 5:
                self.state = 251
                self.string()
                pass

            elif la_ == 6:
                self.state = 252
                self.match(LuaParser.DDD)
                pass

            elif la_ == 7:
                self.state = 253
                self.functiondef()
                pass

            elif la_ == 8:
                self.state = 254
                self.prefixexp()
                pass

            elif la_ == 9:
                self.state = 255
                self.tableconstructor()
                pass

            elif la_ == 10:
                self.state = 256
                localctx.unary_op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5234491392) != 0)):
                    localctx.unary_op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.exp(11)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 293
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 260
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")

                        self.state = 261
                        localctx.op = self.match(LuaParser.CARET)
                        self.state = 262
                        self.exp(12)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 263
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 264
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9024997599215616) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 265
                        self.exp(11)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 266
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 267
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==43):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 268
                        self.exp(10)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 269
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")

                        self.state = 270
                        localctx.op = self.match(LuaParser.DD)
                        self.state = 271
                        self.exp(8)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 272
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 273
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 274
                        self.exp(8)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 275
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 276
                        localctx.op = self.match(LuaParser.AMP)
                        self.state = 277
                        self.exp(7)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 278
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 279
                        localctx.op = self.match(LuaParser.SQUIG)
                        self.state = 280
                        self.exp(6)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 281
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 282
                        localctx.op = self.match(LuaParser.PIPE)
                        self.state = 283
                        self.exp(5)
                        pass

                    elif la_ == 9:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 284
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 285
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 36593396241399808) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 286
                        self.exp(4)
                        pass

                    elif la_ == 10:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 287
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 288
                        localctx.op = self.match(LuaParser.AND)
                        self.state = 289
                        self.exp(3)
                        pass

                    elif la_ == 11:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 290
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                        self.state = 291
                        localctx.op = self.match(LuaParser.OR)
                        self.state = 292
                        self.exp(2)
                        pass

             
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_var)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.prefixexp()
                self.state = 300
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

        def functioncall(self):
            return self.getTypedRuleContext(LuaParser.FunctioncallContext,0)


        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

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
        self.enterRule(localctx, 32, self.RULE_prefixexp)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.functioncall(0)
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 305
                        self.tail() 
                    self.state = 310
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                if not  self.IsFunctionCall() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " self.IsFunctionCall() ")
                self.state = 312
                self.match(LuaParser.NAME)
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 313
                        self.tail() 
                    self.state = 318
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.match(LuaParser.OP)
                self.state = 320
                self.exp(0)
                self.state = 321
                self.match(LuaParser.CP)
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 322
                        self.tail() 
                    self.state = 327
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.CallContext)
            else:
                return self.getTypedRuleContext(LuaParser.CallContext,i)


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

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.CallContext)
            else:
                return self.getTypedRuleContext(LuaParser.CallContext,i)


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

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.CallContext)
            else:
                return self.getTypedRuleContext(LuaParser.CallContext,i)


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

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.CallContext)
            else:
                return self.getTypedRuleContext(LuaParser.CallContext,i)


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
        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.CallContext)
            else:
                return self.getTypedRuleContext(LuaParser.CallContext,i)


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

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.CallContext)
            else:
                return self.getTypedRuleContext(LuaParser.CallContext,i)


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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_functioncall, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Functioncall_nameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 331
                self.match(LuaParser.NAME)
                self.state = 333 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 332
                        self.call()

                    else:
                        raise NoViableAltException(self)
                    self.state = 335 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 2:
                localctx = LuaParser.Functioncall_expContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 337
                self.match(LuaParser.OP)
                self.state = 338
                self.exp(0)
                self.state = 339
                self.match(LuaParser.CP)
                self.state = 341 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 340
                        self.call()

                    else:
                        raise NoViableAltException(self)
                    self.state = 343 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                pass

            elif la_ == 3:
                localctx = LuaParser.Functioncall_invokeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 345
                self.match(LuaParser.NAME)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26 or _la==47:
                    self.state = 346
                    self.tail()
                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 352
                self.match(LuaParser.COL)
                self.state = 353
                self.match(LuaParser.NAME)
                self.state = 354
                self.args()
                self.state = 358
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 355
                        self.call() 
                    self.state = 360
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass

            elif la_ == 4:
                localctx = LuaParser.Functioncall_expinvokeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 361
                self.match(LuaParser.OP)
                self.state = 362
                self.exp(0)
                self.state = 363
                self.match(LuaParser.CP)
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26 or _la==47:
                    self.state = 364
                    self.tail()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 370
                self.match(LuaParser.COL)
                self.state = 371
                self.match(LuaParser.NAME)
                self.state = 372
                self.args()
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 373
                        self.call() 
                    self.state = 378
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 403
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.Functioncall_nestedContext(self, LuaParser.FunctioncallContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 381
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 383 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 382
                                self.call()

                            else:
                                raise NoViableAltException(self)
                            self.state = 385 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                        pass

                    elif la_ == 2:
                        localctx = LuaParser.Functioncall_nestedinvokeContext(self, LuaParser.FunctioncallContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 387
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 391
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==26 or _la==47:
                            self.state = 388
                            self.tail()
                            self.state = 393
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 394
                        self.match(LuaParser.COL)
                        self.state = 395
                        self.match(LuaParser.NAME)
                        self.state = 396
                        self.args()
                        self.state = 400
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 397
                                self.call() 
                            self.state = 402
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

                        pass

             
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = LuaParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==47:
                self.state = 408
                self.tail()
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
            self.args()
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
        self.enterRule(localctx, 38, self.RULE_tail)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(LuaParser.OB)
                self.state = 417
                self.exp(0)
                self.state = 418
                self.match(LuaParser.CB)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(LuaParser.DOT)
                self.state = 421
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
        self.enterRule(localctx, 40, self.RULE_args)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(LuaParser.OP)
                self.state = 426
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 425
                    self.explist()


                self.state = 428
                self.match(LuaParser.CP)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.tableconstructor()
                pass
            elif token in [57, 58, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
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
        self.enterRule(localctx, 42, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(LuaParser.FUNCTION)
            self.state = 434
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
        self.enterRule(localctx, 44, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(LuaParser.OP)
            self.state = 437
            self.parlist()
            self.state = 438
            self.match(LuaParser.CP)
            self.state = 439
            self.block()
            self.state = 440
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

        def varargparam(self):
            return self.getTypedRuleContext(LuaParser.VarargparamContext,0)


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
        self.enterRule(localctx, 46, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.namelist()
                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 443
                    self.match(LuaParser.COMMA)
                    self.state = 444
                    self.varargparam()


                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.varargparam()
                pass
            elif token in [31]:
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


    class VarargparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DDD(self):
            return self.getToken(LuaParser.DDD, 0)

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_varargparam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarargparam" ):
                listener.enterVarargparam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarargparam" ):
                listener.exitVarargparam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarargparam" ):
                return visitor.visitVarargparam(self)
            else:
                return visitor.visitChildren(self)




    def varargparam(self):

        localctx = LuaParser.VarargparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_varargparam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(LuaParser.DDD)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 452
                self.match(LuaParser.NAME)


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
        self.enterRule(localctx, 50, self.RULE_tableconstructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(LuaParser.OCU)
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 456
                self.fieldlist()


            self.state = 459
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
        self.enterRule(localctx, 52, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.field()
            self.state = 467
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 462
                    self.fieldsep()
                    self.state = 463
                    self.field() 
                self.state = 469
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==15:
                self.state = 470
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
        self.enterRule(localctx, 54, self.RULE_field)
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(LuaParser.OB)
                self.state = 474
                self.exp(0)
                self.state = 475
                self.match(LuaParser.CB)
                self.state = 476
                self.match(LuaParser.EQ)
                self.state = 477
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(LuaParser.NAME)
                self.state = 480
                self.match(LuaParser.EQ)
                self.state = 481
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 482
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
        self.enterRule(localctx, 56, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
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
        self.enterRule(localctx, 58, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -1152921504606846976) != 0)):
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
        self.enterRule(localctx, 60, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008806316530991104) != 0)):
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
        self._predicates[4] = self.globalstat_sempred
        self._predicates[14] = self.exp_sempred
        self._predicates[16] = self.prefixexp_sempred
        self._predicates[17] = self.functioncall_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def globalstat_sempred(self, localctx:GlobalstatContext, predIndex:int):
            if predIndex == 0:
                return  self.IsGlobal() 
         

            if predIndex == 1:
                return  self.IsGlobal() 
         

            if predIndex == 2:
                return  self.IsGlobal() 
         

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

    def prefixexp_sempred(self, localctx:PrefixexpContext, predIndex:int):
            if predIndex == 14:
                return  self.IsFunctionCall() 
         

    def functioncall_sempred(self, localctx:FunctioncallContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         




