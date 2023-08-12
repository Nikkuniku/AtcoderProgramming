from sys import setrecursionlimit
setrecursionlimit(10**8)
N = int(input())
A = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for i in range(N):
    Edge[i].append(A[i]-1)

for i in range(N):
    e = Edge[i][0]
    v = Edge[e][0]
    if i == v:
        print(2)
        print(*[v+1, e+1])
        exit()
ans = []
seen = [False]*N
finished = [False]*N
history = []


def dfs(v, p=-1):
    seen[v] = True
    history.append(v)
    for e in Edge[v]:
        if e == p:
            continue
        if finished[e]:
            continue
        if seen[e] and not finished[e]:
            history.append(e)
            return e
        pos = dfs(e, v)
        if pos != -1:
            return pos
    finished[v] = True
    history.pop()
    return -1


for v in range(N):
    if seen[v]:
        continue
    pos = dfs(v)
    ans = []
    history.pop()
    while history:
        v = history[-1]
        ans.append(v+1)
        history.pop()
        if v == pos:
            break
    print(len(ans))
    print(*ans[::-1])
    exit()
