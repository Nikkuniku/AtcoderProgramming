from collections import deque
N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
indeg = [0]*N
for _ in range(M):
    f, s = map(int, input().split())
    Edge[f].append(s)
    indeg[s] += 1

q = deque()
for i, v in enumerate(indeg):
    if v == 0:
        q.append(i)

while q:
    v = q.popleft()
    for e in Edge[v]:
        indeg[e] -= 1
        if indeg[e] == 0:
            q.append(e)
ans = 'Yes'
if sum(indeg) > 0:
    ans = 'No'
print(ans)
