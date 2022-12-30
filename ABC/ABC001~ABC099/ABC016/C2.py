n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

from collections import deque

def bfs(s):
    dist=[-1]*n
    dist[s]=0
    d=deque([s])

    while d:
        v=d.popleft()

        for e in edge[v]:
            if dist[e]==-1:
                dist[e]=dist[v]+1
                d.append(e)

    return dist.count(2)

for i in range(n):
    print(bfs(i))


    