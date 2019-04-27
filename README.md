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
X COMO SE HACE UNA ASIGNACION DE UNA OP_CONTENEDOR
X PREGUNTAR: COMO SE HACE UNA ASIGNACION DE UNA FUNCTION CALL
X CAMBIAR LOS TEMPORALES A GLOBALES O LOCALES
X PONER LA CANTIDAD DE VARIABLES LOCALES EN EL ERA
X HACER EL CUADRUPLO DE ENDPROC
X Generar los 3 arreglos (Global, Local, Constantes)
X Sumas, Resta, Multipliacion, Division
X Prints
X Read


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

# PARA LOCALES USAR UN STACK DE ARREGLOS
###          Locales = []
#CUANDO VIENE UN ERA HACES UN APPEND DE UN ARREGLO COMO EL DE GLOBALES PERO DENTRO DEL STACK
# *** EL ERA DEBE DE DECIRTE CUANTAS VARIABLES VAS A USAR ****
##           Locales.append([0...ERA size])
# CUANDO TERMINA LA FUNCION HACES POP AL STACK DE LOCALES CON EL ENDPROC

*** HAY QUE METER EN EL ERA CUANTAS VARIABLES LOCALES TIENE LA FUNCION ***
*** HA QUE GENERAR EL CUADRUPLO PARA ENDPROC ****



TODO: 
*Validar que el tipo de valor que regresa un op_contenedor sea igual al de la variable donde se va a guardar
print("TODO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

*Hacer todo los relacionado a Funciones
Pasos:
return => Es guardar el valor en la variable
ERA => Es generar un arreglo del tamaño que dice el era en la pila de Locales
param => es asignar el valor a la variable de la funcion
gosub => Es hacer un goto a la linea donde esta la funcion
ENDPROC => es hacer un pop a la pila de locales