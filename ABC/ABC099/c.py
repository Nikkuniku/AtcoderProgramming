n = int(input())
money = [1]
for i in range(1, 7):
    money.append(pow(6, i))
for i in range(1, 6):
    money.append(pow(9, i))
m = len(money)
money.sort()
INF = 10**8
dp = [[INF]*(n+1) for _ in range(m+1)]
dp[0][0] = 0

for i in range(m):
    p = money[i]
    for j in range(n+1):
        dp[i+1][j] = dp[i][j]
        if j-p >= 0:
            dp[i+1][j] = min(dp[i][j], dp[i][j-p]+1, dp[i+1][j-p]+1)

ans = dp[m][n]
print(ans)
