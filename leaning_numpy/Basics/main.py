import numpy as np
a = np.arange(15)
print(a)
a= a.reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
a = type(a)
print(a)
b= np.array([6,7,8])
print(b)
b = type(b)
print(b)


