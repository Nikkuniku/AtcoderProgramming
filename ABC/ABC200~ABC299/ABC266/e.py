n = int(input())
dp = [0]*(n+2)
dp[1] = 3.5
for i in range(2, n+1):
    for j in range(1, 7):
        dp[i] += max(j, dp[i-1])
    dp[i] /= 6

print(dp[n])
