import time
#Ejercicio 1
def es_par_o_impar(n):
    if n%2 == 0: print(f"{n} Es par")
    else: print(f"{n} No es par")

#Ejercicio 2
def sum_list(lista):
    if len(lista) > 1: 
        lista[-2] = lista[-2] + lista[-1]
        sum_list(lista[:-1])
    else: print(lista[0])

#Ejercicio 3
def cuenta_regresiva(n):
    if n < 0: print("Despegue!")
    else:
        print(n)
        cuenta_regresiva(n-1)
        
#Ejercicio 4
def cuenta_ascendente(n,m=1):
    if m > n: return
    print(m)
    cuenta_ascendente(n,m+1)

#Ejercios 5
def sum_hasta(n,sum = 0):
    if n < 0: print(sum)
    else: sum_hasta(n-1,sum+n)

#Ejercicio 6
def factorial(num):
    if num == 1 or num==0: return 1
    elif num < 0: print("error")
    else: return num * factorial(num-1)

#Ejercicio 7
def minimo(l):
    if len(l) < 2:
        print(l[0])
    else:
        if l[0] > l[1]: l.pop(0)
        else: l.pop(1)
        minimo(l)
        

#Juego
def adivina_el_numero(numero, intentos, tiempo_inicio):
    n = 10
    while n > 0: 
        a = int(input("aa"))
        n-=a
        print(tiempo_inicio)
numero_secreto = 80
# Iniciar el juego con 5 intentos
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")
tiempo_inicio = time.time() # Marca el inicio del tiempo
adivina_el_numero(numero_secreto, 5, tiempo_inicio)