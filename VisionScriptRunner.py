#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from antlr4 import *
from VisionScriptLexer import VisionScriptLexer
from VisionScriptParser import VisionScriptParser
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener( ErrorListener ):

    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print('#syntaxError Error: En la linea',line,'columna',column,msg)
        sys.exit()

def main(argv):
    # Tipo de entrada: Archivo de texto recibido como parametro 
    inputFile = FileStream(argv[1], encoding = 'utf8')
    lexer = VisionScriptLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = VisionScriptParser(stream)
    parser._listeners = [ MyErrorListener() ]
    # Nombre de la primer regla de la gramática
    tree = parser.visionscript()
    # Imprimiendo el árbol
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)