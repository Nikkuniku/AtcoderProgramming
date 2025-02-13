from itertools import permutations

N = int(input())
MG = int(input())
Edge_G = [[-1] * N for _ in range(N)]
for _ in range(MG):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge_G[u][v] = Edge_G[v][u] = 1
MH = int(input())
Edge_H = [[-1] * N for _ in range(N)]
for _ in range(MH):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge_H[u][v] = Edge_H[v][u] = 1
cost = [[-1] * N for _ in range(N)]
for i in range(N - 1):
    A = list(map(int, input().split()))
    for j, v in enumerate(A):
        cost[i][i + j + 1] = cost[i + j + 1][i] = v
P = list(permutations(range(N)))


def solve(p, edge_g, edge_h):
    res = 0
    cost_t = [[-1] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            a, b = p[i], p[j]
            cost_t[i][j] = cost_t[j][i] = edge_h[a][b]
    for i in range(N):
        for j in range(i + 1, N):
            a, b = p[i], p[j]
            if cost_t[i][j] != edge_g[i][j]:
                res += cost[a][b]

    return res


ans = 1 << 60
for p in P:
    tmp = solve(p, Edge_G, Edge_H)
    ans = min(ans, tmp)
print(ans)
