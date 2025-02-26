n = int(input("Número de 4 digitos"))

d2 = n//10**2
d1 = d2//10
d2 %= 10

d3 = n%10**2
d4 = d3%10
d3 = d3//10

if n//10**4 == 0:
    if d1%2 == 0 and d2%2 == 0 and d3%2 == 0 and d4%2 == 0:
        print("Todos sus digitos son numero par")
    if (d1+d2+d3+d4) > 20:
        print("La suma de sus digitos es mayor a 20")
else:
    print("Error, lo ingresado no es un numero de 4 digitos")