N = int(input())
A = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N + 1)]
for i in range(N):
    if i != 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][1] + 2 * A[i])
    dp[i + 1][1] = max(dp[i][1], dp[i][0] + A[i])
print(max(dp[-1]))
