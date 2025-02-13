from heapq import heappop, heappush

N = int(input())
edge = [[] for _ in range(N)]
adjacents = [0] * N
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    adjacents[u] += 1
    adjacents[v] += 1
ans = 1 << 60
for v in range(N):
    q = []
    for e in edge[v]:
        heappush(q, adjacents[e] - 1)
    while q:
        x = len(q)
        y = heappop(q)
        temp = 1 + x + x * y
        ans = min(ans, N - temp)
print(ans)
