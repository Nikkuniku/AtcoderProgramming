N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
MOD = 998244353
for i in range(N):
    for j in range(1, 10):
        for k in [-1, 0, 1]:
            if 0 <= j + k < 10:
                dp[i + 1][j] += dp[i][j + k]
        dp[i + 1][j] %= MOD
print(sum(dp[N - 1]))
