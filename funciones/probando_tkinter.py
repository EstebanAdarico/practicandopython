import tkinter as tk

def saludo():
   print("este es tu primer programa en tkinter")

contador = 0   
def conteo ():
   global contador
   contador += 1
   etiqueta.config(text=f"Contador: {contador}")
   


ventana = tk.Tk()
ventana.title("la primera ventan de saludo")

boton_saludo = tk.Button(ventana, text="saludar", command = conteo)
boton_saludo.pack()
boton_depedida = tk.Button(ventana, text="despidete", command= lambda: print("adiós, hasta luego!"))
boton_depedida.pack()
#el texto de la etiqueta se actualiza con el contador
etiqueta = tk.Label(ventana, text="Contador: 0", font=("Arial", 16),anchor="center")
etiqueta.pack(pady=20)

#especificaciones de la ventana
ventana.geometry("400x300")
ventana.mainloop()

class MiVentana():
   def __init__(self,root):
      self.root = root
      self.root.title("la primera ventana")
      self.root.geometry("400x300")
      self.root.config(bg="lightblue")
      




if __name__ == "__main__":
   ventana = tk.Tk()
   #mandamos a llamar a la clase MiVentana y creamos una instancia con el objeto ventana
   app = MiVentana(ventana)
   ventana.mainloop()
   print("fin del programa")