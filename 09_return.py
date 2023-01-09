def buscar_volumen(lenth=1, width=1, depth=1):
  return lenth * width * depth, width, 'hola' #puedes retornar multiple valores solo con una coma

#result = buscar_volumen(10, 20, 3)
result, width, text = buscar_volumen(width=10)

#print(result[0])
print(result)
print(width)
print(text)