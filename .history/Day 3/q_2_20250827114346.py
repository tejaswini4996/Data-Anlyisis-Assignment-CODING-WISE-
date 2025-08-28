'''
3 val ip float
max
min


hw
arr1 = ele 5
arr2= ele 5
 mean of arr1
 mean of arr2

 arr av value?
 arr1 avg> arr2

'''
# que 1
import numpy as np
x1=float(input())
x2=float(input())       
x3=float(input())

min_val=np.min([x1,x2,x3])      
max_val=np.max([x1,x2,x3])   

print("min:",min_val)
print("max:",max_val)


#que 2

arr1=[5]
arr2=[5]
mean1=np.mean(arr1)
mean2=np.mean(arr2) 

if mean1>mean2:
     print("mean1")
else:
    print("mean2")






