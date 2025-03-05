fecha = int(input("Ingrese una fecha en el formato dd/mm/aaaa:\n"))
hora = int(input("Ingrese hora en el formato HH:MM:SS: \n"))
seg = int(input("Ingrese cantidad de segundos que desea agregar: \n"))

#FECHA
dia = fecha//10**6
mes = (fecha%10**6)//10**4
año = fecha%10**4
bisiesto = False

#HORA
h_hora = hora//10**4
h_min = (hora%10**4)//100
h_seg = hora%100

#RESULTADO
resultado_hora = 0
resultado_fecha = 0

if año%4 == 0: bisiesto = True

if (0 <= hora <= 999999) and (0 <= h_hora <= 23) and (0 <= h_min < 60) and (0 <= h_seg < 60):
    if (999999 < fecha <= 99999999) and (1 <= dia <= 31) and (1 <= mes <= 12):
        print("-----------------Resultados--------------")
        #--------------------------------------------HORA--------------------------------------------
        min = (h_seg + seg)//60
        hora = (h_min+min)//60
        dia_sum = hora//24

        #Horas
        if h_hora + hora >= 24:     
            if hora >= 48: hora = abs(hora -dia_sum*24)
            h_hora = (h_hora+hora)%24
            hora = 0
            
            if h_hora + hora == 0: dia_sum +=1

        #Segundos
        if (seg+h_seg >= 60): 
            resultado_hora += ((h_seg + seg)%60)
        else:
            resultado_hora += h_seg + seg

        #Minutos
        if (h_min + min >= 60): resultado_hora += ((h_min+min)%60)*10**2
        else:  resultado_hora += (h_min+min)*10**2

        resultado_hora += (h_hora + hora)*10**4

        print("Hora resultado:")
        print(str(resultado_hora//10**4) + ":" + str((resultado_hora%10**4)//100) + ":" + str(resultado_hora%100))

        #------------------------------------------FECHA-------------------------------------------

        #Dias
        if (mes <= 7 and mes%2 != 0) or (mes >= 8 and mes%2 == 0):
            #31 DÍAS
            if (dia + dia_sum > 31): 
                dia = (dia + dia_sum)%31
                dia_sum = 0
                mes +=1
        elif mes == 2:
            #FEBRERO
            if bisiesto == True:
                if (dia + dia_sum > 29): 
                    dia = (dia + dia_sum)%29
                    dia_sum = 0
                    mes +=1
            else:
                if (dia + dia_sum > 28): 
                    dia = (dia + dia_sum)%28
                    dia_sum = 0
                    mes +=1
        else:
            #30 DÍAS
            if (dia + dia_sum > 30): 
                dia = (dia + dia_sum)%30
                dia_sum = 0
                mes +=1

        #MESES Y AÑOS
        if mes > 12:
            año += 1
            mes = mes%12

        resultado_fecha += (dia + dia_sum)*10**6 +mes*10**4 + año

        print("Fecha resultado:")
        print(str(resultado_fecha//10**6) + "/" + str((resultado_fecha%10**6)//10**4) + "/" + str(resultado_fecha%10**4))
    else:
        print("Entra incorrecta, vuelva a intentarlo")
else: 
    print("Entra incorrecta, vuelva a intentarlo")