# import pypyjit
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
# pypyjit.set_param('max_unroll_recursion=-1')
n = int(input())
c = list(map(int, input().split()))
edge = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].add(b)
    edge[b].add(a)
for i in range(n):
    edge[i] = list(edge[i])

ans = [False]*n


def dfs(s, p, color):
    for e in edge[s]:
        if e == p:
            continue
        color[c[s]] += 1
        dfs(e, s, color)
        color[c[s]] -= 1

    if color[c[s]] == 0:
        ans[s] = True


dfs(0, -1, defaultdict(int))
answer = []
for i in range(n):
    if ans[i]:
        answer.append(i+1)
print(*answer, sep="\n")
