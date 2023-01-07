set_contries = {'colombia', 'mexico', 'bolivia'}

size = len(set_contries)
print(size)

print('colombia' in set_contries)
print('peru' in set_contries)

#add
set_contries.add('peru')
print(set_contries)
set_contries.add('peru')
print(set_contries)

#update
set_contries.update({'argentina', 'chile', 'peru'})
print(set_contries)

#remove

set_contries.remove('colombia')
print(set_contries)

set_contries.remove('argentina')
#discard sirve igual que el remove pero no tira ningun error durante el proceso
set_contries.discard('argentinas')
print(set_contries)

set_contries.add('argentina')
print(set_contries)

set_contries.clear()
print(len(set_contries))