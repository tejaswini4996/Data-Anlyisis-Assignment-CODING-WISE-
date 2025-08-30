'''Create a pandas DataFrame with columns "Product" Rice, Sugar, Oil), and 
"Price" 50, 40, 100. Display the first row and use pandas to find the average 
price'''

import pandas as pd 

data={'Product': ['Rice', 'Sugar', 'Oil'], 'Price': [50, 40, 100]}
df = pd.DataFrame(data)
print(df.iloc[0])