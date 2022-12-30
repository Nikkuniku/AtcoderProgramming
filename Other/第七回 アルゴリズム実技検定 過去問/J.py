from collections import deque
N, M = map(int, input().split())
q = deque([])
indeg = [0]*N
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    indeg[v] += 1
for i, v in enumerate(indeg):
    if v == 0:
        q.append(i)

ans = []
while q:
    v = q.popleft()
    ans.append(v)
    for e in edge[v]:
        indeg[e] -= 1
        if indeg[e] == 0:
            q.append(e)
answer = 'Yes'
if len(ans) == N:
    answer = 'No'
print(answer)
