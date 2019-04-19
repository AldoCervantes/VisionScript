from collections import deque
from SemanticCube import SemanticCube

class Cuadruplos:
    SemanticCube = SemanticCube()
    
    def __init__(self):
        self.PilaO = [] #Pila donde van a ir los Operandos (1,a,"text",false,...)
        self.PTypes = [] #Pila de tipos (number,text,bool,container)
        self.POper = [] #Pila de Operadores (+,-,*,/,...)
        self.Quad = deque([]) #Fila de Cuadruplos
        self.PJumps = [] #Pila de saltos
        self.memTemporal = 40000
        self.paramCounter = 0
        self.CurrentCotainer = 0

    def InsertIdType(self,varId,VarType): #Funcion 1
        self.PilaO.append(varId)
        self.PTypes.append(VarType)
    
    def InsertOperator(self,operator): #Funcion 2, 3 , 8 y 10
        self.POper.append(operator)
    
    #Para operaciones aritmeticas
    def GenerateCuad(self,flag): # Funcion 4 , 5 , 9 y 11
        if len(self.POper) > 0:
            top = self.POper[len(self.POper)-1]
            if (flag == 'Termino' and (top == '+' or top == '-')) or (flag == 'Factor' and (top == '*' or top == '/')) or (flag == 'Expresion' and (top == '>' or top == '<'or top == '<=' or top == '>=' or top == 'not_equal' or top == 'equal')) or (flag == 'Mega_Expresion'  and (top == 'and' or top == 'or')):
                    right_operand = self.PilaO.pop()
                    right_type = self.PTypes.pop()
                    left_operand = self.PilaO.pop()
                    left_type = self.PTypes.pop()
                    operator = self.POper.pop()
                    result_type = SemanticCube.semanticCube[operator][left_type][right_type]
                    if result_type != 'error':
                        # result <- AVAIL.next()
                        result = self.memTemporal
                        self.memTemporal = self.memTemporal + 1
                        cuadruplo = [SemanticCube.opToKey[operator], left_operand, right_operand, result]
                        self.Quad.append(cuadruplo)
                        self.PilaO.append(result)
                        self.PTypes.append(result_type)
                        # If any operands were a temporal space, return into AVAIL
                    else:
                        print("#GenerateCuad Error:",left_operand,"=>",left_type,operator,right_operand,"=>",right_type,"genera",result_type)
    
    #Funcion que genera un cuaduplo de asignacion [=,valor,-1,id]
    def GenerateAssignmentCuad(self,varId,targetType):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            if valueType == targetType:
                cuadruplo = [SemanticCube.opToKey['='],value,-1,varId]
                self.Quad.append(cuadruplo) 
            else:
                print("#GenerateAssignmentCuad Error: Se esta intentando asignar un valor de tipo",valueType,"a una variable de tipo",targetType)
    
    #Funcion 1 de IF
    def FuncionIF1(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            result = self.PilaO.pop()
            exp_type = self.PTypes.pop()
            if exp_type == 'bool':
                cuadruplo = [SemanticCube.opToKey['GotoF'],result,-1,-1]
                self.Quad.append(cuadruplo)
                self.PJumps.append(len(self.Quad) - 1 )
            else:
                print("#GenerateGotoF Error: Se esta intentando hacer un if con una expresion de tipo",exp_type)

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
            if exp_type == 'bool':
                cuadruplo = [SemanticCube.opToKey['GotoF'],result,-1,-1]
                self.Quad.append(cuadruplo)
                self.PJumps.append(len(self.Quad) - 1 )
            else:
                print("#FuncionRepUntil2 Error: Se esta intentando hacer un repeat con una expresion de tipo",exp_type)

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
    def GenerateFunReturns(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            VarType = self.PTypes.pop()
            value = self.PilaO.pop()
            cuadruplo = [SemanticCube.opToKey['return'],SemanticCube.TypeToKey[VarType],-1,value]
            self.Quad.append(cuadruplo)

    #Funcion que genera el Goto de una Funcion
    def GenerateFunGoto(self):
        cuadruplo = ['Goto',-1,-1,-1]
        self.Quad.append(cuadruplo)
        self.PJumps.append(len(self.Quad) - 1)

    #Funcion que llena el Goto de una Funcion
    def FillFunGoto(self):
        returns = self.PJumps.pop()
        self.Quad[returns][3] = len(self.Quad)

    #Funcion que genera el cuadruplo ERA
    def GenerateEra(self,functionId):
        cuadruplo = ['ERA',-1,-1,functionId]
        self.Quad.append(cuadruplo)
    
    #Funcion que inicializa un contenedor
    def GenerateEmptyContainer(self):
        result = self.memTemporal
        self.memTemporal = self.memTemporal + 1
        self.CurrentCotainer = result
        cuadruplo = ['=','[]',-1,result]
        self.Quad.append(cuadruplo)

    #Funcion que llena un contenedor
    def GenerateFillContainer(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            if valueType != 'container':
                cuadruplo = ['append',value,-1,self.CurrentCotainer]
                self.Quad.append(cuadruplo)
            else:
                print('#GenerateFillContainer Error: Se esta intentando insertar un valor de tipo',valueType)

    #Funcion que inserta el contenedor a la pila de Operadores
    def RegisterContainer(self):
        self.PTypes.append('container')
        self.PilaO.append(self.CurrentCotainer)

    #Funcion que genera un cuadruplo de contatenacion de contenedores
    def GenerateConcatContainer(self):
        if len(self.PilaO) > 1 and len(self.PTypes) > 1:
            RightContainer = self.PilaO.pop()
            self.PTypes.pop()
            LeftContainer = self.PilaO.pop()
            self.PTypes.pop()
            result = self.memTemporal
            self.memTemporal = self.memTemporal + 1
            cuadruplo = ['contant',LeftContainer,RightContainer,result]
            self.Quad.append(cuadruplo)
            self.PilaO.append(result)
            self.PTypes.append('container')

    def FuncionOPContainer1(self,flag,varId):
        result = self.memTemporal
        self.memTemporal = self.memTemporal + 1
        cuadruplo = [flag,-1,varId,result]
        self.Quad.append(cuadruplo)

    def FuncionOPContainer2(self,flag,varId):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            result = self.memTemporal
            self.memTemporal = self.memTemporal + 1
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            cuadruplo = [flag,value,varId,result]
            self.Quad.append(cuadruplo)

    def FuncionOPContainer3(self,flag,varId):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            cuadruplo = [flag,value,-1,varId]
            self.Quad.append(cuadruplo)
   
    def FuncionOPContainer4(self,flag,varId):
        if len(self.PilaO) > 1 and len(self.PTypes) > 1:
            element = self.PilaO.pop()
            self.PTypes.pop()
            index = self.PilaO.pop()
            self.PTypes.pop()
            cuadruplo = [flag,index,element,varId]
            self.Quad.append(cuadruplo)

    #Funcion para generar un cuadruplo de parametro
    def GenerateParameter(self,parametros,funcionId):
        if len(parametros) > 0:
            if len(self.PilaO) > 0 and len(self.PTypes) > 0:
                valueType = self.PTypes.pop()
                value = self.PilaO.pop()
                if self.paramCounter < len(parametros):
                    if parametros[self.paramCounter] == valueType:
                        cuadruplo = ['param',value,valueType,'param' + str(self.paramCounter)]
                        self.Quad.append(cuadruplo)
                    else:
                        print('#GenerateParameter Error: El tipo del parametro',self.paramCounter+1,'es',parametros[self.paramCounter],'y el tipo que se esta pasando es',valueType)
                    self.paramCounter = self.paramCounter + 1
                else:
                    print('#GenerateParameter Error: La funcion',funcionId,"()",'tiene unicamente',len(parametros),'parametros')
        else:
            print('#GenerateParameter Error: La funcion',funcionId,"()",'no recibe parametros')

    #Funcion que revisa si se mandaron todos los parametros y ademas resetea el contador de parametros y hace el GOSUB
    def VerifyParameters(self, parametros, funcionId):
        if len(parametros) == self.paramCounter:
            cuadruplo = ['gosub',-1,-1,funcionId]
            self.Quad.append(cuadruplo)
        else:
            print('#VerifyParameters Error: faltan',len(parametros) - self.paramCounter,'parametro(s) an la llamada a la funcion',funcionId)
        self.paramCounter = 0

    #Funcion unicamente para debuggear
    def printCuad(self):
        cont = 0
        print(" ")
        print("++++++++++++ PilaO ++++++++++++++++")
        print(self.PilaO)
        print("++++++++++++++++++++++++++++++++++")
        print(" ")
        print("--------------- PTypes -------------")
        print(self.PTypes)
        print("-------------------------------------")
        print(" ")
        print("================== POper =============")
        print(self.POper)
        print("====================================")
        print(" ")
        print('=========== CUADRUPLOS ==========')
        for cuad in range(len(self.Quad)):
            print(cont,self.Quad[cuad])
            cont = cont + 1
        print('=================================')
    
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