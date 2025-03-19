lista = [10,9,8]
lista.sort()

def consecutivos():
    if lista[1] == (lista[2]-1) and lista[0] == (lista[2]-2): print("consecutivos")
    else: print("No lo son")

#consecutivos()

def mayor(li = []):
    i = 0
    l = li.copy()
    for n in li:
        while i < len(li) -1:
            if li[i] > li[i+1]: 
                li[i] = l[i+1]
                li[i+1] = l[i]
                l = li.copy()
            i+=1
        i = 0

    print(li[0], "menor")
    print(li[len(li) -1], "mayor")
    
    
mayor([1, 516,15,26])


def suma(a,b, c):
    if a == (b+c):
        print(a, " Es suma de", b, c)
    elif b == (a+c):
        print(b, " Es suma de", a, c)
    elif c == (a+b):
        print(c, " Es suma de", a, c)
    else: print("ninguno es suma del otro")    
    

suma(1,2,5)