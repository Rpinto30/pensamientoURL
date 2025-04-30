#EJERCICIO NO.1
class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
class Perro(Animal):
    def __init__(self, nombre, edad, peso, altura, dosis):
        super().__init__(nombre, edad, peso)
        self.altura = altura
        self.dosis = dosis
    
    def check(self):
        print("Datos medicos")
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"peso: {self.peso}")
        print(f"altura: {self.altura}")
    
    def med(self):   
        print(f"Su dosis es: {self.dosis}")
        
class Gato(Animal):
    def __init__(self, nombre, edad, peso, altura, glucosa, dosis):
        super().__init__(nombre, edad, peso)
        self.altura = altura
        self.glucosa = glucosa
        self.dosis = dosis
    
    def check(self):
        print("Datos medicos")
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"peso: {self.peso}")
        print(f"altura: {self.altura}")
        print(f"glucosa: {self.glucosa}")
    
    def med(self):   
        print(f"Su dosis es: {self.dosis}")
        
class Ave(Animal):
    def __init__(self, nombre, edad, peso, plumas, dosis):
        super().__init__(nombre, edad, peso)
        self.plumas = plumas
        self.dosis = dosis
        
    def check(self):
        print("Datos medicos")
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"peso: {self.peso}")
        print(f"plumas cantidad: {self.plumas}")
        
    def med(self):   
        print(f"Su dosis es: {self.dosis}")
        
class Reptil(Animal):
    def __init__(self, nombre, edad, peso, color, dosis, extremidades):
        super().__init__(nombre, edad, peso)
        self.color = color
        self.dosis = dosis
        self.extremidades = extremidades
    
    def check(self):
        print("Datos medicos")
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"peso: {self.peso}")
        print(f"color: {self.color}")
        print(f"Tiene todas las extremidades?: {self.extremidades}")
        
    def med(self):   
        print(f"Su dosis es: {self.dosis}")
        
        
perro1 = Perro('Enya', 8, 20, 30, 4)
gato1 = Gato('Mochi', 4, 50, 40, 4000, 2)
perico = Ave('peciro', 50, 20, 8000, 14)
tortuga = Reptil('chispitas', 1, 5, 'verde', 14, 'Sí')

perro1.check()
perro1.med()

gato1.check()
gato1.med()

perico.check()
perico.med()

tortuga.check()
tortuga.med()

#EJERCICIO 2
class Persona:
    def __init__(self, nombre,edad,DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, carnet,cursos):
        super().__init__(nombre, edad, DNI)
        self.carnet = carnet
        self.cursos = cursos
    
    def datos(self):
        print(f"El estudiante {self.nombre}")
        print(f"Su edad es de {self.edad}")
        print(f"Su DNI es de {self.DNI}")
        print(f"Su carnet es {self.carnet}")
        print(f"Está asigniado a {self.cursos} cursos")

        
class Prosfesor(Persona):
    def __init__(self, nombre, edad, DNI, materia, abuelo):
        super().__init__(nombre, edad, DNI)
        self.materia = materia
        self.abuelo = abuelo
        
    def datos(self):
        print(f"El profesor {self.nombre}")
        print(f"Su edad es de {self.edad}")
        print(f"Su DNI es {self.DNI}")
        print(f"Da el curso de {self.materia}")
        print(f"Su abuelo es {self.abuelo}")
        
class Administrativo(Persona):
    def __init__(self, nombre, edad, DNI, especializacion,atomo):
        super().__init__(nombre, edad, DNI)
        self.especializacion = especializacion
        self.atomo = atomo
    
    def datos(self):
        print(f"El administrativo {self.nombre}")
        print(f"Su edad es de {self.edad}")
        print(f"Su DNI es {self.DNI}")
        print(f"Está especializado en {self.especializacion}")
        print(f"Tiene {self.atomo} atomos")

est = Estudiante('Jose', 25, 9375098, 157425, 'Filosofia')
prof = Prosfesor('Byron', 50, 394857, 'Bioquimica', 'Paco')
adm = Administrativo('Mario',75,93857349,'Encargado de banco de la U', 80000000000000000)

est.datos()
prof.datos()
adm.datos()