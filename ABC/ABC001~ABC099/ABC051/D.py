N, M = map(int, input().split())
INF = 1 << 60
dist = [[INF]*N for _ in range(N)]
Edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c
    Edges.append((a, b, c))
for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
ans = 0
for a, b, c in Edges:
    if dist[a][b] == c:
        ans += 1
print(M-ans)
