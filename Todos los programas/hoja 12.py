#EJERCICIO 1
'''
var
    Entero: I, J
    Array[1..10] de entero: A
inicio
I ← 1
J ← 2
A[I] ← J   #A[1] = 2
A[J] ← I    #A[2] = 1
A[J+I] ← I+ J   #A[3] = 3
I ← A[I] + A[J]    #I = 2+1 = 3
A[3] ← 5    #A[3] = 5
J ← A[I]- A[J]      #J = 5-1=4
Fin

Respuesta:
I = 3
J = 4

A = [1,2,1,5,5,6,7,8,9,10]
'''

#EJERCICIO 2
'''
var
 entero: X, Y
 array[1..4] de entero: M
inicio
 X ← 1
 Y ← 2
 M[X] ← Y   #M[1] = 2
 M[Y] ← X + 1   #M[2] = 1+1=2
 M[3] ← M[1] + M[2]     #M[3] = 2+2=4
 X ← M[3] - Y   #X = 4-2=2
 Y ← M[X] * 2   #Y = 2*2 = 4
 M[3] ← Y   M[3] = 4
fin

Respuestas:
X=2
Y=4

M = [1,2,2,4]
'''

#EJERCICIO 3
while True:
    try:
        m = []
        for i in range(3):
            f = []
            for j in range(3):
                v = int(input(f"Ingresa un número para col: {j} y fila {i}: "))
                f.append(v)
            m.append(f)

        sum_col = []
        sum_fila = []

        for fil in range(3):
            sl, sc = 0, 0
            for col in range(3): 
                sc += m[col][fil]
                sl += m[fil][col]
            sum_fila.append(sl)
            sum_col.append(sc)

        for i in m : print(i)
        print(f"\nSuma de sus filas: {sum_fila}")
        print(f"Suma de sus columnas: {sum_col}")
        break
    except ValueError:
        print("Ingreso no numerico, intente de nuevo")
    except IndexError:
        print("Fila con cantidad e elementos incorrectos")
    except:
        print("No sé, pero algo salio mal")


#EJERCICIO 4
try:
    T = [1,2,3,4,5,
        6,7,8,9,10,
        11,12,13,14,15,
        16,17,18,19,20,
        21,22,23,24,25]

    T_divK = []
    #0,24
    k = 25
    for i in range(25): T_divK.append(T[i]/T[k])

    for i in range(5): print(T[i*5:(i+1)*5])
    print(f"\nTabla T dividida por T[K] con K={k} y T[k]={T[k]}")
    for i in range(5): print(T_divK[i*5:(i+1)*5])
except IndexError:
    print(f"Lo siento, no se encontró un valor k={k} para T[{k}]")
except ZeroDivisionError:
    print(f"Lo siento, Pero el valor T[{k}] es iugal a 0, no se puede reaizar la opearción")
except:
        print("No sé, pero algo salio mal")
