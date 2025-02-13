from itertools import accumulate
from bisect import bisect_right


def f(N, P: list) -> int:
    P_inv = [N + 1 - p for p in P]
    cum_P_inv = list(accumulate(P_inv, initial=0))
    res = 0
    for i, p in enumerate(P):
        if i == len(P) - 1:
            continue
        idx = max(bisect_right(P, N + 1 - p), i + 1)
        res += p * (idx - i - 1)
        res += cum_P_inv[-1] - cum_P_inv[idx]
    return res


N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(1, N + 1):
    ans += (N + 1 - i) * (i // 2)
P = [[] for _ in range(max(A) + 1)]
for i, v in enumerate(A):
    P[v].append(i + 1)
for v in range(max(A) + 1):
    ans -= f(N, P[v])
print(ans)
