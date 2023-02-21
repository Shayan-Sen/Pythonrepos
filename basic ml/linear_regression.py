import matplotlib.pyplot as plt
from scipy import stats
'''dataset list for X axis'''
#x=numpy.random.uniform(5.0,1.0,1000)
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
'''Dataset list for y axis'''
#y=numpy.random.uniform(10.0,2.0,1000)
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
slope,intercept,r,p,std_err=stats.linregress(x,y)
def myfunc(x):
    return slope*x+intercept
mymodel=list(map(myfunc,x))
#x-> X axis ; y-> Y axis
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()      
#slope--->slope of the line
#intercept--->value of y when x is zero in line
#r--->coefficient of correlation

