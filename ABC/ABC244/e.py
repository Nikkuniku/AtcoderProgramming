n, m, k, s, t, x = map(int, input().split())
Edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)

MOD = 998244353
dp = [[[0]*2 for _ in range(n)] for _ in range(k+1)]
dp[0][s-1][0] = 1
for i in range(k):
    for v, ed in enumerate(Edge):
        if ed:
            for e in ed:
                if e == x-1:
                    dp[i+1][e][1] += dp[i][v][0]
                    dp[i+1][e][0] += dp[i][v][1]
                else:
                    dp[i+1][e][0] += dp[i][v][0]
                    dp[i+1][e][1] += dp[i][v][1]
                dp[i+1][e][0] %= MOD
                dp[i+1][e][1] %= MOD

ans = dp[k][t-1][0]
print(ans)
