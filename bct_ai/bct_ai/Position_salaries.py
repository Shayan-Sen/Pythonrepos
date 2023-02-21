import pandas as pd
df =pd.read_csv("Position_Salaries.csv")
x=df.iloc[:,1:2].values
y=df.iloc[:,2].values

from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=4)
poly_x=pf.fit_transform(x)