from sys import stdin
n = int(input())
p = list(map(float, stdin.readline().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    q = p[i]
    for j in range(n):
        dp[i+1][j] += dp[i][j]*(1-q)
        dp[i+1][j+1] += dp[i][j]*q

ans = 0
for k in range((1+n)//2, n+1):
    ans += dp[n][k]
print(ans)
