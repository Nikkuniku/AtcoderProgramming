l,r=map(int,input().split())
from math import gcd
ans=0
for a in range(l,min(l+1500,r)):
    for b in range(max(r-1500,l+1),r+1):
        if gcd(a,b)==1:
            ans=max(b-a,ans)
print(ans)
