from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
edge = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, i))
    edge[v].append((u, i))
C = [0] * (N - 1)


def BFS(N, s, g):
    dist = [-1] * N
    q = deque([s])
    dist[s] = 0
    prev = [-1] * N
    prev_edge = [-1] * N
    while q:
        v = q.popleft()
        for e, i in edge[v]:
            if dist[e] == -1:
                dist[e] = dist[v] + 1
                prev[e] = v
                prev_edge[e] = i
                q.append(e)
    while g != s:
        j = prev_edge[g]
        C[j] += 1
        g = prev[g]
    return


for i in range(M - 1):
    v = A[i] - 1
    w = A[i + 1] - 1
    BFS(N, v, w)
S = sum(C)
dp = [1] + [0] * S
MOD = 998244353
for i in range(N - 1):
    for j in range(S, C[i] - 1, -1):
        dp[j] += dp[j - C[i]]
        dp[j] %= MOD
ans = 0
for r in range(S + 1):
    b = S - r
    if r - b == K:
        ans += dp[r]
        ans %= MOD
print(ans)
