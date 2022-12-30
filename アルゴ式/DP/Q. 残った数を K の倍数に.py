N, K = map(int, input().split())
S = input()
MOD = 10**9 + 7
dp = [[0]*K for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for r in range(K):
        dp[i+1][(10*r+int(S[i])) % K] += dp[i][r]
        dp[i+1][r] += dp[i][r]
    for r in range(K):
        dp[i+1][r] %= MOD
print((dp[N][0]-1) % MOD)
