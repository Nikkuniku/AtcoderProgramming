from collections import defaultdict
from random import sample

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
d = defaultdict(int)
randomval = sample(range(10**7), k=len(set(A + B)))
for i, v in enumerate(list(set(A + B))):
    d[v] = randomval[i]
cumA = [0]
cumB = [0]
tmp = 0
tmp2 = 0
for i in range(N):
    tmp += d[A[i]]
    cumA.append(tmp)
    tmp2 += d[B[i]]
    cumB.append(tmp2)
ans = []
for _ in range(Q):
    l, r, L, R = map(int, input().split())
    res = cumA[r] - cumA[l - 1]
    res2 = cumB[R] - cumB[L - 1]
    if res == res2:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")
