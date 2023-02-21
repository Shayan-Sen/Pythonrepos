import numpy as np
import matplotlib.pyplot as plt
rng=np.random.RandomState(42)
x=rng.random(100)
y=rng.random(100)
cols=rng.random(100)
rad=rng.random(100)*1000

plt.scatter(x, y, c=cols, s=rad, alpha=0.9,
            cmap='ocean')

plt.show()