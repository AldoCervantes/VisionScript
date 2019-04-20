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

#Si en la maquina virtual no sabes como diferenciar en el tipo de a donde lo vamos a guardar
- i.e.: 
    number a = 0
    container n = [true,false,1]

    a = n.get(0) // Deberia de marcar error porque estas intentando guardar un false en una variable de tipo number

    **Solucion, en el cuadruplo de asignacion podemos mandar el tipo como 3 elemento ['=',valor, tipo, id]

#INSERT FRONT
arr.insert(0,10)

#INSERT BACK
arr.append(10)

#INSERT 
arr.insert(3,12)

#GET
arr[2]

#GET_BACK
arr[len(arr)-1]

#GET_FRONT
arr[0]

#LENGTH
len(arr)

- REVISAR SI ES BUENO METER POPs COMO FUNCIONES ADICIONALES DE CONTAINERS
#list.pop(index)
print(arr)


#TODO
X TRADUCIR TODO A CODIGOS ** SOLO FALTAN NOMBRES DE FUNCIONES Y EL FLAG DE [] contenedor vacio **
X Validar que sea un number en las op_contenedor
X Validar que el Return sea del mismo tipo que la funcion
- COMO SE HACE UNA ASIGNACION DE UNA OP_CONTENEDOR
- PREGUNTAR: COMO SE HACE UNA ASIGNACION DE UNA FUNCTION CALL

- Generar los 4 arreglos (Global, Local, Constantes, Temporales)
- Sumas, Resta, Multipliacion, Division
- Prints


#EJEMPLO
number a = 10

number b = 20

number c = 10+20/30*40-80

number y = a + b

0 [0, 30000, -1, 10000]
1 [0, 30001, -1, 10001]
2 [4, 30001, 30002, 40000]
3 [3, 40000, 30003, 40001]
4 [1, 30000, 40001, 40002]
5 [2, 40002, 30004, 40003]
6 [0, 40003, -1, 10002]
7 [1, 10000, 10001, 40004]
8 [0, 40004, -1, 10003]