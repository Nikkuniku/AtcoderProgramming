from collections import defaultdict

N, K = map(int, input().split())
P = list(map(int, input().split()))
L = 60
dp = [[-1] * N for _ in range(L + 1)]
for i in range(N):
    dp[0][i] = P[i] - 1
for i in range(L):
    for v in range(N):
        dp[i + 1][v] = dp[i][dp[i][v]]
seen = [False] * N
g = [-1] * N
groups = defaultdict(dict)
for v in range(N):
    if g[v] == -1:
        tmp = {v}
        seen[v] = True
        g[v] = v
        next = v
        while 1:
            next = P[next] - 1
            if seen[next]:
                break
            tmp.add(next)
            seen[next] = True
            g[next] = v
        groups[v] = tmp
ans = [-1] * N
for i in range(N):
    v = P[i] - 1
    M = len(groups[g[v]])
    move = pow(2, K, M) - 1
    move %= M
    to = v
    for j in range(L):
        if move & (1 << j):
            to = dp[j][to]
    ans[v] = to + 1
res = []
for v in P:
    res.append(ans[v - 1])
print(*res)
