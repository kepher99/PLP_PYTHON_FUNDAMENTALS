list_a = [1,2,3,4,5]
#        0 1 2 3 4 
#print(list_a)
list_a[0] = 10
list_a.insert(len(list_a),6)
list_a.append(7)
list_a.extend([8,9])
list_a.pop(8)
del list_a[7]

for item in list_a:
  print(item)
