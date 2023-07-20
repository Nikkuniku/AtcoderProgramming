X, Y, Z = map(int, input().split())
S = input()
INF = 1 << 60
dp = [[INF]*2 for _ in range(len(S)+1)]
dp[0] = [INF, 0]
for i in range(len(S)):
    if S[i] == 'A':
        dp[i+1][0] = min(dp[i][0], dp[i][1]+Z)+X
        dp[i+1][1] = min(dp[i][1], dp[i][0]+Z)+Y
    else:
        dp[i+1][0] = min(dp[i][0], dp[i][1]+Z)+Y
        dp[i+1][1] = min(dp[i][1], dp[i][0]+Z)+X
ans = min(dp[len(S)])
print(ans)
