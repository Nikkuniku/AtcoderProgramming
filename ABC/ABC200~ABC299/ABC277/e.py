from collections import deque
N, M, K = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    u, v = u-1, v-1
    edge[u].append((v, a))
    edge[v].append((u, a))
Switches = set(list(map(lambda x: int(x)-1, input().split())))
s = 0
switchflg = 1
q = deque([(s, switchflg)])
INF = 1 << 62
dist = [INF]*N
dist_inv = [INF]*N
dist[s] = 0
while q:
    v, f = q.popleft()

    if f == 1:
        for t, isok in edge[v]:
            if dist[t] > dist[v]+1 and f == isok:
                dist[t] = dist[v]+1
                q.append((t, f))
    else:
        for t, isok in edge[v]:
            if dist_inv[t] > dist_inv[v]+1 and f == isok:
                dist_inv[t] = dist_inv[v]+1
                q.append((t, f))

    if v in Switches:
        if f == 1:
            for t, isok in edge[v]:
                if dist_inv[t] > dist[v]+1 and f != isok:
                    dist_inv[t] = dist[v]+1
                    q.append((t, 0))
        else:
            for t, isok in edge[v]:
                if dist[t] > dist_inv[v]+1 and f != isok:
                    dist[t] = dist_inv[v]+1
                    q.append((t, 1))

ans = min(dist[-1], dist_inv[-1])
if ans == INF:
    ans = -1
print(ans)
