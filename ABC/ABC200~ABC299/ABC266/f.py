from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
seen = [False] * N
finished = [False] * N
history = []


def dfs(v, p=-1):
    seen[v] = True
    history.append(v)
    for to in Edge[v]:
        if to == p:
            continue
        if finished[to]:
            continue
        if seen[to] and not finished[to]:
            history.append(to)
            return to
        pos = dfs(to, v)
        if pos != -1:
            return pos
    finished[v] = True
    history.pop()
    return -1


def construct(pos, history):
    res = []
    history.pop()
    while history:
        v = history[-1]
        res.append(v)
        history.pop()
        if v == pos:
            break
    res = res[::-1]
    return res


Root = [-1] * N


def dfs2(v, p, u=-1):
    Root[v] = u
    for to in Edge[v]:
        if to == p or to == u:
            continue
        dfs2(to, v, u)
    return


pos = dfs(0)
Cycle = set(construct(pos, history))
for s in Cycle:
    for c in Edge[s]:
        if c in Cycle:
            continue
        Root[c] = s
        p = s
        dfs2(c, p, s)
Q = int(input())
ans = []
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if Root[u] == -1:
        if Root[v] == u:
            ans.append("Yes")
        else:
            ans.append("No")
    elif Root[v] == -1:
        if Root[u] == v:
            ans.append("Yes")
        else:
            ans.append("No")
    else:
        if Root[u] == Root[v]:
            ans.append("Yes")
        else:
            ans.append("No")
print(*ans, sep="\n")
