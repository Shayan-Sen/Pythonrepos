import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")
x = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values
from sklearn.preprocessing import LabelEncoder

en1 = LabelEncoder()
x[:, 1] = en1.fit_transform(x[:, 1])

en2 = LabelEncoder()
x[:, 2] = en2.fit_transform(x[:, 2])

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size=.25, random_state=42)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(128, input_dim=10, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam",
              metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=10, epochs=5)

y_pred = model.predict(x_test)
y_pred1 = y_pred > .5

a, ac = model.evaluate(x_test, y_test)
print("Accuracy=", ac)
print(model.predict(sc.transform([[619, 0, 0, 42, 2, 40000, 1, 1, 1, 101348]])))