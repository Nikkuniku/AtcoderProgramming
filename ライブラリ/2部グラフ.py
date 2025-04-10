from sys import stdin
from collections import deque

n = int(input())
edge = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, stdin.readline().split())
    a, b = a - 1, b - 1
    edge[a].append(b)
    edge[b].append(a)
colors = [-1] * n
colors[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    for e in edge[v]:
        if colors[e] == -1:
            colors[e] = 1 - colors[v]
            q.append(e)

ans = []
cnt = 0
for i in range(n):
    if colors[i] == 0:
        ans.append(i + 1)
        cnt += 1

    if cnt == n // 2:
        break

print(*ans)
print(*colors)
