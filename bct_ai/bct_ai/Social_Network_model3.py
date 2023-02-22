import pandas as pd
df=pd.read_csv("Social_Network_Ads.csv")
x=df.iloc[:,2:4].values
y=df.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,
                            test_size=.3,random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x1_train=sc.fit_transform(x_train)
x1_test=sc.transform(x_test)

#######Linear SVM Classification:

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
####RBF SVM Classification:
#classifier = SVC(kernel = 'rbf', random_state = 0)
###### POLYNOMIAL########
#classifier = SVC(kernel = 'poly', random_state = 0,degree = 4)
######SIGMOID ############################
#classifier = SVC(kernel = 'sigmoid', random_state = 0)
classifier.fit(x1_train,y_train)
y_pred=classifier.predict(x1_test)

from sklearn.metrics import confusion_matrix
print("Confusion Matrix=",confusion_matrix(y_test,y_pred))

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)
print("Accuracy=",ac)