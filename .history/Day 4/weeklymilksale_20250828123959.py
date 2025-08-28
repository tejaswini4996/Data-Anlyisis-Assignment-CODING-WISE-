'''E1: Weekly Milk Sales (5 Marks)
A dairy shop records litres of milk sold each day:
csharp
Copy10, 12, 9, 11, 13, 8, 14
Tasks:
 Create a DataFrame with columns  day ( Mon,  Tue, ...,  Sun) and  litres. Display the first 3 rows. Print the DataFrameʼs shape, columns, and dtypes.
Show your code and its output'''


import pandas as pd
data = {
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'litres': [10, 12, 9, 11, 13, 8, 14]
}   
df = pd.DataFrame(data)
print(df.head(3))
print("DataFrame Shape:", df.shape)
print("DataFrame Columns:", df.columns)
print("DataFrame dtypes:\n", df.dtypes)         