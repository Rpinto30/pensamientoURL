n = int(input("Ingrese límite para saber los primos inferiores: "))

while n > 0:
    if n==2 or n== 3 or n==5 or n==7: print(n)
    elif n%2 and n%3 and n%5 and n%7 != 0 and n != 1: print(n)
    n-=1
    