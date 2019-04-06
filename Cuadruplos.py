from collections import deque
from SemanticCube import SemanticCube

class Cuadruplos:
    SemanticCube = SemanticCube()
    
    def __init__(self):
        self.PilaO = [] #Pila donde van a ir los Operandos (1,a,"text",false,...)
        self.PTypes = [] #Pila de tipos (number,text,bool,container)
        self.POper = [] #Pila de Operadores (+,-,*,/,...)
        self.Quad = deque([]) #Fila de Cuadruplos
        self.memTemporal = 30000

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
                        print("Error:",left_operand,"=>",left_type,operator,right_operand,"=>",right_type,"genera",result_type)
    
    #Funcion que genera un cuaduplo de asignacion [=,valor,-1,id]
    def GenerateAssignmentCuad(self,varId,targetType):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            valueType = self.PTypes.pop()
            if valueType == targetType:
                cuadruplo = [SemanticCube.opToKey['='],self.PilaO.pop(),-1,varId]
                self.Quad.append(cuadruplo) 
            else:
                print("Error: Se esta intentando asignar un valor de tipo",valueType,"a una variable de tipo",targetType)
    
    def GeneratePrintCuad(self,flag):
        if len(self.PilaO) > 0 and len(self.PTypes) > 0:
            self.PTypes.pop()
            cuadruplo = [SemanticCube.opToKey[flag],-1,-1,self.PilaO.pop()]
            self.Quad.append(cuadruplo)

    def InsertParentesis(self): #Funcion 6
        self.POper.append('(')
    
    def RemoveParentesis(self): # Funcion 7
        self.POper.pop()

    def printCuad(self):
        for cuad in range(len(self.Quad)):
            print(self.Quad[cuad])
    
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