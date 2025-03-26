n = int(input("Escoger n: "))
m = int(input("Escoger extremo: "))
i = 0

for i in range(n,m+1):
    print(f"{i}x{n} = {i*n}")

i = 0
sum_p = 0
sum_n= 0
a_1 = 0
a_2 = 0
for i in range(10):
    n = int(input(f"Ingresa número {i+1}: "))
    
    if n > 0: 
        a_1 += 1
        sum_p += n
    else: 
        a_2 += 1
        sum_n += n

print(f"Media de los positivos: {sum_p/a_1}")
print(f"Media de los negativos: {sum_n/a_2}")
