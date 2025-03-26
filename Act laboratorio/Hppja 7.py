#Ejercicio 1
print("números impares del 0 al 10 usando for:")
for i in range(1,11):
    if i%2 != 0: print(f"-  {i}")

#Ejercicio 2
x = 1
print("números impares del 0 al 10 usando while:")
while x < 11:
    if x%2 != 0: print(f"-  {x}")
    x+=1
    
#Escenario 1
print("Estas en un bucle, no podras salir hasta ingresar la palabra secreta")
while True: 
    a = input("Ingrese palabra secreta: ").lower()
    
    if a == "chupacabras":
        print("¡Has dejado el bucle con éxito")
        break
    else:
        print("Sigue intentando!!")

#Escenario 2
user_word = input("Ingresa una palabra: ").upper()
vocales = ['A','E','I','O','U']

for i in user_word:
    if i not in vocales:
        print(i)