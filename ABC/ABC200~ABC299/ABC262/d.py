from collections import defaultdict
from collections import Counter
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(input())
a = list(map(int, input().split()))
ans = 0
MOD = 998244353
for m in range(1, n+1):
    d = defaultdict(int)
    s = set([tuple([i]*m) for i in range(m+1)])
    for i in range(n):
        d[a[i] % m] += 1

    for k in range(1, m):
        t = []
        tmp = 0
        for j in range(m-1):
            t.append(k)
            tmp += k
            if m-tmp > 0:
                t.append(m-tmp)
            t.sort()
            s.add(tuple(t))
            t.pop()
    for c in s:
        C = Counter(c)
        re = 1
        tmp = m
        for k, v in C.items():
            tmp -= v
            if d[k] < v:
                re = 0
                break
            re *= cmb(d[k], v)
        if d[0] > tmp > 0:
            re *= cmb(d[0], tmp)
        ans += re
        ans %= MOD

print(ans % MOD)
