N, K = map(int, input().split())
dp = [[0, 0] for _ in range(N + 1)]
dp[1][0] = 1
MOD = 1000000007
for i in range(2, N + 1):
    dp[i][0] += dp[i - 1][0]
    dp[i][0] += sum(dp[i - 2])
    dp[i][0] %= MOD
    if K > 2:
        tmp = dp[i - 1][0] - dp[max(1, i - (K - 2)) - 1][0]
        dp[i][1] += dp[i - 1][1]
        dp[i][1] += tmp
        dp[i][1] %= MOD
ans = (sum(dp[N]) - sum(dp[N - 1])) % MOD
print(ans)
