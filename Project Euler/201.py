S = [i * i for i in range(1, 101)]
N = len(S)
M = 50
W = sum(S)
dp = [[[0] * (W + 1) for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for i in range(N):
    vi = S[i]
    for k in range(M + 1):
        for j in range(W + 1):
            dp[i + 1][k][j] = dp[i][k][j]
            if k - 1 >= 0 and j - vi >= 0:
                dp[i + 1][k][j] += dp[i][k - 1][j - vi]
ans = 0
for j in range(W + 1):
    if dp[N][M][j] == 1:
        ans += j
print(ans)
