class VirtualMachine:
    def __init__(self):
        self.Global = []
        self.Local = []
        self.Temporal = []
        self.Constante = []
        self.Cuadruplos = []
    
    def PrintCuadruplos(self):
         cont = 0
         for cuad in range(len(self.Cuadruplos)):
            print(cont,self.Cuadruplos[cuad])
            cont = cont + 1