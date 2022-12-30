mod=10**9+7
from sys import stdin
from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    num =[0]*n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    num[s]=1
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in edge[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                num[to] = num[v]
                heappush(hq, (dist[to], to))
            elif dist[v] + cost == dist[to]:
                num[to]+=num[v]
                num[to]%=mod
    return num

n,m = map(int, stdin.readline().split())
edge = [[] for _ in range(n)]

for _ in range(m):
    a,b=map(int, stdin.readline().split())
    a,b=a-1,b-1
    edge[a].append((b,1))
    edge[b].append((a,1))

print(dijkstra(0,n)[n-1]%mod)