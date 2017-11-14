# Generated from parser/Lua.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u01cc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\3\2\3\3\7\3a\n\3\f\3\16\3d\13\3\3\3\5\3g\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4z\n\4\3\5\3\5\3\5\3\5\3\6\3\6\6\6\u0082")
        buf.write("\n\6\r\6\16\6\u0083\3\7\3\7\3\7\3\7\3\7\6\7\u008b\n\7")
        buf.write("\r\7\16\7\u008c\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00b0\n\16\f\16\16\16\u00b3\13\16\3\16\3\16\5\16")
        buf.write("\u00b7\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00c3\n\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00de\n")
        buf.write("\23\3\24\3\24\5\24\u00e2\n\24\3\24\5\24\u00e5\n\24\3\25")
        buf.write("\3\25\3\25\7\25\u00ea\n\25\f\25\16\25\u00ed\13\25\3\25")
        buf.write("\3\25\5\25\u00f1\n\25\3\26\3\26\3\26\7\26\u00f6\n\26\f")
        buf.write("\26\16\26\u00f9\13\26\3\27\3\27\3\27\7\27\u00fe\n\27\f")
        buf.write("\27\16\27\u0101\13\27\3\30\3\30\3\31\3\31\3\31\7\31\u0108")
        buf.write("\n\31\f\31\16\31\u010b\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0121\n\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u014c\n\32\f\32\16\32\u014f")
        buf.write("\13\32\3\33\3\33\7\33\u0153\n\33\f\33\16\33\u0156\13\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u015d\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0165\n\35\3\35\7\35\u0168\n\35")
        buf.write("\f\35\16\35\u016b\13\35\3\36\7\36\u016e\n\36\f\36\16\36")
        buf.write("\u0171\13\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0179")
        buf.write("\n\36\3\37\3\37\5\37\u017d\n\37\3\37\3\37\3 \3 \5 \u0183")
        buf.write("\n \3 \3 \3 \5 \u0188\n \3!\3!\3!\3\"\3\"\5\"\u018f\n")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u0198\n#\3#\5#\u019b\n")
        buf.write("#\3$\3$\5$\u019f\n$\3$\3$\3%\3%\3%\3%\7%\u01a7\n%\f%\16")
        buf.write("%\u01aa\13%\3%\5%\u01ad\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&")
        buf.write("\3&\3&\5&\u01ba\n&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\3.\2\3\62/\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2")
        buf.write("\b\3\2>A\4\2\3\3\23\23\3\2/\64\4\2  \669\3\2;=\3\2BC\2")
        buf.write("\u01e9\2\\\3\2\2\2\4b\3\2\2\2\6y\3\2\2\2\b{\3\2\2\2\n")
        buf.write("\177\3\2\2\2\f\u0085\3\2\2\2\16\u008e\3\2\2\2\20\u0092")
        buf.write("\3\2\2\2\22\u0094\3\2\2\2\24\u0097\3\2\2\2\26\u009b\3")
        buf.write("\2\2\2\30\u00a1\3\2\2\2\32\u00a6\3\2\2\2\34\u00ba\3\2")
        buf.write("\2\2\36\u00c8\3\2\2\2 \u00d0\3\2\2\2\"\u00d4\3\2\2\2$")
        buf.write("\u00d9\3\2\2\2&\u00df\3\2\2\2(\u00e6\3\2\2\2*\u00f2\3")
        buf.write("\2\2\2,\u00fa\3\2\2\2.\u0102\3\2\2\2\60\u0104\3\2\2\2")
        buf.write("\62\u0120\3\2\2\2\64\u0150\3\2\2\2\66\u015c\3\2\2\28\u0164")
        buf.write("\3\2\2\2:\u016f\3\2\2\2<\u017c\3\2\2\2>\u0187\3\2\2\2")
        buf.write("@\u0189\3\2\2\2B\u018c\3\2\2\2D\u019a\3\2\2\2F\u019c\3")
        buf.write("\2\2\2H\u01a2\3\2\2\2J\u01b9\3\2\2\2L\u01bb\3\2\2\2N\u01bd")
        buf.write("\3\2\2\2P\u01bf\3\2\2\2R\u01c1\3\2\2\2T\u01c3\3\2\2\2")
        buf.write("V\u01c5\3\2\2\2X\u01c7\3\2\2\2Z\u01c9\3\2\2\2\\]\5\4\3")
        buf.write("\2]^\7\2\2\3^\3\3\2\2\2_a\5\6\4\2`_\3\2\2\2ad\3\2\2\2")
        buf.write("b`\3\2\2\2bc\3\2\2\2cf\3\2\2\2db\3\2\2\2eg\5&\24\2fe\3")
        buf.write("\2\2\2fg\3\2\2\2g\5\3\2\2\2hz\7\3\2\2iz\5Z.\2jz\5\b\5")
        buf.write("\2kz\5\n\6\2lz\5\f\7\2mz\5\16\b\2nz\5\20\t\2oz\5\22\n")
        buf.write("\2pz\5\24\13\2qz\5\26\f\2rz\5\30\r\2sz\5\32\16\2tz\5\34")
        buf.write("\17\2uz\5\36\20\2vz\5 \21\2wz\5\"\22\2xz\5$\23\2yh\3\2")
        buf.write("\2\2yi\3\2\2\2yj\3\2\2\2yk\3\2\2\2yl\3\2\2\2ym\3\2\2\2")
        buf.write("yn\3\2\2\2yo\3\2\2\2yp\3\2\2\2yq\3\2\2\2yr\3\2\2\2ys\3")
        buf.write("\2\2\2yt\3\2\2\2yu\3\2\2\2yv\3\2\2\2yw\3\2\2\2yx\3\2\2")
        buf.write("\2z\7\3\2\2\2{|\5*\26\2|}\7\4\2\2}~\5\60\31\2~\t\3\2\2")
        buf.write("\2\177\u0081\5\66\34\2\u0080\u0082\5> \2\u0081\u0080\3")
        buf.write("\2\2\2\u0082\u0083\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\13\3\2\2\2\u0085\u008a\5\66\34\2\u0086")
        buf.write("\u0087\7\5\2\2\u0087\u0088\5.\30\2\u0088\u0089\5> \2\u0089")
        buf.write("\u008b\3\2\2\2\u008a\u0086\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\r\3\2\2")
        buf.write("\2\u008e\u008f\7\6\2\2\u008f\u0090\5.\30\2\u0090\u0091")
        buf.write("\7\6\2\2\u0091\17\3\2\2\2\u0092\u0093\7\7\2\2\u0093\21")
        buf.write("\3\2\2\2\u0094\u0095\7\b\2\2\u0095\u0096\5.\30\2\u0096")
        buf.write("\23\3\2\2\2\u0097\u0098\7\t\2\2\u0098\u0099\5\4\3\2\u0099")
        buf.write("\u009a\7\n\2\2\u009a\25\3\2\2\2\u009b\u009c\7\13\2\2\u009c")
        buf.write("\u009d\5\62\32\2\u009d\u009e\7\t\2\2\u009e\u009f\5\4\3")
        buf.write("\2\u009f\u00a0\7\n\2\2\u00a0\27\3\2\2\2\u00a1\u00a2\7")
        buf.write("\f\2\2\u00a2\u00a3\5\4\3\2\u00a3\u00a4\7\r\2\2\u00a4\u00a5")
        buf.write("\5\62\32\2\u00a5\31\3\2\2\2\u00a6\u00a7\7\16\2\2\u00a7")
        buf.write("\u00a8\5\62\32\2\u00a8\u00a9\7\17\2\2\u00a9\u00b1\5\4")
        buf.write("\3\2\u00aa\u00ab\7\20\2\2\u00ab\u00ac\5\62\32\2\u00ac")
        buf.write("\u00ad\7\17\2\2\u00ad\u00ae\5\4\3\2\u00ae\u00b0\3\2\2")
        buf.write("\2\u00af\u00aa\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b6\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b5\7\21\2\2\u00b5\u00b7\5\4\3")
        buf.write("\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00b9\7\n\2\2\u00b9\33\3\2\2\2\u00ba\u00bb")
        buf.write("\7\22\2\2\u00bb\u00bc\5.\30\2\u00bc\u00bd\7\4\2\2\u00bd")
        buf.write("\u00be\5\62\32\2\u00be\u00bf\7\23\2\2\u00bf\u00c2\5\62")
        buf.write("\32\2\u00c0\u00c1\7\23\2\2\u00c1\u00c3\5\62\32\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c5\7\t\2\2\u00c5\u00c6\5\4\3\2\u00c6\u00c7\7")
        buf.write("\n\2\2\u00c7\35\3\2\2\2\u00c8\u00c9\7\22\2\2\u00c9\u00ca")
        buf.write("\5,\27\2\u00ca\u00cb\7\24\2\2\u00cb\u00cc\5\60\31\2\u00cc")
        buf.write("\u00cd\7\t\2\2\u00cd\u00ce\5\4\3\2\u00ce\u00cf\7\n\2\2")
        buf.write("\u00cf\37\3\2\2\2\u00d0\u00d1\7\25\2\2\u00d1\u00d2\5(")
        buf.write("\25\2\u00d2\u00d3\5B\"\2\u00d3!\3\2\2\2\u00d4\u00d5\7")
        buf.write("\26\2\2\u00d5\u00d6\7\25\2\2\u00d6\u00d7\5.\30\2\u00d7")
        buf.write("\u00d8\5B\"\2\u00d8#\3\2\2\2\u00d9\u00da\7\26\2\2\u00da")
        buf.write("\u00dd\5,\27\2\u00db\u00dc\7\4\2\2\u00dc\u00de\5\60\31")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de%\3\2")
        buf.write("\2\2\u00df\u00e1\7\27\2\2\u00e0\u00e2\5\60\31\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2")
        buf.write("\u00e3\u00e5\7\3\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3")
        buf.write("\2\2\2\u00e5\'\3\2\2\2\u00e6\u00eb\5.\30\2\u00e7\u00e8")
        buf.write("\7\30\2\2\u00e8\u00ea\5.\30\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00f0\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7")
        buf.write("\5\2\2\u00ef\u00f1\5.\30\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1)\3\2\2\2\u00f2\u00f7\58\35\2\u00f3\u00f4")
        buf.write("\7\23\2\2\u00f4\u00f6\58\35\2\u00f5\u00f3\3\2\2\2\u00f6")
        buf.write("\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8+\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00ff\5.\30")
        buf.write("\2\u00fb\u00fc\7\23\2\2\u00fc\u00fe\5.\30\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100-\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u0103\7:\2\2\u0103/\3\2\2\2\u0104\u0109\5\62\32\2\u0105")
        buf.write("\u0106\7\23\2\2\u0106\u0108\5\62\32\2\u0107\u0105\3\2")
        buf.write("\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\61\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d")
        buf.write("\b\32\1\2\u010d\u0121\7\31\2\2\u010e\u0121\7\32\2\2\u010f")
        buf.write("\u0121\7\33\2\2\u0110\u0121\t\2\2\2\u0111\u0121\5X-\2")
        buf.write("\u0112\u0121\7\34\2\2\u0113\u0121\5\n\6\2\u0114\u0121")
        buf.write("\5\f\7\2\u0115\u0121\5@!\2\u0116\u0121\5\64\33\2\u0117")
        buf.write("\u0121\5F$\2\u0118\u0119\7\35\2\2\u0119\u0121\5\62\32")
        buf.write("\22\u011a\u011b\7\36\2\2\u011b\u0121\5\62\32\21\u011c")
        buf.write("\u011d\7\37\2\2\u011d\u0121\5\62\32\20\u011e\u011f\7 ")
        buf.write("\2\2\u011f\u0121\5\62\32\17\u0120\u010c\3\2\2\2\u0120")
        buf.write("\u010e\3\2\2\2\u0120\u010f\3\2\2\2\u0120\u0110\3\2\2\2")
        buf.write("\u0120\u0111\3\2\2\2\u0120\u0112\3\2\2\2\u0120\u0113\3")
        buf.write("\2\2\2\u0120\u0114\3\2\2\2\u0120\u0115\3\2\2\2\u0120\u0116")
        buf.write("\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u0118\3\2\2\2\u0120")
        buf.write("\u011a\3\2\2\2\u0120\u011c\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0121\u014d\3\2\2\2\u0122\u0123\f\16\2\2\u0123\u0124")
        buf.write("\7!\2\2\u0124\u014c\5\62\32\17\u0125\u0126\f\r\2\2\u0126")
        buf.write("\u0127\7\37\2\2\u0127\u014c\5\62\32\16\u0128\u0129\f\f")
        buf.write("\2\2\u0129\u012a\7\"\2\2\u012a\u014c\5\62\32\r\u012b\u012c")
        buf.write("\f\13\2\2\u012c\u012d\7#\2\2\u012d\u014c\5\62\32\f\u012e")
        buf.write("\u012f\f\n\2\2\u012f\u0130\7$\2\2\u0130\u014c\5\62\32")
        buf.write("\13\u0131\u0132\f\t\2\2\u0132\u0133\7%\2\2\u0133\u014c")
        buf.write("\5\62\32\n\u0134\u0135\f\b\2\2\u0135\u0136\7&\2\2\u0136")
        buf.write("\u014c\5\62\32\b\u0137\u0138\f\7\2\2\u0138\u0139\5T+\2")
        buf.write("\u0139\u013a\5\62\32\7\u013a\u014c\3\2\2\2\u013b\u013c")
        buf.write("\f\6\2\2\u013c\u013d\5R*\2\u013d\u013e\5\62\32\7\u013e")
        buf.write("\u014c\3\2\2\2\u013f\u0140\f\5\2\2\u0140\u0141\5P)\2\u0141")
        buf.write("\u0142\5\62\32\6\u0142\u014c\3\2\2\2\u0143\u0144\f\4\2")
        buf.write("\2\u0144\u0145\5N(\2\u0145\u0146\5\62\32\5\u0146\u014c")
        buf.write("\3\2\2\2\u0147\u0148\f\3\2\2\u0148\u0149\5V,\2\u0149\u014a")
        buf.write("\5\62\32\4\u014a\u014c\3\2\2\2\u014b\u0122\3\2\2\2\u014b")
        buf.write("\u0125\3\2\2\2\u014b\u0128\3\2\2\2\u014b\u012b\3\2\2\2")
        buf.write("\u014b\u012e\3\2\2\2\u014b\u0131\3\2\2\2\u014b\u0134\3")
        buf.write("\2\2\2\u014b\u0137\3\2\2\2\u014b\u013b\3\2\2\2\u014b\u013f")
        buf.write("\3\2\2\2\u014b\u0143\3\2\2\2\u014b\u0147\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e\63\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0154\5\66")
        buf.write("\34\2\u0151\u0153\5<\37\2\u0152\u0151\3\2\2\2\u0153\u0156")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155")
        buf.write("\65\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u015d\58\35\2\u0158")
        buf.write("\u0159\7\'\2\2\u0159\u015a\5\62\32\2\u015a\u015b\7(\2")
        buf.write("\2\u015b\u015d\3\2\2\2\u015c\u0157\3\2\2\2\u015c\u0158")
        buf.write("\3\2\2\2\u015d\67\3\2\2\2\u015e\u0165\5.\30\2\u015f\u0160")
        buf.write("\7\'\2\2\u0160\u0161\5\62\32\2\u0161\u0162\7(\2\2\u0162")
        buf.write("\u0163\5:\36\2\u0163\u0165\3\2\2\2\u0164\u015e\3\2\2\2")
        buf.write("\u0164\u015f\3\2\2\2\u0165\u0169\3\2\2\2\u0166\u0168\5")
        buf.write(":\36\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a9\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016c\u016e\5<\37\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0178\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\7")
        buf.write(")\2\2\u0173\u0174\5\62\32\2\u0174\u0175\7*\2\2\u0175\u0179")
        buf.write("\3\2\2\2\u0176\u0177\7\30\2\2\u0177\u0179\5.\30\2\u0178")
        buf.write("\u0172\3\2\2\2\u0178\u0176\3\2\2\2\u0179;\3\2\2\2\u017a")
        buf.write("\u017b\7\5\2\2\u017b\u017d\5.\30\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\5")
        buf.write("> \2\u017f=\3\2\2\2\u0180\u0182\7\'\2\2\u0181\u0183\5")
        buf.write("\60\31\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184\u0188\7(\2\2\u0185\u0188\5F$\2\u0186")
        buf.write("\u0188\5X-\2\u0187\u0180\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188?\3\2\2\2\u0189\u018a\7\25\2\2\u018a")
        buf.write("\u018b\5B\"\2\u018bA\3\2\2\2\u018c\u018e\7\'\2\2\u018d")
        buf.write("\u018f\5D#\2\u018e\u018d\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u0191\7(\2\2\u0191\u0192\5\4\3\2")
        buf.write("\u0192\u0193\7\n\2\2\u0193C\3\2\2\2\u0194\u0197\5,\27")
        buf.write("\2\u0195\u0196\7\23\2\2\u0196\u0198\7\34\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u019b\7\34\2\2\u019a\u0194\3\2\2\2\u019a\u0199\3\2\2")
        buf.write("\2\u019bE\3\2\2\2\u019c\u019e\7+\2\2\u019d\u019f\5H%\2")
        buf.write("\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0\u01a1\7,\2\2\u01a1G\3\2\2\2\u01a2\u01a8\5")
        buf.write("J&\2\u01a3\u01a4\5L\'\2\u01a4\u01a5\5J&\2\u01a5\u01a7")
        buf.write("\3\2\2\2\u01a6\u01a3\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ad\5L\'\2\u01ac\u01ab\3")
        buf.write("\2\2\2\u01ac\u01ad\3\2\2\2\u01adI\3\2\2\2\u01ae\u01af")
        buf.write("\7)\2\2\u01af\u01b0\5\62\32\2\u01b0\u01b1\7*\2\2\u01b1")
        buf.write("\u01b2\7\4\2\2\u01b2\u01b3\5\62\32\2\u01b3\u01ba\3\2\2")
        buf.write("\2\u01b4\u01b5\5.\30\2\u01b5\u01b6\7\4\2\2\u01b6\u01b7")
        buf.write("\5\62\32\2\u01b7\u01ba\3\2\2\2\u01b8\u01ba\5\62\32\2\u01b9")
        buf.write("\u01ae\3\2\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01b8\3\2\2\2")
        buf.write("\u01baK\3\2\2\2\u01bb\u01bc\t\3\2\2\u01bcM\3\2\2\2\u01bd")
        buf.write("\u01be\7-\2\2\u01beO\3\2\2\2\u01bf\u01c0\7.\2\2\u01c0")
        buf.write("Q\3\2\2\2\u01c1\u01c2\t\4\2\2\u01c2S\3\2\2\2\u01c3\u01c4")
        buf.write("\7\65\2\2\u01c4U\3\2\2\2\u01c5\u01c6\t\5\2\2\u01c6W\3")
        buf.write("\2\2\2\u01c7\u01c8\t\6\2\2\u01c8Y\3\2\2\2\u01c9\u01ca")
        buf.write("\t\7\2\2\u01ca[\3\2\2\2%bfy\u0083\u008c\u00b1\u00b6\u00c2")
        buf.write("\u00dd\u00e1\u00e4\u00eb\u00f0\u00f7\u00ff\u0109\u0120")
        buf.write("\u014b\u014d\u0154\u015c\u0164\u0169\u016f\u0178\u017c")
        buf.write("\u0182\u0187\u018e\u0197\u019a\u019e\u01a8\u01ac\u01b9")
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
                     "'nil'", "'false'", "'true'", "'...'", "'not'", "'#'", 
                     "'-'", "'~'", "'+'", "'*'", "'/'", "'%'", "'//'", "'^'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'or'", "'and'", 
                     "'<'", "'>'", "'<='", "'>='", "'~='", "'=='", "'..'", 
                     "'&'", "'|'", "'<<'", "'>>'" ]

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
    RULE_prefixexp = 25
    RULE_varOrExp = 26
    RULE_var = 27
    RULE_varSuffix = 28
    RULE_nameAndArgs = 29
    RULE_args = 30
    RULE_functiondef = 31
    RULE_funcbody = 32
    RULE_parlist = 33
    RULE_tableconstructor = 34
    RULE_fieldlist = 35
    RULE_field = 36
    RULE_fieldsep = 37
    RULE_operatorOr = 38
    RULE_operatorAnd = 39
    RULE_operatorComparison = 40
    RULE_operatorStrcat = 41
    RULE_operatorBitwise = 42
    RULE_string = 43
    RULE_comment_rule = 44

    ruleNames =  [ "chunk", "block", "stat", "setStat", "call", "invoke", 
                   "label", "breakStat", "goto", "do", "whileStat", "repeat", 
                   "ifStat", "fornum", "forin", "func", "localfunc", "localset", 
                   "retstat", "funcname", "varlist", "namelist", "name", 
                   "explist", "exp", "prefixexp", "varOrExp", "var", "varSuffix", 
                   "nameAndArgs", "args", "functiondef", "funcbody", "parlist", 
                   "tableconstructor", "fieldlist", "field", "fieldsep", 
                   "operatorOr", "operatorAnd", "operatorComparison", "operatorStrcat", 
                   "operatorBitwise", "string", "comment_rule" ]

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
            self.state = 90
            self.block()
            self.state = 91
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
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__0) | (1 << LuaParser.T__3) | (1 << LuaParser.T__4) | (1 << LuaParser.T__5) | (1 << LuaParser.T__6) | (1 << LuaParser.T__8) | (1 << LuaParser.T__9) | (1 << LuaParser.T__11) | (1 << LuaParser.T__15) | (1 << LuaParser.T__18) | (1 << LuaParser.T__19) | (1 << LuaParser.T__36) | (1 << LuaParser.NAME))) != 0) or _la==LuaParser.COMMENT or _la==LuaParser.LINE_COMMENT:
                self.state = 93
                self.stat()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__20:
                self.state = 99
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(LuaParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.comment_rule()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.setStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.invoke()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.label()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.breakStat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.goto()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 110
                self.do()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 111
                self.whileStat()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 112
                self.repeat()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 113
                self.ifStat()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 114
                self.fornum()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 115
                self.forin()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 116
                self.func()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 117
                self.localfunc()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 118
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
            self.state = 121
            self.varlist()
            self.state = 122
            self.match(LuaParser.T__1)
            self.state = 123
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
            self.state = 125
            self.varOrExp()
            self.state = 127 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 126
                    self.args()

                else:
                    raise NoViableAltException(self)
                self.state = 129 
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
            self.state = 131
            self.varOrExp()
            self.state = 136 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 132
                    self.match(LuaParser.T__2)
                    self.state = 133
                    self.name()
                    self.state = 134
                    self.args()

                else:
                    raise NoViableAltException(self)
                self.state = 138 
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
            self.state = 140
            self.match(LuaParser.T__3)
            self.state = 141
            self.name()
            self.state = 142
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
            self.state = 144
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
            self.state = 146
            self.match(LuaParser.T__5)
            self.state = 147
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
            self.state = 149
            self.match(LuaParser.T__6)
            self.state = 150
            self.block()
            self.state = 151
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
            self.state = 153
            self.match(LuaParser.T__8)
            self.state = 154
            self.exp(0)
            self.state = 155
            self.match(LuaParser.T__6)
            self.state = 156
            self.block()
            self.state = 157
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
            self.state = 159
            self.match(LuaParser.T__9)
            self.state = 160
            self.block()
            self.state = 161
            self.match(LuaParser.T__10)
            self.state = 162
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
            self.state = 164
            self.match(LuaParser.T__11)
            self.state = 165
            self.exp(0)
            self.state = 166
            self.match(LuaParser.T__12)
            self.state = 167
            self.block()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__13:
                self.state = 168
                self.match(LuaParser.T__13)
                self.state = 169
                self.exp(0)
                self.state = 170
                self.match(LuaParser.T__12)
                self.state = 171
                self.block()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__14:
                self.state = 178
                self.match(LuaParser.T__14)
                self.state = 179
                self.block()


            self.state = 182
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
            self.state = 184
            self.match(LuaParser.T__15)
            self.state = 185
            self.name()
            self.state = 186
            self.match(LuaParser.T__1)
            self.state = 187
            self.exp(0)
            self.state = 188
            self.match(LuaParser.T__16)
            self.state = 189
            self.exp(0)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__16:
                self.state = 190
                self.match(LuaParser.T__16)
                self.state = 191
                self.exp(0)


            self.state = 194
            self.match(LuaParser.T__6)
            self.state = 195
            self.block()
            self.state = 196
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
            self.state = 198
            self.match(LuaParser.T__15)
            self.state = 199
            self.namelist()
            self.state = 200
            self.match(LuaParser.T__17)
            self.state = 201
            self.explist()
            self.state = 202
            self.match(LuaParser.T__6)
            self.state = 203
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
            self.state = 206
            self.match(LuaParser.T__18)
            self.state = 207
            self.funcname()
            self.state = 208
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
            self.state = 210
            self.match(LuaParser.T__19)
            self.state = 211
            self.match(LuaParser.T__18)
            self.state = 212
            self.name()
            self.state = 213
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
            self.state = 215
            self.match(LuaParser.T__19)
            self.state = 216
            self.namelist()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__1:
                self.state = 217
                self.match(LuaParser.T__1)
                self.state = 218
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
            self.state = 221
            self.match(LuaParser.T__20)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__18) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__27) | (1 << LuaParser.T__28) | (1 << LuaParser.T__29) | (1 << LuaParser.T__36) | (1 << LuaParser.T__40) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                self.state = 222
                self.explist()


            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__0:
                self.state = 225
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
            self.state = 228
            self.name()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__21:
                self.state = 229
                self.match(LuaParser.T__21)
                self.state = 230
                self.name()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__2:
                self.state = 236
                self.match(LuaParser.T__2)
                self.state = 237
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
            self.state = 240
            self.var()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__16:
                self.state = 241
                self.match(LuaParser.T__16)
                self.state = 242
                self.var()
                self.state = 247
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
            self.state = 248
            self.name()
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 249
                    self.match(LuaParser.T__16)
                    self.state = 250
                    self.name() 
                self.state = 255
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
            self.state = 256
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
            self.state = 258
            self.exp(0)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LuaParser.T__16:
                self.state = 259
                self.match(LuaParser.T__16)
                self.state = 260
                self.exp(0)
                self.state = 265
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


        def getRuleIndex(self):
            return LuaParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Todo_6Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)

        def operatorOr(self):
            return self.getTypedRuleContext(LuaParser.OperatorOrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo_6" ):
                listener.enterTodo_6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo_6" ):
                listener.exitTodo_6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo_6" ):
                return visitor.visitTodo_6(self)
            else:
                return visitor.visitChildren(self)


    class Todo_5Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)

        def operatorAnd(self):
            return self.getTypedRuleContext(LuaParser.OperatorAndContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo_5" ):
                listener.enterTodo_5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo_5" ):
                listener.exitTodo_5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo_5" ):
                return visitor.visitTodo_5(self)
            else:
                return visitor.visitChildren(self)


    class UnOpLengthContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


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


    class Todo_7Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)

        def operatorBitwise(self):
            return self.getTypedRuleContext(LuaParser.OperatorBitwiseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo_7" ):
                listener.enterTodo_7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo_7" ):
                listener.exitTodo_7(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo_7" ):
                return visitor.visitTodo_7(self)
            else:
                return visitor.visitChildren(self)


    class OpExpoContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpExpo" ):
                listener.enterOpExpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpExpo" ):
                listener.exitOpExpo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpExpo" ):
                return visitor.visitOpExpo(self)
            else:
                return visitor.visitChildren(self)


    class Todo_4Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)

        def operatorComparison(self):
            return self.getTypedRuleContext(LuaParser.OperatorComparisonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo_4" ):
                listener.enterTodo_4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo_4" ):
                listener.exitTodo_4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo_4" ):
                return visitor.visitTodo_4(self)
            else:
                return visitor.visitChildren(self)


    class Todo_3Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)

        def operatorStrcat(self):
            return self.getTypedRuleContext(LuaParser.OperatorStrcatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo_3" ):
                listener.enterTodo_3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo_3" ):
                listener.exitTodo_3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo_3" ):
                return visitor.visitTodo_3(self)
            else:
                return visitor.visitChildren(self)


    class OpMultContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMult" ):
                listener.enterOpMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMult" ):
                listener.exitOpMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMult" ):
                return visitor.visitOpMult(self)
            else:
                return visitor.visitChildren(self)


    class UnOpBitNotContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


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


    class OpSubContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpSub" ):
                listener.enterOpSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpSub" ):
                listener.exitOpSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpSub" ):
                return visitor.visitOpSub(self)
            else:
                return visitor.visitChildren(self)


    class NilContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


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


    class OpAddContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAdd" ):
                listener.enterOpAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAdd" ):
                listener.exitOpAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAdd" ):
                return visitor.visitOpAdd(self)
            else:
                return visitor.visitChildren(self)


    class OpFloorDivContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpFloorDiv" ):
                listener.enterOpFloorDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpFloorDiv" ):
                listener.exitOpFloorDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpFloorDiv" ):
                return visitor.visitOpFloorDiv(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LuaParser.INT, 0)
        def HEX(self):
            return self.getToken(LuaParser.HEX, 0)
        def FLOAT(self):
            return self.getToken(LuaParser.FLOAT, 0)
        def HEX_FLOAT(self):
            return self.getToken(LuaParser.HEX_FLOAT, 0)

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


    class UnOpNotContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


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


    class UnOpMinContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(LuaParser.ExpContext,0)


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


    class OpFloatDivContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpFloatDiv" ):
                listener.enterOpFloatDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpFloatDiv" ):
                listener.exitOpFloatDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpFloatDiv" ):
                return visitor.visitOpFloatDiv(self)
            else:
                return visitor.visitChildren(self)


    class Todo6Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prefixexp(self):
            return self.getTypedRuleContext(LuaParser.PrefixexpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo6" ):
                listener.enterTodo6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo6" ):
                listener.exitTodo6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo6" ):
                return visitor.visitTodo6(self)
            else:
                return visitor.visitChildren(self)


    class Todo7Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tableconstructor(self):
            return self.getTypedRuleContext(LuaParser.TableconstructorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo7" ):
                listener.enterTodo7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo7" ):
                listener.exitTodo7(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo7" ):
                return visitor.visitTodo7(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


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


    class OpModContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LuaParser.ExpContext)
            else:
                return self.getTypedRuleContext(LuaParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMod" ):
                listener.enterOpMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMod" ):
                listener.exitOpMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMod" ):
                return visitor.visitOpMod(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


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


    class Todo4Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def invoke(self):
            return self.getTypedRuleContext(LuaParser.InvokeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo4" ):
                listener.enterTodo4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo4" ):
                listener.exitTodo4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo4" ):
                return visitor.visitTodo4(self)
            else:
                return visitor.visitChildren(self)


    class Todo5Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functiondef(self):
            return self.getTypedRuleContext(LuaParser.FunctiondefContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo5" ):
                listener.enterTodo5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo5" ):
                listener.exitTodo5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo5" ):
                return visitor.visitTodo5(self)
            else:
                return visitor.visitChildren(self)


    class Todo2Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo2" ):
                listener.enterTodo2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo2" ):
                listener.exitTodo2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo2" ):
                return visitor.visitTodo2(self)
            else:
                return visitor.visitChildren(self)


    class Todo3Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def call(self):
            return self.getTypedRuleContext(LuaParser.CallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo3" ):
                listener.enterTodo3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo3" ):
                listener.exitTodo3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo3" ):
                return visitor.visitTodo3(self)
            else:
                return visitor.visitChildren(self)


    class Todo1Context(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LuaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(LuaParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo1" ):
                listener.enterTodo1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo1" ):
                listener.exitTodo1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTodo1" ):
                return visitor.visitTodo1(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LuaParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = LuaParser.NilContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 267
                self.match(LuaParser.T__22)
                pass

            elif la_ == 2:
                localctx = LuaParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 268
                self.match(LuaParser.T__23)
                pass

            elif la_ == 3:
                localctx = LuaParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 269
                self.match(LuaParser.T__24)
                pass

            elif la_ == 4:
                localctx = LuaParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 270
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 5:
                localctx = LuaParser.Todo1Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 271
                self.string()
                pass

            elif la_ == 6:
                localctx = LuaParser.Todo2Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 272
                self.match(LuaParser.T__25)
                pass

            elif la_ == 7:
                localctx = LuaParser.Todo3Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 273
                self.call()
                pass

            elif la_ == 8:
                localctx = LuaParser.Todo4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 274
                self.invoke()
                pass

            elif la_ == 9:
                localctx = LuaParser.Todo5Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 275
                self.functiondef()
                pass

            elif la_ == 10:
                localctx = LuaParser.Todo6Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 276
                self.prefixexp()
                pass

            elif la_ == 11:
                localctx = LuaParser.Todo7Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 277
                self.tableconstructor()
                pass

            elif la_ == 12:
                localctx = LuaParser.UnOpNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 278
                self.match(LuaParser.T__26)
                self.state = 279
                self.exp(16)
                pass

            elif la_ == 13:
                localctx = LuaParser.UnOpLengthContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 280
                self.match(LuaParser.T__27)
                self.state = 281
                self.exp(15)
                pass

            elif la_ == 14:
                localctx = LuaParser.UnOpMinContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 282
                self.match(LuaParser.T__28)
                self.state = 283
                self.exp(14)
                pass

            elif la_ == 15:
                localctx = LuaParser.UnOpBitNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 284
                self.match(LuaParser.T__29)
                self.state = 285
                self.exp(13)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 329
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = LuaParser.OpAddContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 288
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 289
                        self.match(LuaParser.T__30)
                        self.state = 290
                        self.exp(13)
                        pass

                    elif la_ == 2:
                        localctx = LuaParser.OpSubContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 291
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 292
                        self.match(LuaParser.T__28)
                        self.state = 293
                        self.exp(12)
                        pass

                    elif la_ == 3:
                        localctx = LuaParser.OpMultContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 294
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 295
                        self.match(LuaParser.T__31)
                        self.state = 296
                        self.exp(11)
                        pass

                    elif la_ == 4:
                        localctx = LuaParser.OpFloatDivContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 297
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 298
                        self.match(LuaParser.T__32)
                        self.state = 299
                        self.exp(10)
                        pass

                    elif la_ == 5:
                        localctx = LuaParser.OpFloorDivContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 300
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 301
                        self.match(LuaParser.T__33)
                        self.state = 302
                        self.exp(9)
                        pass

                    elif la_ == 6:
                        localctx = LuaParser.OpModContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 303
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 304
                        self.match(LuaParser.T__34)
                        self.state = 305
                        self.exp(8)
                        pass

                    elif la_ == 7:
                        localctx = LuaParser.OpExpoContext(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 306
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 307
                        self.match(LuaParser.T__35)
                        self.state = 308
                        self.exp(6)
                        pass

                    elif la_ == 8:
                        localctx = LuaParser.Todo_3Context(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 309
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 310
                        self.operatorStrcat()
                        self.state = 311
                        self.exp(5)
                        pass

                    elif la_ == 9:
                        localctx = LuaParser.Todo_4Context(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 313
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 314
                        self.operatorComparison()
                        self.state = 315
                        self.exp(5)
                        pass

                    elif la_ == 10:
                        localctx = LuaParser.Todo_5Context(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 317
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 318
                        self.operatorAnd()
                        self.state = 319
                        self.exp(4)
                        pass

                    elif la_ == 11:
                        localctx = LuaParser.Todo_6Context(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 321
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 322
                        self.operatorOr()
                        self.state = 323
                        self.exp(3)
                        pass

                    elif la_ == 12:
                        localctx = LuaParser.Todo_7Context(self, LuaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 325
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 326
                        self.operatorBitwise()
                        self.state = 327
                        self.exp(2)
                        pass

             
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 50, self.RULE_prefixexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.varOrExp()
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 335
                    self.nameAndArgs() 
                self.state = 340
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
        self.enterRule(localctx, 52, self.RULE_varOrExp)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(LuaParser.T__36)
                self.state = 343
                self.exp(0)
                self.state = 344
                self.match(LuaParser.T__37)
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
        self.enterRule(localctx, 54, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.NAME]:
                self.state = 348
                self.name()
                pass
            elif token in [LuaParser.T__36]:
                self.state = 349
                self.match(LuaParser.T__36)
                self.state = 350
                self.exp(0)
                self.state = 351
                self.match(LuaParser.T__37)
                self.state = 352
                self.varSuffix()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 356
                    self.varSuffix() 
                self.state = 361
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
        self.enterRule(localctx, 56, self.RULE_varSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__2) | (1 << LuaParser.T__36) | (1 << LuaParser.T__40) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING))) != 0):
                self.state = 362
                self.nameAndArgs()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.T__38]:
                self.state = 368
                self.match(LuaParser.T__38)
                self.state = 369
                self.exp(0)
                self.state = 370
                self.match(LuaParser.T__39)
                pass
            elif token in [LuaParser.T__21]:
                self.state = 372
                self.match(LuaParser.T__21)
                self.state = 373
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
        self.enterRule(localctx, 58, self.RULE_nameAndArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__2:
                self.state = 376
                self.match(LuaParser.T__2)
                self.state = 377
                self.name()


            self.state = 380
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
        self.enterRule(localctx, 60, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.T__36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(LuaParser.T__36)
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__18) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__27) | (1 << LuaParser.T__28) | (1 << LuaParser.T__29) | (1 << LuaParser.T__36) | (1 << LuaParser.T__40) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                    self.state = 383
                    self.explist()


                self.state = 386
                self.match(LuaParser.T__37)
                pass
            elif token in [LuaParser.T__40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.tableconstructor()
                pass
            elif token in [LuaParser.NORMALSTRING, LuaParser.CHARSTRING, LuaParser.LONGSTRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
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
        self.enterRule(localctx, 62, self.RULE_functiondef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(LuaParser.T__18)
            self.state = 392
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
        self.enterRule(localctx, 64, self.RULE_funcbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(LuaParser.T__36)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__25 or _la==LuaParser.NAME:
                self.state = 395
                self.parlist()


            self.state = 398
            self.match(LuaParser.T__37)
            self.state = 399
            self.block()
            self.state = 400
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
        self.enterRule(localctx, 66, self.RULE_parlist)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LuaParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.namelist()
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LuaParser.T__16:
                    self.state = 403
                    self.match(LuaParser.T__16)
                    self.state = 404
                    self.match(LuaParser.T__25)


                pass
            elif token in [LuaParser.T__25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(LuaParser.T__25)
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
        self.enterRule(localctx, 68, self.RULE_tableconstructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(LuaParser.T__40)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__18) | (1 << LuaParser.T__22) | (1 << LuaParser.T__23) | (1 << LuaParser.T__24) | (1 << LuaParser.T__25) | (1 << LuaParser.T__26) | (1 << LuaParser.T__27) | (1 << LuaParser.T__28) | (1 << LuaParser.T__29) | (1 << LuaParser.T__36) | (1 << LuaParser.T__38) | (1 << LuaParser.T__40) | (1 << LuaParser.NAME) | (1 << LuaParser.NORMALSTRING) | (1 << LuaParser.CHARSTRING) | (1 << LuaParser.LONGSTRING) | (1 << LuaParser.INT) | (1 << LuaParser.HEX) | (1 << LuaParser.FLOAT) | (1 << LuaParser.HEX_FLOAT))) != 0):
                self.state = 411
                self.fieldlist()


            self.state = 414
            self.match(LuaParser.T__41)
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
        self.enterRule(localctx, 70, self.RULE_fieldlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.field()
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 417
                    self.fieldsep()
                    self.state = 418
                    self.field() 
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LuaParser.T__0 or _la==LuaParser.T__16:
                self.state = 425
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
        self.enterRule(localctx, 72, self.RULE_field)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(LuaParser.T__38)
                self.state = 429
                self.exp(0)
                self.state = 430
                self.match(LuaParser.T__39)
                self.state = 431
                self.match(LuaParser.T__1)
                self.state = 432
                self.exp(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.name()
                self.state = 435
                self.match(LuaParser.T__1)
                self.state = 436
                self.exp(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 438
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
        self.enterRule(localctx, 74, self.RULE_fieldsep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
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
        self.enterRule(localctx, 76, self.RULE_operatorOr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(LuaParser.T__42)
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
        self.enterRule(localctx, 78, self.RULE_operatorAnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(LuaParser.T__43)
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
        self.enterRule(localctx, 80, self.RULE_operatorComparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__44) | (1 << LuaParser.T__45) | (1 << LuaParser.T__46) | (1 << LuaParser.T__47) | (1 << LuaParser.T__48) | (1 << LuaParser.T__49))) != 0)):
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
        self.enterRule(localctx, 82, self.RULE_operatorStrcat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(LuaParser.T__50)
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
        self.enterRule(localctx, 84, self.RULE_operatorBitwise)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LuaParser.T__29) | (1 << LuaParser.T__51) | (1 << LuaParser.T__52) | (1 << LuaParser.T__53) | (1 << LuaParser.T__54))) != 0)):
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
        self.enterRule(localctx, 86, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
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
        self.enterRule(localctx, 88, self.RULE_comment_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
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
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         




