n=int(input())
from math import floor

ans=0
k0=floor(n**0.5)

for k in range(1,k0+1):
    ans+=(floor(n/k)-floor(n/(k+1)))*k

for i in range(1,floor(n/(k0+1))+1):
    ans+=floor(n/i)

print(ans)