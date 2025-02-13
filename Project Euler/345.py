N = 15
INF = 1 << 60
dp = [[-INF] * (1 << N) for _ in range(N + 1)]
dp[0][0] = 0
S = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for s in range(1 << N):
        for j in range(N):
            if s & (1 << j):
                continue
            dp[i + 1][s | (1 << j)] = max(dp[i + 1][s | (1 << j)], dp[i][s] + S[i][j])
print(dp[N][-1])
