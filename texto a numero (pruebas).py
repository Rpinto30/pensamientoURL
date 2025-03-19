text = input("Ingresa número de tres cifras en texto: \n").lower()
text = text.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
text = text.split()
unidad = text[len(text)-1]
num = 0

if "y" in text: del text[len(text)-2]
if "dieci" in text[len(text)-1]: 
    text[len(text)-1] = unidad[:5]
    text.append(unidad[5:])
elif "veinti" in text[len(text)-1]: 
    text[len(text)-1] = unidad[:6]
    text.append(unidad[6:])
    
unidad = text[len(text)-1]
decena, centena = "", ""
if len(text) > 1: decena = text[len(text)-2]
if len(text) > 2: centena = text[0]

u = ["cero","uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]

d_0 = ["diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
d_0_esp = ["dieci", "veinti"]
d_diez = ["once", "doce", "trece", "catorce", "quince"]

c = ["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

#Números del 0 al 9
if unidad in u: num = u.index(unidad)

#Números del 11 al 15
if unidad in d_diez: num = d_diez.index(unidad) + 11

#Números entre el 16 al 19 y entre el 21 al 29
if decena in d_0_esp: num += 10*(d_0_esp.index(decena)+1)

#Números del 10 hasta el 90 (en 10 en 10)
if decena in d_0: num += 10*(d_0.index(decena)+1)
elif unidad in d_0: num += 10*(d_0.index(unidad)+1)

#Números del 100 hasta el 909 (en 100 en 100)
if (centena in c): num += 100*(c.index(centena)+1)
elif (decena in c): num += 100*(c.index(decena)+1)
if (unidad in c):
    print(c.index(unidad))
    if c.index(unidad) != 0: num += 100*(c.index(unidad)+1)
elif unidad == "cien": num =100

if num == 0 and unidad != "cero": print(f"Error, se desconoce al número {" ".join(text)}")
else: print(num)
print(f"centena: {centena}, decena: {decena}, unidad: {unidad}")