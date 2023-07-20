from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10**7)
N, M = map(int, input().split())
P = [0]+list(map(int, input().split()))
Edge = [[] for _ in range(N)]
Move = [-1]*N
for i in range(1, N):
    u = P[i]-1
    Edge[u].append(i)
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    Move[x] = max(Move[x], y)
q = deque([(0, Move[0])])
OK = [False]*N
# while q:
#     v, d = q.popleft()
#     d = max(d, Move[v])
#     if d > 0:
#         OK[v] = True
#     for e in Edge[v]:
#         if d > 0:
#             OK[e] = True
#             q.append((e, d-1))


def dfs(v, p=-1, d=Move[0]):
    d = max(d, Move[v])
    if d >= 0:
        OK[v] = True
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v, d-1)


dfs(0)

ans = OK.count(True)
print(ans)
