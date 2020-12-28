a=[2,4,6,8]

import bisect

j=bisect.bisect_right(a,2)

print(j)

import numpy as np
t=[]
for i in np.arange(0.1,100.1,0.1):
    t.append(i)

print(len(t))