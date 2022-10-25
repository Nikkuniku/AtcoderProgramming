n = int(input())
a = list(map(int, input().split()))
MOD = 998244353
ans = 0
for m in range(1, n+1):
    dp = [[[0]*(m+1) for _ in range(m+1)]for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for k in range(m):
                # a_iを選ぶとき
                if j+1 <= m:
                    dp[i+1][j+1][(k+a[i]) % m] += dp[i][j][k]
                    dp[i+1][j+1][(k+a[i]) % m] %= MOD
                # a_iを選ばないとき
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= MOD

    ans += dp[n][m][0]
    ans %= MOD
print(ans)
