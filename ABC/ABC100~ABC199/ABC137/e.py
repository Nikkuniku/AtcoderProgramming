N, M, P = map(int, input().split())
Edge = [[] for _ in range(N)]
graph_edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c))
    graph_edges.append((a, b, c))
INF = 1 << 60
dist_step = [[-1] * N for _ in range(2 * N + 1)]
dist_step_pos = [[-1] * N for _ in range(2 * N + 1)]
dist_step[0][0] = 0
dist_step_pos[0][0] = 0
for k in range(1, N + 1):
    for u, v, c in graph_edges:
        if dist_step[k - 1][u] == -1:
            continue
        dist_step[k][v] = max(dist_step[k][v], dist_step[k - 1][u] + c - P)
        dist_step_pos[k][v] = max(dist_step_pos[k][v], dist_step_pos[k - 1][u] + c)
from collections import deque

q = deque()
for v in range(N):
    if dist_step_pos[N][v] != -1 and dist_step_pos[N][v] != dist_step_pos[N - 1][v]:
        q.append(v)
for k in range(N + 1, 2 * N + 1):
    for u, v, c in graph_edges:
        if dist_step_pos[k - 1][u] == -1:
            continue
        dist_step_pos[k][v] = max(dist_step_pos[k][v], dist_step_pos[k - 1][u] + c)
seen = [False] * N
for v in q:
    seen[v] = True
while q:
    v = q.popleft()
    for e, _ in Edge[v]:
        if seen[e]:
            continue
        seen[e] = True
        q.append(e)
isPoscycle = False
Q = 0
for v in range(N):
    if seen[v]:
        if (
            dist_step_pos[2 * N][v] != -1
            and dist_step_pos[2 * N][v] != dist_step_pos[N][v]
        ):
            isPoscycle = True
            if dist_step_pos[2 * N][v] > 0 and dist_step_pos[N][v] > 0:
                Q = dist_step_pos[2 * N][v] - dist_step_pos[N][v]
ans = max(max(dist_step[k][-1] for k in range(N + 1)), 0)
if isPoscycle:
    if Q - N * P > 0:
        ans = -16
print(ans)
