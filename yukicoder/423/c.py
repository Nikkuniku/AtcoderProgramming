N, P, K = map(int, input().split())
# dp[i+1][j]:i番目まで見てj個のアイテムを装備したときの最大値
Lim = 10**18 + 1
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = P
for i in range(1, N + 1):
    T, B = map(int, input().split())
    for j in range(min(i + 1, K + 1)):
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j > 0:
            if T == 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + B)
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] * 2)
        dp[i][j] = min(dp[i][j], Lim)
ans = dp[N][K]
if ans == Lim:
    ans = -1
print(ans)
