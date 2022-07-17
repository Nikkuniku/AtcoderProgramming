n, m, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
MOD = 998244353
for i in range(n):
    for s in range(i*m+1):
        for j in range(1, m+1):
            if s+j < k+1:
                dp[i+1][s+j] += dp[i][s]
                dp[i+1][s+j] %= MOD
ans = 0
for p in range(k+1):
    ans += dp[n][p]
    ans %= MOD
print(ans)
