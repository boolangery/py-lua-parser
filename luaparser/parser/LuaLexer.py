# Generated from luaparser/parser/Lua.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,64,562,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,
        21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,27,1,
        27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,
        32,1,33,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,
        38,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,1,43,1,43,1,
        44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,
        50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,54,1,54,1,
        55,1,55,3,55,339,8,55,1,55,1,55,1,55,5,55,344,8,55,10,55,12,55,347,
        9,55,1,56,4,56,350,8,56,11,56,12,56,351,1,56,1,56,5,56,356,8,56,
        10,56,12,56,359,9,56,3,56,361,8,56,1,56,3,56,364,8,56,1,56,1,56,
        4,56,368,8,56,11,56,12,56,369,1,56,3,56,373,8,56,3,56,375,8,56,1,
        56,1,56,1,56,1,56,1,56,3,56,382,8,56,3,56,384,8,56,1,56,3,56,387,
        8,56,3,56,389,8,56,1,57,1,57,1,57,5,57,394,8,57,10,57,12,57,397,
        9,57,1,57,1,57,1,57,1,57,5,57,403,8,57,10,57,12,57,406,9,57,1,57,
        1,57,3,57,410,8,57,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,
        1,59,1,59,1,59,1,59,1,59,1,59,5,59,427,8,59,10,59,12,59,430,9,59,
        1,59,1,59,5,59,434,8,59,10,59,12,59,437,9,59,1,59,1,59,5,59,441,
        8,59,10,59,12,59,444,9,59,1,59,1,59,5,59,448,8,59,10,59,12,59,451,
        9,59,3,59,453,8,59,1,59,1,59,1,60,4,60,458,8,60,11,60,12,60,459,
        1,60,1,60,1,61,1,61,1,61,4,61,467,8,61,11,61,12,61,468,1,61,1,61,
        1,62,1,62,1,62,5,62,476,8,62,10,62,12,62,479,9,62,1,62,1,62,1,63,
        1,63,1,64,1,64,1,65,1,65,3,65,489,8,65,1,66,4,66,492,8,66,11,66,
        12,66,493,1,67,1,67,3,67,498,8,67,1,67,4,67,501,8,67,11,67,12,67,
        502,1,68,1,68,3,68,507,8,68,1,68,4,68,510,8,68,11,68,12,68,511,1,
        69,1,69,1,69,3,69,517,8,69,1,69,1,69,1,69,1,69,1,69,1,69,1,69,1,
        69,1,69,3,69,528,8,69,3,69,530,8,69,1,69,1,69,1,69,1,69,3,69,536,
        8,69,1,70,3,70,539,8,70,1,70,1,70,3,70,543,8,70,1,71,1,71,1,71,1,
        71,1,71,1,71,5,71,551,8,71,10,71,12,71,554,9,71,1,71,3,71,557,8,
        71,1,72,1,72,1,72,1,72,1,552,0,73,1,1,3,2,5,3,7,4,9,5,11,6,13,7,
        15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,
        121,61,123,62,125,63,127,0,129,0,131,0,133,0,135,0,137,0,139,0,141,
        0,143,0,145,64,1,0,14,2,0,88,88,120,120,4,0,10,10,13,13,34,34,92,
        92,4,0,10,10,13,13,39,39,92,92,4,0,10,10,13,13,61,61,91,91,2,0,10,
        10,13,13,3,0,10,10,13,13,91,91,2,0,9,9,32,32,2,0,10,10,12,13,2,0,
        65,90,97,122,2,0,65,70,97,102,2,0,69,69,101,101,2,0,43,43,45,45,
        2,0,80,80,112,112,10,0,34,34,39,39,92,92,97,98,102,102,110,110,114,
        114,116,116,118,118,122,122,600,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,
        0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,
        0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,
        0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,
        0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,
        0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,
        0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,
        0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,
        115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,
        0,0,0,125,1,0,0,0,0,145,1,0,0,0,1,147,1,0,0,0,3,151,1,0,0,0,5,157,
        1,0,0,0,7,160,1,0,0,0,9,165,1,0,0,0,11,172,1,0,0,0,13,176,1,0,0,
        0,15,182,1,0,0,0,17,186,1,0,0,0,19,195,1,0,0,0,21,200,1,0,0,0,23,
        203,1,0,0,0,25,206,1,0,0,0,27,212,1,0,0,0,29,216,1,0,0,0,31,220,
        1,0,0,0,33,223,1,0,0,0,35,230,1,0,0,0,37,237,1,0,0,0,39,242,1,0,
        0,0,41,247,1,0,0,0,43,253,1,0,0,0,45,259,1,0,0,0,47,261,1,0,0,0,
        49,263,1,0,0,0,51,265,1,0,0,0,53,267,1,0,0,0,55,270,1,0,0,0,57,272,
        1,0,0,0,59,274,1,0,0,0,61,276,1,0,0,0,63,279,1,0,0,0,65,282,1,0,
        0,0,67,285,1,0,0,0,69,288,1,0,0,0,71,290,1,0,0,0,73,292,1,0,0,0,
        75,294,1,0,0,0,77,296,1,0,0,0,79,298,1,0,0,0,81,300,1,0,0,0,83,303,
        1,0,0,0,85,306,1,0,0,0,87,308,1,0,0,0,89,310,1,0,0,0,91,312,1,0,
        0,0,93,314,1,0,0,0,95,316,1,0,0,0,97,318,1,0,0,0,99,321,1,0,0,0,
        101,323,1,0,0,0,103,325,1,0,0,0,105,329,1,0,0,0,107,332,1,0,0,0,
        109,334,1,0,0,0,111,338,1,0,0,0,113,388,1,0,0,0,115,409,1,0,0,0,
        117,411,1,0,0,0,119,420,1,0,0,0,121,457,1,0,0,0,123,466,1,0,0,0,
        125,472,1,0,0,0,127,482,1,0,0,0,129,484,1,0,0,0,131,488,1,0,0,0,
        133,491,1,0,0,0,135,495,1,0,0,0,137,504,1,0,0,0,139,513,1,0,0,0,
        141,542,1,0,0,0,143,556,1,0,0,0,145,558,1,0,0,0,147,148,5,97,0,0,
        148,149,5,110,0,0,149,150,5,100,0,0,150,2,1,0,0,0,151,152,5,98,0,
        0,152,153,5,114,0,0,153,154,5,101,0,0,154,155,5,97,0,0,155,156,5,
        107,0,0,156,4,1,0,0,0,157,158,5,100,0,0,158,159,5,111,0,0,159,6,
        1,0,0,0,160,161,5,101,0,0,161,162,5,108,0,0,162,163,5,115,0,0,163,
        164,5,101,0,0,164,8,1,0,0,0,165,166,5,101,0,0,166,167,5,108,0,0,
        167,168,5,115,0,0,168,169,5,101,0,0,169,170,5,105,0,0,170,171,5,
        102,0,0,171,10,1,0,0,0,172,173,5,101,0,0,173,174,5,110,0,0,174,175,
        5,100,0,0,175,12,1,0,0,0,176,177,5,102,0,0,177,178,5,97,0,0,178,
        179,5,108,0,0,179,180,5,115,0,0,180,181,5,101,0,0,181,14,1,0,0,0,
        182,183,5,102,0,0,183,184,5,111,0,0,184,185,5,114,0,0,185,16,1,0,
        0,0,186,187,5,102,0,0,187,188,5,117,0,0,188,189,5,110,0,0,189,190,
        5,99,0,0,190,191,5,116,0,0,191,192,5,105,0,0,192,193,5,111,0,0,193,
        194,5,110,0,0,194,18,1,0,0,0,195,196,5,103,0,0,196,197,5,111,0,0,
        197,198,5,116,0,0,198,199,5,111,0,0,199,20,1,0,0,0,200,201,5,105,
        0,0,201,202,5,102,0,0,202,22,1,0,0,0,203,204,5,105,0,0,204,205,5,
        110,0,0,205,24,1,0,0,0,206,207,5,108,0,0,207,208,5,111,0,0,208,209,
        5,99,0,0,209,210,5,97,0,0,210,211,5,108,0,0,211,26,1,0,0,0,212,213,
        5,110,0,0,213,214,5,105,0,0,214,215,5,108,0,0,215,28,1,0,0,0,216,
        217,5,110,0,0,217,218,5,111,0,0,218,219,5,116,0,0,219,30,1,0,0,0,
        220,221,5,111,0,0,221,222,5,114,0,0,222,32,1,0,0,0,223,224,5,114,
        0,0,224,225,5,101,0,0,225,226,5,112,0,0,226,227,5,101,0,0,227,228,
        5,97,0,0,228,229,5,116,0,0,229,34,1,0,0,0,230,231,5,114,0,0,231,
        232,5,101,0,0,232,233,5,116,0,0,233,234,5,117,0,0,234,235,5,114,
        0,0,235,236,5,110,0,0,236,36,1,0,0,0,237,238,5,116,0,0,238,239,5,
        104,0,0,239,240,5,101,0,0,240,241,5,110,0,0,241,38,1,0,0,0,242,243,
        5,116,0,0,243,244,5,114,0,0,244,245,5,117,0,0,245,246,5,101,0,0,
        246,40,1,0,0,0,247,248,5,117,0,0,248,249,5,110,0,0,249,250,5,116,
        0,0,250,251,5,105,0,0,251,252,5,108,0,0,252,42,1,0,0,0,253,254,5,
        119,0,0,254,255,5,104,0,0,255,256,5,105,0,0,256,257,5,108,0,0,257,
        258,5,101,0,0,258,44,1,0,0,0,259,260,5,43,0,0,260,46,1,0,0,0,261,
        262,5,45,0,0,262,48,1,0,0,0,263,264,5,42,0,0,264,50,1,0,0,0,265,
        266,5,47,0,0,266,52,1,0,0,0,267,268,5,47,0,0,268,269,5,47,0,0,269,
        54,1,0,0,0,270,271,5,37,0,0,271,56,1,0,0,0,272,273,5,94,0,0,273,
        58,1,0,0,0,274,275,5,35,0,0,275,60,1,0,0,0,276,277,5,61,0,0,277,
        278,5,61,0,0,278,62,1,0,0,0,279,280,5,126,0,0,280,281,5,61,0,0,281,
        64,1,0,0,0,282,283,5,60,0,0,283,284,5,61,0,0,284,66,1,0,0,0,285,
        286,5,62,0,0,286,287,5,61,0,0,287,68,1,0,0,0,288,289,5,60,0,0,289,
        70,1,0,0,0,290,291,5,62,0,0,291,72,1,0,0,0,292,293,5,61,0,0,293,
        74,1,0,0,0,294,295,5,38,0,0,295,76,1,0,0,0,296,297,5,124,0,0,297,
        78,1,0,0,0,298,299,5,126,0,0,299,80,1,0,0,0,300,301,5,62,0,0,301,
        302,5,62,0,0,302,82,1,0,0,0,303,304,5,60,0,0,304,305,5,60,0,0,305,
        84,1,0,0,0,306,307,5,40,0,0,307,86,1,0,0,0,308,309,5,41,0,0,309,
        88,1,0,0,0,310,311,5,123,0,0,311,90,1,0,0,0,312,313,5,125,0,0,313,
        92,1,0,0,0,314,315,5,91,0,0,315,94,1,0,0,0,316,317,5,93,0,0,317,
        96,1,0,0,0,318,319,5,58,0,0,319,320,5,58,0,0,320,98,1,0,0,0,321,
        322,5,58,0,0,322,100,1,0,0,0,323,324,5,44,0,0,324,102,1,0,0,0,325,
        326,5,46,0,0,326,327,5,46,0,0,327,328,5,46,0,0,328,104,1,0,0,0,329,
        330,5,46,0,0,330,331,5,46,0,0,331,106,1,0,0,0,332,333,5,46,0,0,333,
        108,1,0,0,0,334,335,5,59,0,0,335,110,1,0,0,0,336,339,3,127,63,0,
        337,339,5,95,0,0,338,336,1,0,0,0,338,337,1,0,0,0,339,345,1,0,0,0,
        340,344,3,127,63,0,341,344,5,95,0,0,342,344,3,129,64,0,343,340,1,
        0,0,0,343,341,1,0,0,0,343,342,1,0,0,0,344,347,1,0,0,0,345,343,1,
        0,0,0,345,346,1,0,0,0,346,112,1,0,0,0,347,345,1,0,0,0,348,350,3,
        129,64,0,349,348,1,0,0,0,350,351,1,0,0,0,351,349,1,0,0,0,351,352,
        1,0,0,0,352,360,1,0,0,0,353,357,5,46,0,0,354,356,3,129,64,0,355,
        354,1,0,0,0,356,359,1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,
        361,1,0,0,0,359,357,1,0,0,0,360,353,1,0,0,0,360,361,1,0,0,0,361,
        363,1,0,0,0,362,364,3,135,67,0,363,362,1,0,0,0,363,364,1,0,0,0,364,
        375,1,0,0,0,365,367,5,46,0,0,366,368,3,129,64,0,367,366,1,0,0,0,
        368,369,1,0,0,0,369,367,1,0,0,0,369,370,1,0,0,0,370,372,1,0,0,0,
        371,373,3,135,67,0,372,371,1,0,0,0,372,373,1,0,0,0,373,375,1,0,0,
        0,374,349,1,0,0,0,374,365,1,0,0,0,375,389,1,0,0,0,376,377,5,48,0,
        0,377,378,7,0,0,0,378,383,3,133,66,0,379,381,5,46,0,0,380,382,3,
        133,66,0,381,380,1,0,0,0,381,382,1,0,0,0,382,384,1,0,0,0,383,379,
        1,0,0,0,383,384,1,0,0,0,384,386,1,0,0,0,385,387,3,137,68,0,386,385,
        1,0,0,0,386,387,1,0,0,0,387,389,1,0,0,0,388,374,1,0,0,0,388,376,
        1,0,0,0,389,114,1,0,0,0,390,395,5,34,0,0,391,394,3,139,69,0,392,
        394,8,1,0,0,393,391,1,0,0,0,393,392,1,0,0,0,394,397,1,0,0,0,395,
        393,1,0,0,0,395,396,1,0,0,0,396,398,1,0,0,0,397,395,1,0,0,0,398,
        410,5,34,0,0,399,404,5,39,0,0,400,403,3,139,69,0,401,403,8,2,0,0,
        402,400,1,0,0,0,402,401,1,0,0,0,403,406,1,0,0,0,404,402,1,0,0,0,
        404,405,1,0,0,0,405,407,1,0,0,0,406,404,1,0,0,0,407,410,5,39,0,0,
        408,410,3,145,72,0,409,390,1,0,0,0,409,399,1,0,0,0,409,408,1,0,0,
        0,410,116,1,0,0,0,411,412,5,45,0,0,412,413,5,45,0,0,413,414,5,91,
        0,0,414,415,1,0,0,0,415,416,3,143,71,0,416,417,5,93,0,0,417,418,
        1,0,0,0,418,419,6,58,0,0,419,118,1,0,0,0,420,421,5,45,0,0,421,422,
        5,45,0,0,422,452,1,0,0,0,423,453,1,0,0,0,424,428,5,91,0,0,425,427,
        5,61,0,0,426,425,1,0,0,0,427,430,1,0,0,0,428,426,1,0,0,0,428,429,
        1,0,0,0,429,453,1,0,0,0,430,428,1,0,0,0,431,435,5,91,0,0,432,434,
        5,61,0,0,433,432,1,0,0,0,434,437,1,0,0,0,435,433,1,0,0,0,435,436,
        1,0,0,0,436,438,1,0,0,0,437,435,1,0,0,0,438,442,8,3,0,0,439,441,
        8,4,0,0,440,439,1,0,0,0,441,444,1,0,0,0,442,440,1,0,0,0,442,443,
        1,0,0,0,443,453,1,0,0,0,444,442,1,0,0,0,445,449,8,5,0,0,446,448,
        8,4,0,0,447,446,1,0,0,0,448,451,1,0,0,0,449,447,1,0,0,0,449,450,
        1,0,0,0,450,453,1,0,0,0,451,449,1,0,0,0,452,423,1,0,0,0,452,424,
        1,0,0,0,452,431,1,0,0,0,452,445,1,0,0,0,453,454,1,0,0,0,454,455,
        6,59,0,0,455,120,1,0,0,0,456,458,7,6,0,0,457,456,1,0,0,0,458,459,
        1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,461,1,0,0,0,461,462,
        6,60,0,0,462,122,1,0,0,0,463,464,5,13,0,0,464,467,5,10,0,0,465,467,
        7,7,0,0,466,463,1,0,0,0,466,465,1,0,0,0,467,468,1,0,0,0,468,466,
        1,0,0,0,468,469,1,0,0,0,469,470,1,0,0,0,470,471,6,61,0,0,471,124,
        1,0,0,0,472,473,5,35,0,0,473,477,5,33,0,0,474,476,8,4,0,0,475,474,
        1,0,0,0,476,479,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,478,480,
        1,0,0,0,479,477,1,0,0,0,480,481,6,62,0,0,481,126,1,0,0,0,482,483,
        7,8,0,0,483,128,1,0,0,0,484,485,2,48,57,0,485,130,1,0,0,0,486,489,
        3,129,64,0,487,489,7,9,0,0,488,486,1,0,0,0,488,487,1,0,0,0,489,132,
        1,0,0,0,490,492,3,131,65,0,491,490,1,0,0,0,492,493,1,0,0,0,493,491,
        1,0,0,0,493,494,1,0,0,0,494,134,1,0,0,0,495,497,7,10,0,0,496,498,
        7,11,0,0,497,496,1,0,0,0,497,498,1,0,0,0,498,500,1,0,0,0,499,501,
        3,129,64,0,500,499,1,0,0,0,501,502,1,0,0,0,502,500,1,0,0,0,502,503,
        1,0,0,0,503,136,1,0,0,0,504,506,7,12,0,0,505,507,7,11,0,0,506,505,
        1,0,0,0,506,507,1,0,0,0,507,509,1,0,0,0,508,510,3,129,64,0,509,508,
        1,0,0,0,510,511,1,0,0,0,511,509,1,0,0,0,511,512,1,0,0,0,512,138,
        1,0,0,0,513,535,5,92,0,0,514,517,7,13,0,0,515,517,3,141,70,0,516,
        514,1,0,0,0,516,515,1,0,0,0,517,536,1,0,0,0,518,519,5,117,0,0,519,
        520,5,123,0,0,520,521,1,0,0,0,521,522,3,133,66,0,522,523,5,125,0,
        0,523,536,1,0,0,0,524,529,3,129,64,0,525,527,3,129,64,0,526,528,
        3,129,64,0,527,526,1,0,0,0,527,528,1,0,0,0,528,530,1,0,0,0,529,525,
        1,0,0,0,529,530,1,0,0,0,530,536,1,0,0,0,531,532,5,120,0,0,532,533,
        3,131,65,0,533,534,3,131,65,0,534,536,1,0,0,0,535,516,1,0,0,0,535,
        518,1,0,0,0,535,524,1,0,0,0,535,531,1,0,0,0,536,140,1,0,0,0,537,
        539,5,13,0,0,538,537,1,0,0,0,538,539,1,0,0,0,539,540,1,0,0,0,540,
        543,5,10,0,0,541,543,5,13,0,0,542,538,1,0,0,0,542,541,1,0,0,0,543,
        142,1,0,0,0,544,545,5,61,0,0,545,546,3,143,71,0,546,547,5,61,0,0,
        547,557,1,0,0,0,548,552,5,91,0,0,549,551,9,0,0,0,550,549,1,0,0,0,
        551,554,1,0,0,0,552,553,1,0,0,0,552,550,1,0,0,0,553,555,1,0,0,0,
        554,552,1,0,0,0,555,557,5,93,0,0,556,544,1,0,0,0,556,548,1,0,0,0,
        557,144,1,0,0,0,558,559,5,91,0,0,559,560,3,143,71,0,560,561,5,93,
        0,0,561,146,1,0,0,0,43,0,338,343,345,351,357,360,363,369,372,374,
        381,383,386,388,393,395,402,404,409,428,435,442,449,452,459,466,
        468,477,488,493,497,502,506,511,516,527,529,535,538,542,552,556,
        1,0,1,0
    ]

class LuaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    BREAK = 2
    DO = 3
    ELSE = 4
    ELSEIF = 5
    END = 6
    FALSE = 7
    FOR = 8
    FUNCTION = 9
    GOTO = 10
    IF = 11
    IN = 12
    LOCAL = 13
    NIL = 14
    NOT = 15
    OR = 16
    REPEAT = 17
    RETURN = 18
    THEN = 19
    TRUE = 20
    UNTIL = 21
    WHILE = 22
    ADD = 23
    MINUS = 24
    MULT = 25
    DIV = 26
    FLOOR = 27
    MOD = 28
    POW = 29
    LENGTH = 30
    EQ = 31
    NEQ = 32
    LTEQ = 33
    GTEQ = 34
    LT = 35
    GT = 36
    ASSIGN = 37
    BITAND = 38
    BITOR = 39
    BITNOT = 40
    BITRSHIFT = 41
    BITRLEFT = 42
    OPAR = 43
    CPAR = 44
    OBRACE = 45
    CBRACE = 46
    OBRACK = 47
    CBRACK = 48
    COLCOL = 49
    COL = 50
    COMMA = 51
    VARARGS = 52
    CONCAT = 53
    DOT = 54
    SEMCOL = 55
    NAME = 56
    NUMBER = 57
    STRING = 58
    COMMENT = 59
    LINE_COMMENT = 60
    SPACE = 61
    NEWLINE = 62
    SHEBANG = 63
    LongBracket = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'and'", "'break'", "'do'", "'else'", "'elseif'", "'end'", "'false'", 
            "'for'", "'function'", "'goto'", "'if'", "'in'", "'local'", 
            "'nil'", "'not'", "'or'", "'repeat'", "'return'", "'then'", 
            "'true'", "'until'", "'while'", "'+'", "'-'", "'*'", "'/'", 
            "'//'", "'%'", "'^'", "'#'", "'=='", "'~='", "'<='", "'>='", 
            "'<'", "'>'", "'='", "'&'", "'|'", "'~'", "'>>'", "'<<'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "'::'", "':'", "','", "'...'", 
            "'..'", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "BREAK", "DO", "ELSE", "ELSEIF", "END", "FALSE", "FOR", 
            "FUNCTION", "GOTO", "IF", "IN", "LOCAL", "NIL", "NOT", "OR", 
            "REPEAT", "RETURN", "THEN", "TRUE", "UNTIL", "WHILE", "ADD", 
            "MINUS", "MULT", "DIV", "FLOOR", "MOD", "POW", "LENGTH", "EQ", 
            "NEQ", "LTEQ", "GTEQ", "LT", "GT", "ASSIGN", "BITAND", "BITOR", 
            "BITNOT", "BITRSHIFT", "BITRLEFT", "OPAR", "CPAR", "OBRACE", 
            "CBRACE", "OBRACK", "CBRACK", "COLCOL", "COL", "COMMA", "VARARGS", 
            "CONCAT", "DOT", "SEMCOL", "NAME", "NUMBER", "STRING", "COMMENT", 
            "LINE_COMMENT", "SPACE", "NEWLINE", "SHEBANG", "LongBracket" ]

    ruleNames = [ "AND", "BREAK", "DO", "ELSE", "ELSEIF", "END", "FALSE", 
                  "FOR", "FUNCTION", "GOTO", "IF", "IN", "LOCAL", "NIL", 
                  "NOT", "OR", "REPEAT", "RETURN", "THEN", "TRUE", "UNTIL", 
                  "WHILE", "ADD", "MINUS", "MULT", "DIV", "FLOOR", "MOD", 
                  "POW", "LENGTH", "EQ", "NEQ", "LTEQ", "GTEQ", "LT", "GT", 
                  "ASSIGN", "BITAND", "BITOR", "BITNOT", "BITRSHIFT", "BITRLEFT", 
                  "OPAR", "CPAR", "OBRACE", "CBRACE", "OBRACK", "CBRACK", 
                  "COLCOL", "COL", "COMMA", "VARARGS", "CONCAT", "DOT", 
                  "SEMCOL", "NAME", "NUMBER", "STRING", "COMMENT", "LINE_COMMENT", 
                  "SPACE", "NEWLINE", "SHEBANG", "Letter", "Digit", "HexDigit", 
                  "HexDigits", "Exponent", "BinaryExponent", "EscapeSequence", 
                  "LineBreak", "NESTED_STR", "LongBracket" ]

    grammarFileName = "Lua.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


