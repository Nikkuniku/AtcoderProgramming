from sys import setrecursionlimit
setrecursionlimit(10**8)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
N = int(input())
Edge = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
ans = [0]*N


def rec(v, d=0, p=-1):
    ans[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        rec(e, d+1, v)


rec(0)
print(max(ans))
