'''
Rodrigo Andrés Pinto Ticú - 1507325
Rodrigo Herman Cardenas - 1505925
Pablo David Quijivix Suchi - 1578125
'''

niños_grupo = []
departamentos = ['Alta Verapaz','Baja Verapaz', 'Chimaltenango','Chiquimula','Guatemala',
                 'El Progreso','Escuintla','Huehuetenango','Izabal','Jalapa','Jutiapa','Peten',
                 'Quetzaltenango','Quiche','Retalhuleu','Sacatepequez','San Marcos','Santa Rosa',
                 'Solola','Suchitepequez','Totonicapan','Zacapa']

#RANGOS EXTRAIDOS DE: https://www.apollohospitals.com/es/health-library/baby-girl-growth-chart
OMS_peso = {
    0:(2.5,4.4), 1:(3.4,5.4), 2:(4.4, 6.5), 3:(5.4,7.4), 4:(5.8,7.9), 5:(6.2,8.4), 6:(6.5,8.8), 7:(6.8,9.0), 8:(7.0,9.2), 9:(7.2,9.4), 10:(7.4,9.6), 11:(7.6,9.8), 
    12:(8,10.8), 13:(8.2,11), 14:(8.4,11.2), 15:(8.6,11.4), 16:(8.8,11.6), 17:(9,11.8), 18:(9,11.8), 19:(9.2,12), 20:(9.4,12.2), 21:(9.6,12.4), 22:(9.8,12.6), 
    23:(10,12.8), 24:(10,13)    
}
OMS_long = {
    0 : (45,54), 1 : (50,58), 2 : (53,61), 3 : (56,63), 4 : (58,65), 5 : (60,67), 6 : (62,69), 7 : (63.5,70), 8 : (64.5,71), 9 : (65, 72), 10 : (66,73), 11 : (67,74),
    12 : (70,78), 13 : (71,79), 14 : (72,80), 15 : (73,81), 16 : (74,82), 17 : (75,83), 18 : (77,85), 19 : (78,86), 20 : (79,87), 21 : (80,88), 22 : (81,89),
    23 : (82,90), 24 : (83,91)
}

OMS_percad = {
    0:(32,35), 1:(34,37), 2:(36, 37), 3:(37,41), 4:(38,42), 5:(39,43), 6:(40,44), 7:(40.5,44.5), 8:(41,45), 9:(41.5,45.2), 10:(42,45.4), 11:(42.5,45.6),
    12:(43,47), 13:(43.5,47.2), 14:(44,47.4), 15:(44.5,47.6), 16:(44.8,47.8), 17:(45,48), 18:(45,48), 19:(45.2,48.4), 20:(45.4,48.4), 21:(45.6,48.6), 22:(45.8,48.8), 
    23:(46,49), 24:(46,49)
}
#CREAR CLASE NIÑOS
class Niños:
    prom_peso, prom_talla, prom_pcran = '','',''
    def __init__(self,nombre:str,
                 edad:int,
                 peso:float,
                 talla:float,
                 perimetro_craneal:float,
                 departamento:str):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.perimetro_craneal = perimetro_craneal
        self.departamento = departamento
        niños_grupo.append(self)
        
print("-"*20+"Bienvenido!"+"-"*20)

#---------------------------------------------------TOMA DE DATOS---------------------------------------------------------------
while True: #INGRESO DE NIÑOS
    try:
        n_niños = int(input("> Ingrese la cantidad de niños menores a 24 meses: "))
        if n_niños > 0: break
        else: print("Lo siento, entrada invalida, vuelva a intentar")
    except ValueError:
        print("Lo siento, debe ser un valor entero, vuelva a intentarlo")
        
for n in range(n_niños): #FOR CREAR NIÑOS
    print("\n","-"*10+f"Ingrese el datos del niño {n+1}"+"-"*10)
    nombre = input("> Ingrese el nombre del niño: ")
    
    while True: #EDAD
        try:
            edad = int(input("> Ingrese la edad del niño (en meses): "))
            if 0 <= edad <= 24: break
            else: print("Lo siento, entrada invalida, vuelva a intentar")
        except ValueError:
            print("Lo siento, debe ser un valor entero, vuelva a intentarlo")
            
    
    while True:#PESO
        try:
            peso = float(input("Ingrese el peso del niño en kilogramos: "))
            if peso > 0: break
            else: print("Lo siento, entrada invalida, vuelva a intentar")
        except ValueError:
            print("Lo siento, debe ser un valor entero, vuelva a intentarlo")

    while True:#TALLA
        try: 
            talla = float(input("Ingrese la estatura en centimetros: "))
            if talla > 0: break
            else: print("Lo siento, entrada invalida, vuelva a intentar")
        except ValueError:
            print("Lo siento, debe ser un valor numerico, vuelva a intentarlo")

    while True:#PCRANEAL
        try:
            pcraneal = float(input("Ingrese en centimetros el perimetro craneal: "))
            if pcraneal > 0: break
            else: print("Lo siento, entrada invalida, vuelva a intentar")
        except ValueError:
            print("Lo siento, debe ser un valor numerico, vuelva a intentarlo")
    
    while True:
        print("\nIngrese el departamento del niño:")
        try:
            print(f"{'   1)Alta Verapaz':<20}{'   2)Baja Verapaz':<20}{'   3)Chimaltenango':<20}{'   4)Chiquimula'}")
            print(f"{'   5)Guatemala':<20}{'   6)El Progreso':<20}{'   7)Escuintla':<20}{'   8)Huehuetenango'}")
            print(f"{'   9)Izabal':<20}{'   10)Jalapa':<20}{'   11)Jutiapa':<20}{'   12)Peten'}")
            print(f"{'   13)Quetzaltenango':<20}{'   14)Quiche':<20}{'   15)Retalhuleu':<20}{'   16)Sacatepequez'}")
            print(f"{'   17)San Marcos':<20}{'   18)Santa Rosa':<20}{'   19)Solola':<20}{'   20)Suchitepequez'}")
            print(f"{'   21)Totonicapan':<20}{'   22)Zacapa'}")
            dep = int(input("> Ingrese el departamento donde recide: "))
            if 1<= dep <= 22: 
                departamento = departamentos[dep-1]
                break 
            else: 
                print("Lo siento, no esta dentro del rango, vuelva a intentar")
        except ValueError:
            print("No se permiten caracteres, vuelva a intentar")
        except:
            print("Algo salio mal, vuelva a intentar")

    nuevo_nene = Niños(nombre=nombre, edad=edad, peso=peso, talla=talla, perimetro_craneal=pcraneal, departamento=departamento)

#---------------------------------------------------PONER EN PANTALLA---------------------------------------------------------------

#BAJO=0  DENTRO=1  SOBRE=2
#SIRVE PARA ALMACENAR CUANTOS NIÑOS EXISTEN EN CADA UNA DE LOS IDENTIFICADORES EN SUS RESPECTIVAS CATEGORIAS
nac_peso = [[],[],[]]
nac_talla = [[],[],[]]
nac_craneo = [[],[],[]]

#LO MISMO PERO DIFERENTE
pdep_peso = {}
pdep_talla = {}
pdep_craneo = {}

def rangos(niño, var, OMS_RANGO, nac_mat, dep_dic,prom):
    #AGREGA TODOS LOS DEPARTAMENTOS A CADA DICCIONARIO COMO KEY
    dep_dic.setdefault(niño.departamento, [[],[],[]])
    
    if niño.edad in OMS_RANGO: #SE BUSCA LA EDAD DEL NIÑO EN LOS RANGOS DE LA OMS
        ran_min, ran_max = OMS_RANGO[niño.edad]
        if var <= ran_min: 
            #niño.prom_peso = "Bajo"
            setattr(niño, prom, 'Bajo')
            nac_mat[0].append(niño) #AÑADE A LISTA GENERAL
            dep_dic[niño.departamento][0].append(niño)
        elif var > ran_max: 
            #niño.prom_peso = "Sobre"
            setattr(niño, prom, 'Sobre')
            
            nac_mat[2].append(niño)
            dep_dic[niño.departamento][2].append(niño)
        else: 
            #niño.prom_peso = "Dentro"
            setattr(niño, prom, 'Dentro')
            nac_mat[1].append(niño)
            dep_dic[niño.departamento][1].append(niño)


for niño in niños_grupo: #COMPARACION CON RANGOS DE LA OMS SEGUN LA EDAD
    rangos(niño, var=niño.peso, OMS_RANGO=OMS_peso, nac_mat=nac_peso, dep_dic=pdep_peso, prom='prom_peso')
    rangos(niño, var=niño.talla, OMS_RANGO=OMS_long, nac_mat=nac_talla, dep_dic=pdep_talla, prom='prom_talla')
    rangos(niño, var=niño.perimetro_craneal, OMS_RANGO=OMS_percad, nac_mat=nac_craneo, dep_dic=pdep_craneo, prom='prom_pcran')
    
#SIRVEN PARA GUARDAR EL PORCENTAJE DE CADA UNO DE LOS ELEMENTOS DE LAS MATRICES del tipo NAC (nacional), el ultimo elemento es el promedio com tal
pnac_peso = (len(nac_peso[0])/len(niños_grupo),len(nac_peso[1])/len(niños_grupo),len(nac_peso[2])/len(niños_grupo), sum(i.peso for i in niños_grupo)/len(niños_grupo))
pnac_talla = (len(nac_talla[0])/len(niños_grupo),len(nac_talla[1])/len(niños_grupo),len(nac_talla[2])/len(niños_grupo),sum(i.talla for i in niños_grupo)/len(niños_grupo))
pnac_craneo = (len(nac_craneo[0])/len(niños_grupo),len(nac_craneo[1])/len(niños_grupo),len(nac_craneo[2])/len(niños_grupo),sum(i.perimetro_craneal for i in niños_grupo)/len(niños_grupo))

#ENTRADA DE NIÑOS
print("\n"+"-"*15+"Entrada de niños"+"-"*15)
print(f"{'Niño':<10}{'Nombre':<30}{'Edad':<15}{'Peso':<10}{'Talla':<10}{'Craneo':<10}{'Departamento':<20}{'Peso':<10}{'Talla':<10}{'Craneo':<10}")
for nin in enumerate(niños_grupo,1):
    niño = nin[1]
    print(f"{nin[0]:<10}{niño.nombre:<30}{str(niño.edad)+" meses":<15}{str(niño.peso)+" kg":<10}{str(niño.talla)+" cm":<10}{str(niño.perimetro_craneal)+" cm":<10}{niño.departamento:<20}{niño.prom_peso:<10}{niño.prom_talla:<10}{niño.prom_pcran:<10}")


#DEPARTAMENTOS
def tabla_departamentos(deps,dic, nam):
    total = len(dic[deps][0])+len(dic[deps][1])+len(dic[deps][2])
    per = [round(len(dic[deps][0])/total*100,2), round(len(dic[deps][1])/total*100,2),round(len(dic[deps][2])/total*100,2)]
    print(f"{deps:<20}{nam:<15}{str(per[0])+"%":<25}{str(per[1])+"%":<25}{str(per[2])+"%":<25}")
#Ya no se me ocurren nombres para las varibles x'd
print("\n"+"-"*15+"Departamentos"+"-"*15)
print(f"{'Departamento':<20}{'Indicador':<15}{'Bajo Promedio (%)':<25}{'Dentro Promedio (%)':<25}{'Sobre Promedio (%)':<25}")

for deps in pdep_peso: 
    tabla_departamentos(deps, pdep_peso, 'Peso')
    tabla_departamentos(deps, pdep_talla, 'Talla')
    tabla_departamentos(deps, pdep_craneo, 'Cráneo')
    print("-"*120)

#RESUMEN GENERAL
print("\n"+"-"*15+"Resumen general"+"-"*15)
print(f"{'Indicador':<20}{'Bajo Promedio (%)':<25}{'Dentro Promedio (%)':<25}{'Sobre Promedio (%)':<25}{'Promedio Nacional (%)':<25}")
print(f"{'Peso':<20}{str(round(pnac_peso[0]*100,2))+"%":<25}{str(round(pnac_peso[1]*100,2))+"%":<25}{str(round(pnac_peso[2]*100,2))+"%":<25}{str(round(pnac_peso[3],2))+"kg":<25}")
print(f"{'Talla':<20}{str(round(pnac_talla[0]*100,2))+"%":<25}{str(round(pnac_talla[1]*100,2))+"%":<25}{str(round(pnac_talla[2]*100,2))+"%":<25}{str(round(pnac_talla[3],2))+"cm":<25}")
print(f"{'Cráneo':<20}{str(round(pnac_craneo[0]*100,2))+"%":<25}{str(round(pnac_craneo[1]*100,2))+"%":<25}{str(round(pnac_craneo[2]*100,2))+"%":<25}{str(round(pnac_craneo[3],2))+"cm":<25}")

