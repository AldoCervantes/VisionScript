import sys
from antlr4 import *
from VisionScriptLexer import VisionScriptLexer
from VisionScriptParser import VisionScriptParser


def main(argv):
    # Tipo de entrada: Archivo de texto recibido como parametro 
    input = FileStream(argv[1])
    lexer = VisionScriptLexer(input)
    stream = CommonTokenStream(lexer)
    parser = VisionScriptParser(stream)
    # Nombre de la primer regla de la gramática
    tree = parser.programa()
    # Imprimiendo el árbol
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)