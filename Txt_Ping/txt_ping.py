from Variables_Ping.variables_ping import *
from Funciones_Ping.fun_ping import *

####################__Registro TXT__####################
def ingreso(persona): #función para guardar el evento, la fecha y la persona
    '''
    Funcion para agregar en un txt el ingreso de una persona, con su hora.
    Toma como argumento el nombre de la persona.
    '''
    f = open(f"{ruta}Registro {fecha_y_hora}.txt","a")
    f.write("IN"+" "+fecha_y_hora+" "+persona+"\n")
    f.close()

lista_positivos = juntar_lista(cf_pos, cd_pos)
lista_negativos = juntar_lista(cf_neg, cd_neg)

####################__Guardar datos TXT__####################
def salvar(x, list1, list2, list3, list4, list5, list6):
    '''
    Esta funcion tiene varios argumentos, los cuales se dividen en el nombre del archivo txt,
    y las listas positivas y negativas de las camaras.
    Se agregan al txt de registro con fecha y hora y se cierra el mismo.
    '''
    f = open(x, "a")
    f.write('#'*50)
    f.write(f'''\nREGISTRO del {fecha_y_hora}

Fijas positivos => {list1} 
Domos positivos => {list3} 

Lista:\n{list5}\n

Fijas negativos => {list2} 
Domos negativos => {list4} 

Lista:\n{list6}\n''')
    f.write('#'*50+'\n')
    f.close()