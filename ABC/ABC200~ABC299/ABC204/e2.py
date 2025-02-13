def f(t, C, D):
    return t + (D // (t + 1)) + C


def solve(t0):
    INF = 1 << 60
    dist = [INF] * N
    dist[0] = t0
    q = [(t0, 0)]
    heapify(q)
    while q:
        d, v = heappop(q)
        if d > dist[v]:
            continue
        for u, C, D in Edge[v]:
            min_dist = f(d, C, D)
            if dist[u] > min_dist:
                dist[u] = min_dist
                heappush(q, (dist[u], u))
    ans = dist[-1]
    if ans == INF:
        ans = -1
    return ans


from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c, d))
    Edge[b].append((a, c, d))
l = 0
r = 1 << 30
while r - l > 2:
    m1 = (l + l + r) // 3
    m2 = (l + r + r) // 3
    t1 = solve(m1)
    t2 = solve(m2)
    if t1 == -1:
        exit(print(-1))
    if t1 < t2:
        r = m2
    else:
        l = m1
x = min([solve(j) for j in range(l, r + 1)])
print(x)
