import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import mlab
import math
x=np.arange(-10,10.01,0.01)
tmin=-20
tmax=20
amin=-20
amax=20
x = np.sin(t+a)
y = np.cos(2*t)

dx = 0.01
dy=0.01
xlist = mlab.frange (tmin, tmax, dx)
ylist = mlab.frange (tmin, tmax, dy)

pylab.ion()

for n in range (50):
        ylist = [math.sin (x + n / 2.0) for x in xlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()