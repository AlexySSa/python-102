file = open('./text.txt')
#print(file.read()) #este lee todo el aarchivo de un solo
#print(file.readline()) #este va linea por linea
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
  print(line)

file.close() #siempre debemos cerrar

with open('./text.txt') as file: #este wey cierra automaticamente 
  for line in file:
    print(line)