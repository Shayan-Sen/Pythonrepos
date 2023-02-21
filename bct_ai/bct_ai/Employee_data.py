import pandas as pd
df= pd.read_csv("Employee_Data.csv")
x=df.iloc[:,0:4].values
y=df.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder
en=LabelEncoder()
x[:,0]=en.fit_transform(x[:,0])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,
                    test_size=.3,random_state=1)

from sklearn.linear_model import LinearRegression
rg=LinearRegression()
rg.fit(x_train,y_train)
y_pred=rg.predict(x_test)

from sklearn import metrics
mse=metrics.mean_squared_error(y_test, y_pred)

import numpy as np
rmse=np.sqrt(mse)

print("RMSE=",rmse)

m=rg.coef_
print("M=",m)

c=rg.intercept_
print("C=",c)

'''Development,2400,1,3.4'''
s=rg.predict([[0,2400,1,3.4]])
print("Output :",s)