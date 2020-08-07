n=int(input())
a=list(map(int,input().split()))

import numpy as np

c=np.cumsum(a)
s=sum(a)

ans=float('inf')
index=0
for i in range(n):
    if abs(2*c[i]-s)<ans:
        ans=abs(2*c[i] - s)
        index = i

print(ans)