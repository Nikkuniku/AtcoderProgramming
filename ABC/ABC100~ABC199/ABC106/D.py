N, M, Q = map(int, input().split())
grid = [[0]*(N+2) for _ in range(N+2)]
for _ in range(M):
    L, R = map(int, input().split())
    grid[L][R] += 1

for i in range(N+1):
    for j in range(N+1):
        grid[i][j+1] += grid[i][j]
for j in range(N+1):
    for i in range(N+1):
        grid[i+1][j] += grid[i][j]
ans = []
for _ in range(Q):
    a, b = map(int, input().split())
    tmp = grid[b][b]-grid[a-1][b]-grid[b][a-1]+grid[a-1][a-1]
    ans.append(tmp)
print(*ans, sep="\n")
