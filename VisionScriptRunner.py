import sys
from antlr4 import *
from VisionScriptLexer import VisionScriptLexer
from VisionScriptParser import VisionScriptParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = VisionScriptLexer(input)
    stream = CommonTokenStream(lexer)
    parser = VisionScriptParser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)