N, M = map(int, input().split())
S = 1 << N
items = []
score = [[0]*N for _ in range(N)]
for _ in range(M):
    i, j, s = map(int, input().split())
    score[i][j] = s
dp = [0]*S
pows = set()
for i in range(N):
    pows.add(pow(2, i))
pows.add(0)
for s in range(S):
    for v in range(N):
        tmp = 0
        if s & (1 << v) or (s | (1 << v)) in pows:
            continue
        for u in range(N):
            if u == v:
                continue
            if (s >> u) & 1:
                tmp += score[v][u]
        if dp[s | (1 << v)] < dp[s]+tmp:
            dp[s | (1 << v)] = dp[s]+tmp
print(dp[S-1])
