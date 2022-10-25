s = input()
t = input()
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        else:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i][j+1], dp[i+1][j])

print(dp[len(s)][len(t)])
