# Se importa libreria tkinter con todas sus funciones

from tkinter import *
from tkinter import messagebox

# Funciones de la app

def Matriz():
    z = int(x.get())
    M= int(300+(z-3)*50)
    if M>3:
        t_resultados.insert(INSERT, "Valor a pagar: "+str(M)+"\n")
    else:
        t_resultados.insert(INSERT, "Valor a pagar: $300""\n")

def Borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    t_resultados.delete("1.0","end")

def Salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()


# Se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

# Título de la ventana
ventana_principal.title("MATRIZ CUADRADA")

# Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

# Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

x = StringVar()

#--------------------
# Frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "aquamarine2", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "BUSCAR UN NÚMERO DENTRO DE LA MATRIZ")
titulo.config(bg = "hot pink", fg = "black", font = ("Times New Roman",16))
titulo.place(x = 15, y = 10)

# Etiqueta para Tamaño
lb_x = Label(frame_entrada, text = "Tamaño de la matríz: ")
lb_x.config(bg="orchid2", fg="black", font=("Times New Roman",16))
lb_x.place(x=10, y=50, width=200, height=30)

# Entry para Tamaño
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Times New Roman",25), justify=LEFT,fg="black")
entry_x.focus_set()
entry_x.place(x=215, y=50, width=115, height=30)

# Etiqueta para Buscar
lb_x = Label(frame_entrada, text = "Número a buscar: ")
lb_x.config(bg="orchid2", fg="black", font=("Times New Roman",16))
lb_x.place(x=10, y=100, width=150, height=30)

# Entry para Buscar
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Times New Roman",25), justify=LEFT,fg="black")
entry_x.focus_set()
entry_x.place(x=165, y=100, width=115, height=30)

# Botón para sumar
bt_tiempo = Button(frame_entrada, text="CREAR MATRIZ", command=Matriz)
bt_tiempo.place(x=45, y=150, width=100, height=30)

# Botón borrar
bt_tiempo = Button(frame_entrada, text="BORRAR",command=Borrar)
bt_tiempo.place(x=190, y=150, width=100, height=30)

# Botón buscar
bt_salir = Button(frame_entrada, text="BUSCAR NÚMERO",command=Salir)
bt_salir.place(x=335, y=150, width=120, height=30)

# Botón salir
bt_salir = Button(frame_entrada, text="SALIR",command=Salir)
bt_salir.place(x=190, y=200, width=100, height=30)

#--------------------
# Frame resultados
#--------------------

# Frame resultados
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="aquamarine2", width=480, height=230)
frame_resultados.place(x=10, y =260)

# Área de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="SlateGray1", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=460, height= 210)

ventana_principal.mainloop()