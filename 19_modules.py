#donde se ejecuta un archivo
import sys
print(sys.path)
#para expresiones regulares, aqui sacamos solo los numeros
import re
text = 'mi numero de telefono es 311 123 432, el codigo del pais es +503, mi numero de la suerte es el 2'
result = re.findall('[0-9]+', text)
print(result)
#la hora en formato unix
import time
timestamp = time.time()
print(timestamp)
#la hora en en lenguaje natural
local = time.localtime()
result = time.asctime(local)
print(result)
#saca repeticiones de una lista 
import collections
numbers = [1,2,1,1,5,3,1,2,2,3,4]
counter = collections.Counter(numbers)
print(counter)