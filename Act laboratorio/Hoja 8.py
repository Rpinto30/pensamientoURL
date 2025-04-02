#EJERCICIO 1
'''
tamaño = int(input("Ingrese tamaño de arreglo: "))
base = int(input("Ingrese una base: "))
arreglo = []

for i in range(tamaño):
    arreglo.append(base*(i+1))
print(f"El arreglo es: {arreglo}")

#EJERCICIO 2
tamaño = int(input("Ingrese tamaño de arreglo: "))
nombres = []
longitud = []

for i in range(tamaño):
    nombre = input(f"Ingrese nombre no.{i+1}: ")
    nombres.append(nombre)
    longitud.append(len(nombre))
    
print(f"Los nombres son: {nombres}")
print(f"Su longitud de caracteres es: {longitud}")
'''
#ESCENARIO 1
n = int(input("Cantidad de clientes: "))
a = n
respuestas = []

while n > 0:
    evaluacion = int(input(f"Cliente no. {n+1} está satisfecho con nuestro servicio?: "))
    if evaluacion >= 1 and evaluacion <= 5:
        respuestas.append(evaluacion)
        n -=1
    else:
        print("Error, debe de ser en una escala del 1 al 5")
        print("----------------------------------")
    
resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for r in respuestas:
    resultados[r] +=1

print("\n----------------Resultados--------------")
for calificacion, total in resultados.items():
        print(f"{calificacion}: {total}")
frec = 1
ma_frec = resultados[1]
    
for calificacion in range(2, 6): 
    if resultados[calificacion] > ma_frec:
        frec = calificacion
        ma_frec = resultados[calificacion]
print(f"\nLa respuesta más frecuente es: {ma_frec}")
prom = sum(respuestas)/a
print(f"\nPromedio de respuestas: {prom}")
baj_prom = [i+1 for i, respuesta in enumerate(respuestas) if respuesta < prom]
    
if baj_prom: print(f"Los clientes que respondieron con valores menores al promedio son: {baj_prom}")
else: print("Ningún cliente respondió con un valor menor al promedio.")


