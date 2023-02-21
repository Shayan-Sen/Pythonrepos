import numpy
import matplotlib.pyplot as plt
#numpy.random.uniform(<initial>,<final>,<no_of_values>)
x=numpy.random.uniform(0.0,5.0,1000)
#x=dataset;5 bars
plt.hist(x,100)
plt.show()
#normal_value,gap,no_of_values
x=numpy.random.normal(0.0,5.0,1000)
plt.hist(x,100)
plt.show()
