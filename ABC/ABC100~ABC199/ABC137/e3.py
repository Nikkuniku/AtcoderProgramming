from collections import deque

N, M, P = map(int, input().split())
Edge = []
input_Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    input_Edge[b].append(a)
    Edge.append((a, b, -(c - P)))
q = deque([N - 1])
seen = set()
while q:
    v = q.popleft()
    seen.add(v)
    for e in input_Edge[v]:
        if e in seen:
            continue
        q.append(e)
seen.remove(N - 1)
InNegativecycle = False
INF = float("inf")
dist = [INF] * N
dist[0] = 0
for k in range(N):
    changed = False
    for u, v, w in Edge:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            if v in seen:
                InNegativecycle = True
            changed = True
    if not changed:
        break
ans = dist[N - 1]
if dist[N - 1] == INF:
    ans = "impossible"
elif k == N - 1 and InNegativecycle:
    ans = "-1"
print(ans)
