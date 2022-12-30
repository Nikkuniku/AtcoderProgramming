n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

from collections import Counter
c=Counter(a)

ans='Yes'
for p in b:
    if p not in c:
        c[p]=-1
    else:
        c[p]-=1

for k in list(c.values()):
    if k<0:
        ans='No'
print(ans)