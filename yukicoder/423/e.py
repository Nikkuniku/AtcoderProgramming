from heapq import heapify, heappop, heappush
from collections import defaultdict

H, W, N = map(int, input().split())
Warp = [list(map(int, input().split())) for _ in range(N)]
INF = 1 << 60
dist = defaultdict(lambda: INF)
dist[1, 1] = 0
q = [(0, 1, 1)]
while q:
    d, vx, vy = heappop(q)
    if d > dist[vx, vy]:
        continue
    for i in range(N):
        a, b, c, d = Warp[i]
        if dist[a, b] > dist[vx, vy] + abs(vx - a) + abs(vy - b):
            dist[a, b] = dist[vx, vy] + abs(vx - a) + abs(vy - b)
            heappush(q, (dist[a, b], a, b))
            if dist[c, d] > dist[a, b] + 1:
                dist[c, d] = dist[a, b] + 1
                heappush(q, (dist[c, d], c, d))
        if dist[c, d] > dist[vx, vy] + abs(vx - c) + abs(vy - d):
            dist[c, d] = dist[vx, vy] + abs(vx - c) + abs(vy - d)
            heappush(q, (dist[c, d], c, d))
    if dist[H, W] > dist[vx, vy] + abs(vx - H) + abs(vy - W):
        dist[H, W] = dist[vx, vy] + abs(vx - H) + abs(vy - W)
print(dist[H, W])
