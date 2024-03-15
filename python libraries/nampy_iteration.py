import numpy as np
a = np.arange(0,72,6)
a = a.reshape(3,4)
print('original array is:')
print(a)
print('\n')
print('modified array is:')
for x in np.nditer(a):
  print(x)