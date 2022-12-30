n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1

    edge[a].append(b)
    edge[b].append(a)

dist=[float('inf')]*n
dist[0]=0

from collections import deque
d=deque([0])
symbol=[0]*n

while d:
    v = d.popleft()

    for e in edge[v]:
        if dist[e]>dist[v]+1:
            dist[e]=dist[v]+1
            symbol[e]=v+1
            d.append(e)

print('Yes')
for i in range(1,n):
    print(symbol[i])