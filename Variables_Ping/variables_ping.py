import time
import os
import colorama

####################__Colores__####################
colorama.init()
rojo = "\x1b[1;31;49m"
verde = "\x1b[1;32;49m"
amarillo = "\x1b[1;33;49m"
azul = "\x1b[1;34;49m"
magenta = "\x1b[1;35;49m"
cyan = "\x1b[1;36;49m"
blanco = "\x1b[1;37;49m"

####################__Celdas__####################
columnas = [["Camara" , "Estado"]]
filas = []

####################__Fecha__####################
fecha = time.strftime("%d-%m-%Y")
hora =  time.strftime("%H-%Mhs")
fecha_y_hora = f'{fecha} {hora}'

####################__Carpeta__####################
carpeta = f'PINES {fecha}'
ruta = os.getcwd()+ f"\\{carpeta}\\"

####################__Listas__####################
cf_pos = []
cf_neg = []
cd_pos = []
cd_neg = []
camaras_libres = [6, 13, 29, 30, 44, 57, 59, 64, 76, 81, 82, 84, 93, 107, 109, 133, 135, 143, 150, 173, 175, 176]
camaras_libres_Domos = [1, 7, 8, 13, 24, 33, 37, 39, 49, 51, 58, 59, 60]




