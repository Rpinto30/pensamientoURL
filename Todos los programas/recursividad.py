a = int(input("Numero we: "))
def factorial(num):
    if num == 1: return 1
    else: return num * factorial(num-1)
print(factorial(a))

def fibo(num):
    if num == 0: return 0
    elif num == 1 or num == 2: return 1
    else: return  fibo(num-2) + fibo(num-1)
    
for i in range(a):
    print(fibo(i))