#{"id": '', "org": "", "dest": "", "ast":5, "ast_disp":5,"disp":True}
vuelos = []
#{'id': '', 1: 1, 2: 1, 3: 1 ..., n:1}
asientos = []
#{'id_res': 0, 'id_vuelo': '', 'nombre': '', 'cantidad_asientos': 0, 'asientos_cliente': [0]}
reservas = []

#BUCLE GENERAL
while True:
    print('-'*25 +"¡Bienvenido!"+'-'*25)
    #SELECCION DE OPCIONES
    print(" 1) Crear vuelo\n 2) Reservar vuelo\n 3) Ver reservas\n 4) Salir")
    opc = int(input("\033[1m>>>  ¿Qué desea hacer?: \033[0m"))
    
    if opc == 1:
        #CREAR VUELOS
        print('-'*25 +"Crea un vuelo"+'-'*25)
        while True: #DETECCION DE CODIGO UNICO
            id = input("\033[1m>>>  Ingresa un CÓDIGO para el vuelo(Pues usar cualquier caracter): \033[0m")
            dupl = False
            for v in vuelos:
                if id == v['id']: 
                    print(f'\n...Error, el código {id} ya está en uso, vuelve a intentarlo\n')
                    dupl = True
            if dupl == False: break
        #CREACIÓN DE ATRIBUTOS 
        org = input("\033[1m>>>  Ingresa un ORIGEN para el vuelo: \033[0m")
        dest = input("\033[1m>>>  Ingresa un DESTINO para el vuelos: \033[0m")
        ast = int(input("\033[1m>>>  Ingresa CUANTOS ASIENTOS posee el vuelo: \033[0m"))
        print(f"\nEl vuelo {id}, con origen en {org} y destino a {dest} con disponibilidad de {ast} asientos.\n")
        while True: #PREGUNTA DE CONFIRMACIÓN
            print("Está seguro desea agregar este vuelo?")
            print(" 1) Sí\n 2) No")
            preg = int(input("\033[1m>>>  Seleccione una opción: \033[0m"))
            if preg == 1: #ACEPTAR
                vuelos += [{"id": id, "org": org, "dest": dest, "ast": ast, "ast_disp":ast, "disp": True}]
                #AÑADIR A LISTA DE ASIENTOS
                ast_dic = {'id': id}
                for n in range(ast): ast_dic[n+1] = 1
                asientos += [ast_dic]
                print(f"\n> El vuelo {id} ha sido guardado correctamente\n")
                break
            elif preg == 2: #CANCELAR
                print("\n> Creación de vuelo cancelada\n")
                break
            else: print("\n...Lo siento, vuelve a intentarlo\n") #NO SÉ 
    elif opc == 2:
        print('-'*25 +"Realizar reserva"+'-'*25)
        print("Los vuelos disponibles en este momento son:\n")
        vuelos_disp = []
        
        for v in vuelos:
            if v["ast_disp"] == 0: v["disp"] = False
            
            if v["disp"] == True:
                vuelos_disp += v
                print(f"---> Vuelo {v['id']}")
                print(f"     Origen a {v['org']} y destino a {v['dest']} con {v['ast_disp']} asientos disponibles")
                #GUARDA ASIENTOS DISPONIBLES
                asientos_disponibles = []
                for a in asientos:
                    if a['id'] == v['id']: 
                        for i in range(v['ast']):
                            if a[i+1] == 1: asientos_disponibles += [i+1]
                print("     Disponibilidad de asientos:")
                print(" "*25 +"\033[1mDisponible:1   No Disponible:2\033[0m")
                for z in range(v['ast']): #IMPRIME LOS ASIENTOS QUE ESTAN DISPONIBLES
                    if z+1 == 1:print("     ", end="")
                    if z+1 < 10: print(" ",end="")
                    if z+1 < 100: print(" ",end="")
                    if z+1 in asientos_disponibles:print(f"[{z+1}:1]",end="")
                    else: print(f"({z+1}:0)",end="")
                    
                    if (z+1)%10 == 0:print("\n     ", end="")
                print("\n")
        if len(vuelos_disp) == 0: 
            print("> Lo siento, actualmente ninguno vuelo está disponible")
            continue
        
        print("¿Desea reservar un vuelo?")
        print("1) Sí\n2) No")
        reservacion = False
        while True:#CONFIRMACION DE RESERVACION
            res_v = int(input("\033[1m>>>  ¿Qué desea hacer?: \033[0m"))
            if res_v == 1: 
                reservacion = True
                break
            elif res_v == 2:
                reservacion = False
                break
            else: 
                print("\n...Error, vuelva a intentarlo\n")
                print("-"*50)
        
        if reservacion == True:# SE ACEPTA LA RESERVACION
            print("\n"+"-"*25 + "Bienvenido al Proceso de reservación"+"-"*25)
            vuel_res = {}
            vuelo_encontrado = False
            while True:
                id = input("\033[1m>>>  Seleccione el CÓDIGO de vuelo que desea reservar: \033[0m")
                for v in vuelos: #ENCUENTRA CODIGO DE VUELO
                    if id == v['id'] and v["disp"] == True: #CODIGO ENCONTRADO
                        vuelo_encontrado = True
                        vuel_res = v
                if vuelo_encontrado == False: #SI EL CODIGO DEL VUELO NO SE ENCUENTRA O ESTA LLENO
                    print("\n...Lo siento vuelo no existente o no está disponible, intente nuevamente\n")
                else: break
            #PROCESO DE RESERVACION            
            reserv = {'id_res': 0, 'id_vuelo': id, 'nombre': '', 'cantidad_asientos':0, 'asientos_cliente':[]}
            reserv['id_res'] = len(reservas)+1
            #NOMBRE PARA GUARDAR LA RESERVA
            nombre = input("\033[1m>>>  Ingresa tu NOMBRE para guardar la reseva: \033[0m").lower()
            reserv["nombre"] = nombre
            reserv_ast = []
            
            while True:#BUCLE PARA SELECCIONAR LA CANTIDAD DE ASIENTOS 
                c = int(input("\033[1m>>>  Ingresa la CANTIDAD DE ASIENTOS que deseas reservar: \033[0m"))
                #DETECTA SI NO HAY ASIENTOS O SI LA ENTRADA NO ES VALIDA
                if c > vuel_res['ast_disp']: print(f"\n...Lo siento, el vuelo {vuel_res['id']} solo posee {vuel_res['ast_disp']} disponibles.\n   Porfavor ingrese una cantidad menor.\n")
                elif c <= 0: print("\n...Lo siento, no podemos agregar esa cantidad de asientos, vuelva a intentarlo\n") 
                else: #ENTRADA VALIDA
                    reserv["cantidad_asientos"] = c
                    break
            while c > 0: #PROCESO DE RESERVACIÓN DE ASIENTOS
                print("\nReserva tus asientos: ")
                print("   \033[1m---> Asientos disponibles:\033[0m")
                asientos_disponibles = []
                for a in asientos: #GUARDA ASIENTOS DISPONIBLES EN UNA LISTA
                    if a['id'] == id:
                        for num_a in range(len(a)-1):
                            if a[num_a+1] == 1: asientos_disponibles += [num_a+1]
                for z in range(vuel_res['ast']): #IMPRIME LOS ASIENTOS QUE ESTAN DISPONIBLES
                    if z+1 == 1:print("     ", end="")
                    if z+1 < 10: print(" ",end="")
                    if z+1 < 100: print(" ",end="")
                    if z+1 in asientos_disponibles:print(f"[{z+1}:1]",end="")
                    else: print(f"({z+1}:0)",end="")
                    
                    if (z+1)%10 == 0:print("\n     ", end="")
                print("\n")
                
                while True: #BUCLE PARA 
                    num_ast = int(input("\033[1m>>>  Ingresa NÚMERO DE ASIENTO que deseas reservar: \033[0m"))
                    reservado = False
                    for a in asientos:
                        if a['id'] == id: #DETECTA ID DEL VUELO
                            for num_a in range(len(a)-1):
                                if num_ast in a and a[num_ast] ==1: #DETECTA SI ESTÁ DISPONIBLE
                                    if num_a+1 == num_ast:
                                        a[num_ast] = 0
                                        reserv['asientos_cliente'] += [num_a+1]
                                        reservado = True
                                        print(f"\nAsiento {num_ast} guardado a tu nombre!")
                                        break
                                else: #NO DISPONIBLE
                                    if 0 < num_ast < vuel_res['ast']: print(f"\n...Error, asiento {num_ast} no está disponible, vuelve a intentarlo\n")
                                    else: print(f"\nLo siento, no encontramos el asiento {num_ast}, vuelve a intentarlo\n")
                                    break
                    if reservado == True: #SI LA RESERVA SE CUMPLE SE ELIMINA EL ASIENTO DE LOS DISPONIBLES
                        for v in vuelos:
                            if v['id'] == id: 
                                v['ast_disp'] -=1
                                break
                        break
                #SE RESTA UN INTENTO PARA SELECCIONAR ASIENTO
                if reservado == True: c -= 1
            #CUANDO TERMINA EL BUCLE, SE GUARDA LA RESERVA EN LA LISTA
            print("\n> Reserva guardada con exito!\n")
            reservas += [reserv]
    elif opc == 3: #VER TUS RESERVAS
        if len(reservas) > 0: #SI EXISTEN RESERVAS
            print('-'*25 +"Ver reservas"+'-'*25)
            reserv_encontr = False
            nombre = input("\033[1m>>>  Ingresa el NOMBRE al que estan asignadas tus reservas: \033[0m").lower()
            for r in reservas: #Si se encuentran reservas a tu nombre
                if r['nombre'] == nombre:
                    print(f"\nLas reservas al nombre de {nombre} son:")
                    reserv_encontr = True
                    break

            if reserv_encontr == True: #SI SE ENCUENTRA
                for r in reservas:
                    for v in vuelos:
                        if v['id'] == r['id_vuelo'] and r['nombre'] == nombre: #ENCUENTRA EL RESERVA CON ID DE VUELO Y NOMBRE IDENTICOS
                            print("> Reserva encontrada!")
                            print(f"  -Reserva de {r['nombre']} al vuelo {r['id_vuelo']} con dirección a {v['dest']} y origen en {v['org']},",end="")
                            txt_asientos = f"{r['asientos_cliente']}".replace("[","").replace("]","")
                            print(f" reservando los asientos: {txt_asientos}\n")
                            break
            else:print(f"\n...Lo siento, no encontramos reservas al nombre de {nombre}")
        else:
            print("\n> Lo siento, no tenemos reservas por el momento\n")
    elif opc == 4: break
    else: print("\n...Lo siento, la entrada no es valida, vuelva a intentarlo\n")
        
print("\n¡Vuelva pronto!\n")