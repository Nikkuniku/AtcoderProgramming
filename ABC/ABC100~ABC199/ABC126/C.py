n,k = map(int,input().split())

from fractions import math

ans=0

if n>=k:
    ans += 1 - (k-1)/n

for i in range(1,n+1):
    if i<=k-1:
        exp = math.ceil(math.log2(k/i))
        p_i = (1/n) * ((1/2)**exp)
        ans += p_i

print(ans)