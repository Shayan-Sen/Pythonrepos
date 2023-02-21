from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris=datasets.load_iris()
X=iris['data']
Y=iris['target']
logit=LogisticRegression(max_iter=10000)

C=[0.25,0.5,0.75,1,1.25,1,5,1,75,2]
scores=[]

for choice in C:
    logit.set_params(C=choice)
    logit.fit(X,Y)
    scores.append(logit.score(X,Y))

print(scores)