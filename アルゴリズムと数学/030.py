n = int(input())
a = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n+1)]

for i in range(n):
    dp[i+1][0] = dp[i][1]+a[i]
    dp[i+1][1] = max(dp[i][0], dp[i][1])

ans = max(dp[n])
print(ans)
