import pandas as pd
df =pd.read_csv("Position_Salaries.csv")
x=df.iloc[:,1:2].values
y=df.iloc[:,2].values

from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=5)
poly_x=pf.fit_transform(x)

from sklearn.linear_model import LinearRegression

rg=LinearRegression()
rg.fit(poly_x,y)

p_data=pf.transform([[8.3]])
sal=rg.predict(p_data)
print("Salary=",sal)

import matplotlib.pyplot as plt
plt.plot(x,y,'r*')
pr=rg.predict(poly_x)
plt.plot(x,pr)
plt.xlabel("Lavel")
plt.ylabel("Sal")
plt.show()