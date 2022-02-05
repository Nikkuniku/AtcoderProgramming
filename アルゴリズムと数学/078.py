n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    edge[a].append(b)
    edge[b].append(a)

from collections import deque
s=0
q=deque([s])
dist=[-1]*n
dist[s]=0

while q:
    v=q.popleft()

    for e in edge[v]:
        if dist[e]==-1:
            dist[e]=dist[v]+1
            q.append(e)

for j in range(n):
    if dist[j]>120:
        dist[j]=120
    elif dist[j]==-1:
        dist[j]=120
print(*dist,sep="\n")