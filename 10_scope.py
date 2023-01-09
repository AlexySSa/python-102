price = 100 #global variable

def increment():
  price = 200
  result = price + 10 #local
  print(result)
  return result

print(price)
price2 = increment()
print(price2)
print(result)