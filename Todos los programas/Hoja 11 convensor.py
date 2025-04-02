digits_hex = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
hex_l = "0123456789ABCDEF"
cont = 1

#Bucle Programa en general
while True:
    #Declaración inicial de todas las variables
    dec ,bin, oct, hex = 0,0,0, ""
    opcion, i = 0, 0
    print("-"*10 + "Conversor de sistemas númericos" + "-"*10)
    print("1. Convertir de Decimal a otro sistemas\n" + "2. Convertir de Binario a otro sistemas\n" + "3. Convertir de Octal a otro sistemas\n" + "4. Convertir de Hexadecimal a otro sistemas\n" + "5. Salir\n")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1: #PARA SISTEMA DECIMAL
        #BUCLE PARA TOMAR NUMERO DECIMAL
        while True:
            dec = int(input("Ingrese número Decimal: "))
            if dec > 0:
                save_dec = dec
                #BINARIO
                while dec >= 1:
                    bin += (dec%2)*10**i
                    dec //= 2
                    i +=1
                dec = save_dec
                i = 0
                #OCTAL
                while dec >= 1:
                    oct += (dec%8)*10**i
                    dec //= 8
                    i +=1
                dec = save_dec
                i = 0
                #HEXADECIMAL
                if dec == 0: hex= "0"
                while dec > 0:
                    res = dec % 16
                    hex = hex_l[res] + hex
                    dec //= 16
                print("----------Resultados----------")
                print(f"-Número en Binario: {bin}")
                print(f"-Número en Octal: {oct}")
                print(f"-Número en Hexadecimal: {hex}")
                print("-"*30)
                break
            else: print("Entrada invalida, vuelve a intentar\n")
    elif opcion == 2: #PARA SISTEMA BINARIO
        #BUCLE PARA TOMAR NUMERO BINARIO
        while True:
            bin = int(input("Ingrese número binario: "))
            for a in str(bin):
                if a != '1' and a != '0':
                    print("Entrada invalida, vuelve a intentar\n")
                    break
            else:
                #Decimal
                for a in str(bin)[::-1]:
                    dec += int(a)*(2**(i))
                    i+=1
                i = 0
                save_dec = dec
                #OCTAL
                while save_dec >= 1:
                    oct += (save_dec%8)*10**i
                    save_dec //= 8
                    i +=1
                i = 0
                save_dec = dec
                #HEXADECIMAL
                if save_dec == 0: hex= "0"
                while save_dec > 0:
                    res = save_dec % 16
                    hex = hex_l[res] + hex
                    save_dec //= 16
                print("----------Resultados----------")
                print(f"-Número en Decimal: {dec}")
                print(f"-Número en Octal: {oct}")
                print(f"-Número en Hexadecimal: {hex}")
                print("-"*30)
                break
    elif opcion == 3: #NUMERO OCTAL
        #BUCLE PARA TOMAR NUMERO OCTAL
        while True:
            oct = int(input("Ingrese número octal: "))
            for a in str(oct):
                if int(a) > 7 or int(a) < 0:
                    print("Entrada invalida, vuelve a intentar\n")
                    break
            else:
                #DECIMAL
                for a in str(oct)[::-1]:
                    dec += int(a)*(8**(i))
                    i+=1
                i = 0
                save_dec = dec
                #BINARIO
                while save_dec >= 1:
                    bin += (save_dec%2)*10**i
                    save_dec //= 2
                    i +=1
                save_dec = dec
                i = 0
                #HEXADECIMAL
                if save_dec == 0: hex= "0"
                while save_dec > 0:
                    res = save_dec % 16
                    hex = hex_l[res] + hex
                    save_dec //= 16
                print("----------Resultados----------")
                print(f"-Número en Decimal: {dec}")
                print(f"-Número en Binario: {bin}")
                print(f"-Número en Hexadecimal: {hex}")
                print("-"*30)
                break
    elif opcion == 4: #NUMERO HEXADECIMAL
        #BUCLE PARA TOMAR NUMERO HEXADECIMAL
        while True:
            hex = input("Ingrese número hexadecimal: ")
            for a in hex:
                if a not in hex_l:
                    print("Entrada invalida, vuelve a intentar\n")
                    break
            else:
                #DECIMAL
                for a in str(hex)[::-1]:
                    if a.isdigit(): dec += int(a)*(16**(i))
                    else: dec += digits_hex[a]*(16**(i))
                    i+=1
                i = 0
                save_dec = dec
                #BINARIO
                while save_dec >= 1:
                    bin += (save_dec%2)*10**i
                    save_dec //= 2
                    i +=1
                save_dec = dec
                i = 0
                #OCTAL
                while save_dec >= 1:
                    oct += (save_dec%8)*10**i
                    save_dec //= 8
                    i +=1
                print("----------Resultados----------")
                print(f"-Número en Decimal: {dec}")
                print(f"-Número en Binario: {bin}")
                print(f"-Número en Octal: {oct}")
                print("-"*30)
                break
    elif opcion == 5: break
    else:
        print("Entrada no valida, vuelva a intentar")
        continue
    
    print("\nDesea continuar? \n" + "   sí = 1 \n" +"   no = 2")
    cont = int(input("Seleccione una opción: "))
    if cont == 1: continue 
    else: break
print("-"*10 +"¡¡¡Hasta pronto!!!"+ "-"*10)