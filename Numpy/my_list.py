import numpy as np
my_list = [1,2,3,4]
my_list = my_list *2
print(my_list)

array = np.array([1,2,3,4])
array = array * 2
print(array)
print(type(array))
name = "hawi"
print(type(name))


array3 = np.array([1,2,3,4])
print(array3)


arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3,4])
print(arr1 + arr2)   #fofr this to work it must b the same shape or we must use broadcasting 