H, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(R)]


def bitDP(N, S, P):
    dist = [[0] * N for _ in range(1 << N)]
    for v in range(N):
        if v == S:
            dist[1 << v][v] = 1
        if P[v]:
            dist[1 << v][v] = P[S]
    for s in range(1 << N):
        for u in range(N):
            if not s & (1 << u):
                continue
            for v in range(N):
                if s & (1 << v):
                    continue
                dist[s | (1 << v)][v] += dist[s][u]
                dist[s | (1 << v)][v] %= MOD
    res = []
    for v in range(N):
        temp = 0
        for s in range(1 << N):
            temp += dist[s][v]
        res.append(temp)
    return res


MOD = 1000000007
L = 30
dp = [[[0] * R for _ in range(R)] for _ in range(L + 1)]
for i in range(R):
    dp[0][i] = bitDP(R, i, G[i])
for m in range(L):
    for i in range(R):
        for j in range(R):
            for k in range(R):
                dp[m + 1][i][j] += dp[m][i][k] * dp[m][k][j]
                dp[m + 1][i][j] %= MOD
ep, fp = [0] * R, [0] * R
ep[0] = 1
for m in range(L + 1):
    fp = [0] * R
    if (H - 1) & (1 << m):
        for i in range(R):
            for j in range(R):
                fp[j] += ep[i] * dp[m][i][j]
                fp[j] %= MOD
        ep, fp = fp, ep
print(ep[0])
