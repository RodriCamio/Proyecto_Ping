import os
import subprocess
from Variables_Ping.variables_ping import blanco, rojo, verde, ruta, carpeta, camaras_libres, camaras_libres_Domos
from os import remove, path



####################__Limpiar Pantalla__####################
def limpiar():
    '''
    Funcion para limiar pantalla, detecta si el sistema es nativo y usa "cls", de lo contrario usa "clear"
    '''
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

####################__Verificar__####################
def verificar_vacio(dato): #
    '''
    Funcion para verificar si el campo esta vacio, se pasa como argumento el dato a verificar
    si el mismo esta vacio ("") entonces se pide de nuevo hasta que este sea distindo de "" (vacio)
    '''
    while dato == "":
        print(f"{blanco}Campo vacio")
        print(f"{blanco}Ingrese nuevamente:")
        dato = input (f">>>{rojo} ")
    return dato
 
def verificar_str(dato):
    '''
    Funcion que verifica si el campo esta vacio o es un numero, toma como argumento el dato y lo compara
    si detecta que esta vacio o es un numero, vuelve a pedirlo 
    y luego retorna el dato ya verificado que es un str
    '''
    while dato == "" or dato.isdecimal() == True:
            print(f"{blanco}Campo vacío o número ingresado")
            print(f"{blanco}Ingrese nuevamente:")
            encargado = input(f">>>{rojo} ")
    return dato

def verificar_int(n):
    '''
    Funcion que verifica si el campo esta vacio o es un caracter, toma como argumento el dato y lo compara
    si detecta que esta vacio o es un caracter, vuelve a pedirlo 
    y luego retorna el dato ya verificado que es un int
    '''
    while n == "" or n.isdecimal() == False:
            print(f"{blanco}Campo vacío o no es un numero")
            print(f"{blanco}Ingrese nuevamente:")
            encargado = input(f">>>{rojo} ")
    return n

####################__Ingreso de Datos__####################
def agregar_datos_int(n):
    '''
    Esta funcion toma el dato del argumento como un input pero con la palabra predefinida de: "ingrese"
    Pone en color rojo la entrada del usuario, lo compara para saber si es realmente un entero con otra funcion. 
    Y retorna el dato ingresado por el usuario ya comparado y convertido a entero.
    '''
    x = input(f"{blanco}Ingrese {n}{rojo}")
    x = verificar_vacio(x)
    return x

def agregar_datos_str(n):
    '''
    Esta funcion toma el dato del argumento como un input pero con la palabra predefinida de: "ingrese"
    Pone en color rojo la entrada del usuario, lo compara para saber si es realmente un str con otra funcion. 
    Y retorna el dato ingresado por el usuario ya comparado y convertido a str.
    '''
    x = input(f"{blanco}Ingrese {n}{rojo}")
    x = verificar_str(x)
    return x

####################__Precione tecla cualquiera__####################
def tecla_cualquiera(n):
    '''
    Con esta funcion se pretende evitar que se cierre inesperadamente el programa esperando un enter o un ingreso
    de algun tipo para continuar el programa.
    '''
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
    '''
    Esta funcion usa la libreria os para saber si exite la carpeta que queremos crear primero y si no existe la crea.
    '''
    if not(os.path.exists(ruta)):
        os.mkdir(carpeta)
    else:
        pass

####################__Sacar Ips Libres__####################
def sacar_libres(lista,i):
    '''
    En esta funcion se trata de comprar dos listas y eliminar las que ya estan en la lista del argumento.
    El primer argumento es la lista que contiene los numeros que no queremos que esten en la nueva lista.
    El segundo argumento es el numero limite de la lista nueva que vamos a crear, ese limite se usa en un bucle
    for para armar la lista y luego se los convierte en Set para que no tenga numero repetidos y por ultimo
    se restan los valores de la lista del argumento con las de la nueva lista y se retorna el resultado.
    '''
    pines = []
    for i in range(1, i):
        pines.append(i)
    a = set(pines)
    b = set(lista)
    lista_sin_libres = list(a - b)
    return lista_sin_libres

####################__Tirar Pines__####################
def tirar_ping():
    '''
    Esta funcion crea dos listas vacias que se van a ir llenando.
    Se crea una lista llamada "completo", sacando todos los ips libres con un limite de 180 porque esa es la cantidad maxima.
    Con un for se recorre la lista nueva, se abre un archivo txt donde se guardan los datos del ping que se tiro.
    Se compara, usando el "find" para saber si es positivo o negativo, devido a que cuando el ping es negativo no tiene "bytes=32".
    Al final retorna una tupla con las dos listas, para asignarlas hay que usar la propiedad Unpacking.
    '''
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
    '''
    Esta funcion crea dos listas vacias que se van a ir llenando.
    Se crea una lista llamada "completo", sacando todos los ips libres con un limite de 61 porque esa es la cantidad maxima.
    Con un for se recorre la lista nueva, se abre un archivo txt donde se guardan los datos del ping que se tiro.
    Se compara, usando el "find" para saber si es positivo o negativo, devido a que cuando el ping es negativo no tiene "bytes=32".
    Ademas, se hace una comparacion mas debido a que algunas camaras son 3aa o 30a (siendo a = i) 
    Al final retorna una tupla con las dos listas, para asignarlas hay que usar la propiedad Unpacking.
    '''
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
                    continue
            else:
                if i < 10:
                    print(f'{blanco}Cam 30'+str(i)+f' = {rojo} S/F{blanco}')
                    lista_negativos.append('30'+str(i))
                    continue
                else:
                    print(f'{blanco}Cam 3'+str(i)+f' = {rojo} S/F{blanco}')
                    lista_negativos.append('3'+str(i))
                    continue
    return (lista_positivos, lista_negativos)

####################__Juntar Listas__####################
def juntar_lista(list1, list2):
    '''
    Esta funcion crea una cadena que contiene las dos listas mencionadas en el argumento, separandolas por un salto de linea.
    Retorna la cadena terminada.
    '''
    lista = (f'{list1}\n{list2}')
    return lista