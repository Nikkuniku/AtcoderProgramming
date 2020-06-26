n=int(input())
d=list(map(int,input().split()))
mod=998244353
from collections import Counter

c=dict(Counter(d))
c=sorted(c.items(),key=lambda x: x[0])


if d[0]!=0:
    print(0)
    exit(0)

if c[0][1]!=1:
    print(0)
    exit(0)

for i in range(1,len(c)):
    if c[i][0]!=c[i-1][0]+1:
        print(0)
        exit(0)

ans=1
for i in range(1,len(c)):
    ans*=c[i-1][1]**(c[i][1])

print(ans%mod)
        