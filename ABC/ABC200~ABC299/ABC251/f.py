from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**8)
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
isseen = [False] * N
isfinished = [False] * N
T1 = []
T2 = []


def dfs(v, p=-1):
    isseen[v] = True
    for to in Edge[v]:
        if to == p:
            continue
        if isseen[to]:
            continue
        if isfinished[to]:
            continue
        T1.append((v + 1, to + 1))
        dfs(to, v)
    isfinished[v] = True
    return False


def bfs(v):
    q = deque([v])
    isseen = [False] * N
    isseen[v] = True
    while q:
        v = q.popleft()
        for to in Edge[v]:
            if isseen[to]:
                continue
            T2.append((v + 1, to + 1))
            isseen[to] = True
            q.append(to)
    return True


dfs(0)
bfs(0)
for u, v in T1:
    print(u, v)
for u, v in T2:
    print(u, v)
