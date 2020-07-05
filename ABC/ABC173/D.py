n=int(input())
a=list(map(int,input().split()))

a=sorted(a,reverse=True)
if n==2:
    print(max(a))
    exit(0)

ans=a[0]
a=a[1:]
from math import floor

for i in range(n-2):
    index=floor(i/2)
    ans+=a[index]

print(ans)



