from collections import deque

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
q = deque([0])
dist = [-1] * N
dist[0] = 0
while q:
    v = q.popleft()
    for to in Edge[v]:
        if dist[to] != -1:
            continue
        dist[to] = dist[v] + 1
        q.append(to)
ans = 1e18
for v in range(1, N):
    if dist[v] == -1:
        continue
    for w in Edge[v]:
        if w == 0:
            ans = min(ans, dist[v] + 1)
            break
if ans == 1e18:
    ans = -1
print(ans)
