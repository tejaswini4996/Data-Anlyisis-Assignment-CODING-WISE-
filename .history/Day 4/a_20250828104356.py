import pandas as pd 
#sample dataset
data={ "Name":["Tejas","Sweety","Tejaswini","ABC","XYZ","PQR","LMN","EFG","HIJ","KLM"],
      "Age":[25,27,28,24,26,29,30,31,32,33],
      "Salary":[50000,60000,70000,80000,90000,100000,110000,120000,130000,140000]
}
df=pd.DataFrame(data)
df["Bonus"]=df["Salary"]*0.10
df["Salary"] = df["Salary"] + 5000

print(df)
print(df.shape)
print(df.info())
print(df.head())
print(df.tail())
