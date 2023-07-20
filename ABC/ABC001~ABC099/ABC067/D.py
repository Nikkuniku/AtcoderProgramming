from collections import deque
N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
q = deque([(0, 0), (N-1, 1)])
color = [-1]*N
color[0] = 0
color[N-1] = 1
while q:
    v, c = q.popleft()
    for e in Edge[v]:
        if color[e] != -1:
            continue
        color[e] = c
        q.append((e, c))
ans = 'Fennec'
if color.count(0) <= color.count(1):
    ans = 'Snuke'
print(ans)
