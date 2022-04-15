import numpy as np
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
a=list(reversed(a))
c=list(reversed(c))

p=np.poly1d(a)
q=np.poly1d(c)
r=q/p
print(*list((map(int,list(reversed(list(r[0].c)))))))