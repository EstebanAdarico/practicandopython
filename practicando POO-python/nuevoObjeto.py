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



class Persona2:
   # creando el medoto contructor
   def __init__(self, altura , peso):
      self.alturaDeLaPersona = altura
      self.pesoDeLaPersona = peso
   
   def Despedida (self):
      print(f"Hola, mi altura es {self.alturaDeLaPersona}, tambien mi peso es ")

