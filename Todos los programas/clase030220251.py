import math
from sympy import integrate, init_printing
from sympy.abc import x
m = 1
s = 0
n = float(input("Ingrese n: "))

if n - int(n) == 0:
    pass
else:
    n = integrate(pow(x,n)*pow(math.exp(1),-x), (x, 0, 10))
    print(n)