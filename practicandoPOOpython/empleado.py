from Persona import Persona
#segunda clase
class Empleado(Persona):
   # aqui es donde cramos las variables o las propiedas  
   def __init__(self, nombre, apellido, dni, telefono,salario) -> None:
   # se necesita la palabra reservada super para que jale las propiedades de la clase persona
      super().__init__(nombre, apellido, dni, telefono)
      # aqui podemos comenzar anadiendo mas propiedades
      self.salario = salario
   

