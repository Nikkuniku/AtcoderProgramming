from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
Edge = [[] for _ in range(N)]
deg = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
    deg[a] += 1
    deg[b] += 1

ans = -1


def dfs(v, p=-1):
    global ans
    res = 1
    children = []
    for u in Edge[v]:
        if u == p:
            continue
        children.append(dfs(u, v))
    children.sort(reverse=True)
    if len(children) >= 3:
        res = children[0] + children[1] + children[2] + 1
        if len(children) >= 4:
            ans = max(ans, res + children[3])
    elif len(children) > 0:
        if res + children[0] >= 5:
            ans = max(ans, children[0] + res)
    return res


dfs(0)
print(ans)
