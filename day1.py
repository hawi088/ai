import numpy as np 
arr1 = np.array([1,2,3,4,5])
print(arr1.shape)
arr2 = np.array([[1,2,3],[4,56,7]])
print(arr2)
print(arr2.shape)

zeros = np.zeros((2,3))
ones = np.ones((2,3))
print(ones)

ranging = np.arange(10)
print(ranging)
print(ranging.shape)
print(ranging.size)
print(ranging.ndim)

 ##line space formula step  = (End - start) / stepsize -1
# #then point0 = start + 0 * steps
# #point1 = start +1 * step
# #point2 = start + 2 * step

# #identity matrix 
idntity = np.eye(4)
print(idntity)

 #random generation
np.random.seed(43)
array1 = np.random.rand(3,4)
print(array1)