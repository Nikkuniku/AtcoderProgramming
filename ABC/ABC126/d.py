n=int(input())
edge=[[]for _ in range(n)]
for _ in range(n-1):
    u,v,w=map(int,input().split())
    u,v=u-1,v-1
    edge[u].append([v,w])
    edge[v].append([u,w])

from collections import deque
q=deque([0])
dist=[-1]*n
dist[0]=0
color=[0]*n
while q:
    v=q.popleft()

    for e in edge[v]:
        node=e[0]
        cost=e[1]
        if dist[node]==-1:
            dist[node]=dist[v]+cost
            q.append(node)
            if dist[node]%2==1:
                color[node]=1

print(*color,sep="\n")