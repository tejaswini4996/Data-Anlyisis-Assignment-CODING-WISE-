'''Write Python code to check if a given number is positive, negative, or zero 
using if-elif-else statements. Print the result.    '''


def pos_neg(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"       
print(pos_neg(0))    
