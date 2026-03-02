import tkinter as tk

def saludo():
   print("este es tu primer programa en tkinter")
   
   
def conteo ():
   global contador
   contador += 1
   etiqueta.config(text=f"Contador: {contador}")
   
ventana = tk.Tk()
ventana.title("la primera ventan de saludo")

boton_saludo = tk.Button(ventana, text="saludar", command = saludo)
boton_saludo.pack()

boton_depedida = tk.Button(ventana, text="despidete", command= lambda: print("adiós, hasta luego!"))
boton_depedida.pack()

etiqueta = tk.Label(ventana, text="Contador: 0")
etiqueta.pack()

#especificaciones de la ventana
ventana.geometry("400x300")
ventana.mainloop()