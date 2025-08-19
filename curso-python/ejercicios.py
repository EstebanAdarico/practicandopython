from datos import personajes_principales
#[0,1,2,3,4,5]
def media(p):
   suma = 0
   recorrido = 0
   for personaje in p:
      suma += personaje[4]
      recorrido +=1
   suma = suma // recorrido
   return suma
print(media(personajes_principales))