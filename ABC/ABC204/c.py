from sys import stdin
from collections import deque
n,m=map(int,input().split())
edge=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int, stdin.readline().split())
    a,b=a-1,b-1
    edge[a].append(b)
ans=0
for i in range(n):
    v=i
    q=deque([i])
    dist=[-1]*n
    dist[i]=0

    while q:
        v=q.popleft()

        for e in edge[v]:
            if dist[e]==-1:
                dist[e]=dist[v]+1
                q.append(e)

    tmp=n-dist.count(-1)
    ans+=tmp

print(ans)