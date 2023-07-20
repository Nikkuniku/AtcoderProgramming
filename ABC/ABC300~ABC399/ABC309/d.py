from collections import deque
N1, N2, M = map(int, input().split())
Edge = [[] for _ in range(N1+N2)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
q1 = deque([0])
q2 = deque([N1+N2-1])
dist1 = [-1]*(N1+N2)
dist2 = [-1]*(N1+N2)
dist1[0] = 0
dist2[N1+N2-1] = 0
while q1:
    v = q1.popleft()
    for e in Edge[v]:
        if dist1[e] == -1:
            dist1[e] = dist1[v]+1
            q1.append(e)
while q2:
    v = q2.popleft()
    for e in Edge[v]:
        if dist2[e] == -1:
            dist2[e] = dist2[v]+1
            q2.append(e)
ans = max(dist1)+max(dist2)+1
print(ans)
