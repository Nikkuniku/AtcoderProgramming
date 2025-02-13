import sys
from collections import defaultdict


def solve():
    N, M = map(int, input().split())
    si, sj = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    d = defaultdict(list)
    for i in range(N):
        for j in range(N):
            d[A[i][j]].append((i, j))

    def search(s, ni, nj):
        res = []
        for x, y in d[s]:
            tmp = abs(ni - x) + abs(nj - y) + 1
            res.append((tmp, x, y))
        res.sort()
        return res[0][1], res[0][2]

    ans = []
    d_s = defaultdict(set)
    idx_s = defaultdict(int)
    input_strings = []
    idx_set = set([i for i in range(M)])
    for i in range(M):
        t = input()
        d_s[t[0]].add(t)
        idx_s[t] = i
        input_strings.append(t)
    now = ""
    i = 0
    while len(idx_set) > 0:
        T = input_strings[i]
        for s in T:
            x, y = search(s, si, sj)
            ans.append((x, y))
            now = s
        d_s[T[0]].discard(T)
        idx_set.discard(idx_s[T])
        if len(idx_set) == 0:
            break
        if d_s[now]:
            i = idx_s[min(d_s[now])]
        else:
            i = min(idx_set)

    for c in ans:
        print(*c)


solve()
