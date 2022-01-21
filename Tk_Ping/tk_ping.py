import tkinter as tk

ventana = tk.Tk()
ventana.geometry('900x600')
ventana.resizable(0,0) #nos permite redimencional la pagina. Los parametros son boobleanos, de manera que True es 1 y False es 0

ventana.title('PROGRAMA DE PINES v1.0 BETA')

titulo = tk.Label(ventana,text= 'Programa de Pines', font=('Calibri',20))
titulo.place(x=100,y=70)

nombre = tk.Label(ventana,text= 'Nombre:', font=('Calibri',16))
nombre.place(x=300,y=260)

ingreso_nombre = tk.Entry(ventana)
ingreso_nombre.place(x=400,y=265)

boton_siguiente = tk.Button(ventana, text='Siguiente')
boton_siguiente.pack(anchor='ne')






ventana.mainloop()


