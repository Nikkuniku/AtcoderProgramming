N = int(input())
A = list(map(int, input().split()))
dp = [[[0]*N for _ in range(2)] for _ in range(N+1)]
for i in range(N):
    for j in range(1, N):
        if j == 1:
            dp[i+1][0][j] = max(max(dp[i][0]), dp[i][1][1])
            dp[i+1][1][j] = max(dp[i][0])+A[j-1]
        else:
            dp[i+1][0][j] = max(dp[i+1][0][j], dp[i][1][j-1])
            dp[i+1][1][j] = max(dp[i+1][1][j], dp[i][1][j-1]+A[j-1])

print(max(sum(dp[N], [])))
