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
        buf.write("\u01a2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3K\n\3\f\3\16\3N\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5_\n\5\3\6\3\6\5\6c\n")
        buf.write("\6\3\7\3\7\3\7\3\7\5\7i\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\7\13\u008d\n\13\f\13\16\13\u0090\13\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009f")
        buf.write("\n\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00ac\n\16\3\16\3\16\3\16\7\16\u00b1\n\16\f\16\16")
        buf.write("\16\u00b4\13\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00bc")
        buf.write("\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c6")
        buf.write("\n\21\3\21\3\21\3\21\7\21\u00cb\n\21\f\21\16\21\u00ce")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d6\n\22\3")
        buf.write("\22\3\22\3\22\7\22\u00db\n\22\f\22\16\22\u00de\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e9")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fe")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0111\n\25\f")
        buf.write("\25\16\25\u0114\13\25\5\25\u0116\n\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u0120\n\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u012f\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u0139\n\27\f\27\16\27\u013c\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u0147\n\30\f\30\16\30")
        buf.write("\u014a\13\30\5\30\u014c\n\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u015a\n\31\f")
        buf.write("\31\16\31\u015d\13\31\5\31\u015f\n\31\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u016c\n\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u0178\n\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0180\n")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0190\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u0195\n\34\3\34\3\34\3\34\3\34\5\34\u019b\n\34\3\34")
        buf.write("\6\34\u019e\n\34\r\34\16\34\u019f\3\34\2\2\35\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66\2")
        buf.write("\3\4\2\27\30\60\63\2\u01c4\28\3\2\2\2\4L\3\2\2\2\6O\3")
        buf.write("\2\2\2\b^\3\2\2\2\nb\3\2\2\2\fh\3\2\2\2\16j\3\2\2\2\20")
        buf.write("p\3\2\2\2\22{\3\2\2\2\24\u008e\3\2\2\2\26\u0091\3\2\2")
        buf.write("\2\30\u009e\3\2\2\2\32\u00a5\3\2\2\2\34\u00b5\3\2\2\2")
        buf.write("\36\u00bd\3\2\2\2 \u00bf\3\2\2\2\"\u00cf\3\2\2\2$\u00e8")
        buf.write("\3\2\2\2&\u00fd\3\2\2\2(\u00ff\3\2\2\2*\u012e\3\2\2\2")
        buf.write(",\u013a\3\2\2\2.\u013d\3\2\2\2\60\u0151\3\2\2\2\62\u0163")
        buf.write("\3\2\2\2\64\u0179\3\2\2\2\66\u0194\3\2\2\289\b\2\1\29")
        buf.write(":\5\4\3\2:;\7\2\2\3;<\b\2\1\2<=\b\2\1\2=>\b\2\1\2>?\b")
        buf.write("\2\1\2?@\b\2\1\2@\3\3\2\2\2AK\5\6\4\2BK\5\20\t\2CK\5\22")
        buf.write("\n\2DK\5\26\f\2EK\5\30\r\2FK\5(\25\2GK\5.\30\2HK\5\16")
        buf.write("\b\2IK\5\64\33\2JA\3\2\2\2JB\3\2\2\2JC\3\2\2\2JD\3\2\2")
        buf.write("\2JE\3\2\2\2JF\3\2\2\2JG\3\2\2\2JH\3\2\2\2JI\3\2\2\2K")
        buf.write("N\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\5\3\2\2\2NL\3\2\2\2OP\5")
        buf.write("\b\5\2PQ\7)\2\2QR\7\3\2\2RS\5\n\6\2ST\b\4\1\2TU\b\4\1")
        buf.write("\2U\7\3\2\2\2VW\7\20\2\2W_\b\5\1\2XY\7\21\2\2Y_\b\5\1")
        buf.write("\2Z[\7\22\2\2[_\b\5\1\2\\]\7\31\2\2]_\b\5\1\2^V\3\2\2")
        buf.write("\2^X\3\2\2\2^Z\3\2\2\2^\\\3\2\2\2_\t\3\2\2\2`c\5\f\7\2")
        buf.write("ac\5.\30\2b`\3\2\2\2ba\3\2\2\2c\13\3\2\2\2di\5\32\16\2")
        buf.write("ei\5\66\34\2fi\5\60\31\2gi\5\62\32\2hd\3\2\2\2he\3\2\2")
        buf.write("\2hf\3\2\2\2hg\3\2\2\2i\r\3\2\2\2jk\7)\2\2kl\7\3\2\2l")
        buf.write("m\5\n\6\2mn\b\b\1\2no\b\b\1\2o\17\3\2\2\2pq\7\16\2\2q")
        buf.write("r\5\32\16\2rs\b\t\1\2st\7\32\2\2tu\5\24\13\2uv\7\17\2")
        buf.write("\2vw\b\t\1\2wx\5\24\13\2xy\7\33\2\2yz\b\t\1\2z\21\3\2")
        buf.write("\2\2{|\7\34\2\2|}\7\36\2\2}~\b\n\1\2~\177\5\32\16\2\177")
        buf.write("\u0080\b\n\1\2\u0080\u0081\7\32\2\2\u0081\u0082\5\24\13")
        buf.write("\2\u0082\u0083\7\33\2\2\u0083\u0084\b\n\1\2\u0084\23\3")
        buf.write("\2\2\2\u0085\u008d\5\20\t\2\u0086\u008d\5\22\n\2\u0087")
        buf.write("\u008d\5\26\f\2\u0088\u008d\5\30\r\2\u0089\u008d\5\16")
        buf.write("\b\2\u008a\u008d\5\64\33\2\u008b\u008d\5.\30\2\u008c\u0085")
        buf.write("\3\2\2\2\u008c\u0086\3\2\2\2\u008c\u0087\3\2\2\2\u008c")
        buf.write("\u0088\3\2\2\2\u008c\u0089\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3")
        buf.write("\2\2\2\u008e\u008f\3\2\2\2\u008f\25\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0092\7\n\2\2\u0092\u0093\7\4\2\2\u0093")
        buf.write("\u0094\7)\2\2\u0094\u0095\b\f\1\2\u0095\u0096\7\5\2\2")
        buf.write("\u0096\u0097\b\f\1\2\u0097\27\3\2\2\2\u0098\u0099\7\r")
        buf.write("\2\2\u0099\u009f\b\r\1\2\u009a\u009b\7\13\2\2\u009b\u009f")
        buf.write("\b\r\1\2\u009c\u009d\7\f\2\2\u009d\u009f\b\r\1\2\u009e")
        buf.write("\u0098\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\4\2\2\u00a1\u00a2\5")
        buf.write("\n\6\2\u00a2\u00a3\7\5\2\2\u00a3\u00a4\b\r\1\2\u00a4\31")
        buf.write("\3\2\2\2\u00a5\u00a6\5\34\17\2\u00a6\u00b2\b\16\1\2\u00a7")
        buf.write("\u00a8\7\25\2\2\u00a8\u00ac\b\16\1\2\u00a9\u00aa\7\26")
        buf.write("\2\2\u00aa\u00ac\b\16\1\2\u00ab\u00a7\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\5\34\17\2\u00ae")
        buf.write("\u00af\b\16\1\2\u00af\u00b1\3\2\2\2\u00b0\u00ab\3\2\2")
        buf.write("\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\33\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00bb")
        buf.write("\5 \21\2\u00b6\u00b7\5\36\20\2\u00b7\u00b8\b\17\1\2\u00b8")
        buf.write("\u00b9\5 \21\2\u00b9\u00ba\b\17\1\2\u00ba\u00bc\3\2\2")
        buf.write("\2\u00bb\u00b6\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\35\3")
        buf.write("\2\2\2\u00bd\u00be\t\2\2\2\u00be\37\3\2\2\2\u00bf\u00c0")
        buf.write("\5\"\22\2\u00c0\u00cc\b\21\1\2\u00c1\u00c2\7,\2\2\u00c2")
        buf.write("\u00c6\b\21\1\2\u00c3\u00c4\7-\2\2\u00c4\u00c6\b\21\1")
        buf.write("\2\u00c5\u00c1\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c8\5\"\22\2\u00c8\u00c9\b\21\1\2\u00c9")
        buf.write("\u00cb\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cb\u00ce\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd!\3\2\2")
        buf.write("\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\5$\23\2\u00d0\u00dc")
        buf.write("\b\22\1\2\u00d1\u00d2\7/\2\2\u00d2\u00d6\b\22\1\2\u00d3")
        buf.write("\u00d4\7.\2\2\u00d4\u00d6\b\22\1\2\u00d5\u00d1\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\5")
        buf.write("$\23\2\u00d8\u00d9\b\22\1\2\u00d9\u00db\3\2\2\2\u00da")
        buf.write("\u00d5\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd#\3\2\2\2\u00de\u00dc\3\2\2")
        buf.write("\2\u00df\u00e0\7\4\2\2\u00e0\u00e1\b\23\1\2\u00e1\u00e2")
        buf.write("\5\32\16\2\u00e2\u00e3\7\5\2\2\u00e3\u00e4\b\23\1\2\u00e4")
        buf.write("\u00e9\3\2\2\2\u00e5\u00e6\5&\24\2\u00e6\u00e7\b\23\1")
        buf.write("\2\u00e7\u00e9\3\2\2\2\u00e8\u00df\3\2\2\2\u00e8\u00e5")
        buf.write("\3\2\2\2\u00e9%\3\2\2\2\u00ea\u00eb\7-\2\2\u00eb\u00ec")
        buf.write("\7*\2\2\u00ec\u00ed\b\24\1\2\u00ed\u00fe\b\24\1\2\u00ee")
        buf.write("\u00ef\7*\2\2\u00ef\u00f0\b\24\1\2\u00f0\u00fe\b\24\1")
        buf.write("\2\u00f1\u00f2\7\23\2\2\u00f2\u00f3\b\24\1\2\u00f3\u00fe")
        buf.write("\b\24\1\2\u00f4\u00f5\7\24\2\2\u00f5\u00f6\b\24\1\2\u00f6")
        buf.write("\u00fe\b\24\1\2\u00f7\u00f8\7+\2\2\u00f8\u00f9\b\24\1")
        buf.write("\2\u00f9\u00fe\b\24\1\2\u00fa\u00fb\7)\2\2\u00fb\u00fc")
        buf.write("\b\24\1\2\u00fc\u00fe\b\24\1\2\u00fd\u00ea\3\2\2\2\u00fd")
        buf.write("\u00ee\3\2\2\2\u00fd\u00f1\3\2\2\2\u00fd\u00f4\3\2\2\2")
        buf.write("\u00fd\u00f7\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fe\'\3\2\2")
        buf.write("\2\u00ff\u0100\5*\26\2\u0100\u0101\7\37\2\2\u0101\u0102")
        buf.write("\7)\2\2\u0102\u0103\b\25\1\2\u0103\u0104\b\25\1\2\u0104")
        buf.write("\u0105\b\25\1\2\u0105\u0115\7\4\2\2\u0106\u0107\5\b\5")
        buf.write("\2\u0107\u0108\7)\2\2\u0108\u0109\b\25\1\2\u0109\u0112")
        buf.write("\b\25\1\2\u010a\u010b\7\6\2\2\u010b\u010c\5\b\5\2\u010c")
        buf.write("\u010d\7)\2\2\u010d\u010e\b\25\1\2\u010e\u010f\b\25\1")
        buf.write("\2\u010f\u0111\3\2\2\2\u0110\u010a\3\2\2\2\u0111\u0114")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0106\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7")
        buf.write("\5\2\2\u0118\u0119\7\32\2\2\u0119\u011a\5,\27\2\u011a")
        buf.write("\u011b\7 \2\2\u011b\u011f\7\4\2\2\u011c\u011d\5\f\7\2")
        buf.write("\u011d\u011e\b\25\1\2\u011e\u0120\3\2\2\2\u011f\u011c")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0122\7\5\2\2\u0122\u0123\7\33\2\2\u0123\u0124\b\25\1")
        buf.write("\2\u0124\u0125\b\25\1\2\u0125\u0126\b\25\1\2\u0126\u0127")
        buf.write("\b\25\1\2\u0127\u0128\b\25\1\2\u0128)\3\2\2\2\u0129\u012a")
        buf.write("\5\b\5\2\u012a\u012b\b\26\1\2\u012b\u012f\3\2\2\2\u012c")
        buf.write("\u012d\7\'\2\2\u012d\u012f\b\26\1\2\u012e\u0129\3\2\2")
        buf.write("\2\u012e\u012c\3\2\2\2\u012f+\3\2\2\2\u0130\u0139\5\6")
        buf.write("\4\2\u0131\u0139\5\20\t\2\u0132\u0139\5\22\n\2\u0133\u0139")
        buf.write("\5\26\f\2\u0134\u0139\5\30\r\2\u0135\u0139\5\16\b\2\u0136")
        buf.write("\u0139\5\64\33\2\u0137\u0139\5.\30\2\u0138\u0130\3\2\2")
        buf.write("\2\u0138\u0131\3\2\2\2\u0138\u0132\3\2\2\2\u0138\u0133")
        buf.write("\3\2\2\2\u0138\u0134\3\2\2\2\u0138\u0135\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0137\3\2\2\2\u0139\u013c\3\2\2\2")
        buf.write("\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b-\3\2\2")
        buf.write("\2\u013c\u013a\3\2\2\2\u013d\u013e\7)\2\2\u013e\u013f")
        buf.write("\b\30\1\2\u013f\u014b\7\4\2\2\u0140\u0141\5\f\7\2\u0141")
        buf.write("\u0148\b\30\1\2\u0142\u0143\7\6\2\2\u0143\u0144\5\f\7")
        buf.write("\2\u0144\u0145\b\30\1\2\u0145\u0147\3\2\2\2\u0146\u0142")
        buf.write("\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014b\u0140\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u014e\7\5\2\2\u014e\u014f\b\30\1\2\u014f")
        buf.write("\u0150\b\30\1\2\u0150/\3\2\2\2\u0151\u0152\7\7\2\2\u0152")
        buf.write("\u015e\b\31\1\2\u0153\u0154\5\32\16\2\u0154\u015b\b\31")
        buf.write("\1\2\u0155\u0156\7\6\2\2\u0156\u0157\5\32\16\2\u0157\u0158")
        buf.write("\b\31\1\2\u0158\u015a\3\2\2\2\u0159\u0155\3\2\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0153\3")
        buf.write("\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161")
        buf.write("\7\b\2\2\u0161\u0162\b\31\1\2\u0162\61\3\2\2\2\u0163\u0164")
        buf.write("\7)\2\2\u0164\u0177\7\t\2\2\u0165\u0166\7!\2\2\u0166\u016c")
        buf.write("\b\32\1\2\u0167\u0168\7\"\2\2\u0168\u016c\b\32\1\2\u0169")
        buf.write("\u016a\7(\2\2\u016a\u016c\b\32\1\2\u016b\u0165\3\2\2\2")
        buf.write("\u016b\u0167\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016e\7\4\2\2\u016e\u016f\7\5\2\2\u016f\u0178")
        buf.write("\b\32\1\2\u0170\u0171\7#\2\2\u0171\u0172\b\32\1\2\u0172")
        buf.write("\u0173\7\4\2\2\u0173\u0174\5\32\16\2\u0174\u0175\7\5\2")
        buf.write("\2\u0175\u0176\b\32\1\2\u0176\u0178\3\2\2\2\u0177\u016b")
        buf.write("\3\2\2\2\u0177\u0170\3\2\2\2\u0178\63\3\2\2\2\u0179\u017a")
        buf.write("\7)\2\2\u017a\u018f\7\t\2\2\u017b\u017c\7$\2\2\u017c\u0180")
        buf.write("\b\33\1\2\u017d\u017e\7%\2\2\u017e\u0180\b\33\1\2\u017f")
        buf.write("\u017b\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\7\4\2\2\u0182\u0183\5\32\16\2\u0183\u0184")
        buf.write("\7\5\2\2\u0184\u0185\b\33\1\2\u0185\u0190\3\2\2\2\u0186")
        buf.write("\u0187\7&\2\2\u0187\u0188\b\33\1\2\u0188\u0189\7\4\2\2")
        buf.write("\u0189\u018a\5\32\16\2\u018a\u018b\7\6\2\2\u018b\u018c")
        buf.write("\5\32\16\2\u018c\u018d\7\5\2\2\u018d\u018e\b\33\1\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u017f\3\2\2\2\u018f\u0186\3\2\2\2")
        buf.write("\u0190\65\3\2\2\2\u0191\u0192\7)\2\2\u0192\u0195\b\34")
        buf.write("\1\2\u0193\u0195\5\60\31\2\u0194\u0191\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195\u019d\3\2\2\2\u0196\u019a\7,\2\2\u0197")
        buf.write("\u0198\7)\2\2\u0198\u019b\b\34\1\2\u0199\u019b\5\60\31")
        buf.write("\2\u019a\u0197\3\2\2\2\u019a\u0199\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019e\b\34\1\2\u019d\u0196\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\67\3\2\2\2$JL^bh\u008c\u008e\u009e\u00ab\u00b2")
        buf.write("\u00bb\u00c5\u00cc\u00d5\u00dc\u00e8\u00fd\u0112\u0115")
        buf.write("\u011f\u012e\u0138\u013a\u0148\u014b\u015b\u015e\u016b")
        buf.write("\u0177\u017f\u018f\u0194\u019a\u019f")
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
    RULE_function = 19
    RULE_function_type = 20
    RULE_func_bloque = 21
    RULE_function_call = 22
    RULE_contenedor = 23
    RULE_op_contenedor_returns = 24
    RULE_op_contenedor = 25
    RULE_concat_contenedor = 26

    ruleNames =  [ "visionscript", "programa", "variable", "tipo", "todo", 
                   "casi_todo", "asignacion", "condicion", "ciclo", "bloque", 
                   "read", "imprimir", "mega_expresion", "expresion", "exp_todo", 
                   "exp", "termino", "factor", "ct", "function", "function_type", 
                   "func_bloque", "function_call", "contenedor", "op_contenedor_returns", 
                   "op_contenedor", "concat_contenedor" ]

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
            self.state = 55
            self.programa()
            self.state = 56
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
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.VOID) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 63
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 64
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 65
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 66
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 67
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 68
                    self.function()
                    pass

                elif la_ == 7:
                    self.state = 69
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 70
                    self.asignacion()
                    pass

                elif la_ == 9:
                    self.state = 71
                    self.op_contenedor()
                    pass


                self.state = 76
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
            self.state = 77
            localctx._tipo = self.tipo()
            self.state = 78
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 79
            self.match(VisionScriptParser.T__0)
            self.state = 80
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
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                localctx._NUMBER = self.match(VisionScriptParser.NUMBER)
                localctx.type = (None if localctx._NUMBER is None else localctx._NUMBER.text)
                pass
            elif token in [VisionScriptParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                localctx._TEXT = self.match(VisionScriptParser.TEXT)
                localctx.type = (None if localctx._TEXT is None else localctx._TEXT.text)
                pass
            elif token in [VisionScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                localctx._BOOL = self.match(VisionScriptParser.BOOL)
                localctx.type = (None if localctx._BOOL is None else localctx._BOOL.text)
                pass
            elif token in [VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.casi_todo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
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
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.mega_expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.concat_contenedor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.contenedor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
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
            self.state = 104
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 105
            self.match(VisionScriptParser.T__0)
            self.state = 106
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
            self.state = 110
            self.match(VisionScriptParser.IF)
            self.state = 111
            self.mega_expresion()
            compiler.FuncionIF1()
            self.state = 113
            self.match(VisionScriptParser.BEGIN)
            self.state = 114
            self.bloque()
            self.state = 115
            self.match(VisionScriptParser.ELSE)
            compiler.FuncionIF2()
            self.state = 117
            self.bloque()
            self.state = 118
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
            self.state = 121
            self.match(VisionScriptParser.REPEAT)
            self.state = 122
            self.match(VisionScriptParser.UNTIL)
            compiler.FuncionRepUntil1()
            self.state = 124
            self.mega_expresion()
            compiler.FuncionRepUntil2()
            self.state = 126
            self.match(VisionScriptParser.BEGIN)
            self.state = 127
            self.bloque()
            self.state = 128
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
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 138
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 131
                    self.condicion()
                    pass

                elif la_ == 2:
                    self.state = 132
                    self.ciclo()
                    pass

                elif la_ == 3:
                    self.state = 133
                    self.read()
                    pass

                elif la_ == 4:
                    self.state = 134
                    self.imprimir()
                    pass

                elif la_ == 5:
                    self.state = 135
                    self.asignacion()
                    pass

                elif la_ == 6:
                    self.state = 136
                    self.op_contenedor()
                    pass

                elif la_ == 7:
                    self.state = 137
                    self.function_call()
                    pass


                self.state = 142
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
            self.state = 143
            localctx._READ = self.match(VisionScriptParser.READ)
            self.state = 144
            self.match(VisionScriptParser.T__1)
            self.state = 145
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
            self.state = 147
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
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.BRAILLE]:
                self.state = 150
                localctx._BRAILLE = self.match(VisionScriptParser.BRAILLE)
                localctx.flag = (None if localctx._BRAILLE is None else localctx._BRAILLE.text)
                pass
            elif token in [VisionScriptParser.PRINT]:
                self.state = 152
                localctx._PRINT = self.match(VisionScriptParser.PRINT)
                localctx.flag = (None if localctx._PRINT is None else localctx._PRINT.text)
                pass
            elif token in [VisionScriptParser.HEAR]:
                self.state = 154
                localctx._HEAR = self.match(VisionScriptParser.HEAR)
                localctx.flag = (None if localctx._HEAR is None else localctx._HEAR.text)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 158
            self.match(VisionScriptParser.T__1)
            self.state = 159
            self.todo()
            self.state = 160
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
            self.state = 163
            self.expresion()
            compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.AND or _la==VisionScriptParser.OR:
                self.state = 169
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.AND]:
                    self.state = 165
                    localctx._AND = self.match(VisionScriptParser.AND)
                    compiler.InsertOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [VisionScriptParser.OR]:
                    self.state = 167
                    localctx._OR = self.match(VisionScriptParser.OR)
                    compiler.InsertOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 171
                self.expresion()
                compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
                self.state = 178
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
            self.state = 179
            self.exp()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0):
                self.state = 180
                localctx._exp_todo = self.exp_todo()
                compiler.InsertOperator((None if localctx._exp_todo is None else self._input.getText((localctx._exp_todo.start,localctx._exp_todo.stop))))
                self.state = 182
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
            self.state = 187
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
            self.state = 189
            self.termino()
            compiler.GenerateCuad('Termino',compiler.currentFunction)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.PLUS or _la==VisionScriptParser.MINUS:
                self.state = 195
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.PLUS]:
                    self.state = 191
                    localctx._PLUS = self.match(VisionScriptParser.PLUS)
                    compiler.InsertOperator((None if localctx._PLUS is None else localctx._PLUS.text))
                    pass
                elif token in [VisionScriptParser.MINUS]:
                    self.state = 193
                    localctx._MINUS = self.match(VisionScriptParser.MINUS)
                    compiler.InsertOperator((None if localctx._MINUS is None else localctx._MINUS.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 197
                self.termino()
                compiler.GenerateCuad('Termino',compiler.currentFunction)
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
            self.state = 205
            self.factor()
            compiler.GenerateCuad('Factor',compiler.currentFunction)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.DIVISION or _la==VisionScriptParser.MULTIPLICATION:
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.MULTIPLICATION]:
                    self.state = 207
                    localctx._MULTIPLICATION = self.match(VisionScriptParser.MULTIPLICATION)
                    compiler.InsertOperator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [VisionScriptParser.DIVISION]:
                    self.state = 209
                    localctx._DIVISION = self.match(VisionScriptParser.DIVISION)
                    compiler.InsertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self.factor()
                compiler.GenerateCuad('Factor',compiler.currentFunction)
                self.state = 220
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
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(VisionScriptParser.T__1)
                compiler.InsertParentesis()
                self.state = 223
                self.mega_expresion()
                self.state = 224
                self.match(VisionScriptParser.T__2)
                compiler.RemoveParentesis()
                pass
            elif token in [VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(VisionScriptParser.MINUS)
                self.state = 233
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = compiler.ConstDeclaration(localctx.type , '-'+(None if localctx._CTN is None else localctx._CTN.text) )
                pass
            elif token in [VisionScriptParser.CTN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTN is None else localctx._CTN.text) )
                pass
            elif token in [VisionScriptParser.CTBF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                localctx._CTBF = self.match(VisionScriptParser.CTBF)
                localctx.type = 'bool'
                localctx.value = compiler.ConstDeclaration(localctx.type ,(None if localctx._CTBF is None else localctx._CTBF.text) )
                pass
            elif token in [VisionScriptParser.CTBT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                localctx._CTBT = self.match(VisionScriptParser.CTBT)
                localctx.type = 'bool'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTBT is None else localctx._CTBT.text) )
                pass
            elif token in [VisionScriptParser.CTT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
                localctx._CTT = self.match(VisionScriptParser.CTT)
                localctx.type = 'text'
                localctx.value = compiler.ConstDeclaration(localctx.type , (None if localctx._CTT is None else localctx._CTT.text) )
                pass
            elif token in [VisionScriptParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                localctx._ID = self.match(VisionScriptParser.ID)
                localctx.type = compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text))
                localctx.value = compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text))
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


        def RETURN(self):
            return self.getToken(VisionScriptParser.RETURN, 0)

        def END(self):
            return self.getToken(VisionScriptParser.END, 0)

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.TipoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.TipoContext,i)


        def casi_todo(self):
            return self.getTypedRuleContext(VisionScriptParser.Casi_todoContext,0)


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
        self.enterRule(localctx, 38, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            localctx._function_type = self.function_type()
            self.state = 254
            self.match(VisionScriptParser.FUNCTION)
            self.state = 255
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.GenerateFunGoto()
            compiler.currentFunction = (None if localctx._ID is None else localctx._ID.text)
            compiler.FuncDeclaration(compiler.currentFunction,localctx._function_type.type)
            self.state = 259
            self.match(VisionScriptParser.T__1)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER))) != 0):
                self.state = 260
                localctx._tipo = self.tipo()
                self.state = 261
                localctx._ID = self.match(VisionScriptParser.ID)
                compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                compiler.ParamDeclaration(compiler.currentFunction,localctx._tipo.type)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 264
                    self.match(VisionScriptParser.T__3)
                    self.state = 265
                    localctx._tipo = self.tipo()
                    self.state = 266
                    localctx._ID = self.match(VisionScriptParser.ID)
                    compiler.VarDeclaration(compiler.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                    compiler.ParamDeclaration(compiler.currentFunction,localctx._tipo.type)
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 277
            self.match(VisionScriptParser.T__2)
            self.state = 278
            self.match(VisionScriptParser.BEGIN)
            self.state = 279
            self.func_bloque()
            self.state = 280
            self.match(VisionScriptParser.RETURN)
            self.state = 281
            self.match(VisionScriptParser.T__1)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 282
                self.casi_todo()
                compiler.GenerateFunReturns(localctx._function_type.type,compiler.returnFuncReturnAddress(compiler.currentFunction))


            self.state = 287
            self.match(VisionScriptParser.T__2)
            self.state = 288
            self.match(VisionScriptParser.END)
            compiler.FillFunGoto()
            compiler.RegisterLocalCont(compiler.currentFunction)
            compiler.GenerateEndProc()
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
        self.enterRule(localctx, 40, self.RULE_function_type)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER, VisionScriptParser.TEXT, VisionScriptParser.BOOL, VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                localctx._tipo = self.tipo()
                localctx.type = localctx._tipo.type
                pass
            elif token in [VisionScriptParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
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
        self.enterRule(localctx, 42, self.RULE_func_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 310
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 302
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 303
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 304
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 305
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 306
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 307
                    self.asignacion()
                    pass

                elif la_ == 7:
                    self.state = 308
                    self.op_contenedor()
                    pass

                elif la_ == 8:
                    self.state = 309
                    self.function_call()
                    pass


                self.state = 314
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
        self.enterRule(localctx, 44, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            localctx._ID = self.match(VisionScriptParser.ID)
            compiler.GenerateEra((None if localctx._ID is None else localctx._ID.text))
            self.state = 317
            self.match(VisionScriptParser.T__1)
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 318
                self.casi_todo()
                compiler.GenerateParameter(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 320
                    self.match(VisionScriptParser.T__3)
                    self.state = 321
                    self.casi_todo()
                    compiler.GenerateParameter(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                    self.state = 328
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 331
            self.match(VisionScriptParser.T__2)
            compiler.VerifyParameters(compiler.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
            compiler.addValueToStack(compiler.returnFuncReturnAddress((None if localctx._ID is None else localctx._ID.text)),compiler.returnFuncReturnType((None if localctx._ID is None else localctx._ID.text)))
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
        self.enterRule(localctx, 46, self.RULE_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(VisionScriptParser.T__4)
            compiler.GenerateEmptyContainer(compiler.currentFunction)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 337
                self.mega_expresion()
                compiler.GenerateFillContainer()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 339
                    self.match(VisionScriptParser.T__3)
                    self.state = 340
                    self.mega_expresion()
                    compiler.GenerateFillContainer()
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 350
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
        self.enterRule(localctx, 48, self.RULE_op_contenedor_returns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 354
            self.match(VisionScriptParser.T__6)
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.GET_BACK, VisionScriptParser.GET_FRONT, VisionScriptParser.LENGTH]:
                self.state = 361
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.GET_BACK]:
                    self.state = 355
                    localctx._GET_BACK = self.match(VisionScriptParser.GET_BACK)
                    localctx.flag = (None if localctx._GET_BACK is None else localctx._GET_BACK.text)
                    pass
                elif token in [VisionScriptParser.GET_FRONT]:
                    self.state = 357
                    localctx._GET_FRONT = self.match(VisionScriptParser.GET_FRONT)
                    localctx.flag = (None if localctx._GET_FRONT is None else localctx._GET_FRONT.text)
                    pass
                elif token in [VisionScriptParser.LENGTH]:
                    self.state = 359
                    localctx._LENGTH = self.match(VisionScriptParser.LENGTH)
                    localctx.flag = (None if localctx._LENGTH is None else localctx._LENGTH.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 363
                self.match(VisionScriptParser.T__1)
                self.state = 364
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer1(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.currentFunction)
                pass
            elif token in [VisionScriptParser.GET]:
                self.state = 366
                localctx._GET = self.match(VisionScriptParser.GET)
                localctx.flag = (None if localctx._GET is None else localctx._GET.text)
                self.state = 368
                self.match(VisionScriptParser.T__1)
                self.state = 369
                self.mega_expresion()
                self.state = 370
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
        self.enterRule(localctx, 50, self.RULE_op_contenedor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 376
            self.match(VisionScriptParser.T__6)
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.INSERT_BACK, VisionScriptParser.INSERT_FRONT]:
                self.state = 381
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.INSERT_BACK]:
                    self.state = 377
                    localctx._INSERT_BACK = self.match(VisionScriptParser.INSERT_BACK)
                    localctx.flag = (None if localctx._INSERT_BACK is None else localctx._INSERT_BACK.text)
                    pass
                elif token in [VisionScriptParser.INSERT_FRONT]:
                    self.state = 379
                    localctx._INSERT_FRONT = self.match(VisionScriptParser.INSERT_FRONT)
                    localctx.flag = (None if localctx._INSERT_FRONT is None else localctx._INSERT_FRONT.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 383
                self.match(VisionScriptParser.T__1)
                self.state = 384
                self.mega_expresion()
                self.state = 385
                self.match(VisionScriptParser.T__2)
                compiler.FuncionOPContainer3(localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.INSERT]:
                self.state = 388
                localctx._INSERT = self.match(VisionScriptParser.INSERT)
                localctx.flag = (None if localctx._INSERT is None else localctx._INSERT.text)
                self.state = 390
                self.match(VisionScriptParser.T__1)
                self.state = 391
                self.mega_expresion()
                self.state = 392
                self.match(VisionScriptParser.T__3)
                self.state = 393
                self.mega_expresion()
                self.state = 394
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
        self.enterRule(localctx, 52, self.RULE_concat_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.ID]:
                self.state = 399
                localctx._ID = self.match(VisionScriptParser.ID)
                compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.T__4]:
                self.state = 401
                self.contenedor()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 411 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 404
                self.match(VisionScriptParser.PLUS)
                self.state = 408
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.ID]:
                    self.state = 405
                    localctx._ID = self.match(VisionScriptParser.ID)
                    compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)),compiler.returnIDType(compiler.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                    pass
                elif token in [VisionScriptParser.T__4]:
                    self.state = 407
                    self.contenedor()
                    pass
                else:
                    raise NoViableAltException(self)

                compiler.GenerateConcatContainer(compiler.currentFunction)
                self.state = 413 
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





