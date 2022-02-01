import tkinter as tk

def obtener_nombre():
    '''
    Esta funcion toma el dato de la caja de texto.
    La misma esta pensada para usar con un boton.
    '''
    nombre = ingreso_nombre.get() #con get obtengo el valor de la caja de texto
    turno = ingreso_turno.get()
    f = open(f"Test.txt","a")
    f.write('#'*50)
    f.write(f"\nINGRESO:01/02/22 {nombre} del turno: {turno}\n")
    f.close()
    



#Crear la ventana.
ventana = tk.Tk()
#Establecer un titulo.
ventana.title('PROGRAMA DE PINES v1.0 BETA')
#Establecer un tamaño.
ventana.config(width=900, height=600)
#Bloquear el redireccionamiento.
ventana.resizable(0,0) #nos permite redimencional la pagina. Los parametros son boobleanos, de manera que True es 1 y False es 0
nombre = tk.Label(ventana,text= 'Nombre:', font=('Calibri',16))
nombre.place(x=300,y=220)
#Crear un boton.
boton_siguiente = tk.Button(ventana, text='Siguiente', command=obtener_nombre)
#Le doy un tamaño y una posicion.
boton_siguiente.place(x=700, y=500, width=100, height=25)
#Crear un caja de texto.
ingreso_nombre = tk.Entry(ventana)
#Le doy un tamaño y una posicion.
ingreso_nombre.place(x=400,y=225, width=200, height=25)
#Agregamos una etiqueta con titulo.
turno = tk.Label(ventana,text= 'Turno:', font=('Calibri',16))
turno.place(x=320,y=320)
ingreso_turno = tk.Entry(ventana)
ingreso_turno.place(x=400,y=325, width=200, height=25)



titulo = tk.Label(ventana,text= 'Programa de Pines', font=('Calibri',20))#le ajustamos la fuente y el tamaño.
#Establecemos ubicacion de la etiqueta.
titulo.place(x=100,y=70)





#Mostrar ventana
ventana.mainloop() #corta el codigo hasta que la ventana se cierre. 


