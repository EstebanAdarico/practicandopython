#midiendo el tiempo de ejecucion de un programa
import time

def medidor(f):
   def wrapper():
      inicio = time.time()
      print({inicio})
      f()
      fin = time.time()
      print({fin})
      print(f"tiempo de ejecucin:{fin - inicio: .4f} segundos")
   return wrapper
   

@medidor
def tarea_lenta():
   time.sleep(2)  # Simula una tarea que toma tiempo
   print("Tarea lenta completada")

tarea_lenta()
