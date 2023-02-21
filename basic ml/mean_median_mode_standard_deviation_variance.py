import numpy
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x=numpy.mean(speed)
print(x)
x=numpy.median(speed)
print(x)
x=stats.mode(speed)
print(x)
x=numpy.std(speed)
print(x)
x=numpy.var(speed)
print(x)
x=numpy.percentile(speed,56)
print(x)

