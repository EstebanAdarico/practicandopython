#funciones con el parametro por defecto
def valor (apellido="puma"):
   print(f"hola, tu apellido es {apellido}")

print(valor())
#funciones con numero variable de argumentos
def lista_de_nombres(*nombres):
   for i in nombres:
      print(f"convocados, {i}")

#funcion para llamar todos los nombres no olvidar el asterisco
lista_de_nombres("juan", "pedro", "maria")
def encontrar(*nombres1):
   for nombre in nombres1:
      if nombre =="esteban":
         return(f" el nombre encontrado es:{nombre}")

print(encontrar("juan", "pedro", "maria", "esteban"))

def sumador(*numeros):
   resultado_suma = []
   sumador = 0
   for i in numeros:
      resultado_suma.append(i)
      sumador += i
   return sumador

print(sumador(1, 2, 3, 4, 5))                   