''' Take 3 marks from user, find average, and check if student passed >=40
Hint: Use np.mean() + if-else
'''

import numpy as np
marks = []
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)
avg = np.mean(marks)
if avg >= 40:
    print("Passed")     
else:
    print("Failed")     

    



   ''' Take 3 numbers, find maximum, and check if it is greater than 100.
Hint: Use np.max() + if-else '''

import numpy as np
numbers = []    
for i in range(3):
    num = int(input("Enter number: "))
    numbers.append(num)             
max_num = np.max(numbers)
if max_num > 100:                   
    print("Greater than 100")
else:
    print("Not greater than 100")  


         '''Take 5 numbers as input, check if the array size is greater than 4.
Hint: Use .size + if-else
'''

import numpy as np
numbers = []       
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)                 
arr = np.array(numbers)
if arr.size > 4:                    
    print("Array size is greater than 4")           
else:
    print("Array size is not greater than 4")           

    '''Compare averages of two arrays given by user and print which is higher.
Hint: Use np.mean() + if-else'''

import numpy as np  
arr1 = []
arr2 = []  
for i in range(3):
    num1 = int(input("Enter number for array 1: "))
    arr1.append(num1)                 
    num2 = int(input("Enter number for array 2: "))
    arr2.append(num2)
arr1 = np.array(arr1)
arr2 = np.array(arr2)           
avg1 = np.mean(arr1)
avg2 = np.mean(arr2)                

if avg1 > avg2:                    
    print("Average of array 1 is higher")           
elif avg1 < avg2:
    print("Average of array 2 is higher")   

else:
    print("Averages are equal")         

    


    '''Create an array of 3 numbers. If the minimum value is less than 0, print 
“Negative number existsˮ.
Hint: Use np.min() + if-else '''

import numpy as np
numbers = []            
for i in range(3):
    num = int(input("Enter number: "))
    numbers.append(num)             
arr = np.array(numbers)
min_num = np.min(arr)   
if min_num < 0:                    
    print("Negative number exists")
else:
    print("No negative numbers")


                        

