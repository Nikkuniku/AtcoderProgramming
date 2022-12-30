N, M, K, S, T, X = map(int, input().split())
MOD = 998244353
Edge = []
for _ in range(M):
    u, v = map(int, input().split())
    Edge.append((u, v))
    Edge.append((v, u))
dp = [[[0, 0] for _ in range(N+1)] for _ in range(K+1)]
dp[0][S][0] = 1
for i in range(K):
    for m in range(2*M):
        u, v = Edge[m]
        for k in range(2):
            dp[i+1][v][k ^ (v == X)] += dp[i][u][k]
            dp[i+1][v][k] %= MOD
print(dp[K][T][0])
