#-----------------------------Ejercicio 1-----------------------------
print("-----------------------------Ejercicio 1-----------------------------")
contraseña = contraseña = input("Ingrese contraseña: \n")
c = ["@", "#", "$" , "%", "&", "*", "!"]
a = contraseña.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
#Fuerte
if len(contraseña) >= 8 and contraseña.lower() != contraseña and contraseña != a and (c[0] in contraseña or c[1] in contraseña or c[2] in contraseña or c[3] in contraseña or c[4] in contraseña or c[5] in contraseña or c[6] in contraseña):
    print("Contraseña fuerte")
elif len(contraseña) >= 6 and contraseña != a:
    print("Contraseña moderada")
else:
    print("Contraseña debil")

#-----------------------------Ejercicio 2-----------------------------
print("-----------------------------Ejercicio 1-----------------------------")
num = int(input("Ingrese número del 1 al 99: \n"))

if 1 <= num <= 99:
    un = num%10
    dec = num//10
    a = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    b = ["Dieci", "Veinti", "Treinta y ", "Cuarenta y ", "Cincuenta y ", "Sesenta y",  "Setenta y", "Ochenta y ", "Noventa y "]
    c = ["Diez", "Veinte", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"]
    text = ""
    
    if num < 10:
        text = a[num-1]
    elif 10 <= num < 20:
        if num == 10: text = c[0]
        elif num == 11: text = "Once"
        elif num == 12: text = "Doce"
        elif num == 13: text = "Trece"
        elif num == 14: text = "Catorce"       
        elif num == 15: text = "Quince" 
        text = b[0] + a[un-1]  
    else:
        if un == 0: text = c[dec-1]
        else: text = b[dec-1] + a[un-1] 
    print(text)
else:
    print("Entrada incorrecta")
    
#-----------------------------Ejercicio 3-----------------------------
print("-----------------------------Ejercicio 3-----------------------------")
mess = input("Ingresa un mensaje cifrado: \n")

mess = mess.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u")
print("Mensaje descifrado: "+mess)

#-----------------------------Ejercicio 4-----------------------------
print("-----------------------------Ejercicio 4-----------------------------")
placa = input("Ingrese un número de placa: \n")

if len(placa) >= 6:
    numeros = placa[3] + placa[4] + placa[5]
    mayusc = placa[0] + placa[1] + placa[2]
    
    if mayusc.upper() == mayusc and numeros.isdigit() == True:
        print(f"placa: {placa} es valida")
    else: print("Placa invalida")
else: print("Placa invalida")
    