dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']

n_azucar =[130,160,95,175,160]
n_sal = [2000,2400,1800,2400,2700]
presion = [115,130,110,125,175]

#AZUCAR = 0  SAL = 1 PRESION = 2
prom = [0,0,0]

control = [[],[],[]]

for d in range(len(n_azucar)-1):
    if 70 < n_azucar[d] <= 140: control[0].append('Saludable') 
    else: control[0].append('Bajo el rango')
    
    if n_sal[d] <= 2300: control[1].append('Saludable')
    else: control[1].append('Bajo el rango')
    
    if 80 < presion[d] < 120: control[2].append('Normal') 
    elif 120 <= presion[d] <= 129 or presion[d] < 80: control[2].append('Elevada')
    elif 130 < presion[d] <= 139 or 80 <presion[d] < 89: control[2].append('Hipertension etapa 1')
    elif presion[d] >= 140 or presion[d] >= 90: control[2].append('Hipertension etapa 2')
    else: control[2].append('Bajo el rango')

    prom[0] += n_azucar[d]
    prom[1] += n_sal[d]
    prom[2] += presion[d]
    
prom[0] /= len(dias)
prom[1] /= len(dias)
prom[2] /= len(dias)

print("\n"+"-"*30+"Resultadoss"+"-"*30)
print(f"{'Dia':<20}{'Niveles de azucar':<25}{'Niveles de sal':<25}{'Niveles de presion':<25}{'Promedio':<25}")

for i in range(len(n_azucar)-1):
    print(f"{str(dias[i]):<20}{str(control[0][d]):<25}{str(control[1][d]):<25}{str(control[2][d]):<25}{str(prom[i]):<25}")
