N, M = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(M)]
dist = [[10**9]*N for _ in range(N)]
for k in range(N):
    dist[k][0] = 0
    for u, v, w in Edge:
        dist[k][v] = min(dist[k][v], dist[k][u]+w)
    if k < N-1:
        dist[k+1] = dist[k][:]
ans = 'Yes' if dist[k] != dist[k-1] else 'No'
print(ans)
