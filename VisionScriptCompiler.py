from Cuadruplos import Cuadruplos

#Clase para crear el directorio de funciones
class FunctionDirectory:
    Cuad = Cuadruplos()
    #Variable que sirve como flag para distinguir en que función estamos
    currentFunction = '@global'
    #Inicialización del directorio de funciones
    def __init__(self):
        self.funDirectory = {}
        self.tablaConstantes = {}
        self.tablaConstantes['-1'] = ['number',30000]
        self.tablaConstantes['1'] = ['number',30001]
        self.memGlobal =  10000
        self.memLocal  =  20000
        self.memConst  =  30002

    #Funcion que sirve para crear una nueva funcion en el directorio de funciones
    def FuncDeclaration(self, functionId , FunctionType):
        if functionId in self.funDirectory:
            print("#FuncDeclaration Error: la funcion ",functionId," ya existe")
        else:
            self.funDirectory[functionId] = [FunctionType, {}]

    #Funcion que sirve para crear constantes 
    def ConstDeclaration(self , VarType , value):
        if VarType == 'number':
            float(value) 
        if value not in self.tablaConstantes:
                self.tablaConstantes[value] = [VarType,self.memConst]
                self.memConst+=1
        return self.tablaConstantes[value][1]

    #Funcion que sirve para crear una nueva variable 
    def VarDeclaration(self , functionId , varId , VarType , value):   
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                print("#VarDeclaration Error: La variable ",varId," ya existe")
            else:
                if functionId == '@global':
                    self.funDirectory[functionId][1][varId] = [VarType, value, self.memGlobal]
                    self.memGlobal+=1
                else:
                    self.funDirectory[functionId][1][varId] = [VarType, value, self.memLocal]
                    self.memLocal+=1
        else:
            print("#VarDeclaration Error: La funcion ",functionId," no existe")

    #Funcion que sirve para modificar el valor de una variable
    def VarAssignment(self , functionId , varId , value):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                self.funDirectory[functionId][1][varId][1] = value
            else:
                if functionId != '@global':
                    if varId in self.funDirectory['@global'][1]:
                        self.funDirectory['@global'][1][varId][1] = value
                    else:
                        print("#VarAssignment Error: La variable",varId,"no esta declarada dentro de la funcion",functionId)
                else:
                    print("#VarAssignment Error: La variable",varId,"no esta declarada")
        else:
            print("#VarAssignment Error: La funcion",varId,"no existe")
    
    #Funcion que retorna el tipo de dato de una variable
    def returnIDType(self, functionId, varId):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                return self.funDirectory[functionId][1][varId][0]
            else:
                if functionId != '@global':
                    if varId in self.funDirectory['@global'][1]:
                        return self.funDirectory['@global'][1][varId][0]
                    else:
                        print("#returnIDType Error: La variable",varId,"no esta declarada dentro de la funcion",functionId)
                else:
                    print("#returnIDType Error: La variable",varId,"no esta declarada")
        else:
            print("#returnIDType Error: La funcion",varId,"no existe")
        return 'error'

    #Funcion para debug, sirve para imprimir nuestro directorio 
    def showFunctionDirectory(self):
        print("~~~~~~~~~~~~~~~~~")
        for key , value in self.funDirectory.items():
            print(key,"=>",value)
            print("______________")
        print("~~~~~~~~~~~~~~~~~")
        print("################")
        for key , value in self.tablaConstantes.items():
            print(key,"=>",value)
            print("______________")
        print("################")

    #Funcion que regresa la direccion de memoria de una variable
    def returnIDAddress(self, functionId, varId):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                return self.funDirectory[functionId][1][varId][2]
            else:
                if functionId != '@global':
                    if varId in self.funDirectory['@global'][1]:
                        return self.funDirectory['@global'][1][varId][2]
                    else:
                        print("#returnIDAddress Error: La variable",varId,"no esta declarada dentro de la funcion",functionId)
                else:
                    print("#returnIDAddress Error: La variable",varId,"no esta declarada")
        else:
            print("#returnIDAddress Error: La funcion",varId,"no existe")
        return -999

    #Funcion que regresa la direccion de memoria de una constante
    def returnConstAddress(self, value):
        if value  in self.tablaConstantes:
            return self.tablaConstantes[value][2]
        else:
            print("#returnConstAddress Error: La funcion",varId,"no existe")
            return -999