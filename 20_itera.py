for i in range(1, 11):
  print(i)

my_iter = iter(range(1, 6))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) #tira error si me paso del range dado