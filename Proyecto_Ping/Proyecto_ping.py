

crear_carpeta()
limpiar() 
print(f"{blanco}Bienvenido al Programa para tirar Ping a las Camaras\n")#BIENVENIDA
nombre = agregar_datos_str('nombre del Tecnic@: ')#INGRESA ENCARGADO
caja = ingreso(nombre) #la caja vuelve a 0 para tener un registro de los ingresos del encargado, y se registra en un txt el ingreso

while True:
    limpiar() 
    #MENU CON OPCIONES
    print(f"""{blanco}Laboratorio Tecnico del CIP\n\nMenu principal:

    1 – Tirar Ping a todas las camaras
    2 – Tirar Ping a las camaras fijas
    3 – Tirar Ping a las camaras domos
    4 - Ver Resultados
    5 - Exportar al Excel
    6 - Salir
    """)
    opcion = input(f">>> {rojo}")
    if opcion == "1":#todas las camaras
        limpiar()
        cf_pos, cf_neg = tirar_ping() #Fijas       
        cd_pos, cd_neg = tirar_ping_domos()#Domos 
        tecla_cualquiera('continuar')
    elif opcion =="2": #las camaras fijas
        limpiar()
        cf_pos, cf_neg = tirar_ping() #Fijas
        tecla_cualquiera('continuar')
    elif opcion =="3": #las camaras domos
        limpiar()
        cd_pos, cd_neg = tirar_ping_domos()#Domos 
        tecla_cualquiera('continuar')
    elif opcion =='4': #Ver Resultados
        limpiar() #Limpio pantalla
        lista_positivos = (cf_pos +'\n'+ cd_pos)
        lista_negativos = (cf_neg +'\n'+ cd_neg)
        e = len(cf_pos)
        e2 = len(cf_neg)
        e3 = len(cd_pos)
        e4 = len(cd_neg)
        print(f'{blanco}Resultados')
        print(f'\n{blanco}Fijas positivos => {verde}{e} \n{blanco}Domos positivos => {verde}{e2} \n{blanco}Lista:\n {lista_positivos}\n{blanco}Fijas negativos => {rojo}{e3} \n{blanco}Domos negativos => {rojo}{e4} \n{blanco}Lista:\n', lista_negativos)
        while True:  
            print(f'{blanco}Desea guardar los resultados?\ns = si / n = no')
            opcion = input(f">>>{cyan} ")
            if opcion == 's' or opcion == 'S':
                name = f"{ruta}Registro {fecha} {hora}.txt"
                salvar(name)
                break
            elif opcion == 'n' or opcion == 'N':
                break
            else:
                print(f"{rojo}Error de opcion{blanco}")
        tecla_cualquiera('continuar')
    elif opcion == '5':
        limpiar() #Limpio pantalla
        print(f"{blanco}Guardando datos, por favor espere...")
        time.sleep(3)
        lista_positivos = (cf_pos +'\n'+ cd_pos)
        lista_negativos = (cf_neg +'\n'+ cd_neg)
        if len(lista_positivos) == 0 or len(lista_negativos)==0:
            print('No hay datos en las listas de camaras positivos y negativos')
        else:
            for i in lista_positivos:
                filas.append(['Cam '+str(i), 'OK'])
                reg_sale()
                filas = []
            for i in lista_negativos:
                filas.append(['Cam '+str(i), 'S/F'])
                reg_sale()
                filas = []
        print('{verde}Datos exportados con exito!{blanco}')
        tecla_cualquiera('continuar')        
    elif opcion == '6':
        print("\nCerrando...")
        time.sleep(3)
        limpiar()
        print(f"{blanco}Gracias por utilizar el programa!!!")
        time.sleep(3)
        break  
    else: #opcion incorrecta
        limpiar()
        print("Error en la opción!")
        tecla_cualquiera('finalizar')