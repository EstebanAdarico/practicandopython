def exterior(b):
   x = 10
   def interior(c):
      x = 5+c  # Esta x es local, NO modifica la x de exterior()
      print("Dentro de interior:", x)
   interior(b)
   print("Después de interior:", x)

exterior(10)

#diccionario para registrar contador de llamadas
contador_global = {}

def contador_llamadas(func):
   contador = 0
   def wrapper():
      nonlocal contador
      contador +=1
      contador_global[func.__name__] = contador
      func()
   return wrapper

@contador_llamadas
def saludar():
   print("estas bien")

saludar()
saludar()
saludar()
saludar()

for func, contador in contador_global.items():
   print(f"la funcion {func} ha sido llamada{contador} veces")