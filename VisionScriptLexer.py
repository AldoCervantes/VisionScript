# Generated from VisionScript.g4 by ANTLR 4.7.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0197\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\6+\u0153\n+\r+\16+\u0154\3+\3+\3+\3+\7+\u015b\n+")
        buf.write("\f+\16+\u015e\13+\3,\6,\u0161\n,\r,\16,\u0162\3,\3,\6")
        buf.write(",\u0167\n,\r,\16,\u0168\7,\u016b\n,\f,\16,\u016e\13,\3")
        buf.write("-\3-\7-\u0172\n-\f-\16-\u0175\13-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\5\67\u0190\n")
        buf.write("\67\3\67\3\67\5\67\u0194\n\67\3\67\3\67\3\u0173\28\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2\27\n\31\13\33")
        buf.write("\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63")
        buf.write("\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'")
        buf.write("S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65\3\2\6\3\2c|\3")
        buf.write("\2C\\\3\2\62;\4\2\13\13\"\"\2\u019f\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5q")
        buf.write("\3\2\2\2\7s\3\2\2\2\tu\3\2\2\2\13w\3\2\2\2\ry\3\2\2\2")
        buf.write("\17{\3\2\2\2\21}\3\2\2\2\23\177\3\2\2\2\25\u0081\3\2\2")
        buf.write("\2\27\u0083\3\2\2\2\31\u0088\3\2\2\2\33\u008e\3\2\2\2")
        buf.write("\35\u0093\3\2\2\2\37\u009b\3\2\2\2!\u009e\3\2\2\2#\u00a3")
        buf.write("\3\2\2\2%\u00aa\3\2\2\2\'\u00af\3\2\2\2)\u00b4\3\2\2\2")
        buf.write("+\u00ba\3\2\2\2-\u00bf\3\2\2\2/\u00c3\3\2\2\2\61\u00c6")
        buf.write("\3\2\2\2\63\u00cc\3\2\2\2\65\u00d6\3\2\2\2\67\u00e0\3")
        buf.write("\2\2\29\u00e6\3\2\2\2;\u00ea\3\2\2\2=\u00f1\3\2\2\2?\u00f7")
        buf.write("\3\2\2\2A\u00fd\3\2\2\2C\u0106\3\2\2\2E\u010d\3\2\2\2")
        buf.write("G\u0116\3\2\2\2I\u0120\3\2\2\2K\u0124\3\2\2\2M\u0130\3")
        buf.write("\2\2\2O\u013d\3\2\2\2Q\u0144\3\2\2\2S\u0149\3\2\2\2U\u0152")
        buf.write("\3\2\2\2W\u0160\3\2\2\2Y\u016f\3\2\2\2[\u0178\3\2\2\2")
        buf.write("]\u017a\3\2\2\2_\u017c\3\2\2\2a\u017e\3\2\2\2c\u0180\3")
        buf.write("\2\2\2e\u0182\3\2\2\2g\u0185\3\2\2\2i\u0187\3\2\2\2k\u018a")
        buf.write("\3\2\2\2m\u0193\3\2\2\2op\7?\2\2p\4\3\2\2\2qr\7*\2\2r")
        buf.write("\6\3\2\2\2st\7+\2\2t\b\3\2\2\2uv\7.\2\2v\n\3\2\2\2wx\7")
        buf.write("]\2\2x\f\3\2\2\2yz\7_\2\2z\16\3\2\2\2{|\7\60\2\2|\20\3")
        buf.write("\2\2\2}~\t\2\2\2~\22\3\2\2\2\177\u0080\t\3\2\2\u0080\24")
        buf.write("\3\2\2\2\u0081\u0082\t\4\2\2\u0082\26\3\2\2\2\u0083\u0084")
        buf.write("\7t\2\2\u0084\u0085\7g\2\2\u0085\u0086\7c\2\2\u0086\u0087")
        buf.write("\7f\2\2\u0087\30\3\2\2\2\u0088\u0089\7r\2\2\u0089\u008a")
        buf.write("\7t\2\2\u008a\u008b\7k\2\2\u008b\u008c\7p\2\2\u008c\u008d")
        buf.write("\7v\2\2\u008d\32\3\2\2\2\u008e\u008f\7j\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\u0091\7c\2\2\u0091\u0092\7t\2\2\u0092\34")
        buf.write("\3\2\2\2\u0093\u0094\7d\2\2\u0094\u0095\7t\2\2\u0095\u0096")
        buf.write("\7c\2\2\u0096\u0097\7k\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\u009a\7g\2\2\u009a\36\3\2\2\2\u009b\u009c")
        buf.write("\7k\2\2\u009c\u009d\7h\2\2\u009d \3\2\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\"\3\2\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5")
        buf.write("\7w\2\2\u00a5\u00a6\7o\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\u00a9\7t\2\2\u00a9$\3\2\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7z\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae&\3\2\2\2\u00af\u00b0\7d\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7n\2\2\u00b3(\3")
        buf.write("\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9*\3")
        buf.write("\2\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7w\2\2\u00bd\u00be\7g\2\2\u00be,\3\2\2\2\u00bf\u00c0")
        buf.write("\7c\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7f\2\2\u00c2.\3")
        buf.write("\2\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7t\2\2\u00c5\60")
        buf.write("\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7s\2\2\u00c8\u00c9")
        buf.write("\7w\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7n\2\2\u00cb\62")
        buf.write("\3\2\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7v\2\2\u00cf\u00d0\7a\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7s\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\64\3\2\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7t\2\2\u00df\66\3\2\2\2\u00e0\u00e1")
        buf.write("\7d\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7i\2\2\u00e3\u00e4")
        buf.write("\7k\2\2\u00e4\u00e5\7p\2\2\u00e58\3\2\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7f\2\2\u00e9:\3")
        buf.write("\2\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7r\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7c\2\2\u00ef\u00f0")
        buf.write("\7v\2\2\u00f0<\3\2\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7o\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6")
        buf.write("\7u\2\2\u00f6>\3\2\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc")
        buf.write("\7n\2\2\u00fc@\3\2\2\2\u00fd\u00fe\7h\2\2\u00fe\u00ff")
        buf.write("\7w\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7e\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7k\2\2\u0103\u0104\7q\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105B\3\2\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a\7w\2\2\u010a\u010b")
        buf.write("\7t\2\2\u010b\u010c\7p\2\2\u010cD\3\2\2\2\u010d\u010e")
        buf.write("\7i\2\2\u010e\u010f\7g\2\2\u010f\u0110\7v\2\2\u0110\u0111")
        buf.write("\7a\2\2\u0111\u0112\7d\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7e\2\2\u0114\u0115\7m\2\2\u0115F\3\2\2\2\u0116\u0117")
        buf.write("\7i\2\2\u0117\u0118\7g\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7a\2\2\u011a\u011b\7h\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011fH\3")
        buf.write("\2\2\2\u0120\u0121\7i\2\2\u0121\u0122\7g\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123J\3\2\2\2\u0124\u0125\7k\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\u0127\7u\2\2\u0127\u0128\7g\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7v\2\2\u012a\u012b\7a\2\2\u012b\u012c")
        buf.write("\7d\2\2\u012c\u012d\7c\2\2\u012d\u012e\7e\2\2\u012e\u012f")
        buf.write("\7m\2\2\u012fL\3\2\2\2\u0130\u0131\7k\2\2\u0131\u0132")
        buf.write("\7p\2\2\u0132\u0133\7u\2\2\u0133\u0134\7g\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135\u0136\7v\2\2\u0136\u0137\7a\2\2\u0137\u0138")
        buf.write("\7h\2\2\u0138\u0139\7t\2\2\u0139\u013a\7q\2\2\u013a\u013b")
        buf.write("\7p\2\2\u013b\u013c\7v\2\2\u013cN\3\2\2\2\u013d\u013e")
        buf.write("\7k\2\2\u013e\u013f\7p\2\2\u013f\u0140\7u\2\2\u0140\u0141")
        buf.write("\7g\2\2\u0141\u0142\7t\2\2\u0142\u0143\7v\2\2\u0143P\3")
        buf.write("\2\2\2\u0144\u0145\7x\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7k\2\2\u0147\u0148\7f\2\2\u0148R\3\2\2\2\u0149\u014a")
        buf.write("\7n\2\2\u014a\u014b\7g\2\2\u014b\u014c\7p\2\2\u014c\u014d")
        buf.write("\7i\2\2\u014d\u014e\7v\2\2\u014e\u014f\7j\2\2\u014fT\3")
        buf.write("\2\2\2\u0150\u0153\5\23\n\2\u0151\u0153\5\21\t\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u015c\3")
        buf.write("\2\2\2\u0156\u015b\5\23\n\2\u0157\u015b\5\21\t\2\u0158")
        buf.write("\u015b\5\25\13\2\u0159\u015b\7a\2\2\u015a\u0156\3\2\2")
        buf.write("\2\u015a\u0157\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015dV\3\2\2\2\u015e\u015c\3\2\2\2\u015f")
        buf.write("\u0161\5\25\13\2\u0160\u015f\3\2\2\2\u0161\u0162\3\2\2")
        buf.write("\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u016c")
        buf.write("\3\2\2\2\u0164\u0166\7\60\2\2\u0165\u0167\5\25\13\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2")
        buf.write("\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0164\3")
        buf.write("\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016dX\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0173")
        buf.write("\7$\2\2\u0170\u0172\13\2\2\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u0175\3\2\2\2\u0173\u0174\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0174\u0176\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u0177\7")
        buf.write("$\2\2\u0177Z\3\2\2\2\u0178\u0179\7-\2\2\u0179\\\3\2\2")
        buf.write("\2\u017a\u017b\7/\2\2\u017b^\3\2\2\2\u017c\u017d\7\61")
        buf.write("\2\2\u017d`\3\2\2\2\u017e\u017f\7,\2\2\u017fb\3\2\2\2")
        buf.write("\u0180\u0181\7@\2\2\u0181d\3\2\2\2\u0182\u0183\7@\2\2")
        buf.write("\u0183\u0184\7?\2\2\u0184f\3\2\2\2\u0185\u0186\7>\2\2")
        buf.write("\u0186h\3\2\2\2\u0187\u0188\7>\2\2\u0188\u0189\7?\2\2")
        buf.write("\u0189j\3\2\2\2\u018a\u018b\t\5\2\2\u018b\u018c\3\2\2")
        buf.write("\2\u018c\u018d\b\66\2\2\u018dl\3\2\2\2\u018e\u0190\7\17")
        buf.write("\2\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191\u0194\7\f\2\2\u0192\u0194\7\17\2\2\u0193")
        buf.write("\u018f\3\2\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0196\b\67\2\2\u0196n\3\2\2\2\r\2\u0152\u0154\u015a")
        buf.write("\u015c\u0162\u0168\u016c\u0173\u018f\u0193\3\b\2\2")
        return buf.getvalue()


class VisionScriptLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    READ = 8
    PRINT = 9
    HEAR = 10
    BRAILLE = 11
    IF = 12
    ELSE = 13
    NUMBER = 14
    TEXT = 15
    BOOL = 16
    CTBF = 17
    CTBT = 18
    AND = 19
    OR = 20
    EQUAL = 21
    NOT_EQUAL = 22
    CONTAINER = 23
    BEGIN = 24
    END = 25
    REPEAT = 26
    TIMES = 27
    UNTIL = 28
    FUNCTION = 29
    RETURN = 30
    GET_BACK = 31
    GET_FRONT = 32
    GET = 33
    INSERT_BACK = 34
    INSERT_FRONT = 35
    INSERT = 36
    VOID = 37
    LENGTH = 38
    ID = 39
    CTN = 40
    CTT = 41
    PLUS = 42
    MINUS = 43
    DIVISION = 44
    MULTIPLICATION = 45
    GREATER = 46
    GREATER_EQUAL = 47
    LESS = 48
    LESS_EQUAL = 49
    WHITESPACE = 50
    NEWLINE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "','", "'['", "']'", "'.'", "'read'", "'print'", 
            "'hear'", "'braille'", "'if'", "'else'", "'number'", "'text'", 
            "'bool'", "'false'", "'true'", "'and'", "'or'", "'equal'", "'not_equal'", 
            "'container'", "'begin'", "'end'", "'repeat'", "'times'", "'until'", 
            "'function'", "'return'", "'get_back'", "'get_front'", "'get'", 
            "'insert_back'", "'insert_front'", "'insert'", "'void'", "'length'", 
            "'+'", "'-'", "'/'", "'*'", "'>'", "'>='", "'<'", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "READ", "PRINT", "HEAR", "BRAILLE", "IF", "ELSE", "NUMBER", 
            "TEXT", "BOOL", "CTBF", "CTBT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
            "CONTAINER", "BEGIN", "END", "REPEAT", "TIMES", "UNTIL", "FUNCTION", 
            "RETURN", "GET_BACK", "GET_FRONT", "GET", "INSERT_BACK", "INSERT_FRONT", 
            "INSERT", "VOID", "LENGTH", "ID", "CTN", "CTT", "PLUS", "MINUS", 
            "DIVISION", "MULTIPLICATION", "GREATER", "GREATER_EQUAL", "LESS", 
            "LESS_EQUAL", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "LOWERCASE", "UPPERCASE", "DIGIT", "READ", "PRINT", "HEAR", 
                  "BRAILLE", "IF", "ELSE", "NUMBER", "TEXT", "BOOL", "CTBF", 
                  "CTBT", "AND", "OR", "EQUAL", "NOT_EQUAL", "CONTAINER", 
                  "BEGIN", "END", "REPEAT", "TIMES", "UNTIL", "FUNCTION", 
                  "RETURN", "GET_BACK", "GET_FRONT", "GET", "INSERT_BACK", 
                  "INSERT_FRONT", "INSERT", "VOID", "LENGTH", "ID", "CTN", 
                  "CTT", "PLUS", "MINUS", "DIVISION", "MULTIPLICATION", 
                  "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL", "WHITESPACE", 
                  "NEWLINE" ]

    grammarFileName = "VisionScript.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


