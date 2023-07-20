from sys import setrecursionlimit
from collections import deque
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
setrecursionlimit(10**6)
N, U, V = map(int, input().split())
U, V = U-1, V-1
edge = [[] for _ in range(N)]
leaves = []
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edge[a].append(b)
    edge[b].append(a)

depth = [0]*N
ans = [0]*N
q = deque([U])
dist = [-1]*N
dist[U] = 0
while q:
    v = q.popleft()
    for e in edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v]+1
        q.append(e)


def dfs(v, p=-1, d=0):
    depth[v] = d
    for e in edge[v]:
        if e == p:
            continue
        dfs(e, v, d+1)

    cnt = 0
    for e in edge[v]:
        if e == p:
            continue
        cnt += 1
    if cnt == 0:
        leaves.append((v, d))


def up(v, val, p):
    if v == V:
        ans[v] = 0
    else:
        if ans[v] < val:
            ans[v] = max(ans[v], val)
        else:
            return
    for e in edge[v]:
        if e == p:
            continue
        if depth[e] > depth[v]:
            continue
        up(e, val, v)


dfs(V)
leaves.sort(key=lambda x: x[1], reverse=True)
for v, d in leaves:
    up(v, depth[v]-1, -1)


res = 0
for i in range(N):
    if depth[i] > dist[i]:
        res = max(res, ans[i])
print(res)
