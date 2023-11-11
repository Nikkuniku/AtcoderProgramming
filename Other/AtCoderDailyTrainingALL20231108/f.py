N, X, Y = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
prev = [-1] * N
seen = [False] * N
from collections import deque

q = deque([X - 1])
seen[X - 1] = True
while q:
    v = q.popleft()
    for e in Edge[v]:
        if seen[e]:
            continue
        seen[e] = True
        prev[e] = v
        q.append(e)
ans = []
now = Y - 1
while now != X - 1:
    ans.append(now)
    now = prev[now]
ans.append(X - 1)
ans = ans[::-1]
ans = list(map(lambda x: x + 1, ans))
print(*ans)
