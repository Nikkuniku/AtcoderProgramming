a,b,c=map(int,input().split())
from math import gcd

g=gcd(gcd(a,b),c)

ans=0
for i in [a,b,c]:
    ans+=i//g-1
print(ans)