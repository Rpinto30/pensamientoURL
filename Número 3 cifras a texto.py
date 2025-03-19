n = int(input("Ingresa un número de 3 cifras: \n"))

if 0 <= n <= 999:
    num = n%10
    num_dec = (n%100)//10 
    num_cent = n//100

    un = ["uno","dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    dec = ["deci", "veinti", "treita y ", "cuarenta y ", "cincuenta y ", "sesenta y ", "setenta y ", "ochenta y ", "noventa y "]
    cen = ["ciento ", "doscientos ", "tresientos ", "cuatrocientos ", "quinientos ", "seiscientos ", "setesientos ", "ochosientos ", "novecientos "]
    text = ""


    if num_dec <= 9 and n != 0: text = un[num-1]
    elif n == 0: text = "cero"

    if n == 10: text = "diez"
    elif n == 11: text = "once"
    elif n == 12: text = "doce"
    elif n == 13: text = "trece"
    elif n == 14: text = "catorce"
    elif n == 15: text = "quince"
    elif n == 20: text = "veinte"
    elif num == 0 and num_dec != 0: text = dec[num_dec-1].replace(" y","")
    elif (2 <= num_dec <= 9) and num != 0: text = dec[num_dec-1] + un[num-1]

    if n == 100: text = "cien"
    elif num_cent >= 1: text = cen[num_cent-1] + text

    print(f"Número en texto: \n{text}")
else: print("Entrada incorrecta")