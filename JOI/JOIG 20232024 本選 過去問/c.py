def segfunc_max(x, y):
    return max(x, y)


def segfunc_min(x, y):
    return min(x, y)


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


from sys import stdin

N = int(input())
player = [list(map(int, stdin.readline().split())) + [i] for i in range(N)]
from collections import defaultdict

zatsu = set()
for c, _, _ in player:
    zatsu.add(c)
zatsu = sorted(zatsu)
countrymap = defaultdict(lambda: -1)
for i, v in enumerate(zatsu):
    countrymap[v] = i
C = len(zatsu)
INF = 10**10
dp = SegTree([-1] * (C + 1), segfunc_max, -1)
ep = SegTree([INF] * (C + 1), segfunc_min, INF)
player.sort(key=lambda x: x[0])
player.sort(key=lambda x: x[1])
ans = [INF] * N
for c, x, i in player:
    country = countrymap[c]
    tmp_max1 = dp.query(0, country)
    tmp_max2 = dp.query(country + 1, C)
    tmp_max = max(tmp_max1, tmp_max2)
    if tmp_max != -1:
        ans[i] = x - tmp_max
    dp.update(country, x)
for j in range(N - 1, -1, -1):
    c, x, i = player[j]
    country = countrymap[c]
    tmp_min1 = ep.query(0, country)
    tmp_min2 = ep.query(country + 1, C)
    tmp_min = min(tmp_min1, tmp_min2)
    if tmp_min != INF:
        if ans[i] > abs(x - tmp_min):
            ans[i] = abs(x - tmp_min)
    ep.update(country, x)
print(*ans, sep="\n")
