from sortedcontainers import SortedSet
from collections import defaultdict


def solve(N, K, A):
    M = 0
    ans = []
    idx = defaultdict(int)
    s = SortedSet()
    for i, v in enumerate(A):
        idx[v] = i
        s.add(v)

    for i in range(N):
        now = A[i]
        # (1) 今見ている値より小さい
        tmp = 0
        cnt_lt = s.index(now)
        tmp += cnt_lt
        if K <= M + tmp:
            p = s[K - M - 1]
            for m in range(idx[p], i - 1, -1):
                ans.append(A[m])
            for m in range(idx[p] + 1, N):
                ans.append(A[m])
            break
        # (2)先頭をnowで固定
        tmp += (i + 1) + (N - i - 1) * (N - i) // 2
        if K <= M + tmp:
            M += cnt_lt
            ans.append(now)
            s.discard(now)
            continue
        # (3)今見ている値より大きい
        cnt_gt = len(s) - cnt_lt - 1
        if K <= M + tmp + cnt_gt:
            p = s[K - (M + tmp) - 1 + s.bisect_right(now)]
            for m in range(idx[p], i - 1, -1):
                ans.append(A[m])
            for m in range(idx[p] + 1, N):
                ans.append(A[m])
            break
    return ans


N, K = map(int, input().split())
A = list(map(int, input().split()))
print(*solve(N, K, A))
