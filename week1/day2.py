import numpy as np
ones = np.arange(12).reshape(4,3)
print(ones)
print(ones[1,2])
print(ones[:2]) #show all rows and column 2
print(ones[:2,1])# show all rows column 2 and all column row 1
mask = ones > 5
print(mask)
print(ones[mask])
mask2 = (ones > 3) & (ones <8)
print(ones[mask2])
#the where function
array1 = np.array([1,2,3,-2,-4])
positive = np.where(array1>2,array1,0)
print(positive)