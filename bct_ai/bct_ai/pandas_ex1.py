import pandas as pd
s=pd.Series([11,22,33,44,5])
print(s)
print("##########################")
s1=pd.Series([11,22,33,44],index=['a','b','c','d'])
print(s1)
print("############################")
s2=pd.Series(7,index=['a','b','c','d'])
print(s2)
