from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

M = int(input())
G = list(map(int, input().split()))
H = list(map(int, input().split()))
G1 = G[: len(G) // 2]
G2 = G[len(G) // 2 :]
H1 = H[: len(H) // 2]
H2 = H[len(H) // 2 :]
H1_Select = [defaultdict(int) for _ in range(15)]
H2_Select = [[] for _ in range(15)]
for i in range(15):
    C = list(combinations(range(14), i))
    for c in C:
        tmp = 0
        tmp_2 = 0
        c_set = set(c)
        for j in range(14):
            if j in c_set:
                tmp += G1[j]
                tmp_2 += G2[j]
            else:
                tmp += H1[j]
                tmp_2 += H2[j]
            tmp %= M
            tmp_2 %= M
        H1_Select[i][tmp] += 1
        H2_Select[i].append(tmp_2)
    H2_Select[i].sort()
Q = int(input())
ans = []
for _ in range(Q):
    K, X = map(int, input().split())
    s = max(0, K - 14)
    res = 0
    for i in range(s, min(K, 14) + 1):
        A = H1_Select[i]
        B = H2_Select[K - i]
        for x, y in A.items():
            if x < X:
                cnt = bisect_left(B, M - x) - bisect_left(B, X - x)
            else:
                cnt = bisect_left(B, M - x) + len(B) - bisect_left(B, M + X - x)
            res += cnt * y
    ans.append(res)
print(*ans, sep="\n")
