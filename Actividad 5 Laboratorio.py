#------------------Caso 1------------------
consumo = int(input("Ingrese consumo en m^3: \n"))
habitantes = int(input("Ingrese cantidad de habitantes: \n"))
tarifa = 0


if consumo < 15: tarifa = 5
elif 15 <= consumo < 30:
    if habitantes > 3: tarifa = 4
    elif habitantes == 3: tarifa = 4.5
    else: tarifa = 5
    print(f"La tarifa es de Q{tarifa} por m^3")
elif consumo >= 30: 
    if habitantes > 5: tarifa = 3.5
    elif habitantes%2 == 0: tarifa = 4
    else: tarifa = 4.2
    print(f"La tarifa es de Q{tarifa} por m^3")
else:
    print("Entrada no valida")

#------------------Caso 2------------------
año_ac = int(input("Ingrese año actual: \n"))
año = int(input("Introduzca el año de su vehiculo: \n"))

if año >= 2001:
    placa = input("Introduzca número de placa: \n")
    
    ult = placa[len(placa)-1]
    
    if int(ult)%2 == 0: print("No puede circular su vehiculo los días lunes")
    if int(ult)%2 != 0: print("No puede circular su vehiculo los días viernes")
    
    if año%2 == 0: print("Y no puede circular los días sábados, solo hasta medio día.")
    if año_ac-año > 25: print("\nAdvertencia: \nDebe darle mantenimiento obligatorio a su vehiculo")
        
else:
    pass