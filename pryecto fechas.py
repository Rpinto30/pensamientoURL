fecha = 28022025
hora = 00000
seg = 1568978
a = 0
#fecha = int(input("Ingrese una fecha en el formato dd/mm/aaaa:\n"))
#hora = int(input("Ingrese hora en el formato HH:MM:SS: \n"))
#seg = int(input("Ingrese cantidad de segundos que desea agregar: "))

#FECHA
dia = fecha//10**6
mes = (fecha%10**6)//10**4
año = fecha%10**4
bisiesto = False
if año%4 == 0: bisiesto = True

#HORA
h_hor = hora//10**4
h_min = (hora%10**4)//100
h_seg = hora%100

#RESULTADO
r_hora = 000000
r_fecha = 00000000
min = (h_seg + seg)//60

if (h_hor + (min//60) >= 24):
    hora = 0

if (seg+h_seg >= 60): 
    r_hora += ((h_seg + seg)%60)
else:
    r_hora += h_seg + seg


if (h_min + min >= 60): r_hora += ((h_min+min)%60)*10**2
else:  r_hora += (h_min+min)*10**2

r_hora += (h_hor + (min//60))*10**4


print("Hora resultado:")
print(r_hora)
print(str(r_hora//10**4) + ":" + str((r_hora%10**4)//100) + ":" + str(r_hora%100))

