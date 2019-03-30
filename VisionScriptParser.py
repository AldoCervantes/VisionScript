# Generated from VisionScript.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from VisionScriptCompiler import FunctionDirectory
from Cuadruplos import Cuadruplos
func_dir = FunctionDirectory()
cuadruplos = Cuadruplos() 


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0156\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3D\n\3\f\3\16\3G\13\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\\\n\5\3\6\3\6\3\6\3\6\3\6\5\6c\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\tx\n\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\7\n\u0085\n\n\f\n\16\n\u0088\13")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u009a\n\r\3\r\3\r\3\r\7\r\u009f")
        buf.write("\n\r\f\r\16\r\u00a2\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00aa\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00b4\n\20\3\20\3\20\3\20\7\20\u00b9\n\20\f\20")
        buf.write("\16\20\u00bc\13\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00c4\n\21\3\21\3\21\3\21\7\21\u00c9\n\21\f\21\16\21")
        buf.write("\u00cc\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00d7\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e6\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\7\24\u00f6\n\24\f\24\16\24\u00f9\13\24\5\24")
        buf.write("\u00fb\n\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0103\n")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u010f\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\7\26\u0119\n\26\f\26\16\26\u011c\13\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u0126\n\27\f\27\16\27")
        buf.write("\u0129\13\27\5\27\u012b\n\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0133\n\30\f\30\16\30\u0136\13\30\5\30\u0138")
        buf.write("\n\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u014d")
        buf.write("\n\31\3\32\3\32\3\32\6\32\u0152\n\32\r\32\16\32\u0153")
        buf.write("\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\2\6\3\2\13\r\4\2\27\30\60\63\4\2!\"((\3\2")
        buf.write("#%\2\u0174\2\64\3\2\2\2\4E\3\2\2\2\6H\3\2\2\2\b[\3\2\2")
        buf.write("\2\nb\3\2\2\2\fd\3\2\2\2\16i\3\2\2\2\20q\3\2\2\2\22\u0086")
        buf.write("\3\2\2\2\24\u0089\3\2\2\2\26\u008e\3\2\2\2\30\u0093\3")
        buf.write("\2\2\2\32\u00a3\3\2\2\2\34\u00ab\3\2\2\2\36\u00ad\3\2")
        buf.write("\2\2 \u00bd\3\2\2\2\"\u00d6\3\2\2\2$\u00e5\3\2\2\2&\u00e7")
        buf.write("\3\2\2\2(\u010e\3\2\2\2*\u011a\3\2\2\2,\u011d\3\2\2\2")
        buf.write(".\u012e\3\2\2\2\60\u013b\3\2\2\2\62\u014e\3\2\2\2\64\65")
        buf.write("\b\2\1\2\65\66\5\4\3\2\66\67\7\2\2\3\678\b\2\1\289\b\2")
        buf.write("\1\29\3\3\2\2\2:D\5\6\4\2;D\5\16\b\2<D\5\20\t\2=D\5\24")
        buf.write("\13\2>D\5\26\f\2?D\5&\24\2@D\5,\27\2AD\5\f\7\2BD\5\60")
        buf.write("\31\2C:\3\2\2\2C;\3\2\2\2C<\3\2\2\2C=\3\2\2\2C>\3\2\2")
        buf.write("\2C?\3\2\2\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2DG\3\2\2\2E")
        buf.write("C\3\2\2\2EF\3\2\2\2F\5\3\2\2\2GE\3\2\2\2HI\5\b\5\2IJ\7")
        buf.write(")\2\2JK\7\3\2\2KL\5\n\6\2LM\b\4\1\2MN\b\4\1\2N\7\3\2\2")
        buf.write("\2OP\7\20\2\2P\\\b\5\1\2QR\7\21\2\2R\\\b\5\1\2ST\7\22")
        buf.write("\2\2T\\\b\5\1\2UV\7\31\2\2VW\7\4\2\2WX\5\30\r\2XY\7\5")
        buf.write("\2\2YZ\b\5\1\2Z\\\3\2\2\2[O\3\2\2\2[Q\3\2\2\2[S\3\2\2")
        buf.write("\2[U\3\2\2\2\\\t\3\2\2\2]c\5\30\r\2^c\5\62\32\2_c\5.\30")
        buf.write("\2`c\5,\27\2ac\5\60\31\2b]\3\2\2\2b^\3\2\2\2b_\3\2\2\2")
        buf.write("b`\3\2\2\2ba\3\2\2\2c\13\3\2\2\2de\7)\2\2ef\7\3\2\2fg")
        buf.write("\5\n\6\2gh\b\7\1\2h\r\3\2\2\2ij\7\16\2\2jk\5\30\r\2kl")
        buf.write("\7\32\2\2lm\5\22\n\2mn\7\17\2\2no\5\22\n\2op\7\33\2\2")
        buf.write("p\17\3\2\2\2qw\7\34\2\2rs\5\30\r\2st\7\35\2\2tx\3\2\2")
        buf.write("\2uv\7\36\2\2vx\5\30\r\2wr\3\2\2\2wu\3\2\2\2xy\3\2\2\2")
        buf.write("yz\7\32\2\2z{\5\22\n\2{|\7\33\2\2|\21\3\2\2\2}\u0085\5")
        buf.write("\16\b\2~\u0085\5\20\t\2\177\u0085\5\24\13\2\u0080\u0085")
        buf.write("\5\26\f\2\u0081\u0085\5\f\7\2\u0082\u0085\5\60\31\2\u0083")
        buf.write("\u0085\5,\27\2\u0084}\3\2\2\2\u0084~\3\2\2\2\u0084\177")
        buf.write("\3\2\2\2\u0084\u0080\3\2\2\2\u0084\u0081\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\23\3\2")
        buf.write("\2\2\u0088\u0086\3\2\2\2\u0089\u008a\7\n\2\2\u008a\u008b")
        buf.write("\7\4\2\2\u008b\u008c\7)\2\2\u008c\u008d\7\5\2\2\u008d")
        buf.write("\25\3\2\2\2\u008e\u008f\t\2\2\2\u008f\u0090\7\4\2\2\u0090")
        buf.write("\u0091\5\n\6\2\u0091\u0092\7\5\2\2\u0092\27\3\2\2\2\u0093")
        buf.write("\u0094\5\32\16\2\u0094\u00a0\b\r\1\2\u0095\u0096\7\25")
        buf.write("\2\2\u0096\u009a\b\r\1\2\u0097\u0098\7\26\2\2\u0098\u009a")
        buf.write("\b\r\1\2\u0099\u0095\3\2\2\2\u0099\u0097\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\5\32\16\2\u009c\u009d\b\r\1")
        buf.write("\2\u009d\u009f\3\2\2\2\u009e\u0099\3\2\2\2\u009f\u00a2")
        buf.write("\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\31\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a9\5\36\20\2")
        buf.write("\u00a4\u00a5\5\34\17\2\u00a5\u00a6\b\16\1\2\u00a6\u00a7")
        buf.write("\5\36\20\2\u00a7\u00a8\b\16\1\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u00a4\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\33\3\2\2\2\u00ab")
        buf.write("\u00ac\t\3\2\2\u00ac\35\3\2\2\2\u00ad\u00ae\5 \21\2\u00ae")
        buf.write("\u00ba\b\20\1\2\u00af\u00b0\7,\2\2\u00b0\u00b4\b\20\1")
        buf.write("\2\u00b1\u00b2\7-\2\2\u00b2\u00b4\b\20\1\2\u00b3\u00af")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b6\5 \21\2\u00b6\u00b7\b\20\1\2\u00b7\u00b9\3\2\2")
        buf.write("\2\u00b8\u00b3\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\37\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00be\5\"\22\2\u00be\u00ca\b\21\1\2\u00bf")
        buf.write("\u00c0\7/\2\2\u00c0\u00c4\b\21\1\2\u00c1\u00c2\7.\2\2")
        buf.write("\u00c2\u00c4\b\21\1\2\u00c3\u00bf\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\5\"\22\2\u00c6")
        buf.write("\u00c7\b\21\1\2\u00c7\u00c9\3\2\2\2\u00c8\u00c3\3\2\2")
        buf.write("\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb!\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce")
        buf.write("\7\4\2\2\u00ce\u00cf\b\22\1\2\u00cf\u00d0\5\30\r\2\u00d0")
        buf.write("\u00d1\7\5\2\2\u00d1\u00d2\b\22\1\2\u00d2\u00d7\3\2\2")
        buf.write("\2\u00d3\u00d4\5$\23\2\u00d4\u00d5\b\22\1\2\u00d5\u00d7")
        buf.write("\3\2\2\2\u00d6\u00cd\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7")
        buf.write("#\3\2\2\2\u00d8\u00d9\7-\2\2\u00d9\u00da\7*\2\2\u00da")
        buf.write("\u00e6\b\23\1\2\u00db\u00dc\7*\2\2\u00dc\u00e6\b\23\1")
        buf.write("\2\u00dd\u00de\7\23\2\2\u00de\u00e6\b\23\1\2\u00df\u00e0")
        buf.write("\7\24\2\2\u00e0\u00e6\b\23\1\2\u00e1\u00e2\7+\2\2\u00e2")
        buf.write("\u00e6\b\23\1\2\u00e3\u00e4\7)\2\2\u00e4\u00e6\b\23\1")
        buf.write("\2\u00e5\u00d8\3\2\2\2\u00e5\u00db\3\2\2\2\u00e5\u00dd")
        buf.write("\3\2\2\2\u00e5\u00df\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e6%\3\2\2\2\u00e7\u00e8\5(\25\2\u00e8")
        buf.write("\u00e9\7\37\2\2\u00e9\u00ea\7)\2\2\u00ea\u00eb\b\24\1")
        buf.write("\2\u00eb\u00ec\b\24\1\2\u00ec\u00fa\7\4\2\2\u00ed\u00ee")
        buf.write("\5\b\5\2\u00ee\u00ef\7)\2\2\u00ef\u00f7\b\24\1\2\u00f0")
        buf.write("\u00f1\7\6\2\2\u00f1\u00f2\5\b\5\2\u00f2\u00f3\7)\2\2")
        buf.write("\u00f3\u00f4\b\24\1\2\u00f4\u00f6\3\2\2\2\u00f5\u00f0")
        buf.write("\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2")
        buf.write("\u00fa\u00ed\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc\u00fd\7\5\2\2\u00fd\u00fe\7\32\2\2\u00fe")
        buf.write("\u00ff\5*\26\2\u00ff\u0100\7 \2\2\u0100\u0102\7\4\2\2")
        buf.write("\u0101\u0103\5\n\6\2\u0102\u0101\3\2\2\2\u0102\u0103\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\7\5\2\2\u0105\u0106")
        buf.write("\7\33\2\2\u0106\u0107\b\24\1\2\u0107\u0108\b\24\1\2\u0108")
        buf.write("\'\3\2\2\2\u0109\u010a\5\b\5\2\u010a\u010b\b\25\1\2\u010b")
        buf.write("\u010f\3\2\2\2\u010c\u010d\7\'\2\2\u010d\u010f\b\25\1")
        buf.write("\2\u010e\u0109\3\2\2\2\u010e\u010c\3\2\2\2\u010f)\3\2")
        buf.write("\2\2\u0110\u0119\5\6\4\2\u0111\u0119\5\16\b\2\u0112\u0119")
        buf.write("\5\20\t\2\u0113\u0119\5\24\13\2\u0114\u0119\5\26\f\2\u0115")
        buf.write("\u0119\5\f\7\2\u0116\u0119\5\60\31\2\u0117\u0119\5,\27")
        buf.write("\2\u0118\u0110\3\2\2\2\u0118\u0111\3\2\2\2\u0118\u0112")
        buf.write("\3\2\2\2\u0118\u0113\3\2\2\2\u0118\u0114\3\2\2\2\u0118")
        buf.write("\u0115\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3")
        buf.write("\2\2\2\u011b+\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e")
        buf.write("\7)\2\2\u011e\u012a\7\4\2\2\u011f\u0120\5\n\6\2\u0120")
        buf.write("\u0127\b\27\1\2\u0121\u0122\7\6\2\2\u0122\u0123\5\n\6")
        buf.write("\2\u0123\u0124\b\27\1\2\u0124\u0126\3\2\2\2\u0125\u0121")
        buf.write("\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u012a\u011f\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3")
        buf.write("\2\2\2\u012c\u012d\7\5\2\2\u012d-\3\2\2\2\u012e\u0137")
        buf.write("\7\7\2\2\u012f\u0134\5\30\r\2\u0130\u0131\7\6\2\2\u0131")
        buf.write("\u0133\5\30\r\2\u0132\u0130\3\2\2\2\u0133\u0136\3\2\2")
        buf.write("\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0138")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u012f\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\7\b\2\2")
        buf.write("\u013a/\3\2\2\2\u013b\u013c\7)\2\2\u013c\u014c\7\t\2\2")
        buf.write("\u013d\u013e\t\4\2\2\u013e\u013f\7\4\2\2\u013f\u014d\7")
        buf.write("\5\2\2\u0140\u0141\t\5\2\2\u0141\u0142\7\4\2\2\u0142\u0143")
        buf.write("\5\30\r\2\u0143\u0144\7\5\2\2\u0144\u014d\3\2\2\2\u0145")
        buf.write("\u0146\7&\2\2\u0146\u0147\7\4\2\2\u0147\u0148\5\30\r\2")
        buf.write("\u0148\u0149\7\6\2\2\u0149\u014a\5\30\r\2\u014a\u014b")
        buf.write("\7\5\2\2\u014b\u014d\3\2\2\2\u014c\u013d\3\2\2\2\u014c")
        buf.write("\u0140\3\2\2\2\u014c\u0145\3\2\2\2\u014d\61\3\2\2\2\u014e")
        buf.write("\u0151\5.\30\2\u014f\u0150\7,\2\2\u0150\u0152\5.\30\2")
        buf.write("\u0151\u014f\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0154\3\2\2\2\u0154\63\3\2\2\2\36CE[bw\u0084")
        buf.write("\u0086\u0099\u00a0\u00a9\u00b3\u00ba\u00c3\u00ca\u00d6")
        buf.write("\u00e5\u00f7\u00fa\u0102\u010e\u0118\u011a\u0127\u012a")
        buf.write("\u0134\u0137\u014c\u0153")
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
    RULE_asignacion = 5
    RULE_condicion = 6
    RULE_ciclo = 7
    RULE_bloque = 8
    RULE_read = 9
    RULE_imprimir = 10
    RULE_mega_expresion = 11
    RULE_expresion = 12
    RULE_exp_todo = 13
    RULE_exp = 14
    RULE_termino = 15
    RULE_factor = 16
    RULE_ct = 17
    RULE_function = 18
    RULE_function_type = 19
    RULE_func_bloque = 20
    RULE_function_call = 21
    RULE_contenedor = 22
    RULE_op_contenedor = 23
    RULE_concat_contenedor = 24

    ruleNames =  [ "visionscript", "programa", "variable", "tipo", "todo", 
                   "asignacion", "condicion", "ciclo", "bloque", "read", 
                   "imprimir", "mega_expresion", "expresion", "exp_todo", 
                   "exp", "termino", "factor", "ct", "function", "function_type", 
                   "func_bloque", "function_call", "contenedor", "op_contenedor", 
                   "concat_contenedor" ]

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
            self.state = 51
            self.programa()
            self.state = 52
            self.match(VisionScriptParser.EOF)
            cuadruplos.printCuad()
            func_dir.showFunctionDirectory()
            		
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
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.VOID) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 59
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 60
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 61
                    self.function()
                    pass

                elif la_ == 7:
                    self.state = 62
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 63
                    self.asignacion()
                    pass

                elif la_ == 9:
                    self.state = 64
                    self.op_contenedor()
                    pass


                self.state = 69
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
            self.state = 70
            localctx._tipo = self.tipo()
            self.state = 71
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 72
            self.match(VisionScriptParser.T__0)
            self.state = 73
            localctx._todo = self.todo()
            func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
            		
            cuadruplos.GenerateAssignmentCuad('Assignment',func_dir.returnIDAddress(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text)))
            		
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

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                localctx._NUMBER = self.match(VisionScriptParser.NUMBER)
                localctx.type = (None if localctx._NUMBER is None else localctx._NUMBER.text)
                pass
            elif token in [VisionScriptParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                localctx._TEXT = self.match(VisionScriptParser.TEXT)
                localctx.type = (None if localctx._TEXT is None else localctx._TEXT.text)
                pass
            elif token in [VisionScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                localctx._BOOL = self.match(VisionScriptParser.BOOL)
                localctx.type = (None if localctx._BOOL is None else localctx._BOOL.text)
                pass
            elif token in [VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                localctx._CONTAINER = self.match(VisionScriptParser.CONTAINER)
                self.state = 84
                self.match(VisionScriptParser.T__1)
                self.state = 85
                self.mega_expresion()
                self.state = 86
                self.match(VisionScriptParser.T__2)
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

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def concat_contenedor(self):
            return self.getTypedRuleContext(VisionScriptParser.Concat_contenedorContext,0)


        def contenedor(self):
            return self.getTypedRuleContext(VisionScriptParser.ContenedorContext,0)


        def function_call(self):
            return self.getTypedRuleContext(VisionScriptParser.Function_callContext,0)


        def op_contenedor(self):
            return self.getTypedRuleContext(VisionScriptParser.Op_contenedorContext,0)


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
                self.state = 91
                self.mega_expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.concat_contenedor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.contenedor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.op_contenedor()
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
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 99
            self.match(VisionScriptParser.T__0)
            self.state = 100
            localctx._todo = self.todo()
            func_dir.VarAssignment(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
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
        self.enterRule(localctx, 12, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(VisionScriptParser.IF)
            self.state = 104
            self.mega_expresion()
            self.state = 105
            self.match(VisionScriptParser.BEGIN)
            self.state = 106
            self.bloque()
            self.state = 107
            self.match(VisionScriptParser.ELSE)
            self.state = 108
            self.bloque()
            self.state = 109
            self.match(VisionScriptParser.END)
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

        def BEGIN(self):
            return self.getToken(VisionScriptParser.BEGIN, 0)

        def bloque(self):
            return self.getTypedRuleContext(VisionScriptParser.BloqueContext,0)


        def END(self):
            return self.getToken(VisionScriptParser.END, 0)

        def mega_expresion(self):
            return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,0)


        def TIMES(self):
            return self.getToken(VisionScriptParser.TIMES, 0)

        def UNTIL(self):
            return self.getToken(VisionScriptParser.UNTIL, 0)

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
        self.enterRule(localctx, 14, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(VisionScriptParser.REPEAT)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1, VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.state = 112
                self.mega_expresion()
                self.state = 113
                self.match(VisionScriptParser.TIMES)
                pass
            elif token in [VisionScriptParser.UNTIL]:
                self.state = 115
                self.match(VisionScriptParser.UNTIL)
                self.state = 116
                self.mega_expresion()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self.match(VisionScriptParser.BEGIN)
            self.state = 120
            self.bloque()
            self.state = 121
            self.match(VisionScriptParser.END)
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
        self.enterRule(localctx, 16, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 123
                    self.condicion()
                    pass

                elif la_ == 2:
                    self.state = 124
                    self.ciclo()
                    pass

                elif la_ == 3:
                    self.state = 125
                    self.read()
                    pass

                elif la_ == 4:
                    self.state = 126
                    self.imprimir()
                    pass

                elif la_ == 5:
                    self.state = 127
                    self.asignacion()
                    pass

                elif la_ == 6:
                    self.state = 128
                    self.op_contenedor()
                    pass

                elif la_ == 7:
                    self.state = 129
                    self.function_call()
                    pass


                self.state = 134
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
        self.enterRule(localctx, 18, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(VisionScriptParser.READ)
            self.state = 136
            self.match(VisionScriptParser.T__1)
            self.state = 137
            self.match(VisionScriptParser.ID)
            self.state = 138
            self.match(VisionScriptParser.T__2)
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
        self.enterRule(localctx, 20, self.RULE_imprimir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 141
            self.match(VisionScriptParser.T__1)
            self.state = 142
            self.todo()
            self.state = 143
            self.match(VisionScriptParser.T__2)
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
        self.enterRule(localctx, 22, self.RULE_mega_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expresion()
            cuadruplos.GenerateCuad('Mega_Expresion')
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.AND or _la==VisionScriptParser.OR:
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.AND]:
                    self.state = 147
                    localctx._AND = self.match(VisionScriptParser.AND)
                    cuadruplos.InsertOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [VisionScriptParser.OR]:
                    self.state = 149
                    localctx._OR = self.match(VisionScriptParser.OR)
                    cuadruplos.InsertOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 153
                self.expresion()
                cuadruplos.GenerateCuad('Mega_Expresion')
                self.state = 160
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
        self.enterRule(localctx, 24, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.exp()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0):
                self.state = 162
                localctx._exp_todo = self.exp_todo()
                cuadruplos.InsertOperator((None if localctx._exp_todo is None else self._input.getText((localctx._exp_todo.start,localctx._exp_todo.stop))))
                self.state = 164
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
        self.enterRule(localctx, 26, self.RULE_exp_todo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
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
        self.enterRule(localctx, 28, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.termino()
            cuadruplos.GenerateCuad('Termino')
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.PLUS or _la==VisionScriptParser.MINUS:
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.PLUS]:
                    self.state = 173
                    localctx._PLUS = self.match(VisionScriptParser.PLUS)
                    cuadruplos.InsertOperator((None if localctx._PLUS is None else localctx._PLUS.text))
                    pass
                elif token in [VisionScriptParser.MINUS]:
                    self.state = 175
                    localctx._MINUS = self.match(VisionScriptParser.MINUS)
                    cuadruplos.InsertOperator((None if localctx._MINUS is None else localctx._MINUS.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 179
                self.termino()
                cuadruplos.GenerateCuad('Termino')
                self.state = 186
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
        self.enterRule(localctx, 30, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.factor()
            cuadruplos.GenerateCuad('Factor')
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.DIVISION or _la==VisionScriptParser.MULTIPLICATION:
                self.state = 193
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.MULTIPLICATION]:
                    self.state = 189
                    localctx._MULTIPLICATION = self.match(VisionScriptParser.MULTIPLICATION)
                    cuadruplos.InsertOperator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [VisionScriptParser.DIVISION]:
                    self.state = 191
                    localctx._DIVISION = self.match(VisionScriptParser.DIVISION)
                    cuadruplos.InsertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 195
                self.factor()
                cuadruplos.GenerateCuad('Factor')
                self.state = 202
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
        self.enterRule(localctx, 32, self.RULE_factor)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(VisionScriptParser.T__1)
                cuadruplos.InsertParentesis()
                self.state = 205
                self.mega_expresion()
                self.state = 206
                self.match(VisionScriptParser.T__2)
                cuadruplos.RemoveParentesis()
                pass
            elif token in [VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                localctx._ct = self.ct()
                cuadruplos.InsertIdType((None if localctx._ct is None else self._input.getText((localctx._ct.start,localctx._ct.stop))),localctx._ct.type)
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
        self.enterRule(localctx, 34, self.RULE_ct)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(VisionScriptParser.MINUS)
                self.state = 215
                self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                pass
            elif token in [VisionScriptParser.CTN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                pass
            elif token in [VisionScriptParser.CTBF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.match(VisionScriptParser.CTBF)
                localctx.type = 'bool'
                pass
            elif token in [VisionScriptParser.CTBT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.match(VisionScriptParser.CTBT)
                localctx.type = 'bool'
                pass
            elif token in [VisionScriptParser.CTT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.match(VisionScriptParser.CTT)
                localctx.type = 'text'
                pass
            elif token in [VisionScriptParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 225
                localctx._ID = self.match(VisionScriptParser.ID)
                localctx.type = func_dir.returnIDType(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text))
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


        def todo(self):
            return self.getTypedRuleContext(VisionScriptParser.TodoContext,0)


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
        self.enterRule(localctx, 36, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            localctx._function_type = self.function_type()
            self.state = 230
            self.match(VisionScriptParser.FUNCTION)
            self.state = 231
            localctx._ID = self.match(VisionScriptParser.ID)
            func_dir.currentFunction = (None if localctx._ID is None else localctx._ID.text)
            func_dir.FuncDeclaration(func_dir.currentFunction,localctx._function_type.type)
            		
            self.state = 234
            self.match(VisionScriptParser.T__1)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER))) != 0):
                self.state = 235
                localctx._tipo = self.tipo()
                self.state = 236
                localctx._ID = self.match(VisionScriptParser.ID)
                func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                		
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 238
                    self.match(VisionScriptParser.T__3)
                    self.state = 239
                    localctx._tipo = self.tipo()
                    self.state = 240
                    localctx._ID = self.match(VisionScriptParser.ID)
                    func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                    		
                    self.state = 247
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 250
            self.match(VisionScriptParser.T__2)
            self.state = 251
            self.match(VisionScriptParser.BEGIN)
            self.state = 252
            self.func_bloque()
            self.state = 253
            self.match(VisionScriptParser.RETURN)
            self.state = 254
            self.match(VisionScriptParser.T__1)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 255
                self.todo()


            self.state = 258
            self.match(VisionScriptParser.T__2)
            self.state = 259
            self.match(VisionScriptParser.END)
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
        self.enterRule(localctx, 38, self.RULE_function_type)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER, VisionScriptParser.TEXT, VisionScriptParser.BOOL, VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                localctx._tipo = self.tipo()
                localctx.type = localctx._tipo.type
                pass
            elif token in [VisionScriptParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
        self.enterRule(localctx, 40, self.RULE_func_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 278
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 271
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 272
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 273
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 274
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 275
                    self.asignacion()
                    pass

                elif la_ == 7:
                    self.state = 276
                    self.op_contenedor()
                    pass

                elif la_ == 8:
                    self.state = 277
                    self.function_call()
                    pass


                self.state = 282
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
            self._todo = None # TodoContext

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def todo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.TodoContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.TodoContext,i)


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
        self.enterRule(localctx, 42, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 284
            self.match(VisionScriptParser.T__1)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 285
                localctx._todo = self.todo()
                func_dir.VarAssignment((None if localctx._ID is None else localctx._ID.text),(None if localctx._ID is None else localctx._ID.text),(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 287
                    self.match(VisionScriptParser.T__3)
                    self.state = 288
                    localctx._todo = self.todo()
                    func_dir.VarAssignment(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),(None if localctx._todo is None else self._input.getText((localctx._todo.start,localctx._todo.stop))))
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 298
            self.match(VisionScriptParser.T__2)
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
        self.enterRule(localctx, 44, self.RULE_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(VisionScriptParser.T__4)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 301
                self.mega_expresion()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 302
                    self.match(VisionScriptParser.T__3)
                    self.state = 303
                    self.mega_expresion()
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 311
            self.match(VisionScriptParser.T__5)
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

        def ID(self):
            return self.getToken(VisionScriptParser.ID, 0)

        def mega_expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VisionScriptParser.Mega_expresionContext)
            else:
                return self.getTypedRuleContext(VisionScriptParser.Mega_expresionContext,i)


        def INSERT(self):
            return self.getToken(VisionScriptParser.INSERT, 0)

        def GET_BACK(self):
            return self.getToken(VisionScriptParser.GET_BACK, 0)

        def GET_FRONT(self):
            return self.getToken(VisionScriptParser.GET_FRONT, 0)

        def LENGTH(self):
            return self.getToken(VisionScriptParser.LENGTH, 0)

        def GET(self):
            return self.getToken(VisionScriptParser.GET, 0)

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
        self.enterRule(localctx, 46, self.RULE_op_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(VisionScriptParser.ID)
            self.state = 314
            self.match(VisionScriptParser.T__6)
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.GET_BACK, VisionScriptParser.GET_FRONT, VisionScriptParser.LENGTH]:
                self.state = 315
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.GET_BACK) | (1 << VisionScriptParser.GET_FRONT) | (1 << VisionScriptParser.LENGTH))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 316
                self.match(VisionScriptParser.T__1)
                self.state = 317
                self.match(VisionScriptParser.T__2)
                pass
            elif token in [VisionScriptParser.GET, VisionScriptParser.INSERT_BACK, VisionScriptParser.INSERT_FRONT]:
                self.state = 318
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.GET) | (1 << VisionScriptParser.INSERT_BACK) | (1 << VisionScriptParser.INSERT_FRONT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.match(VisionScriptParser.T__1)
                self.state = 320
                self.mega_expresion()
                self.state = 321
                self.match(VisionScriptParser.T__2)
                pass
            elif token in [VisionScriptParser.INSERT]:
                self.state = 323
                self.match(VisionScriptParser.INSERT)
                self.state = 324
                self.match(VisionScriptParser.T__1)
                self.state = 325
                self.mega_expresion()
                self.state = 326
                self.match(VisionScriptParser.T__3)
                self.state = 327
                self.mega_expresion()
                self.state = 328
                self.match(VisionScriptParser.T__2)
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
        self.enterRule(localctx, 48, self.RULE_concat_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.contenedor()
            self.state = 335 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 333
                self.match(VisionScriptParser.PLUS)
                self.state = 334
                self.contenedor()
                self.state = 337 
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





