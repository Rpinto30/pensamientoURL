a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# posibles sin repetir: a+b, a+c, b+c [3!! tres doble factorial]

if c < a and c < b:
    print(a,b, "suma: " + str(a+b))
elif b < a and b < c:
    print(a,c, "suma: " + str(a+c))
elif a < b and a < c:
    print(b,c, "suma: " + str(b+c))
    