# Generated from VisionScript.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from VisionScriptCompiler import FunctionDirectory
from Cuadruplos import Cuadruplos
from VirtualMachine import VirtualMachine
func_dir = FunctionDirectory()
cuadruplos = Cuadruplos() 
vm = VirtualMachine()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u019e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write("J\n\3\f\3\16\3M\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5^\n\5\3\6\3\6\5\6b\n\6\3")
        buf.write("\7\3\7\3\7\3\7\5\7h\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u008c\n\13\f\13\16\13\u008f\13\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009e\n")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00ab\n\16\3\16\3\16\3\16\7\16\u00b0\n\16\f\16\16")
        buf.write("\16\u00b3\13\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00bb")
        buf.write("\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c5")
        buf.write("\n\21\3\21\3\21\3\21\7\21\u00ca\n\21\f\21\16\21\u00cd")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d5\n\22\3")
        buf.write("\22\3\22\3\22\7\22\u00da\n\22\f\22\16\22\u00dd\13\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e8")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fd")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0110\n\25\f")
        buf.write("\25\16\25\u0113\13\25\5\25\u0115\n\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u011f\n\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u012c\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0136")
        buf.write("\n\27\f\27\16\27\u0139\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u0144\n\30\f\30\16\30\u0147")
        buf.write("\13\30\5\30\u0149\n\30\3\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\7\31\u0156\n\31\f\31\16\31\u0159")
        buf.write("\13\31\5\31\u015b\n\31\3\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\5\32\u0168\n\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0174\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\5\33\u017c\n\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u018c\n\33\3\34\3\34\3\34\5\34\u0191\n\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u0197\n\34\3\34\6\34\u019a\n\34")
        buf.write("\r\34\16\34\u019b\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\66\2\3\4\2\27\30\60")
        buf.write("\63\2\u01c0\28\3\2\2\2\4K\3\2\2\2\6N\3\2\2\2\b]\3\2\2")
        buf.write("\2\na\3\2\2\2\fg\3\2\2\2\16i\3\2\2\2\20o\3\2\2\2\22z\3")
        buf.write("\2\2\2\24\u008d\3\2\2\2\26\u0090\3\2\2\2\30\u009d\3\2")
        buf.write("\2\2\32\u00a4\3\2\2\2\34\u00b4\3\2\2\2\36\u00bc\3\2\2")
        buf.write("\2 \u00be\3\2\2\2\"\u00ce\3\2\2\2$\u00e7\3\2\2\2&\u00fc")
        buf.write("\3\2\2\2(\u00fe\3\2\2\2*\u012b\3\2\2\2,\u0137\3\2\2\2")
        buf.write(".\u013a\3\2\2\2\60\u014d\3\2\2\2\62\u015f\3\2\2\2\64\u0175")
        buf.write("\3\2\2\2\66\u0190\3\2\2\289\b\2\1\29:\5\4\3\2:;\7\2\2")
        buf.write("\3;<\b\2\1\2<=\b\2\1\2=>\b\2\1\2>?\b\2\1\2?\3\3\2\2\2")
        buf.write("@J\5\6\4\2AJ\5\20\t\2BJ\5\22\n\2CJ\5\26\f\2DJ\5\30\r\2")
        buf.write("EJ\5(\25\2FJ\5.\30\2GJ\5\16\b\2HJ\5\64\33\2I@\3\2\2\2")
        buf.write("IA\3\2\2\2IB\3\2\2\2IC\3\2\2\2ID\3\2\2\2IE\3\2\2\2IF\3")
        buf.write("\2\2\2IG\3\2\2\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2")
        buf.write("\2L\5\3\2\2\2MK\3\2\2\2NO\5\b\5\2OP\7)\2\2PQ\7\3\2\2Q")
        buf.write("R\5\n\6\2RS\b\4\1\2ST\b\4\1\2T\7\3\2\2\2UV\7\20\2\2V^")
        buf.write("\b\5\1\2WX\7\21\2\2X^\b\5\1\2YZ\7\22\2\2Z^\b\5\1\2[\\")
        buf.write("\7\31\2\2\\^\b\5\1\2]U\3\2\2\2]W\3\2\2\2]Y\3\2\2\2][\3")
        buf.write("\2\2\2^\t\3\2\2\2_b\5\f\7\2`b\5.\30\2a_\3\2\2\2a`\3\2")
        buf.write("\2\2b\13\3\2\2\2ch\5\32\16\2dh\5\66\34\2eh\5\60\31\2f")
        buf.write("h\5\62\32\2gc\3\2\2\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2h\r")
        buf.write("\3\2\2\2ij\7)\2\2jk\7\3\2\2kl\5\n\6\2lm\b\b\1\2mn\b\b")
        buf.write("\1\2n\17\3\2\2\2op\7\16\2\2pq\5\32\16\2qr\b\t\1\2rs\7")
        buf.write("\32\2\2st\5\24\13\2tu\7\17\2\2uv\b\t\1\2vw\5\24\13\2w")
        buf.write("x\7\33\2\2xy\b\t\1\2y\21\3\2\2\2z{\7\34\2\2{|\7\36\2\2")
        buf.write("|}\b\n\1\2}~\5\32\16\2~\177\b\n\1\2\177\u0080\7\32\2\2")
        buf.write("\u0080\u0081\5\24\13\2\u0081\u0082\7\33\2\2\u0082\u0083")
        buf.write("\b\n\1\2\u0083\23\3\2\2\2\u0084\u008c\5\20\t\2\u0085\u008c")
        buf.write("\5\22\n\2\u0086\u008c\5\26\f\2\u0087\u008c\5\30\r\2\u0088")
        buf.write("\u008c\5\16\b\2\u0089\u008c\5\64\33\2\u008a\u008c\5.\30")
        buf.write("\2\u008b\u0084\3\2\2\2\u008b\u0085\3\2\2\2\u008b\u0086")
        buf.write("\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0088\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\25\3\2")
        buf.write("\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7\n\2\2\u0091\u0092")
        buf.write("\7\4\2\2\u0092\u0093\7)\2\2\u0093\u0094\b\f\1\2\u0094")
        buf.write("\u0095\7\5\2\2\u0095\u0096\b\f\1\2\u0096\27\3\2\2\2\u0097")
        buf.write("\u0098\7\r\2\2\u0098\u009e\b\r\1\2\u0099\u009a\7\13\2")
        buf.write("\2\u009a\u009e\b\r\1\2\u009b\u009c\7\f\2\2\u009c\u009e")
        buf.write("\b\r\1\2\u009d\u0097\3\2\2\2\u009d\u0099\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7\4\2\2")
        buf.write("\u00a0\u00a1\5\n\6\2\u00a1\u00a2\7\5\2\2\u00a2\u00a3\b")
        buf.write("\r\1\2\u00a3\31\3\2\2\2\u00a4\u00a5\5\34\17\2\u00a5\u00b1")
        buf.write("\b\16\1\2\u00a6\u00a7\7\25\2\2\u00a7\u00ab\b\16\1\2\u00a8")
        buf.write("\u00a9\7\26\2\2\u00a9\u00ab\b\16\1\2\u00aa\u00a6\3\2\2")
        buf.write("\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad")
        buf.write("\5\34\17\2\u00ad\u00ae\b\16\1\2\u00ae\u00b0\3\2\2\2\u00af")
        buf.write("\u00aa\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\33\3\2\2\2\u00b3\u00b1\3\2")
        buf.write("\2\2\u00b4\u00ba\5 \21\2\u00b5\u00b6\5\36\20\2\u00b6\u00b7")
        buf.write("\b\17\1\2\u00b7\u00b8\5 \21\2\u00b8\u00b9\b\17\1\2\u00b9")
        buf.write("\u00bb\3\2\2\2\u00ba\u00b5\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\35\3\2\2\2\u00bc\u00bd\t\2\2\2\u00bd\37\3\2\2\2")
        buf.write("\u00be\u00bf\5\"\22\2\u00bf\u00cb\b\21\1\2\u00c0\u00c1")
        buf.write("\7,\2\2\u00c1\u00c5\b\21\1\2\u00c2\u00c3\7-\2\2\u00c3")
        buf.write("\u00c5\b\21\1\2\u00c4\u00c0\3\2\2\2\u00c4\u00c2\3\2\2")
        buf.write("\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\5\"\22\2\u00c7\u00c8")
        buf.write("\b\21\1\2\u00c8\u00ca\3\2\2\2\u00c9\u00c4\3\2\2\2\u00ca")
        buf.write("\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2")
        buf.write("\u00cc!\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00cf\5$\23")
        buf.write("\2\u00cf\u00db\b\22\1\2\u00d0\u00d1\7/\2\2\u00d1\u00d5")
        buf.write("\b\22\1\2\u00d2\u00d3\7.\2\2\u00d3\u00d5\b\22\1\2\u00d4")
        buf.write("\u00d0\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d7\5$\23\2\u00d7\u00d8\b\22\1\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d4\3\2\2\2\u00da\u00dd\3\2\2\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc#\3\2\2\2\u00dd")
        buf.write("\u00db\3\2\2\2\u00de\u00df\7\4\2\2\u00df\u00e0\b\23\1")
        buf.write("\2\u00e0\u00e1\5\32\16\2\u00e1\u00e2\7\5\2\2\u00e2\u00e3")
        buf.write("\b\23\1\2\u00e3\u00e8\3\2\2\2\u00e4\u00e5\5&\24\2\u00e5")
        buf.write("\u00e6\b\23\1\2\u00e6\u00e8\3\2\2\2\u00e7\u00de\3\2\2")
        buf.write("\2\u00e7\u00e4\3\2\2\2\u00e8%\3\2\2\2\u00e9\u00ea\7-\2")
        buf.write("\2\u00ea\u00eb\7*\2\2\u00eb\u00ec\b\24\1\2\u00ec\u00fd")
        buf.write("\b\24\1\2\u00ed\u00ee\7*\2\2\u00ee\u00ef\b\24\1\2\u00ef")
        buf.write("\u00fd\b\24\1\2\u00f0\u00f1\7\23\2\2\u00f1\u00f2\b\24")
        buf.write("\1\2\u00f2\u00fd\b\24\1\2\u00f3\u00f4\7\24\2\2\u00f4\u00f5")
        buf.write("\b\24\1\2\u00f5\u00fd\b\24\1\2\u00f6\u00f7\7+\2\2\u00f7")
        buf.write("\u00f8\b\24\1\2\u00f8\u00fd\b\24\1\2\u00f9\u00fa\7)\2")
        buf.write("\2\u00fa\u00fb\b\24\1\2\u00fb\u00fd\b\24\1\2\u00fc\u00e9")
        buf.write("\3\2\2\2\u00fc\u00ed\3\2\2\2\u00fc\u00f0\3\2\2\2\u00fc")
        buf.write("\u00f3\3\2\2\2\u00fc\u00f6\3\2\2\2\u00fc\u00f9\3\2\2\2")
        buf.write("\u00fd\'\3\2\2\2\u00fe\u00ff\5*\26\2\u00ff\u0100\7\37")
        buf.write("\2\2\u0100\u0101\7)\2\2\u0101\u0102\b\25\1\2\u0102\u0103")
        buf.write("\b\25\1\2\u0103\u0104\b\25\1\2\u0104\u0114\7\4\2\2\u0105")
        buf.write("\u0106\5\b\5\2\u0106\u0107\7)\2\2\u0107\u0108\b\25\1\2")
        buf.write("\u0108\u0111\b\25\1\2\u0109\u010a\7\6\2\2\u010a\u010b")
        buf.write("\5\b\5\2\u010b\u010c\7)\2\2\u010c\u010d\b\25\1\2\u010d")
        buf.write("\u010e\b\25\1\2\u010e\u0110\3\2\2\2\u010f\u0109\3\2\2")
        buf.write("\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0114")
        buf.write("\u0105\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0117\7\5\2\2\u0117\u0118\7\32\2\2\u0118\u0119")
        buf.write("\5,\27\2\u0119\u011a\7 \2\2\u011a\u011e\7\4\2\2\u011b")
        buf.write("\u011c\5\f\7\2\u011c\u011d\b\25\1\2\u011d\u011f\3\2\2")
        buf.write("\2\u011e\u011b\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0121\7\5\2\2\u0121\u0122\7\33\2\2\u0122")
        buf.write("\u0123\b\25\1\2\u0123\u0124\b\25\1\2\u0124\u0125\b\25")
        buf.write("\1\2\u0125)\3\2\2\2\u0126\u0127\5\b\5\2\u0127\u0128\b")
        buf.write("\26\1\2\u0128\u012c\3\2\2\2\u0129\u012a\7\'\2\2\u012a")
        buf.write("\u012c\b\26\1\2\u012b\u0126\3\2\2\2\u012b\u0129\3\2\2")
        buf.write("\2\u012c+\3\2\2\2\u012d\u0136\5\6\4\2\u012e\u0136\5\20")
        buf.write("\t\2\u012f\u0136\5\22\n\2\u0130\u0136\5\26\f\2\u0131\u0136")
        buf.write("\5\30\r\2\u0132\u0136\5\16\b\2\u0133\u0136\5\64\33\2\u0134")
        buf.write("\u0136\5.\30\2\u0135\u012d\3\2\2\2\u0135\u012e\3\2\2\2")
        buf.write("\u0135\u012f\3\2\2\2\u0135\u0130\3\2\2\2\u0135\u0131\3")
        buf.write("\2\2\2\u0135\u0132\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0134")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138-\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013b\7)\2\2\u013b\u013c\b\30\1\2\u013c\u0148\7\4\2\2")
        buf.write("\u013d\u013e\5\f\7\2\u013e\u0145\b\30\1\2\u013f\u0140")
        buf.write("\7\6\2\2\u0140\u0141\5\f\7\2\u0141\u0142\b\30\1\2\u0142")
        buf.write("\u0144\3\2\2\2\u0143\u013f\3\2\2\2\u0144\u0147\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0149\3")
        buf.write("\2\2\2\u0147\u0145\3\2\2\2\u0148\u013d\3\2\2\2\u0148\u0149")
        buf.write("\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\7\5\2\2\u014b")
        buf.write("\u014c\b\30\1\2\u014c/\3\2\2\2\u014d\u014e\7\7\2\2\u014e")
        buf.write("\u015a\b\31\1\2\u014f\u0150\5\32\16\2\u0150\u0157\b\31")
        buf.write("\1\2\u0151\u0152\7\6\2\2\u0152\u0153\5\32\16\2\u0153\u0154")
        buf.write("\b\31\1\2\u0154\u0156\3\2\2\2\u0155\u0151\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u014f\3")
        buf.write("\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d")
        buf.write("\7\b\2\2\u015d\u015e\b\31\1\2\u015e\61\3\2\2\2\u015f\u0160")
        buf.write("\7)\2\2\u0160\u0173\7\t\2\2\u0161\u0162\7!\2\2\u0162\u0168")
        buf.write("\b\32\1\2\u0163\u0164\7\"\2\2\u0164\u0168\b\32\1\2\u0165")
        buf.write("\u0166\7(\2\2\u0166\u0168\b\32\1\2\u0167\u0161\3\2\2\2")
        buf.write("\u0167\u0163\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169\u016a\7\4\2\2\u016a\u016b\7\5\2\2\u016b\u0174")
        buf.write("\b\32\1\2\u016c\u016d\7#\2\2\u016d\u016e\b\32\1\2\u016e")
        buf.write("\u016f\7\4\2\2\u016f\u0170\5\32\16\2\u0170\u0171\7\5\2")
        buf.write("\2\u0171\u0172\b\32\1\2\u0172\u0174\3\2\2\2\u0173\u0167")
        buf.write("\3\2\2\2\u0173\u016c\3\2\2\2\u0174\63\3\2\2\2\u0175\u0176")
        buf.write("\7)\2\2\u0176\u018b\7\t\2\2\u0177\u0178\7$\2\2\u0178\u017c")
        buf.write("\b\33\1\2\u0179\u017a\7%\2\2\u017a\u017c\b\33\1\2\u017b")
        buf.write("\u0177\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017e\7\4\2\2\u017e\u017f\5\32\16\2\u017f\u0180")
        buf.write("\7\5\2\2\u0180\u0181\b\33\1\2\u0181\u018c\3\2\2\2\u0182")
        buf.write("\u0183\7&\2\2\u0183\u0184\b\33\1\2\u0184\u0185\7\4\2\2")
        buf.write("\u0185\u0186\5\32\16\2\u0186\u0187\7\6\2\2\u0187\u0188")
        buf.write("\5\32\16\2\u0188\u0189\7\5\2\2\u0189\u018a\b\33\1\2\u018a")
        buf.write("\u018c\3\2\2\2\u018b\u017b\3\2\2\2\u018b\u0182\3\2\2\2")
        buf.write("\u018c\65\3\2\2\2\u018d\u018e\7)\2\2\u018e\u0191\b\34")
        buf.write("\1\2\u018f\u0191\5\60\31\2\u0190\u018d\3\2\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0199\3\2\2\2\u0192\u0196\7,\2\2\u0193")
        buf.write("\u0194\7)\2\2\u0194\u0197\b\34\1\2\u0195\u0197\5\60\31")
        buf.write("\2\u0196\u0193\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u019a\b\34\1\2\u0199\u0192\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019c\67\3\2\2\2$IK]ag\u008b\u008d\u009d\u00aa\u00b1")
        buf.write("\u00ba\u00c4\u00cb\u00d4\u00db\u00e7\u00fc\u0111\u0114")
        buf.write("\u011e\u012b\u0135\u0137\u0145\u0148\u0157\u015a\u0167")
        buf.write("\u0173\u017b\u018b\u0190\u0196\u019b")
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
            func_dir.FuncDeclaration('@global','void')
            self.state = 55
            self.programa()
            self.state = 56
            self.match(VisionScriptParser.EOF)
            cuadruplos.printCuad()
            func_dir.showFunctionDirectory()
            vm.Cuadruplos = cuadruplos.ReturnCuads()
            vm.PrintCuadruplos()
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
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.VOID) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 71
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 63
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 64
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 65
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 66
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 67
                    self.function()
                    pass

                elif la_ == 7:
                    self.state = 68
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 69
                    self.asignacion()
                    pass

                elif la_ == 9:
                    self.state = 70
                    self.op_contenedor()
                    pass


                self.state = 75
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
            self.state = 76
            localctx._tipo = self.tipo()
            self.state = 77
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 78
            self.match(VisionScriptParser.T__0)
            self.state = 79
            localctx._todo = self.todo()
            func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
            cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text)), func_dir.returnIDType(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
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
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                localctx._NUMBER = self.match(VisionScriptParser.NUMBER)
                localctx.type = (None if localctx._NUMBER is None else localctx._NUMBER.text)
                pass
            elif token in [VisionScriptParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                localctx._TEXT = self.match(VisionScriptParser.TEXT)
                localctx.type = (None if localctx._TEXT is None else localctx._TEXT.text)
                pass
            elif token in [VisionScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                localctx._BOOL = self.match(VisionScriptParser.BOOL)
                localctx.type = (None if localctx._BOOL is None else localctx._BOOL.text)
                pass
            elif token in [VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.casi_todo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
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
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.mega_expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.concat_contenedor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.contenedor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 100
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
            self.state = 103
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 104
            self.match(VisionScriptParser.T__0)
            self.state = 105
            localctx._todo = self.todo()
            func_dir.VarAssignment(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
            cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text)), func_dir.returnIDType(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
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
            self.state = 109
            self.match(VisionScriptParser.IF)
            self.state = 110
            self.mega_expresion()
            cuadruplos.FuncionIF1()
            self.state = 112
            self.match(VisionScriptParser.BEGIN)
            self.state = 113
            self.bloque()
            self.state = 114
            self.match(VisionScriptParser.ELSE)
            cuadruplos.FuncionIF2()
            self.state = 116
            self.bloque()
            self.state = 117
            self.match(VisionScriptParser.END)
            cuadruplos.FuncionIF3()
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
            self.state = 120
            self.match(VisionScriptParser.REPEAT)
            self.state = 121
            self.match(VisionScriptParser.UNTIL)
            cuadruplos.FuncionRepUntil1()
            self.state = 123
            self.mega_expresion()
            cuadruplos.FuncionRepUntil2()
            self.state = 125
            self.match(VisionScriptParser.BEGIN)
            self.state = 126
            self.bloque()
            self.state = 127
            self.match(VisionScriptParser.END)
            cuadruplos.FuncionRepUntil3()
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
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 137
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 130
                    self.condicion()
                    pass

                elif la_ == 2:
                    self.state = 131
                    self.ciclo()
                    pass

                elif la_ == 3:
                    self.state = 132
                    self.read()
                    pass

                elif la_ == 4:
                    self.state = 133
                    self.imprimir()
                    pass

                elif la_ == 5:
                    self.state = 134
                    self.asignacion()
                    pass

                elif la_ == 6:
                    self.state = 135
                    self.op_contenedor()
                    pass

                elif la_ == 7:
                    self.state = 136
                    self.function_call()
                    pass


                self.state = 141
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
            self.state = 142
            localctx._READ = self.match(VisionScriptParser.READ)
            self.state = 143
            self.match(VisionScriptParser.T__1)
            self.state = 144
            localctx._ID = self.match(VisionScriptParser.ID)
            cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)),func_dir.returnIDType(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
            self.state = 146
            self.match(VisionScriptParser.T__2)
            cuadruplos.GenerateReadCuad((None if localctx._READ is None else localctx._READ.text),func_dir.returnIDType(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
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
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.BRAILLE]:
                self.state = 149
                localctx._BRAILLE = self.match(VisionScriptParser.BRAILLE)
                localctx.flag = (None if localctx._BRAILLE is None else localctx._BRAILLE.text)
                pass
            elif token in [VisionScriptParser.PRINT]:
                self.state = 151
                localctx._PRINT = self.match(VisionScriptParser.PRINT)
                localctx.flag = (None if localctx._PRINT is None else localctx._PRINT.text)
                pass
            elif token in [VisionScriptParser.HEAR]:
                self.state = 153
                localctx._HEAR = self.match(VisionScriptParser.HEAR)
                localctx.flag = (None if localctx._HEAR is None else localctx._HEAR.text)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self.match(VisionScriptParser.T__1)
            self.state = 158
            self.todo()
            self.state = 159
            self.match(VisionScriptParser.T__2)
            cuadruplos.GeneratePrintCuad(localctx.flag)
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
            self.state = 162
            self.expresion()
            cuadruplos.GenerateCuad('Mega_Expresion')
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.AND or _la==VisionScriptParser.OR:
                self.state = 168
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.AND]:
                    self.state = 164
                    localctx._AND = self.match(VisionScriptParser.AND)
                    cuadruplos.InsertOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [VisionScriptParser.OR]:
                    self.state = 166
                    localctx._OR = self.match(VisionScriptParser.OR)
                    cuadruplos.InsertOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 170
                self.expresion()
                cuadruplos.GenerateCuad('Mega_Expresion')
                self.state = 177
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
            self.state = 178
            self.exp()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0):
                self.state = 179
                localctx._exp_todo = self.exp_todo()
                cuadruplos.InsertOperator((None if localctx._exp_todo is None else self._input.getText((localctx._exp_todo.start,localctx._exp_todo.stop))))
                self.state = 181
                self.exp()
                cuadruplos.GenerateCuad('Expresion')
                			


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
            self.state = 186
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
            self.state = 188
            self.termino()
            cuadruplos.GenerateCuad('Termino')
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.PLUS or _la==VisionScriptParser.MINUS:
                self.state = 194
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.PLUS]:
                    self.state = 190
                    localctx._PLUS = self.match(VisionScriptParser.PLUS)
                    cuadruplos.InsertOperator((None if localctx._PLUS is None else localctx._PLUS.text))
                    pass
                elif token in [VisionScriptParser.MINUS]:
                    self.state = 192
                    localctx._MINUS = self.match(VisionScriptParser.MINUS)
                    cuadruplos.InsertOperator((None if localctx._MINUS is None else localctx._MINUS.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 196
                self.termino()
                cuadruplos.GenerateCuad('Termino')
                self.state = 203
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
            self.state = 204
            self.factor()
            cuadruplos.GenerateCuad('Factor')
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.DIVISION or _la==VisionScriptParser.MULTIPLICATION:
                self.state = 210
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.MULTIPLICATION]:
                    self.state = 206
                    localctx._MULTIPLICATION = self.match(VisionScriptParser.MULTIPLICATION)
                    cuadruplos.InsertOperator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [VisionScriptParser.DIVISION]:
                    self.state = 208
                    localctx._DIVISION = self.match(VisionScriptParser.DIVISION)
                    cuadruplos.InsertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 212
                self.factor()
                cuadruplos.GenerateCuad('Factor')
                self.state = 219
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
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(VisionScriptParser.T__1)
                cuadruplos.InsertParentesis()
                self.state = 222
                self.mega_expresion()
                self.state = 223
                self.match(VisionScriptParser.T__2)
                cuadruplos.RemoveParentesis()
                pass
            elif token in [VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                localctx._ct = self.ct()
                cuadruplos.InsertIdType(localctx._ct.value,localctx._ct.type)
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
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(VisionScriptParser.MINUS)
                self.state = 232
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = func_dir.ConstDeclaration(localctx.type , '-'+(None if localctx._CTN is None else localctx._CTN.text) )
                pass
            elif token in [VisionScriptParser.CTN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = func_dir.ConstDeclaration(localctx.type , (None if localctx._CTN is None else localctx._CTN.text) )
                pass
            elif token in [VisionScriptParser.CTBF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                localctx._CTBF = self.match(VisionScriptParser.CTBF)
                localctx.type = 'bool'
                localctx.value = func_dir.ConstDeclaration(localctx.type ,(None if localctx._CTBF is None else localctx._CTBF.text) )
                pass
            elif token in [VisionScriptParser.CTBT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                localctx._CTBT = self.match(VisionScriptParser.CTBT)
                localctx.type = 'bool'
                localctx.value = func_dir.ConstDeclaration(localctx.type , (None if localctx._CTBT is None else localctx._CTBT.text) )
                pass
            elif token in [VisionScriptParser.CTT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                localctx._CTT = self.match(VisionScriptParser.CTT)
                localctx.type = 'text'
                localctx.value = func_dir.ConstDeclaration(localctx.type , (None if localctx._CTT is None else localctx._CTT.text) )
                pass
            elif token in [VisionScriptParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 247
                localctx._ID = self.match(VisionScriptParser.ID)
                localctx.type = func_dir.returnIDType(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text))
                localctx.value = func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text))
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
            self.state = 252
            localctx._function_type = self.function_type()
            self.state = 253
            self.match(VisionScriptParser.FUNCTION)
            self.state = 254
            localctx._ID = self.match(VisionScriptParser.ID)
            cuadruplos.GenerateFunGoto()
            func_dir.currentFunction = (None if localctx._ID is None else localctx._ID.text)
            func_dir.FuncDeclaration(func_dir.currentFunction,localctx._function_type.type)
            self.state = 258
            self.match(VisionScriptParser.T__1)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER))) != 0):
                self.state = 259
                localctx._tipo = self.tipo()
                self.state = 260
                localctx._ID = self.match(VisionScriptParser.ID)
                func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                func_dir.ParamDeclaration(func_dir.currentFunction,localctx._tipo.type)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 263
                    self.match(VisionScriptParser.T__3)
                    self.state = 264
                    localctx._tipo = self.tipo()
                    self.state = 265
                    localctx._ID = self.match(VisionScriptParser.ID)
                    func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                    func_dir.ParamDeclaration(func_dir.currentFunction,localctx._tipo.type)
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 276
            self.match(VisionScriptParser.T__2)
            self.state = 277
            self.match(VisionScriptParser.BEGIN)
            self.state = 278
            self.func_bloque()
            self.state = 279
            self.match(VisionScriptParser.RETURN)
            self.state = 280
            self.match(VisionScriptParser.T__1)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 281
                self.casi_todo()
                cuadruplos.GenerateFunReturns(localctx._function_type.type)


            self.state = 286
            self.match(VisionScriptParser.T__2)
            self.state = 287
            self.match(VisionScriptParser.END)
            cuadruplos.FillFunGoto()
            func_dir.currentFunction = '@global'
            func_dir.memLocal = 9000
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
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER, VisionScriptParser.TEXT, VisionScriptParser.BOOL, VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                localctx._tipo = self.tipo()
                localctx.type = localctx._tipo.type
                pass
            elif token in [VisionScriptParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
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
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 299
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 300
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 301
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 302
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 303
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 304
                    self.asignacion()
                    pass

                elif la_ == 7:
                    self.state = 305
                    self.op_contenedor()
                    pass

                elif la_ == 8:
                    self.state = 306
                    self.function_call()
                    pass


                self.state = 311
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
            self.state = 312
            localctx._ID = self.match(VisionScriptParser.ID)
            cuadruplos.GenerateEra((None if localctx._ID is None else localctx._ID.text))
            self.state = 314
            self.match(VisionScriptParser.T__1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 315
                self.casi_todo()
                cuadruplos.GenerateParameter(func_dir.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 317
                    self.match(VisionScriptParser.T__3)
                    self.state = 318
                    self.casi_todo()
                    cuadruplos.GenerateParameter(func_dir.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                    self.state = 325
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 328
            self.match(VisionScriptParser.T__2)
            cuadruplos.VerifyParameters(func_dir.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
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
            self.state = 331
            self.match(VisionScriptParser.T__4)
            cuadruplos.GenerateEmptyContainer()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 333
                self.mega_expresion()
                cuadruplos.GenerateFillContainer()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 335
                    self.match(VisionScriptParser.T__3)
                    self.state = 336
                    self.mega_expresion()
                    cuadruplos.GenerateFillContainer()
                    self.state = 343
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 346
            self.match(VisionScriptParser.T__5)
            cuadruplos.RegisterContainer()
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
            self.state = 349
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 350
            self.match(VisionScriptParser.T__6)
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.GET_BACK, VisionScriptParser.GET_FRONT, VisionScriptParser.LENGTH]:
                self.state = 357
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.GET_BACK]:
                    self.state = 351
                    localctx._GET_BACK = self.match(VisionScriptParser.GET_BACK)
                    localctx.flag = (None if localctx._GET_BACK is None else localctx._GET_BACK.text)
                    pass
                elif token in [VisionScriptParser.GET_FRONT]:
                    self.state = 353
                    localctx._GET_FRONT = self.match(VisionScriptParser.GET_FRONT)
                    localctx.flag = (None if localctx._GET_FRONT is None else localctx._GET_FRONT.text)
                    pass
                elif token in [VisionScriptParser.LENGTH]:
                    self.state = 355
                    localctx._LENGTH = self.match(VisionScriptParser.LENGTH)
                    localctx.flag = (None if localctx._LENGTH is None else localctx._LENGTH.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 359
                self.match(VisionScriptParser.T__1)
                self.state = 360
                self.match(VisionScriptParser.T__2)
                cuadruplos.FuncionOPContainer1(localctx.flag,func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.GET]:
                self.state = 362
                localctx._GET = self.match(VisionScriptParser.GET)
                localctx.flag = (None if localctx._GET is None else localctx._GET.text)
                self.state = 364
                self.match(VisionScriptParser.T__1)
                self.state = 365
                self.mega_expresion()
                self.state = 366
                self.match(VisionScriptParser.T__2)
                cuadruplos.FuncionOPContainer2(localctx.flag,func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
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
            self.state = 371
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 372
            self.match(VisionScriptParser.T__6)
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.INSERT_BACK, VisionScriptParser.INSERT_FRONT]:
                self.state = 377
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.INSERT_BACK]:
                    self.state = 373
                    localctx._INSERT_BACK = self.match(VisionScriptParser.INSERT_BACK)
                    localctx.flag = (None if localctx._INSERT_BACK is None else localctx._INSERT_BACK.text)
                    pass
                elif token in [VisionScriptParser.INSERT_FRONT]:
                    self.state = 375
                    localctx._INSERT_FRONT = self.match(VisionScriptParser.INSERT_FRONT)
                    localctx.flag = (None if localctx._INSERT_FRONT is None else localctx._INSERT_FRONT.text)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 379
                self.match(VisionScriptParser.T__1)
                self.state = 380
                self.mega_expresion()
                self.state = 381
                self.match(VisionScriptParser.T__2)
                cuadruplos.FuncionOPContainer3(localctx.flag,func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.INSERT]:
                self.state = 384
                localctx._INSERT = self.match(VisionScriptParser.INSERT)
                localctx.flag = (None if localctx._INSERT is None else localctx._INSERT.text)
                self.state = 386
                self.match(VisionScriptParser.T__1)
                self.state = 387
                self.mega_expresion()
                self.state = 388
                self.match(VisionScriptParser.T__3)
                self.state = 389
                self.mega_expresion()
                self.state = 390
                self.match(VisionScriptParser.T__2)
                cuadruplos.FuncionOPContainer4(localctx.flag,func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
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
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.ID]:
                self.state = 395
                localctx._ID = self.match(VisionScriptParser.ID)
                cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)),func_dir.returnIDType(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                pass
            elif token in [VisionScriptParser.T__4]:
                self.state = 397
                self.contenedor()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 407 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 400
                self.match(VisionScriptParser.PLUS)
                self.state = 404
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.ID]:
                    self.state = 401
                    localctx._ID = self.match(VisionScriptParser.ID)
                    cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)),func_dir.returnIDType(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
                    pass
                elif token in [VisionScriptParser.T__4]:
                    self.state = 403
                    self.contenedor()
                    pass
                else:
                    raise NoViableAltException(self)

                cuadruplos.GenerateConcatContainer()
                self.state = 409 
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





