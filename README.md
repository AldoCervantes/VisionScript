# VisionScript
Lenguaje de programación sencillo e inclusivo. Especial para personas con discapacidad visual.

## Versiones
### Antlr4
ANTLR Parser Generator  ```Version 4.7.2```
### Java
Javac ```1.8.0_144```
### Python
Python ```3.7.2```
### PIP
Pip ```version 19.0.2```
### PIP Packages
| Package                |      Version     |
| -------------          | -------------    |
|antlr4-python3-runtime |4.7.2|
|beautifulsoup4         |4.7.1|
|bs4                    |0.0.1|
|certifi                |2019.3.9|
|chardet                |3.0.4|
|Click                  |7.0|
|gTTS                   |2.0.3|
|gTTS-token             |1.1.3|
|idna                   |2.8|
|numpy                  |1.16.2|
|Pillow                 |6.0.0|
|pip                    |19.0.2|
|pygame                 |1.9.6|
|requests               |2.21.0|
|setuptools             |40.6.2|
|six                    |1.12.0|
|soupsieve              |1.9.1|
|urllib3                |1.24.3|

## Ejecutar
Pasos:
1. ```antlr4 -Dlanguage=Python3 VisionScript.g4```
2. ```python VisionScriptRunner.py NombredelArchivo.vs```


## Manual de Usuario
### Tipos de Variables
``` VisionScript ``` tiene los siguientes tipos:
- ``` number``` Puede ser cualquier número entero o decimal positivo o negativo
- ``` bool```   Es un valor entre ```false``` o ```true```
- ``` text```   Puede ser cualquier cadena de texto
- ``` container``` Simula una lista que puede guardar valores de cualquier tipo antes mencionado

### Declaración de Variables
Para declarar una variable es importante recordad que debe iniciar con una  ```letra``` seguido de cualquier cantidad de  ```letras```,  ```números``` ó ```_```

### Ejemplos de Variables
```
number Numero1 = 20
number numero_2 = 3.1416

text Texto_1 = "Cualquier Mensaje"
text texto_a = ""

bool Booleano_uno = false
bool booleanoDos = true

container contenedor_con_datos = [0,1,2,3,"A","B",false,true]
container ContenedorVacio = []
```

### Operaciones
```VisionScript``` posee los operadores básicos para realizar operaciones matemáticas: ```+, -, *, /``` y los operadores lógicos como ```<, >, <=, >=, equal, not_equal```

### Input/Output
```VisionScript``` cuenta con funciones especiales para leer valores desde la terminal y desplegar valores desde la terminal.Además de esto ```VisionScript``` cuenta con funciones especiales para imprimir resultados en formato braille e incluso convertir valores a audio y escuchar dicho audio.

#### Read
Está función permite guardar el valor leido desde terminal a una variable previamente definida.

###### Ejemplo:
```
number a = 0

read(a)

print(a + 1)
```
###### Input:
```
10
```
###### Output:
```
11
```
#### Print
Está función permite desplegar el valor dado dentro de los paréntesis en consola utilizando el formato del alfabeto latino.

###### Ejemplo:
```
print("Hola Mundo!")
```
###### Output:
```
Hola Mundo!
```

#### Braille
Está función permite desplegar el valor dado dentro de los paréntesis en consola utilizando el formato del alfabeto braille.

###### Ejemplo:
```
braille("Hola Mundo!")
```
###### Output:
```
⠓⠕⠇⠁ ⠍⠥⠝⠙⠕⠮
```
#### Hear
Está función permite escuchar el valor dado dentro de los paréntesis.

###### Ejemplo:
```
hear("Hola Mundo!")
```
###### Output:
```
Sonido por los altavoces: Hola Mundo!
```

### Ciclos y Condicionales
#### If Else
```VisionScript``` posee el típico ```if else```, sin embargo a diferencia de otros lenguajes ```VisionScript``` no usa ```{}``` para definir lo que está dentro del rango de cada condición, para definir esto se utilizan las palabras ```begin``` y ```end```, otro punto importante a destacar es todos los if's deben de ir acompañados de un else, esto con el objetivo de que las personas con discapacidad visual no tengan problemas al momento de escuchar o leer condiciones muy largas o anidadas.

###### Ejemplo:
```
number a = 10
number b = 12

if a > b
begin
   print(a)
else
   print(b)
end
```
###### Output:
```
12
```
#### Repeat Until
Otro aspecto muy importante es a la hora de definir un ciclo, a diferencia de otros lenguajes ```VisionScript``` no tiene un ```while```, este es substituido por un ```repeat until``` el cual funciona de la manera opuesta a un ```while```. En este caso un ```repeat until``` va a iterar hasta que la expresión proporcionada se vuela falsa.

###### Ejemplo:
```
number i = 0
repeat until i > 10
begin
   print(i)
   i = i + 1
end
```
###### Output:
```
0
1
2
3
4
5
6
7
8
9
10
```

### Funciones
En ```VisionScript``` es posible definir funciones y hacer uso de ellas por medio de llamadas. Al igual que otros lenguajes existen diferentes tipos de funciones las que tienen un valor de retorno y las que no. Las funciones pueden tener distintos tipos de parámetros.

Tipos de Funciones:
- ```void```    Se usa cuando una función no tiene valor de retorno
- ``` number``` Se usa cuando una función regresa un valor numérico
- ``` bool```   Se usa cuando una función regresa un valor booleano
- ``` text```   Se usa cuando una función regresa un texto
- ``` container``` Se usa cuando una función regresa un contenedor

Para llamar a una función solo se necesita poner su nombre seguido de paréntesis con los valores de los parámetros.

Es posible declarar variables dentro de una función, pero hay que tener en cuenta de que estas solo podrán ser usadas dentro de la función.
###### Ejemplo:
```
number function add(number x, number y)
begin
   return(x + y)
end

number a = add(1,2)

print(a)
```
###### Output:
```
3
```

### Contenedores
Como ya se mencionó un contenedor es una lista ordenada de elementos de distintos tipos (```number```,```bool```ó```text```) que pueden ser intercambiables. Los contenedores aceptan valores repetidos y es posible crear contenedores vacíos asignado el valor de ```[]``` a la variable.

Todos los contenedores tienen un índice inicial de ```0```.

#### Operaciones con Contenedores
A diferencia de otros lenguajes ```VisionScript``` no utiliza los ```[]``` para acceder a un índice, en lugar de ello se utilizan funciones especiales.

##### Contenedor.insert(indice,elemento)
Sirve para insertar un elemento a un contenedor. Esta función no regresa ningún valor.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.insert(indice,elemento)```

###### Ejemplo:
```
container arr = [0,1,2]

arr.insert(0,3)

print(arr)
```
###### Output:
```
[3, 0, 1, 2]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.insert(1,3)

print(arr)
```
###### Output:
```
[0, 3, 1, 2]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.insert(-1,3)

print(arr)
```
###### Output:
```
[0, 1, 3, 2]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.insert(-100,3)

print(arr)
```
###### Output:
```
[3, 0, 1, 2]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.insert(100,3)

print(arr)
```
###### Output:
```
[0, 1, 2, 3]
```
##### Contenedor.insert_back(elemento)
Sirve para insertar un elemento al final de un contenedor. Esta función no regresa ningún valor.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.insert_back(elemento)```

###### Ejemplo:
```
container arr = [0,1,2]

arr.insert_back(3)

print(arr)
```
###### Output:
```
[0, 1, 2, 3]
```
##### Contenedor.insert_front(elemento)
Sirve para insertar un elemento al principio de un contenedor. Esta función no regresa ningún valor.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.insert_front(elemento)```

###### Ejemplo:
```
container arr = [0,1,2]

arr.insert_front(3)

print(arr)
```
###### Output:
```
[3, 0, 1, 2]
```

##### Contenedor.replace(indice,elemento)
Sirve para reemplazar un elemento a un contenedor. Esta función no regresa ningún valor. Es importante que el índice está dentro del rango del tamaño del contenedor de lo contrario genera un error.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.replace(indice,elemento)```

###### Ejemplo:
```
container arr = [0,1,2]

arr.replace(0,3)

print(arr)
```
###### Output:
```
[3, 1, 2]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.replace(1,3)

print(arr)
```
###### Output:
```
[0, 3, 2]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.replace(-1,3)

print(arr)
```
###### Output:
```
[0, 1, 3]
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.replace(-100,3)

print(arr)
```
###### Output:
```
Error! indice fuera del rango.
```
###### Ejemplo:
```
container arr = [0,1,2]

arr.replace(100,3)

print(arr)
```
###### Output:
```
Error! indice fuera del rango.
```
##### Contenedor.get(indice)
Sirve para obtener un elemento de un contenedor. Esta función regresa el valor en el índice dado. Es importante que el índice está dentro del rango del tamaño del contenedor de lo contrario genera un error.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.get(indice)```

###### Ejemplo:
```
container arr = [0,1,2]

print(arr.get(0))

```
###### Output:
```
0
```
###### Ejemplo:
```
container arr = [0,1,2]

print(arr.get(-1))

```
###### Output:
```
2
```
###### Ejemplo:
```
container arr = [0,1,2]

print(arr.get(-100))

```
###### Output:
```
Error! indice fuera del rango.
```
##### Contenedor.get_back()
Sirve para obtener el último elemento de un contenedor. Esta función regresa el valor del último elemento de un contenedor.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.get_back()```

###### Ejemplo:
```
container arr = [0,1,2]

print(arr.get_back())

```
###### Output:
```
2
```
##### Contenedor.get_front()
Sirve para obtener el primer elemento de un contenedor. Esta función regresa el valor del primer elemento de un contenedor.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.get_front()```

###### Ejemplo:
```
container arr = [0,1,2]

print(arr.get_front())

```
###### Output:
```
0
```
##### Contenedor.length()
Sirve para obtener el primer elemento de un contenedor. Esta función regresa el valor del primer elemento de un contenedor.
Dicha función tiene la siguiente sintaxis: ```nombre_del_contenedor.get_front()```

###### Ejemplo:
```
container arr = [0,1,2]

print(arr.length())

```
###### Output:
```
3
```
### Editor de Textos
Algo que hace único a ```VisionScript``` es que tiene su propio editor de texto, el cual es utilizado para escribir código, que posteriormente puede ser ejecutado desde la terminal. Lo que hace único a este editor es que tiene botones especiales para traducir el código de alfabeto latino a braille y viceversa, e incluso reproducir el código en formato de audio, permitiendo que las personas con discapacidad visual tengan mayor facilidad de escribir código en ```VisionScript```.


![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
