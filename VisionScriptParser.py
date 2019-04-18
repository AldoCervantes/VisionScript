# Generated from VisionScript.g4 by ANTLR 4.7.1
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
        buf.write("\u016f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3F\n\3\f\3\16\3I\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5Z\n\5\3\6\3\6\5\6^\n\6\3\7\3\7\3\7\3\7\5\7")
        buf.write("d\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u0088\n")
        buf.write("\13\f\13\16\13\u008b\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009a\n\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a7\n\16\3\16")
        buf.write("\3\16\3\16\7\16\u00ac\n\16\f\16\16\16\u00af\13\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00b7\n\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c1\n\21\3\21\3\21")
        buf.write("\3\21\7\21\u00c6\n\21\f\21\16\21\u00c9\13\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00d1\n\22\3\22\3\22\3\22\7")
        buf.write("\22\u00d6\n\22\f\22\16\22\u00d9\13\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00f9\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\7\25\u010c\n\25\f\25\16\25\u010f")
        buf.write("\13\25\5\25\u0111\n\25\3\25\3\25\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u0119\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0126\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0130\n\27\f\27\16\27\u0133\13")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u013e\n\30\f\30\16\30\u0141\13\30\5\30\u0143\n\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u014c\n\31\f\31\16")
        buf.write("\31\u014f\13\31\5\31\u0151\n\31\3\31\3\31\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0166\n\32\3\33\3\33\3\33\6")
        buf.write("\33\u016b\n\33\r\33\16\33\u016c\3\33\2\2\34\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\5\4")
        buf.write("\2\27\30\60\63\4\2!\"((\3\2#%\2\u018d\2\66\3\2\2\2\4G")
        buf.write("\3\2\2\2\6J\3\2\2\2\bY\3\2\2\2\n]\3\2\2\2\fc\3\2\2\2\16")
        buf.write("e\3\2\2\2\20k\3\2\2\2\22v\3\2\2\2\24\u0089\3\2\2\2\26")
        buf.write("\u008c\3\2\2\2\30\u0099\3\2\2\2\32\u00a0\3\2\2\2\34\u00b0")
        buf.write("\3\2\2\2\36\u00b8\3\2\2\2 \u00ba\3\2\2\2\"\u00ca\3\2\2")
        buf.write("\2$\u00e3\3\2\2\2&\u00f8\3\2\2\2(\u00fa\3\2\2\2*\u0125")
        buf.write("\3\2\2\2,\u0131\3\2\2\2.\u0134\3\2\2\2\60\u0147\3\2\2")
        buf.write("\2\62\u0154\3\2\2\2\64\u0167\3\2\2\2\66\67\b\2\1\2\67")
        buf.write("8\5\4\3\289\7\2\2\39:\b\2\1\2:;\b\2\1\2;\3\3\2\2\2<F\5")
        buf.write("\6\4\2=F\5\20\t\2>F\5\22\n\2?F\5\26\f\2@F\5\30\r\2AF\5")
        buf.write("(\25\2BF\5.\30\2CF\5\16\b\2DF\5\62\32\2E<\3\2\2\2E=\3")
        buf.write("\2\2\2E>\3\2\2\2E?\3\2\2\2E@\3\2\2\2EA\3\2\2\2EB\3\2\2")
        buf.write("\2EC\3\2\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H")
        buf.write("\5\3\2\2\2IG\3\2\2\2JK\5\b\5\2KL\7)\2\2LM\7\3\2\2MN\5")
        buf.write("\n\6\2NO\b\4\1\2OP\b\4\1\2P\7\3\2\2\2QR\7\20\2\2RZ\b\5")
        buf.write("\1\2ST\7\21\2\2TZ\b\5\1\2UV\7\22\2\2VZ\b\5\1\2WX\7\31")
        buf.write("\2\2XZ\b\5\1\2YQ\3\2\2\2YS\3\2\2\2YU\3\2\2\2YW\3\2\2\2")
        buf.write("Z\t\3\2\2\2[^\5\f\7\2\\^\5.\30\2][\3\2\2\2]\\\3\2\2\2")
        buf.write("^\13\3\2\2\2_d\5\32\16\2`d\5\64\33\2ad\5\60\31\2bd\5\62")
        buf.write("\32\2c_\3\2\2\2c`\3\2\2\2ca\3\2\2\2cb\3\2\2\2d\r\3\2\2")
        buf.write("\2ef\7)\2\2fg\7\3\2\2gh\5\n\6\2hi\b\b\1\2ij\b\b\1\2j\17")
        buf.write("\3\2\2\2kl\7\16\2\2lm\5\32\16\2mn\b\t\1\2no\7\32\2\2o")
        buf.write("p\5\24\13\2pq\7\17\2\2qr\b\t\1\2rs\5\24\13\2st\7\33\2")
        buf.write("\2tu\b\t\1\2u\21\3\2\2\2vw\7\34\2\2wx\7\36\2\2xy\b\n\1")
        buf.write("\2yz\5\32\16\2z{\b\n\1\2{|\7\32\2\2|}\5\24\13\2}~\7\33")
        buf.write("\2\2~\177\b\n\1\2\177\23\3\2\2\2\u0080\u0088\5\20\t\2")
        buf.write("\u0081\u0088\5\22\n\2\u0082\u0088\5\26\f\2\u0083\u0088")
        buf.write("\5\30\r\2\u0084\u0088\5\16\b\2\u0085\u0088\5\62\32\2\u0086")
        buf.write("\u0088\5.\30\2\u0087\u0080\3\2\2\2\u0087\u0081\3\2\2\2")
        buf.write("\u0087\u0082\3\2\2\2\u0087\u0083\3\2\2\2\u0087\u0084\3")
        buf.write("\2\2\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\25\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\7\n\2\2\u008d")
        buf.write("\u008e\7\4\2\2\u008e\u008f\7)\2\2\u008f\u0090\b\f\1\2")
        buf.write("\u0090\u0091\7\5\2\2\u0091\u0092\b\f\1\2\u0092\27\3\2")
        buf.write("\2\2\u0093\u0094\7\r\2\2\u0094\u009a\b\r\1\2\u0095\u0096")
        buf.write("\7\13\2\2\u0096\u009a\b\r\1\2\u0097\u0098\7\f\2\2\u0098")
        buf.write("\u009a\b\r\1\2\u0099\u0093\3\2\2\2\u0099\u0095\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\7")
        buf.write("\4\2\2\u009c\u009d\5\n\6\2\u009d\u009e\7\5\2\2\u009e\u009f")
        buf.write("\b\r\1\2\u009f\31\3\2\2\2\u00a0\u00a1\5\34\17\2\u00a1")
        buf.write("\u00ad\b\16\1\2\u00a2\u00a3\7\25\2\2\u00a3\u00a7\b\16")
        buf.write("\1\2\u00a4\u00a5\7\26\2\2\u00a5\u00a7\b\16\1\2\u00a6\u00a2")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00a9\5\34\17\2\u00a9\u00aa\b\16\1\2\u00aa\u00ac\3\2")
        buf.write("\2\2\u00ab\u00a6\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\33\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00b0\u00b6\5 \21\2\u00b1\u00b2\5\36\20\2\u00b2")
        buf.write("\u00b3\b\17\1\2\u00b3\u00b4\5 \21\2\u00b4\u00b5\b\17\1")
        buf.write("\2\u00b5\u00b7\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\35\3\2\2\2\u00b8\u00b9\t\2\2\2\u00b9\37")
        buf.write("\3\2\2\2\u00ba\u00bb\5\"\22\2\u00bb\u00c7\b\21\1\2\u00bc")
        buf.write("\u00bd\7,\2\2\u00bd\u00c1\b\21\1\2\u00be\u00bf\7-\2\2")
        buf.write("\u00bf\u00c1\b\21\1\2\u00c0\u00bc\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\5\"\22\2\u00c3")
        buf.write("\u00c4\b\21\1\2\u00c4\u00c6\3\2\2\2\u00c5\u00c0\3\2\2")
        buf.write("\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8!\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb")
        buf.write("\5$\23\2\u00cb\u00d7\b\22\1\2\u00cc\u00cd\7/\2\2\u00cd")
        buf.write("\u00d1\b\22\1\2\u00ce\u00cf\7.\2\2\u00cf\u00d1\b\22\1")
        buf.write("\2\u00d0\u00cc\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2")
        buf.write("\3\2\2\2\u00d2\u00d3\5$\23\2\u00d3\u00d4\b\22\1\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d6\u00d9\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8#\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7\4\2\2\u00db\u00dc")
        buf.write("\b\23\1\2\u00dc\u00dd\5\32\16\2\u00dd\u00de\7\5\2\2\u00de")
        buf.write("\u00df\b\23\1\2\u00df\u00e4\3\2\2\2\u00e0\u00e1\5&\24")
        buf.write("\2\u00e1\u00e2\b\23\1\2\u00e2\u00e4\3\2\2\2\u00e3\u00da")
        buf.write("\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6")
        buf.write("\7-\2\2\u00e6\u00e7\7*\2\2\u00e7\u00e8\b\24\1\2\u00e8")
        buf.write("\u00f9\b\24\1\2\u00e9\u00ea\7*\2\2\u00ea\u00eb\b\24\1")
        buf.write("\2\u00eb\u00f9\b\24\1\2\u00ec\u00ed\7\23\2\2\u00ed\u00ee")
        buf.write("\b\24\1\2\u00ee\u00f9\b\24\1\2\u00ef\u00f0\7\24\2\2\u00f0")
        buf.write("\u00f1\b\24\1\2\u00f1\u00f9\b\24\1\2\u00f2\u00f3\7+\2")
        buf.write("\2\u00f3\u00f4\b\24\1\2\u00f4\u00f9\b\24\1\2\u00f5\u00f6")
        buf.write("\7)\2\2\u00f6\u00f7\b\24\1\2\u00f7\u00f9\b\24\1\2\u00f8")
        buf.write("\u00e5\3\2\2\2\u00f8\u00e9\3\2\2\2\u00f8\u00ec\3\2\2\2")
        buf.write("\u00f8\u00ef\3\2\2\2\u00f8\u00f2\3\2\2\2\u00f8\u00f5\3")
        buf.write("\2\2\2\u00f9\'\3\2\2\2\u00fa\u00fb\5*\26\2\u00fb\u00fc")
        buf.write("\7\37\2\2\u00fc\u00fd\7)\2\2\u00fd\u00fe\b\25\1\2\u00fe")
        buf.write("\u00ff\b\25\1\2\u00ff\u0100\b\25\1\2\u0100\u0110\7\4\2")
        buf.write("\2\u0101\u0102\5\b\5\2\u0102\u0103\7)\2\2\u0103\u0104")
        buf.write("\b\25\1\2\u0104\u010d\b\25\1\2\u0105\u0106\7\6\2\2\u0106")
        buf.write("\u0107\5\b\5\2\u0107\u0108\7)\2\2\u0108\u0109\b\25\1\2")
        buf.write("\u0109\u010a\b\25\1\2\u010a\u010c\3\2\2\2\u010b\u0105")
        buf.write("\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2")
        buf.write("\u0110\u0101\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0113\7\5\2\2\u0113\u0114\7\32\2\2\u0114")
        buf.write("\u0115\5,\27\2\u0115\u0116\7 \2\2\u0116\u0118\7\4\2\2")
        buf.write("\u0117\u0119\5\f\7\2\u0118\u0117\3\2\2\2\u0118\u0119\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\7\5\2\2\u011b\u011c")
        buf.write("\7\33\2\2\u011c\u011d\b\25\1\2\u011d\u011e\b\25\1\2\u011e")
        buf.write("\u011f\b\25\1\2\u011f)\3\2\2\2\u0120\u0121\5\b\5\2\u0121")
        buf.write("\u0122\b\26\1\2\u0122\u0126\3\2\2\2\u0123\u0124\7\'\2")
        buf.write("\2\u0124\u0126\b\26\1\2\u0125\u0120\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126+\3\2\2\2\u0127\u0130\5\6\4\2\u0128\u0130")
        buf.write("\5\20\t\2\u0129\u0130\5\22\n\2\u012a\u0130\5\26\f\2\u012b")
        buf.write("\u0130\5\30\r\2\u012c\u0130\5\16\b\2\u012d\u0130\5\62")
        buf.write("\32\2\u012e\u0130\5.\30\2\u012f\u0127\3\2\2\2\u012f\u0128")
        buf.write("\3\2\2\2\u012f\u0129\3\2\2\2\u012f\u012a\3\2\2\2\u012f")
        buf.write("\u012b\3\2\2\2\u012f\u012c\3\2\2\2\u012f\u012d\3\2\2\2")
        buf.write("\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3")
        buf.write("\2\2\2\u0131\u0132\3\2\2\2\u0132-\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0134\u0135\7)\2\2\u0135\u0136\b\30\1\2\u0136")
        buf.write("\u0142\7\4\2\2\u0137\u0138\5\f\7\2\u0138\u013f\b\30\1")
        buf.write("\2\u0139\u013a\7\6\2\2\u013a\u013b\5\f\7\2\u013b\u013c")
        buf.write("\b\30\1\2\u013c\u013e\3\2\2\2\u013d\u0139\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0137\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145")
        buf.write("\7\5\2\2\u0145\u0146\b\30\1\2\u0146/\3\2\2\2\u0147\u0150")
        buf.write("\7\7\2\2\u0148\u014d\5\32\16\2\u0149\u014a\7\6\2\2\u014a")
        buf.write("\u014c\5\32\16\2\u014b\u0149\3\2\2\2\u014c\u014f\3\2\2")
        buf.write("\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0151")
        buf.write("\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0148\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\7\b\2\2")
        buf.write("\u0153\61\3\2\2\2\u0154\u0155\7)\2\2\u0155\u0165\7\t\2")
        buf.write("\2\u0156\u0157\t\3\2\2\u0157\u0158\7\4\2\2\u0158\u0166")
        buf.write("\7\5\2\2\u0159\u015a\t\4\2\2\u015a\u015b\7\4\2\2\u015b")
        buf.write("\u015c\5\32\16\2\u015c\u015d\7\5\2\2\u015d\u0166\3\2\2")
        buf.write("\2\u015e\u015f\7&\2\2\u015f\u0160\7\4\2\2\u0160\u0161")
        buf.write("\5\32\16\2\u0161\u0162\7\6\2\2\u0162\u0163\5\32\16\2\u0163")
        buf.write("\u0164\7\5\2\2\u0164\u0166\3\2\2\2\u0165\u0156\3\2\2\2")
        buf.write("\u0165\u0159\3\2\2\2\u0165\u015e\3\2\2\2\u0166\63\3\2")
        buf.write("\2\2\u0167\u016a\5\60\31\2\u0168\u0169\7,\2\2\u0169\u016b")
        buf.write("\5\60\31\2\u016a\u0168\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\65\3\2\2\2\37")
        buf.write("EGY]c\u0087\u0089\u0099\u00a6\u00ad\u00b6\u00c0\u00c7")
        buf.write("\u00d0\u00d7\u00e3\u00f8\u010d\u0110\u0118\u0125\u012f")
        buf.write("\u0131\u013f\u0142\u014d\u0150\u0165\u016c")
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
    RULE_op_contenedor = 24
    RULE_concat_contenedor = 25

    ruleNames =  [ "visionscript", "programa", "variable", "tipo", "todo", 
                   "casi_todo", "asignacion", "condicion", "ciclo", "bloque", 
                   "read", "imprimir", "mega_expresion", "expresion", "exp_todo", 
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
        self.checkVersion("4.7.1")
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
            self.state = 53
            self.programa()
            self.state = 54
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
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.VOID) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 67
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 58
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 59
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 60
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 61
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 62
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 63
                    self.function()
                    pass

                elif la_ == 7:
                    self.state = 64
                    self.function_call()
                    pass

                elif la_ == 8:
                    self.state = 65
                    self.asignacion()
                    pass

                elif la_ == 9:
                    self.state = 66
                    self.op_contenedor()
                    pass


                self.state = 71
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
            self.state = 72
            localctx._tipo = self.tipo()
            self.state = 73
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 74
            self.match(VisionScriptParser.T__0)
            self.state = 75
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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                localctx._NUMBER = self.match(VisionScriptParser.NUMBER)
                localctx.type = (None if localctx._NUMBER is None else localctx._NUMBER.text)
                pass
            elif token in [VisionScriptParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                localctx._TEXT = self.match(VisionScriptParser.TEXT)
                localctx.type = (None if localctx._TEXT is None else localctx._TEXT.text)
                pass
            elif token in [VisionScriptParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                localctx._BOOL = self.match(VisionScriptParser.BOOL)
                localctx.type = (None if localctx._BOOL is None else localctx._BOOL.text)
                pass
            elif token in [VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.casi_todo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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


        def op_contenedor(self):
            return self.getTypedRuleContext(VisionScriptParser.Op_contenedorContext,0)


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
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.mega_expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.concat_contenedor()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.contenedor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
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
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            localctx._ID = self.match(VisionScriptParser.ID)
            self.state = 100
            self.match(VisionScriptParser.T__0)
            self.state = 101
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
            self.state = 105
            self.match(VisionScriptParser.IF)
            self.state = 106
            self.mega_expresion()
            cuadruplos.FuncionIF1()
            self.state = 108
            self.match(VisionScriptParser.BEGIN)
            self.state = 109
            self.bloque()
            self.state = 110
            self.match(VisionScriptParser.ELSE)
            cuadruplos.FuncionIF2()
            self.state = 112
            self.bloque()
            self.state = 113
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
            self.state = 116
            self.match(VisionScriptParser.REPEAT)
            self.state = 117
            self.match(VisionScriptParser.UNTIL)
            cuadruplos.FuncionRepUntil1()
            self.state = 119
            self.mega_expresion()
            cuadruplos.FuncionRepUntil2()
            self.state = 121
            self.match(VisionScriptParser.BEGIN)
            self.state = 122
            self.bloque()
            self.state = 123
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
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 126
                    self.condicion()
                    pass

                elif la_ == 2:
                    self.state = 127
                    self.ciclo()
                    pass

                elif la_ == 3:
                    self.state = 128
                    self.read()
                    pass

                elif la_ == 4:
                    self.state = 129
                    self.imprimir()
                    pass

                elif la_ == 5:
                    self.state = 130
                    self.asignacion()
                    pass

                elif la_ == 6:
                    self.state = 131
                    self.op_contenedor()
                    pass

                elif la_ == 7:
                    self.state = 132
                    self.function_call()
                    pass


                self.state = 137
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
            self.state = 138
            localctx._READ = self.match(VisionScriptParser.READ)
            self.state = 139
            self.match(VisionScriptParser.T__1)
            self.state = 140
            localctx._ID = self.match(VisionScriptParser.ID)
            cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)),func_dir.returnIDType(func_dir.currentFunction, (None if localctx._ID is None else localctx._ID.text)))
            self.state = 142
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.BRAILLE]:
                self.state = 145
                localctx._BRAILLE = self.match(VisionScriptParser.BRAILLE)
                localctx.flag = (None if localctx._BRAILLE is None else localctx._BRAILLE.text)
                pass
            elif token in [VisionScriptParser.PRINT]:
                self.state = 147
                localctx._PRINT = self.match(VisionScriptParser.PRINT)
                localctx.flag = (None if localctx._PRINT is None else localctx._PRINT.text)
                pass
            elif token in [VisionScriptParser.HEAR]:
                self.state = 149
                localctx._HEAR = self.match(VisionScriptParser.HEAR)
                localctx.flag = (None if localctx._HEAR is None else localctx._HEAR.text)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 153
            self.match(VisionScriptParser.T__1)
            self.state = 154
            self.todo()
            self.state = 155
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
            self.state = 158
            self.expresion()
            cuadruplos.GenerateCuad('Mega_Expresion')
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.AND or _la==VisionScriptParser.OR:
                self.state = 164
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.AND]:
                    self.state = 160
                    localctx._AND = self.match(VisionScriptParser.AND)
                    cuadruplos.InsertOperator((None if localctx._AND is None else localctx._AND.text))
                    pass
                elif token in [VisionScriptParser.OR]:
                    self.state = 162
                    localctx._OR = self.match(VisionScriptParser.OR)
                    cuadruplos.InsertOperator((None if localctx._OR is None else localctx._OR.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 166
                self.expresion()
                cuadruplos.GenerateCuad('Mega_Expresion')
                self.state = 173
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
            self.state = 174
            self.exp()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.EQUAL) | (1 << VisionScriptParser.NOT_EQUAL) | (1 << VisionScriptParser.GREATER) | (1 << VisionScriptParser.GREATER_EQUAL) | (1 << VisionScriptParser.LESS) | (1 << VisionScriptParser.LESS_EQUAL))) != 0):
                self.state = 175
                localctx._exp_todo = self.exp_todo()
                cuadruplos.InsertOperator((None if localctx._exp_todo is None else self._input.getText((localctx._exp_todo.start,localctx._exp_todo.stop))))
                self.state = 177
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
            self.state = 182
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
            self.state = 184
            self.termino()
            cuadruplos.GenerateCuad('Termino')
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.PLUS or _la==VisionScriptParser.MINUS:
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.PLUS]:
                    self.state = 186
                    localctx._PLUS = self.match(VisionScriptParser.PLUS)
                    cuadruplos.InsertOperator((None if localctx._PLUS is None else localctx._PLUS.text))
                    pass
                elif token in [VisionScriptParser.MINUS]:
                    self.state = 188
                    localctx._MINUS = self.match(VisionScriptParser.MINUS)
                    cuadruplos.InsertOperator((None if localctx._MINUS is None else localctx._MINUS.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 192
                self.termino()
                cuadruplos.GenerateCuad('Termino')
                self.state = 199
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
            self.state = 200
            self.factor()
            cuadruplos.GenerateCuad('Factor')
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==VisionScriptParser.DIVISION or _la==VisionScriptParser.MULTIPLICATION:
                self.state = 206
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [VisionScriptParser.MULTIPLICATION]:
                    self.state = 202
                    localctx._MULTIPLICATION = self.match(VisionScriptParser.MULTIPLICATION)
                    cuadruplos.InsertOperator((None if localctx._MULTIPLICATION is None else localctx._MULTIPLICATION.text))
                    pass
                elif token in [VisionScriptParser.DIVISION]:
                    self.state = 204
                    localctx._DIVISION = self.match(VisionScriptParser.DIVISION)
                    cuadruplos.InsertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 208
                self.factor()
                cuadruplos.GenerateCuad('Factor')
                self.state = 215
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
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(VisionScriptParser.T__1)
                cuadruplos.InsertParentesis()
                self.state = 218
                self.mega_expresion()
                self.state = 219
                self.match(VisionScriptParser.T__2)
                cuadruplos.RemoveParentesis()
                pass
            elif token in [VisionScriptParser.CTBF, VisionScriptParser.CTBT, VisionScriptParser.ID, VisionScriptParser.CTN, VisionScriptParser.CTT, VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
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
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(VisionScriptParser.MINUS)
                self.state = 228
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = func_dir.ConstDeclaration(localctx.type , '-'+(None if localctx._CTN is None else localctx._CTN.text) )
                pass
            elif token in [VisionScriptParser.CTN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                localctx._CTN = self.match(VisionScriptParser.CTN)
                localctx.type = 'number'
                localctx.value = func_dir.ConstDeclaration(localctx.type , (None if localctx._CTN is None else localctx._CTN.text) )
                pass
            elif token in [VisionScriptParser.CTBF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                localctx._CTBF = self.match(VisionScriptParser.CTBF)
                localctx.type = 'bool'
                localctx.value = func_dir.ConstDeclaration(localctx.type ,(None if localctx._CTBF is None else localctx._CTBF.text) )
                pass
            elif token in [VisionScriptParser.CTBT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                localctx._CTBT = self.match(VisionScriptParser.CTBT)
                localctx.type = 'bool'
                localctx.value = func_dir.ConstDeclaration(localctx.type , (None if localctx._CTBT is None else localctx._CTBT.text) )
                pass
            elif token in [VisionScriptParser.CTT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                localctx._CTT = self.match(VisionScriptParser.CTT)
                localctx.type = 'text'
                localctx.value = func_dir.ConstDeclaration(localctx.type , (None if localctx._CTT is None else localctx._CTT.text) )
                pass
            elif token in [VisionScriptParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
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
            self.state = 248
            localctx._function_type = self.function_type()
            self.state = 249
            self.match(VisionScriptParser.FUNCTION)
            self.state = 250
            localctx._ID = self.match(VisionScriptParser.ID)
            cuadruplos.GenerateFunGoto()
            func_dir.currentFunction = (None if localctx._ID is None else localctx._ID.text)
            func_dir.FuncDeclaration(func_dir.currentFunction,localctx._function_type.type)
            self.state = 254
            self.match(VisionScriptParser.T__1)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER))) != 0):
                self.state = 255
                localctx._tipo = self.tipo()
                self.state = 256
                localctx._ID = self.match(VisionScriptParser.ID)
                func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                func_dir.ParamDeclaration(func_dir.currentFunction,localctx._tipo.type)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 259
                    self.match(VisionScriptParser.T__3)
                    self.state = 260
                    localctx._tipo = self.tipo()
                    self.state = 261
                    localctx._ID = self.match(VisionScriptParser.ID)
                    func_dir.VarDeclaration(func_dir.currentFunction,(None if localctx._ID is None else localctx._ID.text),localctx._tipo.type,'@parameter')
                    func_dir.ParamDeclaration(func_dir.currentFunction,localctx._tipo.type)
                    self.state = 269
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 272
            self.match(VisionScriptParser.T__2)
            self.state = 273
            self.match(VisionScriptParser.BEGIN)
            self.state = 274
            self.func_bloque()
            self.state = 275
            self.match(VisionScriptParser.RETURN)
            self.state = 276
            self.match(VisionScriptParser.T__1)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 277
                self.casi_todo()


            self.state = 280
            self.match(VisionScriptParser.T__2)
            self.state = 281
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
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.NUMBER, VisionScriptParser.TEXT, VisionScriptParser.BOOL, VisionScriptParser.CONTAINER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                localctx._tipo = self.tipo()
                localctx.type = localctx._tipo.type
                pass
            elif token in [VisionScriptParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.READ) | (1 << VisionScriptParser.PRINT) | (1 << VisionScriptParser.HEAR) | (1 << VisionScriptParser.BRAILLE) | (1 << VisionScriptParser.IF) | (1 << VisionScriptParser.NUMBER) | (1 << VisionScriptParser.TEXT) | (1 << VisionScriptParser.BOOL) | (1 << VisionScriptParser.CONTAINER) | (1 << VisionScriptParser.REPEAT) | (1 << VisionScriptParser.ID))) != 0):
                self.state = 301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 293
                    self.variable()
                    pass

                elif la_ == 2:
                    self.state = 294
                    self.condicion()
                    pass

                elif la_ == 3:
                    self.state = 295
                    self.ciclo()
                    pass

                elif la_ == 4:
                    self.state = 296
                    self.read()
                    pass

                elif la_ == 5:
                    self.state = 297
                    self.imprimir()
                    pass

                elif la_ == 6:
                    self.state = 298
                    self.asignacion()
                    pass

                elif la_ == 7:
                    self.state = 299
                    self.op_contenedor()
                    pass

                elif la_ == 8:
                    self.state = 300
                    self.function_call()
                    pass


                self.state = 305
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
            self.state = 306
            localctx._ID = self.match(VisionScriptParser.ID)
            cuadruplos.GenerateEra((None if localctx._ID is None else localctx._ID.text))
            self.state = 308
            self.match(VisionScriptParser.T__1)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.T__4) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 309
                self.casi_todo()
                cuadruplos.GenerateParameter(func_dir.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 311
                    self.match(VisionScriptParser.T__3)
                    self.state = 312
                    self.casi_todo()
                    cuadruplos.GenerateParameter(func_dir.ReturnParams((None if localctx._ID is None else localctx._ID.text)),(None if localctx._ID is None else localctx._ID.text))
                    self.state = 319
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 322
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
            self.state = 325
            self.match(VisionScriptParser.T__4)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.T__1) | (1 << VisionScriptParser.CTBF) | (1 << VisionScriptParser.CTBT) | (1 << VisionScriptParser.ID) | (1 << VisionScriptParser.CTN) | (1 << VisionScriptParser.CTT) | (1 << VisionScriptParser.MINUS))) != 0):
                self.state = 326
                self.mega_expresion()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==VisionScriptParser.T__3:
                    self.state = 327
                    self.match(VisionScriptParser.T__3)
                    self.state = 328
                    self.mega_expresion()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 336
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
        self.enterRule(localctx, 48, self.RULE_op_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(VisionScriptParser.ID)
            self.state = 339
            self.match(VisionScriptParser.T__6)
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [VisionScriptParser.GET_BACK, VisionScriptParser.GET_FRONT, VisionScriptParser.LENGTH]:
                self.state = 340
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.GET_BACK) | (1 << VisionScriptParser.GET_FRONT) | (1 << VisionScriptParser.LENGTH))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 341
                self.match(VisionScriptParser.T__1)
                self.state = 342
                self.match(VisionScriptParser.T__2)
                pass
            elif token in [VisionScriptParser.GET, VisionScriptParser.INSERT_BACK, VisionScriptParser.INSERT_FRONT]:
                self.state = 343
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << VisionScriptParser.GET) | (1 << VisionScriptParser.INSERT_BACK) | (1 << VisionScriptParser.INSERT_FRONT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 344
                self.match(VisionScriptParser.T__1)
                self.state = 345
                self.mega_expresion()
                self.state = 346
                self.match(VisionScriptParser.T__2)
                pass
            elif token in [VisionScriptParser.INSERT]:
                self.state = 348
                self.match(VisionScriptParser.INSERT)
                self.state = 349
                self.match(VisionScriptParser.T__1)
                self.state = 350
                self.mega_expresion()
                self.state = 351
                self.match(VisionScriptParser.T__3)
                self.state = 352
                self.mega_expresion()
                self.state = 353
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
        self.enterRule(localctx, 50, self.RULE_concat_contenedor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.contenedor()
            self.state = 360 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 358
                self.match(VisionScriptParser.PLUS)
                self.state = 359
                self.contenedor()
                self.state = 362 
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





