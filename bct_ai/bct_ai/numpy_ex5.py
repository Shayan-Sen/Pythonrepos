import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a)
print("#######################")
print(b)
print("######################")
c=a.dot(b)
print(c)
print("############################")
n=np.arange(12).reshape(3,4)
print(n)
print("Sum of all :",n.sum())
print("Row sum=",n.sum(axis=1))
print("Column sum=",n.sum(axis=0))
print("Max of all:",n.max())
print("Row wise max=",n.max(axis=1))
print("Column wise max=",n.max(axis=0))
print("Average of all=",n.mean())
print("Row wise average=",n.mean(axis=1))
print("Column wise average=",n.mean(axis=0))







