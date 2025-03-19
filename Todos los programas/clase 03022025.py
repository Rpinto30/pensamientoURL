from math import *
import pygame as py

print("Selecciona valor de a")
a = float(input())
print("Selecciona valor de b")
b = float(input())
print("Selecciona valor de c")
c = float(input())
x1 = 0
x2 = 0


d = (b*b) - (4*a*c)

if d == 0:
    x1 = (-b)/(2*a)
    print("X1 =", x1)
    print("x2 = no pertenece a los reales")
    
else:
    if d > 0:
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        
        print("X1 =", x1)
        print("X2 =", x2)
    elif d < 0:
        print("x1 y x2 no pertenecen a los reales")
