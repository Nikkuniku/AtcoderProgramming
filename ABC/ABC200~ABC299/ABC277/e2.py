from collections import deque
N, M, K = map(int, input().split())
edge = [[[], []] for _ in range(N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    u, v = u-1, v-1
    edge[u][a].append((v, a))
    edge[v][a].append((u, a))
Switches = set(list(map(lambda x: int(x)-1, input().split())))
for u in Switches:
    edge[u][0].append((u, 1))
    edge[u][1].append((u, 0))

q = deque([(0, 1)])
INF = 1 << 62
dist = [[INF]*2 for _ in range(N)]
dist[0][1] = 0
while q:
    v, f = q.popleft()

    for t, g in edge[v][f]:
        if dist[t][g] == INF:
            if t == v:
                dist[t][g] = dist[v][f]
                q.appendleft((t, g))
            else:
                dist[t][g] = dist[v][f]+1
                q.append((t, g))
ans = min(dist[-1])
if ans == INF:
    ans = -1
print(ans)
