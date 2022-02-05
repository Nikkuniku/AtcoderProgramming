n, m = map(int, input().split())
score = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b, s = map(int, input().split())
    score[a][b] = s
dp = [0]*(1 << n)
for s in range(1 << n):
    for v in range(n):
        tmp=0
        for u in range(n):
            if (s >> u) & 1 and (s >> v) & 1 == 0:
                tmp+=score[u][v]
        if dp[s]+tmp >= dp[s | (1 << v)]:
            dp[s | (1 << v)] = dp[s]+tmp

print(dp[(1 << n)-1])
