items = [
  {
    'producto': 'camisa',
    'price': 100
  },
  {
    'producto': 'pantolones',
    'price': 300
  },
  {
  
    'producto': 'pantolones_2',
    'price': 200
  }
]

def add_IVA(item):
  new_item = item.copy()
  new_item['IVA'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_IVA, items))
print('new list')
print(new_items)
print('old list')
print(items)

'''
tiene como objetivo no crear efectos secundarios creando una copia del input, modificando y luego retornando esta copia modificada
'''