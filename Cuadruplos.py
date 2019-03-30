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
                        print("Error:",left_operand,operator,right_operand,"genera",result_type)
        if flag == 'Assignment':
            if len(self.PilaO) > 0:
                print("=",self.PilaO.pop())
            #print("=",self.PilaO) ESTO TE DA LOS VALORES FINALES 
            #EN TEORIA ASI DEBERIA SER CUANDO LLEGA UN =
            # cuadruplo = [SemanticCube.opToKey['='],value,-1,target]
            # self.Quad.append(cuadruplo) 
           
    def InsertParentesis(self): #Funcion 6
        self.POper.append('(')
    
    def RemoveParentesis(self): # Funcion 7
        self.POper.pop()

    def printCuad(self):
        for cuad in range(len(self.Quad)):
            print(self.Quad[cuad])


        