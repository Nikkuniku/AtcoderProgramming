n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [-1]*n
dp[0] = 0
for i in range(n-1):
    if dp[i] == -1:
        continue
    p = a[i]-1
    q = b[i]-1
    dp[p] = max(dp[i]+100, dp[p])
    dp[q] = max(dp[i]+150, dp[q])

print(dp[n-1])
