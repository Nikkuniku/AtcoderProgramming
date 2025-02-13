from sortedcontainers import SortedList
from collections import defaultdict, deque


def LIS(input_array: list) -> int:
    """
    配列のLISの長さを返す。

    Parameters
    ----------
    input_array:list
    """
    from bisect import bisect_right, bisect_left

    INF = 1 << 62
    dp = [INF] * len(input_array)
    for c in input_array:
        dp[bisect_right(dp, c)] = c
    ans = bisect_left(dp, INF)
    # return (ans, dp[:ans])
    return ans


N, M = map(int, input().split())
A = []
S = SortedList()
d = defaultdict(deque)
A = [list(map(int, input().split())) for _ in range(N)]
C = sorted([int(input()) for _ in range(M)])
for i, c in enumerate(C):
    S.add(c)
    d[c].append(i)
V_c = [-1] * M
A.sort(key=lambda x: x[0])
A.sort(key=lambda x: x[1])
for s, v in A:
    idx = S.bisect_left(s)
    if idx == len(S):
        continue
    p = S[idx]
    j = d[p].popleft()
    V_c[j] = v
    S.discard(p)
D = []
for v in V_c:
    if v != -1:
        D.append(v)
K = LIS(D)
print(K)
