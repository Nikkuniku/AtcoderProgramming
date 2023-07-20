S = input()
T = input()
INF = 1 << 60
dp = [[INF]*(len(T)+1) for _ in range(len(S)+1)]
dp[0][0] = 0
for i in range(len(S)):
    dp[i][0] = i
for j in range(len(T)):
    dp[0][j] = j
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] != T[j]:
            dp[i+1][j+1] = min(dp[i][j]+1, dp[i+1][j]+1, dp[i][j+1]+1)
        else:
            dp[i+1][j+1] = min(dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
ans = dp[len(S)][len(T)]
print(ans)
