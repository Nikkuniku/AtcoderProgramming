N, M = map(int, input().split())
Edge = [[0]*N for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u][v] = 1
    Edge[v][u] = 1
ans = 0
for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if Edge[a][b] and Edge[b][c] and Edge[c][a]:
                ans += 1
print(ans)
