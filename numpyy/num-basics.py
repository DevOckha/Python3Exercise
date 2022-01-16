import numpy as np




py_list = [1,2,3,4,5,6,7,8,9]



# numpy array
nparray = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(nparray))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]

np_multi = nparray.reshape(3,3)

print(py_multi)
print(np_multi)