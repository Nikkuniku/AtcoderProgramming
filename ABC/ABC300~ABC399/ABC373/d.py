from collections import deque

N, M = map(int, input().split())
Edge_out = [[] for _ in range(N)]
Edge_in = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    Edge_out[u].append((v, w))
    Edge_in[v].append((u, w))
INF = 1 << 60
ans = [-INF] * N
q = deque()
for i in range(N):
    if ans[i] != -INF:
        continue
    q.append(i)
    ans[i] = 0
    while q:
        v = q.popleft()
        for to, cost in Edge_out[v]:
            if ans[to] != -INF:
                continue
            ans[to] = ans[v] + cost
            q.append(to)
        for fr, cost in Edge_in[v]:
            if ans[fr] != -INF:
                continue
            ans[fr] = ans[v] - cost
            q.append(fr)
print(*ans)
