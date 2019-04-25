import sys

class VirtualMachine:
    def __init__(self):
        self.Global = []
        self.Local = []
        self.Constante = []
        self.Temporal = []
        self.Cuadruplos = []
        self.currentCuad = 0

    #Funcion que rellena los arreglos de memoria
    def FillMemoryArrays(self,GlobalCont,constTable,TemporalCont):
        for x in range(0, GlobalCont):
            self.Global.append(0)
        
        for x in range(0, TemporalCont):
            self.Temporal.append(0)

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

        self.PrintCuadruplos()
        self.PrintMemArrays()


    #Funcion que regresa el valor de una direccion de memoria
    def getValue(self,dir):
        if dir >= 10000 and dir < 20000: #memGlobal
            return self.Global[dir - 10000]
        elif dir >= 20000 and dir < 30000: #memLocal
            return self.Local[dir - 20000]
        elif dir >= 30000 and dir < 40000: #memConst
            return self.Constante[dir - 30000]
        elif dir >= 40000: #memTemporal 
            return self.Temporal[dir - 40000]
        else:
            print('#getValue Error: la direccion',dir,'no es valida.')
            sys.exit()

    #Funcion que modifica el valor de una direccion de memoria
    def setValue(self,dir,value):
        if dir >= 10000 and dir < 20000: #memGlobal
            self.Global[dir - 10000] = value
        elif dir >= 20000 and dir < 30000: #memLocal
            self.Local[dir - 20000] = value
        elif dir >= 30000 and dir < 40000: #memConst
            self.Constante[dir - 30000] = value
        elif dir >= 40000: #memTemporal 
            self.Temporal[dir - 40000] = value
        else:
            print('#setValue Error: la direccion',dir,'no es valida.')
            sys.exit()

    #Funcion que realiza una asignacion de un valor a una variable [=,value,valueType,varId]
    def Assignacion(self,cuadruplo):
        if cuadruplo[2] == 'op_container':
            print("TODO")
            #TODO: HAY QUE VALIDAR QUE EL TIPO DE LA VARIABLE SEA IGUAL AL TIPO QUE EN DONDE SE QUIERE GUARDAR
        self.setValue(cuadruplo[3],self.getValue(cuadruplo[1]))

    #Funcion que realiza las operaciones de + , - , * y / [+,arg1,arg2,resultado]
    def OperacionesAritmeticas(self, cuadruplo):
        op = cuadruplo[0]
        arg1 = self.getValue(cuadruplo[1])
        arg2 = self.getValue(cuadruplo[2])

        if op == 1:
            result = arg1 + arg2
        elif op == 2:
            result = arg1 - arg2
        elif op == 3:
            result = arg1 * arg2
        elif op == 4:
            if(arg2 == 0):
                print('#OperacionesAritmeticas Error:',arg1,'/',arg2,'genera error.')
                sys.exit()
            else: 
                result = arg1 / arg2
        
        self.setValue(cuadruplo[3], result)

    #Funcion que realiza operaciones Logicas > , < , >= , <= , == , != , and , or [>,arg1,arg2,resultado]
    def OperacionesLogicas(self,cuadruplo):
        op = cuadruplo[0]
        arg1 = self.getValue(cuadruplo[1])
        arg2 = self.getValue(cuadruplo[2])
            
        if op == 5:
            result = arg1 > arg2
        elif op == 6:
            result = arg1 < arg2
        elif op == 7:
            result = arg1 >= arg2
        elif op == 8:
            result = arg1 <= arg2
        elif op == 9:
            result = arg1 == arg2
        elif op == 10:
            result = arg1 != arg2
        elif op == 11:
            result = arg1 and arg2
        elif op == 12:
            result = arg1 or arg2 
        
        self.setValue(cuadruplo[3], result)

    def OperacionesContenedores(self,cuadruplo):
        op = cuadruplo[0]

        #arr ???
        if op == 'append':
            arr.append(self.cuadruplo[1])
        elif op == 'concat':
            result = self.cuadruplo[1] + self.cuadruplo[2]
        elif op == 'insert':
            arr.insert(self.cuadruplo[1],self.cuadruplo[2])
        elif op == 'insert_back':
            arr.append(self.cuadruplo[1])
        elif op == 'insert_front':
            arr.insert(0,self.cuadruplo[1])
        elif op == 'get':
            arr[self.cuadruplo[2]]
        elif op == 'get_back':
            arr[len(arr)-1]
        elif op == 'get_front':
            arr[0]
        elif op == 'length':
            len(arr) 

    #Funcion que imprime el valor de un cuadruplo [flag,value,-1,-1]
    def Write(self, cuadruplo):
        op = cuadruplo[0]
        value = self.getValue(cuadruplo[1])
        if op == 15:
            print(value)
        elif op == 16:
            #FALTA HACER EL HEAR
            print(value)
        elif op == 17:
            #FALTA HACER EL BRAILLE
            print(value)

    #Funcion que lee de la terminal y guarda su valor en una variable  [SemanticCube.opToKey[flag],SemanticCube.TypeToKey[VarType],-1,self.PilaO.pop()]
    def Read(self, cuadruplo):
        temporal = input()
        tipo = cuadruplo[1]
        if tipo == 101:
            try:
                temp = float(temporal)
            except:
                print("La variable leida no es de tipo numerica")
                sys.exit()
        elif tipo == 102:
            temp = str(temporal)
        elif tipo == 103:
            if temporal == 'TRUE' or temporal == 'true' or temporal == 'True':
                temporal = True
            else:
                temporal = False
        elif tipo == 104:
            print(temp)
        else:
            print("ERROR:",temporal)
        self.setValue(cuadruplo[3], temp)


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
            elif op == 'GotoF':
                self.GoToF(cuadruplo)
            elif op == 'Goto':
                self.GoTo(cuadruplo)
            elif op >= 15 and op <= 17:
                self.Write(cuadruplo)
            elif op == 18:
                self.Read(cuadruplo)
            elif op == 'return':
                self.RETURN(cuadruplo)
            elif op == 'ERA':
                self.ERA(cuadruplo)
            elif op == 'param':
                self.PARAM(cuadruplo)
            elif op == 'gosub':
                self.GOSUB(cuadruplo)
            elif  op == 'append' or op == 'concat' or op == 'insert' or op == 'insert_back' or op == 'insert_front' or op == 'get' or op == 'get_back' or op == 'get_front' or op == 'length':
                self.OperacionesContenedores(cuadruplo)
            else:
                print('ERROR, cuadruplo invalido: ')
                print(cuadruplo)
            self.currentCuad = self.currentCuad + 1

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
        print('...... TEMPORAL .......')
        print(self.Temporal)
        print('..........................')
        print(' ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('$$$$$$$$$$$$$$$ COMPILADO $$$$$$$$$$$$$$$ ')


