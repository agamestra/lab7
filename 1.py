import math
x1=1
x2=10
x3=1000
def y(x):
    y=math.log(1+x**2,(math.e**(1/(math.sin(x)+1))/(1.25+x**15)))
    print (y)
y(x1)
y(x2)
y(x3)