from heapq import heapify, heappop, heappush
from collections import defaultdict, deque

N, M = map(int, input().split())
Edge = [set() for _ in range(N)]
A = list(map(int, input().split()))
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if A[u] < A[v]:
        Edge[u].add((1, v))
    if A[v] < A[u]:
        Edge[v].add((1, u))
    if A[u] == A[v]:
        Edge[u].add((0, v))
        Edge[v].add((0, u))

dp = [-1] * N
q = deque([0])
dp[0] = 1
while q:
    v = q.popleft()
    for c, e in Edge[v]:
        t = dp[v] + c
        if c == 1 and dp[e] == -1:
            dp[e] = t
            q.appendleft(e)
        elif c == 0 and dp[e] == -1:
            dp[e] = t
            q.append(e)
ans = dp[-1]
if dp[-1] == -1:
    ans = 0
print(ans)
