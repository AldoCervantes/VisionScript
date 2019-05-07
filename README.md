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
- ``` bool```   Es un valor entre ```false``` ó ```true```
- ``` text```   Puede ser cualquier cadena de texto
- ``` container``` Simula una lista que puede guardar valores de cualquier tipo antes mencionado

### Declaración de Variables
Para declarar una variable es importante recordad que debe iniciar con una  ```letra``` seguido de cualquier cantidad de  ```letras```,  ```numeros``` ó ```_```

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
```VisionScript``` posee los operadores basicos para realizar operaciones matematicas: ```+, -, *, /``` y los operadores logicos como ```<, >, <=, >=, equal, not_equal```

### Contenedores
Como ya se menciono un contenedor es una lista ordenada de elementos de distintos tipos (```number```,```bool```ó```text```) que pueden ser intercambiables. Los contenedores aceptan valores repetidos y es posible crear contenedores vacios asigando el valor de ```[]``` a la variable.

Todos los contenedores tienen un indice inicial de ```0```.

#### Operaciones con Contenedores
A diferencia de otros lenguajes ```VisionScript``` no utiliza los ```[]``` para accesar a un indice, en lugar de ello se utilizan funciones especiales.

##### Contenedor.insert(indice,elemento)
Sirve para insertar un elemento a un contenedor. Esta función no regresa ningun valor. 
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
Sirve para insertar un elemento al final de un contenedor. Esta función no regresa ningun valor. 
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
Sirve para insertar un elemento al principio de un contenedor. Esta función no regresa ningun valor. 
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
Sirve para reemplazar un elemento a un contenedor. Esta función no regresa ningun valor. Es importante que el indice este dentro del rango del tamaño del contenedor de lo contrario genera un error.
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
Sirve para obtener un elemento de un contenedor. Esta función regresa el valor en el indice dado. Es importante que el indice este dentro del rango del tamaño del contenedor de lo contrario genera un error.
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
Sirve para obtener el ultimo elemento de un contenedor. Esta función regresa el valor del ultimo elemento de un contenedor.
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