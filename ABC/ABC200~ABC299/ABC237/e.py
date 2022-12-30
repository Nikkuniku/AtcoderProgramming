import heapq
n, m = map(int, input().split())
h = list(map(int, input().split()))
edge = [[] for _ in range(n)]
geta = 2 + 2 * 10**8
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if h[u] >= h[v]:
        edge[u].append((geta-(h[u]-h[v]), v))
        edge[v].append((geta+2*(h[u]-h[v]), u))
    else:
        edge[u].append((geta+2*(h[v]-h[u]), v))
        edge[v].append((geta-(h[v]-h[u]), u))
INF = float('inf')
dp = [INF]*n
dp[0] = 0
cnt = [INF]*n
cnt[0] = 0
q = []
heapq.heappush(q, (0, 0))
while q:
    d, v = heapq.heappop(q)

    if dp[v] != d:
        continue

    for cost, to in edge[v]:
        if dp[to] <= d+cost:
            continue
        dp[to] = d+cost
        cnt[to] = min(cnt[v]+1, cnt[to])
        q.append((dp[to], to))

ans = -float('inf')
for i in range(n):
    tmp = -(dp[i]-cnt[i]*geta)
    ans = max(ans, tmp)
print(ans)
