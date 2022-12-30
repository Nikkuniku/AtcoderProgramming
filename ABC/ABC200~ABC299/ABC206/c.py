n=int(input())
a=list(map(int,input().split()))


from operator import countOf, mul
from functools import reduce
from collections import Counter


def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

total = n*(n-1)//2

c=Counter(a)

C = list(c.values())
for i in range(len(C)):
    if C[i]>=2:
        total-=cmb(C[i],2)

print(total)