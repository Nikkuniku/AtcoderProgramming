N = int(input())
A = list(map(int, input().split()))
INF = 1 << 60
dp = [[-INF]*2 for _ in range(N+1)]
dp[0] = [0, 0]
for i in range(N):
    dp[i+1][0] = max(dp[i+1][0], max(dp[i])+A[i])
    dp[i+1][1] = max(dp[i+1][1], max(dp[i]))
ans = max(dp[N])
print(ans)
