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



