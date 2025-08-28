#Section A – Array Creation & Basics

'''Take 3 numbers from the user and store them in a NumPy array. Print the 
array.
Hint: Use np.array() with input() '''

import numpy as np
arr=np.array([int(input("Num1:")),int(input("Num2:")),int(input("Num3:"))])
print(arr)


'''Create a 1D array of 5 integers using NumPy. Print its size.
Hint: Use .size '''

import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr.size)

'''Create a 23 array filled with zeros.
Hint: Use np.zeros((rows, cols)) '''

import numpy as np
arr=np.zeros((2,3))
print(arr)

''' Create a 32 array filled with ones  Hint: Use np.ones((rows, cols)'''

import numpy as np
arr=np.ones((3,2))
print(arr)  

'''Take 2 integers from the user and create an array. Print its shape.
Hint: Use .shape '''

import numpy as np
arr = np.array([int(input('num1:')), int(input('num2:'))])
print(arr.shape)


