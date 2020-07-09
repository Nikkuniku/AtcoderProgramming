n=int(input())
s=input()
mod=10**9+7
from collections import Counter

c=list(Counter(s).values())

ans=1

for i in c:
    ans*=(i+1)

print((ans-1)%mod)
