#generales
def crea_matriz(matriz,tam_i,tam_j):
    for i in range(tam_i): 
        fila = []
        for j in range(tam_j):  
            valor = int(input(f"Ingrese valor para posición [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def ip_m(matriz):
    t = "\n"
    for k in matriz: t += str(k).replace(","," ")+"\n"
    return t

#----------------------------EJERCICIO 1----------------------------
def ejercicio_1():
    print("-"*10+"SUMA DE TODOS LOS VALORES"+"-"*10)
    m = [[1,2,3],
         [4,-5,6],
         [7,8,9]]
    sum = 0

    for i in m: 
        for j in i: sum += j
            
    print("Matriz M:" + ip_m(m)) 
    print(f"Suma de todos sus valores: {sum}")

#----------------------------EJERCICIO 2----------------------------
def ejercicio_2():
    print("-"*10+"SUMA DE MATRICES"+"-"*10)
    m = [[1,2],
         [3,4]]
    n = [[4,5],
         [6,7]]
    r = []

    print("Matriz M: " +ip_m(m))
    print("Matriz N: " +ip_m(n))

    for i in range(len(m)):
        l = []
        for j in range(len(n[0])):
            l.append(m[i][j]+n[i][j])
        r.append(l)

    print("Respuesta de la suma de matrices:")
    print("M + N= " + ip_m(r))

#----------------------------EJERCICIO 3----------------------------
def ejercicio_3():
    print("-"*10+"ESCALAR MATRICES"+"-"*10)
    m = [[1,2,3],
         [4,5,6]]
    print("Matriz M: " + ip_m(m))
    
    a = int(input("Ingresa un valor para escalar la matriz M: "))
    r = []
    
    for i in m: 
        fila = []
        for j in i:  
            j*=a
            fila.append(j)
        r.append(fila)
    print("\nMatriz escalada: ")
    print(f"{a}xM= " + ip_m(r))
    
#----------------------------EJERCICIO 4----------------------------
def ejercicio_4():
    print("-"*10+"TRANSPONER MATRICES"+"-"*10)
    m = []
    crea_matriz(m,3,3)
    mT = []
    
    print("Matriz M: " + ip_m(m))
    
    for i in range(3): mT.append([])
    for i in range(3):
        for j in range(3):
            mT[j].append(m[i][j])
    
    print("\nMatriz transpuesta:")
    print("M^T = " + ip_m(mT))
    
#----------------------------EJERCICIO 5----------------------------
def ejercicio_5():
    print("-"*10+"MULTIPLICACIÓN DE MATRICES"+"-"*10)
    m = [[11,3],
         [7,11]]
    n = [[8,0,1],
         [0,3,5]]
    
    print("Matriz M= " +ip_m(m))
    print("Matriz N= " +ip_m(n))
    
    r = []
    if len(m[-1]) == len(n):
        for i in range(len(m)): 
            r.append([])
            for sig in range(len(n[0])):
                s = 0
                for j in range(len(m[0])): s += m[i][j] * n[j][sig]
                r[i].append(s)
        
        print("Respuesta: ")
        print("M x N= " + ip_m(r))      
    else:
        print("No es posible la multiplicación")

ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()