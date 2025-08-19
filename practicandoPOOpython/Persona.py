#Primera clase
class Persona:
   def __init__(self, nombre,apellido ,dni,telefono) -> None:
      self.nombre = nombre
      self.apellido = apellido
      self.dni = dni
      self.telefono = telefono

   #funcion para convertirlo a string
   def __str__(self) -> str:
      return (f"{self.nombre} {self.apellido} - {self.dni}") 
   
   



      #SOLO faltaria el init para definir las propiedades que van dentro de la clase 
   # def formulaCuadrado(self):
    #  area = self.ancho * self.alto
   # return area
   
#figura = Cuadrado (10 , 12)
#print(figura.formulaCuadrado())


