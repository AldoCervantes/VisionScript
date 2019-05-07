#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
from SemanticCube import SemanticCube
import sys


#Clase para crear el directorio de funciones
class Compiler:
    SemanticCube = SemanticCube()

    #Variable que sirve como flag para distinguir en que función estamos
    currentFunction = '@global'
    
    #Inicialización del directorio de funciones
    def __init__(self):
        self.funDirectory = {} #Directorio de Funciones
        self.tablaConstantes = {} #Tabla de valores constantes
        self.memGlobal =  10000
        self.memLocal  =  20000
        self.memConst  =  30000  
        self.PilaO = [] #Pila donde van a ir los Operandos (1,a,"text",false,...)
        self.PTypes = [] #Pila de tipos (number,text,bool,container)
        self.POper = [] #Pila de Operadores (+,-,*,/,...)
        self.Quad = deque([]) #Fila de Cuadruplos
        self.PJumps = [] #Pila de saltos
        self.paramCounter = 0 #Contador de Parametros de una funcion
        self.CurrentCotainer = 0 #Flag que indica la direccion del contenedor actual
        self.FunLocalMems = {} #Diccionario que almacena las funciones y su cantidad de variables locales y temporales
        self.haveReturn = False

    #Funcion que regresa una direccion de memorial temporal relativa a el contexto donde se este usando
    def returnTemp(self,functionId):
        if functionId == '@global':
            tempGlobal = self.memGlobal
            self.memGlobal = self.memGlobal + 1
            return tempGlobal
        else:
            tempLocal = self.memLocal
            self.memLocal = self.memLocal + 1
            return tempLocal

    #Funcion que sirve para crear una nueva funcion en el directorio de funciones
    def FuncDeclaration(self, functionId , FunctionType):
        if functionId in self.funDirectory:
            print("#FuncDeclaration Error: la funcion ",functionId," ya existe")
            sys.exit()
        else:
            if FunctionType != 'void':
                self.funDirectory[functionId] = [FunctionType, {}, [],0, 0,0]
            else:
                self.funDirectory[functionId] = [FunctionType, {}, [],-1,0,0]

    #Funcion que sirve para registrar los parametros
    def ParamDeclaration(self,functionId, ParamType):
        if functionId  in self.funDirectory:
            self.funDirectory[functionId][2].append(ParamType)
        else:
            print("#ParamDeclaration Error: La funcion ",functionId," no existe")
            sys.exit()

    #Funcion que regresa un arreglo con los paremtros de la funcion
    def ReturnParams(self,functionId):
        if functionId  in self.funDirectory:
            return self.funDirectory[functionId][2]
        else:
            print("#ReturnParams Error: La funcion ",functionId," no existe")
            sys.exit()

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
                sys.exit()
            else:
                if functionId == '@global':
                    self.funDirectory[functionId][1][varId] = [VarType, value, self.memGlobal]
                    self.memGlobal+=1
                else:
                    self.funDirectory[functionId][1][varId] = [VarType, value, self.memLocal]
                    self.memLocal+=1
        else:
            print("#VarDeclaration Error: La funcion ",functionId," no existe")
            sys.exit()

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
                        sys.exit()
                else:
                    print("#VarAssignment Error: La variable",varId,"no esta declarada")
                    sys.exit()
        else:
            print("#VarAssignment Error: La funcion",varId,"no existe")
            sys.exit()
    
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
                        sys.exit()
                else:
                    print("#returnIDType Error: La variable",varId,"no esta declarada")
                    sys.exit()
        else:
            print("#returnIDType Error: La funcion",varId,"no existe")
            sys.exit()
        return 'error'

    #Funcion para debug, sirve para imprimir nuestro directorio 
    def showFunctionDirectory(self):
        print(" ")
        print("~~~~~~~~ DIRECTORIO DE FUNCIONES ~~~~~~~~~")
        for key , value in self.funDirectory.items():
            print(key,"=>",value)
            print("______________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ")
        print("####### TABLA DE CONSTANTES #########")
        for key , value in self.tablaConstantes.items():
            print(key,"=>",value)
            print("______________")
        print("#####################################")
        print(" ")
        print(";;;;;; CANTIDAD DE FUNCIONES ;;;;;;;;")
        for key , value in self.FunLocalMems.items():
            print(key,"=>",value)
            print("______________")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")

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
                        sys.exit()
                else:
                    print("#returnIDAddress Error: La variable",varId,"no esta declarada")
                    sys.exit()
        else:
            print("#returnIDAddress Error: La funcion",varId,"no existe")
            sys.exit()
        return -999

    #Funcion que regresa la direccion de memoria de una constante
    def returnConstAddress(self, value):
        if value  in self.tablaConstantes:
            return self.tablaConstantes[value][2]
        else:
            print("#returnConstAddress Error: La funcion",varId,"no existe")
            sys.exit()
            return -999
    
    #Funcion que regresa la direccion de memoria para el retorno de una funcion
    def returnFuncReturnAddress(self,functionId):
        if functionId in self.funDirectory:
            return 99999
        else:
            print('#returnFuncReturnAddress Error: La funcion',functionId,'no existe')
            sys.exit()
            return -999

    #Funcion que regresa el tipo de una funcion
    def returnFuncReturnType(self,functionId):
        if functionId in self.funDirectory:
            return self.funDirectory[functionId][0]
        else:
            print('#returnFuncReturnType Error: La funcion',functionId,'no existe')
            sys.exit()
            return 'error'
    
    #Funcion que registra cuantas variables locales tiene una funcion
    def RegisterLocalCont(self,functionId):
        LocalCont = self.memLocal - 20000
        if functionId in self.funDirectory:
            self.funDirectory[functionId][4] = LocalCont
            self.FunLocalMems[functionId] = LocalCont
        else:
            print('#RegisterLocalCont Error: La funcion no existe.')
            sys.exit()

    #Funcion que regresa cuantas variables globales existen
    def returnGlobalCont(self):
        return self.memGlobal - 10000

    #Funcion que regresa la tabla de constantes
    def returnConstTable(self):
        return self.tablaConstantes
    
    def InsertIdType(self,varId,VarType): #Funcion 1
        self.PilaO.append(varId)
        self.PTypes.append(VarType)
    
    def InsertOperator(self,operator): #Funcion 2, 3 , 8 y 10
        self.POper.append(operator)
    
    #Para operaciones aritmeticas
    def GenerateCuad(self,flag,functionId): # Funcion 4 , 5 , 9 y 11
        if len(self.POper) > 0:
            top = self.POper[len(self.POper)-1]
            if (flag == 'Termino' and (top == '+' or top == '-')) or (flag == 'Factor' and (top == '*' or top == '/')) or (flag == 'Expresion' and (top == '>' or top == '<'or top == '<=' or top == '>=' or top == 'not_equal' or top == 'equal')) or (flag == 'Mega_Expresion'  and (top == 'and' or top == 'or')):
                    right_operand = self.PilaO.pop()
                    right_type = self.PTypes.pop()
                    left_operand = self.PilaO.pop()
                    left_type = self.PTypes.pop()
                    operator = self.POper.pop()
                    if (left_type == 'op_container' or right_type == 'op_container') and (left_type != 'error' and right_type != 'error') :
                        result_type = 'op_container'
                    elif left_type != 'error' and right_type != 'error':
                        result_type = SemanticCube.semanticCube[operator][left_type][right_type]
                    else:
                        print("#GenerateCuad Error:",left_type,operator,right_type,"genera",result_type)
                        sys.exit()
                    if result_type != 'error':
                        result = self.returnTemp(functionId)
                        cuadruplo = [SemanticCube.opToKey[operator], left_operand, right_operand, result]
                        self.Quad.append(cuadruplo)
                        self.PilaO.append(result)
                        self.PTypes.append(result_type)
                    else:
                        print("#GenerateCuad Error:",left_type,operator,right_type,"genera",result_type)
                        sys.exit()
    
    #Funcion que genera un cuaduplo de asignacion [=,valor,-1,id]
    def GenerateAssignmentCuad(self,varId,targetType):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            if valueType == targetType or valueType == 'op_container':
                cuadruplo = [SemanticCube.opToKey['='],value,[SemanticCube.TypeToKey[valueType],SemanticCube.TypeToKey[targetType]],varId]
                self.Quad.append(cuadruplo)
            else:
                print("#GenerateAssignmentCuad Error: Se esta intentando asignar un valor de tipo",valueType,"a una variable de tipo",targetType)
                sys.exit()
    
    #Funcion 1 de IF
    def FuncionIF1(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            result = self.PilaO.pop()
            exp_type = self.PTypes.pop()
            if exp_type == 'bool' or exp_type == 'op_container':
                cuadruplo = [SemanticCube.opToKey['GotoF'],result,-1,-1]
                self.Quad.append(cuadruplo)
                self.PJumps.append(len(self.Quad) - 1 )
            else:
                print("#GenerateGotoF Error: Se esta intentando hacer un if con una expresion de tipo",exp_type)
                sys.exit()

    #Funcion 3 de IF
    def FuncionIF2(self):
        cuadruplo = [SemanticCube.opToKey['Goto'],-1,-1,-1]
        self.Quad.append(cuadruplo)
        false = self.PJumps.pop()
        self.PJumps.append(len(self.Quad) - 1)
        self.Quad[false][3] = len(self.Quad)
     
    #Funcion 2 de IF
    def  FuncionIF3(self):
        end = self.PJumps.pop()
        self.Quad[end][3] = len(self.Quad)

    #Funcion 1 de repeat until
    def FuncionRepUntil1(self):
        self.PJumps.append(len(self.Quad))

    #Funcion 2 de repat until
    def FuncionRepUntil2(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            result = self.PilaO.pop()
            exp_type = self.PTypes.pop()
            if exp_type == 'bool' or exp_type == 'op_container':
                cuadruplo = [SemanticCube.opToKey['GotoV'],result,-1,-1]
                self.Quad.append(cuadruplo)
                self.PJumps.append(len(self.Quad) - 1 )
            else:
                print("#FuncionRepUntil2 Error: Se esta intentando hacer un repeat con una expresion de tipo",exp_type)
                sys.exit()

    #Funcion 3 de repat until
    def FuncionRepUntil3(self):
        end = self.PJumps.pop()
        returns = self.PJumps.pop()
        cuadruplo = [SemanticCube.opToKey['Goto'],-1,-1,returns]
        self.Quad.append(cuadruplo)
        self.Quad[end][3] = len(self.Quad)

    #Funcion para Generar los cuadruplos de los 3 tipos de print
    def GeneratePrintCuad(self,flag):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            self.PTypes.pop()
            cuadruplo = [SemanticCube.opToKey[flag],self.PilaO.pop(),-1,-1]
            self.Quad.append(cuadruplo)

    #Funcion para generar los cuadruplos de la funcion read
    def GenerateReadCuad(self,flag,VarType):
        if VarType == 'container':
            print('#GenerateReadCuad Error: No se puede leer una variable container desde consola.')
            sys.exit()
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            self.PTypes.pop()
            cuadruplo = [SemanticCube.opToKey[flag],SemanticCube.TypeToKey[VarType],-1,self.PilaO.pop()]
            self.Quad.append(cuadruplo)
    
    #Funcion 6
    def InsertParentesis(self):
        self.POper.append('(')
    
    # Funcion 7
    def RemoveParentesis(self):
        self.POper.pop()

    #Funcion para generar los cuadruplos de los RETURNS de las funciones
    def GenerateFunReturns(self,returnDir):
        funcType = self.funDirectory[self.currentFunction][0]
        self.haveReturn = True
        if self.currentFunction == '@global':
            print("#GenerateFunReturns Error: Existe un return() que no forma parte de una funcion")
            sys.exit()
        else:
            if funcType == 'void':
                print('#GenerateFunReturns Error: Una funcion void no debe tener retorno')  
                sys.exit()  

        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            VarType = self.PTypes.pop()
            value = self.PilaO.pop()
            if VarType == funcType or VarType == 'op_container':
                cuadruplo = [SemanticCube.opToKey['return'],SemanticCube.TypeToKey[VarType],value,returnDir]
                self.Quad.append(cuadruplo)
            else:
                print('#GenerateFunReturns Error: Se esta intentando retornar un valor de tipo',VarType,'de una funcion tipo',funcType)
                sys.exit()
            
            cuadruplo = [SemanticCube.opToKey['ENDPROC'],-1,-1,-1]
            self.Quad.append(cuadruplo)
        


    #Funcion que valida que una funcion distinta a void tenga por lo menos un retorno
    def verifyReturn(self):
        funcType = self.funDirectory[self.currentFunction][0]
        if funcType != 'void':
            if self.haveReturn == False:
                print('#verifyReturn Error: La funcion',self.currentFunction,' de tipo',funcType,'necesita por lo menos un return()')
                sys.exit()
        elif funcType == 'void' and self.haveReturn:
            print('#verifyReturn Error: La funcion',self.currentFunction,' de tipo',funcType,'no debe tener return()')
            sys.exit()
        self.haveReturn = False


    #Funcion que genera el Goto de una Funcion
    def GenerateFunGoto(self):
        cuadruplo = [SemanticCube.opToKey['Goto'],-1,-1,-1]
        self.Quad.append(cuadruplo)
        self.PJumps.append(len(self.Quad) - 1)
        self.funDirectory[self.currentFunction][5] = len(self.Quad)

    #Funcion que llena el Goto de una Funcion
    def FillFunGoto(self):
        returns = self.PJumps.pop()
        self.Quad[returns][3] = len(self.Quad)

    #Funcion que genera el cuadruplo ERA
    def GenerateEra(self,functionId):
        cuadruplo = [SemanticCube.opToKey['ERA'],-1,-1,functionId]
        self.Quad.append(cuadruplo)
    
    #Funcion que inicializa un contenedor
    def GenerateEmptyContainer(self,functionId):
        result = self.returnTemp(functionId)
        self.CurrentCotainer = result
        cuadruplo = [SemanticCube.opToKey['[]'],-1,-1,result]
        self.Quad.append(cuadruplo)

    #Funcion que llena un contenedor
    def GenerateFillContainer(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            if valueType != 'container':
                cuadruplo = [SemanticCube.opToKey['append'],value,-1,self.CurrentCotainer]
                self.Quad.append(cuadruplo)
            else:
                print('#GenerateFillContainer Error: Se esta intentando insertar un valor de tipo',valueType)
                sys.exit()

    #Funcion que inserta el contenedor a la pila de Operadores
    def RegisterContainer(self):
        self.PTypes.append('container')
        self.PilaO.append(self.CurrentCotainer)

    #Funcion que genera un cuadruplo de contatenacion de contenedores
    def GenerateConcatContainer(self,functionId):
        if len(self.PilaO) > 1 and len(self.PTypes) > 1:
            RightContainer = self.PilaO.pop()
            self.PTypes.pop()
            LeftContainer = self.PilaO.pop()
            self.PTypes.pop()
            result = self.returnTemp(functionId)
            cuadruplo = [SemanticCube.opToKey['concat'],LeftContainer,RightContainer,result]
            self.Quad.append(cuadruplo)
            self.PilaO.append(result)
            self.PTypes.append('container')
    
    #Funcion para generar un cuadruplo de length, get_front y get_back
    def FuncionOPContainer1(self,flag,varId,functionId):
        result = self.returnTemp(functionId)
        cuadruplo = [SemanticCube.opToKey[flag],-1,varId,result]
        self.Quad.append(cuadruplo)
        # Aqui hay que resaltar que el tipo que se introduce es:
        # "El que se espera, no necesariamente es el tipo del valor que regresa"
        # *** SE TIENE QUE VALIDAR EL TIPO EN LA MAQUINA VIRTUAL ***
        return result
    
    #Funcion para generar un cuadruplo de get
    def FuncionOPContainer2(self,flag,varId,functionId):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            result = self.returnTemp(functionId)
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            if valueType == 'number' or valueType == 'op_container':
                cuadruplo = [SemanticCube.opToKey[flag],value,varId,result]
                self.Quad.append(cuadruplo)
                # Aqui hay que resaltar que el tipo que se introduce es:
                # "El que se espera, no necesariamente es el tipo del valor que regresa"
                # *** SE TIENE QUE VALIDAR EL TIPO EN LA MAQUINA VIRTUAL ***
            else:
                print('#FuncionOPContainer2 Error: El indice proporcionado no es de tipo numerico')
                sys.exit()
            return result
    
    #Funcion para generar un cuadruplo de insert_back y insert_front
    def FuncionOPContainer3(self,flag,varId):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            cuadruplo = [SemanticCube.opToKey[flag],value,-1,varId]
            self.Quad.append(cuadruplo)
   
   #Funcion para generar un cuadruplo de insert
    def FuncionOPContainer4(self,flag,varId):
        if len(self.PilaO) > 1 and len(self.PTypes) > 1:
            element = self.PilaO.pop()
            elementType = self.PTypes.pop()
            index = self.PilaO.pop()
            indexType = self.PTypes.pop()
            if indexType == 'number' or indexType == 'op_container':
                cuadruplo = [SemanticCube.opToKey[flag],index,element,varId]
                self.Quad.append(cuadruplo)
            else:
                print('#FuncionOPContainer4 Error: El indice proporcionado no es de tipo numerico')
                sys.exit()

    #Funcion para generar un cuadruplo de parametro
    def GenerateParameter(self,parametros,funcionId):
        if len(parametros) > 0:
            if len(self.PilaO) > 0 and len(self.PTypes) > 0:
                valueType = self.PTypes.pop()
                value = self.PilaO.pop()
                if self.paramCounter < len(parametros):
                    if parametros[self.paramCounter] == valueType or valueType == 'op_container':
                        cuadruplo = [SemanticCube.opToKey['param'],value,[SemanticCube.TypeToKey[valueType],SemanticCube.TypeToKey[parametros[self.paramCounter]]],self.paramCounter]
                        self.Quad.append(cuadruplo)
                    else:
                        print('#GenerateParameter Error: El tipo del parametro',self.paramCounter+1,'es',parametros[self.paramCounter],'y el tipo que se esta pasando es',valueType)
                        sys.exit()
                    self.paramCounter = self.paramCounter + 1
                else:
                    print('#GenerateParameter Error: La funcion',funcionId,"()",'tiene unicamente',len(parametros),'parametros')
                    sys.exit()
        else:
            print('#GenerateParameter Error: La funcion',funcionId,"()",'no recibe parametros')
            sys.exit()

    #Funcion que revisa si se mandaron todos los parametros y ademas resetea el contador de parametros y hace el GOSUB
    def VerifyParameters(self, parametros, funcionId):
        if len(parametros) == self.paramCounter:
            cuadruplo = [SemanticCube.opToKey['gosub'],-1,-1,self.funDirectory[funcionId][5]]
            self.Quad.append(cuadruplo)
        else:
            print('#VerifyParameters Error: faltan',len(parametros) - self.paramCounter,'parametro(s) an la llamada a la funcion',funcionId)
            sys.exit()
        self.paramCounter = 0

    #Funcion que genera el cuadruplo de ENDPROC
    def GenerateEndProc(self):
        cuadruplo = [SemanticCube.opToKey['ENDPROC'],-1,-1,-1]
        self.Quad.append(cuadruplo)

    #Funcion unicamente para debuggear
    def printCuad(self):
        cont = 0
        print(" ")
        print("++++++++++++ PilaO +++++++++++++++")
        print(self.PilaO)
        print("++++++++++++++++++++++++++++++++++")
        print(" ")
        print("--------------- PTypes -----------")
        print(self.PTypes)
        print("----------------------------------")
        print(" ")
        print("::::::::::::::::: POper ::::::::::")
        print(self.POper)
        print("::::::::::::::::::::::::::::::::::")
        print(" ")
        print('=========== CUADRUPLOS ===========')
        for cuad in range(len(self.Quad)):
            print(cont,self.Quad[cuad])
            cont = cont + 1
        print('==================================')
    
    #Funcion para debug se puede llamar con self.printAll()
    def printAll(self):
        print("***************")
        print("PilaO")
        print("***************")
        for element in  self.PilaO:
            print(element)
            print("***************")
        print("PTypes")
        print("***************")
        for element in  self.PTypes:
            print(element)
            print("***************")
        print("POper")
        print("***************")
        for element in  self.POper:
            print(element)
            print("***************")

    #Funcion que regresa los cuadruplos
    def ReturnCuads(self):
        return self.Quad

    #Agregar valores de la function call
    def addValueToStack(self,value,valueType):
        if value == -999:
            print('#addValueToStack Error: La funcion a la que se esta llamando es de tipo void')
            sys.exit()
        else:
            if valueType == 'error':
                print('#addValueToStack Error: La funcion a la que se esta llamando no existe')
                sys.exit()
            else:
                self.PTypes.append(valueType)
                self.PilaO.append(value)
