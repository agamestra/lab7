import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10.01,0.01)
fl=0
def y(x):
    return x*x-6-x

plt.plot(x,y(x))
for i in range (1000):
    if (x[i]*x[i]-6-x[i])==0:
        print(x[i])
        fl=1
if fl==0:
    print ("no")
plt.show()
