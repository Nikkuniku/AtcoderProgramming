A,B,C=map(int,input().split())

import numpy as np
import math
def f(t):
    return A*t + B*math.sin(C*t*math.pi)-100


l=0
r=l
for i in np.arange(0.1,102.1,0.1):
    if f(i)>0:
        r=i
        break


t=l+(r-l)/2

while abs(f(t))>=0.0000001:
    t=l+(r-l)/2

    if f(l)*f(t)>0:
        l=t
    elif f(r)*f(t)>0:
        r=t

print(t)

