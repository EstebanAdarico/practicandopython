# nombres = ["Ana", "Luis"]
# edades = [25, 30]

#zip es para que recorra los dos parametros dados como lista
# for nombre, edad in zip(nombres, edades):
   # print(f"{nombre} tiene {edad} año")
#########################################################
#nums = [1, 2, 3, 4, 5]
#for numero in range(1,len(nums)):
#   nums[numero] = nums[numero] + nums[numero - 1]      
#print(nums)
######################################################

#dado un array de enteros  arr y un entero k, encuentre el menor numero de enteros unicos depues
#depues de eliminar exactamente k de elementos
arr = [4,3,1,1,3,3,2]
ordenado = []
conteo=[]
for x in arr:
   if x not in ordenado:
      contador = 0
      for y in arr:
         if y == x:
            contador += 1
      conteo.append(contador)
      ordenado.append(x)
print(conteo)
# conteo=[1,3,2,1]
n=len(conteo)
for i in range(n):
   #range(es para que en cada recorido ya no cuente el ultimo indice)
   for j in range(0,n-i-1):
      if conteo[j] > conteo[j+1]:
         conteo[j],conteo[j+1]=conteo[j+1],conteo[j]
print(conteo)
nuevo_conteo = []
k = 1
suma = 0
for i in range(0,len(conteo)):
   suma += conteo[i] 
   if suma > k:
      nuevo_conteo.append(conteo[i])
   elif suma == k:
      nuevo_conteo.append(conteo[i])
      break
print(len(nuevo_conteo))


frec = Counter(arr)
      conteos = sorted(frec.values())  # ordena frecuencias (más eficiente)
        
        i = 0
        while i < len(conteos) and k >= conteos[i]:
            k -= conteos[i]
            i += 1
        
        return len(conteos) - i