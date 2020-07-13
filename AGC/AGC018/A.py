n,k=map(int,input().split())
a=list(map(int,input().split()))

import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

g=gcd(*a)
p=max(a)-k
ans='POSSIBLE'
if p>=0:
    if p%g!=0:
        ans='IMPOSSIBLE'
else:
    ans='IMPOSSIBLE'

print(ans)