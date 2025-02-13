N, Q = map(int, input().split())
X = list(map(int, input().split()))
P = [[] for _ in range(N + 1)]
S = set()
V = []
from itertools import accumulate

for i, v in enumerate(X):
    P[v].append(i)
    if v in S:
        S.discard(v)
    else:
        S.add(v)
    V.append(len(S))
cum = list(accumulate(V, initial=0))
A = [0] * N
for i in range(N + 1):
    if len(P[i]) % 2 == 1:
        P[i].append(Q)
for i in range(1, N + 1):
    B = P[i]
    for j in range(len(B)):
        if j % 2 != 0:
            continue
        L = B[j]
        R = B[j + 1]
        A[i - 1] += cum[R] - cum[L]
print(*A)
