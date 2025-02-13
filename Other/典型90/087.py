def f(k, B, P):
    cost = [[-1] * (len(B[0])) for _ in range((len(B[0])))]
    for i in range(len(cost)):
        for j in range(len(cost[i])):
            if B[i][j] == -1:
                cost[i][j] = k
            else:
                cost[i][j] = B[i][j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] != INF and cost[k][j] != INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    res = 0
    for i in range(len(cost)):
        for j in range(len(cost[i])):
            if i == j:
                continue
            if cost[i][j] <= P:
                res += 1
    res //= 2
    return res


N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
INF = 1 << 60
l0, r0 = 0, INF
while r0 - l0 > 1:
    mid = (l0 + r0) // 2
    if f(mid, A, P) <= K:
        r0 = mid
    else:
        l0 = mid
l1, r1 = 0, INF
while r1 - l1 > 1:
    mid = (l1 + r1) // 2
    if f(mid, A, P) < K:
        r1 = mid
    else:
        l1 = mid
ans = l1 - r0 + 1
if ans > 10**10:
    ans = "Infinity"
print(ans)
