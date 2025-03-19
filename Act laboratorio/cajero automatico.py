saldo = 3000
intento = 3

while intento > 0:
    print("------------------------------------------------------------")
    print(f"Tu saldo actual es de: {saldo}")
    ret = int(input("Ingrese monto a retirar: ")) 
    result = saldo - ret #Saldo final
    if result >= 0: 
        saldo = result #Se actualiza el saldo
        if saldo <= 0: break
        else: 
            print(f"Retiro exitoso, tu saldo actual es de: {saldo}")
            intento -= 1 
            print(f"Número de intentos restantes: {intento}")
    else: print("Saldo insuficiente, porfavor intente de nuevo")


print(f"Retiro exitoso, saldo agotado, adios.")
