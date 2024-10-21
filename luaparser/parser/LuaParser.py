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
        4,1,68,445,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,
        0,1,1,1,1,1,2,5,2,85,8,2,10,2,12,2,88,9,2,1,2,3,2,91,8,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,108,8,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,
        141,8,9,10,9,12,9,144,9,9,1,9,1,9,3,9,148,8,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,160,8,10,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,187,8,14,1,15,1,15,
        1,15,1,15,1,15,5,15,194,8,15,10,15,12,15,197,9,15,1,16,1,16,1,16,
        3,16,202,8,16,1,17,1,17,3,17,206,8,17,1,17,1,17,3,17,210,8,17,1,
        17,3,17,213,8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,222,8,19,
        10,19,12,19,225,9,19,1,19,1,19,3,19,229,8,19,1,20,1,20,1,20,5,20,
        234,8,20,10,20,12,20,237,9,20,1,21,1,21,1,21,5,21,242,8,21,10,21,
        12,21,245,9,21,1,22,1,22,1,22,5,22,250,8,22,10,22,12,22,253,9,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        267,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        5,23,293,8,23,10,23,12,23,296,9,23,1,24,1,24,1,24,1,24,3,24,302,
        8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,5,25,311,8,25,10,25,12,25,
        314,9,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,324,8,25,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,351,
        8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,363,
        8,26,10,26,12,26,366,9,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,374,
        8,27,1,28,5,28,377,8,28,10,28,12,28,380,9,28,1,29,1,29,3,29,384,
        8,29,1,29,1,29,1,29,3,29,389,8,29,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,1,31,1,32,1,32,1,32,3,32,403,8,32,1,32,1,32,3,32,407,8,
        32,1,33,1,33,3,33,411,8,33,1,33,1,33,1,34,1,34,1,34,1,34,5,34,419,
        8,34,10,34,12,34,422,9,34,1,34,3,34,425,8,34,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,3,35,437,8,35,1,36,1,36,1,37,1,37,
        1,38,1,38,1,38,0,2,46,52,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,0,8,2,0,28,30,33,33,3,0,37,38,45,45,54,54,2,0,29,29,44,
        44,4,0,19,20,40,41,50,50,56,56,3,0,28,28,34,36,52,52,2,0,1,1,15,
        15,1,0,61,64,1,0,58,60,476,0,78,1,0,0,0,2,81,1,0,0,0,4,86,1,0,0,
        0,6,107,1,0,0,0,8,109,1,0,0,0,10,113,1,0,0,0,12,116,1,0,0,0,14,120,
        1,0,0,0,16,126,1,0,0,0,18,131,1,0,0,0,20,151,1,0,0,0,22,165,1,0,
        0,0,24,173,1,0,0,0,26,177,1,0,0,0,28,182,1,0,0,0,30,188,1,0,0,0,
        32,201,1,0,0,0,34,209,1,0,0,0,36,214,1,0,0,0,38,218,1,0,0,0,40,230,
        1,0,0,0,42,238,1,0,0,0,44,246,1,0,0,0,46,266,1,0,0,0,48,301,1,0,
        0,0,50,323,1,0,0,0,52,350,1,0,0,0,54,373,1,0,0,0,56,378,1,0,0,0,
        58,388,1,0,0,0,60,390,1,0,0,0,62,393,1,0,0,0,64,406,1,0,0,0,66,408,
        1,0,0,0,68,414,1,0,0,0,70,436,1,0,0,0,72,438,1,0,0,0,74,440,1,0,
        0,0,76,442,1,0,0,0,78,79,3,2,1,0,79,80,5,0,0,1,80,1,1,0,0,0,81,82,
        3,4,2,0,82,3,1,0,0,0,83,85,3,6,3,0,84,83,1,0,0,0,85,88,1,0,0,0,86,
        84,1,0,0,0,86,87,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,91,3,34,
        17,0,90,89,1,0,0,0,90,91,1,0,0,0,91,5,1,0,0,0,92,108,5,1,0,0,93,
        108,3,8,4,0,94,108,3,52,26,0,95,108,3,36,18,0,96,108,5,3,0,0,97,
        108,3,10,5,0,98,108,3,12,6,0,99,108,3,14,7,0,100,108,3,16,8,0,101,
        108,3,18,9,0,102,108,3,20,10,0,103,108,3,22,11,0,104,108,3,24,12,
        0,105,108,3,26,13,0,106,108,3,28,14,0,107,92,1,0,0,0,107,93,1,0,
        0,0,107,94,1,0,0,0,107,95,1,0,0,0,107,96,1,0,0,0,107,97,1,0,0,0,
        107,98,1,0,0,0,107,99,1,0,0,0,107,100,1,0,0,0,107,101,1,0,0,0,107,
        102,1,0,0,0,107,103,1,0,0,0,107,104,1,0,0,0,107,105,1,0,0,0,107,
        106,1,0,0,0,108,7,1,0,0,0,109,110,3,40,20,0,110,111,5,2,0,0,111,
        112,3,44,22,0,112,9,1,0,0,0,113,114,5,4,0,0,114,115,5,57,0,0,115,
        11,1,0,0,0,116,117,5,5,0,0,117,118,3,4,2,0,118,119,5,6,0,0,119,13,
        1,0,0,0,120,121,5,7,0,0,121,122,3,46,23,0,122,123,5,5,0,0,123,124,
        3,4,2,0,124,125,5,6,0,0,125,15,1,0,0,0,126,127,5,8,0,0,127,128,3,
        4,2,0,128,129,5,9,0,0,129,130,3,46,23,0,130,17,1,0,0,0,131,132,5,
        10,0,0,132,133,3,46,23,0,133,134,5,11,0,0,134,142,3,4,2,0,135,136,
        5,12,0,0,136,137,3,46,23,0,137,138,5,11,0,0,138,139,3,4,2,0,139,
        141,1,0,0,0,140,135,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,
        143,1,0,0,0,143,147,1,0,0,0,144,142,1,0,0,0,145,146,5,13,0,0,146,
        148,3,4,2,0,147,145,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,
        150,5,6,0,0,150,19,1,0,0,0,151,152,5,14,0,0,152,153,5,57,0,0,153,
        154,5,2,0,0,154,155,3,46,23,0,155,156,5,15,0,0,156,159,3,46,23,0,
        157,158,5,15,0,0,158,160,3,46,23,0,159,157,1,0,0,0,159,160,1,0,0,
        0,160,161,1,0,0,0,161,162,5,5,0,0,162,163,3,4,2,0,163,164,5,6,0,
        0,164,21,1,0,0,0,165,166,5,14,0,0,166,167,3,42,21,0,167,168,5,16,
        0,0,168,169,3,44,22,0,169,170,5,5,0,0,170,171,3,4,2,0,171,172,5,
        6,0,0,172,23,1,0,0,0,173,174,5,17,0,0,174,175,3,38,19,0,175,176,
        3,62,31,0,176,25,1,0,0,0,177,178,5,18,0,0,178,179,5,17,0,0,179,180,
        5,57,0,0,180,181,3,62,31,0,181,27,1,0,0,0,182,183,5,18,0,0,183,186,
        3,42,21,0,184,185,5,2,0,0,185,187,3,44,22,0,186,184,1,0,0,0,186,
        187,1,0,0,0,187,29,1,0,0,0,188,189,5,57,0,0,189,195,3,32,16,0,190,
        191,5,15,0,0,191,192,5,57,0,0,192,194,3,32,16,0,193,190,1,0,0,0,
        194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,31,1,0,0,0,197,
        195,1,0,0,0,198,199,5,19,0,0,199,200,5,57,0,0,200,202,5,20,0,0,201,
        198,1,0,0,0,201,202,1,0,0,0,202,33,1,0,0,0,203,205,5,21,0,0,204,
        206,3,44,22,0,205,204,1,0,0,0,205,206,1,0,0,0,206,210,1,0,0,0,207,
        210,5,3,0,0,208,210,5,22,0,0,209,203,1,0,0,0,209,207,1,0,0,0,209,
        208,1,0,0,0,210,212,1,0,0,0,211,213,5,1,0,0,212,211,1,0,0,0,212,
        213,1,0,0,0,213,35,1,0,0,0,214,215,5,23,0,0,215,216,5,57,0,0,216,
        217,5,23,0,0,217,37,1,0,0,0,218,223,5,57,0,0,219,220,5,27,0,0,220,
        222,5,57,0,0,221,219,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,
        224,1,0,0,0,224,228,1,0,0,0,225,223,1,0,0,0,226,227,5,39,0,0,227,
        229,5,57,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,39,1,0,0,0,230,
        235,3,48,24,0,231,232,5,15,0,0,232,234,3,48,24,0,233,231,1,0,0,0,
        234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,41,1,0,0,0,237,
        235,1,0,0,0,238,243,5,57,0,0,239,240,5,15,0,0,240,242,5,57,0,0,241,
        239,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,
        43,1,0,0,0,245,243,1,0,0,0,246,251,3,46,23,0,247,248,5,15,0,0,248,
        250,3,46,23,0,249,247,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,
        252,1,0,0,0,252,45,1,0,0,0,253,251,1,0,0,0,254,255,6,23,-1,0,255,
        267,5,24,0,0,256,267,5,25,0,0,257,267,5,26,0,0,258,267,3,74,37,0,
        259,267,3,76,38,0,260,267,5,55,0,0,261,267,3,24,12,0,262,267,3,50,
        25,0,263,267,3,66,33,0,264,265,7,0,0,0,265,267,3,46,23,8,266,254,
        1,0,0,0,266,256,1,0,0,0,266,257,1,0,0,0,266,258,1,0,0,0,266,259,
        1,0,0,0,266,260,1,0,0,0,266,261,1,0,0,0,266,262,1,0,0,0,266,263,
        1,0,0,0,266,264,1,0,0,0,267,294,1,0,0,0,268,269,10,9,0,0,269,270,
        5,53,0,0,270,293,3,46,23,9,271,272,10,7,0,0,272,273,7,1,0,0,273,
        293,3,46,23,8,274,275,10,6,0,0,275,276,7,2,0,0,276,293,3,46,23,7,
        277,278,10,5,0,0,278,279,5,51,0,0,279,293,3,46,23,5,280,281,10,4,
        0,0,281,282,7,3,0,0,282,293,3,46,23,5,283,284,10,3,0,0,284,285,5,
        42,0,0,285,293,3,46,23,4,286,287,10,2,0,0,287,288,5,43,0,0,288,293,
        3,46,23,3,289,290,10,1,0,0,290,291,7,4,0,0,291,293,3,46,23,2,292,
        268,1,0,0,0,292,271,1,0,0,0,292,274,1,0,0,0,292,277,1,0,0,0,292,
        280,1,0,0,0,292,283,1,0,0,0,292,286,1,0,0,0,292,289,1,0,0,0,293,
        296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,47,1,0,0,0,296,294,
        1,0,0,0,297,302,5,57,0,0,298,299,3,50,25,0,299,300,3,54,27,0,300,
        302,1,0,0,0,301,297,1,0,0,0,301,298,1,0,0,0,302,49,1,0,0,0,303,312,
        5,57,0,0,304,305,5,48,0,0,305,306,3,46,23,0,306,307,5,49,0,0,307,
        311,1,0,0,0,308,309,5,27,0,0,309,311,5,57,0,0,310,304,1,0,0,0,310,
        308,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,
        324,1,0,0,0,314,312,1,0,0,0,315,316,3,52,26,0,316,317,3,56,28,0,
        317,324,1,0,0,0,318,319,5,31,0,0,319,320,3,46,23,0,320,321,5,32,
        0,0,321,322,3,56,28,0,322,324,1,0,0,0,323,303,1,0,0,0,323,315,1,
        0,0,0,323,318,1,0,0,0,324,51,1,0,0,0,325,326,6,26,-1,0,326,327,5,
        57,0,0,327,328,3,56,28,0,328,329,3,58,29,0,329,351,1,0,0,0,330,331,
        5,31,0,0,331,332,3,46,23,0,332,333,5,32,0,0,333,334,3,56,28,0,334,
        335,3,58,29,0,335,351,1,0,0,0,336,337,5,57,0,0,337,338,3,56,28,0,
        338,339,5,39,0,0,339,340,5,57,0,0,340,341,3,58,29,0,341,351,1,0,
        0,0,342,343,5,31,0,0,343,344,3,46,23,0,344,345,5,32,0,0,345,346,
        3,56,28,0,346,347,5,39,0,0,347,348,5,57,0,0,348,349,3,58,29,0,349,
        351,1,0,0,0,350,325,1,0,0,0,350,330,1,0,0,0,350,336,1,0,0,0,350,
        342,1,0,0,0,351,364,1,0,0,0,352,353,10,5,0,0,353,354,3,56,28,0,354,
        355,3,58,29,0,355,363,1,0,0,0,356,357,10,2,0,0,357,358,3,56,28,0,
        358,359,5,39,0,0,359,360,5,57,0,0,360,361,3,58,29,0,361,363,1,0,
        0,0,362,352,1,0,0,0,362,356,1,0,0,0,363,366,1,0,0,0,364,362,1,0,
        0,0,364,365,1,0,0,0,365,53,1,0,0,0,366,364,1,0,0,0,367,368,5,48,
        0,0,368,369,3,46,23,0,369,370,5,49,0,0,370,374,1,0,0,0,371,372,5,
        27,0,0,372,374,5,57,0,0,373,367,1,0,0,0,373,371,1,0,0,0,374,55,1,
        0,0,0,375,377,3,54,27,0,376,375,1,0,0,0,377,380,1,0,0,0,378,376,
        1,0,0,0,378,379,1,0,0,0,379,57,1,0,0,0,380,378,1,0,0,0,381,383,5,
        31,0,0,382,384,3,44,22,0,383,382,1,0,0,0,383,384,1,0,0,0,384,385,
        1,0,0,0,385,389,5,32,0,0,386,389,3,66,33,0,387,389,3,76,38,0,388,
        381,1,0,0,0,388,386,1,0,0,0,388,387,1,0,0,0,389,59,1,0,0,0,390,391,
        5,17,0,0,391,392,3,62,31,0,392,61,1,0,0,0,393,394,5,31,0,0,394,395,
        3,64,32,0,395,396,5,32,0,0,396,397,3,4,2,0,397,398,5,6,0,0,398,63,
        1,0,0,0,399,402,3,42,21,0,400,401,5,15,0,0,401,403,5,55,0,0,402,
        400,1,0,0,0,402,403,1,0,0,0,403,407,1,0,0,0,404,407,5,55,0,0,405,
        407,1,0,0,0,406,399,1,0,0,0,406,404,1,0,0,0,406,405,1,0,0,0,407,
        65,1,0,0,0,408,410,5,46,0,0,409,411,3,68,34,0,410,409,1,0,0,0,410,
        411,1,0,0,0,411,412,1,0,0,0,412,413,5,47,0,0,413,67,1,0,0,0,414,
        420,3,70,35,0,415,416,3,72,36,0,416,417,3,70,35,0,417,419,1,0,0,
        0,418,415,1,0,0,0,419,422,1,0,0,0,420,418,1,0,0,0,420,421,1,0,0,
        0,421,424,1,0,0,0,422,420,1,0,0,0,423,425,3,72,36,0,424,423,1,0,
        0,0,424,425,1,0,0,0,425,69,1,0,0,0,426,427,5,48,0,0,427,428,3,46,
        23,0,428,429,5,49,0,0,429,430,5,2,0,0,430,431,3,46,23,0,431,437,
        1,0,0,0,432,433,5,57,0,0,433,434,5,2,0,0,434,437,3,46,23,0,435,437,
        3,46,23,0,436,426,1,0,0,0,436,432,1,0,0,0,436,435,1,0,0,0,437,71,
        1,0,0,0,438,439,7,5,0,0,439,73,1,0,0,0,440,441,7,6,0,0,441,75,1,
        0,0,0,442,443,7,7,0,0,443,77,1,0,0,0,37,86,90,107,142,147,159,186,
        195,201,205,209,212,223,228,235,243,251,266,292,294,301,310,312,
        323,350,362,364,373,378,383,388,402,406,410,420,424,436
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
    RULE_nestedtail = 28
    RULE_args = 29
    RULE_anonfunctiondef = 30
    RULE_funcbody = 31
    RULE_parlist = 32
    RULE_tableconstructor = 33
    RULE_fieldlist = 34
    RULE_field = 35
    RULE_fieldsep = 36
    RULE_number = 37
    RULE_string = 38

    ruleNames =  [ "start_", "chunk", "block", "stat", "assign", "goto", 
                   "do", "while", "repeat", "if", "for", "forin", "functiondef", 
                   "localfunction", "localassign", "attnamelist", "attrib", 
                   "retstat", "label", "funcname", "varlist", "namelist", 
                   "explist", "exp", "var", "prefixexp", "functioncall", 
                   "tail", "nestedtail", "args", "anonfunctiondef", "funcbody", 
                   "parlist", "tableconstructor", "fieldlist", "field", 
                   "fieldsep", "number", "string" ]

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
            self.state = 78
            self.chunk()
            self.state = 79
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
            self.state = 81
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
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self.stat() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291464) != 0):
                self.state = 89
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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(LuaParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.functioncall(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.label()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.match(LuaParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.goto()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.do()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.while_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.repeat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 101
                self.if_()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 102
                self.for_()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 103
                self.forin()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 104
                self.functiondef()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 105
                self.localfunction()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 106
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
            self.state = 109
            self.varlist()
            self.state = 110
            self.match(LuaParser.EQ)
            self.state = 111
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
            self.state = 113
            self.match(LuaParser.GOTO)
            self.state = 114
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
            self.state = 116
            self.match(LuaParser.DO)
            self.state = 117
            self.block()
            self.state = 118
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
            self.state = 120
            self.match(LuaParser.WHILE)
            self.state = 121
            self.exp(0)
            self.state = 122
            self.match(LuaParser.DO)
            self.state = 123
            self.block()
            self.state = 124
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
            self.state = 126
            self.match(LuaParser.REPEAT)
            self.state = 127
            self.block()
            self.state = 128
            self.match(LuaParser.UNTIL)
            self.state = 129
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
            self.state = 131
            self.match(LuaParser.IF)
            self.state = 132
            self.exp(0)
            self.state = 133
            self.match(LuaParser.THEN)
            self.state = 134
            self.block()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 135
                self.match(LuaParser.ELSEIF)
                self.state = 136
                self.exp(0)
                self.state = 137
                self.match(LuaParser.THEN)
                self.state = 138
                self.block()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 145
                self.match(LuaParser.ELSE)
                self.state = 146
                self.block()


            self.state = 149
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
            self.state = 151
            self.match(LuaParser.FOR)
            self.state = 152
            self.match(LuaParser.NAME)
            self.state = 153
            self.match(LuaParser.EQ)
            self.state = 154
            self.exp(0)
            self.state = 155
            self.match(LuaParser.COMMA)
            self.state = 156
            self.exp(0)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 157
                self.match(LuaParser.COMMA)
                self.state = 158
                self.exp(0)


            self.state = 161
            self.match(LuaParser.DO)
            self.state = 162
            self.block()
            self.state = 163
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
            self.state = 165
            self.match(LuaParser.FOR)
            self.state = 166
            self.namelist()
            self.state = 167
            self.match(LuaParser.IN)
            self.state = 168
            self.explist()
            self.state = 169
            self.match(LuaParser.DO)
            self.state = 170
            self.block()
            self.state = 171
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
            self.state = 173
            self.match(LuaParser.FUNCTION)
            self.state = 174
            self.funcname()
            self.state = 175
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
            self.state = 177
            self.match(LuaParser.LOCAL)
            self.state = 178
            self.match(LuaParser.FUNCTION)
            self.state = 179
            self.match(LuaParser.NAME)
            self.state = 180
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
            self.state = 182
            self.match(LuaParser.LOCAL)
            self.state = 183
            self.namelist()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 184
                self.match(LuaParser.EQ)
                self.state = 185
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
            self.state = 188
            self.match(LuaParser.NAME)
            self.state = 189
            self.attrib()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 190
                self.match(LuaParser.COMMA)
                self.state = 191
                self.match(LuaParser.NAME)
                self.state = 192
                self.attrib()
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
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 198
                self.match(LuaParser.LT)
                self.state = 199
                self.match(LuaParser.NAME)
                self.state = 200
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 203
                self.match(LuaParser.RETURN)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 204
                    self.explist()


                pass
            elif token in [3]:
                self.state = 207
                self.match(LuaParser.BREAK)
                pass
            elif token in [22]:
                self.state = 208
                self.match(LuaParser.CONTINUE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 211
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
            self.state = 214
            self.match(LuaParser.CC)
            self.state = 215
            self.match(LuaParser.NAME)
            self.state = 216
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
            self.state = 218
            self.match(LuaParser.NAME)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 219
                self.match(LuaParser.DOT)
                self.state = 220
                self.match(LuaParser.NAME)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 226
                self.match(LuaParser.COL)
                self.state = 227
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
            self.state = 230
            self.var()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 231
                self.match(LuaParser.COMMA)
                self.state = 232
                self.var()
                self.state = 237
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
            self.state = 238
            self.match(LuaParser.NAME)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 239
                    self.match(LuaParser.COMMA)
                    self.state = 240
                    self.match(LuaParser.NAME) 
                self.state = 245
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
            self.state = 246
            self.exp(0)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 247
                self.match(LuaParser.COMMA)
                self.state = 248
                self.exp(0)
                self.state = 253
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
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 255
                self.match(LuaParser.NIL)
                pass
            elif token in [25]:
                self.state = 256
                self.match(LuaParser.FALSE)
                pass
            elif token in [26]:
                self.state = 257
                self.match(LuaParser.TRUE)
                pass
            elif token in [61, 62, 63, 64]:
                self.state = 258
                self.number()
                pass
            elif token in [58, 59, 60]:
                self.state = 259
                self.string()
                pass
            elif token in [55]:
                self.state = 260
                self.match(LuaParser.DDD)
                pass
            elif token in [17]:
                self.state = 261
                self.functiondef()
                pass
            elif token in [31, 57]:
                self.state = 262
                self.prefixexp()
                pass
            elif token in [46]:
                self.state = 263
                self.tableconstructor()
                pass
            elif token in [28, 29, 30, 33]:
                self.state = 264
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 10468982784) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.exp(8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 292
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 268
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")

                        self.state = 269
                        self.match(LuaParser.CARET)
                        self.state = 270
                        self.exp(9)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 271
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 272
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18049995198431232) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 273
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 274
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 275
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==44):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 276
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 277
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")

                        self.state = 278
                        self.match(LuaParser.DD)
                        self.state = 279
                        self.exp(5)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 280
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 281
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 73186792481226752) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 282
                        self.exp(5)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 283
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")

                        self.state = 284
                        self.match(LuaParser.AND)
                        self.state = 285
                        self.exp(4)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 286
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 287
                        self.match(LuaParser.OR)
                        self.state = 288
                        self.exp(3)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 289
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 290
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503720154890240) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 291
                        self.exp(2)
                        pass

             
                self.state = 296
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
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(LuaParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.prefixexp()
                self.state = 299
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


        def nestedtail(self):
            return self.getTypedRuleContext(LuaParser.NestedtailContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixexp" ):
                return visitor.visitPrefixexp(self)
            else:
                return visitor.visitChildren(self)




    def prefixexp(self):

        localctx = LuaParser.PrefixexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_prefixexp)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(LuaParser.NAME)
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 310
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [48]:
                            self.state = 304
                            self.match(LuaParser.OB)
                            self.state = 305
                            self.exp(0)
                            self.state = 306
                            self.match(LuaParser.CB)
                            pass
                        elif token in [27]:
                            self.state = 308
                            self.match(LuaParser.DOT)
                            self.state = 309
                            self.match(LuaParser.NAME)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 314
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.functioncall(0)
                self.state = 316
                self.nestedtail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(LuaParser.OP)
                self.state = 319
                self.exp(0)
                self.state = 320
                self.match(LuaParser.CP)
                self.state = 321
                self.nestedtail()
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

        def nestedtail(self):
            return self.getTypedRuleContext(LuaParser.NestedtailContext,0)


        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 326
                self.match(LuaParser.NAME)
                self.state = 327
                self.nestedtail()
                self.state = 328
                self.args()
                pass

            elif la_ == 2:
                self.state = 330
                self.match(LuaParser.OP)
                self.state = 331
                self.exp(0)
                self.state = 332
                self.match(LuaParser.CP)
                self.state = 333
                self.nestedtail()
                self.state = 334
                self.args()
                pass

            elif la_ == 3:
                self.state = 336
                self.match(LuaParser.NAME)
                self.state = 337
                self.nestedtail()
                self.state = 338
                self.match(LuaParser.COL)
                self.state = 339
                self.match(LuaParser.NAME)
                self.state = 340
                self.args()
                pass

            elif la_ == 4:
                self.state = 342
                self.match(LuaParser.OP)
                self.state = 343
                self.exp(0)
                self.state = 344
                self.match(LuaParser.CP)
                self.state = 345
                self.nestedtail()
                self.state = 346
                self.match(LuaParser.COL)
                self.state = 347
                self.match(LuaParser.NAME)
                self.state = 348
                self.args()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 364
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 362
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.FunctioncallContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 352
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 353
                        self.nestedtail()
                        self.state = 354
                        self.args()
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.FunctioncallContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_functioncall)
                        self.state = 356
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 357
                        self.nestedtail()
                        self.state = 358
                        self.match(LuaParser.COL)
                        self.state = 359
                        self.match(LuaParser.NAME)
                        self.state = 360
                        self.args()
                        pass

             
                self.state = 366
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 367
                self.match(LuaParser.OB)
                self.state = 368
                self.exp(0)
                self.state = 369
                self.match(LuaParser.CB)
                pass
            elif token in [27]:
                self.state = 371
                self.match(LuaParser.DOT)
                self.state = 372
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


    class NestedtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.TailContext)
            else:
                return self.getTypedRuleContext(LuaParser.TailContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_nestedtail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedtail" ):
                listener.enterNestedtail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedtail" ):
                listener.exitNestedtail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedtail" ):
                return visitor.visitNestedtail(self)
            else:
                return visitor.visitChildren(self)




    def nestedtail(self):

        localctx = LuaParser.NestedtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_nestedtail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 375
                    self.tail() 
                self.state = 380
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 58, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(LuaParser.OP)
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280650879957889) != 0):
                    self.state = 382
                    self.explist()


                self.state = 385
                self.match(LuaParser.CP)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.tableconstructor()
                pass
            elif token in [58, 59, 60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
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
        self.enterRule(localctx, 60, self.RULE_anonfunctiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(LuaParser.FUNCTION)
            self.state = 391
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
        self.enterRule(localctx, 62, self.RULE_funcbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(LuaParser.OP)
            self.state = 394
            self.parlist()
            self.state = 395
            self.match(LuaParser.CP)
            self.state = 396
            self.block()
            self.state = 397
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
        self.enterRule(localctx, 64, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.namelist()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 400
                    self.match(LuaParser.COMMA)
                    self.state = 401
                    self.match(LuaParser.DDD)


                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
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
        self.enterRule(localctx, 66, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(LuaParser.OCU)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 280653027441537) != 0):
                self.state = 409
                self.fieldlist()


            self.state = 412
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
        self.enterRule(localctx, 68, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.field()
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 415
                    self.fieldsep()
                    self.state = 416
                    self.field() 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==15:
                self.state = 423
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
        self.enterRule(localctx, 70, self.RULE_field)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.match(LuaParser.OB)
                self.state = 427
                self.exp(0)
                self.state = 428
                self.match(LuaParser.CB)
                self.state = 429
                self.match(LuaParser.EQ)
                self.state = 430
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(LuaParser.NAME)
                self.state = 433
                self.match(LuaParser.EQ)
                self.state = 434
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 435
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
        self.enterRule(localctx, 72, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
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
        self.enterRule(localctx, 74, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
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
        self.enterRule(localctx, 76, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
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
         




