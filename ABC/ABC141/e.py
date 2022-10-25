n = int(input())
S = input()
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(i+1, n):
        if S[i] == S[j]:
            if j-dp[i][j] <= i:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
        else:
            dp[i+1][j+1] = 0

ans = 0
for i in range(n+1):
    for j in range(n+1):
        ans = max(ans, dp[i][j])
print(ans)
