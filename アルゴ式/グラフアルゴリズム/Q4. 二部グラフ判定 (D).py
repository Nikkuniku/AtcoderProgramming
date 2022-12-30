from sys import setrecursionlimit
setrecursionlimit(10**8)
N, M = map(int, input().split())
input_Edges = []
Edge = [[]for _ in range(N)]
color = [-1]*N
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
    input_Edges.append((a, b))


def dfs(v, c=0, p=-1):
    color[v] = c
    for e in Edge[v]:
        if e == p:
            continue
        if color[e] != -1:
            continue
        dfs(e, 1-c, v)


for i in range(N):
    if color[i] == -1:
        dfs(i)
ans = 'Yes'
for u, v in input_Edges:
    if color[u] == color[v]:
        ans = 'No'
print(ans)
