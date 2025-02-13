from itertools import pairwise
from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
C = []
for x, y in pairwise(A):
    C.append((y - x) ** 2)
q = deque()
ans = float("inf")
tmp = 0
for i in range(len(C)):
    q.append(C[i])
    tmp += C[i]
    if len(q) == M - 1:
        ans = min(ans, tmp)
        tmp -= q.popleft()
if M == 1:
    ans = 0
print(ans)
