import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

a_del = np.delete(a, 1, 0)
print(a_del)

print(a)