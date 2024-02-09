class Persona:
   # creando un metodo constructor
   def __init__(self, nombre , puesto):
      self.nombre = nombre
      self.puesto = puesto

   ## creando un metodo para la clase persona   
   def Presentacion(self):
      print(f" Hola, mi nombre es {self.nombre} y soy {self.puesto}, mucho gusto")

# haciendo una instanciacion de la clase persona
alumno = Persona("esteba", "estudiante")
profesor = Persona("jose", "profesor")


# llamando al metodo presentacion de la clase persona
alumno.Presentacion()
profesor.Presentacion()
