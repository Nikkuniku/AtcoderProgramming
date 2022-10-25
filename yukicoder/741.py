k = int(input())
n = str(pow(10, k))
m = len(n)
MOD = 1000_000_007
dp = [[0]*11 for _ in range(2)]
dp[0][0] = 1
for i in range(m):
    for j in range(10):
        dp[0][j+1] += dp[0][j]
        dp[0][j+1] %= MOD
        dp[0][j] = dp[0][j] % MOD

        dp[1][j+1] += dp[1][j]
        dp[1][j+1] %= MOD
        dp[1][j] = (dp[0][j]+dp[1][j]) % MOD


ans = dp[0][9] % MOD
print(ans)
