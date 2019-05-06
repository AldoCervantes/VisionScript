#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from antlr4 import *
from VisionScriptLexer import VisionScriptLexer
from VisionScriptParser import VisionScriptParser


def main(argv):
    # Tipo de entrada: Archivo de texto recibido como parametro 
    inputFile = FileStream(argv[1], encoding = 'utf8')
    lexer = VisionScriptLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = VisionScriptParser(stream)
    # Nombre de la primer regla de la gramática
    tree = parser.visionscript()
    # Imprimiendo el árbol
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)