N = int(input())
M = int(input())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
from collections import deque

q = deque([0])
dist = [-1] * N
dist[0] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] == -1:
            dist[e] = dist[v] + 1
            q.append(e)
ans = 0
for i in range(N):
    if 1 <= dist[i] <= 2:
        ans += 1
print(ans)
