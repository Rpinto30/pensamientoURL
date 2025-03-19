fecha = 28022025
hora = 214712
seg = 172800

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
h_hora = hora//10**4
h_min = (hora%10**4)//100
h_seg = hora%100

#RESULTADO
resultado_hora = 0
resultado_fecha = 0

min = (h_seg + seg)//60
hora = ((h_min+min)//60)
d = hora//24

if h_hora + hora >= 24:     
    d+=1 
    if hora >= 48: hora = abs(hora -d*24)
    h_hora = ((h_hora+hora)%24)
    hora = 0

if (seg+h_seg >= 60): 
    resultado_hora += ((h_seg + seg)%60)
else:
    resultado_hora += h_seg + seg


if (h_min + min >= 60): resultado_hora += ((h_min+min)%60)*10**2
else:  resultado_hora += (h_min+min)*10**2

resultado_hora += (h_hora + hora)*10**4

print("Hora resultado:")
print(str(resultado_hora//10**4) + ":" + str((resultado_hora%10**4)//100) + ":" + str(resultado_hora%100))

#---------------------------------------FECHA---------------------------------------
if (mes <= 7 and mes%2 != 0) or (mes >= 8 and mes%2 == 0):
    #31 DÍAS
    if (dia + d > 31): 
        resultado_fecha += (((dia + d)%31))*10**6
        mes +=1
    else:
        resultado_fecha += (dia + d)*10**6
    
elif mes == 2:
    #FEBRERO
    if bisiesto == True:
        if (dia + d > 29): 
            resultado_fecha += (((dia + d)%29))*10**6
            mes +=1
        else:
            resultado_fecha += (dia + d)*10**6
    else:
        if (dia + d > 28): 
            resultado_fecha += (((dia + d)%28))*10**6
            mes +=1
        else:
            resultado_fecha += (dia + d)*10**6
else:
    #30 DÍAS
    if (dia + d > 30): 
        resultado_fecha += (((dia + d)%30))*10**6
        mes +=1
    else:
        resultado_fecha += (dia + d)*10**6

resultado_fecha += (dia + d)*10**6
resultado_fecha += mes*10**4 + año

print("Fecha resultado:")
print(str(resultado_fecha//10**6) + "/" + str((resultado_fecha%10**6)//10**4) + "/" + str(resultado_fecha%10**4))
