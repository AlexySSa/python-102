def increment(x):
  return x + 1

def hof(x, func):
  return x + func(x)

result = hof(2, increment)
# 2 + (2 + 1)
print(result)


#con lambdas

incremet_2 = lambda x : x + 1

hof_2 = lambda x, func: x + func(x)

result = hof_2(2, incremet_2)
# 2 + (2 + 1)
print(result)

result = hof_2(2, lambda x : x + 2)
print(result)

result = hof_2(2, lambda x : x * 5)
print(result)