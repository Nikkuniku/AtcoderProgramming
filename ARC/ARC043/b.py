from bisect import bisect_right

N = int(input())
D = sorted([int(input()) for _ in range(N)])
dp = [[0] * 5 for _ in range(N + 1)]
dp[0][0] = 1
MOD = 1000000007
for i in range(N):
    d = D[i]
    idx = bisect_right(D, d // 2)
    for j in range(1, min(i + 1 + 1, 5)):
        dp[i + 1][j] += dp[idx][j - 1]
        dp[i + 1][j] %= MOD
    for j in range(5):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
print(dp[N][4])
