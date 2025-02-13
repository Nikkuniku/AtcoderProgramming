N, M = map(int, input().split())
MOD = 998244353
dp = [[0, 0] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    dp[i + 1][0] = (M - 1) * dp[i][1] % MOD
    dp[i + 1][1] = (dp[i][0] + (M - 2) * dp[i][1]) % MOD
ans = M * dp[N - 1][1] * (M - 1) % MOD
print(ans)
