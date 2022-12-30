from sys import stdin
from decimal import Decimal
from math import ceil
r,x,y=map(int, stdin.readline().split())

D=(x**2 + y**2)**(1/2)

ans=int(-(-D//r))
if D<r:
    ans=2

print(ans)