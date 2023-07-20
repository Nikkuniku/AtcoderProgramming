N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    Edge[u].append((v, w))
ans = []
for v in range(N):
    Edge[v].sort(key=lambda x: x[0])
    Edge[v].sort(key=lambda x: x[1])
    if Edge[v]:
        ans.append(Edge[v][0][0])
    else:
        ans.append(-1)
print(*ans, sep="\n")
