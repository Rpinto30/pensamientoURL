num = int(input("Ingrese un número de 5 dígitos: \n"))

if num >= 10000 and num <= 99999:
    
    d1 = num//10**4
    d2 = (num%10**4)//10**3
    d3 = (num%10**3)//10**2
    d4 = (num%10**2)//10
    d5 = num%10

    # Comparación y ordenación de mayor a menor
    if d1 < d2:
        d1, d2 = d2, d1
    if d1 < d3:
        d1, d3 = d3, d1
    if d1 < d4:
        d1, d4 = d4, d1
    if d1 < d5:
        d1, d5 = d5, d1

    if d2 < d3:
        d2, d3 = d3, d2
    if d2 < d4:
        d2, d4 = d4, d2
    if d2 < d5:
        d2, d5 = d5, d2

    if d3 < d4:
        d3, d4 = d4, d3
    if d3 < d5:
        d3, d5 = d5, d3

    if d4 < d5:
        d4, d5 = d5, d4

    # Resultado final del número ordenado
    numero_mayor_ordenado = d1 * 10**4 + d2 * 10**3 + d3 * 10**2 + d4 * 10 + d5
    numero_menor_ordenado = d5 * 10**4 + d4 * 10**3 + d3 * 10**2 + d2 * 10 + d1
    print("Número ordenado descendente")
    print(numero_mayor_ordenado)
    print("Número ordenado ascendente") 
    print(numero_menor_ordenado)
elif num < 10000:
    print("Número menor a 5 dígitos, no valido")
elif num > 99999:
    print("Número mayor a 5 dígitos, no valido")
else:
    print("Entrada invalida")