MAX_N = 30000
MAX_M = 30000

# 入力
n, m = MAX_N, MAX_M
M = 1000_000
dp = [[0] * (MAX_N + 1) for _ in range(MAX_M + 1)]  # DPテーブル

dp[0][0] = 1
for i in range(1, m + 1):
    for j in range(n + 1):
        if j - i >= 0:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % M
        else:
            dp[i][j] = dp[i - 1][j]
    if dp[i][i] % M == 0:
        exit(print(i))

for i in range(1, MAX_N):
    if dp[i][i] % M == 0:
        exit(print(i))
