N, M = map(int, input().split())
from collections import defaultdict, deque

d = defaultdict(list)
q = deque()
B = [[] for _ in range(M)]
C = [0] * (N + 1)
for i in range(M):
    k = int(input())
    A = list(map(int, input().split()))
    for a in A:
        d[a].append(i)
        B[i].append(a)
    C[B[i][-1]] += 1
    if C[B[i][-1]] == 2:
        q.append(B[i][-1])

while q:
    v = q.popleft()
    for e in d[v]:
        B[e].pop()
        if B[e]:
            C[B[e][-1]] += 1
            if C[B[e][-1]] == 2:
                q.append(B[e][-1])
ans = "Yes"
for i in range(M):
    if B[i]:
        ans = "No"
print(ans)
