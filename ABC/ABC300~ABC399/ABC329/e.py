N, M = map(int, input().split())
S = input()
T = input()
if set(list(S)) != set(list(T)):
    exit(print("No"))
if not (S.startswith(T) and S.endswith(T)):
    exit(print("No"))
from collections import deque

q = deque(list(S))
for _ in range(M):
    q.popleft()
    q.pop()

can = [[-1] * M for _ in range(M)]
for i in range(M):
    for j in range(M):
        can[i][j] = "".join([T[i], T[j]])
oks = set()
ngs = set()
for i in range(M):
    if i < M - 1:
        for j in range(M):
            if j == 0 or j == i + 1:
                oks.add(can[i][j])
            else:
                ngs.add(can[i][j])
    else:
        for j in range(M):
            oks.add(can[i][j])
P = "".join(S)
ngs -= oks
ans = "Yes"
for s in ngs:
    if s in P:
        ans = "No"
print(ans)
