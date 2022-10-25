n = int(input())
m = n-1
a = list(map(int, input().split()))
dp = [[0]*21 for _ in range(m+1)]
dp[0][0] = 1
for i in range(m):
    if i == 0 and a[i] == 0:
        for j in range(21):
            dp[i+1][j] += dp[i][j]
        continue

    p = a[i]
    for j in range(21):
        if 0 <= j+p <= 20:
            dp[i+1][j+p] += dp[i][j]
        if 0 <= j-p <= 20:
            dp[i+1][j-p] += dp[i][j]

print(dp[m][a[-1]])
