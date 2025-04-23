import time
#Ejercicio 1
def es_par_o_impar(n):
    if n%2 == 0: print(f"{n} Es par")
    else: print(f"{n} No es par")

#Ejercicio 2
def sum_list(lista):
    res = 0
    for i in lista: res +=i
    return res

#Ejercicio 3
def cuenta_regresiva(n):
    if n < 0: print("Despegue!")
    else:
        print(n)
        cuenta_regresiva(n-1)
        
#Ejercicio 4
def cuenta_ascendente(n):
    a = n-1
    if a == 0: print(n)
    else:
        print(n)
        cuenta_ascendente(a)

#Ejercios 5
a = 0
def suma_hasta(n):
    a += n
    if n < 0: print(a)
    else:
        cuenta_regresiva(n-1)

#Ejercicio 6
def factorial(num):
    if num == 1: return 1
    else: return num * factorial(num-1)

#Ejercicio 7
def minimo(l):
    if len(l) < 2:
        print(l[0])
    else:
        if l[0] > l[1]: l.pop(0)
        else: l.pop(1)
        minimo(l)
        
minimo([5,3,8,2])


#Juego
def adivina_el_numero(numero, intentos, tiempo_inico):
    if intentos == 0: print("")
    else:
        a =int(input("Ingresa un número a adivinar: "))
        if a == numero: 
            intentos =0
            print("Felicidades, ganaste")
        else:
            print("Vuelve a intentarlo")
            if intentos == 0: print("Lo siento, vuelve a intntarlo")
            adivina_el_numero(numero_secreto, intentos-1, tiempo_inicio)
            print(tiempo_inicio)
        
    
numero_secreto = 80
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")
tiempo_inicio = time.time() # Marca el inicio del tiempo
adivina_el_numero(numero_secreto, 5, tiempo_inicio)
