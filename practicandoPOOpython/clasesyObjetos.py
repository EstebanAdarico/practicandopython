# para crear una clase en python
# se usa la palabra reservada class

class persona:
   #atributos o propiedades 
   def __init__(self,nombre , edad, dni):
      #esto es una variable o propiedad 
      self.nombre = nombre
      self.edad =edad
      self.dni = dni

   #agregando el metodo notas   
   def presentarse(self):
      print(f'Hola soy {self.nombre} tengo {self.edad} años')
      
      
class estudiantes(persona):
   def __init__(slef,grado, *args):
      super(estudiantes,self).__init__(*args)
      self.grado = grado