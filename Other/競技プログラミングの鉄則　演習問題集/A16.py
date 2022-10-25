n = int(input())
a = [0]+list(map(int, input().split()))
b = [0, 0]+list(map(int, input().split()))
INF = 10**18
dp = [INF]*(n+1)
dp[1] = 0
for i in range(2, n+1):
    if i-1 >= 1:
        dp[i] = min(dp[i], dp[i-1]+a[i-1])
    if i-2 >= 1:
        dp[i] = min(dp[i], dp[i-2]+b[i-1])

print(dp[n])
