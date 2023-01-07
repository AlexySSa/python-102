'''

numbers = []
for element in range(1, 11):
  numbers.append(element * 2)
  
print(numbers)   #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numbers_v2 = [i * 2 for i in range(1, 11)]
print(numbers_v2)   #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
   numbers.append(i * 2)
  
print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)
