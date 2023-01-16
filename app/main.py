import utils


data = [
  {
    'Country': 'Colombia',
    'population': 500
  },
  {
    'Country': 'Bolivia',
    'population': 300
  }
]
  

def run():

  keys, value = utils.get_population()
  
  print(keys, value)
  
  country = input('Type country => ')
  
  result = utils.population_by_country(data, country)
  print(result)
  
  print(utils.a)

if __name__ == '__main__':
  run()

  '''Este if dice que si es ejecutado desde la terminal, entre al run y si es ejecutado desde otro archivo, no se ejecuta.'''
  