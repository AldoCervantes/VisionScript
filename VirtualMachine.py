#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gtts import gTTS
import contextlib
with contextlib.redirect_stdout(None):
    from pygame import mixer
import os
import mmap

class VirtualMachine:
    def __init__(self):
        self.Global = [] #Es el espacio de memoria que almacena el valor de las globales
        self.Local = [] #Es el espacio de memoria que almacena el valor de las locales
        self.Constante = [] #Es el espacio de memoria que almacena el valor de las constantes
        self.Cuadruplos = [] #Es un contenedor que contiene todos los cuadruplos creados por compiler
        self.currentCuad = 0 #contador de el cuadruplo actual
        self.keyToType = { 101:'number', 102:'text', 103:'bool', 104:'container' } #Hacer conversiones claves a tipos
        self.FuncitonJumps = [] #Pila de jumps que se usa con los gosubs
        self.FunSpaceMemTable = {} #Diccionario que almacena las funciones y su cantidad de variables locales y temporales
        self.newMemLocal = [] #Es un contenedor que hace referencia al nuevo contenedor creado por los ERA
        self.returnMem = [] #Es una pila que almacena los valores de los retuns para ser usados por las function calls

    #Funcion que rellena los contenedors de memoria
    def FillMemoryArrays(self,GlobalCont,constTable):
        for x in range(0, GlobalCont):
            self.Global.append(0)

        for key, value in constTable.items():
            if value[0] == 'number':
                    if key.find(".") == -1:
                        a = int(float(key))
                        self.Constante.append(a)
                    else:
                        a = float(key)
                        self.Constante.append(a)
            elif value[0] == 'bool':
                    if key == 'true':
                            a = True
                            self.Constante.append(a)
                    elif key == 'false':
                            a = False
                            self.Constante.append(a)
            else:
                a = key[1:len(key)-1]
                self.Constante.append(a)
        
        cuadruplo = [777,777,777,777]
        self.Cuadruplos.append(cuadruplo)

        #self.PrintCuadruplos()
        #self.PrintMemArrays()


    #Funcion que regresa el valor de una direceccion de memoria
    def getValue(self,direc):
        if direc >= 10000 and direc < 20000: #memGlobal
            return self.Global[direc - 10000]
        elif direc >= 20000 and direc < 30000: #memLocal
            return self.Local[-1][direc - 20000]
        elif direc >= 30000 and direc < 40000: #memConst
            return self.Constante[direc - 30000]
        elif direc == 99999:
            return self.returnMem.pop()
        else:
            print('#getValue Error: la direceccion',direc,'no es valida.')
            sys.exit()

    #Funcion que modifica el valor de una direceccion de memoria
    def setValue(self,direc,value):
        if direc >= 10000 and direc < 20000: #memGlobal
            self.Global[direc - 10000] = value
        elif direc >= 20000 and direc < 30000: #memLocal
            self.Local[-1][direc - 20000] = value
        elif direc >= 30000 and direc < 40000: #memConst
            self.Constante[direc - 30000] = value
        elif direc == 99999:
            self.returnMem.append(value)
        else:
            print('#setValue Error: la direceccion',direc,'no es valida.')
            sys.exit()

    #Funcion que realiza una asignacion de un valor a una variable  a = 10 => [=,10,[number,number],a]
    def Assignacion(self,cuadruplo):
        value = self.getValue(cuadruplo[1])
        targetType = self.keyToType[cuadruplo[2][1]]
        if cuadruplo[2][0] == 106:
            if type(value) == int or type(value) == float:
                valueType = 'number'
            elif type(value) == bool:
                valueType = 'bool'
            elif type(value) == str:
                valueType = 'text'
            elif type(value) == list:
                valueType = 'container'
        else:
            valueType = self.keyToType[cuadruplo[2][0]]

        if valueType == targetType:
            self.setValue(cuadruplo[3],value)
        else:
            print('#Assignacion Error:Se esta intentando guardar un valor de tipo',valueType,'en una variable de tipo',targetType)
            sys.exit()

    #Funcion que realiza las operaciones de + , - , * y / [+,arg1,arg2,resultado]
    def OperacionesAritmeticas(self, cuadruplo):
        op = cuadruplo[0]
        arg1 = self.getValue(cuadruplo[1])
        arg2 = self.getValue(cuadruplo[2])

        if op == 1:
            if type(arg1) == str:
                arg2 = str(arg2)
            try:
                result = arg1 + arg2
            except:
                print('# Error: la operacion',arg1,'+',arg2,'no es valida')
                sys.exit()
        elif op == 2:
            try:
                result = arg1 - arg2
            except:
                print('# Error: la operacion',arg1,'-',arg2,'no es valida')
                sys.exit()
        elif op == 3:
            try:
                result = arg1 * arg2
            except:
                print('# Error: la operacion',arg1,'*',arg2,'no es valida')
                sys.exit()
        elif op == 4:
            try:
                result = arg1 / arg2
            except:
                print('# Error: la operacion',arg1,'/',arg2,'no es valida')
                sys.exit()
        self.setValue(cuadruplo[3], result)

    #Funcion que realiza operaciones Logicas > , < , >= , <= , == , != , and , or [>,arg1,arg2,resultado]
    def OperacionesLogicas(self,cuadruplo):
        op = cuadruplo[0]
        arg1 = self.getValue(cuadruplo[1])
        arg2 = self.getValue(cuadruplo[2])
            
        if op == 5:
            try:
                result = arg1 > arg2
            except:
                print('# Error: la operacion',arg1,'>',arg2,'no es valida')
                sys.exit()
        elif op == 6:
            try:
                result = arg1 < arg2
            except:
                print('# Error: la operacion',arg1,'<',arg2,'no es valida')
                sys.exit()
        elif op == 7:
            try:
                result = arg1 >= arg2
            except:
                print('# Error: la operacion',arg1,'>=',arg2,'no es valida')
                sys.exit()
        elif op == 8:
            try:
                result = arg1 <= arg2
            except:
                print('# Error: la operacion',arg1,'<=',arg2,'no es valida')
                sys.exit()
        elif op == 9:
            try:
                result = arg1 == arg2
            except:
                print('# Error: la operacion',arg1,'equal',arg2,'no es valida')
                sys.exit()
        elif op == 10:
            try:
                result = arg1 != arg2
            except:
                print('# Error: la operacion',arg1,'not_equal',arg2,'no es valida')
                sys.exit()
        elif op == 11:
            try:
                result = arg1 and arg2
            except:
                print('# Error: la operacion',arg1,'and',arg2,'no es valida')
                sys.exit()
        elif op == 12:
            try:
                result = arg1 or arg2 
            except:
                print('# Error: la operacion',arg1,'or',arg2,'no es valida')
                sys.exit()
        self.setValue(cuadruplo[3], result)

    #Funcion que se encarga de validar la expresion si es y cambia el self.currentCuad al cuadruplo que dicta el GotoF 
    #[SemanticCube.opToKey['GotoF'],result,-1,-1]
    def GoToF(self,cuadruplo):
        evaluate = self.getValue(cuadruplo[1])
        if evaluate:
            self.currentCuad = self.currentCuad
        else:
            self.currentCuad = cuadruplo[3] - 1
    
    #Funcion que se encarga de validar la expresion si es y cambia el self.currentCuad al cuadruplo que dicta el GotoV 
    #[SemanticCube.opToKey['GotoV'],result,-1,-1]
    def GoToV(self,cuadruplo):
        evaluate = self.getValue(cuadruplo[1])
        if evaluate:
            self.currentCuad = cuadruplo[3] - 1
        else:
            self.currentCuad = self.currentCuad
    
    #Funcion que se encarga de cambiar el self.currentCuad al cuadruplo que dicta el Goto
    def GoTo(self,cuadruplo):
        self.currentCuad = cuadruplo[3] - 1

    #Funcion que imprime el valor de un cuadruplo [flag,value,-1,-1]
    def Write(self, cuadruplo):
        op = cuadruplo[0]
        value = str(self.getValue(cuadruplo[1]))
        if op == 16:
            print(value)
        elif op == 17:
            #Generación del archivo .mp3
            tts = gTTS(text= value, lang='es')
            tts.save('speech.mp3')
            #Carga el archivo .mp3 a memoria
            with open('speech.mp3') as f: 
                PlayedMp3File = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) 
            #Enciende el mixer
            mixer.init()
            #carga el audio al mixer
            mixer.music.load(PlayedMp3File)
            #Reproduce el audio
            mixer.music.play()
            #Mientras el audio se esta reproduciendo espera
            while mixer.music.get_busy() == True:
                continue
            #Cierra el archivo .mp3
            PlayedMp3File.close()
            #Apaga el mixer
            mixer.quit()
            #Si el archivo existe borralo
            if os.path.exists('speech.mp3'):
                os.remove('speech.mp3')
        elif op == 18:
            intab = ' !#$%&"()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz'
            outtab = ' ⠮⠼⠫⠩⠯⠄⠷⠾⠡⠬⠠⠤⠨⠌⠴⠂⠆⠒⠲⠢⠖⠶⠦⠔⠱⠰⠣⠿⠜⠹⠈⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵⠪⠳⠻⠘⠸⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵'
            transtab = str.maketrans(intab, outtab)
            print(value.translate(transtab))

    #Funcion que lee de la terminal y guarda su valor en una variable  ['read',tipo de a,-1,dir de a]  number a = 0 read(a)
    def Read(self, cuadruplo):
        temporal = input()
        tipo = cuadruplo[1]
        if tipo == 101:
            try:
                if temporal.find(".") == -1:
                    temp = int(float(temporal))
                else:
                    temp = float(temporal)
                self.setValue(cuadruplo[3], temp)
            except:
                print("#Read Error: La variable leida no es de tipo numerica")
                sys.exit()
        elif tipo == 102:
            temp = str(temporal)
            self.setValue(cuadruplo[3], temp)
        elif tipo == 103:
            if temporal == 'true':
               temp = True
            elif temporal == 'false':
                temp = False
            else:
                print("#Read Error: La variable leida no es de tipo boolean (true/false)")
                sys.exit()
            self.setValue(cuadruplo[3], temp)
        else:
            print("#Read Error: La variable no tiene un tipo registrado",temporal)
            sys.exit()

    #Funcion de que agrega un elemento a un contenedor ya existente ['append',value,-1,self.CurrentCotainer]
    def AppendElement(self,cuadruplo):
        value = self.getValue(cuadruplo[1])
        direc = cuadruplo[3]
        if direc >= 10000 and direc < 20000: #memGlobal
            self.Global[direc - 10000].append(value)
        elif direc >= 20000 and direc < 30000: #memLocal
            self.Local[-1][direc - 20000].append(value)
        elif direc >= 30000 and direc < 40000: #memConst
            self.Constante[direc - 30000].append(value)
        elif direc == 99999:
            self.returnMem[-1].append(value)
        else:
            print('#AppendElement Error: la direceccion',direc,'no es valida.')
            sys.exit()

    #Funcion que concatena dos contenedores y almacena el resultado en la variable dicha por el cuadruplo
    #['concant',LeftContainer,RightContainer,result]
    def ConcatContainers(self,cuadruplo):
        LeftContainer = self.getValue(cuadruplo[1])
        RightContainer = self.getValue(cuadruplo[2])
        result = LeftContainer + RightContainer
        self.setValue(cuadruplo[3],result)

    #Funcion que inicializa un contenedor en una variable
    def InicializaContenedor(self,cadruplo):
        self.setValue(cadruplo[3],[])

    #Funcion que se encarga de las operaciones de contenedores que no regresan un valor
    def OpContenedor(self,cuadruplo):
        op = cuadruplo[0]
        if op == 26 or op == 35: #insert [SemanticCube.opToKey[flag],index,element,varId]
            index = self.getValue(cuadruplo[1])
            if type(index) == int or type(index) == float:
                index = int(float(index))
            else:
                print("#OpContenedor Error: El indice",index,"no es de tipo number")
                sys.exit()
            element = self.getValue(cuadruplo[2])
        elif op == 27: #insert_back [SemanticCube.opToKey[flag],value,-1,varId]
            element = self.getValue(cuadruplo[1])
        elif op == 28: #insert_front [SemanticCube.opToKey[flag],value,-1,varId]
            index = 0
            element = self.getValue(cuadruplo[1])
        
        direc = cuadruplo[3]
        
        if direc >= 10000 and direc < 20000: #memGlobal
            if op == 27:
                index = len(self.Global[direc - 10000])
                self.Global[direc - 10000].insert(index, element)
            elif op == 35:
                try:
                    self.Global[direc - 10000][index] = element
                except:
                    print('#OpContenedor Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
            else:
                self.Global[direc - 10000].insert(index, element)
        elif direc >= 20000 and direc < 30000: #memLocal
            if op == 27:
                index = len(self.Local[-1][direc - 20000])
                self.Local[-1][direc - 20000].insert(index, element)
            elif op == 35:
                try:
                    self.Local[-1][direc - 20000][index] = element
                except:
                    print('#OpContenedor Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
            else:
                self.Local[-1][direc - 20000].insert(index, element)
        elif direc >= 30000 and direc < 40000: #memConst
            if op == 27:
                index = len(self.Constante[direc - 30000])
                self.Constante[direc - 30000].insert(index, element)
            elif op == 35:
                try:
                    self.Constante[direc - 30000][index] = element
                except:
                    print('#OpContenedor Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
            else:
                self.Constante[direc - 30000].insert(index, element)
        elif direc == 99999:
            if op == 27:
                index = len(self.returnMem[-1])
                self.returnMem[-1].insert(index,element)
            elif op == 35:
                try:
                    self.returnMem[-1][index] = element
                except:
                    print('#OpContenedor Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
            else:
                self.returnMem[-1].insert(index,element)
        else:
            print('#OpContenedor Error: la direceccion',direc,'no es valida.')
            sys.exit()

    #Funcion que se encarga de las operaciones de contenedores que regresan un valor 
    def OpContenedorReturns(self,cuadruplo):
        op = cuadruplo[0]
        
        if op == 29: #get [SemanticCube.opToKey[flag],value,varId,result] 
            index = self.getValue(cuadruplo[1])
        elif op == 30: #get_back [SemanticCube.opToKey[flag],-1,varId,result]
            index = -1
        elif op == 31: #get_front [SemanticCube.opToKey[flag],-1,varId,result]
            index = 0

        direc = cuadruplo[2]
        result = cuadruplo[3]

        if direc >= 10000 and direc < 20000: #memGlobal
            if op == 32: #lenght
                self.setValue(result,len(self.Global[direc - 10000]))
            else:
                try:
                    self.setValue(result,self.Global[direc - 10000][index])
                except:
                    print('#OpContenedorReturns Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
        elif direc >= 20000 and direc < 30000: #memLocal
            if op == 32: #lenght
                self.setValue(result,len(self.Local[-1][direc - 20000]))
            else:
                try:
                    self.setValue(result,self.Local[-1][direc - 20000][index])
                except:
                    print('#OpContenedorReturns Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
        elif direc >= 30000 and direc < 40000: #memConst
            if op == 32: #lenght
               self.setValue(result,len(self.Constante[direc - 30000]))
            else:  
                try:
                    self.setValue(result,self.Constante[direc - 30000][index])
                except:
                    print('#OpContenedorReturns Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
        elif direc == 99999: #memConst
            if op == 32: #lenght
               self.setValue(result,len(self.returnMem[-1]))
            else:  
                try:
                    self.setValue(result,self.returnMem[-1][index])
                except:
                    print('#OpContenedorReturns Error: El indice',index,'no se encuentra dentro del rango del contenedor')
                    sys.exit()
        else:
            print('#OpContenedorReturns Error: la direceccion',direc,'no es valida.')
            sys.exit()

    #Funcion que realiza el ERA (Generacion de un espacio de memoria para dicha funcion) 
    def ERA(self,cuadruplo): #[SemanticCube.opToKey['ERA'],-1,-1,functionId]
        localMemSpace = self.FunSpaceMemTable[cuadruplo[3]]
        self.newMemLocal = []
        for x in range(0, localMemSpace):
            self.newMemLocal.append(0)

    #Funcion que asigna el valor a un parametro
    def PARAM(self,cuadruplo): #['param',value,valueType,self.paramCounter]
        value = self.getValue(cuadruplo[1])
        targetType = self.keyToType[cuadruplo[2][1]]
        if cuadruplo[2][0] == 106:
            if type(value) == int or type(value) == float:
                valueType = 'number'
            elif type(value) == bool:
                valueType = 'bool'
            elif type(value) == str:
                valueType = 'text'
            elif type(value) == list:
                valueType = 'container'
        else:
            valueType = self.keyToType[cuadruplo[2][0]]

        if valueType == targetType:
            self.newMemLocal[cuadruplo[3]] = self.getValue(cuadruplo[1])
        else:
            print('#PARAM Error:Se esta intentando mandar un valor de tipo',valueType,'a un parametro de tipo',targetType)
            sys.exit()

    #Funcion que realiza el gosub
    def GOSUB(self,cuadruplo):
        self.Local.append(self.newMemLocal)
        self.FuncitonJumps.append(self.currentCuad)
        self.currentCuad = cuadruplo[3] - 1

    #Funcion que realiza el ENDPROC
    def ENDPROC(self,cuadruplo):
        self.Local.pop()
        self.currentCuad = self.FuncitonJumps.pop()

    #Funcion que realiza la asignacion de un return ['return',VarType,value,returnDir]
    def RETURN(self,cuadruplo):
        value = self.getValue(cuadruplo[2])
        self.setValue(cuadruplo[3],value)

    def run(self):
        while self.Cuadruplos[self.currentCuad][0] != 777:
            cuadruplo = self.Cuadruplos[self.currentCuad]
            op = cuadruplo[0]
            if op == 0:
                self.Assignacion(cuadruplo)
            elif op >= 1 and op <= 4:
                self.OperacionesAritmeticas(cuadruplo)
            elif  op >= 5 and op <= 12:
                self.OperacionesLogicas(cuadruplo)
            elif op == 13:
                self.GoToF(cuadruplo)
            elif op == 14:
                self.GoToV(cuadruplo)
            elif op == 15:
                self.GoTo(cuadruplo)
            elif op >= 16 and op <= 18:
                self.Write(cuadruplo)
            elif op == 19:
                self.Read(cuadruplo)
            elif op == 20:
                self.RETURN(cuadruplo)
            elif op == 21:
                self.ERA(cuadruplo)
            elif op == 22:
                self.PARAM(cuadruplo)
            elif op == 23:
                self.GOSUB(cuadruplo)
            elif op == 24:
                self.AppendElement(cuadruplo)
            elif op == 25:
                self.ConcatContainers(cuadruplo)
            elif (op >= 26 and op <= 28) or op == 35:
                self.OpContenedor(cuadruplo)
            elif op >= 29 and op <= 32:
                self.OpContenedorReturns(cuadruplo)
            elif op == 33:
                self.InicializaContenedor(cuadruplo)
            elif op == 34:
                self.ENDPROC(cuadruplo)
            else:
                print('#run Error: cuadruplo invalido: ')
                print(cuadruplo)
                sys.exit()
            self.currentCuad = self.currentCuad + 1
            #print(cuadruplo)

    #Funcion para debugear
    def PrintCuadruplos(self):
        print(" ")
        print(" ")
        print("~~~~~~~~~~~~~~ MAQUINA VIRTUAL ~~~~~~~~~~~~")
        print(" ")
        cont = 0

        print('@@@@@@ CUADRUPLOS @@@@@@@')
        for cuad in range(len(self.Cuadruplos)):
            print(cont,self.Cuadruplos[cuad])
            cont = cont + 1
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    #Funcion para debugear
    def PrintMemArrays(self):
        print(' ')
        print('###### GLOBAL #######')
        print(self.Global)
        print('##########################')
        print(' ')
        print('====== CONSTANTES =======')
        print(self.Constante)
        print('==========================')
        print(' ')
        print('...... LOCAL .......')
        print(self.Local)
        print('..........................')
        print(' ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('$$$$$$$$$$$$$$$ COMPILADO $$$$$$$$$$$$$$$ ')


