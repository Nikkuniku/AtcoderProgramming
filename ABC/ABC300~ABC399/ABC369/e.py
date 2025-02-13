from itertools import permutations

N, M = map(int, input().split())
INF = 1 << 60
cost = [[INF] * N for _ in range(N)]
edge = []
for _ in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    cost[u][v] = min(cost[u][v], t)
    cost[v][u] = min(cost[v][u], t)
    edge.append((u, v, t))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != INF and cost[k][j] != INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


def solve(k, b, Edge):
    P = list(permutations(b))
    ans = 1 << 60
    for p in P:
        for i in range(1 << k):
            s = 0
            tmp = []
            for j in range(k):
                if i & (1 << j):
                    tmp.append(1)
                else:
                    tmp.append(0)
            res = 0
            for j in range(k):
                u, v, t = Edge[p[j]]
                if tmp[j] == 1:
                    u, v = v, u
                if s != u:
                    res += cost[s][u]
                res += t
                s = v
            if s != N - 1:
                res += cost[s][N - 1]
            ans = min(ans, res)
    return ans


Q = int(input())
for _ in range(Q):
    K = int(input())
    B = list(map(lambda x: int(x) - 1, input().split()))
    print(solve(K, B, edge))
