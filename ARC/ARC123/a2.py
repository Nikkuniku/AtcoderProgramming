a,b,c=map(int,input().split())
x=2*b-a-c
from math import ceil
k0 = max(0,ceil(-x/2))

ans=x + 3*k0

print(ans)