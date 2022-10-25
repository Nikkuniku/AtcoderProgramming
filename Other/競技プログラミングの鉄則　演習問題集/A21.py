n = int(input())
block = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n-1, i-1, -1):
        if j+1 <= n-1:
            dp[i][j] = max(dp[i][j], dp[i][j+1]+(block[j+1][1]
                           if i <= block[j+1][0]-1 < j+1 else 0))
        if 0 <= i-1:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+(block[i-1][1]
                           if i-1 < block[i-1][0]-1 <= j else 0))
ans = 0
for i in range(n):
    ans = max(ans, dp[i][i])
print(ans)
