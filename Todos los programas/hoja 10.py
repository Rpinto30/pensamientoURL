#Ejercio 1
lim = int(input("Ingrese un número mayor que 1 para saber cuantos pares existe: "))
if lim >= 1:
    c = 1
    pares = 0
    while c <= lim:
        if c%2 == 0: pares +=1
        c+=1
    print(f"Cantidad de número pares entre 1 y {lim} es: \n{pares}")
else: print("entrada invalida")

#Ejerciio 2
n = int(input("Ingrese un número mayor que 1 para realizar la sumatoria: "))
if n >= 1:
    sum = 0
    i = 0
    while i <= n:
        sum += n
        i+=1
    print(f"La suma de 1 hasta {n} es de: \n{sum}")
else: print("entrada invalida")

#Ejercicio 3
n = int(input("Ingrese número para calcular su factorial: "))
c = 1
fac = 1
if n > 0:
    while c <= n:
        fac *= c
        c +=1
    if n== 0: fac = 1
    print(f"{n}! = {fac}")
else: print("entrada invalida")

#Ejercicio 4
n = 10
while True:
    print("-----------------------------------------")
    ad = int(input("¡Adivina el número del 1 al 100 que estoy pensando!: "))
    if 1 <= ad <= 100:
        if ad == n: 
            print("Felicidades!! Ese es el número correcto")
            break
        else: 
            if ad > n: print("El número que colocaste es mayor al que estoy pensando")
            else: print("El número que colocaste es menor al que estoy pensando")
            print("Vuelve a intentarlo!!!")
    else: print("Es entre 1 al 100!!! Vuelve a intentar")

# Ejercicio 5
contraseña = "contraseña"
intentos = 3
while intentos > 0:
    con = input("Para acceder, ingrese la contraseña: ")
    if con.lower() == contraseña.lower(): 
        print("Acceso permitido ¡Bienvenido!")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta, vuelva a intentarlo")
        print(f"Número de intentos: {intentos}")
    
    if intentos == 0: print("Intentos suficientes, cuenta bloquead")
    
# Ejercicio 6

while True:
    cont = input("Ingrese una contraseña: \n")
    if len(cont) < 8: 
        print("Contraseña muy corta, debe al menor colocar 8 caracteres")
        continue
    if cont.lower() == cont or cont.upper() == cont: 
        print("La contraseña debe tener mayusculas y minusculas")
        continue
    
    num = False
    i = 0
    while i < len(cont):
        if cont[i].isdigit():
            num = True
            break
        i += 1
    
    if num == False:
        print("La contraseña debe tener al menos un número")
        continue
    
    print("Contraseña aceptada")
    break

#Ejercicio 7
print("Solo pueden infectar las personas que estan completamente infectadas")
pob = int(input("Ingresa una población: \n"))
inf_ac = int(input("Ingresa cantidad de infectados actuales: \n"))
d = int(input("Ingresa cuantos dias quieres que pasen: \n"))
i = 1

while i < d+1:
    inf_ac += 1.5*int(inf_ac)
    if inf_ac >= pob:
        inf_ac = pob
        print("TODA LA POBLACIÓN ESTÁ INFECTADA")
        break
    print(f"Día: {i} | Infectados: {int(inf_ac)} personas")
    i+=1
print(f"La población total infectada es de: {int(inf_ac)} personas")