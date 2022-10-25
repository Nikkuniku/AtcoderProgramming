n = int(input())
h = list(map(int, input().split()))
INF = 10**9
dp = [INF]*n
dp[0] = 0
for i in range(1, n):
    dp[i] = min(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
    if i-2 >= 0:
        dp[i] = min(dp[i], dp[i-2]+abs(h[i]-h[i-2]))

print(dp[n-1])
