N, M, K = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    Edge[x].append(y)
dp = [[0] * N for _ in range(K + 1)]
dp[0][0] = 1
MOD = 998244353
for i in range(K):
    for j in range(N):
        dp[i + 1][(j + 1) % N] += dp[i][j]
        dp[i + 1][(j + 1) % N] %= MOD
        for to in Edge[j]:
            dp[i + 1][to] += dp[i][j]
            dp[i + 1][to] %= MOD
print(sum(dp[K]) % MOD)
