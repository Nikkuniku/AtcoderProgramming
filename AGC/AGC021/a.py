N = input()
dp = [[0, 0] for _ in range(len(N)+1)]
dp[0] = [0, -(1 << 60)]
for i in range(len(N)):
    p = int(str(N)[i])
    dp[i+1][0] = max(dp[i+1][0], dp[i][0]+p)
    dp[i+1][1] = max(dp[i+1][1], dp[i][0]+p-1, dp[i][1]+9)
print(max(dp[len(N)]))
