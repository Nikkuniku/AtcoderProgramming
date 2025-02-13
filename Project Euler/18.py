N = 15
S = [list(map(int, input().split())) for _ in range(N)]
print(*S, sep="\n")
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    if i == 0:
        dp[i + 1][0] = S[i][0]
    else:
        for j in range(len(S[i])):
            if j < len(S[i - 1]):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + S[i][j])
            if j - 1 < len(S[i - 1]):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + S[i][j])
print(*dp, sep="\n")
ans = max(dp[N])
print(ans)
