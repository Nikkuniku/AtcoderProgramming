n=int(input())
a=list(map(int,input().split()))
mod = 200

for i in range(n):
    a[i]=a[i]%mod

from operator import countOf, mul
from functools import reduce
from collections import Counter

c=Counter(a)

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

k = list(c.values())

ans=0
for j in k:
    if j>=2:
        ans+=cmb(j,2)

print(ans)