n,k=map(int,input().split())

ans= 0
from math import ceil,log2

for i in range(1,n+1):
    if i<k:
        a = ceil(log2(k/i))
        ans +=(1/n)*(1/2)**a
    else:
        ans += (1/n)

print(ans)
