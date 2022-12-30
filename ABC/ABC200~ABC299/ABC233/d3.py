n,k=map(int,input().split())
a=list(map(int,input().split()))

csum=0
from collections import defaultdict
ans=0
d=defaultdict(int)
for i in range(n):
    d[csum]+=1
    ans+=d[csum-k]
print(ans)