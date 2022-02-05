n, m = map(int, input().split())
seen = [-1]*n
edge = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    s, t = s-1, t-1
    edge[s].append(t)
    edge[t].append(s)


def dfs(x):
    if seen[x] == -1:
        seen[x] = 1
    else:
        return
    for v in edge[x]:
        dfs(v)


dfs(0)

print(seen)
