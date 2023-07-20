from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)
K = int(input())
Condition = [list(map(int, input().split())) for _ in range(K)]


def BFS(s):
    q = deque([s])
    dist = [-1]*N
    dist[s] = 0
    while q:
        v = q.popleft()
        for e in Edge[v]:
            if dist[e] != -1:
                continue
            dist[e] = dist[v]+1
            q.append(e)

    return dist


ans = [0]*N
for s in range(N):
    distance = BFS(s)
    isBlack = True
    for p, d in Condition:
        if distance[p-1] < d:
            isBlack = False
    if isBlack:
        ans[s] = 1
for p, d in Condition:
    distance = BFS(p-1)
    isExist = False
    for s in range(N):
        if ans[s]:
            if distance[s] == d:
                isExist = True
    if not isExist:
        print('No')
        exit()
if 1 not in ans:
    print('No')
    exit()
res = ''.join([str(a) for a in ans])
print('Yes')
print(res)
