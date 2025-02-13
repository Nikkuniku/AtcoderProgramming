N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    l, d, k, c, A, B = map(int, input().split())
    A -= 1
    B -= 1
    Edge[B].append((A, l, d, k, c))
INF = 1 << 60
dp = [-1] * N
dp[-1] = INF
from heapq import heappop, heappush, heapify

q = [(-dp[N - 1], N - 1)]
heapify(q)
while q:
    t, v = heappop(q)
    t = -t
    if t < dp[v]:
        continue
    for A, l, d, k, c in Edge[v]:
        if l + c > t:
            continue
        m = min(1 + (t - c - l) // d, k)
        if dp[A] < l + (m - 1) * d:
            dp[A] = l + (m - 1) * d
            heappush(q, (-dp[A], A))
ans = []
for v in dp[: N - 1]:
    if v == -1:
        ans.append("Unreachable")
    else:
        ans.append(v)
print(*ans, sep="\n")
