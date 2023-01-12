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
prices = list(map(lambda item: item['price'], items))
print(prices)

def add_IVA(item):
  item['IVA'] = item['price'] * .19
  return item

new_items = list(map(add_IVA, items))
print(new_items)