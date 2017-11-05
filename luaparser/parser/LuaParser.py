# Generated from parser/Lua.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u01ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2")
        buf.write("\3\3\7\3w\n\3\f\3\16\3z\13\3\3\3\5\3}\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u0090\n\4\3\5\3\5\3\5\3\5\3\6\3\6\6\6\u0098\n\6")
        buf.write("\r\6\16\6\u0099\3\7\3\7\3\7\3\7\3\7\6\7\u00a1\n\7\r\7")
        buf.write("\16\7\u00a2\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u00c6\n\16\f\16\16\16\u00c9\13\16\3\16\3\16\5\16\u00cd")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00d9\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00f4\n\23\3")
        buf.write("\24\3\24\5\24\u00f8\n\24\3\24\5\24\u00fb\n\24\3\25\3\25")
        buf.write("\3\25\7\25\u0100\n\25\f\25\16\25\u0103\13\25\3\25\3\25")
        buf.write("\5\25\u0107\n\25\3\26\3\26\3\26\7\26\u010c\n\26\f\26\16")
        buf.write("\26\u010f\13\26\3\27\3\27\3\27\7\27\u0114\n\27\f\27\16")
        buf.write("\27\u0117\13\27\3\30\3\30\3\31\3\31\3\31\7\31\u011e\n")
        buf.write("\31\f\31\16\31\u0121\13\31\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0133\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u0155\n\32\f\32\16\32\u0158\13\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\7#\u0170\n#\f#\16")
        buf.write("#\u0173\13#\3$\3$\3$\3$\3$\5$\u017a\n$\3%\3%\3%\3%\3%")
        buf.write("\3%\5%\u0182\n%\3%\7%\u0185\n%\f%\16%\u0188\13%\3&\7&")
        buf.write("\u018b\n&\f&\16&\u018e\13&\3&\3&\3&\3&\3&\3&\5&\u0196")
        buf.write("\n&\3\'\3\'\5\'\u019a\n\'\3\'\3\'\3(\3(\5(\u01a0\n(\3")
        buf.write("(\3(\3(\5(\u01a5\n(\3)\3)\3)\3*\3*\5*\u01ac\n*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\5+\u01b5\n+\3+\5+\u01b8\n+\3,\3,\5,\u01bc")
        buf.write("\n,\3,\3,\3-\3-\3-\3-\7-\u01c4\n-\f-\16-\u01c7\13-\3-")
        buf.write("\5-\u01ca\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01d7")
        buf.write("\n.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\2\3")
        buf.write("\62:\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\n\3\2>A\4\2")
        buf.write("\3\3\23\23\3\2).\4\2\37\37\60\60\3\2\61\64\4\2  \658\3")
        buf.write("\2;=\3\2BC\2\u01fd\2r\3\2\2\2\4x\3\2\2\2\6\u008f\3\2\2")
        buf.write("\2\b\u0091\3\2\2\2\n\u0095\3\2\2\2\f\u009b\3\2\2\2\16")
        buf.write("\u00a4\3\2\2\2\20\u00a8\3\2\2\2\22\u00aa\3\2\2\2\24\u00ad")
        buf.write("\3\2\2\2\26\u00b1\3\2\2\2\30\u00b7\3\2\2\2\32\u00bc\3")
        buf.write("\2\2\2\34\u00d0\3\2\2\2\36\u00de\3\2\2\2 \u00e6\3\2\2")
        buf.write("\2\"\u00ea\3\2\2\2$\u00ef\3\2\2\2&\u00f5\3\2\2\2(\u00fc")
        buf.write("\3\2\2\2*\u0108\3\2\2\2,\u0110\3\2\2\2.\u0118\3\2\2\2")
        buf.write("\60\u011a\3\2\2\2\62\u0132\3\2\2\2\64\u0159\3\2\2\2\66")
        buf.write("\u015b\3\2\2\28\u015d\3\2\2\2:\u015f\3\2\2\2<\u0161\3")
        buf.write("\2\2\2>\u0164\3\2\2\2@\u0167\3\2\2\2B\u016a\3\2\2\2D\u016d")
        buf.write("\3\2\2\2F\u0179\3\2\2\2H\u0181\3\2\2\2J\u018c\3\2\2\2")
        buf.write("L\u0199\3\2\2\2N\u01a4\3\2\2\2P\u01a6\3\2\2\2R\u01a9\3")
        buf.write("\2\2\2T\u01b7\3\2\2\2V\u01b9\3\2\2\2X\u01bf\3\2\2\2Z\u01d6")
        buf.write("\3\2\2\2\\\u01d8\3\2\2\2^\u01da\3\2\2\2`\u01dc\3\2\2\2")
        buf.write("b\u01de\3\2\2\2d\u01e0\3\2\2\2f\u01e2\3\2\2\2h\u01e4\3")
        buf.write("\2\2\2j\u01e6\3\2\2\2l\u01e8\3\2\2\2n\u01ea\3\2\2\2p\u01ec")
        buf.write("\3\2\2\2rs\5\4\3\2st\7\2\2\3t\3\3\2\2\2uw\5\6\4\2vu\3")
        buf.write("\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y|\3\2\2\2zx\3\2\2")
        buf.write("\2{}\5&\24\2|{\3\2\2\2|}\3\2\2\2}\5\3\2\2\2~\u0090\7\3")
        buf.write("\2\2\177\u0090\5p9\2\u0080\u0090\5\b\5\2\u0081\u0090\5")
        buf.write("\n\6\2\u0082\u0090\5\f\7\2\u0083\u0090\5\16\b\2\u0084")
        buf.write("\u0090\5\20\t\2\u0085\u0090\5\22\n\2\u0086\u0090\5\24")
        buf.write("\13\2\u0087\u0090\5\26\f\2\u0088\u0090\5\30\r\2\u0089")
        buf.write("\u0090\5\32\16\2\u008a\u0090\5\34\17\2\u008b\u0090\5\36")
        buf.write("\20\2\u008c\u0090\5 \21\2\u008d\u0090\5\"\22\2\u008e\u0090")
        buf.write("\5$\23\2\u008f~\3\2\2\2\u008f\177\3\2\2\2\u008f\u0080")
        buf.write("\3\2\2\2\u008f\u0081\3\2\2\2\u008f\u0082\3\2\2\2\u008f")
        buf.write("\u0083\3\2\2\2\u008f\u0084\3\2\2\2\u008f\u0085\3\2\2\2")
        buf.write("\u008f\u0086\3\2\2\2\u008f\u0087\3\2\2\2\u008f\u0088\3")
        buf.write("\2\2\2\u008f\u0089\3\2\2\2\u008f\u008a\3\2\2\2\u008f\u008b")
        buf.write("\3\2\2\2\u008f\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\7\3\2\2\2\u0091\u0092\5*\26\2\u0092")
        buf.write("\u0093\7\4\2\2\u0093\u0094\5\60\31\2\u0094\t\3\2\2\2\u0095")
        buf.write("\u0097\5F$\2\u0096\u0098\5N(\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\13\3\2\2\2\u009b\u00a0\5F$\2\u009c\u009d\7\5\2")
        buf.write("\2\u009d\u009e\5.\30\2\u009e\u009f\5N(\2\u009f\u00a1\3")
        buf.write("\2\2\2\u00a0\u009c\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\r\3\2\2\2\u00a4\u00a5")
        buf.write("\7\6\2\2\u00a5\u00a6\5.\30\2\u00a6\u00a7\7\6\2\2\u00a7")
        buf.write("\17\3\2\2\2\u00a8\u00a9\7\7\2\2\u00a9\21\3\2\2\2\u00aa")
        buf.write("\u00ab\7\b\2\2\u00ab\u00ac\5.\30\2\u00ac\23\3\2\2\2\u00ad")
        buf.write("\u00ae\7\t\2\2\u00ae\u00af\5\4\3\2\u00af\u00b0\7\n\2\2")
        buf.write("\u00b0\25\3\2\2\2\u00b1\u00b2\7\13\2\2\u00b2\u00b3\5\62")
        buf.write("\32\2\u00b3\u00b4\7\t\2\2\u00b4\u00b5\5\4\3\2\u00b5\u00b6")
        buf.write("\7\n\2\2\u00b6\27\3\2\2\2\u00b7\u00b8\7\f\2\2\u00b8\u00b9")
        buf.write("\5\4\3\2\u00b9\u00ba\7\r\2\2\u00ba\u00bb\5\62\32\2\u00bb")
        buf.write("\31\3\2\2\2\u00bc\u00bd\7\16\2\2\u00bd\u00be\5\62\32\2")
        buf.write("\u00be\u00bf\7\17\2\2\u00bf\u00c7\5\4\3\2\u00c0\u00c1")
        buf.write("\7\20\2\2\u00c1\u00c2\5\62\32\2\u00c2\u00c3\7\17\2\2\u00c3")
        buf.write("\u00c4\5\4\3\2\u00c4\u00c6\3\2\2\2\u00c5\u00c0\3\2\2\2")
        buf.write("\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3")
        buf.write("\2\2\2\u00c8\u00cc\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb")
        buf.write("\7\21\2\2\u00cb\u00cd\5\4\3\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7\n\2\2")
        buf.write("\u00cf\33\3\2\2\2\u00d0\u00d1\7\22\2\2\u00d1\u00d2\5.")
        buf.write("\30\2\u00d2\u00d3\7\4\2\2\u00d3\u00d4\5\62\32\2\u00d4")
        buf.write("\u00d5\7\23\2\2\u00d5\u00d8\5\62\32\2\u00d6\u00d7\7\23")
        buf.write("\2\2\u00d7\u00d9\5\62\32\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\7\t\2\2\u00db")
        buf.write("\u00dc\5\4\3\2\u00dc\u00dd\7\n\2\2\u00dd\35\3\2\2\2\u00de")
        buf.write("\u00df\7\22\2\2\u00df\u00e0\5,\27\2\u00e0\u00e1\7\24\2")
        buf.write("\2\u00e1\u00e2\5\60\31\2\u00e2\u00e3\7\t\2\2\u00e3\u00e4")
        buf.write("\5\4\3\2\u00e4\u00e5\7\n\2\2\u00e5\37\3\2\2\2\u00e6\u00e7")
        buf.write("\7\25\2\2\u00e7\u00e8\5(\25\2\u00e8\u00e9\5R*\2\u00e9")
        buf.write("!\3\2\2\2\u00ea\u00eb\7\26\2\2\u00eb\u00ec\7\25\2\2\u00ec")
        buf.write("\u00ed\5.\30\2\u00ed\u00ee\5R*\2\u00ee#\3\2\2\2\u00ef")
        buf.write("\u00f0\7\26\2\2\u00f0\u00f3\5,\27\2\u00f1\u00f2\7\4\2")
        buf.write("\2\u00f2\u00f4\5\60\31\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4%\3\2\2\2\u00f5\u00f7\7\27\2\2\u00f6\u00f8")
        buf.write("\5\60\31\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00fa\3\2\2\2\u00f9\u00fb\7\3\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\'\3\2\2\2\u00fc\u0101\5.\30")
        buf.write("\2\u00fd\u00fe\7\30\2\2\u00fe\u0100\5.\30\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0106\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0104\u0105\7\5\2\2\u0105\u0107\5.\30\2\u0106\u0104\3")
        buf.write("\2\2\2\u0106\u0107\3\2\2\2\u0107)\3\2\2\2\u0108\u010d")
        buf.write("\5H%\2\u0109\u010a\7\23\2\2\u010a\u010c\5H%\2\u010b\u0109")
        buf.write("\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e+\3\2\2\2\u010f\u010d\3\2\2\2\u0110")
        buf.write("\u0115\5.\30\2\u0111\u0112\7\23\2\2\u0112\u0114\5.\30")
        buf.write("\2\u0113\u0111\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116-\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0118\u0119\7:\2\2\u0119/\3\2\2\2\u011a\u011f")
        buf.write("\5\62\32\2\u011b\u011c\7\23\2\2\u011c\u011e\5\62\32\2")
        buf.write("\u011d\u011b\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3")
        buf.write("\2\2\2\u011f\u0120\3\2\2\2\u0120\61\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0122\u0123\b\32\1\2\u0123\u0133\5\64\33\2\u0124")
        buf.write("\u0133\5\66\34\2\u0125\u0133\58\35\2\u0126\u0133\5:\36")
        buf.write("\2\u0127\u0133\5n8\2\u0128\u0133\7\31\2\2\u0129\u0133")
        buf.write("\5\n\6\2\u012a\u0133\5\f\7\2\u012b\u0133\5P)\2\u012c\u0133")
        buf.write("\5D#\2\u012d\u0133\5V,\2\u012e\u0133\5<\37\2\u012f\u0133")
        buf.write("\5> \2\u0130\u0133\5@!\2\u0131\u0133\5B\"\2\u0132\u0122")
        buf.write("\3\2\2\2\u0132\u0124\3\2\2\2\u0132\u0125\3\2\2\2\u0132")
        buf.write("\u0126\3\2\2\2\u0132\u0127\3\2\2\2\u0132\u0128\3\2\2\2")
        buf.write("\u0132\u0129\3\2\2\2\u0132\u012a\3\2\2\2\u0132\u012b\3")
        buf.write("\2\2\2\u0132\u012c\3\2\2\2\u0132\u012d\3\2\2\2\u0132\u012e")
        buf.write("\3\2\2\2\u0132\u012f\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0156\3\2\2\2\u0134\u0135\f\16\2")
        buf.write("\2\u0135\u0136\5l\67\2\u0136\u0137\5\62\32\16\u0137\u0155")
        buf.write("\3\2\2\2\u0138\u0139\f\t\2\2\u0139\u013a\5h\65\2\u013a")
        buf.write("\u013b\5\62\32\n\u013b\u0155\3\2\2\2\u013c\u013d\f\b\2")
        buf.write("\2\u013d\u013e\5f\64\2\u013e\u013f\5\62\32\t\u013f\u0155")
        buf.write("\3\2\2\2\u0140\u0141\f\7\2\2\u0141\u0142\5d\63\2\u0142")
        buf.write("\u0143\5\62\32\7\u0143\u0155\3\2\2\2\u0144\u0145\f\6\2")
        buf.write("\2\u0145\u0146\5b\62\2\u0146\u0147\5\62\32\7\u0147\u0155")
        buf.write("\3\2\2\2\u0148\u0149\f\5\2\2\u0149\u014a\5`\61\2\u014a")
        buf.write("\u014b\5\62\32\6\u014b\u0155\3\2\2\2\u014c\u014d\f\4\2")
        buf.write("\2\u014d\u014e\5^\60\2\u014e\u014f\5\62\32\5\u014f\u0155")
        buf.write("\3\2\2\2\u0150\u0151\f\3\2\2\u0151\u0152\5j\66\2\u0152")
        buf.write("\u0153\5\62\32\4\u0153\u0155\3\2\2\2\u0154\u0134\3\2\2")
        buf.write("\2\u0154\u0138\3\2\2\2\u0154\u013c\3\2\2\2\u0154\u0140")
        buf.write("\3\2\2\2\u0154\u0144\3\2\2\2\u0154\u0148\3\2\2\2\u0154")
        buf.write("\u014c\3\2\2\2\u0154\u0150\3\2\2\2\u0155\u0158\3\2\2\2")
        buf.write("\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\63\3\2")
        buf.write("\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7\32\2\2\u015a\65")
        buf.write("\3\2\2\2\u015b\u015c\7\33\2\2\u015c\67\3\2\2\2\u015d\u015e")
        buf.write("\7\34\2\2\u015e9\3\2\2\2\u015f\u0160\t\2\2\2\u0160;\3")
        buf.write("\2\2\2\u0161\u0162\7\35\2\2\u0162\u0163\5\62\32\2\u0163")
        buf.write("=\3\2\2\2\u0164\u0165\7\36\2\2\u0165\u0166\5\62\32\2\u0166")
        buf.write("?\3\2\2\2\u0167\u0168\7\37\2\2\u0168\u0169\5\62\32\2\u0169")
        buf.write("A\3\2\2\2\u016a\u016b\7 \2\2\u016b\u016c\5\62\32\2\u016c")
        buf.write("C\3\2\2\2\u016d\u0171\5F$\2\u016e\u0170\5L\'\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172E\3\2\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write("\u017a\5H%\2\u0175\u0176\7!\2\2\u0176\u0177\5\62\32\2")
        buf.write("\u0177\u0178\7\"\2\2\u0178\u017a\3\2\2\2\u0179\u0174\3")
        buf.write("\2\2\2\u0179\u0175\3\2\2\2\u017aG\3\2\2\2\u017b\u0182")
        buf.write("\5.\30\2\u017c\u017d\7!\2\2\u017d\u017e\5\62\32\2\u017e")
        buf.write("\u017f\7\"\2\2\u017f\u0180\5J&\2\u0180\u0182\3\2\2\2\u0181")
        buf.write("\u017b\3\2\2\2\u0181\u017c\3\2\2\2\u0182\u0186\3\2\2\2")
        buf.write("\u0183\u0185\5J&\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2")
        buf.write("\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187I\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0189\u018b\5L\'\2\u018a\u0189")
        buf.write("\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u0195\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018f\u0190\7#\2\2\u0190\u0191\5\62\32\2\u0191\u0192")
        buf.write("\7$\2\2\u0192\u0196\3\2\2\2\u0193\u0194\7\30\2\2\u0194")
        buf.write("\u0196\5.\30\2\u0195\u018f\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0196K\3\2\2\2\u0197\u0198\7\5\2\2\u0198\u019a\5.\30")
        buf.write("\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u019c\5N(\2\u019cM\3\2\2\2\u019d\u019f")
        buf.write("\7!\2\2\u019e\u01a0\5\60\31\2\u019f\u019e\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a5\7\"\2\2")
        buf.write("\u01a2\u01a5\5V,\2\u01a3\u01a5\5n8\2\u01a4\u019d\3\2\2")
        buf.write("\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5O\3\2")
        buf.write("\2\2\u01a6\u01a7\7\25\2\2\u01a7\u01a8\5R*\2\u01a8Q\3\2")
        buf.write("\2\2\u01a9\u01ab\7!\2\2\u01aa\u01ac\5T+\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ae\7\"\2\2\u01ae\u01af\5\4\3\2\u01af\u01b0\7\n\2\2")
        buf.write("\u01b0S\3\2\2\2\u01b1\u01b4\5,\27\2\u01b2\u01b3\7\23\2")
        buf.write("\2\u01b3\u01b5\7\31\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5")
        buf.write("\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b8\7\31\2\2\u01b7")
        buf.write("\u01b1\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8U\3\2\2\2\u01b9")
        buf.write("\u01bb\7%\2\2\u01ba\u01bc\5X-\2\u01bb\u01ba\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\7&\2\2")
        buf.write("\u01beW\3\2\2\2\u01bf\u01c5\5Z.\2\u01c0\u01c1\5\\/\2\u01c1")
        buf.write("\u01c2\5Z.\2\u01c2\u01c4\3\2\2\2\u01c3\u01c0\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca\5")
        buf.write("\\/\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01caY\3")
        buf.write("\2\2\2\u01cb\u01cc\7#\2\2\u01cc\u01cd\5\62\32\2\u01cd")
        buf.write("\u01ce\7$\2\2\u01ce\u01cf\7\4\2\2\u01cf\u01d0\5\62\32")
        buf.write("\2\u01d0\u01d7\3\2\2\2\u01d1\u01d2\5.\30\2\u01d2\u01d3")
        buf.write("\7\4\2\2\u01d3\u01d4\5\62\32\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d7\5\62\32\2\u01d6\u01cb\3\2\2\2\u01d6\u01d1\3\2\2")
        buf.write("\2\u01d6\u01d5\3\2\2\2\u01d7[\3\2\2\2\u01d8\u01d9\t\3")
        buf.write("\2\2\u01d9]\3\2\2\2\u01da\u01db\7\'\2\2\u01db_\3\2\2\2")
        buf.write("\u01dc\u01dd\7(\2\2\u01dda\3\2\2\2\u01de\u01df\t\4\2\2")
        buf.write("\u01dfc\3\2\2\2\u01e0\u01e1\7/\2\2\u01e1e\3\2\2\2\u01e2")
        buf.write("\u01e3\t\5\2\2\u01e3g\3\2\2\2\u01e4\u01e5\t\6\2\2\u01e5")
        buf.write("i\3\2\2\2\u01e6\u01e7\t\7\2\2\u01e7k\3\2\2\2\u01e8\u01e9")
        buf.write("\79\2\2\u01e9m\3\2\2\2\u01ea\u01eb\t\b\2\2\u01ebo\3\2")
        buf.write("\2\2\u01ec\u01ed\t\t\2\2\u01edq\3\2\2\2%x|\u008f\u0099")
        buf.write("\u00a2\u00c7\u00cc\u00d8\u00f3\u00f7\u00fa\u0101\u0106")
        buf.write("\u010d\u0115\u011f\u0132\u0154\u0156\u0171\u0179\u0181")
        buf.write("\u0186\u018c\u0195\u0199\u019f\u01a4\u01ab\u01b4\u01b7")
        buf.write("\u01bb\u01c5\u01c9\u01d6")
        return buf.getvalue()


class LuaParser ( Parser ):

    grammarFileName = "Lua.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "':'", "'::'", "'break'", 
                     "'goto'", "'do'", "'end'", "'while'", "'repeat'", "'until'", 
                     "'if'", "'then'", "'elseif'", "'else'", "'for'", "','", 
                     "'in'", "'function'", "'local'", "'return'", "'.'", 
                     "'...'", "'nil'", "'false'", "'true'", "'not'", "'#'", 
                     "'-'", "'~'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'or'", "'and'", "'<'", "'>'", "'<='", "'>='", "'~='", 
                     "'=='", "'..'", "'+'", "'*'", "'/'", "'%'", "'//'", 
                     "'&'", "'|'", "'<<'", "'>>'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NAME", "NORMALSTRING", "CHARSTRING", "LONGSTRING", 
                      "INT", "HEX", "FLOAT", "HEX_FLOAT", "COMMENT", "LINE_COMMENT", 
                      "WS", "SHEBANG" ]

    RULE_chunk = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_setStat = 3
    RULE_call = 4
    RULE_invoke = 5
    RULE_label = 6
    RULE_breakStat = 7
    RULE_goto = 8
    RULE_do = 9
    RULE_whileStat = 10
    RULE_repeat = 11
    RULE_ifStat = 12
    RULE_fornum = 13
    RULE_forin = 14
    RULE_func = 15
    RULE_localfunc = 16
    RULE_localset = 17
    RULE_retstat = 18
    RULE_funcname = 19
    RULE_varlist = 20
    RULE_namelist = 21
    RULE_name = 22
    RULE_explist = 23
    RULE_exp = 24
    RULE_nil = 25
    RULE_false = 26
    RULE_true = 27
    RULE_number = 28
    RULE_unOpNot = 29
    RULE_unOpLength = 30
    RULE_unOpMin = 31
    RULE_unOpBitNot = 32
    RULE_prefixexp = 33
    RULE_varOrExp = 34
    RULE_var = 35
    RULE_varSuffix = 36
    RULE_nameAndArgs = 37
    RULE_args = 38
    RULE_functiondef = 39
    RULE_funcbody = 40
    RULE_parlist = 41
    RULE_tableconstructor = 42
    RULE_fieldlist = 43
    RULE_field = 44
    RULE_fieldsep = 45
    RULE_operatorOr = 46
    RULE_operatorAnd = 47
    RULE_operatorComparison = 48
    RULE_operatorStrcat = 49
    RULE_operatorAddSub = 50
    RULE_operatorMulDivMod = 51
    RULE_operatorBitwise = 52
    RULE_operatorPower = 53
    RULE_string = 54
    RULE_comment_rule = 55

    ruleNames =  [ "chunk", "block", "stat", "setStat", "call", "invoke", 
                   "label", "breakStat", "goto", "do", "whileStat", "repeat", 
                   "ifStat", "fornum", "forin", "func", "localfunc", "localset", 
                   "retstat", "funcname", "varlist", "namelist", "name", 
                   "explist", "exp", "nil", "false", "true", "number", "unOpNot", 
                   "unOpLength", "unOpMin", "unOpBitNot", "prefixexp", "varOrExp", 
                   "var", "varSuffix", "nameAndArgs", "args", "functiondef", 
                   "funcbody", "parlist", "tableconstructor", "fieldlist", 
                   "field", "fieldsep", "operatorOr", "operatorAnd", "operatorComparison", 
                   "operatorStrcat", "operatorAddSub", "operatorMulDivMod", 
                   "operatorBitwise", "operatorPower", "string", "comment_rule" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
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
    SHEBANG=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ChunkContext(ParserRuleContext):

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChunk" ):
                return visitor.visitChunk(self)
            else:
                return visitor.visitChildren(self)




    def chunk(self):

        localctx = LuaParser.ChunkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_chunk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.block()
            self.state = 113
            self.match(LuaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

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
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__0) | (1 << LuaParser.T__3) | (1 << LuaParser.T__4) | (1 << LuaParser.T__5) | (1 << LuaParser.T__6) | (1 << LuaParser.T__8) | (1 << LuaParser.T__9) | (1 << LuaParser.T__11) | (1 << LuaParser.T__15) | (1 << LuaParser.T__18) | (1 << LuaParser.T__19) | (1 << LuaParser.T__30) | (1 << LuaParser.NAME))) != 0) or _la==LuaParser.COMMENT or _la==LuaParser.LINE_COMMENT:
                self.state = 115
                self.stat()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__20:
                self.state = 121
                self.retstat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment_rule(self):
            return self.getTypedRuleContext(LuaParser.Comment_ruleContext,0)


        def setStat(self):
            return self.getTypedRuleContext(LuaParser.SetStatContext,0)


        def call(self):
            return self.getTypedRuleContext(LuaParser.CallContext,0)


        def invoke(self):
            return self.getTypedRuleContext(LuaParser.InvokeContext,0)


        def label(self):
            return self.getTypedRuleContext(LuaParser.LabelContext,0)


        def breakStat(self):
            return self.getTypedRuleContext(LuaParser.BreakStatContext,0)


        def goto(self):
            return self.getTypedRuleContext(LuaParser.GotoContext,0)


        def do(self):
            return self.getTypedRuleContext(LuaParser.DoContext,0)


        def whileStat(self):
            return self.getTypedRuleContext(LuaParser.WhileStatContext,0)


        def repeat(self):
            return self.getTypedRuleContext(LuaParser.RepeatContext,0)


        def ifStat(self):
            return self.getTypedRuleContext(LuaParser.IfStatContext,0)


        def fornum(self):
            return self.getTypedRuleContext(LuaParser.FornumContext,0)


        def forin(self):
            return self.getTypedRuleContext(LuaParser.ForinContext,0)


        def func(self):
            return self.getTypedRuleContext(LuaParser.FuncContext,0)


        def localfunc(self):
            return self.getTypedRuleContext(LuaParser.LocalfuncContext,0)


        def localset(self):
            return self.getTypedRuleContext(LuaParser.LocalsetContext,0)


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
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(LuaParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.comment_rule()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.setStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.invoke()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.label()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.breakStat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.goto()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.do()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.whileStat()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 134
                self.repeat()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 135
                self.ifStat()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 136
                self.fornum()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 137
                self.forin()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 138
                self.func()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 139
                self.localfunc()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 140
                self.localset()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SetStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varlist(self):
            return self.getTypedRuleContext(LuaParser.VarlistContext,0)


        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_setStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStat" ):
                listener.enterSetStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStat" ):
                listener.exitSetStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStat" ):
                return visitor.visitSetStat(self)
            else:
                return visitor.visitChildren(self)




    def setStat(self):

        localctx = LuaParser.SetStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_setStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.varlist()
            self.state = 144
            self.match(LuaParser.T__1)
            self.state = 145
            self.explist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.ArgsContext,i)


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
        self.enterRule(localctx, 8, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.varOrExp()
            self.state = 149 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 148
                    self.args()

                else:
                    raise NoViableAltException(self)
                self.state = 151 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InvokeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameContext,i)


        def args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.ArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_invoke

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvoke" ):
                listener.enterInvoke(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvoke" ):
                listener.exitInvoke(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvoke" ):
                return visitor.visitInvoke(self)
            else:
                return visitor.visitChildren(self)




    def invoke(self):

        localctx = LuaParser.InvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_invoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.varOrExp()
            self.state = 158 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 154
                    self.match(LuaParser.T__2)
                    self.state = 155
                    self.name()
                    self.state = 156
                    self.args()

                else:
                    raise NoViableAltException(self)
                self.state = 160 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


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
        self.enterRule(localctx, 12, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(LuaParser.T__3)
            self.state = 163
            self.name()
            self.state = 164
            self.match(LuaParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_breakStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStat" ):
                listener.enterBreakStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStat" ):
                listener.exitBreakStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStat" ):
                return visitor.visitBreakStat(self)
            else:
                return visitor.visitChildren(self)




    def breakStat(self):

        localctx = LuaParser.BreakStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_breakStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(LuaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GotoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


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
        self.enterRule(localctx, 16, self.RULE_goto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(LuaParser.T__5)
            self.state = 169
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


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
        self.enterRule(localctx, 18, self.RULE_do)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(LuaParser.T__6)
            self.state = 172
            self.block()
            self.state = 173
            self.match(LuaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_whileStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)




    def whileStat(self):

        localctx = LuaParser.WhileStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(LuaParser.T__8)
            self.state = 176
            self.exp(0)
            self.state = 177
            self.match(LuaParser.T__6)
            self.state = 178
            self.block()
            self.state = 179
            self.match(LuaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RepeatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


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
        self.enterRule(localctx, 22, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(LuaParser.T__9)
            self.state = 182
            self.block()
            self.state = 183
            self.match(LuaParser.T__10)
            self.state = 184
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.BlockContext)
            else:
                return self.getTypedRuleContext(LuaParser.BlockContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = LuaParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(LuaParser.T__11)
            self.state = 187
            self.exp(0)
            self.state = 188
            self.match(LuaParser.T__12)
            self.state = 189
            self.block()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__13:
                self.state = 190
                self.match(LuaParser.T__13)
                self.state = 191
                self.exp(0)
                self.state = 192
                self.match(LuaParser.T__12)
                self.state = 193
                self.block()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__14:
                self.state = 200
                self.match(LuaParser.T__14)
                self.state = 201
                self.block()


            self.state = 204
            self.match(LuaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FornumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_fornum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFornum" ):
                listener.enterFornum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFornum" ):
                listener.exitFornum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFornum" ):
                return visitor.visitFornum(self)
            else:
                return visitor.visitChildren(self)




    def fornum(self):

        localctx = LuaParser.FornumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fornum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(LuaParser.T__15)
            self.state = 207
            self.name()
            self.state = 208
            self.match(LuaParser.T__1)
            self.state = 209
            self.exp(0)
            self.state = 210
            self.match(LuaParser.T__16)
            self.state = 211
            self.exp(0)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__16:
                self.state = 212
                self.match(LuaParser.T__16)
                self.state = 213
                self.exp(0)


            self.state = 216
            self.match(LuaParser.T__6)
            self.state = 217
            self.block()
            self.state = 218
            self.match(LuaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


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
        self.enterRule(localctx, 28, self.RULE_forin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(LuaParser.T__15)
            self.state = 221
            self.namelist()
            self.state = 222
            self.match(LuaParser.T__17)
            self.state = 223
            self.explist()
            self.state = 224
            self.match(LuaParser.T__6)
            self.state = 225
            self.block()
            self.state = 226
            self.match(LuaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcname(self):
            return self.getTypedRuleContext(LuaParser.FuncnameContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = LuaParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(LuaParser.T__18)
            self.state = 229
            self.funcname()
            self.state = 230
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LocalfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


        def funcbody(self):
            return self.getTypedRuleContext(LuaParser.FuncbodyContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_localfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalfunc" ):
                listener.enterLocalfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalfunc" ):
                listener.exitLocalfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalfunc" ):
                return visitor.visitLocalfunc(self)
            else:
                return visitor.visitChildren(self)




    def localfunc(self):

        localctx = LuaParser.LocalfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_localfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(LuaParser.T__19)
            self.state = 233
            self.match(LuaParser.T__18)
            self.state = 234
            self.name()
            self.state = 235
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LocalsetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


        def explist(self):
            return self.getTypedRuleContext(LuaParser.ExplistContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_localset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalset" ):
                listener.enterLocalset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalset" ):
                listener.exitLocalset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalset" ):
                return visitor.visitLocalset(self)
            else:
                return visitor.visitChildren(self)




    def localset(self):

        localctx = LuaParser.LocalsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_localset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(LuaParser.T__19)
            self.state = 238
            self.namelist()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__1:
                self.state = 239
                self.match(LuaParser.T__1)
                self.state = 240
                self.explist()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RetstatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 36, self.RULE_retstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(LuaParser.T__20)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__18) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__27) | (1 << LuaParser.T__28) | (1 << LuaParser.T__29) | (1 << LuaParser.T__30) | (1 << LuaParser.T__34) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                self.state = 244
                self.explist()


            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__0:
                self.state = 247
                self.match(LuaParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameContext,i)


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
            self.state = 250
            self.name()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__21:
                self.state = 251
                self.match(LuaParser.T__21)
                self.state = 252
                self.name()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__2:
                self.state = 258
                self.match(LuaParser.T__2)
                self.state = 259
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarContext,i)


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
            self.state = 262
            self.var()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__16:
                self.state = 263
                self.match(LuaParser.T__16)
                self.state = 264
                self.var()
                self.state = 269
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameContext,i)


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
            self.state = 270
            self.name()
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 271
                    self.match(LuaParser.T__16)
                    self.state = 272
                    self.name() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(LuaParser.NAME, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = LuaParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(LuaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


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
        self.enterRule(localctx, 46, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.exp(0)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__16:
                self.state = 281
                self.match(LuaParser.T__16)
                self.state = 282
                self.exp(0)
                self.state = 287
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nil(self):
            return self.getTypedRuleContext(LuaParser.NilContext,0)


        def false(self):
            return self.getTypedRuleContext(LuaParser.FalseContext,0)


        def true(self):
            return self.getTypedRuleContext(LuaParser.TrueContext,0)


        def number(self):
            return self.getTypedRuleContext(LuaParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def call(self):
            return self.getTypedRuleContext(LuaParser.CallContext,0)


        def invoke(self):
            return self.getTypedRuleContext(LuaParser.InvokeContext,0)


        def functiondef(self):
            return self.getTypedRuleContext(LuaParser.FunctiondefContext,0)


        def prefixexp(self):
            return self.getTypedRuleContext(LuaParser.PrefixexpContext,0)


        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def unOpNot(self):
            return self.getTypedRuleContext(LuaParser.UnOpNotContext,0)


        def unOpLength(self):
            return self.getTypedRuleContext(LuaParser.UnOpLengthContext,0)


        def unOpMin(self):
            return self.getTypedRuleContext(LuaParser.UnOpMinContext,0)


        def unOpBitNot(self):
            return self.getTypedRuleContext(LuaParser.UnOpBitNotContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def operatorPower(self):
            return self.getTypedRuleContext(LuaParser.OperatorPowerContext,0)


        def operatorMulDivMod(self):
            return self.getTypedRuleContext(LuaParser.OperatorMulDivModContext,0)


        def operatorAddSub(self):
            return self.getTypedRuleContext(LuaParser.OperatorAddSubContext,0)


        def operatorStrcat(self):
            return self.getTypedRuleContext(LuaParser.OperatorStrcatContext,0)


        def operatorComparison(self):
            return self.getTypedRuleContext(LuaParser.OperatorComparisonContext,0)


        def operatorAnd(self):
            return self.getTypedRuleContext(LuaParser.OperatorAndContext,0)


        def operatorOr(self):
            return self.getTypedRuleContext(LuaParser.OperatorOrContext,0)


        def operatorBitwise(self):
            return self.getTypedRuleContext(LuaParser.OperatorBitwiseContext,0)


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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 289
                self.nil()
                pass

            elif la_ == 2:
                self.state = 290
                self.false()
                pass

            elif la_ == 3:
                self.state = 291
                self.true()
                pass

            elif la_ == 4:
                self.state = 292
                self.number()
                pass

            elif la_ == 5:
                self.state = 293
                self.string()
                pass

            elif la_ == 6:
                self.state = 294
                self.match(LuaParser.T__22)
                pass

            elif la_ == 7:
                self.state = 295
                self.call()
                pass

            elif la_ == 8:
                self.state = 296
                self.invoke()
                pass

            elif la_ == 9:
                self.state = 297
                self.functiondef()
                pass

            elif la_ == 10:
                self.state = 298
                self.prefixexp()
                pass

            elif la_ == 11:
                self.state = 299
                self.tableconstructor()
                pass

            elif la_ == 12:
                self.state = 300
                self.unOpNot()
                pass

            elif la_ == 13:
                self.state = 301
                self.unOpLength()
                pass

            elif la_ == 14:
                self.state = 302
                self.unOpMin()
                pass

            elif la_ == 15:
                self.state = 303
                self.unOpBitNot()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 338
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 306
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 307
                        self.operatorPower()
                        self.state = 308
                        self.exp(12)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 310
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 311
                        self.operatorMulDivMod()
                        self.state = 312
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 314
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 315
                        self.operatorAddSub()
                        self.state = 316
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 318
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 319
                        self.operatorStrcat()
                        self.state = 320
                        self.exp(5)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 322
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 323
                        self.operatorComparison()
                        self.state = 324
                        self.exp(5)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 326
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 327
                        self.operatorAnd()
                        self.state = 328
                        self.exp(4)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 330
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 331
                        self.operatorOr()
                        self.state = 332
                        self.exp(3)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 334
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 335
                        self.operatorBitwise()
                        self.state = 336
                        self.exp(2)
                        pass

             
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class NilContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_nil

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNil" ):
                listener.enterNil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNil" ):
                listener.exitNil(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil" ):
                return visitor.visitNil(self)
            else:
                return visitor.visitChildren(self)




    def nil(self):

        localctx = LuaParser.NilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_nil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(LuaParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FalseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_false

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)




    def false(self):

        localctx = LuaParser.FalseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_false)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(LuaParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_true

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)




    def true(self):

        localctx = LuaParser.TrueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_true)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(LuaParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

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
        self.enterRule(localctx, 56, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0)):
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

    class UnOpNotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_unOpNot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnOpNot" ):
                listener.enterUnOpNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnOpNot" ):
                listener.exitUnOpNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnOpNot" ):
                return visitor.visitUnOpNot(self)
            else:
                return visitor.visitChildren(self)




    def unOpNot(self):

        localctx = LuaParser.UnOpNotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unOpNot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(LuaParser.T__26)
            self.state = 352
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnOpLengthContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_unOpLength

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnOpLength" ):
                listener.enterUnOpLength(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnOpLength" ):
                listener.exitUnOpLength(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnOpLength" ):
                return visitor.visitUnOpLength(self)
            else:
                return visitor.visitChildren(self)




    def unOpLength(self):

        localctx = LuaParser.UnOpLengthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_unOpLength)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(LuaParser.T__27)
            self.state = 355
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnOpMinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_unOpMin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnOpMin" ):
                listener.enterUnOpMin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnOpMin" ):
                listener.exitUnOpMin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnOpMin" ):
                return visitor.visitUnOpMin(self)
            else:
                return visitor.visitChildren(self)




    def unOpMin(self):

        localctx = LuaParser.UnOpMinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_unOpMin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(LuaParser.T__28)
            self.state = 358
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnOpBitNotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_unOpBitNot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnOpBitNot" ):
                listener.enterUnOpBitNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnOpBitNot" ):
                listener.exitUnOpBitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnOpBitNot" ):
                return visitor.visitUnOpBitNot(self)
            else:
                return visitor.visitChildren(self)




    def unOpBitNot(self):

        localctx = LuaParser.UnOpBitNotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_unOpBitNot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(LuaParser.T__29)
            self.state = 361
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varOrExp(self):
            return self.getTypedRuleContext(LuaParser.VarOrExpContext,0)


        def nameAndArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


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
        self.enterRule(localctx, 66, self.RULE_prefixexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.varOrExp()
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 364
                    self.nameAndArgs() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarOrExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LuaParser.VarContext,0)


        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_varOrExp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarOrExp" ):
                listener.enterVarOrExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarOrExp" ):
                listener.exitVarOrExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarOrExp" ):
                return visitor.visitVarOrExp(self)
            else:
                return visitor.visitChildren(self)




    def varOrExp(self):

        localctx = LuaParser.VarOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_varOrExp)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.match(LuaParser.T__30)
                self.state = 372
                self.exp(0)
                self.state = 373
                self.match(LuaParser.T__31)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def varSuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.VarSuffixContext)
            else:
                return self.getTypedRuleContext(LuaParser.VarSuffixContext,i)


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
        self.enterRule(localctx, 70, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.NAME]:
                self.state = 377
                self.name()
                pass
            elif token in [LuaParser.T__30]:
                self.state = 378
                self.match(LuaParser.T__30)
                self.state = 379
                self.exp(0)
                self.state = 380
                self.match(LuaParser.T__31)
                self.state = 381
                self.varSuffix()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 385
                    self.varSuffix() 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarSuffixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


        def nameAndArgs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.NameAndArgsContext)
            else:
                return self.getTypedRuleContext(LuaParser.NameAndArgsContext,i)


        def getRuleIndex(self):
            return LuaParser.RULE_varSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarSuffix" ):
                listener.enterVarSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarSuffix" ):
                listener.exitVarSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarSuffix" ):
                return visitor.visitVarSuffix(self)
            else:
                return visitor.visitChildren(self)




    def varSuffix(self):

        localctx = LuaParser.VarSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_varSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__2) | (1 << LuaParser.T__30) | (1 << LuaParser.T__34) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING))) != 0):
                self.state = 391
                self.nameAndArgs()
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.T__32]:
                self.state = 397
                self.match(LuaParser.T__32)
                self.state = 398
                self.exp(0)
                self.state = 399
                self.match(LuaParser.T__33)
                pass
            elif token in [LuaParser.T__21]:
                self.state = 401
                self.match(LuaParser.T__21)
                self.state = 402
                self.name()
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

    class NameAndArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def args(self):
            return self.getTypedRuleContext(LuaParser.ArgsContext,0)


        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


        def getRuleIndex(self):
            return LuaParser.RULE_nameAndArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameAndArgs" ):
                listener.enterNameAndArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameAndArgs" ):
                listener.exitNameAndArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameAndArgs" ):
                return visitor.visitNameAndArgs(self)
            else:
                return visitor.visitChildren(self)




    def nameAndArgs(self):

        localctx = LuaParser.NameAndArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_nameAndArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__2:
                self.state = 405
                self.match(LuaParser.T__2)
                self.state = 406
                self.name()


            self.state = 409
            self.args()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 76, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.T__30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(LuaParser.T__30)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__18) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__27) | (1 << LuaParser.T__28) | (1 << LuaParser.T__29) | (1 << LuaParser.T__30) | (1 << LuaParser.T__34) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                    self.state = 412
                    self.explist()


                self.state = 415
                self.match(LuaParser.T__31)
                pass
            elif token in [LuaParser.T__34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.tableconstructor()
                pass
            elif token in [LuaParser.NORMALSTRING, LuaParser.CHARSTRING, LuaParser.LONGSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 78, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(LuaParser.T__18)
            self.state = 421
            self.funcbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncbodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LuaParser.BlockContext,0)


        def parlist(self):
            return self.getTypedRuleContext(LuaParser.ParlistContext,0)


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
        self.enterRule(localctx, 80, self.RULE_funcbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(LuaParser.T__30)
            self.state = 425
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__22 or _la==LuaParser.NAME:
                self.state = 424
                self.parlist()


            self.state = 427
            self.match(LuaParser.T__31)
            self.state = 428
            self.block()
            self.state = 429
            self.match(LuaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(LuaParser.NamelistContext,0)


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
        self.enterRule(localctx, 82, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.namelist()
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LuaParser.T__16:
                    self.state = 432
                    self.match(LuaParser.T__16)
                    self.state = 433
                    self.match(LuaParser.T__22)


                pass
            elif token in [LuaParser.T__22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(LuaParser.T__22)
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 84, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(LuaParser.T__34)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__18) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__27) | (1 << LuaParser.T__28) | (1 << LuaParser.T__29) | (1 << LuaParser.T__30) | (1 << LuaParser.T__32) | (1 << LuaParser.T__34) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                self.state = 440
                self.fieldlist()


            self.state = 443
            self.match(LuaParser.T__35)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldlistContext(ParserRuleContext):

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
        self.enterRule(localctx, 86, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.field()
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 446
                    self.fieldsep()
                    self.state = 447
                    self.field() 
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__0 or _la==LuaParser.T__16:
                self.state = 454
                self.fieldsep()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def name(self):
            return self.getTypedRuleContext(LuaParser.NameContext,0)


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
        self.enterRule(localctx, 88, self.RULE_field)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(LuaParser.T__32)
                self.state = 458
                self.exp(0)
                self.state = 459
                self.match(LuaParser.T__33)
                self.state = 460
                self.match(LuaParser.T__1)
                self.state = 461
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.name()
                self.state = 464
                self.match(LuaParser.T__1)
                self.state = 465
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


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
        self.enterRule(localctx, 90, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not(_la==LuaParser.T__0 or _la==LuaParser.T__16):
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

    class OperatorOrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorOr" ):
                listener.enterOperatorOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorOr" ):
                listener.exitOperatorOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorOr" ):
                return visitor.visitOperatorOr(self)
            else:
                return visitor.visitChildren(self)




    def operatorOr(self):

        localctx = LuaParser.OperatorOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_operatorOr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(LuaParser.T__36)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorAndContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorAnd" ):
                listener.enterOperatorAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorAnd" ):
                listener.exitOperatorAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorAnd" ):
                return visitor.visitOperatorAnd(self)
            else:
                return visitor.visitChildren(self)




    def operatorAnd(self):

        localctx = LuaParser.OperatorAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_operatorAnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(LuaParser.T__37)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorComparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorComparison" ):
                listener.enterOperatorComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorComparison" ):
                listener.exitOperatorComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorComparison" ):
                return visitor.visitOperatorComparison(self)
            else:
                return visitor.visitChildren(self)




    def operatorComparison(self):

        localctx = LuaParser.OperatorComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_operatorComparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__38) | (1 << LuaParser.T__39) | (1 << LuaParser.T__40) | (1 << LuaParser.T__41) | (1 << LuaParser.T__42) | (1 << LuaParser.T__43))) != 0)):
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

    class OperatorStrcatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorStrcat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorStrcat" ):
                listener.enterOperatorStrcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorStrcat" ):
                listener.exitOperatorStrcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorStrcat" ):
                return visitor.visitOperatorStrcat(self)
            else:
                return visitor.visitChildren(self)




    def operatorStrcat(self):

        localctx = LuaParser.OperatorStrcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_operatorStrcat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(LuaParser.T__44)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorAddSubContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorAddSub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorAddSub" ):
                listener.enterOperatorAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorAddSub" ):
                listener.exitOperatorAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorAddSub" ):
                return visitor.visitOperatorAddSub(self)
            else:
                return visitor.visitChildren(self)




    def operatorAddSub(self):

        localctx = LuaParser.OperatorAddSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_operatorAddSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            _la = self._input.LA(1)
            if not(_la==LuaParser.T__28 or _la==LuaParser.T__45):
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

    class OperatorMulDivModContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorMulDivMod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorMulDivMod" ):
                listener.enterOperatorMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorMulDivMod" ):
                listener.exitOperatorMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorMulDivMod" ):
                return visitor.visitOperatorMulDivMod(self)
            else:
                return visitor.visitChildren(self)




    def operatorMulDivMod(self):

        localctx = LuaParser.OperatorMulDivModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_operatorMulDivMod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__46) | (1 << LuaParser.T__47) | (1 << LuaParser.T__48) | (1 << LuaParser.T__49))) != 0)):
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

    class OperatorBitwiseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorBitwise

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorBitwise" ):
                listener.enterOperatorBitwise(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorBitwise" ):
                listener.exitOperatorBitwise(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorBitwise" ):
                return visitor.visitOperatorBitwise(self)
            else:
                return visitor.visitChildren(self)




    def operatorBitwise(self):

        localctx = LuaParser.OperatorBitwiseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_operatorBitwise)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__29) | (1 << LuaParser.T__50) | (1 << LuaParser.T__51) | (1 << LuaParser.T__52) | (1 << LuaParser.T__53))) != 0)):
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

    class OperatorPowerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LuaParser.RULE_operatorPower

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorPower" ):
                listener.enterOperatorPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorPower" ):
                listener.exitOperatorPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperatorPower" ):
                return visitor.visitOperatorPower(self)
            else:
                return visitor.visitChildren(self)




    def operatorPower(self):

        localctx = LuaParser.OperatorPowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_operatorPower)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(LuaParser.T__54)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

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
        self.enterRule(localctx, 108, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING))) != 0)):
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

    class Comment_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(LuaParser.COMMENT, 0)

        def LINE_COMMENT(self):
            return self.getToken(LuaParser.LINE_COMMENT, 0)

        def getRuleIndex(self):
            return LuaParser.RULE_comment_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment_rule" ):
                listener.enterComment_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment_rule" ):
                listener.exitComment_rule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment_rule" ):
                return visitor.visitComment_rule(self)
            else:
                return visitor.visitChildren(self)




    def comment_rule(self):

        localctx = LuaParser.Comment_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_comment_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            _la = self._input.LA(1)
            if not(_la==LuaParser.COMMENT or _la==LuaParser.LINE_COMMENT):
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
        self._predicates[24] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

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
         




