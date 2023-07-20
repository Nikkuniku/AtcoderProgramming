N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
cum = [[0]*(M+1) for _ in range(N+1)]
MOD = 10**9 + 7
for i in range(N):
    for j in range(M):
        if S[i] == T[j]:
            dp[i+1][j+1] = cum[i][j]+1
            dp[i+1][j+1] %= MOD
        cum[i+1][j+1] = cum[i+1][j]+cum[i][j+1]-cum[i][j]+dp[i+1][j+1]
        cum[i+1][j+1] %= MOD
ans = (cum[N][M]+1) % MOD
print(ans)
