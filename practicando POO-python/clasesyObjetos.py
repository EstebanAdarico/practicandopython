# para crear una clase en python
# se usa la palabra reservada class

class Estudiante:
   def __init__(self,nombre , edad , grado,nota) :
      #esto es una variable o propiedad 
      self.nombre = nombre
      self.edad =edad
      self.grado = grado
      self.nota = nota

   #segundo metodo
   def estudiar(self,):
      print(f"Estudiando...,,,,,,,,{self.nombre}")
   #tercer metodo
   def reprobado(self , nota, nombre , grado):
      if nota < 10 :
         print(f'el alumno {nombre } de grado  {grado}')


#enumerar los dias de la semana e imprimir por pantalla segun los dias que voy ingresando por teclado
diasSemana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
def discovered (dias,parametro):
   for i in range(len(dias)):
      if i == parametro:
         print(dias[i])
      elif(parametro <= 0 or parametro >= len(dias[-1])):
         print(f"sigue intentadolo el numero fue {parametro}")
         break
discovered(diasSemana,7)

