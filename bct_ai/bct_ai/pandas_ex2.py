import pandas as pd
df=pd.read_csv("Income_data.csv")
print(df)
df2=df.set_index("State")
df3=df2.loc["Alabama":"Arizona","2005":"2007"]
df4=df2.iloc[0:3,1:4]
df5=df2.iloc[0:3,[2,4,6]]
df6=df2.loc["California","2005":"2013"]
print("Total Sales amount:",df6.sum())
ark_sales=df2.loc["Arkansas","2007"]
print("Arkansas sales amount fro 2007:",ark_sales)
print("out:",df2.iloc[3,3])
df7=df2.iloc[:,1:4]
y_sum=df7.sum(axis=0)
s_sum=df7.sum(axis=1)
