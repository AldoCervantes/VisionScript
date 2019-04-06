# Compiladores
ProjectoFinal


#EN JAVA
1 --> antlr4 VisionScript.g4

2 -->  javac VisionScript*.java

3 --> grun VisionScript visionscript -tokens -gui sampleCode.txt

#EN PYTHON
1 --> antlr4 -Dlanguage=Python3 VisionScript.g4

2 --> python VisionScriptRunner.py sampleCode.txt


#print (self.funDirectory['@global'])
- ['void', {'n': ['number', '1']}] => all info of the function

#print (self.funDirectory['@global'][0])
- void => function type

# print (self.funDirectory['@global'][0]['n'])
- ['number', '1'] => var directory

# print (self.funDirectory['@global'][0]['n'][0])
- number => variable type

# print (self.funDirectory['@global'][0]['n'][1])
- 1 => variable value



- Hacer cuadruplos Prints(3 tipos), Read
- Hacer cuadruplos para if
- Hacer cuadruplos para los repeat
- Hacer cuadruplos para funciones