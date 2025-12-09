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
        4,1,68,463,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,1,1,1,1,2,5,2,65,8,2,10,2,12,2,
        68,9,2,1,2,3,2,71,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,107,8,3,10,3,12,3,110,9,3,1,3,
        1,3,3,3,114,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,126,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,152,8,3,3,3,154,8,3,1,4,
        1,4,1,4,5,4,159,8,4,10,4,12,4,162,9,4,1,5,1,5,3,5,166,8,5,1,6,1,
        6,1,6,1,6,1,7,1,7,3,7,174,8,7,1,7,3,7,177,8,7,1,7,3,7,180,8,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,189,8,9,10,9,12,9,192,9,9,1,9,1,9,
        3,9,196,8,9,1,10,1,10,1,10,5,10,201,8,10,10,10,12,10,204,9,10,1,
        11,1,11,1,11,5,11,209,8,11,10,11,12,11,212,9,11,1,12,1,12,1,12,5,
        12,217,8,12,10,12,12,12,220,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,234,8,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,5,13,269,8,13,10,13,12,13,272,9,13,1,14,1,14,1,14,1,
        14,3,14,278,8,14,1,15,1,15,5,15,282,8,15,10,15,12,15,285,9,15,1,
        15,1,15,1,15,5,15,290,8,15,10,15,12,15,293,9,15,1,15,1,15,1,15,1,
        15,5,15,299,8,15,10,15,12,15,302,9,15,3,15,304,8,15,1,16,1,16,1,
        16,4,16,309,8,16,11,16,12,16,310,1,16,1,16,1,16,1,16,4,16,317,8,
        16,11,16,12,16,318,1,16,1,16,5,16,323,8,16,10,16,12,16,326,9,16,
        1,16,1,16,1,16,1,16,5,16,332,8,16,10,16,12,16,335,9,16,1,16,1,16,
        1,16,1,16,5,16,341,8,16,10,16,12,16,344,9,16,1,16,1,16,1,16,1,16,
        5,16,350,8,16,10,16,12,16,353,9,16,3,16,355,8,16,1,16,1,16,4,16,
        359,8,16,11,16,12,16,360,1,16,1,16,5,16,365,8,16,10,16,12,16,368,
        9,16,1,16,1,16,1,16,1,16,5,16,374,8,16,10,16,12,16,377,9,16,5,16,
        379,8,16,10,16,12,16,382,9,16,1,17,5,17,385,8,17,10,17,12,17,388,
        9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,398,8,18,1,19,
        1,19,3,19,402,8,19,1,19,1,19,1,19,3,19,407,8,19,1,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,3,22,421,8,22,1,22,1,
        22,3,22,425,8,22,1,23,1,23,3,23,429,8,23,1,23,1,23,1,24,1,24,1,24,
        1,24,5,24,437,8,24,10,24,12,24,440,9,24,1,24,3,24,443,8,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,455,8,25,1,26,
        1,26,1,27,1,27,1,28,1,28,1,28,0,2,26,32,29,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,8,
        2,0,27,29,32,32,3,0,36,37,44,44,53,53,2,0,28,28,43,43,1,0,33,34,
        4,0,19,20,39,40,49,49,55,55,2,0,1,1,15,15,1,0,60,63,1,0,57,59,516,
        0,58,1,0,0,0,2,61,1,0,0,0,4,66,1,0,0,0,6,153,1,0,0,0,8,155,1,0,0,
        0,10,163,1,0,0,0,12,167,1,0,0,0,14,176,1,0,0,0,16,181,1,0,0,0,18,
        185,1,0,0,0,20,197,1,0,0,0,22,205,1,0,0,0,24,213,1,0,0,0,26,233,
        1,0,0,0,28,277,1,0,0,0,30,303,1,0,0,0,32,354,1,0,0,0,34,386,1,0,
        0,0,36,397,1,0,0,0,38,406,1,0,0,0,40,408,1,0,0,0,42,411,1,0,0,0,
        44,424,1,0,0,0,46,426,1,0,0,0,48,432,1,0,0,0,50,454,1,0,0,0,52,456,
        1,0,0,0,54,458,1,0,0,0,56,460,1,0,0,0,58,59,3,2,1,0,59,60,5,0,0,
        1,60,1,1,0,0,0,61,62,3,4,2,0,62,3,1,0,0,0,63,65,3,6,3,0,64,63,1,
        0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,70,1,0,0,0,68,
        66,1,0,0,0,69,71,3,14,7,0,70,69,1,0,0,0,70,71,1,0,0,0,71,5,1,0,0,
        0,72,154,5,1,0,0,73,74,3,20,10,0,74,75,5,2,0,0,75,76,3,24,12,0,76,
        154,1,0,0,0,77,154,3,32,16,0,78,154,3,16,8,0,79,154,5,3,0,0,80,81,
        5,4,0,0,81,154,5,56,0,0,82,83,5,5,0,0,83,84,3,4,2,0,84,85,5,6,0,
        0,85,154,1,0,0,0,86,87,5,7,0,0,87,88,3,26,13,0,88,89,5,5,0,0,89,
        90,3,4,2,0,90,91,5,6,0,0,91,154,1,0,0,0,92,93,5,8,0,0,93,94,3,4,
        2,0,94,95,5,9,0,0,95,96,3,26,13,0,96,154,1,0,0,0,97,98,5,10,0,0,
        98,99,3,26,13,0,99,100,5,11,0,0,100,108,3,4,2,0,101,102,5,12,0,0,
        102,103,3,26,13,0,103,104,5,11,0,0,104,105,3,4,2,0,105,107,1,0,0,
        0,106,101,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,
        0,109,113,1,0,0,0,110,108,1,0,0,0,111,112,5,13,0,0,112,114,3,4,2,
        0,113,111,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,6,0,
        0,116,154,1,0,0,0,117,118,5,14,0,0,118,119,5,56,0,0,119,120,5,2,
        0,0,120,121,3,26,13,0,121,122,5,15,0,0,122,125,3,26,13,0,123,124,
        5,15,0,0,124,126,3,26,13,0,125,123,1,0,0,0,125,126,1,0,0,0,126,127,
        1,0,0,0,127,128,5,5,0,0,128,129,3,4,2,0,129,130,5,6,0,0,130,154,
        1,0,0,0,131,132,5,14,0,0,132,133,3,22,11,0,133,134,5,16,0,0,134,
        135,3,24,12,0,135,136,5,5,0,0,136,137,3,4,2,0,137,138,5,6,0,0,138,
        154,1,0,0,0,139,140,5,17,0,0,140,141,3,18,9,0,141,142,3,42,21,0,
        142,154,1,0,0,0,143,144,5,18,0,0,144,145,5,17,0,0,145,146,5,56,0,
        0,146,154,3,42,21,0,147,148,5,18,0,0,148,151,3,8,4,0,149,150,5,2,
        0,0,150,152,3,24,12,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,1,
        0,0,0,153,72,1,0,0,0,153,73,1,0,0,0,153,77,1,0,0,0,153,78,1,0,0,
        0,153,79,1,0,0,0,153,80,1,0,0,0,153,82,1,0,0,0,153,86,1,0,0,0,153,
        92,1,0,0,0,153,97,1,0,0,0,153,117,1,0,0,0,153,131,1,0,0,0,153,139,
        1,0,0,0,153,143,1,0,0,0,153,147,1,0,0,0,154,7,1,0,0,0,155,160,3,
        10,5,0,156,157,5,15,0,0,157,159,3,10,5,0,158,156,1,0,0,0,159,162,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,9,1,0,0,0,162,160,1,
        0,0,0,163,165,5,56,0,0,164,166,3,12,6,0,165,164,1,0,0,0,165,166,
        1,0,0,0,166,11,1,0,0,0,167,168,5,19,0,0,168,169,5,56,0,0,169,170,
        5,20,0,0,170,13,1,0,0,0,171,173,5,21,0,0,172,174,3,24,12,0,173,172,
        1,0,0,0,173,174,1,0,0,0,174,177,1,0,0,0,175,177,5,3,0,0,176,171,
        1,0,0,0,176,175,1,0,0,0,177,179,1,0,0,0,178,180,5,1,0,0,179,178,
        1,0,0,0,179,180,1,0,0,0,180,15,1,0,0,0,181,182,5,22,0,0,182,183,
        5,56,0,0,183,184,5,22,0,0,184,17,1,0,0,0,185,190,5,56,0,0,186,187,
        5,26,0,0,187,189,5,56,0,0,188,186,1,0,0,0,189,192,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,195,1,0,0,0,192,190,1,0,0,0,193,194,
        5,38,0,0,194,196,5,56,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,19,
        1,0,0,0,197,202,3,28,14,0,198,199,5,15,0,0,199,201,3,28,14,0,200,
        198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,
        21,1,0,0,0,204,202,1,0,0,0,205,210,5,56,0,0,206,207,5,15,0,0,207,
        209,5,56,0,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,
        211,1,0,0,0,211,23,1,0,0,0,212,210,1,0,0,0,213,218,3,26,13,0,214,
        215,5,15,0,0,215,217,3,26,13,0,216,214,1,0,0,0,217,220,1,0,0,0,218,
        216,1,0,0,0,218,219,1,0,0,0,219,25,1,0,0,0,220,218,1,0,0,0,221,222,
        6,13,-1,0,222,234,5,23,0,0,223,234,5,24,0,0,224,234,5,25,0,0,225,
        234,3,54,27,0,226,234,3,56,28,0,227,234,5,54,0,0,228,234,3,40,20,
        0,229,234,3,30,15,0,230,234,3,46,23,0,231,232,7,0,0,0,232,234,3,
        26,13,11,233,221,1,0,0,0,233,223,1,0,0,0,233,224,1,0,0,0,233,225,
        1,0,0,0,233,226,1,0,0,0,233,227,1,0,0,0,233,228,1,0,0,0,233,229,
        1,0,0,0,233,230,1,0,0,0,233,231,1,0,0,0,234,270,1,0,0,0,235,236,
        10,12,0,0,236,237,5,52,0,0,237,269,3,26,13,12,238,239,10,10,0,0,
        239,240,7,1,0,0,240,269,3,26,13,11,241,242,10,9,0,0,242,243,7,2,
        0,0,243,269,3,26,13,10,244,245,10,8,0,0,245,246,5,50,0,0,246,269,
        3,26,13,8,247,248,10,7,0,0,248,249,7,3,0,0,249,269,3,26,13,8,250,
        251,10,6,0,0,251,252,5,35,0,0,252,269,3,26,13,7,253,254,10,5,0,0,
        254,255,5,27,0,0,255,269,3,26,13,6,256,257,10,4,0,0,257,258,5,51,
        0,0,258,269,3,26,13,5,259,260,10,3,0,0,260,261,7,4,0,0,261,269,3,
        26,13,4,262,263,10,2,0,0,263,264,5,41,0,0,264,269,3,26,13,3,265,
        266,10,1,0,0,266,267,5,42,0,0,267,269,3,26,13,2,268,235,1,0,0,0,
        268,238,1,0,0,0,268,241,1,0,0,0,268,244,1,0,0,0,268,247,1,0,0,0,
        268,250,1,0,0,0,268,253,1,0,0,0,268,256,1,0,0,0,268,259,1,0,0,0,
        268,262,1,0,0,0,268,265,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,
        270,271,1,0,0,0,271,27,1,0,0,0,272,270,1,0,0,0,273,278,5,56,0,0,
        274,275,3,30,15,0,275,276,3,36,18,0,276,278,1,0,0,0,277,273,1,0,
        0,0,277,274,1,0,0,0,278,29,1,0,0,0,279,283,3,32,16,0,280,282,3,36,
        18,0,281,280,1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,
        0,0,284,304,1,0,0,0,285,283,1,0,0,0,286,287,4,15,11,0,287,291,5,
        56,0,0,288,290,3,36,18,0,289,288,1,0,0,0,290,293,1,0,0,0,291,289,
        1,0,0,0,291,292,1,0,0,0,292,304,1,0,0,0,293,291,1,0,0,0,294,295,
        5,30,0,0,295,296,3,26,13,0,296,300,5,31,0,0,297,299,3,36,18,0,298,
        297,1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,
        304,1,0,0,0,302,300,1,0,0,0,303,279,1,0,0,0,303,286,1,0,0,0,303,
        294,1,0,0,0,304,31,1,0,0,0,305,306,6,16,-1,0,306,308,5,56,0,0,307,
        309,3,34,17,0,308,307,1,0,0,0,309,310,1,0,0,0,310,308,1,0,0,0,310,
        311,1,0,0,0,311,355,1,0,0,0,312,313,5,30,0,0,313,314,3,26,13,0,314,
        316,5,31,0,0,315,317,3,34,17,0,316,315,1,0,0,0,317,318,1,0,0,0,318,
        316,1,0,0,0,318,319,1,0,0,0,319,355,1,0,0,0,320,324,5,56,0,0,321,
        323,3,36,18,0,322,321,1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,
        325,1,0,0,0,325,327,1,0,0,0,326,324,1,0,0,0,327,328,5,38,0,0,328,
        329,5,56,0,0,329,333,3,38,19,0,330,332,3,34,17,0,331,330,1,0,0,0,
        332,335,1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,355,1,0,0,0,
        335,333,1,0,0,0,336,337,5,30,0,0,337,338,3,26,13,0,338,342,5,31,
        0,0,339,341,3,36,18,0,340,339,1,0,0,0,341,344,1,0,0,0,342,340,1,
        0,0,0,342,343,1,0,0,0,343,345,1,0,0,0,344,342,1,0,0,0,345,346,5,
        38,0,0,346,347,5,56,0,0,347,351,3,38,19,0,348,350,3,34,17,0,349,
        348,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,
        355,1,0,0,0,353,351,1,0,0,0,354,305,1,0,0,0,354,312,1,0,0,0,354,
        320,1,0,0,0,354,336,1,0,0,0,355,380,1,0,0,0,356,358,10,5,0,0,357,
        359,3,34,17,0,358,357,1,0,0,0,359,360,1,0,0,0,360,358,1,0,0,0,360,
        361,1,0,0,0,361,379,1,0,0,0,362,366,10,2,0,0,363,365,3,36,18,0,364,
        363,1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,
        369,1,0,0,0,368,366,1,0,0,0,369,370,5,38,0,0,370,371,5,56,0,0,371,
        375,3,38,19,0,372,374,3,34,17,0,373,372,1,0,0,0,374,377,1,0,0,0,
        375,373,1,0,0,0,375,376,1,0,0,0,376,379,1,0,0,0,377,375,1,0,0,0,
        378,356,1,0,0,0,378,362,1,0,0,0,379,382,1,0,0,0,380,378,1,0,0,0,
        380,381,1,0,0,0,381,33,1,0,0,0,382,380,1,0,0,0,383,385,3,36,18,0,
        384,383,1,0,0,0,385,388,1,0,0,0,386,384,1,0,0,0,386,387,1,0,0,0,
        387,389,1,0,0,0,388,386,1,0,0,0,389,390,3,38,19,0,390,35,1,0,0,0,
        391,392,5,47,0,0,392,393,3,26,13,0,393,394,5,48,0,0,394,398,1,0,
        0,0,395,396,5,26,0,0,396,398,5,56,0,0,397,391,1,0,0,0,397,395,1,
        0,0,0,398,37,1,0,0,0,399,401,5,30,0,0,400,402,3,24,12,0,401,400,
        1,0,0,0,401,402,1,0,0,0,402,403,1,0,0,0,403,407,5,31,0,0,404,407,
        3,46,23,0,405,407,3,56,28,0,406,399,1,0,0,0,406,404,1,0,0,0,406,
        405,1,0,0,0,407,39,1,0,0,0,408,409,5,17,0,0,409,410,3,42,21,0,410,
        41,1,0,0,0,411,412,5,30,0,0,412,413,3,44,22,0,413,414,5,31,0,0,414,
        415,3,4,2,0,415,416,5,6,0,0,416,43,1,0,0,0,417,420,3,22,11,0,418,
        419,5,15,0,0,419,421,5,54,0,0,420,418,1,0,0,0,420,421,1,0,0,0,421,
        425,1,0,0,0,422,425,5,54,0,0,423,425,1,0,0,0,424,417,1,0,0,0,424,
        422,1,0,0,0,424,423,1,0,0,0,425,45,1,0,0,0,426,428,5,45,0,0,427,
        429,3,48,24,0,428,427,1,0,0,0,428,429,1,0,0,0,429,430,1,0,0,0,430,
        431,5,46,0,0,431,47,1,0,0,0,432,438,3,50,25,0,433,434,3,52,26,0,
        434,435,3,50,25,0,435,437,1,0,0,0,436,433,1,0,0,0,437,440,1,0,0,
        0,438,436,1,0,0,0,438,439,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,
        0,441,443,3,52,26,0,442,441,1,0,0,0,442,443,1,0,0,0,443,49,1,0,0,
        0,444,445,5,47,0,0,445,446,3,26,13,0,446,447,5,48,0,0,447,448,5,
        2,0,0,448,449,3,26,13,0,449,455,1,0,0,0,450,451,5,56,0,0,451,452,
        5,2,0,0,452,455,3,26,13,0,453,455,3,26,13,0,454,444,1,0,0,0,454,
        450,1,0,0,0,454,453,1,0,0,0,455,51,1,0,0,0,456,457,7,5,0,0,457,53,
        1,0,0,0,458,459,7,6,0,0,459,55,1,0,0,0,460,461,7,7,0,0,461,57,1,
        0,0,0,47,66,70,108,113,125,151,153,160,165,173,176,179,190,195,202,
        210,218,233,268,270,277,283,291,300,303,310,318,324,333,342,351,
        354,360,366,375,378,380,386,397,401,406,420,424,428,438,442,454
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
    RULE_call = 17
    RULE_tail = 18
    RULE_args = 19
    RULE_functiondef = 20
    RULE_funcbody = 21
    RULE_parlist = 22
    RULE_tableconstructor = 23
    RULE_fieldlist = 24
    RULE_field = 25
    RULE_fieldsep = 26
    RULE_number = 27
    RULE_string = 28

    ruleNames =  [ "start_", "chunk", "block", "stat", "attnamelist", "nameattrib", 
                   "attrib", "retstat", "label", "funcname", "varlist", 
                   "namelist", "explist", "exp", "var", "prefixexp", "functioncall", 
                   "call", "tail", "args", "functiondef", "funcbody", "parlist", 
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
            self.state = 58
            self.chunk()
            self.state = 59
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
            self.state = 61
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
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 63
                    self.stat() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3 or _la==21:
                self.state = 69
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Stat_emptyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(LuaParser.SEMI)
                pass

            elif la_ == 2:
                localctx = LuaParser.Stat_assignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.varlist()
                self.state = 74
                self.match(LuaParser.EQ)
                self.state = 75
                self.explist()
                pass

            elif la_ == 3:
                localctx = LuaParser.Stat_functioncallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.functioncall(0)
                pass

            elif la_ == 4:
                localctx = LuaParser.Stat_labelContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.label()
                pass

            elif la_ == 5:
                localctx = LuaParser.Stat_breakContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 6:
                localctx = LuaParser.Stat_gotoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.match(LuaParser.GOTO)
                self.state = 81
                self.match(LuaParser.NAME)
                pass

            elif la_ == 7:
                localctx = LuaParser.Stat_doContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.match(LuaParser.DO)
                self.state = 83
                self.block()
                self.state = 84
                self.match(LuaParser.END)
                pass

            elif la_ == 8:
                localctx = LuaParser.Stat_whileContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.match(LuaParser.WHILE)
                self.state = 87
                self.exp(0)
                self.state = 88
                self.match(LuaParser.DO)
                self.state = 89
                self.block()
                self.state = 90
                self.match(LuaParser.END)
                pass

            elif la_ == 9:
                localctx = LuaParser.Stat_repeatContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 92
                self.match(LuaParser.REPEAT)
                self.state = 93
                self.block()
                self.state = 94
                self.match(LuaParser.UNTIL)
                self.state = 95
                self.exp(0)
                pass

            elif la_ == 10:
                localctx = LuaParser.Stat_ifContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 97
                self.match(LuaParser.IF)
                self.state = 98
                self.exp(0)
                self.state = 99
                self.match(LuaParser.THEN)
                self.state = 100
                self.block()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 101
                    self.match(LuaParser.ELSEIF)
                    self.state = 102
                    self.exp(0)
                    self.state = 103
                    self.match(LuaParser.THEN)
                    self.state = 104
                    self.block()
                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 111
                    self.match(LuaParser.ELSE)
                    self.state = 112
                    self.block()


                self.state = 115
                self.match(LuaParser.END)
                pass

            elif la_ == 11:
                localctx = LuaParser.Stat_forContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 117
                self.match(LuaParser.FOR)
                self.state = 118
                self.match(LuaParser.NAME)
                self.state = 119
                self.match(LuaParser.EQ)
                self.state = 120
                self.exp(0)
                self.state = 121
                self.match(LuaParser.COMMA)
                self.state = 122
                self.exp(0)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 123
                    self.match(LuaParser.COMMA)
                    self.state = 124
                    self.exp(0)


                self.state = 127
                self.match(LuaParser.DO)
                self.state = 128
                self.block()
                self.state = 129
                self.match(LuaParser.END)
                pass

            elif la_ == 12:
                localctx = LuaParser.Stat_forContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 131
                self.match(LuaParser.FOR)
                self.state = 132
                self.namelist()
                self.state = 133
                self.match(LuaParser.IN)
                self.state = 134
                self.explist()
                self.state = 135
                self.match(LuaParser.DO)
                self.state = 136
                self.block()
                self.state = 137
                self.match(LuaParser.END)
                pass

            elif la_ == 13:
                localctx = LuaParser.Stat_functionContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 139
                self.match(LuaParser.FUNCTION)
                self.state = 140
                self.funcname()
                self.state = 141
                self.funcbody()
                pass

            elif la_ == 14:
                localctx = LuaParser.Stat_localfunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 143
                self.match(LuaParser.LOCAL)
                self.state = 144
                self.match(LuaParser.FUNCTION)
                self.state = 145
                self.match(LuaParser.NAME)
                self.state = 146
                self.funcbody()
                pass

            elif la_ == 15:
                localctx = LuaParser.Stat_localContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 147
                self.match(LuaParser.LOCAL)
                self.state = 148
                self.attnamelist()
                self.state = 151
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 149
                    self.match(LuaParser.EQ)
                    self.state = 150
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.nameattrib()
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 156
                    self.match(LuaParser.COMMA)
                    self.state = 157
                    self.nameattrib() 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(LuaParser.NAME)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 164
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
            self.state = 167
            self.match(LuaParser.LT)
            self.state = 168
            self.match(LuaParser.NAME)
            self.state = 169
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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 171
                self.match(LuaParser.RETURN)
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 172
                    self.explist()


                pass
            elif token in [3]:
                self.state = 175
                self.match(LuaParser.BREAK)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 178
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
            self.state = 181
            self.match(LuaParser.CC)
            self.state = 182
            self.match(LuaParser.NAME)
            self.state = 183
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
            self.state = 185
            self.match(LuaParser.NAME)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 186
                self.match(LuaParser.DOT)
                self.state = 187
                self.match(LuaParser.NAME)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 193
                self.match(LuaParser.COL)
                self.state = 194
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
            self.state = 197
            self.var()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 198
                self.match(LuaParser.COMMA)
                self.state = 199
                self.var()
                self.state = 204
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
            self.state = 205
            self.match(LuaParser.NAME)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 206
                    self.match(LuaParser.COMMA)
                    self.state = 207
                    self.match(LuaParser.NAME) 
                self.state = 212
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.exp(0)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 214
                    self.match(LuaParser.COMMA)
                    self.state = 215
                    self.exp(0) 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 222
                self.match(LuaParser.NIL)
                pass

            elif la_ == 2:
                self.state = 223
                self.match(LuaParser.FALSE)
                pass

            elif la_ == 3:
                self.state = 224
                self.match(LuaParser.TRUE)
                pass

            elif la_ == 4:
                self.state = 225
                self.number()
                pass

            elif la_ == 5:
                self.state = 226
                self.string()
                pass

            elif la_ == 6:
                self.state = 227
                self.match(LuaParser.DDD)
                pass

            elif la_ == 7:
                self.state = 228
                self.functiondef()
                pass

            elif la_ == 8:
                self.state = 229
                self.prefixexp()
                pass

            elif la_ == 9:
                self.state = 230
                self.tableconstructor()
                pass

            elif la_ == 10:
                self.state = 231
                localctx.unary_op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 5234491392) != 0)):
                    localctx.unary_op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self.exp(11)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 268
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 235
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")

                        self.state = 236
                        localctx.op = self.match(LuaParser.CARET)
                        self.state = 237
                        self.exp(12)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 238
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 239
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9024997599215616) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 240
                        self.exp(11)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 241
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 242
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==43):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 243
                        self.exp(10)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 244
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")

                        self.state = 245
                        localctx.op = self.match(LuaParser.DD)
                        self.state = 246
                        self.exp(8)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 247
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 248
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 249
                        self.exp(8)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 250
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")

                        self.state = 251
                        localctx.op = self.match(LuaParser.AMP)
                        self.state = 252
                        self.exp(7)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 253
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 254
                        localctx.op = self.match(LuaParser.SQUIG)
                        self.state = 255
                        self.exp(6)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 256
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")

                        self.state = 257
                        localctx.op = self.match(LuaParser.PIPE)
                        self.state = 258
                        self.exp(5)
                        pass

                    elif la_ == 9:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 259
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 260
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 36593396241399808) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 261
                        self.exp(4)
                        pass

                    elif la_ == 10:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 262
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 263
                        localctx.op = self.match(LuaParser.AND)
                        self.state = 264
                        self.exp(3)
                        pass

                    elif la_ == 11:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 265
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                        self.state = 266
                        localctx.op = self.match(LuaParser.OR)
                        self.state = 267
                        self.exp(2)
                        pass

             
                self.state = 272
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
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.prefixexp()
                self.state = 275
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
        self.enterRule(localctx, 30, self.RULE_prefixexp)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.functioncall(0)
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 280
                        self.tail() 
                    self.state = 285
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                if not  self.IsFunctionCall() :
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, " self.IsFunctionCall() ")
                self.state = 287
                self.match(LuaParser.NAME)
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 288
                        self.tail() 
                    self.state = 293
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.match(LuaParser.OP)
                self.state = 295
                self.exp(0)
                self.state = 296
                self.match(LuaParser.CP)
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 297
                        self.tail() 
                    self.state = 302
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_functioncall, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = LuaParser.Functioncall_nameContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 306
                self.match(LuaParser.NAME)
                self.state = 308 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 307
                        self.call()

                    else:
                        raise NoViableAltException(self)
                    self.state = 310 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
                self.state = 316 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 315
                        self.call()

                    else:
                        raise NoViableAltException(self)
                    self.state = 318 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                pass

            elif la_ == 3:
                localctx = LuaParser.Functioncall_invokeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 320
                self.match(LuaParser.NAME)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26 or _la==47:
                    self.state = 321
                    self.tail()
                    self.state = 326
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 327
                self.match(LuaParser.COL)
                self.state = 328
                self.match(LuaParser.NAME)
                self.state = 329
                self.args()
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 330
                        self.call() 
                    self.state = 335
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass

            elif la_ == 4:
                localctx = LuaParser.Functioncall_expinvokeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 336
                self.match(LuaParser.OP)
                self.state = 337
                self.exp(0)
                self.state = 338
                self.match(LuaParser.CP)
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26 or _la==47:
                    self.state = 339
                    self.tail()
                    self.state = 344
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 345
                self.match(LuaParser.COL)
                self.state = 346
                self.match(LuaParser.NAME)
                self.state = 347
                self.args()
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 348
                        self.call() 
                    self.state = 353
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 378
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.Functioncall_nestedContext(self, LuaParser.FunctioncallContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 356
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 358 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 357
                                self.call()

                            else:
                                raise NoViableAltException(self)
                            self.state = 360 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                        pass

                    elif la_ == 2:
                        localctx = LuaParser.Functioncall_nestedinvokeContext(self, LuaParser.FunctioncallContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 362
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 366
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==26 or _la==47:
                            self.state = 363
                            self.tail()
                            self.state = 368
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 369
                        self.match(LuaParser.COL)
                        self.state = 370
                        self.match(LuaParser.NAME)
                        self.state = 371
                        self.args()
                        self.state = 375
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 372
                                self.call() 
                            self.state = 377
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                        pass

             
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==47:
                self.state = 383
                self.tail()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 389
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
        self.enterRule(localctx, 36, self.RULE_tail)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(LuaParser.OB)
                self.state = 392
                self.exp(0)
                self.state = 393
                self.match(LuaParser.CB)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(LuaParser.DOT)
                self.state = 396
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
        self.enterRule(localctx, 38, self.RULE_args)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(LuaParser.OP)
                self.state = 401
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 400
                    self.explist()


                self.state = 403
                self.match(LuaParser.CP)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.tableconstructor()
                pass
            elif token in [57, 58, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
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
        self.enterRule(localctx, 40, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(LuaParser.FUNCTION)
            self.state = 409
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
        self.enterRule(localctx, 42, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(LuaParser.OP)
            self.state = 412
            self.parlist()
            self.state = 413
            self.match(LuaParser.CP)
            self.state = 414
            self.block()
            self.state = 415
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
        self.enterRule(localctx, 44, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.namelist()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 418
                    self.match(LuaParser.COMMA)
                    self.state = 419
                    self.match(LuaParser.DDD)


                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(LuaParser.DDD)
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
        self.enterRule(localctx, 46, self.RULE_tableconstructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(LuaParser.OCU)
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 427
                self.fieldlist()


            self.state = 430
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
        self.enterRule(localctx, 48, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.field()
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 433
                    self.fieldsep()
                    self.state = 434
                    self.field() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==15:
                self.state = 441
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
        self.enterRule(localctx, 50, self.RULE_field)
        try:
            self.state = 454
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.match(LuaParser.OB)
                self.state = 445
                self.exp(0)
                self.state = 446
                self.match(LuaParser.CB)
                self.state = 447
                self.match(LuaParser.EQ)
                self.state = 448
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.match(LuaParser.NAME)
                self.state = 451
                self.match(LuaParser.EQ)
                self.state = 452
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
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
        self.enterRule(localctx, 52, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
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
        self.enterRule(localctx, 54, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
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
        self.enterRule(localctx, 56, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
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
        self._predicates[13] = self.exp_sempred
        self._predicates[15] = self.prefixexp_sempred
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
         

    def prefixexp_sempred(self, localctx:PrefixexpContext, predIndex:int):
            if predIndex == 11:
                return  self.IsFunctionCall() 
         

    def functioncall_sempred(self, localctx:FunctioncallContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         




