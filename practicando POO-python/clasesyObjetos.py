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
   def estudiar(self):
      print("Estudiando...,,,,,,,,")
   #tercer metodo
   def reprobado(self , nota, nombre , grado):
      if nota < 10 :
         print(f'el alumno {nombre } de grado  {grado}')

   
# para que el usuario interactue deberiamos crear inputs
nombre1 = input("digame su nombre: ")
edad1 = input("digame su edad: ")
grado1 = input("digame su grado:")

#
estudiante = Estudiante(nombre1,edad1,grado1)

#las comillas triples es para poder hacer los saltos de linea
print(f"""
      DATOS DEL ESTUDIANTE :\n\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado:{estudiante.grado}\n
      """)

while True:
   estudiar = input()
   if(estudiar.lower() == "estudiar"):
      estudiante.estudiar()

