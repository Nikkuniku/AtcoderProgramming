from heapq import heappop, heappush

N, M, X = map(int, input().split())
T = [int(input()) for _ in range(N)]
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, d))
    Edge[b].append((a, d))
INF = 1 << 60
dp = [[INF] * (2 * X + 2) for _ in range(N)]
ep = [INF] * N
ep[0] = 0
q = [(ep[0], 0, -1)]
while q:
    d, v, t = heappop(q)
    if T[v] != 1 and d > ep[v]:
        continue
    if T[v] == 1 and d > dp[v][t]:
        continue
    # 寒いところ
    if T[v] == 0:
        for to, c in Edge[v]:
            if T[to] == 1:
                if dp[to][min(c, X)] > d + c:
                    dp[to][min(c, X)] = d + c
                    heappush(q, (dp[to][min(c, X)], to, min(c, X)))
            elif T[to] == 0:
                if ep[to] > d + c:
                    ep[to] = d + c
                    heappush(q, (ep[to], to, -1))
            elif T[to] == 2:
                if c < X:
                    continue
                if ep[to] > d + c:
                    ep[to] = d + c
                    heappush(q, (ep[to], to, -1))
    # 熱いところ
    elif T[v] == 2:
        for to, c in Edge[v]:
            if T[to] == 0:
                if c < X:
                    continue
                if ep[to] > d + c:
                    ep[to] = d + c
                    heappush(q, (ep[to], to, -1))
            elif T[to] == 2:
                if ep[to] > d + c:
                    ep[to] = d + c
                    heappush(q, (ep[to], to, -1))
            elif T[to] == 1:
                if dp[to][min(X + 1 + c, 2 * X + 1)] > d + c:
                    dp[to][min(X + 1 + c, 2 * X + 1)] = d + c
                    heappush(
                        q,
                        (
                            dp[to][min(X + 1 + c, 2 * X + 1)],
                            to,
                            min(X + 1 + c, 2 * X + 1),
                        ),
                    )
    # 快適
    elif T[v] == 1:
        for to, c in Edge[v]:
            if T[to] == 2:
                if t + c >= X or X + 1 <= t:
                    if ep[to] > d + c:
                        ep[to] = d + c
                        heappush(q, (ep[to], to, -1))
            elif T[to] == 0:
                if t - (X + 1) + c >= X or t <= X:
                    if ep[to] > d + c:
                        ep[to] = d + c
                        heappush(q, (ep[to], to, -1))
            elif T[to] == 1:
                if 0 <= t <= X:
                    if dp[to][min(t + c, X)] > d + c:
                        dp[to][min(t + c, X)] = d + c
                        heappush(q, (dp[to][min(t + c, X)], to, min(t + c, X)))
                elif X + 1 <= t:
                    if dp[to][min(t + c, 2 * X + 1)] > d + c:
                        dp[to][min(t + c, 2 * X + 1)] = d + c
                        heappush(
                            q,
                            (dp[to][min(t + c, 2 * X + 1)], to, min(t + c, 2 * X + 1)),
                        )
if T[N - 1] != 1:
    ans = ep[N - 1]
else:
    ans = min(dp[N - 1])
print(ans)
