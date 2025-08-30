'''Write a Python code that takes an integer input from the user, and checks if the 
number is even or odd using if-else. Print "Even" or "Odd" as output.   '''

def even_odd(num):
    if num % 2==0:
        return "Even"
    else:
        return "Odd"
    
print(even_odd(num))    
