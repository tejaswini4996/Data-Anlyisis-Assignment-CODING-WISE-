'''Take 3 exam scores from the user. If the average is more than 90, print “Grade 
Aˮ. Else print “Grade Bˮ.
Hint: Use np.mean() + if-else'''

import numpy as np
arr = np.array([int(i) for i in input().split()]) 
      
if arr.size == 0:
    print("No scores provided")
elif np.mean(arr)>90:
    print("Grade A")    
else:
    print("Grade B")        

'''Ask the user for 2 ages. Find which is larger using NumPy.
Hint: Use np.max()'''

import numpy as np
arr = np.array([int(i) for i in input().split()]) 
print(np.max(arr))  


'''Create an array of 3 numbers. If all numbers are even, print Even array. 
Otherwise, print Mixed.
Hint: Use % 2 with if-else'''

import numpy as np
arr = np.array([int(i) for i in input().split()])       
if np.all(arr%2==0):
    print("Even array")                 
else:
    print("Mixed")  


    '''Ask the user to enter 2 salaries. Print both and show their difference.
Hint: Use np.subtract()'''

import numpy as np
arr = np.array([int(i) for i in input().split()])       
print(arr)
print(np.subtract(arr[0],arr[1]))           


'''Create an array of  3, 6, 9. Multiply every element by 10.
Hint: Use * operator'''

import numpy as np
arr = np.array([3,6,9])             
print(arr*10)   

'''Take 3 floating-point numbers from the user. Convert them into integers using 
NumPy.
Hint: Use .astype(int)'''

import numpy as np
arr = np.array([float(i) for i in input().split()]) 
print(arr.astype(int))

