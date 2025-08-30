''' Create a NumPy array with values from 1 to 10. Find the mean, maximum, and 
minimum of the array. Print each result. '''

import numpy as np
arr = np.arange(1, 11)
mean_val = np.mean(arr)     
max_val = np.max(arr)
min_val = np.min(arr)
print("Mean:", mean_val)
print("Max:", max_val)      
print("Min:", min_val)

