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


- Hacer cuadruplos para funciones: Tenemos que meter un Goto al principio de cada definicion que te mande a el final de la funcion y guardar la direccion de esa funcion para sus llamadas

- Cuando se cree un container no se debe de meter a el PType ni al Poper
- i.e.: container a = [1,x-2,3] Se traduce a:
    - [ =       ,   []  ,   -   ,   t1]
    - [append   ,   1   ,   -   ,   t1]
    - [ -       ,   x   ,   2   ,   t2]
    - [append   ,   t2  ,   -   ,   t1]
    - [append   ,   3   ,   -   ,   t1]
    - [ =       ,   t1  ,   -   ,   a ]

- Checar que no se pueda guardar una variable de tipo container dentro de un container
- i.e.: 
    - container a = [1,2,3]
    - container b = [a,1]

- Hacer cuadruplos para la concatenacion de contenedores
- i.e.:
    - container a = [1,2] + ["A",false]
    - [ =       ,   []  ,   -   ,   t2]
    - [append   ,   1   ,   -   ,   t2]
    - [append   ,   2   ,   -   ,   t2]
    - [ =       ,   []  ,   -   ,   t3]
    - [append   ,  "A"  ,   -   ,   t3]
    - [append   , false ,   -   ,   t3]
    - [ =       ,   []  ,   -   ,   t4]
    - [concat   , t2    ,   t3  ,   t4]
    - [ =       ,   t4  ,   -   ,   a ]

- Hacer cuadruplos para las funciones de contenedores
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



		