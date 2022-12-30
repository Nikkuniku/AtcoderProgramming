import sys
def input():
    return sys.stdin.readline()[:-1]
    
N,M=map(int,input().split())
adj=[[] for _ in range(N)]

for _ in range(M):
    u,v,l=map(int,input().split())
    u,v=u-1,v-1
    adj[u].append((l,v))
    adj[v].append((l,u))

inf =float('inf')

from heapq import heappop,heappush
from collections import deque

def dijkstra(s,g,adj):
    dist=[inf]*N
    seen=[False]*N

    hq=[(0,s)]
    dist[s]=0
    seen[s]=True

    while hq:
        v=heappop(hq)[1]
        seen[v]=True

        for cost,to in adj[v]:
            if seen[to]==False and dist[to]>dist[v]+cost:
                dist[to]=dist[v]+cost
                heappush(hq,(dist[to],to))

    return dist[g]

ans=inf

adj[0]=deque(adj[0])
for _ in range(len(adj[0])):
    q=adj[0].popleft()
    ans=min(ans,q[0]+dijkstra(0,q[1],adj))
    adj[0].append(q)

if ans==inf:
    ans=-1

print(ans)   