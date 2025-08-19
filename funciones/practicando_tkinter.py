import tkinter as tk
def saludar():
   print("siente la focking vibra")
ventana = tk.Tk()
ventana.title("la primera focking primera ventana")
ventana.geometry("400x300")
ventana.config(bg="lightblue")


btn=tk.Button(ventana, text="saludar", command=saludar,bg="lightblue",
   fg="darkblue",
   font=("Helvetica", 14, "bold"),
   width=15,
   height=2,
   relief="raised",
   cursor="hand2")
btn.pack(pady=20)

ventana.mainloop()