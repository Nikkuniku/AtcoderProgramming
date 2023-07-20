from heapq import heappush, heappop


def dijkstra(s, n, adj):  # (始点, ノード数)
    INF = 10 ** 9
    dist = [INF] * n
    hq = [(0, s)]  # (distance, node)
    dist[s] = 0
    seen = [False] * n  # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1]  # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]:  # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


N, K = map(int, input().split())
sx, sy, gx, gy = map(int, input().split())
Points = [[sx, sy]]
for _ in range(N):
    Points.append(list(map(int, input().split())))
Points.append([gx, gy])
# 距離配列作成
dist = [[0]*(N+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        if i == j:
            continue
        D = abs(Points[i][0]-Points[j][0])+abs(Points[i][1]-Points[j][1])
        dist[i][j] = D
        dist[j][i] = D
l = 0
r = 2*10**5 + 5
while r-l > 1:
    Edge = [[] for _ in range(N+2)]
    mid = (l+r)//2
    for i in range(N+2):
        for j in range(i+1, N+2):
            p = dist[i][j]//mid
            if dist[i][j] % mid == 0:
                p -= 1
            Edge[i].append((j, p))
            Edge[j].append((i, p))
    res = dijkstra(0, N+2, Edge)
    if res[-1] <= K:
        r = mid
    else:
        l = mid
print(r)
