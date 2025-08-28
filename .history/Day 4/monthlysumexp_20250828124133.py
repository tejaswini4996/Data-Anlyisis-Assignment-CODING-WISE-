'''E2: Monthly Expenses Summary (5 Marks)
You track your January expenses:
category amount ₹rent 15 000food 8 000utilities 2 000transport 3 000
Tasks:
 Create a DataFrame with this data. Use a single pandas command to compute total, average, maximum, 
and minimum expense. Print the results clearly. Day 4 Pandas Basics  Assignment 40 Marks)3 '''

import pandas as pd
data = {
    'category': ['rent', 'food', 'utilities', 'transport'],
    'amount': [15000, 8000, 2000, 3000]
}   
df = pd.DataFrame(data)
summary = df['amount'].agg(['sum', 'mean', 'max', 'min'])       
print("Expense Summary:")
print(summary)      

