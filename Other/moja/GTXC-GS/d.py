K = int(input())
U = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for j, v in enumerate(A):
    Edge[v - 1].append(j + 1)
    Edge[j + 1].append(v - 1)
from collections import deque

ans = []
for u in U:
    q = deque([0])
    dist = [-1] * N
    dist[0] = 0
    while q:
        v = q.popleft()
        for e in Edge[v]:
            if dist[e] == -1 and u <= C[e]:
                dist[e] = dist[v] + 1
                q.append(e)
    ans.append(max(dist))
print(*ans, sep="\n")
