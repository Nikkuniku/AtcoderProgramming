S = input()
N = len(S)
dp = [[0] * 4 for _ in range(N + 1)]
dp[0][0] = 1
MOD = 10**9 + 7
for i, v in enumerate(S):
    for j in range(4):
        dp[i + 1][j] += (3 if v == "?" else 1) * dp[i][j]
    if v in ("A", "?"):
        dp[i + 1][1] += dp[i][0]
    if v in ("B", "?"):
        dp[i + 1][2] += dp[i][1]
    if v in ("C", "?"):
        dp[i + 1][3] += dp[i][2]
    for j in range(4):
        dp[i + 1][j] %= MOD
print(dp[N][3])
