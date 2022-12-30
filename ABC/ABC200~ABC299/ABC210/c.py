n,k=map(int,input().split())
c=list(map(int,input().split()))
from collections import deque

q=deque()
i=0
d={}
ans=0
tmp=0
while i<=n-1:
    if len(q)>=k:
        v=q.popleft()
        d[v]-=1
        if d[v]==0:
            tmp-=1

    q.append(c[i])
    if c[i] in d:
        d[c[i]]+=1
        if d[c[i]]==1:
            tmp+=1
    else:
        d[c[i]]=1
        tmp+=1

    ans= max(ans,tmp)
    i+=1

print(ans)