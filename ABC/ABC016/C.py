n,m=map(int,input().split())

edge=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

from collections import deque

for i in range(n):
    dist=[-1]*n
    dist[i]=0

    d=deque([i])

    while d:
        v=d.popleft()

        for e in edge[v]:
            if dist[e]==-1:
                dist[e]=dist[v]+1
                d.append(e)

    print(dist.count(2))