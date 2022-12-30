n=int(input())
edge=[[] for _ in range(n+1)]
times=[0]*n
for i in range(n):
    l=list(map(int,input().split()))
    k=l[1]
    if k>0:
        for j in range(k):
            edge[i].append(l[2+j]-1)
    times[i]+=l[0]

from collections import deque
dist=[-1]*n
q=deque([n-1])
dist[n-1]=0

while q:
    v=q.popleft()

    for e in edge[v]:
        if dist[e]==-1:
            dist[e]=dist[v]+1
            q.append(e)

ans=0
for i in range(n):
    if dist[i]==-1:
        continue    
    ans+=times[i]
print(ans)