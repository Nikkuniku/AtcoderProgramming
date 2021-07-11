n,k=map(int,input().split())
a=list(map(int,input().split()))

co={}
from collections import deque

q=deque()

ans=0
num=0
for c in a:
    q.append(c)

    if c in co:
        if co[c]==0:
            co[c]+=1
            num+=1
        else:
            co[c]+=1
    else:
        co[c]=1
        num+=1
    
    while q and num > k:
        rm =q.popleft()
        co[rm]-=1
        if co[rm]==0:
            num-=1
        
    ans = max(ans,len(q))

print(ans)