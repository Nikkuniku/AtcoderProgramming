n, m, k = map(int, input().split())

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0] = [0]+[1]*(m)
MOD = 998244353
for i in range(1, n+1):
    if i == 1:
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] % MOD
    else:
        if k == 0:
            for j in range(1, m+1):
                dp[i][j] += dp[i-1][m]
        else:
            for j in range(1, m+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                p = j+k-1
                if 0 <= p <= m:
                    dp[i][j] += dp[i-1][m]-dp[i-1][p]
        dp[i][j] %= MOD
    for j in range(m):
        dp[i][j+1] += dp[i][j]
        dp[i][j+1] %= MOD
ans = dp[n][m]
print(ans)
