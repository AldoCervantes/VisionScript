class FunctionDirectory:
    #Variable que sirve como flag para distinguir en que función estamos
    currentFunction = '@global'
    #Inicialización del directorio de funciones
    def __init__(self):
        self.funDirectory = {}

    #Funcion que sirve para crear una nueva funcion en el directorio de funciones
    def FuncDeclaration(self, functionId , type):
        if functionId in self.funDirectory:
            print("Error: la funcion ",functionId," ya existe")
        else:
            self.funDirectory[functionId] = [type, {}]

    #Funcion que sirve para crear una nueva variable 
    def VarDeclaration(self , functionId , varId , type , value):
        if functionId  in self.funDirectory:
            if varId in self.funDirectory[functionId][1]:
                print("Error: La variable ",varId," ya existe")
            else:
                self.funDirectory[functionId][1][varId] = [type, value]
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
    
    #Funcion para debug, sirve para imprimir nuestro directorio 
    def showFunctionDirectory(self):
        print("______________")
        for key , value in self.funDirectory.items():
            print(key,"=>",value)
            print("______________")
