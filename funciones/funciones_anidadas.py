
#funcion anidadas simple
def saludar(nombre):
   def mensaje():
      return "hola puma"
   return f"nuevamente el saludo es: {nombre}{mensaje()}"

print(saludar("esteban"))

#funcion anidada pero con dos parametros
def nombre_modificado(nombre,apellido):
   def frase(mod_non,mod_ap):
      return f"el nombre modificado es: {mod_non} {mod_ap}"
   return frase(nombre,apellido)

print(nombre_modificado("principe","persa"))