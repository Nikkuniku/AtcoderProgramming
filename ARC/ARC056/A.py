a,b,k,l=map(int,input().split())

from math import ceil
n=ceil(k/l)

ans=10**18
for i in range(n):
    j=k-l*i
    if j<0:
        continue
    ans=min(ans,j*a + i*b)

ans = min(ans,n*b)
print(ans)