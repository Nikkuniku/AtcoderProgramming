s = input()
t = input()
n, m = len(s), len(t)
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
        else:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j], dp[i][j])

print(dp[n][m])
