N, K = map(int, input().split())
G = [[] for _ in range(10)]
for _ in range(N):
    c, g = map(int, input().split())
    g -= 1
    G[g].append(c)
for g in range(10):
    G[g].sort(reverse=True)
dp = [[0]*(K+1) for _ in range(11)]
INF = 1 << 60
dp[0] = [0]+[-INF]*K
buy = [[0] for _ in range(10)]
for g in range(10):
    for i in range(len(G[g])):
        buy[g].append(sum(G[g][:(i+1)])+(i+1)*i)
for i in range(10):
    for j in range(K+1):
        for k in range(len(buy[i])):
            if j-k >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-k]+buy[i][k])
            else:
                break
ans = dp[10][K]
print(ans)
