import math
from abc import ABC, abstractmethod

#EJERCICIO 1
class ExperimentoFisico:
    @abstractmethod
    def calcula_tiempo():
        pass

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad= 9.81):
        self.altura = altura
        self.gravedad = gravedad
        
    def calcula_tiempo(self):
        try:
            return math.sqrt(2*self.altura/self.gravedad)
        except:
            return ' No se permite altura negativa o gravedad 0'
    
caida = CaidaLibre(altura=-5)
print(f"El tiempo de caida es: {caida.calcula_tiempo()}")

#EJRCICIO 2
class OperacionCientifica:
    @abstractmethod
    def calcular():
        pass

class Raiz_cuadrada:
    def __init__(self, n):
        self.n = n
        
    def calcular(self):
        try:
            return self.n**(1/2)
        except: 
            return ' No se puede raiz de un numero negativo'
    
class Potencia:
    def __init__(self, n, exponente):
        self.n = n
        self.exponente = exponente
        
    def calcular(self):
        return self.n**self.exponente
    
class Logaritmo:
    def __init__(self, n, base):
        self.n = n
        self.base = base
        
    def calcular(self):
        try:
            return math.log(self.n, self.base)
        except: 
            return ' No se puede logaritmo de menor o igual 0'
    
class factorial:
    def __init__(self, n):
        self.n = n
    def calcular(self):
        try:
            fac = 1
            for i in range(1,self.n+1):
                fac*=i 
            return fac          
        except: 
            return ' No se puede factorial de un numero negativo o decimal'
