''' Create a NumPy array  1, 2, 3, 4. Print its number of dimensions.
Hint: Use .ndim'''

import numpy as np 
arr = np.array([1, 2,3,4])
print(arr.ndim) 

'''Take 4 numbers as input, create an array, and print its data type.
Hint: Use .dtype'''

import numpy as np 
arr = np.array([int(i) for i in input().split()])
print(arr.dtype)    


''' Convert an integer array into float type.
Hint: Use .astype(float)  '''

import numpy as np 
arr = np.array([1, 2, 3, 4])
arr = arr.astype(float)
print(arr)
print(arr.dtype)    

