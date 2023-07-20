from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
deg = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    Edge[b].append(a)
    deg[a] += 1
for i in range(N):
    Edge[i] = sorted(Edge[i])
q = deque()
for v in range(N):
    if deg[v] == 0:
        q.append(v)
ans = []
while q:
    v = q.popleft()
    ans.append(v)
    for e in Edge[v]:
        deg[e] -= 1
        if deg[e] == 0:
            q.append(e)
print(*ans[::-1])
