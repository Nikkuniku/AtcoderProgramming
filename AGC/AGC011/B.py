n=int(input())
a=list(map(int,input().split()))
a=sorted(a)

import numpy as np
cum=list(np.cumsum(a))

cnt=0
for i in range(n-1,-1,-1):
    if i==n-1:
        cnt+=1
        continue

    if 2*cum[i]>=a[i+1]:
        cnt+=1
    else:
        break

print(cnt) 

