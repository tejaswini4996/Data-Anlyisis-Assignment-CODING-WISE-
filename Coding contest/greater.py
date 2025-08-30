'''Given a NumPy array  arr = np.array([3, 8, 1, 6, 0, 7, write code to count how many 
elements are greater than 4 '''


import numpy as np 
arr = np.array([3, 8, 1, 6, 0, 7])
count = np.sum(arr > 4)
print(count)
