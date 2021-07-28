n=int(input())
a=list(map(int,input().split()))
b=[]
import numpy as np
for i in range(n):
    b.append(a[i]/2)
b=sorted(b)
x=np.median(b)

ans=0
for i in range(n):
    ans+=min(a[i],2*x)

ans=x + (sum(a)/n)-(ans/n)
print(ans)