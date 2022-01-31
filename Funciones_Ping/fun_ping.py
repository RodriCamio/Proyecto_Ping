import os
import subprocess
from Variables_Ping.variables_ping import blanco, rojo, verde, ruta, carpeta, camaras_libres, camaras_libres_Domos
from os import remove
from os import path


####################__Limpiar Pantalla__####################
def limpiar():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

####################__Verificar__####################
def verificar_vacio(dato): #función para verificar si está vació el campo
    while dato == "":
        print(f"{blanco}Campo vacio")
        print(f"{blanco}Ingrese nuevamente:")
        dato = input (f">>>{rojo} ")
    return dato
 
def verificar_str(tecnico):
    while tecnico == "" or tecnico.isdecimal() == True:
            print(f"{blanco}Campo vacío o número ingresado")
            print(f"{blanco}Ingrese nuevamente:")
            encargado = input(f">>>{rojo} ")
    return tecnico

####################__Ingreso de Datos__####################
def agregar_datos_int(n):
    x = input(f"{blanco}Ingrese {n}{rojo}")
    x = verificar_vacio(x)
    return x

def agregar_datos_str(n):
    x = input(f"{blanco}Ingrese {n}{rojo}")
    x = verificar_str(x)
    return x

####################__Precione tecla cualquiera__####################
def tecla_cualquiera(n):
    while True:
        continuar = input(f"{blanco}\nPresione Enter para {n}...")
        if continuar =="":
            limpiar()
            break
        else:
            limpiar()
            break

####################__Crear Carpeta__####################
def crear_carpeta():
    if not(os.path.exists(ruta)):
        os.mkdir(carpeta)
    else:
        pass

####################__Sacar Ips Libres__####################
def sacar_libres(lista,i):
    pines = []
    for i in range(1, i):
        pines.append(i)
    a = set(pines)
    b = set(lista)
    lista_sin_libres = list(a - b)
    return lista_sin_libres

####################__Tirar Pines__####################
def tirar_ping():
    lista_positivos = []
    lista_negativos = []
    completo = sacar_libres(camaras_libres, 180)
    for i in completo:
        with open('pines fijas.txt', encoding='utf-8', mode='w') as e:
            c = subprocess.run('ping 10.0.2.'+ str(i) +' -n 1',stdout=e) # -n sirve para indicar la cantidad de piness
            f = open('pines fijas.txt', 'r')
            data = f.readlines()
            data = str(data)
            r = data.find('bytes=32')
            if not(r == -1):
                print(f'{blanco}Cam '+str(i)+f' = {verde} OK{blanco}')
                lista_positivos.append(i) 
            else:
                print(f'{blanco}Cam '+str(i)+f' = {rojo} S/F{blanco}')
                lista_negativos.append(i)

    return (lista_positivos, lista_negativos)

def tirar_ping_domos():
    lista_positivos = []
    lista_negativos = []
    completo2 = sacar_libres(camaras_libres_Domos,61)
    for i in completo2:
        with open('pines domos.txt', encoding='utf-8', mode='w') as e:
            c = subprocess.run('ping 10.0.3.'+ str(i) +' -n 1',stdout=e) # -n sirve para indicar la cantidad de piness
            f = open('pines domos.txt', 'r')
            data = f.readlines()
            data = str(data)
            r = data.find('bytes=32')
            if not(r == -1):           
                if i < 10:
                    print(f'{blanco}Cam 30'+str(i)+f' = {verde} OK{blanco}')
                    lista_positivos.append('30'+str(i))                       
                    continue
                else:
                    print(f'{blanco}Cam 3'+str(i)+f' = {verde} OK{blanco}')
                    lista_positivos.append('3'+str(i)) 
            else:
                if i < 10:
                    print(f'{blanco}Cam 30'+str(i)+f' = {rojo} S/F{blanco}')
                    lista_negativos.append('30'+str(i))
                    continue
                else:
                    print(f'{blanco}Cam 3'+str(i)+f' = {rojo} S/F{blanco}')
                    lista_negativos.append('3'+str(i))
    return (lista_positivos, lista_negativos)

####################__Juntar Listas__####################
def juntar_lista(list1, list2):
    lista = (f'{list1}\n{list2}')
    return lista