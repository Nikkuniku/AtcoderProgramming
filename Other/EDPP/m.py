n, k = map(int, input().split())
a = list(map(int, input().split()))

MOD = 1000000007
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n):
    p = a[i]
    if i == 0:
        for j in range(p+1):
            dp[i+1][j] = 1
            dp[i+1][j] %= MOD
    else:
        for j in range(k+1):
            dp[i+1][j] += dp[i][j]
            if j-p >= 1:
                dp[i+1][j] -= dp[i][j-p-1]
            dp[i+1][j] %= MOD
    if i != n-1:
        for j in range(k):
            dp[i+1][j+1] += dp[i+1][j]
            dp[i+1][j+1] %= MOD

print(dp[n][k])
