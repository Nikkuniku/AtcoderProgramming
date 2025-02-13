from sys import setrecursionlimit

setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i, v in enumerate(P):
    Edge[v - 1].append(i + 1)
depth = [0] * N


def dfs(v, d=0, p=-1):
    depth[v] = d
    for e in Edge[v]:
        if e == p:
            continue
        dfs(e, d + 1, v)


dfs(0)
s = [[] for _ in range(N)]
for i, v in enumerate(depth):
    s[v].append(i)
for j in range(N - 1, -1, -1):
    if s[j]:
        tmp = sum([A[k] for k in s[j]])
        if tmp == 0:
            continue
        if tmp > 0:
            exit(print("+"))
        elif tmp < 0:
            exit(print("-"))
if A[0] == 0:
    print(0)
elif A[0] > 0:
    print("+")
elif A[i] < 0:
    print("-")
