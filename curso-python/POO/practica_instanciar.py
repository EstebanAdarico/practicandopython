class Personaje:
   def __init__(self,nombre, fuerza,inteligencia,defensa,vida):
      self.nombre = nombre
      self.fuerza = fuerza
      self.inteligencia = inteligencia
      self.defensa = defensa
      self.vida = vida

   def atributos(self):
      print(self.nombre,":",sep="")
      print(".Fuerza:", self.fuerza)
      print(".Inteligencia:", self.inteligencia)
      print(".Defensa:", self.defensa)
      print(".Vida:" , self.vida)
   
   def subir_nivel(self, fuerza,inteligencia,defensa):
      self.fuerza = self.fuerza + fuerza
      self.inteligencia = self.inteligencia + inteligencia
      self.defensa = self.defensa + defensa

   def esta_vivo(self):
      return self.vida > 0
   
   def morir(self):
      self.vida = 0
      print(self.nombre,"ha muerto")
   
   def damage(self,atacante):
      return max(0,self.fuerza - atacante.defensa)#7
   
   def atack(self,enemigo):
      damage = self.damage(enemigo)
      enemigo.vida = enemigo.vida - damage
      print(self.nombre,"ha realizado",damage,"puntos de damage a",enemigo.nombre)
      if enemigo.esta_vivo():
         print("la vida de", enemigo.nombre, "es", enemigo.vida)  
      else:
         enemigo.morir()


#clase heredada llamada Guerrero
#Personaje seria la superClase

class Guerrero(Personaje):
   def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida)
      self.espada = espada

   def cambiar_arma(self):
      opcion = int(input("elige el arma: (1)Acero valyrio,damage 8. (2)Matadragones,damage 10"))
      if opcion ==1:
         self.espada = 8
      elif opcion == 2:
         self.espada =10
      else:
         print("Number de arma incorrecto")


   def atributos(self):
      super().atributos()
      print(".Espada:", self.espada)

   def damage(self,enemigo):
      return self.fuerza* self.espada - enemigo.defensa

class Mago(Personaje):
   def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro):
      super().__init__(nombre, fuerza, inteligencia, defensa, vida)
      self.libro = libro
   
   def atributos(self):
      super().atributos()
      print(".Libro:", self.libro)
      
   def damage(self,enemigo):
      return self.fuerza*self.libro - enemigo.defensa
   



persona1 = Personaje("bann",10,5,8,100)
persona1.atributos()
celda = Guerrero("jugger",10,5,9,100,8)
celda.atributos()
mago = Mago("vanessa",20,15,10,100,5)
mago.atributos()


def combate(player_1,player_2):
   turno = 0
   while player_1.esta_vivo() and player_2.esta_vivo():
      player_1.atack(player_2)
      print(">>> Accion de ", player_1.nombre,":", sep="")
      player_2.atack(player_1)
      print(">>> Accion de ", player_2.nombre,":", sep="")
      if player_1.esta_vivo():
         print("\nHa ganado",player_1.nombre)
      elif player_2.esta_vivo():
         print("\hHa ganado",player_2.nombre)
      else:
         print("\Empate")
