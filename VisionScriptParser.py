# Generated from VisionScript.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from Compiler import Compiler
from VirtualMachine import VirtualMachine
compiler = Compiler()
vm = VirtualMachine()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01ab\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3M\n\3\f\3\16\3P\13\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5a\n\5\3\6")
        buf.write("\3\6\5\6e\n\6\3\7\3\7\3\7\3\7\5\7k\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\7\13\u008f\n\13\f\13\16\13\u0092")
        buf.write("\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00a1\n\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00ae\n\16\3\16\3\16\3\16\7\16\u00b3")
        buf.write("\n\16\f\16\16\16\u00b6\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00be\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00c8\n\21\3\21\3\21\3\21\7\21\u00cd\n\21")
        buf.write("\f\21\16\21\u00d0\13\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00d8\n\22\3\22\3\22\3\22\7\22\u00dd\n\22\f\22\16")
        buf.write("\22\u00e0\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00eb\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0104\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u010b\n\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u0120\n\26\f\26\16\26\u0123")
        buf.write("\13\26\5\26\u0125\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u0136")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u0141\n\30\f\30\16\30\u0144\13\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0151\n\31\f")
        buf.write("\31\16\31\u0154\13\31\5\31\u0156\n\31\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0163\n\32")
        buf.write("\f\32\16\32\u0166\13\32\5\32\u0168\n\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0175\n")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0181\n\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0189")
        buf.write("\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0199\n\34\3\35\3\35\3\35\5")
        buf.write("\35\u019e\n\35\3\35\3\35\3\35\3\35\5\35\u01a4\n\35\3\35")
        buf.write("\6\35\u01a7\n\35\r\35\16\35\u01a8\3\35\2\2\36\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write("\2\3\4\2\27\30\60\63\2\u01ce\2:\3\2\2\2\4N\3\2\2\2\6Q")
        buf.write("\3\2\2\2\b`\3\2\2\2\nd\3\2\2\2\fj\3\2\2\2\16l\3\2\2\2")
        buf.write("\20r\3\2\2\2\22}\3\2\2\2\24\u0090\3\2\2\2\26\u0093\3\2")
        buf.write("\2\2\30\u00a0\3\2\2\2\32\u00a7\3\2\2\2\34\u00b7\3\2\2")
        buf.write("\2\36\u00bf\3\2\2\2 \u00c1\3\2\2\2\"\u00d1\3\2\2\2$\u00ea")
        buf.write("\3\2\2\2&\u0103\3\2\2\2(\u0105\3\2\2\2*\u010e\3\2\2\2")
        buf.write(",\u0135\3\2\2\2.\u0142\3\2\2\2\60\u0145\3\2\2\2\62\u015a")
        buf.write("\3\2\2\2\64\u016c\3\2\2\2\66\u0182\3\2\2\28\u019d\3\2")
        buf.write("\2\2:;\b\2\1\2;<\5\4\3\2<=\7\2\2\3=>\b\2\1\2>?\b\2\1\2")
        buf.write("?@\b\2\1\2@A\b\2\1\2AB\b\2\1\2B\3\3\2\2\2CM\5\6\4\2DM")
        buf.write("\5\20\t\2EM\5\22\n\2FM\5\26\f\2GM\5\30\r\2HM\5*\26\2I")
        buf.write("M\5\60\31\2JM\5\16\b\2KM\5\66\34\2LC\3\2\2\2LD\3\2\2\2")
        buf.write("LE\3\2\2\2LF\3\2\2\2LG\3\2\2\2LH\3\2\2\2LI\3\2\2\2LJ\3")
        buf.write("\2\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\5\3\2")
        buf.write("\2\2PN\3\2\2\2QR\5\b\5\2RS\7)\2\2ST\7\3\2\2TU\5\n\6\2")
        buf.write("UV\b\4\1\2VW\b\4\1\2W\7\3\2\2\2XY\7\20\2\2Ya\b\5\1\2Z")
        buf.write("[\7\21\2\2[a\b\5\1\2\\]\7\22\2\2]a\b\5\1\2^_\7\31\2\2")
        buf.write("_a\b\5\1\2`X\3\2\2\2`Z\3\2\2\2`\\\3\2\2\2`^\3\2\2\2a\t")
        buf.write("\3\2\2\2be\5\f\7\2ce\5\60\31\2db\3\2\2\2dc\3\2\2\2e\13")
        buf.write("\3\2\2\2fk\5\32\16\2gk\58\35\2hk\5\62\32\2ik\5\64\33\2")
        buf.write("jf\3\2\2\2jg\3\2\2\2jh\3\2\2\2ji\3\2\2\2k\r\3\2\2\2lm")
        buf.write("\7)\2\2mn\7\3\2\2no\5\n\6\2op\b\b\1\2pq\b\b\1\2q\17\3")
        buf.write("\2\2\2rs\7\16\2\2st\5\32\16\2tu\b\t\1\2uv\7\32\2\2vw\5")
        buf.write("\24\13\2wx\7\17\2\2xy\b\t\1\2yz\5\24\13\2z{\7\33\2\2{")
        buf.write("|\b\t\1\2|\21\3\2\2\2}~\7\34\2\2~\177\7\36\2\2\177\u0080")
        buf.write("\b\n\1\2\u0080\u0081\5\32\16\2\u0081\u0082\b\n\1\2\u0082")
        buf.write("\u0083\7\32\2\2\u0083\u0084\5\24\13\2\u0084\u0085\7\33")
        buf.write("\2\2\u0085\u0086\b\n\1\2\u0086\23\3\2\2\2\u0087\u008f")
        buf.write("\5\20\t\2\u0088\u008f\5\22\n\2\u0089\u008f\5\26\f\2\u008a")
        buf.write("\u008f\5\30\r\2\u008b\u008f\5\16\b\2\u008c\u008f\5\66")
        buf.write("\34\2\u008d\u008f\5(\25\2\u008e\u0087\3\2\2\2\u008e\u0088")
        buf.write("\3\2\2\2\u008e\u0089\3\2\2\2\u008e\u008a\3\2\2\2\u008e")
        buf.write("\u008b\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3")
        buf.write("\2\2\2\u0091\25\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094")
        buf.write("\7\n\2\2\u0094\u0095\7\4\2\2\u0095\u0096\7)\2\2\u0096")
        buf.write("\u0097\b\f\1\2\u0097\u0098\7\5\2\2\u0098\u0099\b\f\1\2")
        buf.write("\u0099\27\3\2\2\2\u009a\u009b\7\r\2\2\u009b\u00a1\b\r")
        buf.write("\1\2\u009c\u009d\7\13\2\2\u009d\u00a1\b\r\1\2\u009e\u009f")
        buf.write("\7\f\2\2\u009f\u00a1\b\r\1\2\u00a0\u009a\3\2\2\2\u00a0")
        buf.write("\u009c\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a3\7\4\2\2\u00a3\u00a4\5\n\6\2\u00a4\u00a5\7")
        buf.write("\5\2\2\u00a5\u00a6\b\r\1\2\u00a6\31\3\2\2\2\u00a7\u00a8")
        buf.write("\5\34\17\2\u00a8\u00b4\b\16\1\2\u00a9\u00aa\7\25\2\2\u00aa")
        buf.write("\u00ae\b\16\1\2\u00ab\u00ac\7\26\2\2\u00ac\u00ae\b\16")
        buf.write("\1\2\u00ad\u00a9\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b0\5\34\17\2\u00b0\u00b1\b\16\1\2\u00b1")
        buf.write("\u00b3\3\2\2\2\u00b2\u00ad\3\2\2\2\u00b3\u00b6\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\33\3\2")
        buf.write("\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00bd\5 \21\2\u00b8\u00b9")
        buf.write("\5\36\20\2\u00b9\u00ba\b\17\1\2\u00ba\u00bb\5 \21\2\u00bb")
        buf.write("\u00bc\b\17\1\2\u00bc\u00be\3\2\2\2\u00bd\u00b8\3\2\2")
        buf.write("\2\u00bd\u00be\3\2\2\2\u00be\35\3\2\2\2\u00bf\u00c0\t")
        buf.write("\2\2\2\u00c0\37\3\2\2\2\u00c1\u00c2\5\"\22\2\u00c2\u00ce")
        buf.write("\b\21\1\2\u00c3\u00c4\7,\2\2\u00c4\u00c8\b\21\1\2\u00c5")
        buf.write("\u00c6\7-\2\2\u00c6\u00c8\b\21\1\2\u00c7\u00c3\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\5")
        buf.write("\"\22\2\u00ca\u00cb\b\21\1\2\u00cb\u00cd\3\2\2\2\u00cc")
        buf.write("\u00c7\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf!\3\2\2\2\u00d0\u00ce\3\2\2")
        buf.write("\2\u00d1\u00d2\5$\23\2\u00d2\u00de\b\22\1\2\u00d3\u00d4")
        buf.write("\7/\2\2\u00d4\u00d8\b\22\1\2\u00d5\u00d6\7.\2\2\u00d6")
        buf.write("\u00d8\b\22\1\2\u00d7\u00d3\3\2\2\2\u00d7\u00d5\3\2\2")
        buf.write("\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\5$\23\2\u00da\u00db")
        buf.write("\b\22\1\2\u00db\u00dd\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df#\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\7\4\2")
        buf.write("\2\u00e2\u00e3\b\23\1\2\u00e3\u00e4\5\32\16\2\u00e4\u00e5")
        buf.write("\7\5\2\2\u00e5\u00e6\b\23\1\2\u00e6\u00eb\3\2\2\2\u00e7")
        buf.write("\u00e8\5&\24\2\u00e8\u00e9\b\23\1\2\u00e9\u00eb\3\2\2")
        buf.write("\2\u00ea\u00e1\3\2\2\2\u00ea\u00e7\3\2\2\2\u00eb%\3\2")
        buf.write("\2\2\u00ec\u00ed\7-\2\2\u00ed\u00ee\7*\2\2\u00ee\u00ef")
        buf.write("\b\24\1\2\u00ef\u0104\b\24\1\2\u00f0\u00f1\7*\2\2\u00f1")
        buf.write("\u00f2\b\24\1\2\u00f2\u0104\b\24\1\2\u00f3\u00f4\7\23")
        buf.write("\2\2\u00f4\u00f5\b\24\1\2\u00f5\u0104\b\24\1\2\u00f6\u00f7")
        buf.write("\7\24\2\2\u00f7\u00f8\b\24\1\2\u00f8\u0104\b\24\1\2\u00f9")
        buf.write("\u00fa\7+\2\2\u00fa\u00fb\b\24\1\2\u00fb\u0104\b\24\1")
        buf.write("\2\u00fc\u00fd\7)\2\2\u00fd\u00fe\b\24\1\2\u00fe\u0104")
        buf.write("\b\24\1\2\u00ff\u0100\5\60\31\2\u0100\u0101\b\24\1\2\u0101")
        buf.write("\u0102\b\24\1\2\u0102\u0104\3\2\2\2\u0103\u00ec\3\2\2")
        buf.write("\2\u0103\u00f0\3\2\2\2\u0103\u00f3\3\2\2\2\u0103\u00f6")
        buf.write("\3\2\2\2\u0103\u00f9\3\2\2\2\u0103\u00fc\3\2\2\2\u0103")
        buf.write("\u00ff\3\2\2\2\u0104\'\3\2\2\2\u0105\u0106\7 \2\2\u0106")
        buf.write("\u010a\7\4\2\2\u0107\u0108\5\n\6\2\u0108\u0109\b\25\1")
        buf.write("\2\u0109\u010b\3\2\2\2\u010a\u0107\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\7\5\2\2\u010d")
        buf.write(")\3\2\2\2\u010e\u010f\5,\27\2\u010f\u0110\7\37\2\2\u0110")
        buf.write("\u0111\7)\2\2\u0111\u0112\b\26\1\2\u0112\u0113\b\26\1")
        buf.write("\2\u0113\u0114\b\26\1\2\u0114\u0124\7\4\2\2\u0115\u0116")
        buf.write("\5\b\5\2\u0116\u0117\7)\2\2\u0117\u0118\b\26\1\2\u0118")
        buf.write("\u0121\b\26\1\2\u0119\u011a\7\6\2\2\u011a\u011b\5\b\5")
        buf.write("\2\u011b\u011c\7)\2\2\u011c\u011d\b\26\1\2\u011d\u011e")
        buf.write("\b\26\1\2\u011e\u0120\3\2\2\2\u011f\u0119\3\2\2\2\u0120")
        buf.write("\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0115\3")
        buf.write("\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127")
        buf.write("\7\5\2\2\u0127\u0128\7\32\2\2\u0128\u0129\5.\30\2\u0129")
        buf.write("\u012a\7\33\2\2\u012a\u012b\b\26\1\2\u012b\u012c\b\26")
        buf.write("\1\2\u012c\u012d\b\26\1\2\u012d\u012e\b\26\1\2\u012e\u012f")
        buf.write("\b\26\1\2\u012f+\3\2\2\2\u0130\u0131\5\b\5\2\u0131\u0132")
        buf.write("\b\27\1\2\u0132\u0136\3\2\2\2\u0133\u0134\7\'\2\2\u0134")
        buf.write("\u0136\b\27\1\2\u0135\u0130\3\2\2\2\u0135\u0133\3\2\2")
        buf.write("\2\u0136-\3\2\2\2\u0137\u0141\5\6\4\2\u0138\u0141\5\20")
        buf.write("\t\2\u0139\u0141\5\22\n\2\u013a\u0141\5\26\f\2\u013b\u0141")
        buf.write("\5\30\r\2\u013c\u0141\5\16\b\2\u013d\u0141\5\66\34\2\u013e")
        buf.write("\u0141\5\60\31\2\u013f\u0141\5(\25\2\u0140\u0137\3\2\2")
        buf.write("\2\u0140\u0138\3\2\2\2\u0140\u0139\3\2\2\2\u0140\u013a")
        buf.write("\3\2\2\2\u0140\u013b\3\2\2\2\u0140\u013c\3\2\2\2\u0140")
        buf.write("\u013d\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2")
        buf.write("\u0141\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3")
        buf.write("\2\2\2\u0143/\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146")
        buf.write("\7)\2\2\u0146\u0147\b\31\1\2\u0147\u0148\b\31\1\2\u0148")
        buf.write("\u0149\b\31\1\2\u0149\u0155\7\4\2\2\u014a\u014b\5\f\7")
        buf.write("\2\u014b\u0152\b\31\1\2\u014c\u014d\7\6\2\2\u014d\u014e")
        buf.write("\5\f\7\2\u014e\u014f\b\31\1\2\u014f\u0151\3\2\2\2\u0150")
        buf.write("\u014c\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3")
        buf.write("\2\2\2\u0155\u014a\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\7\5\2\2\u0158\u0159\b\31\1\2\u0159")
        buf.write("\61\3\2\2\2\u015a\u015b\7\7\2\2\u015b\u0167\b\32\1\2\u015c")
        buf.write("\u015d\5\32\16\2\u015d\u0164\b\32\1\2\u015e\u015f\7\6")
        buf.write("\2\2\u015f\u0160\5\32\16\2\u0160\u0161\b\32\1\2\u0161")
        buf.write("\u0163\3\2\2\2\u0162\u015e\3\2\2\2\u0163\u0166\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0168\3")
        buf.write("\2\2\2\u0166\u0164\3\2\2\2\u0167\u015c\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\7\b\2\2\u016a")
        buf.write("\u016b\b\32\1\2\u016b\63\3\2\2\2\u016c\u016d\7)\2\2\u016d")
        buf.write("\u0180\7\t\2\2\u016e\u016f\7!\2\2\u016f\u0175\b\33\1\2")
        buf.write("\u0170\u0171\7\"\2\2\u0171\u0175\b\33\1\2\u0172\u0173")
        buf.write("\7(\2\2\u0173\u0175\b\33\1\2\u0174\u016e\3\2\2\2\u0174")
        buf.write("\u0170\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\7\4\2\2\u0177\u0178\7\5\2\2\u0178\u0181\b")
        buf.write("\33\1\2\u0179\u017a\7#\2\2\u017a\u017b\b\33\1\2\u017b")
        buf.write("\u017c\7\4\2\2\u017c\u017d\5\32\16\2\u017d\u017e\7\5\2")
        buf.write("\2\u017e\u017f\b\33\1\2\u017f\u0181\3\2\2\2\u0180\u0174")
        buf.write("\3\2\2\2\u0180\u0179\3\2\2\2\u0181\65\3\2\2\2\u0182\u0183")
        buf.write("\7)\2\2\u0183\u0198\7\t\2\2\u0184\u0185\7$\2\2\u0185\u0189")
        buf.write("\b\34\1\2\u0186\u0187\7%\2\2\u0187\u0189\b\34\1\2\u0188")
        buf.write("\u0184\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u018b\7\4\2\2\u018b\u018c\5\32\16\2\u018c\u018d")
        buf.write("\7\5\2\2\u018d\u018e\b\34\1\2\u018e\u0199\3\2\2\2\u018f")
        buf.write("\u0190\7&\2\2\u0190\u0191\b\34\1\2\u0191\u0192\7\4\2\2")
        buf.write("\u0192\u0193\5\32\16\2\u0193\u0194\7\6\2\2\u0194\u0195")
        buf.write("\5\32\16\2\u0195\u0196\7\5\2\2\u0196\u0197\b\34\1\2\u0197")
        buf.write("\u0199\3\2\2\2\u0198\u0188\3\2\2\2\u0198\u018f\3\2\2\2")
        buf.write("\u0199\67\3\2\2\2\u019a\u019b\7)\2\2\u019b\u019e\b\35")
        buf.write("\1\2\u019c\u019e\5\62\32\2\u019d\u019a\3\2\2\2\u019d\u019c")
        buf.write("\3\2\2\2\u019e\u01a6\3\2\2\2\u019f\u01a3\7,\2\2\u01a0")
        buf.write("\u01a1\7)\2\2\u01a1\u01a4\b\35\1\2\u01a2\u01a4\5\62\32")
        buf.write("\2\u01a3\u01a0\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a7\b\35\1\2\u01a6\u019f\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a99\3\2\2\2$LN`dj\u008e\u0090\u00a0\u00ad\u00b4\u00bd")
        buf.write("\u00c7\u00ce\u00d7\u00de\u00ea\u0103\u010a\u0121\u0124")
        buf.write("\u0135\u0140\u0142\u0152\u0155\u0164\u0167\u0174\u0180")
        buf.write("\u0188\u0198\u019d\u01a3\u01a8")
        return buf.getvalue()


class VisionScriptParser ( Parser ):

    grammarFileName = "VisionScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','", "'['", "']'", 
                     "'.'", "'read'", "'print'", "'hear'", "'braille'", 
                     "'if'", "'else'", "'number'", "'text'", "'bool'", "'False'", 
                     "'True'", "'and'", "'or'", "'equal'", "'not_equal'", 
                     "'container'", "'begin'", "'end'", "'repeat'", "'times'", 
                     "'until'", "'function'", "'return'", "'get_back'", 
                     "'get_front'", "'get'", "'insert_back'", "'insert_front'", 
                     "'insert'", "'void'", "'length'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'/'", "'*'", "'>'", "'>='", 
                     "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "READ", "PRINT", "HEAR", "BRAILLE", "IF", "ELSE", 
                      "NUMBER", "TEXT", "BOOL", "CTBF", "CTBT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL", "CONTAINER", "BEGIN", "END", 
                      "REPEAT", "TIMES", "UNTIL", "FUNCTION", "RETURN", 
                      "GET_BACK", "GET_FRONT", "GET", "INSERT_BACK", "INSERT_FRONT", 
                      "INSERT", "VOID", "LENGTH", "ID", "CTN", "CTT", "PLUS", 
                      "MINUS", "DIVISION", "MULTIPLICATION", "GREATER", 
                      "GREATER_EQUAL", "LESS", "LESS_EQUAL", "WHITESPACE", 
                      "NEWLINE" ]

    RULE_visionscript = 0
    RULE_programa = 1
    RULE_variable = 2
    RULE_tipo = 3
    RULE_todo = 4
    RULE_casi_todo = 5
    RULE_asignacion = 6
    RULE_condicion = 7
    RULE_ciclo = 8
    RULE_bloque = 9
    RULE_read = 10
    RULE_imprimir = 11
    RULE_mega_expresion = 12
    RULE_expresion = 13
    RULE_exp_todo = 14
    RULE_exp = 15
    RULE_termino = 16
    RULE_factor = 17
    RULE_ct = 18
    RULE_retorno = 19
    RULE_function = 20
    RULE_function_type = 21
    RULE_func_bloque = 22
    RULE_function_call = 23
    RULE_contenedor = 24
    RULE_op_contenedor_returns = 25
    RULE_op_contenedor = 26
    RULE_concat_contenedor = 27

    ruleNames =  [ "visionscript", "programa", "variable", "tipo", "todo", 
                   "casi_todo", "asignacion", "condicion", "ciclo", "bloque", 
                   "read", "imprimir", "mega_expresion", "expresion", "exp_todo", 
                   "exp", "termino", "factor", "ct", "retorno", "function", 
                   "function_type", "func_bloque", "function_call", "contenedor", 
                   "op_contenedor_returns", "op_contenedor", "concat_contenedor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    READ=8
    PRINT=9
    HEAR=10
    BRAILLE=11
    IF=12
    ELSE=13
    NUMBER=14
    TEXT=15
    BOOL=16
    CTBF=17
    CTBT=18
    AND=19
    OR=20
    EQUAL=21
    NOT_EQUAL=22
    CONTAINER=23
    BEGIN=24
    END=25
    REPEAT=26
    TIMES=27
    UNTIL=28
    FUNCTION=29
    RETURN=30
    GET_BACK=31
    GET_FRONT=32
    GET=33
    INSERT_BACK=34
    INSERT_FRONT=35
    INSERT=36
    VOID=37
    LENGTH=38
    ID=39
    CTN=40
    CTT=41
    PLUS=42
    MINUS=43
    DIVISION=44
    MULTIPLICATION=45
    GREATER=46
    GREATER_EQUAL=47
    LESS=48
    LESS_EQUAL=49
    WHITESPACE=50
    NEWLINE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class VisionscriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programa(self):
            return self.getTypedRuleContext(VisionScriptParser.ProgramaContext,0)


        def EOF(self):
            return self.getToken(VisionScriptParser.EOF, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_visionscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisionscript" ):
                listener.enterVisionscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisionscript" ):
                listener.exitVisionscript(self)




    def visionscript(self):

        localctx = VisionScriptParser.VisionscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_visionscript)
        try:
            self.enterOuterAlt(localctx, 1)
            compiler.FuncDeclaration('@global','void')
            self.state = 57
            self.programa()
            self.state = 58
            self.match(VisionScriptParser.EOF)
            compiler.printCuad()
            compiler.showFunctionDirectory()
            vm.Cuadruplos = compiler.ReturnCuads()
            vm.FillMemoryArrays(compiler.returnGlobalCont(),compiler.returnConstTable())
            vm.run()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.VariableContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.VariableContext,i)


        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.CondicionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.CondicionContext,i)


        def ciclo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.CicloContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.CicloContext,i)


        def read(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ReadContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ReadContext,i)


        def imprimir(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ImprimirContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ImprimirContext,i)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.FunctionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.FunctionContext,i)


        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Function_callContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Function_callContext,i)


        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.AsignacionContext,i)


        def op_contenedor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Op_contenedorContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Op_contenedorContext,i)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = VisionScriptParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.VOID) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 74
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 65
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 66
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 67
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 68
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 69
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 70
                    self.function()
                    pass

                elif la_ == 7:
                    self.state = 71
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 72
                    self.asignacion()
                    pass

                elif la_ == 9:
                    self.state = 73
                    self.op_contenedor()
                    pass


                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token
            self._todo = None # TodoContext

        def tipo(self):
            return self.getTypedRuleContext(VisionScriptParser.TipoContext,0)


        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def todo(self):
            return self.getTypedRuleContext(VisionScriptParser.TodoContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = VisionScriptParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            localctx._tipo = self.tipo()
            self.state = 80
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 81
            self.match(VisionScriptParser.T__0)
            self.state = 82
            localctx._todo = self.todo()
            compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
            compiler.GenerateAssignmentCuad(compiler.returnIDAddress(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text)), compiler.returnIDType(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._NUMBER = None # Token
            self._TEXT = None # Token
            self._BOOL = None # Token
            self._CONTAINER = None # Token

        def NUMBER(self):
            return self.getToken(VisionScriptParser.NUMBER, 0)

        def TEXT(self):
            return self.getToken(VisionScriptParser.TEXT, 0)

        def BOOL(self):
            return self.getToken(VisionScriptParser.BOOL, 0)

        def CONTAINER(self):
            return self.getToken(VisionScriptParser.CONTAINER, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = VisionScriptParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                localctx._NUMBER = self.match(VisionScriptParser.NUMBER)
                localctx.type = (None if localctx._NUMBER is None else localctx._NUMBER.text)
                pass
            elif token in [VisionScriptParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                localctx._TEXT = self.match(VisionScriptParser.TEXT)
                localctx.type = (None if localctx._TEXT is None else localctx._TEXT.text)
                pass
            elif token in [VisionScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                localctx._BOOL = self.match(VisionScriptParser.BOOL)
                localctx.type = (None if localctx._BOOL is None else localctx._BOOL.text)
                pass
            elif token in [VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                localctx._CONTAINER = self.match(VisionScriptParser.CONTAINER)
                localctx.type = (None if localctx._CONTAINER is None else localctx._CONTAINER.text)
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


    class TodoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def casi_todo(self):
            return self.getTypedRuleContext(VisionScriptParser.Casi_todoContext,0)


        def function_call(self):
            return self.getTypedRuleContext(VisionScriptParser.Function_callContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_todo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTodo" ):
                listener.enterTodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTodo" ):
                listener.exitTodo(self)




    def todo(self):

        localctx = VisionScriptParser.TodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_todo)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.casi_todo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Casi_todoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def concat_contenedor(self):
            return self.getTypedRuleContext(VisionScriptParser.Concat_contenedorContext,0)


        def contenedor(self):
            return self.getTypedRuleContext(VisionScriptParser.ContenedorContext,0)


        def op_contenedor_returns(self):
            return self.getTypedRuleContext(VisionScriptParser.Op_contenedor_returnsContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_casi_todo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasi_todo" ):
                listener.enterCasi_todo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasi_todo" ):
                listener.exitCasi_todo(self)




    def casi_todo(self):

        localctx = VisionScriptParser.Casi_todoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_casi_todo)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.mega_expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.concat_contenedor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.contenedor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.op_contenedor_returns()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._todo = None # TodoContext

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def todo(self):
            return self.getTypedRuleContext(VisionScriptParser.TodoContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = VisionScriptParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 107
            self.match(VisionScriptParser.T__0)
            self.state = 108
            localctx._todo = self.todo()
            compiler.VarAssignment(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
            compiler.GenerateAssignmentCuad(compiler.returnIDAddress(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text)), compiler.returnIDType(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(VisionScriptParser.IF, 0)

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def BEGIN(self):
            return self.getToken(VisionScriptParser.BEGIN, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.BloqueContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(VisionScriptParser.ELSE, 0)

        def END(self):
            return self.getToken(VisionScriptParser.END, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = VisionScriptParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(VisionScriptParser.IF)
            self.state = 113
            self.mega_expresion()
            compiler.FuncionIF1()
            self.state = 115
            self.match(VisionScriptParser.BEGIN)
            self.state = 116
            self.bloque()
            self.state = 117
            self.match(VisionScriptParser.ELSE)
            compiler.FuncionIF2()
            self.state = 119
            self.bloque()
            self.state = 120
            self.match(VisionScriptParser.END)
            compiler.FuncionIF3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(VisionScriptParser.REPEAT, 0)

        def UNTIL(self):
            return self.getToken(VisionScriptParser.UNTIL, 0)

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def BEGIN(self):
            return self.getToken(VisionScriptParser.BEGIN, 0)

        def bloque(self):
            return self.getTypedRuleContext(VisionScriptParser.BloqueContext,0)


        def END(self):
            return self.getToken(VisionScriptParser.END, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = VisionScriptParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(VisionScriptParser.REPEAT)
            self.state = 124
            self.match(VisionScriptParser.UNTIL)
            compiler.FuncionRepUntil1()
            self.state = 126
            self.mega_expresion()
            compiler.FuncionRepUntil2()
            self.state = 128
            self.match(VisionScriptParser.BEGIN)
            self.state = 129
            self.bloque()
            self.state = 130
            self.match(VisionScriptParser.END)
            compiler.FuncionRepUntil3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.CondicionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.CondicionContext,i)


        def ciclo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.CicloContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.CicloContext,i)


        def read(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ReadContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ReadContext,i)


        def imprimir(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ImprimirContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ImprimirContext,i)


        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.AsignacionContext,i)


        def op_contenedor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Op_contenedorContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Op_contenedorContext,i)


        def retorno(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.RetornoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.RetornoContext,i)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = VisionScriptParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.RETURN) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 140
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 133
                    self.condicion()
                    pass

                elif la_ == 2:
                    self.state = 134
                    self.ciclo()
                    pass

                elif la_ == 3:
                    self.state = 135
                    self.read()
                    pass

                elif la_ == 4:
                    self.state = 136
                    self.imprimir()
                    pass

                elif la_ == 5:
                    self.state = 137
                    self.asignacion()
                    pass

                elif la_ == 6:
                    self.state = 138
                    self.op_contenedor()
                    pass

                elif la_ == 7:
                    self.state = 139
                    self.retorno()
                    pass


                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._READ = None # Token
            self._ID = None # Token

        def READ(self):
            return self.getToken(VisionScriptParser.READ, 0)

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = VisionScriptParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            localctx._READ = self.match(VisionScriptParser.READ)
            self.state = 146
            self.match(VisionScriptParser.T__1)
            self.state = 147
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
            self.state = 149
            self.match(VisionScriptParser.T__2)
            compiler.GenerateReadCuad((None if localctx._READ is None else localctx._READ.text),compiler.returnIDType(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.flag = None
            self._BRAILLE = None # Token
            self._PRINT = None # Token
            self._HEAR = None # Token

        def todo(self):
            return self.getTypedRuleContext(VisionScriptParser.TodoContext,0)


        def BRAILLE(self):
            return self.getToken(VisionScriptParser.BRAILLE, 0)

        def PRINT(self):
            return self.getToken(VisionScriptParser.PRINT, 0)

        def HEAR(self):
            return self.getToken(VisionScriptParser.HEAR, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)




    def imprimir(self):

        localctx = VisionScriptParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.BRAILLE]:
                self.state = 152
                localctx._BRAILLE = self.match(VisionScriptParser.BRAILLE)
                localctx.flag = (None if localctx._BRAILLE is None else localctx._BRAILLE.text)
                pass
            elif token in [VisionScriptParser.PRINT]:
                self.state = 154
                localctx._PRINT = self.match(VisionScriptParser.PRINT)
                localctx.flag = (None if localctx._PRINT is None else localctx._PRINT.text)
                pass
            elif token in [VisionScriptParser.HEAR]:
                self.state = 156
                localctx._HEAR = self.match(VisionScriptParser.HEAR)
                localctx.flag = (None if localctx._HEAR is None else localctx._HEAR.text)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 160
            self.match(VisionScriptParser.T__1)
            self.state = 161
            self.todo()
            self.state = 162
            self.match(VisionScriptParser.T__2)
            compiler.GeneratePrintCuad(localctx.flag)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mega_expresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._AND = None # Token
            self._OR = None # Token

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ExpresionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.AND)
            else:
                return self.getToken(VisionScriptParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.OR)
            else:
                return self.getToken(VisionScriptParser.OR, i)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_mega_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMega_expresion" ):
                listener.enterMega_expresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMega_expresion" ):
                listener.exitMega_expresion(self)




    def mega_expresion(self):

        localctx = VisionScriptParser.Mega_expresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mega_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expresion()
            compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.AND or _la==VisionScriptParser.OR:
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.AND]:
                    self.state = 167
                    localctx._AND = self.match(VisionScriptParser.AND)
                    compiler.InsertOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [VisionScriptParser.OR]:
                    self.state = 169
                    localctx._OR = self.match(VisionScriptParser.OR)
                    compiler.InsertOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 173
                self.expresion()
                compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._exp_todo = None # Exp_todoContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ExpContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ExpContext,i)


        def exp_todo(self):
            return self.getTypedRuleContext(VisionScriptParser.Exp_todoContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = VisionScriptParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.exp()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0):
                self.state = 182
                localctx._exp_todo = self.exp_todo()
                compiler.InsertOperator((None if localctx._exp_todo is None else self._input.getText((localctx._exp_todo.start,localctx._exp_todo.stop))))
                self.state = 184
                self.exp()
                compiler.GenerateCuad('Expresion',compiler.currentFunction)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_todoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER(self):
            return self.getToken(VisionScriptParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(VisionScriptParser.GREATER_EQUAL, 0)

        def LESS(self):
            return self.getToken(VisionScriptParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(VisionScriptParser.LESS_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(VisionScriptParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(VisionScriptParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_exp_todo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp_todo" ):
                listener.enterExp_todo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp_todo" ):
                listener.exitExp_todo(self)




    def exp_todo(self):

        localctx = VisionScriptParser.Exp_todoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp_todo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0)):
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


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._PLUS = None # Token
            self._MINUS = None # Token

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.TerminoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.TerminoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.PLUS)
            else:
                return self.getToken(VisionScriptParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.MINUS)
            else:
                return self.getToken(VisionScriptParser.MINUS, i)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = VisionScriptParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.termino()
            compiler.GenerateCuad('Termino',compiler.currentFunction)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.PLUS or _la==VisionScriptParser.MINUS:
                self.state = 197
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.PLUS]:
                    self.state = 193
                    localctx._PLUS = self.match(VisionScriptParser.PLUS)
                    compiler.InsertOperator((None if localctx._PLUS is None else localctx._PLUS.text))
                    pass
                elif token in [VisionScriptParser.MINUS]:
                    self.state = 195
                    localctx._MINUS = self.match(VisionScriptParser.MINUS)
                    compiler.InsertOperator((None if localctx._MINUS is None else localctx._MINUS.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 199
                self.termino()
                compiler.GenerateCuad('Termino',compiler.currentFunction)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULTIPLICATION = None # Token
            self._DIVISION = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.FactorContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.FactorContext,i)


        def MULTIPLICATION(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.MULTIPLICATION)
            else:
                return self.getToken(VisionScriptParser.MULTIPLICATION, i)

        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.DIVISION)
            else:
                return self.getToken(VisionScriptParser.DIVISION, i)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = VisionScriptParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.factor()
            compiler.GenerateCuad('Factor',compiler.currentFunction)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.DIVISION or _la==VisionScriptParser.MULTIPLICATION:
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.MULTIPLICATION]:
                    self.state = 209
                    localctx._MULTIPLICATION = self.match(VisionScriptParser.MULTIPLICATION)
                    compiler.InsertOperator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [VisionScriptParser.DIVISION]:
                    self.state = 211
                    localctx._DIVISION = self.match(VisionScriptParser.DIVISION)
                    compiler.InsertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 215
                self.factor()
                compiler.GenerateCuad('Factor',compiler.currentFunction)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ct = None # CtContext

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def ct(self):
            return self.getTypedRuleContext(VisionScriptParser.CtContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = VisionScriptParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(VisionScriptParser.T__1)
                compiler.InsertParentesis()
                self.state = 225
                self.mega_expresion()
                self.state = 226
                self.match(VisionScriptParser.T__2)
                compiler.RemoveParentesis()
                pass
            elif token in [VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                localctx._ct = self.ct()
                compiler.InsertIdType(localctx._ct.value,localctx._ct.type)
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


    class CtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.value = None
            self._CTN = None # Token
            self._CTBF = None # Token
            self._CTBT = None # Token
            self._CTT = None # Token
            self._ID = None # Token
            self._function_call = None # Function_callContext

        def MINUS(self):
            return self.getToken(VisionScriptParser.MINUS, 0)

        def CTN(self):
            return self.getToken(VisionScriptParser.CTN, 0)

        def CTBF(self):
            return self.getToken(VisionScriptParser.CTBF, 0)

        def CTBT(self):
            return self.getToken(VisionScriptParser.CTBT, 0)

        def CTT(self):
            return self.getToken(VisionScriptParser.CTT, 0)

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(VisionScriptParser.Function_callContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_ct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCt" ):
                listener.enterCt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCt" ):
                listener.exitCt(self)




    def ct(self):

        localctx = VisionScriptParser.CtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ct)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(VisionScriptParser.MINUS)
                self.state = 235
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = compiler.ConstDeclaration(localctx.type , '-'+(None if localctx._CTN is None else localctx._CTN.text) )
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTN is None else localctx._CTN.text) )
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                localctx._CTBF = self.match(VisionScriptParser.CTBF)
                localctx.type = 'bool'
                localctx.value = compiler.ConstDeclaration(localctx.type ,(None if localctx._CTBF is None else localctx._CTBF.text) )
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                localctx._CTBT = self.match(VisionScriptParser.CTBT)
                localctx.type = 'bool'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTBT is None else localctx._CTBT.text) )
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                localctx._CTT = self.match(VisionScriptParser.CTT)
                localctx.type = 'text'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTT is None else localctx._CTT.text) )
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 250
                localctx._ID = self.match(VisionScriptParser.ID)
                localctx.type = compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text))
                localctx.value = compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 253
                localctx._function_call = self.function_call()
                localctx.type = localctx._function_call.type
                localctx.value = localctx._function_call.value
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(VisionScriptParser.RETURN, 0)

        def todo(self):
            return self.getTypedRuleContext(VisionScriptParser.TodoContext,0)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)




    def retorno(self):

        localctx = VisionScriptParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_retorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(VisionScriptParser.RETURN)
            self.state = 260
            self.match(VisionScriptParser.T__1)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 261
                self.todo()
                compiler.GenerateFunReturns(compiler.returnFuncReturnAddress(compiler.currentFunction))


            self.state = 266
            self.match(VisionScriptParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._function_type = None # Function_typeContext
            self._ID = None # Token
            self._tipo = None # TipoContext

        def function_type(self):
            return self.getTypedRuleContext(VisionScriptParser.Function_typeContext,0)


        def FUNCTION(self):
            return self.getToken(VisionScriptParser.FUNCTION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.ID)
            else:
                return self.getToken(VisionScriptParser.ID, i)

        def BEGIN(self):
            return self.getToken(VisionScriptParser.BEGIN, 0)

        def func_bloque(self):
            return self.getTypedRuleContext(VisionScriptParser.Func_bloqueContext,0)


        def END(self):
            return self.getToken(VisionScriptParser.END, 0)

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.TipoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.TipoContext,i)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = VisionScriptParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            localctx._function_type = self.function_type()
            self.state = 269
            self.match(VisionScriptParser.FUNCTION)
            self.state = 270
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.currentFunction = (None if localctx._ID is None else localctx._ID.text)
            compiler.FuncDeclaration(compiler.currentFunction,localctx._function_type.type)
            compiler.GenerateFunGoto()
            self.state = 274
            self.match(VisionScriptParser.T__1)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER))) != 0):
                self.state = 275
                localctx._tipo = self.tipo()
                self.state = 276
                localctx._ID = self.match(VisionScriptParser.ID)
                compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                compiler.ParamDeclaration(compiler.currentFunction,localctx._tipo.type)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 279
                    self.match(VisionScriptParser.T__3)
                    self.state = 280
                    localctx._tipo = self.tipo()
                    self.state = 281
                    localctx._ID = self.match(VisionScriptParser.ID)
                    compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                    compiler.ParamDeclaration(compiler.currentFunction,localctx._tipo.type)
                    self.state = 289
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 292
            self.match(VisionScriptParser.T__2)
            self.state = 293
            self.match(VisionScriptParser.BEGIN)
            self.state = 294
            self.func_bloque()
            self.state = 295
            self.match(VisionScriptParser.END)
            compiler.GenerateEndProc()
            compiler.RegisterLocalCont(compiler.currentFunction)
            compiler.FillFunGoto()
            compiler.currentFunction = '@global'
            compiler.memLocal = 20000
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self._tipo = None # TipoContext
            self._VOID = None # Token

        def tipo(self):
            return self.getTypedRuleContext(VisionScriptParser.TipoContext,0)


        def VOID(self):
            return self.getToken(VisionScriptParser.VOID, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_function_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_type" ):
                listener.enterFunction_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_type" ):
                listener.exitFunction_type(self)




    def function_type(self):

        localctx = VisionScriptParser.Function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_function_type)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER, VisionScriptParser.TEXT, VisionScriptParser.BOOL, VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                localctx._tipo = self.tipo()
                localctx.type = localctx._tipo.type
                pass
            elif token in [VisionScriptParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                localctx._VOID = self.match(VisionScriptParser.VOID)
                localctx.type = (None if localctx._VOID is None else localctx._VOID.text)
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


    class Func_bloqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.VariableContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.VariableContext,i)


        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.CondicionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.CondicionContext,i)


        def ciclo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.CicloContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.CicloContext,i)


        def read(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ReadContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ReadContext,i)


        def imprimir(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ImprimirContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ImprimirContext,i)


        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.AsignacionContext,i)


        def op_contenedor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Op_contenedorContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Op_contenedorContext,i)


        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Function_callContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Function_callContext,i)


        def retorno(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.RetornoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.RetornoContext,i)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_func_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_bloque" ):
                listener.enterFunc_bloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_bloque" ):
                listener.exitFunc_bloque(self)




    def func_bloque(self):

        localctx = VisionScriptParser.Func_bloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.RETURN) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 318
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 309
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 310
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 311
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 312
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 313
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 314
                    self.asignacion()
                    pass

                elif la_ == 7:
                    self.state = 315
                    self.op_contenedor()
                    pass

                elif la_ == 8:
                    self.state = 316
                    self.function_call()
                    pass

                elif la_ == 9:
                    self.state = 317
                    self.retorno()
                    pass


                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None
            self.value = None
            self._ID = None # Token

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def casi_todo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Casi_todoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Casi_todoContext,i)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = VisionScriptParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.GenerateEra((None if localctx._ID is None else localctx._ID.text))
            localctx.value = compiler.returnFuncReturnAddress((None if localctx._ID is None else localctx._ID.text))
            localctx.type = compiler.returnFuncReturnType((None if localctx._ID is None else localctx._ID.text))
            self.state = 327
            self.match(VisionScriptParser.T__1)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 328
                self.casi_todo()
                compiler.GenerateParameter(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 330
                    self.match(VisionScriptParser.T__3)
                    self.state = 331
                    self.casi_todo()
                    compiler.GenerateParameter(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 341
            self.match(VisionScriptParser.T__2)
            compiler.VerifyParameters(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContenedorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mega_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Mega_expresionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,i)


        def getRuleIndex(self):
            return VisionScriptParser.RULE_contenedor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContenedor" ):
                listener.enterContenedor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContenedor" ):
                listener.exitContenedor(self)




    def contenedor(self):

        localctx = VisionScriptParser.ContenedorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(VisionScriptParser.T__4)
            compiler.GenerateEmptyContainer(compiler.currentFunction)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 346
                self.mega_expresion()
                compiler.GenerateFillContainer()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 348
                    self.match(VisionScriptParser.T__3)
                    self.state = 349
                    self.mega_expresion()
                    compiler.GenerateFillContainer()
                    self.state = 356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 359
            self.match(VisionScriptParser.T__5)
            compiler.RegisterContainer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_contenedor_returnsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.flag = None
            self._ID = None # Token
            self._GET_BACK = None # Token
            self._GET_FRONT = None # Token
            self._LENGTH = None # Token
            self._GET = None # Token

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def GET(self):
            return self.getToken(VisionScriptParser.GET, 0)

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def GET_BACK(self):
            return self.getToken(VisionScriptParser.GET_BACK, 0)

        def GET_FRONT(self):
            return self.getToken(VisionScriptParser.GET_FRONT, 0)

        def LENGTH(self):
            return self.getToken(VisionScriptParser.LENGTH, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_op_contenedor_returns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_contenedor_returns" ):
                listener.enterOp_contenedor_returns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_contenedor_returns" ):
                listener.exitOp_contenedor_returns(self)




    def op_contenedor_returns(self):

        localctx = VisionScriptParser.Op_contenedor_returnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_op_contenedor_returns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 363
            self.match(VisionScriptParser.T__6)
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.GET_BACK, VisionScriptParser.GET_FRONT, VisionScriptParser.LENGTH]:
                self.state = 370
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.GET_BACK]:
                    self.state = 364
                    localctx._GET_BACK = self.match(VisionScriptParser.GET_BACK)
                    localctx.flag = (None if localctx._GET_BACK is None else localctx._GET_BACK.text)
                    pass
                elif token in [VisionScriptParser.GET_FRONT]:
                    self.state = 366
                    localctx._GET_FRONT = self.match(VisionScriptParser.GET_FRONT)
                    localctx.flag = (None if localctx._GET_FRONT is None else localctx._GET_FRONT.text)
                    pass
                elif token in [VisionScriptParser.LENGTH]:
                    self.state = 368
                    localctx._LENGTH = self.match(VisionScriptParser.LENGTH)
                    localctx.flag = (None if localctx._LENGTH is None else localctx._LENGTH.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 372
                self.match(VisionScriptParser.T__1)
                self.state = 373
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer1(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.currentFunction)
                pass
            elif token in [VisionScriptParser.GET]:
                self.state = 375
                localctx._GET = self.match(VisionScriptParser.GET)
                localctx.flag = (None if localctx._GET is None else localctx._GET.text)
                self.state = 377
                self.match(VisionScriptParser.T__1)
                self.state = 378
                self.mega_expresion()
                self.state = 379
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer2(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.currentFunction)
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


    class Op_contenedorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.flag = None
            self._ID = None # Token
            self._INSERT_BACK = None # Token
            self._INSERT_FRONT = None # Token
            self._INSERT = None # Token

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def mega_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Mega_expresionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,i)


        def INSERT(self):
            return self.getToken(VisionScriptParser.INSERT, 0)

        def INSERT_BACK(self):
            return self.getToken(VisionScriptParser.INSERT_BACK, 0)

        def INSERT_FRONT(self):
            return self.getToken(VisionScriptParser.INSERT_FRONT, 0)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_op_contenedor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_contenedor" ):
                listener.enterOp_contenedor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_contenedor" ):
                listener.exitOp_contenedor(self)




    def op_contenedor(self):

        localctx = VisionScriptParser.Op_contenedorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_op_contenedor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 385
            self.match(VisionScriptParser.T__6)
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.INSERT_BACK, VisionScriptParser.INSERT_FRONT]:
                self.state = 390
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.INSERT_BACK]:
                    self.state = 386
                    localctx._INSERT_BACK = self.match(VisionScriptParser.INSERT_BACK)
                    localctx.flag = (None if localctx._INSERT_BACK is None else localctx._INSERT_BACK.text)
                    pass
                elif token in [VisionScriptParser.INSERT_FRONT]:
                    self.state = 388
                    localctx._INSERT_FRONT = self.match(VisionScriptParser.INSERT_FRONT)
                    localctx.flag = (None if localctx._INSERT_FRONT is None else localctx._INSERT_FRONT.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 392
                self.match(VisionScriptParser.T__1)
                self.state = 393
                self.mega_expresion()
                self.state = 394
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer3(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.INSERT]:
                self.state = 397
                localctx._INSERT = self.match(VisionScriptParser.INSERT)
                localctx.flag = (None if localctx._INSERT is None else localctx._INSERT.text)
                self.state = 399
                self.match(VisionScriptParser.T__1)
                self.state = 400
                self.mega_expresion()
                self.state = 401
                self.match(VisionScriptParser.T__3)
                self.state = 402
                self.mega_expresion()
                self.state = 403
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer4(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
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


    class Concat_contenedorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.ID)
            else:
                return self.getToken(VisionScriptParser.ID, i)

        def contenedor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.ContenedorContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.ContenedorContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(VisionScriptParser.PLUS)
            else:
                return self.getToken(VisionScriptParser.PLUS, i)

        def getRuleIndex(self):
            return VisionScriptParser.RULE_concat_contenedor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat_contenedor" ):
                listener.enterConcat_contenedor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat_contenedor" ):
                listener.exitConcat_contenedor(self)




    def concat_contenedor(self):

        localctx = VisionScriptParser.Concat_contenedorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_concat_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.ID]:
                self.state = 408
                localctx._ID = self.match(VisionScriptParser.ID)
                compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.T__4]:
                self.state = 410
                self.contenedor()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 420 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 413
                self.match(VisionScriptParser.PLUS)
                self.state = 417
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.ID]:
                    self.state = 414
                    localctx._ID = self.match(VisionScriptParser.ID)
                    compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                    pass
                elif token in [VisionScriptParser.T__4]:
                    self.state = 416
                    self.contenedor()
                    pass
                else:
                    raise NoViableAltException(self)

                compiler.GenerateConcatContainer(compiler.currentFunction)
                self.state = 422 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==VisionScriptParser.PLUS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





