import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,2,30)
y=np.sin(x)

plt.plot(x, y, '-p',
         color='gray',
         markersize=12,
         linewidth=4,
         markerfacecolor='red',
         markeredgecolor='gray',
         markeredgewidth=2                 
         )
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.show()



