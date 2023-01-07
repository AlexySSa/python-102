#no se pueden poner elementos duplicados
set_contries = {'colombia', 'mexico', 'bolivia'}
print(set_contries)
print(type(set_contries))

set_numbers = {1, 2, 3, 4, 5, 6, 2, 7, 8, 9, 10}
print(set_numbers)
print(type(set_numbers))

set_type = {1, 'hola', False, 12.12}
print(set_type)
print(type(set_type))
# un conjunto o set no tiene ningun orden
set_from_string = set('hoola')
print(set_from_string)
print(type(set_from_string))

set_from_tuples = set(('abc', 'cbs', 'de', 'abc'))
print(set_from_tuples)
print(type(set_from_tuples))

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
print(type(set_numbers))

unique_numbers = list(set_numbers)
print(unique_numbers)
print(type(unique_numbers))