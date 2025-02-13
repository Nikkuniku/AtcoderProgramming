M, N = map(int, input().split())
X = list(map(int, input().split()))
dp = [[[0] * M for _ in range(1 << M)] for _ in range(N + 1)]
for v in range(M):
    dp[0][1 << v][v] = 1
for i in range(N):
    for s in range(1 << M):
        for v in range(M):
            p = X[v] - 1
            if s & (1 << v):
                dp[i + 1][s - (1 << v)][v] += dp[i][s][w]
