import utils

keys, value = utils.get_population()

print(keys, value)

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

country = input('Type country => ')

result = utils.population_by_country(data, country)
print(result)

print(utils.a)

