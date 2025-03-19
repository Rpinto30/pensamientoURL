n = int(input("Ingrese un numero de tres digitos"))

if n//10**3 == 0:
    if n//10**2 == n%10:
        print("Es capicua")
    else:
        print("No es capicua")
else:
    print("No es un número de 3 cifras")