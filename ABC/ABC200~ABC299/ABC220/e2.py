def graph(N):
    INF = 1 << 60
    M = (1 << N) - 1
    cost = [[INF] * M for _ in range(M)]
    for i in range(M):
        cost[i][i] = 0
    for i in range(1, (M // 2) + 1):
        a = i - 1
        b = (2 * i) - 1
        c = 2 * i
        cost[a][b] = 1
        cost[a][c] = 1
        cost[b][a] = 1
        cost[c][a] = 1
    for k in range(M):
        for i in range(M):
            for j in range(M):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost


def check(A, D):
    res = 0
    N = len(A)
    for i in range(N):
        for j in range(N):
            res += A[i][j] == D
    return res


from itertools import accumulate

N, D = map(int, input().split())
MOD = 998244353
pow1 = [pow(2, D - i, MOD) for i in range(D + 1)]
power = list(accumulate(pow1))
ans = 0
for d in range(N):
    k = max((D - N + 1 + d + 1) // 2, 0)
    cnt = pow(2, d, MOD)
    p = max(d - D + 1, 0)
    diff = d - p
    if k == 0:
        ans += pow(2, D, MOD) * cnt
        ans %= MOD
        k += 1
    if d - D >= 0:
        ans += cnt
        ans %= MOD
    if diff >= k:
        ans += (power[diff] - power[k - 1]) * pow(2, -1, MOD) * cnt
        ans %= MOD

print(ans)
# print(check(graph(N), D))
