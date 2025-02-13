N, M, D = map(int, input().split())
A = list(map(int, input().split()))
to = [i for i in range(N)]
res = [i for i in range(N)]
for a in A:
    a -= 1
    b1, b2 = to[a], to[a + 1]
    res[b1], res[b2] = res[b2], res[b1]
    to[res[b1]], to[res[b2]] = b1, b2
L = 61
dp = [[-1] * N for _ in range(L + 1)]
for v in range(N):
    dp[0][v] = res[v]
for i in range(L):
    for v in range(N):
        dp[i + 1][v] = dp[i][dp[i][v]]
ans = [-1] * N
for v in range(N):
    to = v
    for j in range(L):
        if D & (1 << j):
            to = dp[j][to]
    ans[v] = to + 1
print(*ans, sep="\n")
