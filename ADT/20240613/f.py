from heapq import heappop, heappush

N = int(input())
Edge = [[] for _ in range(N)]
S = list(map(int, input().split()))
for i in range(N):
    Edge[i].append(((i + 1) % N, S[i]))
dist = list(map(int, input().split()))
q = []
for i in range(N):
    heappush(q, (dist[i], i))
while q:
    d, v = heappop(q)
    for e, cost in Edge[v]:
        if d + cost < dist[e]:
            dist[e] = d + cost
            heappush(q, (dist[e], e))
print(*dist, sep="\n")
