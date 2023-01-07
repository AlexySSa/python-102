'''

dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict) #{1: 2, 2: 4, 3: 6, 4: 8}

dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2) #{1: 2, 2: 4, 3: 6, 4: 8}



import random
paises = ['col', 'mex', 'bol', 'pe']
poblacion = {}
for pais in paises:
  poblacion[pais] = random.randint(1, 100)

  
print(poblacion) #{'col': 18, 'mex': 92, 'bol': 40, 'pe': 34}


poblacion_v2 = { pais: random.randint(1, 100) for pais in paises }
print(poblacion_v2) #{'col': 18, 'mex': 92, 'bol': 40, 'pe': 34}

'''

names = ['nico', 'jose','zule']
ages = [18, 20, 22]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)