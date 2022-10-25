n = int(input())
s = [list(input()) for _ in range(5)]
INF = 1 << 60
dp = [[[INF]*5 for _ in range(3)] for _ in range(n+1)]
dp[0][0] = [0]*5
dp[0][1] = [0]*5
dp[0][2] = [0]*5
d = {"W": 0, 'B': 1, 'R': 2, "#": 3}
for i in range(n):
    for j in range(3):
        for k in range(5):
            if k == 0:
                for m in range(3):
                    if j == m:
                        continue
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i]
                                        [m][4]+(1 if d[s[k][i]] != j else 0))
            else:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i+1]
                                    [j][k-1]+(1 if d[s[k][i]] != j else 0))
ans = INF
for i in range(3):
    ans = min(ans, dp[n][i][4])
print(ans)
