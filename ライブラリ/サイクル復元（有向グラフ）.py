from sys import setrecursionlimit

setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
seen = [False] * N
finished = [False] * N
history = []


# サイクル検出
def dfs(v, p=-1):
    seen[v] = True
    history.append(v)
    for e in Edge[v]:
        if e == p or finished[e]:
            continue
        if seen[e] and not finished[e]:
            history.append(e)
            return e
        pos = dfs(e, v)
        if pos != -1:
            return pos
    finished[v] = True
    history.pop()
    return -1


ans = "No"
cycle = []
for v in range(N):
    if seen[v]:
        continue
    pos = dfs(v)
    if pos != -1:
        history.pop()
        while history:
            w = history.pop()
            cycle.append(w)
            if w == pos:
                break
        break
if pos != -1:
    print("Yes")
    print(*cycle)
else:
    print("No")
