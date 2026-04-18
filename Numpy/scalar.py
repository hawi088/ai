import numpy as np
import time
size = 1000000
arr1 = np.random.rand(size)
arr2 = np.random.rand(size)
start = time.time()
result_scalar=[]
for i in range(size):
    result_scalar.append(arr1[i]+arr2[i])
scalar_time = time.time() - start
print(scalar_time)

start = time.time()
result_vectorized = arr1 + arr2
vectorized_time = time.time() - start
print(vectorized_time)



#weather

temps = np.array([72, 68, 75, 80, 77, 70, 65])
hot_days = temps > 75

print(temps[hot_days])

#ages and incomes
ages = np.array([25, 32, 19, 45, 31, 28, 52])
incomes = np.array([45000, 52000, 25000, 80000, 48000, 35000, 95000])

age_25_35 = (ages >25) & (ages < 35)
print(ages[age_25_35])

age_income = (ages > 30) | (incomes > 50000)
print(ages[age_income],incomes[age_income])