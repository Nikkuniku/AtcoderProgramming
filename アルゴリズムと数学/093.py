a,b=map(int,input().split())
from math import gcd
ab=a*b
lcm=ab//gcd(a,b)

ans=lcm
if ans>10**18:
    ans='Large'
print(ans)