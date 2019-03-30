# Compiladores
ProjectoFinal


#EN JAVA
1 --> antlr4 VisionScript.g4

2 -->  javac VisionScript*.java

3 --> grun VisionScript visionscript -tokens -gui sampleCode.txt

#EN PYTHON
1 --> antlr4 -Dlanguage=Python3 VisionScript.g4

2 --> python VisionScriptRunner.py sampleCode.txt



Nos faltaría:
- Cambiar el arreglo provisional por localidades de memoria
- Agregar una nueva columna que represente su localidad de memoria
- Mandar el tipo de las id en lugar de su id
- Implementar la clase cuadruplos al momento de crear el directorio de funciones.
- Agregar al directorio de Funciones los parametros de las funciones como variables


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


number n = 1

n = ((1*2-3*4) > n + 2 * 5 / 6 ) and ( 7 * 8 - 9 > 10 - 1 ) and 2 + 3 > 4 * 6