n, m = map(int, input().split())
d = [int(input()) for _ in range(n)]
weather = [int(input()) for _ in range(m)]
INF = 1 << 62
dp = [[INF]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    dp[i][0] = 0

for i in range(m):
    for j in range(n):
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1])
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+d[j]*weather[i])

print(dp[m][n], sep="\n")
