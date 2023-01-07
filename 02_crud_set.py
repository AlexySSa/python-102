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