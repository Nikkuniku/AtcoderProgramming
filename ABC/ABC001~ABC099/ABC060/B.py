a,b,c=map(int,input().split())

from math import gcd

g=gcd(a,b)

if c%g==0:
    print('YES')
else:
    print('NO')