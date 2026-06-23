inventario = {
   "manguera":   {"stock": 10,  "precio": 50},
   "fitting":    {"stock": 25,  "precio": 30},
   "conector":   {"stock": 8,   "precio": 15},
   "adaptador":  {"stock": 40,  "precio": 22},
   "valvula":    {"stock": 5,   "precio": 80},
   "abrazadera": {"stock": 100, "precio": 8},
   "niple":      {"stock": 60,  "precio": 12},
   "codo":       {"stock": 33,  "precio": 18},
   "tee":        {"stock": 17,  "precio": 25},
   "reduccion":  {"stock": 22,  "precio": 35},
}

inventario["manguera"]["precio"]=80
inventario["manguera_hidraulica"] = inventario.pop("manguera")
for producto,datos in inventario.items():
   print(producto)
   for c,v in datos.items():
      print(f"   {c}:{v}")
   

