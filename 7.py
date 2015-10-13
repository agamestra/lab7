import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import mlab
import math
x=np.arange(-2,2.01,0.001)
def w(x):
    s=0
    for n in range (100):
        s+=(0.3**n)*np.cos(3**n*np.pi*x)
    return s
plt.plot(x, w(x))
plt.show()