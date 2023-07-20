# import pypyjit
from sys import setrecursionlimit
setrecursionlimit(10**9)
# pypyjit.set_param('max_unroll_recursion=-1')
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
INF = 10**6
ans = [1]
cnt = [0]*N
cnt[0] = 1
seen = [False]*N


def rec(v, d, c=1):
    seen[v] = True
    if v == d:
        if ans[0] > INF:
            print(INF)
            exit()
    else:
        for e in Edge[v]:
            if not seen[e]:
                rec(e, d, c)
                cnt[e] += cnt[v]
                ans[0] += cnt[v]
    seen[v] = False


for v in range(1, N):
    rec(0, v)
print(min(ans[0], INF))
print(cnt)
