#EJERCICIO 1
def text_num(numero: str):
    try:
        return int(numero)
    except:
        print("La entrada no es numerica")

#EJERCICIO 2
def abre(path: str):
    fichero = open(path)
    try:
        print(fichero.readline())
    except:
        print("El archivo no existe")
        fichero.close()

#EJERCICIO 3
while True:
    try:
        a = int(input("Ingresa un número: "))
        b = int(input("Ingresa otro número: "))
        break
    except:
        print('VUELVA A INTENTARLO')
        
while True:
    print("\nIngrese una operación: ")
    print("1)\tSuma\n2)\tResta\n3)\tMultiplicación\n4)\tDivision")
    
    try:
        op = int(input("Opcion: "))
        if 0 < op < 5: break
        else: print("Ingresa una opción valida")
    except:
        print("Ingrese una opcion valida")

if op == 1: print(f"La suma de {a} y {b} es: {a+b}" )
elif op == 2: print(f"La resta de {a} y {b} es: {a-b}" )
elif op == 3: print(f"La multiplicacion de {a} y {b} es: {a*b}" )
elif op == 4: 
    try:
        print(f"La division de {a} y {b} es: {a/b}" )
    except:
        print("La division por 0 no es valida")
        

#EJERCICIO 4
def lista_acceder(lista: list):
    while True:
        try:
            ind = int(input(f"Ingresa un index para la lista {lista}"))
            print(lista.index(ind))
            break
        except:
            print("Parece que algo salio mal, intnta de nyuevo")
        
    
#EJERCICIO 5
try:
    edad = int(input("Ingresa edad: "))
    print(f"Tu edad es de {edad}")
except:
    print("Edad no validad")