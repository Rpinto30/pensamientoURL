opcion = '''
    print("1:conversor de temperatura")
    print("2:conversor de moneda")
    print("3:calcular factorial")
'''

print("HOLA!! ¿Qué es lo que deseas?")
print("   Conversor de temperatura=1\n   Conversor de moneda=2\n   Calcular factorial=3")
opcion = int(input("Seleccione una opción:" ))



if opcion == 1:
    print("¿Qué desea convertir?")
    tem_opc = int(input("   Celsius a Fahrenheit=1\n   Celsius a Kelvin=2 \n   Fahrenheit a Celsius=3 \n   Fahrenheit a Kelvin=4 \n   Kelvin a Celsius=5 \n   Kelvin a Fahrenheit=6 \n Opción:"))
    temp = float(input("Ingrese cantidad: "))
    i_temp = temp
    if tem_opc == 1:
        temp = ((9/5) * temp)+32
        print("°C" + str(i_temp) + "son: " + "°F" + str(temp))
    elif tem_opc == 2:
        temp = temp + 273.15
        print("°C" + str(i_temp) + "son: " + "K" + str(temp))
    elif tem_opc == 3:
        temp = (5/9)*(temp-32)
        print("°F" + str(i_temp) + "son: " + "°C" + str(temp)) 
    elif tem_opc == 4:
        temp = [(5/9)*(temp-32)]+273.15
        print("°F" + str(i_temp) + "son: " + "K" + str(temp))
    elif tem_opc == 5:
        temp= temp -273.15
        print("K" + str(i_temp) + "son: " + "°C" + str(temp))
    elif tem_opc == 6:
        temp = 1.8*(temp-273.15) + 32
        print("K" + str(i_temp) + "son: " + "°F" + str(temp))
    else: print("Opción invalida, hasta luego") 
elif opcion == 2:
    print("¿Qué deseas convertir?")
    mod_opc = int(input("   Quetzal a Dolar=1\n   Quetzal a Peso Mx=2\n Opción: "))
    mod = float(input("Ingrese cantidad: "))
    quetzal = mod
    
    if mod_opc == 1:  
        mod *= 2.66
        print("Q" + str(quetzal) + " son: " + "$"+ str(mod))
    elif mod_opc == 2:
        mod *= 0.13
        print("Q" + str(quetzal) + " son: " +  str(mod) + " Pesos mx")
    else: print("Opción invalida, hasta luego")
elif opcion == 3:
    fac_opc = int(input("Ingrese un valor n (Unicamente numeros enteros): "))
    n = 1
    i = 1
    
    while i <= fac_opc:
        n*= i
        i+=1
    print("El factorial de " + str(fac_opc) + " es: ",n)
    
else: print("Hasta luego")
