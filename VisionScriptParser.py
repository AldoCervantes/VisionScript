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
        buf.write("\u01b6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3N\n\3\f\3\16\3Q\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5b\n\5")
        buf.write("\3\6\3\6\5\6f\n\6\3\7\3\7\3\7\5\7k\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\7\13\u0090\n\13\f\13\16\13\u0093")
        buf.write("\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00a2\n\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00af\n\16\3\16\3\16\3\16\7\16\u00b4")
        buf.write("\n\16\f\16\16\16\u00b7\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00bf\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00c9\n\21\3\21\3\21\3\21\7\21\u00ce\n\21")
        buf.write("\f\21\16\21\u00d1\13\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00d9\n\22\3\22\3\22\3\22\7\22\u00de\n\22\f\22\16")
        buf.write("\22\u00e1\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00ec\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u010d\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0126\n")
        buf.write("\26\f\26\16\26\u0129\13\26\5\26\u012b\n\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u013d\n\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\7\30\u0148\n\30\f\30\16\30\u014b")
        buf.write("\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\7\31\u0158\n\31\f\31\16\31\u015b\13\31\5\31\u015d")
        buf.write("\n\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u016a\n\32\f\32\16\32\u016d\13\32\5\32\u016f")
        buf.write("\n\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u017c\n\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u0188\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u0190\n\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u019b\n\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u01a4\n\34\3\35\3\35\3\35\5\35\u01a9")
        buf.write("\n\35\3\35\3\35\3\35\3\35\5\35\u01af\n\35\3\35\6\35\u01b2")
        buf.write("\n\35\r\35\16\35\u01b3\3\35\2\2\36\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668\2\3\4\2\27\30")
        buf.write("\60\63\2\u01da\2:\3\2\2\2\4O\3\2\2\2\6R\3\2\2\2\ba\3\2")
        buf.write("\2\2\ne\3\2\2\2\fj\3\2\2\2\16l\3\2\2\2\20r\3\2\2\2\22")
        buf.write("}\3\2\2\2\24\u0091\3\2\2\2\26\u0094\3\2\2\2\30\u00a1\3")
        buf.write("\2\2\2\32\u00a8\3\2\2\2\34\u00b8\3\2\2\2\36\u00c0\3\2")
        buf.write("\2\2 \u00c2\3\2\2\2\"\u00d2\3\2\2\2$\u00eb\3\2\2\2&\u010c")
        buf.write("\3\2\2\2(\u010e\3\2\2\2*\u0114\3\2\2\2,\u013c\3\2\2\2")
        buf.write(".\u0149\3\2\2\2\60\u014c\3\2\2\2\62\u0161\3\2\2\2\64\u0173")
        buf.write("\3\2\2\2\66\u0189\3\2\2\28\u01a8\3\2\2\2:;\b\2\1\2;<\5")
        buf.write("\4\3\2<=\7\2\2\3=>\b\2\1\2>?\b\2\1\2?@\b\2\1\2@A\b\2\1")
        buf.write("\2AB\b\2\1\2BC\b\2\1\2C\3\3\2\2\2DN\5\6\4\2EN\5\20\t\2")
        buf.write("FN\5\22\n\2GN\5\26\f\2HN\5\30\r\2IN\5*\26\2JN\5\60\31")
        buf.write("\2KN\5\16\b\2LN\5\66\34\2MD\3\2\2\2ME\3\2\2\2MF\3\2\2")
        buf.write("\2MG\3\2\2\2MH\3\2\2\2MI\3\2\2\2MJ\3\2\2\2MK\3\2\2\2M")
        buf.write("L\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\5\3\2\2\2QO\3")
        buf.write("\2\2\2RS\5\b\5\2ST\7)\2\2TU\7\3\2\2UV\5\n\6\2VW\b\4\1")
        buf.write("\2WX\b\4\1\2X\7\3\2\2\2YZ\7\20\2\2Zb\b\5\1\2[\\\7\21\2")
        buf.write("\2\\b\b\5\1\2]^\7\22\2\2^b\b\5\1\2_`\7\31\2\2`b\b\5\1")
        buf.write("\2aY\3\2\2\2a[\3\2\2\2a]\3\2\2\2a_\3\2\2\2b\t\3\2\2\2")
        buf.write("cf\5\f\7\2df\5\60\31\2ec\3\2\2\2ed\3\2\2\2f\13\3\2\2\2")
        buf.write("gk\5\32\16\2hk\58\35\2ik\5\62\32\2jg\3\2\2\2jh\3\2\2\2")
        buf.write("ji\3\2\2\2k\r\3\2\2\2lm\7)\2\2mn\7\3\2\2no\5\n\6\2op\b")
        buf.write("\b\1\2pq\b\b\1\2q\17\3\2\2\2rs\7\16\2\2st\5\32\16\2tu")
        buf.write("\b\t\1\2uv\7\32\2\2vw\5\24\13\2wx\7\17\2\2xy\b\t\1\2y")
        buf.write("z\5\24\13\2z{\7\33\2\2{|\b\t\1\2|\21\3\2\2\2}~\7\34\2")
        buf.write("\2~\177\7\35\2\2\177\u0080\b\n\1\2\u0080\u0081\5\32\16")
        buf.write("\2\u0081\u0082\b\n\1\2\u0082\u0083\7\32\2\2\u0083\u0084")
        buf.write("\5\24\13\2\u0084\u0085\7\33\2\2\u0085\u0086\b\n\1\2\u0086")
        buf.write("\23\3\2\2\2\u0087\u0090\5\20\t\2\u0088\u0090\5\22\n\2")
        buf.write("\u0089\u0090\5\26\f\2\u008a\u0090\5\30\r\2\u008b\u0090")
        buf.write("\5\16\b\2\u008c\u0090\5\66\34\2\u008d\u0090\5(\25\2\u008e")
        buf.write("\u0090\5\60\31\2\u008f\u0087\3\2\2\2\u008f\u0088\3\2\2")
        buf.write("\2\u008f\u0089\3\2\2\2\u008f\u008a\3\2\2\2\u008f\u008b")
        buf.write("\3\2\2\2\u008f\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\25\3\2\2\2\u0093\u0091\3\2")
        buf.write("\2\2\u0094\u0095\7\n\2\2\u0095\u0096\7\4\2\2\u0096\u0097")
        buf.write("\7)\2\2\u0097\u0098\b\f\1\2\u0098\u0099\7\5\2\2\u0099")
        buf.write("\u009a\b\f\1\2\u009a\27\3\2\2\2\u009b\u009c\7\r\2\2\u009c")
        buf.write("\u00a2\b\r\1\2\u009d\u009e\7\13\2\2\u009e\u00a2\b\r\1")
        buf.write("\2\u009f\u00a0\7\f\2\2\u00a0\u00a2\b\r\1\2\u00a1\u009b")
        buf.write("\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a4\7\4\2\2\u00a4\u00a5\5\n\6\2")
        buf.write("\u00a5\u00a6\7\5\2\2\u00a6\u00a7\b\r\1\2\u00a7\31\3\2")
        buf.write("\2\2\u00a8\u00a9\5\34\17\2\u00a9\u00b5\b\16\1\2\u00aa")
        buf.write("\u00ab\7\25\2\2\u00ab\u00af\b\16\1\2\u00ac\u00ad\7\26")
        buf.write("\2\2\u00ad\u00af\b\16\1\2\u00ae\u00aa\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\5\34\17\2\u00b1")
        buf.write("\u00b2\b\16\1\2\u00b2\u00b4\3\2\2\2\u00b3\u00ae\3\2\2")
        buf.write("\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\33\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00be")
        buf.write("\5 \21\2\u00b9\u00ba\5\36\20\2\u00ba\u00bb\b\17\1\2\u00bb")
        buf.write("\u00bc\5 \21\2\u00bc\u00bd\b\17\1\2\u00bd\u00bf\3\2\2")
        buf.write("\2\u00be\u00b9\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\35\3")
        buf.write("\2\2\2\u00c0\u00c1\t\2\2\2\u00c1\37\3\2\2\2\u00c2\u00c3")
        buf.write("\5\"\22\2\u00c3\u00cf\b\21\1\2\u00c4\u00c5\7,\2\2\u00c5")
        buf.write("\u00c9\b\21\1\2\u00c6\u00c7\7-\2\2\u00c7\u00c9\b\21\1")
        buf.write("\2\u00c8\u00c4\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cb\5\"\22\2\u00cb\u00cc\b\21\1\2\u00cc")
        buf.write("\u00ce\3\2\2\2\u00cd\u00c8\3\2\2\2\u00ce\u00d1\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0!\3\2\2")
        buf.write("\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\5$\23\2\u00d3\u00df")
        buf.write("\b\22\1\2\u00d4\u00d5\7/\2\2\u00d5\u00d9\b\22\1\2\u00d6")
        buf.write("\u00d7\7.\2\2\u00d7\u00d9\b\22\1\2\u00d8\u00d4\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\5")
        buf.write("$\23\2\u00db\u00dc\b\22\1\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00d8\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e0#\3\2\2\2\u00e1\u00df\3\2\2")
        buf.write("\2\u00e2\u00e3\7\4\2\2\u00e3\u00e4\b\23\1\2\u00e4\u00e5")
        buf.write("\5\32\16\2\u00e5\u00e6\7\5\2\2\u00e6\u00e7\b\23\1\2\u00e7")
        buf.write("\u00ec\3\2\2\2\u00e8\u00e9\5&\24\2\u00e9\u00ea\b\23\1")
        buf.write("\2\u00ea\u00ec\3\2\2\2\u00eb\u00e2\3\2\2\2\u00eb\u00e8")
        buf.write("\3\2\2\2\u00ec%\3\2\2\2\u00ed\u00ee\7-\2\2\u00ee\u00ef")
        buf.write("\7*\2\2\u00ef\u00f0\b\24\1\2\u00f0\u010d\b\24\1\2\u00f1")
        buf.write("\u00f2\7*\2\2\u00f2\u00f3\b\24\1\2\u00f3\u010d\b\24\1")
        buf.write("\2\u00f4\u00f5\7\23\2\2\u00f5\u00f6\b\24\1\2\u00f6\u010d")
        buf.write("\b\24\1\2\u00f7\u00f8\7\24\2\2\u00f8\u00f9\b\24\1\2\u00f9")
        buf.write("\u010d\b\24\1\2\u00fa\u00fb\7+\2\2\u00fb\u00fc\b\24\1")
        buf.write("\2\u00fc\u010d\b\24\1\2\u00fd\u00fe\7)\2\2\u00fe\u00ff")
        buf.write("\b\24\1\2\u00ff\u010d\b\24\1\2\u0100\u0101\b\24\1\2\u0101")
        buf.write("\u0102\5\60\31\2\u0102\u0103\b\24\1\2\u0103\u0104\b\24")
        buf.write("\1\2\u0104\u0105\b\24\1\2\u0105\u010d\3\2\2\2\u0106\u0107")
        buf.write("\b\24\1\2\u0107\u0108\5\64\33\2\u0108\u0109\b\24\1\2\u0109")
        buf.write("\u010a\b\24\1\2\u010a\u010b\b\24\1\2\u010b\u010d\3\2\2")
        buf.write("\2\u010c\u00ed\3\2\2\2\u010c\u00f1\3\2\2\2\u010c\u00f4")
        buf.write("\3\2\2\2\u010c\u00f7\3\2\2\2\u010c\u00fa\3\2\2\2\u010c")
        buf.write("\u00fd\3\2\2\2\u010c\u0100\3\2\2\2\u010c\u0106\3\2\2\2")
        buf.write("\u010d\'\3\2\2\2\u010e\u010f\7\37\2\2\u010f\u0110\7\4")
        buf.write("\2\2\u0110\u0111\5\n\6\2\u0111\u0112\b\25\1\2\u0112\u0113")
        buf.write("\7\5\2\2\u0113)\3\2\2\2\u0114\u0115\5,\27\2\u0115\u0116")
        buf.write("\7\36\2\2\u0116\u0117\7)\2\2\u0117\u0118\b\26\1\2\u0118")
        buf.write("\u0119\b\26\1\2\u0119\u011a\b\26\1\2\u011a\u012a\7\4\2")
        buf.write("\2\u011b\u011c\5\b\5\2\u011c\u011d\7)\2\2\u011d\u011e")
        buf.write("\b\26\1\2\u011e\u0127\b\26\1\2\u011f\u0120\7\6\2\2\u0120")
        buf.write("\u0121\5\b\5\2\u0121\u0122\7)\2\2\u0122\u0123\b\26\1\2")
        buf.write("\u0123\u0124\b\26\1\2\u0124\u0126\3\2\2\2\u0125\u011f")
        buf.write("\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u012a\u011b\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c\u012d\7\5\2\2\u012d\u012e\7\32\2\2\u012e")
        buf.write("\u012f\5.\30\2\u012f\u0130\7\33\2\2\u0130\u0131\b\26\1")
        buf.write("\2\u0131\u0132\b\26\1\2\u0132\u0133\b\26\1\2\u0133\u0134")
        buf.write("\b\26\1\2\u0134\u0135\b\26\1\2\u0135\u0136\b\26\1\2\u0136")
        buf.write("+\3\2\2\2\u0137\u0138\5\b\5\2\u0138\u0139\b\27\1\2\u0139")
        buf.write("\u013d\3\2\2\2\u013a\u013b\7&\2\2\u013b\u013d\b\27\1\2")
        buf.write("\u013c\u0137\3\2\2\2\u013c\u013a\3\2\2\2\u013d-\3\2\2")
        buf.write("\2\u013e\u0148\5\6\4\2\u013f\u0148\5\20\t\2\u0140\u0148")
        buf.write("\5\22\n\2\u0141\u0148\5\26\f\2\u0142\u0148\5\30\r\2\u0143")
        buf.write("\u0148\5\16\b\2\u0144\u0148\5\66\34\2\u0145\u0148\5\60")
        buf.write("\31\2\u0146\u0148\5(\25\2\u0147\u013e\3\2\2\2\u0147\u013f")
        buf.write("\3\2\2\2\u0147\u0140\3\2\2\2\u0147\u0141\3\2\2\2\u0147")
        buf.write("\u0142\3\2\2\2\u0147\u0143\3\2\2\2\u0147\u0144\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148\u014b\3")
        buf.write("\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a/")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d\7)\2\2\u014d")
        buf.write("\u014e\b\31\1\2\u014e\u014f\b\31\1\2\u014f\u0150\b\31")
        buf.write("\1\2\u0150\u015c\7\4\2\2\u0151\u0152\5\f\7\2\u0152\u0159")
        buf.write("\b\31\1\2\u0153\u0154\7\6\2\2\u0154\u0155\5\f\7\2\u0155")
        buf.write("\u0156\b\31\1\2\u0156\u0158\3\2\2\2\u0157\u0153\3\2\2")
        buf.write("\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a")
        buf.write("\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015c")
        buf.write("\u0151\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015f\7\5\2\2\u015f\u0160\b\31\1\2\u0160\61\3\2")
        buf.write("\2\2\u0161\u0162\7\7\2\2\u0162\u016e\b\32\1\2\u0163\u0164")
        buf.write("\5\32\16\2\u0164\u016b\b\32\1\2\u0165\u0166\7\6\2\2\u0166")
        buf.write("\u0167\5\32\16\2\u0167\u0168\b\32\1\2\u0168\u016a\3\2")
        buf.write("\2\2\u0169\u0165\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016f\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016e\u0163\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\3\2\2\2\u0170\u0171\7\b\2\2\u0171\u0172\b")
        buf.write("\32\1\2\u0172\63\3\2\2\2\u0173\u0174\7)\2\2\u0174\u0187")
        buf.write("\7\t\2\2\u0175\u0176\7 \2\2\u0176\u017c\b\33\1\2\u0177")
        buf.write("\u0178\7!\2\2\u0178\u017c\b\33\1\2\u0179\u017a\7\'\2\2")
        buf.write("\u017a\u017c\b\33\1\2\u017b\u0175\3\2\2\2\u017b\u0177")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017e\7\4\2\2\u017e\u017f\7\5\2\2\u017f\u0188\b\33\1")
        buf.write("\2\u0180\u0181\7\"\2\2\u0181\u0182\b\33\1\2\u0182\u0183")
        buf.write("\7\4\2\2\u0183\u0184\5\32\16\2\u0184\u0185\7\5\2\2\u0185")
        buf.write("\u0186\b\33\1\2\u0186\u0188\3\2\2\2\u0187\u017b\3\2\2")
        buf.write("\2\u0187\u0180\3\2\2\2\u0188\65\3\2\2\2\u0189\u018a\7")
        buf.write(")\2\2\u018a\u01a3\7\t\2\2\u018b\u018c\7#\2\2\u018c\u0190")
        buf.write("\b\34\1\2\u018d\u018e\7$\2\2\u018e\u0190\b\34\1\2\u018f")
        buf.write("\u018b\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0192\7\4\2\2\u0192\u0193\5\32\16\2\u0193\u0194")
        buf.write("\7\5\2\2\u0194\u0195\b\34\1\2\u0195\u01a4\3\2\2\2\u0196")
        buf.write("\u0197\7%\2\2\u0197\u019b\b\34\1\2\u0198\u0199\7(\2\2")
        buf.write("\u0199\u019b\b\34\1\2\u019a\u0196\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\7\4\2\2\u019d")
        buf.write("\u019e\5\32\16\2\u019e\u019f\7\6\2\2\u019f\u01a0\5\32")
        buf.write("\16\2\u01a0\u01a1\7\5\2\2\u01a1\u01a2\b\34\1\2\u01a2\u01a4")
        buf.write("\3\2\2\2\u01a3\u018f\3\2\2\2\u01a3\u019a\3\2\2\2\u01a4")
        buf.write("\67\3\2\2\2\u01a5\u01a6\7)\2\2\u01a6\u01a9\b\35\1\2\u01a7")
        buf.write("\u01a9\5\62\32\2\u01a8\u01a5\3\2\2\2\u01a8\u01a7\3\2\2")
        buf.write("\2\u01a9\u01b1\3\2\2\2\u01aa\u01ae\7,\2\2\u01ab\u01ac")
        buf.write("\7)\2\2\u01ac\u01af\b\35\1\2\u01ad\u01af\5\62\32\2\u01ae")
        buf.write("\u01ab\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01b2\b\35\1\2\u01b1\u01aa\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("9\3\2\2\2$MOaej\u008f\u0091\u00a1\u00ae\u00b5\u00be\u00c8")
        buf.write("\u00cf\u00d8\u00df\u00eb\u010c\u0127\u012a\u013c\u0147")
        buf.write("\u0149\u0159\u015c\u016b\u016e\u017b\u0187\u018f\u019a")
        buf.write("\u01a3\u01a8\u01ae\u01b3")
        return buf.getvalue()


class VisionScriptParser ( Parser ):

    grammarFileName = "VisionScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','", "'['", "']'", 
                     "'.'", "'read'", "'print'", "'hear'", "'braille'", 
                     "'if'", "'else'", "'number'", "'text'", "'bool'", "'false'", 
                     "'true'", "'and'", "'or'", "'equal'", "'not_equal'", 
                     "'container'", "'begin'", "'end'", "'repeat'", "'until'", 
                     "'function'", "'return'", "'get_back'", "'get_front'", 
                     "'get'", "'insert_back'", "'insert_front'", "'insert'", 
                     "'void'", "'length'", "'replace'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'/'", "'*'", "'>'", "'>='", 
                     "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "READ", "PRINT", "HEAR", "BRAILLE", "IF", "ELSE", 
                      "NUMBER", "TEXT", "BOOL", "CTBF", "CTBT", "AND", "OR", 
                      "EQUAL", "NOT_EQUAL", "CONTAINER", "BEGIN", "END", 
                      "REPEAT", "UNTIL", "FUNCTION", "RETURN", "GET_BACK", 
                      "GET_FRONT", "GET", "INSERT_BACK", "INSERT_FRONT", 
                      "INSERT", "VOID", "LENGTH", "REPLACE", "ID", "CTN", 
                      "CTT", "PLUS", "MINUS", "DIVISION", "MULTIPLICATION", 
                      "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL", 
                      "WHITESPACE", "NEWLINE" ]

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
    UNTIL=27
    FUNCTION=28
    RETURN=29
    GET_BACK=30
    GET_FRONT=31
    GET=32
    INSERT_BACK=33
    INSERT_FRONT=34
    INSERT=35
    VOID=36
    LENGTH=37
    REPLACE=38
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
            #compiler.printCuad()
            #compiler.showFunctionDirectory()
            vm.FunSpaceMemTable = compiler.FunLocalMems 
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
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.VOID) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 75
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 66
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 67
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 68
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 69
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 70
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 71
                    self.function()
                    pass

                elif la_ == 7:
                    self.state = 72
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 73
                    self.asignacion()
                    pass

                elif la_ == 9:
                    self.state = 74
                    self.op_contenedor()
                    pass


                self.state = 79
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
            self.state = 80
            localctx._tipo = self.tipo()
            self.state = 81
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 82
            self.match(VisionScriptParser.T__0)
            self.state = 83
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
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                localctx._NUMBER = self.match(VisionScriptParser.NUMBER)
                localctx.type = (None if localctx._NUMBER is None else localctx._NUMBER.text)
                pass
            elif token in [VisionScriptParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                localctx._TEXT = self.match(VisionScriptParser.TEXT)
                localctx.type = (None if localctx._TEXT is None else localctx._TEXT.text)
                pass
            elif token in [VisionScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                localctx._BOOL = self.match(VisionScriptParser.BOOL)
                localctx.type = (None if localctx._BOOL is None else localctx._BOOL.text)
                pass
            elif token in [VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.casi_todo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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
                self.state = 101
                self.mega_expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.concat_contenedor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.contenedor()
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


        def function_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Function_callContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Function_callContext,i)


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
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.RETURN) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 141
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

                elif la_ == 8:
                    self.state = 140
                    self.function_call()
                    pass


                self.state = 145
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
            self.state = 146
            localctx._READ = self.match(VisionScriptParser.READ)
            self.state = 147
            self.match(VisionScriptParser.T__1)
            self.state = 148
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
            self.state = 150
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
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.BRAILLE]:
                self.state = 153
                localctx._BRAILLE = self.match(VisionScriptParser.BRAILLE)
                localctx.flag = (None if localctx._BRAILLE is None else localctx._BRAILLE.text)
                pass
            elif token in [VisionScriptParser.PRINT]:
                self.state = 155
                localctx._PRINT = self.match(VisionScriptParser.PRINT)
                localctx.flag = (None if localctx._PRINT is None else localctx._PRINT.text)
                pass
            elif token in [VisionScriptParser.HEAR]:
                self.state = 157
                localctx._HEAR = self.match(VisionScriptParser.HEAR)
                localctx.flag = (None if localctx._HEAR is None else localctx._HEAR.text)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.match(VisionScriptParser.T__1)
            self.state = 162
            self.todo()
            self.state = 163
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
            self.state = 166
            self.expresion()
            compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.AND or _la==VisionScriptParser.OR:
                self.state = 172
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.AND]:
                    self.state = 168
                    localctx._AND = self.match(VisionScriptParser.AND)
                    compiler.InsertOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [VisionScriptParser.OR]:
                    self.state = 170
                    localctx._OR = self.match(VisionScriptParser.OR)
                    compiler.InsertOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 174
                self.expresion()
                compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
                self.state = 181
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
            self.state = 182
            self.exp()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0):
                self.state = 183
                localctx._exp_todo = self.exp_todo()
                compiler.InsertOperator((None if localctx._exp_todo is None else self._input.getText((localctx._exp_todo.start,localctx._exp_todo.stop))))
                self.state = 185
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
            self.state = 190
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
            self.state = 192
            self.termino()
            compiler.GenerateCuad('Termino',compiler.currentFunction)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.PLUS or _la==VisionScriptParser.MINUS:
                self.state = 198
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.PLUS]:
                    self.state = 194
                    localctx._PLUS = self.match(VisionScriptParser.PLUS)
                    compiler.InsertOperator((None if localctx._PLUS is None else localctx._PLUS.text))
                    pass
                elif token in [VisionScriptParser.MINUS]:
                    self.state = 196
                    localctx._MINUS = self.match(VisionScriptParser.MINUS)
                    compiler.InsertOperator((None if localctx._MINUS is None else localctx._MINUS.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 200
                self.termino()
                compiler.GenerateCuad('Termino',compiler.currentFunction)
                self.state = 207
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
            self.state = 208
            self.factor()
            compiler.GenerateCuad('Factor',compiler.currentFunction)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.DIVISION or _la==VisionScriptParser.MULTIPLICATION:
                self.state = 214
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.MULTIPLICATION]:
                    self.state = 210
                    localctx._MULTIPLICATION = self.match(VisionScriptParser.MULTIPLICATION)
                    compiler.InsertOperator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [VisionScriptParser.DIVISION]:
                    self.state = 212
                    localctx._DIVISION = self.match(VisionScriptParser.DIVISION)
                    compiler.InsertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 216
                self.factor()
                compiler.GenerateCuad('Factor',compiler.currentFunction)
                self.state = 223
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
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(VisionScriptParser.T__1)
                compiler.InsertParentesis()
                self.state = 226
                self.mega_expresion()
                self.state = 227
                self.match(VisionScriptParser.T__2)
                compiler.RemoveParentesis()
                pass
            elif token in [VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
            self._op_contenedor_returns = None # Op_contenedor_returnsContext

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


        def op_contenedor_returns(self):
            return self.getTypedRuleContext(VisionScriptParser.Op_contenedor_returnsContext,0)


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
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(VisionScriptParser.MINUS)
                self.state = 236
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = compiler.ConstDeclaration(localctx.type , '-'+(None if localctx._CTN is None else localctx._CTN.text) )
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTN is None else localctx._CTN.text) )
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                localctx._CTBF = self.match(VisionScriptParser.CTBF)
                localctx.type = 'bool'
                localctx.value = compiler.ConstDeclaration(localctx.type ,(None if localctx._CTBF is None else localctx._CTBF.text) )
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                localctx._CTBT = self.match(VisionScriptParser.CTBT)
                localctx.type = 'bool'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTBT is None else localctx._CTBT.text) )
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                localctx._CTT = self.match(VisionScriptParser.CTT)
                localctx.type = 'text'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTT is None else localctx._CTT.text) )
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 251
                localctx._ID = self.match(VisionScriptParser.ID)
                localctx.type = compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text))
                localctx.value = compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text))
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                compiler.InsertParentesis()
                self.state = 255
                localctx._function_call = self.function_call()
                localctx.type = localctx._function_call.type
                localctx.value = localctx._function_call.value
                compiler.RemoveParentesis()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                compiler.InsertParentesis()
                self.state = 261
                localctx._op_contenedor_returns = self.op_contenedor_returns()
                localctx.type = 'op_container'
                localctx.value = localctx._op_contenedor_returns.result
                compiler.RemoveParentesis()
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(VisionScriptParser.RETURN)
            self.state = 269
            self.match(VisionScriptParser.T__1)
            self.state = 270
            self.todo()
            compiler.GenerateFunReturns(compiler.returnFuncReturnAddress(compiler.currentFunction))
            self.state = 272
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
            self.state = 274
            localctx._function_type = self.function_type()
            self.state = 275
            self.match(VisionScriptParser.FUNCTION)
            self.state = 276
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.currentFunction = (None if localctx._ID is None else localctx._ID.text)
            compiler.FuncDeclaration(compiler.currentFunction,localctx._function_type.type)
            compiler.GenerateFunGoto()
            self.state = 280
            self.match(VisionScriptParser.T__1)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER))) != 0):
                self.state = 281
                localctx._tipo = self.tipo()
                self.state = 282
                localctx._ID = self.match(VisionScriptParser.ID)
                compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                compiler.ParamDeclaration(compiler.currentFunction,localctx._tipo.type)
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 285
                    self.match(VisionScriptParser.T__3)
                    self.state = 286
                    localctx._tipo = self.tipo()
                    self.state = 287
                    localctx._ID = self.match(VisionScriptParser.ID)
                    compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                    compiler.ParamDeclaration(compiler.currentFunction,localctx._tipo.type)
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 298
            self.match(VisionScriptParser.T__2)
            self.state = 299
            self.match(VisionScriptParser.BEGIN)
            self.state = 300
            self.func_bloque()
            self.state = 301
            self.match(VisionScriptParser.END)
            compiler.verifyReturn()
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
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER, VisionScriptParser.TEXT, VisionScriptParser.BOOL, VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                localctx._tipo = self.tipo()
                localctx.type = localctx._tipo.type
                pass
            elif token in [VisionScriptParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.RETURN) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 325
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 316
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 317
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 318
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 319
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 320
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 321
                    self.asignacion()
                    pass

                elif la_ == 7:
                    self.state = 322
                    self.op_contenedor()
                    pass

                elif la_ == 8:
                    self.state = 323
                    self.function_call()
                    pass

                elif la_ == 9:
                    self.state = 324
                    self.retorno()
                    pass


                self.state = 329
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
            self.state = 330
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.GenerateEra((None if localctx._ID is None else localctx._ID.text))
            localctx.value = compiler.returnFuncReturnAddress((None if localctx._ID is None else localctx._ID.text))
            localctx.type = compiler.returnFuncReturnType((None if localctx._ID is None else localctx._ID.text))
            self.state = 334
            self.match(VisionScriptParser.T__1)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 335
                self.casi_todo()
                compiler.GenerateParameter(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 337
                    self.match(VisionScriptParser.T__3)
                    self.state = 338
                    self.casi_todo()
                    compiler.GenerateParameter(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 348
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
            self.state = 351
            self.match(VisionScriptParser.T__4)
            compiler.GenerateEmptyContainer(compiler.currentFunction)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 353
                self.mega_expresion()
                compiler.GenerateFillContainer()
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 355
                    self.match(VisionScriptParser.T__3)
                    self.state = 356
                    self.mega_expresion()
                    compiler.GenerateFillContainer()
                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 366
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
            self.result = None
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
            self.state = 369
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 370
            self.match(VisionScriptParser.T__6)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.GET_BACK, VisionScriptParser.GET_FRONT, VisionScriptParser.LENGTH]:
                self.state = 377
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.GET_BACK]:
                    self.state = 371
                    localctx._GET_BACK = self.match(VisionScriptParser.GET_BACK)
                    localctx.flag = (None if localctx._GET_BACK is None else localctx._GET_BACK.text)
                    pass
                elif token in [VisionScriptParser.GET_FRONT]:
                    self.state = 373
                    localctx._GET_FRONT = self.match(VisionScriptParser.GET_FRONT)
                    localctx.flag = (None if localctx._GET_FRONT is None else localctx._GET_FRONT.text)
                    pass
                elif token in [VisionScriptParser.LENGTH]:
                    self.state = 375
                    localctx._LENGTH = self.match(VisionScriptParser.LENGTH)
                    localctx.flag = (None if localctx._LENGTH is None else localctx._LENGTH.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 379
                self.match(VisionScriptParser.T__1)
                self.state = 380
                self.match(VisionScriptParser.T__2)
                localctx.result = compiler.FuncionOPContainer1(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.currentFunction)
                pass
            elif token in [VisionScriptParser.GET]:
                self.state = 382
                localctx._GET = self.match(VisionScriptParser.GET)
                localctx.flag = (None if localctx._GET is None else localctx._GET.text)
                self.state = 384
                self.match(VisionScriptParser.T__1)
                self.state = 385
                self.mega_expresion()
                self.state = 386
                self.match(VisionScriptParser.T__2)
                localctx.result = compiler.FuncionOPContainer2(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.currentFunction)
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
            self._REPLACE = None # Token

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def mega_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Mega_expresionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,i)


        def INSERT_BACK(self):
            return self.getToken(VisionScriptParser.INSERT_BACK, 0)

        def INSERT_FRONT(self):
            return self.getToken(VisionScriptParser.INSERT_FRONT, 0)

        def INSERT(self):
            return self.getToken(VisionScriptParser.INSERT, 0)

        def REPLACE(self):
            return self.getToken(VisionScriptParser.REPLACE, 0)

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
            self.state = 391
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 392
            self.match(VisionScriptParser.T__6)
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.INSERT_BACK, VisionScriptParser.INSERT_FRONT]:
                self.state = 397
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.INSERT_BACK]:
                    self.state = 393
                    localctx._INSERT_BACK = self.match(VisionScriptParser.INSERT_BACK)
                    localctx.flag = (None if localctx._INSERT_BACK is None else localctx._INSERT_BACK.text)
                    pass
                elif token in [VisionScriptParser.INSERT_FRONT]:
                    self.state = 395
                    localctx._INSERT_FRONT = self.match(VisionScriptParser.INSERT_FRONT)
                    localctx.flag = (None if localctx._INSERT_FRONT is None else localctx._INSERT_FRONT.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 399
                self.match(VisionScriptParser.T__1)
                self.state = 400
                self.mega_expresion()
                self.state = 401
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer3(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.INSERT, VisionScriptParser.REPLACE]:
                self.state = 408
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.INSERT]:
                    self.state = 404
                    localctx._INSERT = self.match(VisionScriptParser.INSERT)
                    localctx.flag = (None if localctx._INSERT is None else localctx._INSERT.text)
                    pass
                elif token in [VisionScriptParser.REPLACE]:
                    self.state = 406
                    localctx._REPLACE = self.match(VisionScriptParser.REPLACE)
                    localctx.flag = (None if localctx._REPLACE is None else localctx._REPLACE.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 410
                self.match(VisionScriptParser.T__1)
                self.state = 411
                self.mega_expresion()
                self.state = 412
                self.match(VisionScriptParser.T__3)
                self.state = 413
                self.mega_expresion()
                self.state = 414
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
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.ID]:
                self.state = 419
                localctx._ID = self.match(VisionScriptParser.ID)
                compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.T__4]:
                self.state = 421
                self.contenedor()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 431 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 424
                self.match(VisionScriptParser.PLUS)
                self.state = 428
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.ID]:
                    self.state = 425
                    localctx._ID = self.match(VisionScriptParser.ID)
                    compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                    pass
                elif token in [VisionScriptParser.T__4]:
                    self.state = 427
                    self.contenedor()
                    pass
                else:
                    raise NoViableAltException(self)

                compiler.GenerateConcatContainer(compiler.currentFunction)
                self.state = 433 
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





