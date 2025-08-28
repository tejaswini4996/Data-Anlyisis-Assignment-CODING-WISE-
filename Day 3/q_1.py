'''user 5 int value
create arr 
mean 
 > 50 
 value is greater than 50 
 <50else less than 50
'''

import numpy as np
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))
arr = np.array([x, y, z])

mean_value = np.mean(arr)
if mean_value > 50:
    print("Mean value is greater than 50")  
else:
    print("Mean value is less than or equal to 50")    
