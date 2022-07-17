n, m, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0] = [1]*(k+1)
MOD = 998244353
for i in range(n):
    for j in range(k+1):
        if j-1 >= 0:
            dp[i+1][j] += dp[i][j-1]
        if j-m-1 >= 0:
            dp[i+1][j] -= dp[i][j-m-1]
        dp[i+1][j] %= MOD
    for j in range(1, k+1):
        dp[i+1][j] += dp[i+1][j-1]
        dp[i+1][j] %= MOD
print(dp[n][k])
