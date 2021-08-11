from collections import deque
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
vertics = [0]*n
for _ in range(m):
    x, y = map(int, input().split())
    edge[x].append(y)
    vertics[y] += 1
q = deque()
ans = []
for i in range(n):
    if vertics[i] == 0:
        q.append((i, 0))
        ans.append((i, 0))

while q:
    v = q.popleft()
    w = v[0]
    d = v[1]
    for e in edge[w]:
        vertics[e] -= 1
        if vertics[e] == 0:
            q.append((e, d+1))
            ans.append((e, d+1))

for j in range(n):
    print(ans[j][0])
