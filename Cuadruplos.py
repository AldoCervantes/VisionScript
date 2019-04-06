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
        self.memTimes = 50000

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
                print("#FuncionRepUntil2 Error: Se esta intentando hacer un if con una expresion de tipo",exp_type)

    #Funcion 3 de repat until
    def FuncionRepUntil3(self):
        end = self.PJumps.pop()
        returns = self.PJumps.pop()
        cuadruplo = [SemanticCube.opToKey['Goto'],-1,-1,returns]
        self.Quad.append(cuadruplo)
        self.Quad[end][3] = len(self.Quad)

    #Funcion 1 de repat times
    def FuncionRepTimes1(self):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            value = self.PilaO.pop()
            if valueType == 'number':
                vartimes = self.memTimes
                self.memTimes = self.memTimes + 1
                cuadruplo = [SemanticCube.opToKey['='],30000,-1,vartimes]
                self.Quad.append(cuadruplo)
                self.PJumps.append(len(self.Quad))

                cuadruplo = [SemanticCube.opToKey['+'],vartimes,30001,self.memTemporal]
                self.Quad.append(cuadruplo)

                cuadruplo = [SemanticCube.opToKey['='],self.memTemporal,-1,vartimes]
                self.Quad.append(cuadruplo)
                self.memTemporal = self.memTemporal + 1

                cuadruplo = [SemanticCube.opToKey['<'],vartimes,value,self.memTemporal]
                self.Quad.append(cuadruplo)

                cuadruplo = [SemanticCube.opToKey['GotoF'],self.memTemporal,-1,-1]
                self.Quad.append(cuadruplo)

                self.memTemporal = self.memTemporal + 1

                self.PJumps.append(len(self.Quad) -1)
            else:
                print("#FuncionRepTimes1 Error: Se esta intentando hacer un times con una expresion de tipo",valueType)

    #Funcion para Generar los cuadruplos de los 3 tipos de print
    def GeneratePrintCuad(self,flag):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            self.PTypes.pop()
            cuadruplo = [SemanticCube.opToKey[flag],self.PilaO.pop(),-1,-1]
            self.Quad.append(cuadruplo)

    #Funcion para generar los cuadruplos de la funcion read
    def GenerateReadCuad(self,flag):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            self.PTypes.pop()
            cuadruplo = [SemanticCube.opToKey[flag],-1,-1,self.PilaO.pop()]
            self.Quad.append(cuadruplo)
    
    def InsertParentesis(self): #Funcion 6
        self.POper.append('(')
    
    def RemoveParentesis(self): # Funcion 7
        self.POper.pop()

    def printCuad(self):
        cont = 0
        for cuad in range(len(self.Quad)):
            print(cont,self.Quad[cuad])
            cont = cont + 1
    
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