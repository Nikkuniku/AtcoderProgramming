n = int(input())
dp = [[0]*(n+1) for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1

for i in range(n):
    s = input()
    if s == 'AND':
        dp[0][i+1] = 2*dp[0][i]+dp[1][i]
        dp[1][i+1] = dp[1][i]
    else:
        dp[0][i+1] = dp[0][i]
        dp[1][i+1] = dp[0][i]+2*dp[1][i]

ans = dp[1][n]
print(ans)
