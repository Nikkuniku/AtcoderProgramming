from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = [[] for _ in range(N + 1)]
ans = [-1] * Q
for i in range(Q):
    R, X = map(int, input().split())
    Query[R].append((i, X))
INF = 1 << 60
dp = [INF] * (N + 1)
for i in range(N):
    idx = bisect_left(dp, A[i])
    dp[idx] = A[i]
    for j, x in Query[i + 1]:
        k = bisect_left(dp, x)
        if dp[k] == x:
            ans[j] = k + 1
        else:
            ans[j] = k
print(*ans, sep="\n")
