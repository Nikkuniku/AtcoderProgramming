M, N = map(int, input().split())
Cost = [list(map(int, input().split())) for _ in range(M)]
INF = 1 << 60
dp = [[INF]*(1 << M) for _ in range(N+1)]
S = set()
for s in range(1 << M):
    Flg = True
    for i in range(M-1):
        if (s >> i) & 1 == (s >> (i+1)) & 1 == 0:
            Flg = False
            break
    if Flg:
        S.add(s)
        dp[0][s] = 0
full = (1 << M)-1
for i in range(N):
    for s in S:
        for t in S:
            if s | t == full:
                tmp = 0
                for k in range(M):
                    if (s >> k) & 1:
                        tmp += Cost[k][i]
                dp[i+1][s] = min(dp[i+1][s], dp[i][t]+tmp)

print(min(dp[N]))
