n=int(input())
a=list(map(int,input().split()))

import numpy as np

a=sorted(a)
cum = np.cumsum(a)

cum=list(reversed(cum))
a=list(reversed(a))
ans=1
for i in range(1,n):
    if a[i-1]<=cum[i]*2:
        ans+=1
    else:
        break

print(ans)
