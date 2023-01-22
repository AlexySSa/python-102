with open('./text.txt', 'w+') as file: #este wey cierra automaticamente 
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea nueva\n')
  file.write('otra linea nueva mas\n')