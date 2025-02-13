from collections import deque

N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

q = deque([0])
dist1 = [-1] * N
dist1[0] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist1[e] != -1:
            continue
        dist1[e] = dist1[v] + 1
        q.append(e)
w = dist1.index(max(dist1))
q = deque([w])
dist2 = [-1] * N
dist2[w] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist2[e] != -1:
            continue
        dist2[e] = dist2[v] + 1
        q.append(e)
x = dist2.index(max(dist2))
print(w + 1, x + 1)
