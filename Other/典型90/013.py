n,m=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    a,b = a-1,b-1
    edge[a].append((b,c))
    edge[b].append((a,c))

from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in edge[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

p=dijkstra(0,n)
q=dijkstra(n-1,n)

for i in range(n):
    ans = p[i]+q[i]
    print(ans)