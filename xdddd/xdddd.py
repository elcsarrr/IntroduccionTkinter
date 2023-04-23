# -*- coding: utf-8 -*-
from PIL import Image
from tkinter import*

root = Tk() #ventana

root.title("Mi primer Ventana") #poner titulo

root.geometry ("500x300") #le da el tamaño a la ventana
root.iconbitmap("C:/Users/cnscn/OneDrive/Escritorio/imagenes pyton/azulitoo.ico")
root.resizable(0,0) #el usuario no pues cambiar el tamaño, imdica el 0 que no pueda moverlo hacia un lado

#----------------------------------------------------------------

#root.config(bg= "red", cursor= "mouse") #pone la ventana en rojo y el mouse cambia como ve el mouse


"""
texto = Label(root, text="Hola Mundo") # label es texto y se pone en que ventana va a mostar
texto.pack() #imprime el hola mundo

boton1 = Button(root, text="minimizar", command=root.iconify)
boton1.pack(side=RIGHT)#posiciona el boton

def imprimir():
    #print("Imprimiendo.....") imprime pero en la consola
    label1 = Label(root, text = "imprimiendo.....")
    label1.pack()
boton2 = Button(root, text="imprimir", command=imprimir, bg = "blue")
boton2.pack(side=LEFT)#POSICIONA

"""
#-------------------------------------------------------------
"""
etiqueta = Label(root, text="Etiqueta")
etiqueta.place(x=30, y=40)
#etiqueta.grid(row=0,column=0) ubica con filas y columnas

boton3 = Button(root, text="boton")
boton3.grid(row=0, column=1)
"""


"""
def saludo():
    print("hola te saludo")
def minimizar():
    root.iconify()

etiqueta4 = Label(root, text= "Saluda desde aqui")
etiqueta4.place(x=30, y=50)


etiqueta3 = Label(root, text= "Minimizar desde aqui")
etiqueta3.place(x=30, y=100)

boton5 = Button(root, text="haz click para saludar", command=saludo)
boton5.place(x=200, y=50)


boton6 = Button(root, text="haz click para Minimizar", command=minimizar)
boton6.place(x=200, y=100)
"""

#-------------------------------------------------------------------------
"""
nombre = StringVar()
Apellido = StringVar()

nombre.set("")

Apellido.set("")

def saludar():
    print ("hola "+nombre.get()+" ", Apellido.get())


etiqueta1 = Label(root, text = "escribe tu nombre")
etiqueta1.place(x=10, y=10)
entrada1 = Entry(root, textvariable=nombre)
entrada1.place(x=170, y=10)


etiqueta2 = Label(root, text = "escribe tu apellido")
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable=Apellido)
entrada2.place(x=170, y=40)
boton1 = Button(root, text="saludar ahora", command=saludar)
boton1.place(x=10, y=100)
"""














root.mainloop() #hace que la venta no se cierre hasta que queramos, va en el final