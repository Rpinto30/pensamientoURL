class Calculadora_nodinamica:
    def __init__(self, a: int,b: int):
        self.a = a 
        self.b = b
    #AND
    def suma(self):
        r = []
        if len(self.a) == len(self.b):
            print("A Y B")
            for i in range(len(self.a)):
                r.append(self.a[i] and self.b[i])
                print(self.a[i], self.b[i], r[i])
            return r
        else: 
            print("no se puede operar A con B")
            return []

    #OR
    def resta(self):
        r = []
        if len(self.a) == len(self.b):
            print("A O B")
            for i in range(len(self.a)):
                r.append(self.a[i] or self.b[i])
                print(self.a[i], self.b[i], r[i])
            return r
        else: 
            print("no se puede operar A con B")
            return []
    
    #NOT
    def multiplicacion(self):
        r = [[],[]]
        if len(self.a) == len(self.b):
            print("A not B not")
            for i in range(len(self.a)):
                if self.a[i] == 0: r[0].append(1)
                else: r[0].append(0)
                
                if self.b[i] == 0: r[1].append(1)
                else: r[1].append(0)
                print(self.a[i], r[0][i], "|", self.b[i], r[1][i])
            return r
        else: 
            print("no se puede operar A con B")
            return []


A = [0,1,1,0]
B = [1,1,1,0]
operar = Calculadora_nodinamica([0,1,1,0],[1,1,1,0])


operar.suma()
operar.resta()
operar.multiplicacion()
