import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import mlab
import math
tlist = mlab.frange (-10, 10, 0.005)
alist = mlab.frange (-10, 10, 0.005)

pylab.ion()

for n in range (500):
        a=n/20
        xlist = [np.sin(t+a) for t in tlist]
        ylist = [np.cos(2*t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()