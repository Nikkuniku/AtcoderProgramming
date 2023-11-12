N, M, K = map(int, input().split())
cost = [[-1] * N for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    cost[u][v] = cost[v][u] = w % K
# dp[s]:頂点集合がsである時の全域木のコストとして考えられる値の集合
dp = [set() for _ in range(1 << N)]
# 初期値の設定(1点のみは0のみ)
for i in range(N):
    dp[1 << i].add(0)
for s in range(1 << N):
    for u in range(N):
        for v in range(N):
            if s != 0 and not s & (1 << u):
                continue
            if s & (1 << v) == 0 and cost[u][v] != -1:
                for a in dp[s]:
                    dp[s | (1 << v)].add((a + cost[u][v]) % K)
ans = min(dp[-1])
print(ans)
