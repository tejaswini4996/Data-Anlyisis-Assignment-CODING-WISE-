'''user 5 int value
create arr 
mean 
 > 50 
 value is greater than 50 
 <50else less than 50
'''

import numpy as np
arr= input("Enter 5 integer values separated by space: ")
arr = np.array(list(map(int, arr.split())))
mean_value = np.mean(arr)
if mean_value > 50:
    print("Mean value is greater than 50")  
else:
    print("Mean value is less than or equal to 50")    
