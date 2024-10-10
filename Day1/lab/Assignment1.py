import numpy as np
from math import sqrt,ceil
from numpy import random

print("\n1. Write a NumPy program to get the numpy version and show numpy build configuration.")
print(np.__version__)


print("\n2. Write a NumPy program to get help on the add function.")
print(help(np.add))


print("\n3. Write a NumPy program to test whether none of the elements of a given array is zero.")
arr1 = np.array([1,2,3,0,3])
print(np.all(arr1))

arr2 = np.array([1,2,3,np.nan,367])
print(np.isnan(arr2))


print("\n4. Write a NumPy program to test whether any of the elements of a given array is non-zero.")
arr3 = np.array([1, 0, 0, 1, 0, 2])
print(np.any(arr3))


print("\n5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).")
arr4 = np.array([1,np.inf,3,np.nan,367])
print(np.logical_or(np.isnan(arr4), np.isinf(arr4)))


print("\n6. Write a NumPy program to test element-wise for positive or negative infinity.")
arr5 = np.array([1, np.inf, 3, -np.inf, 367])
print(np.logical_or(np.isposinf(arr5), np.isneginf(arr5)))
print(np.logical_not(np.isfinite(arr5)))


print("\n7. Write a NumPy program to test element-wise for NaN of a given array.")
arr6 = np.array([1,np.nan,3,np.nan,367])
print(np.isnan(arr6))


print("\n8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.")
print(np.iscomplex([1+1j, 1+0j, 4.5, 3, 2, 2j]))
print(np.isreal([1+1j, 1+0j, 4.5, 3, 2, 2j]))
print(np.apply_along_axis(func1d=np.isscalar,axis=0 , arr = np.array([3.1,2,4,1.1])))


print("\n9. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.")
arr7 = np.random.randint(1,100,10)
arr8 = np.random.randint(1,100,10)
print("greater -> ",np.greater(arr7,arr8))
print("less -> ",np.less(arr7,arr8))
print("greater_equal -> ",np.greater_equal(arr7,arr8))
print("less_equal -> ",np.less_equal(arr7,arr8))


print("\n10. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.")
arr9 = np.array([1, 7, 13, 105], dtype=np.float64)
print("size -> ", arr9.size)
print("itemsize -> ", arr9.itemsize)
print("size*itemsize -> ", arr9.size*arr9.itemsize)

print("\n11. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.")
print(np.zeros(10,dtype=np.int32))
print(np.ones(10,dtype=np.int32))
print(np.full(10,5,dtype=np.int32))


print("\n12. Write a NumPy program to create an array of the integers from 30 to70.")
print(np.arange(start=30,stop=71,step=1, dtype=np.int32))

print("\n13. Write a NumPy program to create an array of all the even integers from 30 to 70.")
print(np.arange(start=30,stop=71,step=2, dtype=np.int32))


print("\n14. Write a NumPy program to create a 3x3 identity matrix.")
print(np.eye(3))

print("\n15. Write a NumPy program to generate a random number between 0 and 1.")
print(np.random.random())

print("\n16. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.")
print(np.random.normal(0, 1, 15))
# print(np.random.random_sample(15))


print("\n17. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.")
print(np.arange(15, 55)[1:-1])


print("\n18. Write a NumPy program to create a 3X4 array.")
print(np.random.random((3,4)))
print(np.arange(1,13).reshape(3,4))


print("\n19. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.")
print(np.linspace(5, 50, 10))

print("\n20. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.")
arr10 = np.arange(0,20)
arr10[9:16] = -1*arr10[9:16]
print(arr10)

print("\n21. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.")
print(np.random.randint(0, 11, 5))

print("\n22. Write a NumPy program to multiply the values of two given vectors.")
arr11 = np.random.randint(1,12,5)
arr12 = np.random.randint(1,12,5)
print(f'{arr11}*{arr12}={arr11*arr12}')

print("\n23. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.")
print(np.random.randint(10,21,12).reshape(3,4))

print("\n24. Write a NumPy program to find the number of rows and columns of a given matrix.")
print(np.full((3,4), np.random.random()).shape)


print("\n25. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.")
# 1
print(np.eye(3))
# 2
arr13 = np.zeros(9).reshape(3,3)
np.fill_diagonal(arr13,1)
print(arr13)

print("\n26. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.")
# 1
temp1 = np.pad(np.zeros((8,8)),1,mode='constant',constant_values=1)
print(temp1)
# 2
temp2 = np.ones((10,10))
temp2[1:-1,1:-1] = 0
print(temp2)

print("\n27. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5.")
arr14 = np.zeros((5,5))
np.fill_diagonal(arr14,np.arange(1,6))
print(arr14)

print("\n28. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.")
arr15 = np.random.randint(low=0, high=100,size=27).reshape(3,3,3)
print(arr15)

print("\n29. Write a NumPy program to compute the inner product of two given vectors.")
arr17 = np.random.randint(low=0, high=10,size=9).reshape(3,3)
arr16 = np.random.randint(low=0, high=10,size=9).reshape(3,3)
print(arr16, arr17, sep='\n')
print(np.dot(arr16,arr17))
print(np.inner(arr16,arr17))



print("\n30. Write a NumPy program to sort a given array by row and column in ascending order.")
arr20 = np.random.randint(low=0, high=30,size=9).reshape(3,3)
print(arr20)
print(np.sort(arr20,axis=0))  # Row wise
print(np.sort(arr20,axis=1))  # Column wise wise
print(np.sort(np.sort(arr20,axis=0),axis=1))  # Row the column both



print("\n31. Write a NumPy program to extract all numbers from a given array which are less and greater than a specified number.")
limit = 12
arr21 = np.random.randint(low=0, high=30,size=9).reshape(3,3)
print("Original -> \n",arr21)
print(f"Which are greater than limit {limit} -> \n", arr21> limit)
print(f"Greater than limit {limit} values -> \n", arr21[arr21> limit])

print("\n32. Write a NumPy program to replace all numbers in a given array which is equal, less and greater to a given number.")
value = 11
limit = 12

arr22 = arr21.copy()
arr22[arr22 == limit] = value
print(arr22)

arr22 = arr21.copy()
arr22[arr22 < limit] = value
print(arr22)

arr22 = arr21.copy()
arr22[arr22 > limit] = value
print(arr22)


print("\n33. Write a NumPy program to create an array of equal shape and data type of a given array.")
nums = np.random.randint(low=0, high=30,size=9).reshape(3,3)
temp3 = np.full_like(nums,2)
print("\nNew array of equal shape and data type :\n",temp3)
print(temp3.shape, temp3.dtype)



print("\n34. Write a NumPy program to create a three-dimension array with shape (3,5,4) and set to a variable.")
shape = (3,5,4)
arr23 = np.arange(1,shape[0]*shape[1]*shape[2]+1).reshape(shape)


print("\n35. Write a NumPy program to multiply two given arrays of same size element-by-element.")
arr24 = np.random.randint(low=0, high=10,size=9).reshape(3,3)
arr25 = np.random.randint(low=0, high=10,size=9).reshape(3,3)
print(arr24, arr25, sep='\n')
print(arr24*arr25)