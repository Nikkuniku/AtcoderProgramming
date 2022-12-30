from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
dist = [-1]*N
dist[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v]+1
        q.append(e)
ans = max(dist)
print(ans)
