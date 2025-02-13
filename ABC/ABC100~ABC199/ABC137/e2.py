from collections import deque

N, M, P = map(int, input().split())
graph_edge = []
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # c-Pとして、最大経路問題に
    # -1をかけて、最短経路問題に
    graph_edge.append((a, b, -(c - P)))
    Edge[b].append(a)
INF = 1 << 60
dist = [INF] * N
dist[0] = 0
isNegativeCycle = False
for k in range(2 * N + 1):
    for u, v, c in graph_edge:
        if dist[u] == INF:
            continue
        if dist[u] + c < dist[v]:
            if k >= N - 1 and v == N - 1:
                isNegativeCycle = True
                break
            elif k >= N - 1:
                dist[v] = -INF
            else:
                dist[v] = dist[u] + c
ans = max(-dist[-1], 0)
if isNegativeCycle:
    ans = -1
print(ans)
