def saludo(func):
   def wrapper(*args,**kwargs):
      print("Hola, bienvenido al decorador de saludo")
      edad = kwargs.get('edad')
      nombre = kwargs.get('nombre')
      apellido = kwargs.get('apellido')
      if edad is not None:
         if(edad>= 18):
            mensaje = f" {nombre}{apellido}, tienes {edad} años, eres mayor de edad"
         else:
            mensaje = f" {nombre}{apellido}, es menor de edad por que tiene {edad} años"
      else:
         mensaje  = "Edad no identificada"
      kwargs['mensaje'] = mensaje
      return func(*args, **kwargs)
   return wrapper

@saludo
def mejorando_saludo(nombre,apellido,edad, mensaje=None):
   print(f"hola {mensaje}")

@saludo
def despedida(nombre, apellido, edad, mensaje=None):
   print(f"Adiós {mensaje}")
   
# LLmando a una funcion decorada
# mejorando_saludo(nombre ="Juan", apellido="Pérez", edad=30)
# mejorando_saludo(nombre = "Ana", apellido="Gómez", edad=17)
despedida(nombre="Carlos", apellido="López", edad=25)
despedida(nombre="Lucía", apellido="Martínez", edad=15)