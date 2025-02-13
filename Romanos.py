print("--------------------Convertidor a números Romanos--------------------")
entrada = int(input("Ingrese un número del 1 al 9:\n"))
resultado = ""

if entrada <= 9 and entrada >= 1:
    if entrada <=3: resultado = entrada*"I"
    elif entrada == 4: resultado = "IV"
    elif entrada >= 5 and entrada <= 8: resultado = "V" + "I"*(entrada-5) 
    elif entrada == 9: resultado = "IX"
    
    print("El número " + str(entrada) + " en Romanos es: " + resultado)
else:
    print("Entrada invalida")