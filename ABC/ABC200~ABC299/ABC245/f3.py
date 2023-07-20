from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
deg = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[b].append(a)
    deg[a] += 1
q = deque()
ans = N
for i, v in enumerate(deg):
    if v == 0:
        q.append(i)
        ans -= 1
while q:
    v = q.popleft()
    for e in Edge[v]:
        deg[e] -= 1
        if deg[e] == 0:
            q.append(e)
            ans -= 1
print(ans)
