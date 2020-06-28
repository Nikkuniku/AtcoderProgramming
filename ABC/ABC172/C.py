n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

import numpy as np
import bisect

ra=[0]+list(np.cumsum(a))
rb=[0]+list(np.cumsum(b))

ans=0
for i in range(n+1):    
    capa = k - ra[i]
    if capa<0:
        break
    j=bisect.bisect_right(rb,capa)
    ans=max(ans,i-1+j)
            
print(ans)    