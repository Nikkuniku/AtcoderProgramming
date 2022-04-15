n,k,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)

for i in range(n):
    c=a[i]//x
    if c>k:
        c=k
    a[i]-=x*c
    k-=c
a.sort(key=lambda p:p%x,reverse=True)
a.sort(reverse=True)
from math import ceil
for i in range(n):
    c=ceil(a[i]/x)
    if c>k:
        c=k
    a[i]-=x*c
    if a[i]<0:
        a[i]=0
    k-=c
    if k==0:
        break

ans=sum(a)
print(ans)