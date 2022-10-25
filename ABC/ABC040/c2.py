n = int(input())
a = [0]+list(map(int, input().split()))
INF = 1 << 60
dp = [INF]*(n+1)
dp[1] = 0
for i in range(2, n+1):
    if i-1 >= 1:
        dp[i] = min(dp[i], dp[i-1]+abs(a[i]-a[i-1]))
    if i-2 >= 1:
        dp[i] = min(dp[i], dp[i-2]+abs(a[i]-a[i-2]))
print(dp[n])
