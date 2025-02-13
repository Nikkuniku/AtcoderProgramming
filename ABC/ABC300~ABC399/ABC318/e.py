from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
P = [[] for _ in range(N + 1)]
for i, v in enumerate(A):
    P[v].append(i)
Q = [[] for _ in range(N + 1)]
for v in range(N + 1):
    for i in range(len(P[v])):
        Q[v].append(P[v][i] - len(Q[v]))
CUM = [list(accumulate(Q[v])) for v in range(N + 1)]
ans = 0
for v in range(N + 1):
    if not CUM[v]:
        continue
    for i in range(len(CUM[v])):
        ans += (CUM[v][-1] - CUM[v][i]) - (len(CUM[v]) - i - 1) * Q[v][i]
print(ans)
