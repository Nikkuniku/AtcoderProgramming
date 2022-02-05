n=int(input())

ans=0

from math import floor

for i in range(1,floor(n**0.5)+1):
    ans+=floor(n/i)
    ans-=i

ans*=2
ans+=floor(n**0.5)
print(ans)