N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
C = list(map(int, input().split()))
dp1 = [[0, 0] for _ in range(N)]


def dfs(v, p=-1):
    isleaf = True
    for e in edge[v]:
        if e == p:
            continue
        dfs(e, v)
        isleaf = False
    if not isleaf:
        for e in edge[v]:
            if e == p:
                continue
            dp1[v][0] += sum(dp1[e])
            dp1[v][1] += dp1[e][1]
    dp1[v][1] += C[v]


dfs(0)

print(dp1)
