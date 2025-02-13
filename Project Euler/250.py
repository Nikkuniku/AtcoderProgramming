L = 250
N = 250250
P = [pow(i, i, L) for i in range(1, N + 1)]
dp = [[0] * L for _ in range(N + 1)]
dp[0][0] = 1
MOD = 10_000_000_000_000_000
for i in range(N):
    p = P[i]
    for j in range(L):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][(j + p) % L] += dp[i][j]
        dp[i + 1][j] %= MOD
        dp[i + 1][(j + p) % L] %= MOD
ans = dp[N][0] - 1
print(ans)
