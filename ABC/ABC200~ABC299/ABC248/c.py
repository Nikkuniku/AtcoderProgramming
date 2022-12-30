n, m, k = map(int, input().split())
dp = [[0]*(m*k+3) for _ in range(n)]
for i in range(1, m+1):
    dp[0][i] = 1
mod = 998244353

for i in range(1, n):
    for j in range(m*i+1):
        for p in range(1, m+1):
            if 0 <= j+p < m*k+3:
                dp[i][j+p] += dp[i-1][j]
                dp[i][j+p] %= mod
ans = 0
for j in range(n, k + 1):
    ans += dp[n-1][j]
    ans %= mod
print(ans)
