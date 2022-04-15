n=int(input())
a=list(map(int,input().split()))
k=0
cumsum=[0]
for i in range(n):
    tmp=cumsum[-1]+a[i]
    cumsum.append(tmp)

from collections import defaultdict
d=defaultdict(lambda:0)

currsum=0
ans=0
for i in range(n):
    currsum+=a[i]

    if cumsum[i+1]==k:
        ans+=1

    if (cumsum[i+1]-k) in d:
        ans+=d[cumsum[i+1]-k]

    d[currsum]+=1

print(ans)