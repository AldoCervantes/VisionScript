class VirtualMachine:
    def __init__(self):
        self.Global = []
        self.Local = []
        self.Temporal = []
        self.Constante = []
        self.Cuadruplos = []
        self.currentCuad = 0

    def PrintCuadruplos(self):
         cont = 0
         for cuad in range(len(self.Cuadruplos)):
            print(cont,self.Cuadruplos[cuad])
            cont = cont + 1

    #a esta funcion se le manda el cuadruplo Cuadruplos[i], ej. [0, 30000, -1, 10000]
    def OperacionesAritmeticas(self, cuadruplo):
        op = cuadruplo[0]
        arg1 = self.cuadruplo[1]
        arg2 = self.cuadruplo[2]

        if op == '+':
            arg3 = arg1 + arg2
        elif op == '-':
            arg3 = arg1 - arg2
        elif op == '*':
            arg3 = arg1 * arg2
        elif op == '/':
            if(arg2 == 0):
                print('ERROR, se esta intentando una division con 0')
                #para detenerlo
                sys.exit()
            else: arg3 = arg1 / arg2
        #funcion de set value??
        #setValue(cuadruplo[3], arg3)

    def OperacionesLogicas(self,cuadruplo):
        op = cuadruplo[0]
        arg1 = self.cuadruplo[1]
        arg2 = self.cuadruplo[2]

        if op == 'and':
            arg3 = arg1 and arg2
        elif op == 'or':
            arg3 = arg1 or arg2 
        elif op == '<':
            arg3 = arg1 < arg2
        elif op == '<=':
            arg3 = arg1 <= arg2
        elif op == '>':
            arg3 = arg1 > arg2
        elif op == '>=':
            arg3 = arg1 >= arg2
        elif op == 'not_equl':
            arg3 = arg1 != arg2
        elif op == 'equal':
            arg3 = arg1 == arg2 
        #funcion de set value??
        #setValue(cuadruplo[3], arg3)

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

    def Write(self, cuadruplo):
        op = cuadruplo[0]
        
        if op == 'print':
            a = 0
            #print()
        elif op == 'hear':
            a = 1
            #funcion hear
        elif op == 'braille':
            a = 2
            #funcion braille
            
    def Read(self, cuadruplo):
        temporal = input()
        tipo = cuadruplo[1]
        if tipo == 'number':
            temp = float(temp)
        elif tipo == 'text':
            temp = str(temp)
        elif tipo == 'bool':
            if temp == 'TRUE' or temp == 'true' or temp == 'True':
                temp = 1
            else:
                temp = 0
        #setValue(cuadruplo[3], temp)


    def run(self):
        while self.Cuadruplos[self.currentCuad][0] != 'END OF CODE':
            cuadruplo = self.Cuadruplos[self.currentCuad]
            op = cuadruplo[0]
            if op == 'Goto':
                self.GoTo(cuadruplo)
            elif op == 'GotoF':
                self.GoToF(cuadruplo)
            elif op == 'ERA':
                self.ERA(cuadruplo)
            elif op == 'gosub':
                self.GOSUB(cuadruplo)
            elif op == 'param':
                self.PARAM(cuadruplo)
            elif op == 'return':
                self.RETURN(cuadruplo)
            elif  op == 'append' or op == 'concat' or op == 'insert' or op == 'insert_back' or op == 'insert_front' or op == 'get' or op == 'get_back' or op == 'get_front' or op == 'length':
                self.OperacionesContenedores(cuadruplo)
            elif op == '+' or op == '-' or op == '*' or op == '/':
                self.OperacionesAritmeticas(cuadruplo)
            elif  op == 'and' or op == 'or' or op == '<' or op == '<=' or op == '>' or op == '>=' or op == 'not_equl' or op == 'equal':
                self.OperacionesLogicas(cuadruplo)
            elif op == '=':
                self.Assignacion(cuadruplo)
            elif op == 'print' or op == 'hear' or op == 'braille':
                self.Write(cuadruplo)
            elif op == 'read':
                self.Read(cuadruplo)
            else:
                print('ERROR, cuadruplo invalido: ')
                print(cuadruplo)
            self.currentCuad = self.currentCuad + 1

