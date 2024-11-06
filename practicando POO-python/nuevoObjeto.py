class Persona:
   # creando un metodo constructor
   def __init__(self, nombre , puesto):
      self.name = nombre
      self.pues = puesto

   ## creando un metodo para la clase persona   
   def Presentacion(self):
      print(f" Hola, mi nombre es {self.name} y soy {self.pues}, mucho gusto")

# haciendo una instanciacion de la clase persona
alumno = Persona("esteba", "estudiante")
profesor = Persona("jose", "profesor")


# llamando al metodo presentacion de la clase persona
alumno.Presentacion()
profesor.Presentacion()

class Person1:
   def __init__(self,nombre) -> None:
      self.__nombre = nombre

   def get_nombre(self):
      return self.__nombre
   
   def set_nombre(self,nombre):
      self.__nombre = nombre

h = Person1("Juan")
print(h.get_nombre())
h.set_nombre("Carlos")
print(h.get_nombre())

estudiante = ('alex',22,'M')
print(estudiante.index('M'))