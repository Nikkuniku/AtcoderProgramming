N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1
MOD = 1000
for i in range(N):
    for s in range(M+1):
        dp[i+1][s] += dp[i][s]
        if s-A[i] >= 0:
            dp[i+1][s] += dp[i][s-A[i]]
        dp[i+1][s] %= MOD
ans = dp[N][M]
print(ans)
