from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
P = list(map(int, input().split()))
Edge = [set() for _ in range(N)]
Depth = [0] * N
for a, b in enumerate(P, 1):
    b -= 1
    Edge[a].add(b)
    Edge[b].add(a)
ET = []


def dfs(v, p=-1, d=0):
    Depth[v] = d
    ET.append(v)
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, v, d + 1)
    ET.append(v)


dfs(0)
seen = set()
depth_indexes = [[] for _ in range(N)]
Time_In = [1 << 60] * N
Time_Out = [0] * N
for i, v in enumerate(ET):
    Time_In[v] = min(Time_In[v], i)
    Time_Out[v] = max(Time_In[v], i)
    if v in seen:
        continue
    depth_indexes[Depth[v]].append(i)
    seen.add(v)
Q = int(input())
from bisect import bisect_left

ans = []
for _ in range(Q):
    U, D = map(int, input().split())
    U -= 1
    a = Time_In[U]
    b = Time_Out[U]
    cnt = bisect_left(depth_indexes[D], b) - bisect_left(depth_indexes[D], a)
    ans.append(cnt)
print(*ans, sep="\n")
