from Cuadruplos import Cuadruplos

#Clase para crear el directorio de funciones
class FunctionDirectory:
    
    Cuad = Cuadruplos()
    #Variable que sirve como flag para distinguir en que función estamos
    currentFunction = '@global'
    #Inicialización del directorio de funciones
    def __init__(self):
        self.funDirectory = {}
        self.memGlobal =  5000
        self.memLocal  =  9000
        self.memConst  =  20000
    #Funcion que sirve para crear una nueva funcion en el directorio de funciones
    def FuncDeclaration(self, functionId , FunctionType):
        if functionId in self.funDirectory:
            print("Error: la funcion ",functionId," ya existe")
        else:
            self.funDirectory[functionId] = [FunctionType, {}]

    #Funcion que sirve para crear una nueva variable 
    def VarDeclaration(self , functionId , varId , VarType , value):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                print("Error: La variable ",varId," ya existe")
            else:
                if functionId == '@global':
                    self.funDirectory[functionId][1][varId] = [VarType, value, self.memGlobal]
                    self.memGlobal+=1
                else:
                    self.funDirectory[functionId][1][varId] = [VarType, value, self.memLocal]
                    self.memLocal+=1
        else:
            print("Error: La funcion ",functionId," no existe")

    #Funcion que sirve para modificar el valor de una variable
    def VarAssignment(self , functionId , varId , value):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                self.funDirectory[functionId][1][varId][1] = value
            else:
                if functionId != '@global':
                    print("Error: La variable",varId,"no esta declarada dentro de la funcion",functionId)
                else:
                    print("Error: La variable",varId,"no esta declarada")
        else:
            print("Error: La funcion",varId,"no existe")
    
    #Funcion que retorna el tipo de dato de una variable
    def returnIDType(self, functionId, varId):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                return self.funDirectory[functionId][1][varId][0]
            else:
                if functionId != '@global':
                    print("Error: La variable",varId,"no esta declarada dentro de la funcion",functionId)
                else:
                    print("Error: La variable",varId,"no esta declarada")
        else:
            print("Error: La funcion",varId,"no existe")
        return 'error'

    #Funcion para debug, sirve para imprimir nuestro directorio 
    def showFunctionDirectory(self):
        print("______________")
        for key , value in self.funDirectory.items():
            print(key,"=>",value)
            print("______________")

    #Funcion que regresa la direccion de memoria de una variable
    def returnIDAddress(self, functionId, varId):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                return self.funDirectory[functionId][1][varId][2]
            else:
                if functionId != '@global':
                    print("Error: La variable",varId,"no esta declarada dentro de la funcion",functionId)
                else:
                    print("Error: La variable",varId,"no esta declarada")
        else:
            print("Error: La funcion",varId,"no existe")
        return -999