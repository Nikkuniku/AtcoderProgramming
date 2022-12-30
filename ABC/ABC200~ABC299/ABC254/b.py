n = int(input())
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

for i in range(1, n+1):
    tmp = []
    for j in range(i+1):
        if j == 0:
            continue
        tmp.append(dp[i][j])
    print(*tmp)
