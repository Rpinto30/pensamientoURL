n = int(input("Ingrese numero:"))

print(n)

if len(str(n))%2 != 0:
    a = (len(str(n)) -1)/2
    b = n//(10**int(a +1))
    c = n%(10**int(a))
    
    n = str(b) + str(c)

if int(n)%11 == 0:
    print("Es capicua")
else:
    print("No es capicua")