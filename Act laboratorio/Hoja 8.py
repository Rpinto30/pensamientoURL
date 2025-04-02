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
atencion = {1:"malo", 2:"regular", 3:"buena",4:"muy buena", 5:"excelente"}
resultados = [0,0,0,0,0]


while n > 0:
    calificacion = int(input("Como calificaria nuestro servicio?" +
                            "\n 5. Excelente" + 
                            "\n 4. Muy buena" +
                            "\n 3. Buena" +
                            "\n 2. Regular" +
                            "\n 1. Malo" +
                            "\nCalificación: "))
    
    if calificacion < 1 or calificacion > 5: print("Error, vuelva a intentarlo")
    else: 
        if calificacion == 1: resultados[0] +=1
        elif calificacion == 2: resultados [1] += 1
        elif calificacion == 3: resultados[2] +=1
        elif calificacion == 4: resultados[3] +=1
        elif calificacion == 5: resultados[4] += 1
        n -= 1

a = resultados[0]
z = 0
mayor = 0
for i in resultados:
    if resultados.index(i) > 1:
        print(a, (resultados[resultados.index(i)] -1))
        if a > i:
            mayor = z
        if a < i: 
            menor = z
    a = resultados[resultados.index(i)]
    z += 1
print("----------------Resultados-------------")
print(f"Excelente: {resultados[4]}\n"+ 
      f"Muy buena: {resultados[3]}\n"+ 
      f"Buena: {resultados[2]}\n"+
      f"Regular: {resultados[1]}\n"+
      f"Mala: {resultados[0]}\n")

print(f"Respuesta mayor: {mayor}")
print(f"Respuesta menor: {menor}")