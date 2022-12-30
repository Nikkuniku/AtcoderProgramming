from sys import setrecursionlimit
setrecursionlimit(10**8)
N, M, s, t = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    Edge[a].append(b)
seen = [False]*N
prev = [-1]*N


def dfs(v, p=-1):
    seen[v] = True
    prev[v] = p
    for e in Edge[v]:
        if e == p:
            continue
        if seen[e]:
            continue
        dfs(e, v)


dfs(s)
ans = []
now = t
while now != -1:
    ans.append(now)
    now = prev[now]
print(len(ans))
print(*ans[::-1])
